# Daily Macro Briefing — Project Spec

This is a setup spec for a new Cowork project.

## Purpose

A daily macro briefing for Alfie Meek (Director, CEDR @ Georgia Tech) to read before the workday begins. Primary use: staying current on the national macroeconomy for talks given around the country. Secondary use: situational awareness when scoping sponsored research.

## Audience

One reader (Alfie). Ph.D. economist, 30 years experience. Write at peer level — no jargon translation needed, no "explainer" framing. Numbers, context, what changed, what to watch.

## Format

A single page, delivered as a markdown file each morning. Sections, in order:

1. **Top of mind** — 2–4 sentences.
2. **Yesterday's releases** — bulleted list of any data released the prior day.
3. **Today's calendar** — what's releasing today (ET).
4. **This week ahead** — next 5 business days.
5. **Markets close** — UST 2y/10y/30y, 3m10y, SOFR, eff. fed funds, S&P/Dow/NASDAQ, WTI/Brent, gold/silver, DXY, IG/HY OAS.
6. **Fed watch** — FOMC speeches/minutes/Beige Book/SEP in the next 24h or upcoming.
7. **Overnight headlines** — 4–6 top news stories, any topic.

Target length: ~500–700 words. No charts in the daily file.

## Indicators

**Labor** — Employment Situation, JOLTS, weekly initial claims, ADP, ECI
**Prices** — CPI, PPI, PCE/Core PCE, import/export prices, U Mich 1y/5y, NY Fed SCE
**Growth** — GDP, personal income & spending, retail sales, industrial production
**Housing** — starts & permits, new & existing home sales, Case-Shiller, FHFA, NAHB
**Business activity** — ISM Mfg, ISM Services, durable goods, factory orders
**Sentiment** — Conference Board, U Michigan, NFIB
**Financial conditions** — UST 2y/10y/30y, 3m10y, SOFR, IG/HY spreads, DXY, SPX/Dow/NASDAQ, WTI/Brent, gold/silver
**Fed** — FOMC statements, minutes, SEP, Beige Book, governor speeches
**Regional Fed** — Empire State, Philly, Richmond, Dallas, KC, Chicago Fed NAI

## Sources / APIs

Primary: **FRED API** (St. Louis Fed) — covers ~90% of the above.
Secondary: **BLS**, **BEA**, **Census**, **EIA**, **USDA** APIs for release timing & enrichment.
Metals: **metalpriceapi.com**.
Headlines: **Tavily**.
Interpretive prose: **Moonshot Kimi K2.6** (OpenAI-compatible API).
Email delivery: **Resend**.

## Delivery

- **When:** 7:00 AM ET, Monday–Friday.
- **How:** GitHub Actions cron → generate markdown → email via Resend → commit to repo.
- **History:** `briefings/` subfolder, dated files.
