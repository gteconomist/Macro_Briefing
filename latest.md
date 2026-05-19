# Daily Macro Briefing — Tuesday, May 19, 2026

## Top of mind
  2. ## Yesterday's releases (May 18)
  3. ## Today's calendar (May 19, ET)
  4. ## This week ahead
  5. ## Fed watch
- Wait, the instructions say FOUR sections but list five headers. Let me re-read carefully.
  - "Output FOUR markdown sections in this exact order and with these exact headers:"
  - Then it lists: Top of mind, Yesterday's releases ({date}), Today's calendar ({today}, ET), This week ahead, Fed watch. That's FIVE headers listed.
  - Wait, let me count again:
    1. ## Top of mind
    2. ## Yesterday's releases ({date})
    3. ## Today's calendar ({today}, ET)
    4. ## This week ahead
    5. ## Fed watch
  - That's 5. But the text says "Output FOUR markdown sections". This is ambiguous. However, looking at the exact headers listed, there are 5. But the first sentence says FOUR. Let me check if one is optional or if the instruction has a typo. Actually, looking carefully: "Output FOUR markdown sections in this exact order and with these exact headers:" followed by 5 headers. This is likely a typo in the prompt where Fed watch is the fifth, but maybe they meant five? Or maybe "Fed watch" is considered part of one of the others? No, it's listed separately.
  - Actually, re-reading: "Output FOUR markdown sections in this exact order and with these exact headers:" — perhaps they consider "Fed watch" as part of the four? No, that doesn't make sense.
  - Wait, maybe I miscounted: 1) Top of mind, 2) Yesterday's releases, 3) Today's calendar, 4) This week ahead, 5) Fed watch. That's definitely 5.
  - I think the safest approach is to include all 5 sections as listed, because they are explicitly listed as "these exact headers". The number "FOUR" is likely a typo by the user given that 5 headers follow. However, I should be careful. If I include 5, I violate "FOUR". If I include 4, I violate "these exact headers" by omitting one.
  - Looking at the instruction again: "Output FOUR markdown sections in this exact order and with these exact headers:" — this is contradictory. But given the headers are explicitly enumerated, I will output all 5 sections because omitting one would violate "these exact headers". The "FOUR" is likely an error in the prompt. Actually, maybe they meant "Output the following markdown sections..." and "FOUR" was left from an earlier draft. I'll include all 5 to be safe because the headers are explicitly itemized.
  - Actually, looking very carefully, maybe the user copy-pasted from a template where there were four, then added Fed watch. I will include all 5 because the headers are explicitly listed.

Let me extract the relevant data:

Today: 2026-05-19 (Tuesday)
Last business day: 2026-05-18 (Monday)

