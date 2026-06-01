"""
Email today's briefing to BRIEFING_RECIPIENT via Resend.

Environment variables required:
  RESEND_API_KEY, BRIEFING_RECIPIENT, RESEND_FROM (optional)

Note on delivery: Resend's POST /emails only confirms that the message was
*accepted* into Resend's queue (HTTP 2xx). A bounce, block, or spam rejection
happens asynchronously afterward and would otherwise look like success. After
sending we poll GET /emails/{id} and fail loudly if delivery bounces/fails, so
a silent non-delivery can't slip by unnoticed again.
"""

import base64
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
import markdown as md_lib

ROOT = Path(__file__).resolve().parent.parent

TEST_SENDER = "onboarding@resend.dev"

try:
    from zoneinfo import ZoneInfo
    ET = ZoneInfo("America/New_York")
except ImportError:
    ET = timezone(timedelta(hours=-5))

TODAY = datetime.now(ET).date()


def load_dotenv(path):
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


load_dotenv(ROOT / ".env")


CSS = """
<style>
  body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
         line-height: 1.45; color: #1a1a1a; max-width: 760px; margin: 24px auto;
         padding: 0 16px; font-size: 15px; }
  h1 { font-size: 22px; border-bottom: 2px solid #1a1a1a; padding-bottom: 6px; margin-top: 0; }
  h2 { font-size: 17px; margin-top: 24px; color: #1a3a6e; }
  table { border-collapse: collapse; margin: 8px 0 16px; font-size: 14px; }
  th, td { border: 1px solid #ddd; padding: 4px 10px; text-align: right; }
  th:first-child, td:first-child { text-align: left; }
  thead th, tr:first-child th { background: #f4f4f4; }
  ul { padding-left: 22px; }
  li { margin: 4px 0; }
  em { color: #666; }
  hr { border: none; border-top: 1px solid #ddd; margin: 24px 0; }
  code { background: #f4f4f4; padding: 1px 4px; border-radius: 3px; font-size: 13px; }
</style>
"""

# Resend last_event values that mean the message will NOT reach the inbox.
FATAL_EVENTS = {"bounced", "failed", "complained", "canceled"}


def render_html(markdown_text):
    body = md_lib.markdown(markdown_text, extensions=["tables", "fenced_code", "nl2br"])
    return f"<!doctype html><html><head><meta charset='utf-8'>{CSS}</head><body>{body}</body></html>"


def confirm_delivery(api_key, email_id, recipient, timeout_s=120, interval_s=10):
    """Poll Resend for the actual delivery outcome of a sent message.

    Exits non-zero (fails the workflow run) on a terminal failure event so the
    red run is a loud signal. A "delivered" event is success. If neither has
    happened by the timeout, the message was accepted but delivery is still
    unconfirmed -- warn, but don't fail the run over a slow-but-fine delivery.
    """
    url = f"https://api.resend.com/emails/{email_id}"
    headers = {"Authorization": f"Bearer {api_key}"}
    deadline = time.time() + timeout_s
    last = None
    while time.time() < deadline:
        try:
            r = requests.get(url, headers=headers, timeout=20)
        except requests.RequestException as e:
            print(f"WARN: delivery status check errored ({e}); not failing the run.",
                  file=sys.stderr)
            return
        if r.status_code >= 300:
            print(f"WARN: could not fetch delivery status [{r.status_code}]: {r.text}; "
                  "not failing the run.", file=sys.stderr)
            return
        last = (r.json().get("last_event") or "").lower()
        print(f"Delivery status: {last or '<pending>'}")
        if last == "delivered":
            print(f"Confirmed delivered to {recipient}.")
            return
        if last in FATAL_EVENTS:
            print(f"ERROR: delivery {last!r} for {recipient} (Resend id {email_id}). "
                  "The message was NOT delivered.", file=sys.stderr)
            sys.exit(1)
        time.sleep(interval_s)
    print(f"WARN: delivery not confirmed within {timeout_s}s (last status: "
          f"{last or '<pending>'}). Resend accepted the message but delivery is "
          "unconfirmed -- check the Resend dashboard if it doesn't arrive.",
          file=sys.stderr)


def send():
    api_key = os.environ["RESEND_API_KEY"]
    recipient = os.environ["BRIEFING_RECIPIENT"]
    sender = os.environ.get("RESEND_FROM", "Macro Brief <onboarding@resend.dev>")
    md_path = ROOT / "briefings" / f"briefing-{TODAY.isoformat()}.md"
    if not md_path.exists():
        print(f"ERROR: briefing not found at {md_path}", file=sys.stderr)
        sys.exit(1)

    if TEST_SENDER in sender:
        print(f"WARN: sending from Resend's shared test address ({TEST_SENDER}). "
              "Deliverability is unreliable and mail is easily filtered as spam. "
              "Set the RESEND_FROM secret to an address on a domain verified in "
              "Resend (e.g. brief@economicimpact.com).", file=sys.stderr)

    markdown_text = md_path.read_text()
    html_body = render_html(markdown_text)
    weekday = TODAY.strftime("%a")
    date_str = TODAY.strftime("%b %-d, %Y")
    subject = f"Daily Macro Briefing — {weekday} {date_str}"
    attachment_b64 = base64.b64encode(markdown_text.encode("utf-8")).decode("ascii")
    payload = {
        "from": sender,
        "to": [recipient],
        "subject": subject,
        "html": html_body,
        "text": markdown_text,
        "attachments": [{"filename": md_path.name, "content": attachment_b64}],
    }
    r = requests.post(
        "https://api.resend.com/emails",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json=payload, timeout=20,
    )
    if r.status_code >= 300:
        print(f"Resend send failed [{r.status_code}]: {r.text}", file=sys.stderr)
        sys.exit(1)
    email_id = r.json().get("id")
    print(f"Sent: {email_id or '<no-id>'} to {recipient}")

    if email_id:
        confirm_delivery(api_key, email_id, recipient)
    else:
        print("WARN: Resend returned no email id; cannot confirm delivery.", file=sys.stderr)


if __name__ == "__main__":
    send()
