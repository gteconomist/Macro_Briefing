# Daily Macro Briefing — Project Instructions for Claude

This file is loaded automatically each session. Read it first.

## Who this is for
Alfie Meek, Ph.D. economist, Director of the Center for Economic Development Research at Georgia Tech. He tracks the national macroeconomy for talks given around the country and uses this briefing to start his workday. Write at peer level — no jargon translation.

## Communication style
Direct and concise. No disclaimers, no corporate language, no "Great question". Don't repeat his words back. He has zero programming background — do the work for him rather than handing him code to run.

## Project files
- `macro-briefing-spec.md` — the full project spec. Authoritative on format, sections, indicators, sources.
- `.env` — API keys (FRED, and whatever else gets added). Do not commit; do not echo.
- `briefings/` — dated markdown files, one per business day.
- `scripts/` — Python that pulls data and renders the briefing.
- `latest.md` — symlink/copy of the most recent briefing, for quick access.

## Format reminders
Single page, ~500–700 words, no charts. Sections in this order:
0. Your calendar today — combined personal + work events, from the ICS feeds in `CAL_FEED_1..N` (parsed by `scripts/calendars.py`). Rendered deterministically by the script, not the LLM.
1. Top of mind (2–4 sentences)
2. Yesterday's releases
3. Today's calendar
4. This week ahead
5. Markets close (UST 2y/10y, 2s10s, fed funds path, DXY, S&P 500, WTI)
6. Fed watch
7. Regional pulse

## When generating a briefing
- Pull live data via FRED/BLS/BEA/Census/Treasury APIs. Do not invent numbers.
- For "yesterday's releases" use the actual release calendar — if nothing released, say so.
- For "today's calendar" and "this week ahead", consult the BLS/BEA/Census release schedules.
- Save the output to `briefings/briefing-YYYY-MM-DD.md` and update `latest.md`.

## Schedule
Runs weekday mornings at 7:00 AM ET. The trigger is a **Cowork scheduled task** (`macro-briefing-trigger`, cron `0 7 * * 1-5`) that bumps the file `.github/briefing-trigger` on `main`; that push runs `.github/workflows/daily-briefing.yml`, which triggers `on: push` to that file (plus manual `workflow_dispatch`). The workflow no longer has an ET-hour gate — the scheduled task controls timing.

Retired: the external **OpenClaw** cron and GitHub's own `schedule:` cron. GitHub scheduled workflows fire unreliably on this repo (Actions-bot commits don't reset GitHub's 60-day scheduler-disable timer), which is why timing is driven externally by the scheduled task instead. Caveat: Cowork scheduled tasks run only while the Claude desktop app is open — if it's closed at 7 AM, the task runs on next launch.