FRED data to use:
- DGS2: 4.07 (May 18) vs 4.09 (May 15) → down 2bp
- DGS10: 4.61 (May 18) vs 4.59 (May 15) → up 2bp
- DGS30: 5.14 (May 18) vs 5.12 (May 15) → up 2bp
- T10Y3M: 1.0 (May 19) vs 0.93 (May 18) → steepened
- SOFR: 3.53 (May 18) vs 3.55 (May 15) → down 2bp
- DFF: 3.63 (May 18) vs 3.63 (May 17) → unchanged
- DFEDTARU: 3.75 (May 19)
- DFEDTARL: 3.5 (May 19)
- SP500: 7403.05 (May 18) vs 7408.5 (May 15) → down slightly
- DJIA: 49686.12 (May 18) vs 49526.17 (May 15) → up
- NASDAQCOM: 26090.73 (May 18) vs 26225.14 (May 15) → down
- DCOILWTICO: 101.56 (May 11) vs 98.87 (May 8) → up (note: stale, May 11)
- DCOILBRENTEU: 106.11 (May 11) vs 103.48 (May 8) → up (stale)
- DTWEXBGS: 119.2825 (May 15) vs 118.6696 (May 14) → dollar up
- BAMLC0A0CM (IG spread): 0.75 unchanged
- BAMLH0A0HYM2 (HY spread): 2.83 vs 2.80 → widened 3bp
- UNRATE: 4.3 (April) vs 4.3 (March) → unchanged
- PAYEMS: 158736 (April) vs 158621 (March) → +115k jobs
- CIVPART: 61.8 (April) vs 61.9 (March) → down 0.1pp
- AHETPI: 32.23 (April) vs 32.12 (March) → wage growth continues
- ICSA: 211000 (May 9) vs 199000 (May 2) → claims up
- CCSA: 1782000 (May 2) vs 1758000 (April 25) → continuing claims up
- JTSJOL: 6866 (March) vs 6922 (February) → job openings down
- CPIAUCSL: 332.407 (April) vs 330.293 (March) → headline CPI up
- CPILFESL: 335.423 (April) vs 334.165 (March) → core CPI up
- PPIFIS: 156.496 (April) vs 154.372 (March) → PPI up
- PCEPI: 130.344 (March) vs 129.484 (February)
- PCEPILFE: 129.279 (March) vs 128.901 (February)
- RSAFS: 757085 (April) vs 753370 (March) → retail sales up
- RSFSXMV: 617856 (April) vs 613556 (March) → retail ex-auto up
- INDPRO: 102.4963 (April) vs 101.806 (March) → industrial production up
- TCU: 76.1194 (April) vs 75.6716 (March) → capacity utilization up
- HOUST: 1502 (March) vs 1356 (February) → housing starts up
- PERMIT: 1363 (March) vs 1538 (February) → permits down
- HSN1F: 682 (March) vs 635 (February) → new home sales up
- GACDISA066MSFRBNY (NY Fed GSCPI): 19.6 (May) vs 11.0 (April) → supply chain pressure up significantly
- GACDFSA066MSFRBPHI (Philly Fed prices paid): 26.7 (April) vs 18.1 (March) → input prices up
- CFNAI: -0.2 (March) vs 0.03 (February) → below zero
- UMCSENT: 53.3 (March) vs 56.6 (February) → sentiment down
- MICH: 3.8 (March) vs 3.4 (February) → inflation expectations up
- GDPNOW: 3.9912 (April/Q2?) vs 1.2392 (Jan/Q1?) → GDP tracking strong
- IR: 147.6 (April) vs 144.8 (March) → interest rates component? Actually IR is Real Retail and Food Services? No, IR might be Imports? Wait, IR and IQ. Actually in FRED, IR is "Real Retail and Food Services Sales"? No. Let me think. IR could be "Business Inventory to Sales Ratio"? No. Actually IR and IQ might not be standard acronyms I recognize immediately. But the values are 147.6 and 166.1. Without clear identification, I should avoid them or be careful. Actually, IR might be "Import Price Index"? IQ might be "Export Price Index"? No, those are usually IQ and IR? Wait. Looking at FRED codes: IQ might be "Real Gross Domestic Product" no. Actually, IR could be "Real Imports of Goods" (IR). IQ could be "Real Imports of Services" or maybe "Business Inventories"? Without certainty, I should be cautious about interpreting them. But looking at the payload, they were included. Maybe IR = Industrial Production? No, that's INDPRO. Maybe IR and IQ are from some specific dataset. Given I can't confidently identify them from standard FRED mnemonics without guessing, and the prompt says "use those numbers — do not invent any", I can reference them if I know what they are. Actually, looking at FRED: IR is "Interest Rates, Government Securities, Treasury Bills for United States" but that doesn't fit the values (147.6). Wait, maybe these are Atlanta Fed GDPNow subcomponents? IR = "Real gross private domestic investment"? No. Let me not use them if I'm unsure. Actually, upon second thought, in some contexts IR = "Import Index" and IQ = "Export Index"? No. Given the ambiguity and to avoid inventing context, I'll omit them unless necessary.
- FRED releases last business day (May 18): Business Leaders Survey, Quarterly Retail E-Commerce Sales, State Unemployment Insurance Weekly Claims Report. Note: The payload says these were released, but I don't have the values in the fred section for these specific series (except ICSA which is weekly claims). Actually "State Unemployment Insurance Weekly Claims Report" corresponds to ICSA, which is in the data: 211k for May 9 vs prior 199k. Business Leaders Survey might be the NY Fed Business Leaders Survey? That's GACDISA066MSFRBNY? No, that's GSCPI. The Business Leaders Survey is a separate NY Fed survey. But we don't have its value in the fred dict. Quarterly Retail E-Commerce Sales would correspond to a Census release. No value in fred dict. So for Yesterday's releases, I can mention what released but if I don't have the number in the payload, should I mention it? The instructions say: "Bulleted list of indicators released on the prior business day. Each bullet: **Indicator name (period):** value (vs. prior or vs. consensus) — one-line interpretation." Since I only have the ICSA value explicitly in the payload (211k), and the others aren't in the fred dict with values, I have to be careful. The payload lists the releases but doesn't give numbers for Business Leaders Survey or Quarterly Retail E-Commerce Sales. However, ICSA is in the payload. For the others, since there are no numbers provided, I cannot invent them. I should only list the ones where I have data? Or note that they released but I don't have values? The instructions say "Use those numbers — do not invent any." So I will only list ICSA with its value, or perhaps note the others without values? The bullet format requires "value (vs. prior or vs. consensus)". If I don't have the value, I can't complete the bullet. So I should probably only include ICSA, or include the others and say data not in payload? No, the user likely expects me to use what's available. Actually, maybe I should check if any of the FRED codes correspond. "Quarterly Retail E-Commerce Sales" — no FRED code in the dict matches this exactly. "Business Leaders Survey" — no matching code. So I'll only include the Weekly Claims Report (ICSA) for which I have data. But wait, the payload explicitly lists these three as releases. The user might expect all three listed. If I list them without numbers, I violate the format. If I omit them, I might miss something. I think the safest is to list all three but for the ones without numbers, I cannot provide values. However, looking back at the prompt: "Each bullet: **Indicator name (period):** value (vs. prior or vs. consensus) — one-line interpretation." This implies I need values. Since I don't have them for two of the three, I will only include the one with data (ICSA). Actually, maybe I can infer "Business Leaders Survey" is the NY Empire State or something? But no value is given. I'll stick to what I have numbers for. Actually, I just noticed: the prompt says "FRED-confirmed releases on the previous business day". These are confirmed releases. But the payload's fred dict includes ICSA. So I'll mention ICSA. For the others, I'll omit since no values are provided and I cannot invent them.

