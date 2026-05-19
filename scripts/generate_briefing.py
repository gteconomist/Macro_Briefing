"""
Daily Macro Briefing generator for Alfie Meek (Director, CEDR @ Georgia Tech).
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BRIEFINGS_DIR = ROOT / "briefings"
CACHE_DIR = ROOT / "cache"
BRIEFINGS_DIR.mkdir(exist_ok=True)
CACHE_DIR.mkdir(exist_ok=True)

try:
    from zoneinfo import ZoneInfo
    ET = ZoneInfo("America/New_York")
except ImportError:
    ET = timezone(timedelta(hours=-5))

NOW_ET = datetime.now(ET)
TODAY = NOW_ET.date()


def load_dotenv(path):
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        if "=" in line and not line.strip().startswith("#"):
            k, v = line.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip())


load_dotenv(ROOT / ".env")


FRED_BASE = "https://api.stlouisfed.org/fred"


def fred_obs(series_id, limit=24):
    r = requests.get(
        f"{FRED_BASE}/series/observations",
        params={
            "series_id": series_id,
            "api_key": os.environ["FRED_API_KEY"],
            "file_type": "json",
            "sort_order": "desc",
            "limit": limit,
        },
        timeout=15,
    )
    r.raise_for_status()
    return [o for o in r.json().get("observations", []) if o.get("value", ".") != "."]


DAILY_REFRESH_RELEASE_IDS = {
    17, 18, 72, 86, 101, 185, 187, 190, 200, 209, 212, 221, 239, 242,
    269, 271, 279, 280, 287, 304, 315, 317, 328, 342, 345, 354, 363,
    371, 375, 378, 379, 383, 400, 427, 441, 443, 445, 454, 465, 468,
    473, 483, 484, 487, 492, 494, 500, 502, 504, 637, 736, 739, 742,
    769, 1105,
}


def fred_release_dates_today(target_date):
    r = requests.get(
        f"{FRED_BASE}/releases/dates",
        params={
            "api_key": os.environ["FRED_API_KEY"],
            "file_type": "json",
            "realtime_start": target_date.isoformat(),
            "realtime_end": target_date.isoformat(),
            "include_release_dates_with_no_data": "false",
            "limit": 1000,
            "sort_order": "asc",
        },
        timeout=15,
    )
    r.raise_for_status()
    out = []
    for rd in r.json().get("release_dates", []):
        if rd["date"] != target_date.isoformat():
            continue
        rid = rd["release_id"]
        if rid in DAILY_REFRESH_RELEASE_IDS:
            continue
        out.append((rid, rd.get("release_name", "")))
    return out


METALS_CACHE = CACHE_DIR / "metals_prev.json"


def pull_metals():
    r = requests.get(
        "https://api.metalpriceapi.com/v1/latest",
        params={
            "api_key": os.environ["METALPRICE_API_KEY"],
            "base": "USD",
            "currencies": "XAU,XAG",
        },
        timeout=15,
    )
    r.raise_for_status()
    j = r.json()
    if not j.get("success"):
        return {}
    rates = j["rates"]
    gold = rates.get("USDXAU")
    silver = rates.get("USDXAG")
    prev = {}
    if METALS_CACHE.exists():
        try:
            prev = json.loads(METALS_CACHE.read_text())
        except Exception:
            prev = {}
    gold_dd = ((gold / prev["gold"] - 1) * 100) if prev.get("gold") else None
    silver_dd = ((silver / prev["silver"] - 1) * 100) if prev.get("silver") else None
    METALS_CACHE.write_text(json.dumps({"gold": gold, "silver": silver, "as_of": NOW_ET.isoformat()}))
    return {"gold": gold, "silver": silver, "gold_dd": gold_dd, "silver_dd": silver_dd}


def pull_headlines(n=6):
    r = requests.post(
        "https://api.tavily.com/search",
        headers={
            "Authorization": f"Bearer {os.environ['TAVILY_API_KEY']}",
            "Content-Type": "application/json",
        },
        json={
            "query": "most important top news stories today United States global",
            "topic": "news",
            "max_results": 15,
            "days": 1,
            "include_answer": False,
            "search_depth": "advanced",
            "include_domains": [
                "reuters.com", "apnews.com", "bloomberg.com", "ft.com",
                "wsj.com", "nytimes.com", "washingtonpost.com", "bbc.com",
                "cnbc.com", "axios.com", "politico.com", "economist.com",
            ],
        },
        timeout=20,
    )
    r.raise_for_status()
    results = r.json().get("results", [])
    drop_kw = ("cannes", "box office", "humpback", "barbra streisand", "cate blanchett", "metoo", "palme")
    cleaned = []
    seen = set()
    for res in results:
        title = res.get("title", "").strip()
        low = title.lower()
        if any(k in low for k in drop_kw):
            continue
        key = title.split(" - ")[0][:60].lower()
        if key in seen:
            continue
        seen.add(key)
        if " - " in title:
            head, _, tail = title.rpartition(" - ")
            source = tail
            title = head
        else:
            source = res.get("url", "").split("/")[2].replace("www.", "")
        cleaned.append({"title": title, "url": res["url"], "source": source})
        if len(cleaned) >= n:
            break
    return cleaned


def fmt_pct(latest, prior):
    if not (latest and prior):
        return "—"
    try:
        return f"{(float(latest) / float(prior) - 1) * 100:+.2f}%"
    except Exception:
        return "—"


MOONSHOT_ENDPOINT = "https://api.moonshot.ai/v1/chat/completions"
DEFAULT_MOONSHOT_MODEL = "kimi-k2.6"

INTERPRETIVE_SYSTEM = """You write the interpretive sections of a daily macro briefing for Alfie Meek, a Ph.D. economist and Director of the Center for Economic Development Research at Georgia Tech. He uses the briefing to start his workday and to inform talks he gives around the country on the U.S. macroeconomy.

