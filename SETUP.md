# GitHub deployment — step-by-step

This walks you through the one-time setup so the daily briefing runs.

---

## 1. Add the 13 secrets to GitHub

On this repo page, go to:
**Settings → Secrets and variables → Actions → New repository secret**

Add each of these (name on left, value on right — copy from your local `.env` file):

| Secret name | Value |
|---|---|
| `FRED_API_KEY` | (from .env) |
| `BLS_API_KEY` | (from .env) |
| `BEA_API_KEY` | (from .env) |
| `CENSUS_API_KEY` | (from .env) |
| `EIA_API_KEY` | (from .env) |
| `USDA_API_KEY` | (from .env) |
| `METALPRICE_API_KEY` | (from .env) |
| `TAVILY_API_KEY` | (from .env) |
| `RESEND_API_KEY` | (from .env) |
| `MOONSHOT_API_KEY` | (from .env) |
| `MOONSHOT_MODEL` | `kimi-k2.6` |
| `BRIEFING_RECIPIENT` | `alfie@economicimpact.com` |
| `RESEND_FROM` | `Macro Brief <onboarding@resend.dev>` |

---

## 2. Verify your sender address in Resend

On the Resend free tier you can only send to addresses you've verified.

1. Log in to <https://resend.com>
2. Left sidebar → **Emails** → **Verified Emails** (or **Settings → Verified Emails**)
3. Add `alfie@economicimpact.com` and click the link in the verification email

(Alternative: verify your full `economicimpact.com` domain via DNS records, then you can send to any address at that domain. Heavier setup; do it later if you want.)

---

## 3. Run a manual test

On this repo page: **Actions** tab → click **Daily Macro Briefing** in the left sidebar → **Run workflow** dropdown (right side) → leave "Skip the 7-AM-ET gate" set to `true` → click **Run workflow**.

The run will:
1. Generate `briefings/briefing-YYYY-MM-DD.md`
2. Email it to you via Resend
3. Commit the briefing back to the repo

Check your inbox at alfie@economicimpact.com.

If the email doesn't arrive, check <https://resend.com/emails> — it logs every send attempt with the reason for failure.

---

## 4. The schedule

Once the manual test passes, the job runs automatically every weekday morning at 7:00 AM ET. No further action required — your Mac can be off.

The workflow has two cron entries (11:00 UTC + 12:00 UTC). The first matches 7 AM during EDT (March–November); the second matches 7 AM during EST (November–March). A gate inside the job checks the actual ET hour and skips if it's not 7, so only one fires per day across the year.

---

## 5. Cost

- FRED / BLS / BEA / Census / EIA / USDA / Tavily / Resend / GitHub Actions: free-tier (well within limits)
- metalpriceapi: exactly 1 call/day (script caches prior-day value for d/d)
- Moonshot Kimi K2.6: ~$0.006/day = **~$0.12/month** (~$1.50/year)

Total recurring spend: ~$0.12/month.