Wait, actually, I should check if the "Quarterly Retail E-Commerce Sales" could relate to RSFSXMV or RSAFS? Those are monthly Retail Sales and Retail Sales ex-auto. The payload has April values for RSAFS and RSFSXMV (757085 and 617856), but those were likely released earlier (around mid-May). But Quarterly Retail E-Commerce Sales is a quarterly series (Q1 2026?). I don't have that in the fred dict. So no.

So Yesterday's releases:
- **State Unemployment Insurance Weekly Claims Report (week ended May 9):** 211k (vs. 199k prior) — a 12k jump in initial claims that bears watching but remains in a low range.

That's the only one with data. But should I mention the others without numbers? I think not, because I can't provide the required format.

Today's calendar (May 19, ET):
What typically releases on May 19?
I need to infer from typical BLS/BEA/Census/Fed release schedules.
Mid-May: Housing data? Actually, we already have housing starts/permits/new home sales data in the payload through March. Those are usually released mid-month. But today is May 19, 2026.
Typical schedule around May 19:
- Building Permits and Housing Starts for April? No, those were likely released earlier (the payload has March data). Actually, Housing Starts and Permits are usually released around the 16th-18th of the month. Since the payload has March data for HOUST/PERMIT/HSN1F, the April data might be releasing today or soon. Wait: the payload has March 2026 data for housing variables. That suggests April housing data hasn't been released yet. But typically New Home Sales (HSN1F) is released near the end of the month. Housing Starts/Permits are released around the middle. If today is May 19, April Housing Starts and Permits could be releasing today. Actually, Census Bureau typically releases housing starts around the 16th-18th business day? Let me think: In the real world, housing starts are usually released around the 17th-18th of the month. So May 19 (Tuesday) could be the release day for April housing starts and building permits. New Home Sales is usually later (around the 23rd).
What else in mid-May?
- FOMC minutes? The last FOMC meeting was likely April 28-29, 2026. Minutes are released 3 weeks after, which would be around May 20 or 21. So maybe Wednesday May 20, not today.
- Existing Home Sales? Usually around the 21st-22nd. So maybe later this week.
- Leading Economic Index? Released toward month-end.
- PMIs (S&P Global) are usually around the 20th-24th for preliminary? Actually S&P Global PMI flash is around the 20th-24th. But the full month is later.
- Regional Fed surveys: Philadelphia Fed Business Outlook? Usually third Thursday of the month (May 21). Kansas City Fed? Later.
- Jobless claims? That's Thursday.
- BLS data: We already had CPI, PPI, retail sales, industrial production. What about Business Inventories? Wholesale inventories? Those are later.
- Treasury International Capital (TIC) data? Usually mid-month.
- NAHB Housing Market Index? Usually around the 15th-17th. Could be today or yesterday.
Given the payload has NY Fed GSCPI as of May 1 (19.6), which is a monthly supply chain index, but that's not a standard daily release.

