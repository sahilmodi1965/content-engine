# My AI can see all my ad money and structurally cannot spend a cent
**Angle:** automation · **Leverage:** high · **Sells via:** the owner who wants AI on their numbers but won't hand it the keys — this is how you get the report without the risk.
**Receipt:** scripts/metrics — pulls AdMob revenue, Google Ads spend, and GA4→BigQuery engagement into one ROAS report. README: "The credential value never enters Claude's context window." .claude/settings.json denies the key files. The report surfaced the real diagnosis: install cost great, ad earnings catastrophic, a 100x revenue-per-user gap.
**Hook (0-3s):** "I let an AI read every dollar of my ad revenue. It still has never once seen my passwords."

## 🎬 REEL CUT (9:16, ~35s)
| Sec | On-screen text | What you say (VO) | What we show |
|-----|----------------|-------------------|--------------|
| 0–3 | IT SEES THE MONEY. NOT THE KEYS. | "I let an AI read every dollar of my revenue. It's never once seen my passwords." | Sahil to camera, then the ROAS report fills the screen. |
| 3–12 | revenue + spend + engagement, one report | "It pulls ad revenue, ad spend, and engagement into one report. Every morning I get the real ROAS, not three dashboards I have to mentally staple together." | Run the pull; the ROAS table renders. |
| 12–22 | the credential never enters its context | "Here's the part that matters. The keys live in a file the AI is denied from reading. It can see the money. It structurally cannot touch the account." | Show the README line + the settings file denying the key paths. |
| 22–30 | it told me the truth | "First report wasn't flattering. Cheap installs, but the ad earnings were a disaster — a hundred-x gap in what each user was worth. I'd have never seen it across separate tools." | Cursor on the diagnosis row. |
| CTA 30–35 | DM "AUTOMATE" / "BUILD" | "Want AI on your numbers without handing it the keys? DM me 'AUTOMATE.'" | DM card. |

**Caption:** I let an AI read every dollar of my ad revenue. It has never seen a single password. The credential lives in a file it's denied from reading — it can see the money, it structurally can't spend it. That's how you put AI on your numbers safely. DM "AUTOMATE." #buildinpublic #aiagents #founders #paidads #automation #dataprivacy

## 💼 LINKEDIN CUT
**Hook line:** I let an AI read every dollar of my ad revenue. It has never once seen my passwords.
**Body:**
Every owner I talk to wants AI on their numbers, and every one of them hesitates at the same place: I'm not pasting my API keys into a chatbot.

You don't have to. I built a pipeline that pulls ad revenue, ad spend, and engagement into one ROAS report — and the credentials live in a file the model is explicitly denied from reading. The AI sees the output. It never sees the secret. It can read where every dollar goes and it structurally cannot move one.

The first report it produced wasn't flattering, which is exactly why I trust it. Cheap installs, but the earnings per user were catastrophic — a 100x gap I'd never have spotted with the numbers spread across three separate dashboards.

Guardrails aren't the boring part of this. They're the whole reason it's safe to run on a real business. The AI proposes the read. It can't perform the write.

**CTA:** If you want AI working your numbers without handing it the keys, DM me "AUTOMATE." I build these in public — credential-safe by construction.

## 🎯 Shoot notes (what only Sahil can capture)
- Run the metrics pull and cat the ROAS report so revenue/spend/engagement land in one table on screen.
- Show the README line "the credential never enters Claude's context" next to the settings file that denies the key paths — the guardrail has to be visibly real.
- Park the cursor on the diagnosis row (cheap installs vs catastrophic earnings) so the "it told me the truth" beat has a receipt.
