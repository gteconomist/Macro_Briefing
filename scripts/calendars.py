"""
Calendar module for the Daily Macro Briefing.

Fetches one or more published .ics feeds and returns the events occurring on a
target date (in America/New_York), with recurring events expanded. Pure
stdlib + python-dateutil -- no icalendar dependency, so nothing exotic to
install and nothing to break at 7 AM.

Feeds are supplied via env vars CAL_FEED_1..N as "Label|URL" (or just URL).
"""

import os
import re
import sys
from datetime import datetime, date, timedelta, time as dtime
from dateutil.rrule import rrulestr

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    from backports.zoneinfo import ZoneInfo

import requests

ET = ZoneInfo("America/New_York")

# Outlook publishes Windows timezone IDs, not IANA. Map the common ones; any
# unmapped TZID falls back to Eastern (Alfie's zone) rather than crashing.
WINDOWS_TZ = {
    "Eastern Standard Time": "America/New_York",
    "Central Standard Time": "America/Chicago",
    "Mountain Standard Time": "America/Denver",
    "US Mountain Standard Time": "America/Phoenix",
    "Pacific Standard Time": "America/Los_Angeles",
    "Atlantic Standard Time": "America/Halifax",
    "GMT Standard Time": "Europe/London",
    "Greenwich Standard Time": "Etc/GMT",
    "UTC": "UTC",
    "W. Europe Standard Time": "Europe/Berlin",
    "Central Europe Standard Time": "Europe/Budapest",
    "Romance Standard Time": "Europe/Paris",
}


def _resolve_tz(tzid):
    if not tzid:
        return ET
    tzid = tzid.strip().strip('"')
    if tzid in WINDOWS_TZ:
        tzid = WINDOWS_TZ[tzid]
    try:
        return ZoneInfo(tzid)
    except Exception:
        return ET


def _unfold(raw):
    """RFC5545 line unfolding: continuation lines start with space/tab."""
    out = []
    for line in raw.replace("\r\n", "\n").replace("\r", "\n").split("\n"):
        if line[:1] in (" ", "\t") and out:
            out[-1] += line[1:]
        else:
            out.append(line)
    return out


def _unescape(text):
    return (text.replace("\\n", " ").replace("\\N", " ")
                .replace("\\,", ",").replace("\\;", ";").replace("\\\\", "\\")).strip()


def _split_prop(line):
    """'DTSTART;TZID=...:20260714T090000' -> (name, {params}, value)."""
    colon = line.find(":")
    if colon == -1:
        return None, {}, ""
    head, value = line[:colon], line[colon + 1:]
    parts = head.split(";")
    name = parts[0].upper()
    params = {}
    for p in parts[1:]:
        if "=" in p:
            k, v = p.split("=", 1)
            params[k.upper()] = v
    return name, params, value


def _parse_dt(value, params):
    """Return (naive_datetime_or_date, tzinfo, is_all_day)."""
    value = value.strip()
    if params.get("VALUE", "").upper() == "DATE" or (len(value) == 8 and "T" not in value):
        return datetime.strptime(value[:8], "%Y%m%d").date(), None, True
    if value.endswith("Z"):
        naive = datetime.strptime(value[:15], "%Y%m%dT%H%M%S")
        return naive, ZoneInfo("UTC"), False
    naive = datetime.strptime(value[:15], "%Y%m%dT%H%M%S")
    return naive, _resolve_tz(params.get("TZID")), False