Actually, a very typical release for the third week of May:
- April Housing Starts and Building Permits (Census) — often around May 19.
- April Industrial Production and Capacity Utilization? No, that's usually mid-month and already in payload as April values (released earlier, perhaps May 15).
- April Retail Sales? Already in payload (April values), likely released May 15.
- April PPI? Already in payload (April values).
- April CPI? Already in payload (April values).

So what's left for May 19?
Possibly:
- Housing Starts and Building Permits for April (Census Bureau) at 8:30 AM ET
- FOMC minutes? If the meeting was April 28-29, minutes would be Wednesday May 20 (3 weeks later). But if the schedule is slightly different... Actually, standard is 3 weeks after, so April 29 + 21 days = May 20. So likely Wednesday.
- Weekly Redbook? Not a major FRED release.
- EIA Petroleum Status Report? Not FRED macro.
- Treasury auction? Not macro data.

Another possibility: The NY Fed's Empire State Manufacturing Survey for May? Actually that's usually released around May 15. The Business Leaders Survey (general business conditions) might be the Empire State? But the payload lists "Business Leaders Survey" as released yesterday (May 18). Wait, the Business Leaders Survey is released by the NY Fed on the Monday after the second Friday of the month? Actually, the NY Fed Business Leaders Survey is quarterly? No, it's monthly? Let me check: The Business Leaders Survey is a monthly survey by NY Fed, released on the Monday after the second Friday. So May 11 would be second Friday? Actually May 8 is second Friday of May 2026? Let's count: May 1 is Friday. May 8 is second Friday. So Monday after is May 11. But the payload says it released May 18. Hmm. Maybe I'm wrong about the schedule.

Given I need to infer today's calendar, I should list plausible major releases. Common releases for the third Tuesday of May:
- Housing Starts and Building Permits (April) - Census Bureau, 8:30 AM ET.
- This is the most likely candidate.

Could also be:
- April New Residential Construction (Housing Starts & Permits) — yes, this is a standard Census release.
- FOMC minutes are likely Wednesday, not Tuesday.
- Existing Home Sales (April) — NAR, usually around the 21st, so maybe Thursday.
- Leading Indicators (Conference Board LEI) for April — usually third or fourth week, maybe Thursday or Friday.

So for Today:
- **8:30 AM:** April housing starts and building permits — watch if the March surge in starts (1502k) holds or if permits (1363k) signal a pullback.
- Maybe also something else? April Treasury International Capital (TIC) data is usually released around the 15th business day. May 19 could be the release. But that's less prominent.
- Or NY Fed's Empire State Manufacturing Survey for May? Wait, if Business Leaders Survey was yesterday, maybe Empire State was yesterday too? Actually the Empire State Manufacturing Survey is a different survey from the NY Fed. It's usually released around the 15th of the month. In May 2026, the 15th was a Friday. So it might have been Friday. But the payload lists "Business Leaders Survey" as a release yesterday (Monday May 18). Perhaps they release on a lag.

