# Daily Macro Briefing

Automated daily macroeconomic briefing for Alfie Meek (Director, Center for
Economic Development Research, Georgia Tech).

Pulls live data from FRED, BLS, BEA, Census, EIA, metalpriceapi, and Tavily;
renders a one-page markdown brief; emails it via Resend at 7:00 AM ET each
weekday morning.

## Layout

```
.
├── CLAUDE.md                 Project context for Claude sessions
├── macro-briefing-spec.md    Full spec (format, sections, indicators, sources)
├── SETUP.md                  Step-by-step GitHub deployment guide
├── requirements.txt          Python dependencies
├── scripts/
│   ├── generate_briefing.py  Pulls data, renders briefing markdown
│   └── send_email.py         Emails today's briefing via Resend
├── .github/workflows/
│   └── daily-briefing.yml    Weekday 7 AM ET cron + email
├── briefings/                Dated archive of past briefings
├── latest.md                 Copy of most recent briefing
└── cache/                    Per-day cache for d/d computations (metals)
```

## Local run (testing)

```bash
pip install -r requirements.txt
python scripts/generate_briefing.py
python scripts/send_email.py
```

API keys are read from `.env` (gitignored — never commit it) or from
environment variables (used by the GitHub Actions runner).

## Deployment

See `SETUP.md` for the one-time GitHub setup. Once deployed, no manual action
is required — the workflow runs automatically.