def _parse_events(raw):
    events = []
    cur = None
    for line in _unfold(raw):
        if line == "BEGIN:VEVENT":
            cur = {"exdate": []}
        elif line == "END:VEVENT":
            if cur is not None:
                events.append(cur)
            cur = None
        elif cur is not None:
            name, params, value = _split_prop(line)
            if name == "SUMMARY":
                cur["summary"] = _unescape(value)
            elif name == "DTSTART":
                cur["dtstart"] = _parse_dt(value, params)
            elif name == "DTEND":
                cur["dtend"] = _parse_dt(value, params)
            elif name == "RRULE":
                cur["rrule"] = value.strip()
            elif name == "EXDATE":
                for chunk in value.split(","):
                    try:
                        cur["exdate"].append(_parse_dt(chunk, params)[0])
                    except Exception:
                        pass
            elif name == "STATUS":
                cur["status"] = value.strip().upper()
            elif name == "LOCATION":
                cur["location"] = _unescape(value)
            elif name == "TRANSP":
                cur["transp"] = value.strip().upper()
            elif name == "UID":
                cur["uid"] = value.strip()
            elif name == "RECURRENCE-ID":
                try:
                    cur["recurrence_id"] = _parse_dt(value, params)[0]
                except Exception:
                    pass
    return events


def _occurrences_on(ev, target, exclude_dates=None):
    """Yield (start_et, end_et, all_day) for occurrences overlapping target date."""
    if ev.get("status") == "CANCELLED" or "dtstart" not in ev:
        return
    start_raw, tz, all_day = ev["dtstart"]
    day_start = datetime.combine(target, dtime.min)
    day_end = day_start + timedelta(days=1)

    # duration
    if "dtend" in ev:
        end_raw = ev["dtend"][0]
    else:
        end_raw = (start_raw + timedelta(days=1)) if all_day else (start_raw + timedelta(hours=1))
    duration = end_raw - start_raw

    if all_day:
        if "rrule" in ev:
            base = datetime.combine(start_raw, dtime.min)
            rule = _build_rule(ev["rrule"], base)
            if rule is None:
                return
            exdates = {d for d in ev["exdate"]}
            for occ in rule.between(day_start - timedelta(days=1), day_end + timedelta(days=1), inc=True):
                occ_date = occ.date()
                if occ_date in exdates:
                    continue
                if exclude_dates and occ_date in exclude_dates:
                    continue
                if occ_date <= target < occ_date + duration:
                    yield None, None, True
                    return
        else:
            if start_raw <= target < start_raw + duration:
                yield None, None, True
        return

    # timed events: expand in naive local wall-time, then localize to event tz
    if "rrule" in ev:
        rule = _build_rule(ev["rrule"], start_raw)
        if rule is None:
            return
        exdates = {d if isinstance(d, datetime) else datetime.combine(d, dtime.min)
                   for d in ev["exdate"]}
        window_lo = day_start - timedelta(days=2)
        window_hi = day_end + timedelta(days=2)
        for occ in rule.between(window_lo, window_hi, inc=True):
            if occ in exdates:
                continue
            if exclude_dates and occ.date() in exclude_dates:
                continue
            s_et = occ.replace(tzinfo=tz).astimezone(ET)
            e_et = (occ + duration).replace(tzinfo=tz).astimezone(ET)
            if s_et < day_end.replace(tzinfo=ET) and e_et > day_start.replace(tzinfo=ET):
                yield s_et, e_et, False
    else:
        s_et = start_raw.replace(tzinfo=tz).astimezone(ET)
        e_et = end_raw.replace(tzinfo=tz).astimezone(ET)
        if s_et < day_end.replace(tzinfo=ET) and e_et > day_start.replace(tzinfo=ET):
            yield s_et, e_et, False


def _build_rule(rrule_str, dtstart_naive):
    """Build a naive dateutil rrule; strip UNTIL tz so expansion stays naive."""
    cleaned = []
    for part in rrule_str.split(";"):
        if part.upper().startswith("UNTIL="):
            val = part.split("=", 1)[1]
            val = val.rstrip("Z")
            if len(val) == 8:
                val += "T000000"
            cleaned.append("UNTIL=" + val[:15])
        else:
            cleaned.append(part)
    try:
        return rrulestr(";".join(cleaned), dtstart=dtstart_naive)
    except Exception as e:
        print(f"  rrule parse fail: {rrule_str!r}: {e}", file=sys.stderr)
        return None