Given the constraint to infer from typical schedules, I will include Housing Starts/Permits for April as the primary release today. I might also include FOMC Minutes for tomorrow (Wednesday) in This Week Ahead rather than today.

Wait, I need to be careful about "Today's calendar (May 19, ET)". I should only list what's actually releasing today. If I'm not sure, I should only list what is highly probable. Housing starts and building permits for April is very likely.

What else? The payload has crude oil data from May 11 (stale). EIA inventory data is weekly but not a FRED/BEA/BLS/Census/Fed macro release per se, though it's on the calendar.

Another possibility: The Federal Reserve's April Industrial Production was already released (in payload). April Capacity Utilization too.

April New Home Sales? Usually released toward the end of the month. But the payload has March new home sales. So April new home sales could be today or later. Actually New Home Sales is usually released on the 23rd-26th. So probably not today.

April Existing Home Sales? Usually around the 21st.

April Wholesale Inventories? Mid-month-ish.

Given the instructions say "Bulleted list of what's releasing today, with release time in ET and a one-line note on what to watch. Infer from typical BLS/BEA/Census/Fed release schedules." I will include:
- **8:30 AM:** Census Bureau releases April new residential construction (housing starts and building permits) — watch if the March starts spike to 1.502 million annualizes or reverses, and whether permits remain soft at 1.363 million.

Is there anything else? Maybe the Federal Reserve's April Treasury International Capital (TIC) data at 4:00 PM? That's less prominent but standard. I'll skip to keep it clean unless I'm confident.

What about the weekly Redbook retail sales index? Not typically in macro briefings.

I'll stick with Housing Starts/Permits.

This week ahead:
Remaining business days after Tuesday:
- Wednesday 5/20
- Thursday 5/21
- Friday 5/22

Typical releases:
- Wednesday: FOMC minutes from April 28-29 meeting (2:00 PM ET). Also possibly Existing Home Sales for April? Actually Existing Home Sales is usually around the 21st-22nd, so Thursday or Friday more likely. Wait, NAR Existing Home Sales is usually the third week, around the 20th-22nd. So Wednesday 5/20 or Thursday 5/21 or Friday 5/22. Let's say Thursday. Or maybe Wednesday.
- Thursday: Weekly jobless claims (May 16 week), Philadelphia Fed Manufacturing Outlook Survey (May), Leading Economic Index (April), Existing Home Sales (April).
- Friday: S&P Global US Manufacturing and Services PMIs (flash for May)? Actually S&P Global flash PMIs are usually around the 20th-24th. In May 2026, Friday May 22 could be the flash PMI day. Or maybe Friday. Also Kansas City Fed Manufacturing Survey? That's usually the last Thursday of the month. So not this week.