Tone and style:
- Peer-level. He's a Ph.D. economist with 30 years of experience — no jargon translation, no explainer framing.
- Direct and concise. No disclaimers. No corporate language. No "in summary." No repeating the question.
- Numbers, context, what changed, what to watch — not commentary about commentary.

You will be given a JSON payload of the morning's pulled data: FRED indicator values (latest and prior), the list of FRED-confirmed releases on the previous business day, headlines, and market levels. Use those numbers — do not invent any.

Output FOUR markdown sections in this exact order and with these exact headers:

## Top of mind
2–4 sentences. The single most important macro story right now, and what (if anything) overnight changed it. Reference specific numbers from the payload.

## Yesterday's releases ({date})
Bulleted list of indicators released on the prior business day. Each bullet: **Indicator name (period):** value (vs. prior or vs. consensus) — one-line interpretation.

## Today's calendar ({today}, ET)
Bulleted list of what's releasing today, with release time in ET and a one-line note on what to watch. Infer from typical BLS/BEA/Census/Fed release schedules.

## This week ahead
Bulleted list, one bullet per remaining business day this week. Format: **Day M/D:** indicator(s).

## Fed watch
2–4 sentences. Current target range (use DFEDTARU/DFEDTARL from payload), effective rate (DFF), SOFR. Note any FOMC speech, minutes, Beige Book, or SEP refresh in the next 5 business days.

