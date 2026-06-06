# My terminal caught my agency going dark for 3 weeks. They thought no one was watching.
**Angle:** automation · **Leverage:** high · **Proof:** FB Agent runs a live read-only audit — curl+jq against the ad account, a report with red-flag rows, a "Questions for the agency" footer, and three weeks of blackout zeros it surfaced on its own.
**Hook (0-3s):** "Every founder's quiet dread: is my budget evaporating while I'm not looking? So I built the thing that watches the watchers."

## 🎬 REEL CUT (9:16, 25-40s)
**On-screen text (open):** IT WENT DARK FOR 3 WEEKS. NOBODY TOLD ME.
**Beat 1 — Hook (0-3s):** "Every founder's quiet dread — is my ad budget evaporating while I'm not looking?" · *Show:* Sahil to camera, then hard cut to a dark terminal cursor blinking.
**Beat 2 — Tension (3-10s):** "I wasn't going to log into the dashboard every morning and trust a spreadsheet someone else fills in. So I built the thing that watches the watchers." · *Show:* type one command, terminal fires a live `curl ... | jq` against the ad account — rows streaming in.
**Beat 3 — Proof (10-25s):** "Read-only. The credential never touches Claude's context — it can see the money, it structurally can't spend it. And the first time it ran, it didn't hand me a green checkmark. It handed me red rows. Three weeks. Spend, zero. Zero. Zero." · *Show:* scroll the report — red-flag rows, then the blackout: a column of 0.00 / 0.00 / 0.00 across three weeks. Cursor parks on the zeros.
**Beat 4 — Turn (25-32s):** "No CRM. No analyst on retainer. A folder of text files that audits my agency every morning — and writes the questions I should be asking them." · *Show:* scroll to the report footer: "Questions for the agency:" with itemized lines.
**CTA (32-40s):** "If you run ads and you're trusting someone else's screenshot — DM me 'AUTOMATE.' I build these in public. Yours could be next." · *On-screen card:* DM 'AUTOMATE' · build-in-public
**Caption:** It caught a 3-week blackout my agency never mentioned. Read-only terminal, runs every morning, writes the questions for me. DM 'AUTOMATE' to follow the build. #buildinpublic #aiagents #claudecode #founders #paidads #automation

## 💼 LINKEDIN CUT
**Hook line:** My agency went dark for three weeks. Nobody told me. My terminal did.
**Body:**
I never wanted to be the founder refreshing the ads dashboard at 7am, half-trusting a spreadsheet someone else fills in. So I built an agent that audits the account for me — every morning, before I even sit down.

It's blunt by design. One command, and it runs a live read-only pull against the ad account — `curl` straight to the source, `jq` to shape it. Read-only is the whole point: the credential never enters the model's context. It can see exactly where the money is going. It structurally cannot move a dollar. The AI proposes the questions. I dispose.

The first time it ran, it didn't congratulate me. It handed me a report with red-flag rows — and a stretch of zeros. Spend, zero. Zero. Zero. Three weeks of blackout I'd have caught eventually, on a dashboard, after the budget was already gone. The agent caught it cold and parked the cursor right on it.

And it doesn't stop at flagging. The report ends with a footer titled "Questions for the agency" — itemized, specific, the exact things I should be walking into that call asking. No CRM. No analyst on retainer. A folder of text files that watches the people I'm paying to watch my money.

This is what I mean by leverage. I'm not working harder on my ads. I built the thing that audits them for me — and it doesn't have a reason to look away.

**CTA:** If you run paid spend through an agency and you're trusting their screenshots, DM me 'AUTOMATE.' I build these in public — yours could be the next one I run on camera.

## 🎯 Impact unlocked from Sahil
- Screen-record the live run: type the single command, let the `curl ... | jq` stream rows into the terminal in real time (input → output in one unbroken take).
- Capture the report with the three-week blackout visible — a clean column of 0.00 zeros — plus at least one red-flag row, and park the cursor on the zeros for the freeze frame.
- Scroll to the "Questions for the agency:" footer so the itemized lines are readable on screen — that's the moment that turns a flag into leverage.
- Optional but strong: a half-second of the read-only guardrail being true on screen (e.g. the agent can list spend but has no write path / credential not in context) to back the "can see it, can't spend it" line with a receipt.