def fetch_feed(url, timeout=25):
    r = requests.get(url, headers={"User-Agent": "macro-briefing-cal/1.0"}, timeout=timeout)
    r.raise_for_status()
    return r.text


def events_for_day(feeds, target):
    """feeds: list of (label, url). Returns sorted list of event dicts for target."""
    all_events = []
    for label, url in feeds:
        try:
            raw = fetch_feed(url)
        except Exception as e:
            print(f"Calendar '{label}' fetch failed: {e}", file=sys.stderr)
            all_events.append({"_error": True, "label": label, "err": str(e)})
            continue
        try:
            evs = _parse_events(raw)
        except Exception as e:
            print(f"Calendar '{label}' parse failed: {e}", file=sys.stderr)
            continue
        # dates that have a modified/override instance -> suppress the series
        # occurrence on that date so it is not shown twice.
        override_dates = {}
        for ev in evs:
            rid = ev.get("recurrence_id")
            if rid is not None and ev.get("uid"):
                d = rid.date() if hasattr(rid, "date") else rid
                override_dates.setdefault(ev["uid"], set()).add(d)
        for ev in evs:
            excl = override_dates.get(ev.get("uid")) if ev.get("rrule") else None
            for s_et, e_et, all_day in _occurrences_on(ev, target, exclude_dates=excl):
                all_events.append({
                    "label": label,
                    "summary": ev.get("summary", "(no title)"),
                    "location": ev.get("location", ""),
                    "start": s_et,
                    "end": e_et,
                    "all_day": all_day,
                })
    seen = set()
    deduped = []
    for e in all_events:
        if e.get("_error"):
            deduped.append(e); continue
        k = (e["summary"].strip().lower(), None if e["all_day"] else e["start"].isoformat(), e["all_day"])
        if k in seen:
            continue
        seen.add(k); deduped.append(e)
    all_events = deduped

    def sort_key(e):
        if e.get("_error"):
            return (2, "")
        if e["all_day"]:
            return (0, "")
        return (1, e["start"].strftime("%H%M"))
    all_events.sort(key=sort_key)
    return all_events


def _clean_loc(loc):
    if not loc:
        return ""
    low = loc.lower()
    if low.startswith("http") or "teams.microsoft.com" in low or "zoom.us/j" in low:
        return "online"
    if len(loc) > 60:
        loc = loc[:57].rstrip() + "..."
    return loc


def render_calendar_section(feeds, target):
    evs = events_for_day(feeds, target)
    real = [e for e in evs if not e.get("_error")]
    errors = [e for e in evs if e.get("_error")]
    lines = []
    if not real:
        lines.append("_No events on your calendars today._")
    else:
        for e in real:
            tag = f" · _{e['label']}_"
            loc_txt = _clean_loc(e.get("location"))
            loc = f" — {loc_txt}" if loc_txt else ""
            if e["all_day"]:
                lines.append(f"- **All day:** {e['summary']}{loc}{tag}")
            else:
                t = e["start"].strftime("%-I:%M %p").lower()
                te = e["end"].strftime("%-I:%M %p").lower()
                lines.append(f"- **{t}–{te}:** {e['summary']}{loc}{tag}")
    for e in errors:
        lines.append(f"- _⚠ Could not load {e['label']} calendar._")
    return "\n".join(lines)


def feeds_from_env():
    feeds = []
    for i in range(1, 9):
        raw = os.environ.get(f"CAL_FEED_{i}", "").strip()
        if not raw:
            continue
        if "|" in raw:
            label, url = raw.split("|", 1)
        else:
            label, url = f"Calendar {i}", raw
        url = url.strip()
        if url.startswith("webcal://"):
            url = "https://" + url[len("webcal://"):]
        feeds.append((label.strip(), url))
    return feeds