Important: return ONLY those four sections in valid markdown. No preamble."""


def _condense_fred(fred):
    out = {}
    for sid, obs in fred.items():
        if not obs:
            continue
        rec = {"latest": {"date": obs[0]["date"], "value": obs[0]["value"]}}
        if len(obs) > 1:
            rec["prior"] = {"date": obs[1]["date"], "value": obs[1]["value"]}
        out[sid] = rec
    return out


def call_llm_for_prose(today, data):
    api_key = os.environ.get("MOONSHOT_API_KEY", "").strip()
    if not api_key:
        return _stub_prose(today, data, reason="MOONSHOT_API_KEY not present in environment")
    model = os.environ.get("MOONSHOT_MODEL", DEFAULT_MOONSHOT_MODEL).strip() or DEFAULT_MOONSHOT_MODEL
    last_bday = today - timedelta(days=1)
    while last_bday.weekday() > 4:
        last_bday -= timedelta(days=1)
    payload = {
        "today": today.isoformat(),
        "today_weekday": today.strftime("%A"),
        "last_business_day": last_bday.isoformat(),
        "last_business_day_weekday": last_bday.strftime("%A"),
        "fred": _condense_fred(data.get("fred", {})),
        "fred_releases_last_business_day": [name for _, name in data.get("releases_yday", [])],
        "metals": data.get("metals", {}),
        "headlines": data.get("headlines", []),
    }
    body = {
        "model": model,
        "max_tokens": 2500,
        "temperature": 1,
        "messages": [
            {"role": "system", "content": INTERPRETIVE_SYSTEM},
            {"role": "user", "content": "Morning data payload follows. Write the four interpretive sections per system instructions:\n\n" + json.dumps(payload, indent=2, default=str)},
        ],
    }
    try:
        r = requests.post(
            MOONSHOT_ENDPOINT,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json=body, timeout=60,
        )
    except Exception as e:
        print(f"Moonshot connection error: {e}", file=sys.stderr)
        return _stub_prose(today, data, reason=f"Connection error: {type(e).__name__}: {e}")
    if r.status_code >= 300:
        err_body = (r.text or "")[:600]
        print(f"Moonshot call failed [{r.status_code}]: {err_body}", file=sys.stderr)
        return _stub_prose(today, data, reason=f"HTTP {r.status_code} from {MOONSHOT_ENDPOINT} (model={model}). Response: {err_body}")
    try:
        resp = r.json()
        text = resp.get("choices", [{}])[0].get("message", {}).get("content", "")
        if not text.strip():
            return _stub_prose(today, data, reason=f"Moonshot returned empty content. Raw: {str(resp)[:400]}")
        return text.strip()
    except Exception as e:
        print(f"Moonshot parse error: {e}", file=sys.stderr)
        return _stub_prose(today, data, reason=f"Parse error: {type(e).__name__}: {e}")


def _stub_prose(today, data, reason="unknown"):
    last_bday = today - timedelta(days=1)
    while last_bday.weekday() > 4:
        last_bday -= timedelta(days=1)
    releases = data.get("releases_yday", [])
    rel_text = "\n".join(f"- {name}" for _, name in releases[:8]) if releases else f"_No major U.S. economic releases dated {last_bday.isoformat()}._"
    return f"""## Top of mind
_LLM section unavailable. Reason: **{reason}**_

## Yesterday's releases ({last_bday.strftime('%a %-m/%-d')})
{rel_text}

## Today's calendar ({today.strftime('%a %-m/%-d')}, ET)
_Auto-calendar unavailable (LLM step failed)._

## This week ahead
_Auto-calendar unavailable (LLM step failed)._

## Fed watch
_Auto-Fed-watch unavailable (LLM step failed)._"""


def render(today, data):
    weekday = today.strftime("%A")
    date_str = today.strftime("%B %d, %Y")
    rows = []

    def m(name, sid, fmt="{:.2f}"):
        obs = data["fred"].get(sid, [])
        if len(obs) < 2:
            return f"| {name} | — | — | — |"
        latest = float(obs[0]["value"])
        prior = float(obs[1]["value"])
        wk_ago = float(obs[5]["value"]) if len(obs) > 5 else None
        if "%" in name or "bp" in name.lower() or sid.startswith("DGS") or sid in ("SOFR", "T10Y2Y", "T10Y3M", "BAMLC0A0CM", "BAMLH0A0HYM2"):
            dd_str = f"{(latest - prior) * 100:+.0f} bp" if sid.startswith("BAML") else f"{latest - prior:+.2f}"
            ww_str = f"{(latest - wk_ago) * 100:+.0f} bp" if (wk_ago is not None and sid.startswith("BAML")) else (f"{latest - wk_ago:+.2f}" if wk_ago is not None else "—")
        else:
            dd_str = fmt_pct(latest, prior)
            ww_str = fmt_pct(latest, wk_ago) if wk_ago is not None else "—"
        return f"| {name} | {fmt.format(latest)} | {dd_str} | {ww_str} |"

    rows.append(m("UST 2y", "DGS2"))
    rows.append(m("UST 10y", "DGS10"))
    rows.append(m("UST 30y", "DGS30"))
    rows.append(m("3m10y", "T10Y3M"))
    rows.append(m("SOFR", "SOFR"))
    rows.append(m("Eff. fed funds", "DFF"))
    rows.append(m("S&P 500", "SP500", "{:,.2f}"))
    rows.append(m("Dow Jones", "DJIA", "{:,.2f}"))
    rows.append(m("NASDAQ Comp.", "NASDAQCOM", "{:,.2f}"))
    rows.append(m("WTI", "DCOILWTICO", "${:.2f}"))
    rows.append(m("Brent", "DCOILBRENTEU", "${:.2f}"))
    metals = data.get("metals", {})
    if metals.get("gold"):
        gd = f"{metals['gold_dd']:+.2f}%" if metals.get("gold_dd") is not None else "—"
        rows.append(f"| Gold (spot) | ${metals['gold']:,.2f} | {gd} | — |")
    if metals.get("silver"):
        sd = f"{metals['silver_dd']:+.2f}%" if metals.get("silver_dd") is not None else "—"
        rows.append(f"| Silver (spot) | ${metals['silver']:,.2f} | {sd} | — |")
    rows.append(m("Broad USD (DTWEXBGS)*", "DTWEXBGS", "{:.2f}"))
    rows.append(m("HY OAS", "BAMLH0A0HYM2", "{:.0f} bp"))
    rows.append(m("IG OAS", "BAMLC0A0CM", "{:.0f} bp"))

    markets_table = "\n".join(["| | Level | d/d | w/w |", "|---|---|---|---|"] + rows)

    hl_lines = [f"- **{h['title']}** — *{h['source']}*" for h in data.get("headlines", [])]
    headlines_md = "\n".join(hl_lines) if hl_lines else "_No headlines pulled this run._"

    prose = call_llm_for_prose(today, data)

    return f"""# Daily Macro Briefing — {weekday}, {date_str}