Let me think about what makes sense for late May:
- FOMC Minutes: Wednesday May 20 (almost certainly, as it's 3 weeks after April 29).
- Existing Home Sales (April): Thursday May 21 or Friday May 22. NAR usually releases around 10:00 AM on the third Thursday or Friday. Let's say Thursday.
- Philadelphia Fed Manufacturing Survey (May): Thursday May 21 (third Thursday).
- Leading Economic Index (April): Thursday May 21 or Friday May 22. Conference Board usually releases LEI around the third or fourth week, often on Thursdays. Let's say Thursday.
- Weekly Initial Claims (week ended May 16): Thursday May 21, 8:30 AM.
- S&P Global PMIs (May flash): Friday May 22 (if following the schedule where it's around the 20th-24th).

Actually, I should check if any of these are already in the payload:
- UMCSENT in payload is March (53.3). University of Michigan Consumer Sentiment is typically preliminary on the second Friday of the month, final on the fourth Friday. So final May UMich would be Friday May 29. Preliminary was May 8 or 9. Not relevant.
- CFNAI is March. Chicago Fed National Activity Index is usually released around the 20th-24th of the following month. So April CFNAI might be around May 20-24. That could be Thursday or Friday this week.

So for This week ahead:
- **Wednesday 5/20:** FOMC minutes from the April meeting — watch for discussion of tariff pass-through, inflation risk, and the path for the terminal rate.
- **Thursday 5/21:** Weekly initial claims; Philadelphia Fed manufacturing outlook (May); existing home sales (April) — focus on whether the factory floor is stabilizing after the April price spike in Philly Fed prices paid (26.7).
- **Friday 5/22:** S&P Global flash PMIs for May — early read on whether services momentum is holding and if manufacturing output is cracking under tariff uncertainty.

I should also consider if there are any Fed speeches. The Fed watch section asks to note any FOMC speech, minutes, Beige Book, or SEP refresh in the next 5 business days. So I need to check if there are any scheduled speeches. I don't have a calendar of speeches in the payload. I can note the FOMC minutes (Wednesday) since that's in the data/fed schedule. If I don't have speech data, I should not invent it. I can mention the minutes.

Fed watch:
- Target range: 3.50–3.75% (DFEDTARL/DFEDTARU).
- Effective rate (DFF): 3.63%, unchanged from prior.
- SOFR: 3.53%, down 2bp from 3.55%.
- T10Y3M: 1.0, up from 0.93 — yield curve steepening.
- Next 5 business days: FOMC minutes from the April meeting release Wednesday 5/20.

Wait, is there any other Fed event? The Beige Book is usually released two weeks before each FOMC meeting. Next meeting is likely June 16-17, 2026. Beige Book would be around June 3. So not in next 5 days. SEP refresh is only quarterly (March, June, September, December). Next would be June. So not in next 5 days.

For Fed watch, I should also note the HY spread widening (2.83 vs 2.80) and IG unchanged, or the effective rate relative to the target. SOFR at 3.53 is 22bp below the effective rate? Actually EFFR is 3.63, SOFR is 3.53. That's a 10bp spread. Wait, normally SOFR and EFFR are very close. Here SOFR is 10bp below EFFR. That might indicate some funding pressure or just daily noise. But DFF is 3.63, right in the middle of 3.50-3.75. SOFR at 3.53 is near the bottom of the range. That could be worth noting as a subtle easing in overnight repo.

Top of mind:
Need the single most important macro story and what overnight changed it.
Given the data:
- Tariff/Trade policy uncertainty is a major theme (headlines mention Iran talks, Trump's IRS deal, ACA overhaul).
- Supply chain pressures (GSCPI jumped to 19.6 in May from 11.0 in April) — massive spike.
- Inflation data has been firm: CPI, PPI, PCE all rising. Philly Fed prices paid at 26.7. Inflation expectations (MICH) at 3.8%.
- GDPNow tracking 3.99% for Q2, very strong.
- Labor market: claims ticked up to 211k, but payrolls were +115k in April. JOLTS job openings falling (6866 from 6922).
- HY spreads widened slightly (2.83 from 2.80), stocks mixed (DJIA up, SPX/NASDAQ down slightly).

What is the single most important macro story? Probably the intersection of resurgent inflation/supply chain stress and strong growth (GDPNow ~4%). The curve is steepening (T10Y3M to 1.0) and long yields are rising (10y +2bp to 4.61, 30y +2bp to 5.14). The market is pricing in higher inflation risk or stronger growth despite Fed on hold.

What changed overnight? The payload has May 19 data for T10Y3M (1.0 vs 0.93 prior) — steepening continued. Gold is at $4526.97 (up? gold_dd is 0.0, meaning no day-over-day change? Or maybe it's just the value). Oil is stale (May 11) but Brent was at $106.11.

Headlines mention Iran talks (geopolitical/oil risk), Trump's IRS deal ($1.8B), ACA overhaul. But the prompt says "Reference specific numbers from the payload." So I should focus on the data, not headlines.

Top of mind draft:
Supply chain stress and inflation momentum are reasserting faster than the Fed can absorb. The NY Fed’s global supply chain pressure index spiked to 19.6 in May from 11.0 in April, while the Philly Fed prices-paid diffusion index hit 26.7. Despite that, the Atlanta Fed’s GDPNow estimate for Q2 is tracking near 4.0%, and the 10-year Treasury yield added 2 basis points to 4.61% Monday while the 2-year slipped to 4.07%, pushing the 10y–3m spread to 1.0 percentage point. The macro story is a supply-side inflation pulse against resilient demand, leaving the Fed anchored at 3.50–3.75% while markets test the long end.

Wait, T10Y3M is the 10-Year Treasury Constant Maturity Minus 3-Month Treasury Constant Maturity. The latest is 1.0 (May 19) vs 0.93 (May 18). That steepened. I should mention that.

Top of mind (2-4 sentences):
"The re-emergence of supply-side inflation pressure against still-resilient growth is the dominant macro story. The NY Fed’s GSCPI jumped to 19.6 in May from 11.0 in April, the Philly Fed prices-paid index is at 26.7, and headline/core CPI both printed strong in April, yet the Atlanta Fed’s GDPNow estimate for Q2 sits near 4.0%. Overnight, the 10-year Treasury yield rose 2 bp to 4.61% while the 2-year fell to 4.07%, steepening the 10y–3m spread to 1.0 pp, and SOFR drifted down 2 bp to 3.53%. The market is pricing a supply-driven inflation scare with the Fed stuck on hold."

Check sentence count: 3 sentences. Good.
Specific numbers: GSCPI 19.6 vs 11.0, Philly Fed 26.7, GDPNow ~4.0%, 10y 4.61%, 2y 4.07%, 10y-3m 1.0, SOFR 3.53%. All from payload.

Yesterday's releases (May 18):
Only ICSA has data. But wait, the payload lists three releases. If I only include one, is that okay? The user said "Bulleted list of indicators released on the prior business day." The payload says these were FRED-confirmed releases. It doesn't say I have values for all of them. But the format says "value (vs. prior or vs. consensus)". Since I only have ICSA, I'll list that one. Actually, I can check if GACDISA066MSFRBNY or GACDFSA066MSFRBPHI correspond to Business Leaders Survey. GACDISA066MSFRBNY is the NY Fed GSCPI. GACDFSA066MSFRBPHI is Philly Fed prices paid. Neither is the Business Leaders Survey. Quarterly Retail E-Commerce Sales doesn't match any FRED code in the dict.

So I'll only list:
- **State Unemployment Insurance Weekly Claims (week ended May 9):** 211k (vs. 199k prior) — a 12k increase that nudges the series off cycle lows but keeps layoff activity muted.

That's one bullet. Is that enough? The user said "Bulleted list". One bullet is a list. I'll keep it tight.

Wait, is there any chance that the "Business Leaders Survey" is the NY Fed Empire State? The Empire State Manufacturing Survey is sometimes called the Business Leaders Survey? Actually no, the NY Fed has a separate "Business Leaders Survey" for the service sector, released quarterly? Or monthly? It's a monthly survey of service firms in the New York Fed's district. I don't have its value. So I'll omit.

Today's calendar (May 19, ET):
- **8:30 AM:** April housing starts and building permits (Census Bureau) — watch whether the March jump in starts to 1.502 million annualized holds or if the permits decline to 1.363 million signals fading forward supply.

Any other releases today?
April New Residential Construction is the standard release. It includes housing starts and building permits. It is typically released at 8:30 AM ET.

I could add:
- **9:00 AM:** S&P/Case-Shiller Home Price Indices for March? Actually Case-Shiller is released on the last Tuesday of the month. May 26 would be the last Tuesday. So not today.

- **10:00 AM:** May NAHB Housing Market Index? Actually NAHB is usually the third Tuesday or Wednesday? Wait, NAHB/Wells Fargo Housing Market Index is typically released on the third Tuesday of the month, often at 10:00 AM. So today (May 19, third Tuesday) could be the NAHB release. The payload has March housing data, but NAHB is a monthly survey. It's plausible. But I'm less certain. I'll stick with Housing Starts/Permits which I'm confident about.

Actually, the third Tuesday of May is indeed the 19th. NAHB is released on the third Tuesday. So:
- **10:00 AM:** NAHB/Wells Fargo Housing Market Index for May — watch if builder confidence is eroding under higher mortgage rates and input cost volatility.

But do I have mortgage rate data in the payload? No. But it's a standard release. However, I'm less certain about the exact date. Given the instruction to infer, I can include it if it's highly typical. But to be safe and concise, maybe just Housing Starts/Permits. Or include both.

Let me reconsider. The prompt says "Bulleted list of what's releasing today". If I'm wrong about the exact release, that's bad. But the prompt explicitly asks me to infer from typical schedules.

Standard Census release calendar for New Residential Construction (Housing Starts and Building Permits):
Usually released around the 16th-18th of the month. If May 16 was Saturday, it would be Friday May 15 or Tuesday May 19. Since May 16 is Saturday in 2026? Let's check: May 1, 2026 is a Friday. So May 2 is Saturday. May 16 is indeed a Saturday. So the release would be Friday May 15 or Tuesday May 19. The payload shows no April housing data (only March), so it's very likely releasing today (May 19) since it wasn't released Friday (maybe due to a lag). Actually, Census often releases on the day if the scheduled day is a weekend? No, they usually release on the next business day. But if the schedule is third week Tuesday, it could be today.

Given the payload has March housing data as the latest, and today is May 19, April housing data is definitely due.

I'll include:
- **8:30 AM:** April housing starts and building permits — watch if the March starts surge to 1.502m annualized holds or reverses, and whether permits remain constrained at 1.363m.
- **10:00 AM:** May NAHB/Wells Fargo Housing Market Index — early read on builder sentiment and forward-looking buyer traffic.

Is there a FOMC speaker today? I don't know. The Fed watch section covers speeches.

This week ahead:
- **Wednesday 5/20:** FOMC minutes from the April 28–29 meeting (2

## Markets close
| | Level | d/d | w/w |
|---|---|---|---|
| UST 2y | 4.07 | -0.02 | +0.12 |
| UST 10y | 4.61 | +0.02 | +0.19 |
| UST 30y | 5.14 | +0.02 | +0.16 |
| 3m10y | 1.00 | +0.07 | +0.24 |
| SOFR | 3.53 | -0.02 | -0.07 |
| Eff. fed funds | 3.63 | +0.00% | +0.00% |
| S&P 500 | 7,403.05 | -0.07% | -0.13% |
| Dow Jones | 49,686.12 | +0.32% | -0.04% |
| NASDAQ Comp. | 26,090.73 | -0.51% | -0.70% |
| WTI | $101.56 | +2.72% | -7.47% |
| Brent | $106.11 | +2.54% | -10.27% |
| Gold (spot) | $4,526.97 | +0.00% | — |
| Silver (spot) | $76.38 | +0.00% | — |
| Broad USD (DTWEXBGS)* | 119.28 | +0.52% | +1.05% |
| HY OAS | 3 bp | +3 bp | +4 bp |
| IG OAS | 1 bp | +0 bp | -3 bp |

*DTWEXBGS publishes with ~1-week lag. Gold/silver from metalpriceapi.com.*

## Overnight headlines
- **Tuesday briefing: Iran talks; San Diego shooting; Trump’s IRS deal; ‘forever chemicals’; better sleep; and more** — *The Washington Post*
- **Trump’s New $1.8 Billion Pot of Money, and a Deadly Mosque Attack in California** — *The New York Times*
- **What Trump’s ACA overhaul means** — *The Washington Post*
- **Big Tech Is Cutting Back on Buybacks. Nvidia Could Be the Exception.** — *WSJ*
- **Jim Cramer's top 10 things to watch in the stock market Tuesday** — *CNBC*
- **Post Market Wrap: May 18, 2026** — *CNBC*

---
*Sources: FRED; metalpriceapi.com; Tavily; Moonshot Kimi. Data current as of 2026-05-19.*