{prose}

## Markets close
{markets_table}

*DTWEXBGS publishes with ~1-week lag. Gold/silver from metalpriceapi.com.*

## Overnight headlines
{headlines_md}

---
*Sources: FRED; metalpriceapi.com; Tavily; Moonshot Kimi. Data current as of {today.isoformat()}.*
"""


FRED_SERIES = [
    "DGS2", "DGS10", "DGS30", "T10Y3M", "SOFR", "DFF",
    "DFEDTARU", "DFEDTARL",
    "SP500", "DJIA", "NASDAQCOM",
    "DCOILWTICO", "DCOILBRENTEU",
    "DTWEXBGS",
    "BAMLC0A0CM", "BAMLH0A0HYM2",
    "UNRATE", "PAYEMS", "CIVPART", "AHETPI", "ICSA", "CCSA", "JTSJOL",
    "CPIAUCSL", "CPILFESL", "PPIFIS", "PCEPI", "PCEPILFE",
    "RSAFS", "RSFSXMV", "INDPRO", "TCU", "HOUST", "PERMIT", "HSN1F",
    "GACDISA066MSFRBNY", "GACDFSA066MSFRBPHI", "CFNAI",
    "UMCSENT", "MICH", "GDPNOW", "IR", "IQ",
]


def main():
    data = {"fred": {}, "metals": {}, "headlines": [], "releases_yday": []}
    for sid in FRED_SERIES:
        try:
            data["fred"][sid] = fred_obs(sid, limit=12)
        except Exception as e:
            print(f"FRED {sid} failed: {e}", file=sys.stderr)
    last_bday = TODAY - timedelta(days=1)
    while last_bday.weekday() > 4:
        last_bday -= timedelta(days=1)
    try:
        data["releases_yday"] = fred_release_dates_today(last_bday)
    except Exception as e:
        print(f"FRED releases failed: {e}", file=sys.stderr)
    try:
        data["metals"] = pull_metals()
    except Exception as e:
        print(f"metalpriceapi failed: {e}", file=sys.stderr)
    try:
        data["headlines"] = pull_headlines(n=6)
    except Exception as e:
        print(f"Tavily failed: {e}", file=sys.stderr)
    md = render(TODAY, data)
    out_path = BRIEFINGS_DIR / f"briefing-{TODAY.isoformat()}.md"
    out_path.write_text(md)
    (ROOT / "latest.md").write_text(md)
    print(f"Wrote {out_path}")
    print(f"Words: {len(md.split())}")


if __name__ == "__main__":
    main()
