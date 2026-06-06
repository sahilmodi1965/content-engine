# An AI that can see all my ad money — and structurally can't spend a cent
**Angle:** automation · **Leverage:** high · **Proof:** `pull-metrics.sh` pulling live ROAS into a report Claude reads, the credential-safety line in the README, and the AI diagnosing a 100x gap in revenue-per-user — all without the token ever entering its context.
**Hook (0-3s):** My AI reads my real ad revenue every morning — and it physically cannot spend or leak a single dollar of it.

## 🎬 REEL CUT (9:16, 25-40s)
**On-screen text (open):** IT SEES THE MONEY. IT CAN'T TOUCH IT.
**Beat 1 — Hook (0-3s):** "My AI reads my real ad-network revenue — and structurally it cannot spend or leak a cent of it." · *Show:* Terminal full-screen, cursor blinking, type one command.
**Beat 2 — Tension (3-10s):** "Most people paste their ad account creds straight into the chat. You just handed the model the keys to your money. I don't. The credential never enters Claude's context." · *Show:* Run `./pull-metrics.sh` — rows of live ROAS data scroll in.
**Beat 3 — Proof (10-25s):** "The script pulls the numbers. Claude only ever sees the report — never the token. Then it reads it back to me." `cat roas-report.md` → AI diagnosis on screen: one cohort earning ~100x more revenue per user than another. · *Show:* `cat roas-report.md`, then highlight the README line: *"the credential never enters Claude's context."*
**Beat 4 — Turn (25-32s):** "So it can see every dollar coming in, tell me exactly where I'm leaving money on the table — and it's structurally incapable of moving a cent. The AI proposes. I dispose." · *Show:* Split: the 100x diagnosis line + the read-only README guardrail line side by side.
**CTA (32-40s):** "If you run ads and you're still eyeballing this in a dashboard by hand — DM me 'AUTOMATE.' I build these in public." · *On-screen card:* DM 'AUTOMATE' · build-in-public
**Caption:** It reads my real ad revenue and is structurally incapable of spending or leaking it. The token never touches its context. DM 'AUTOMATE' to follow the build. #buildinpublic #aiagents #claudecode #roas #marketingautomation #founders

## 💼 LINKEDIN CUT
**Hook line:** I gave an AI read access to my real ad-network revenue. By design, it cannot spend or leak a single dollar of it.

**Body:**
Most operators do the dangerous thing without thinking: paste the ad-account credential straight into the chat window. The moment you do that, the model — and whatever it's connected to — has the keys to your money.

I built it the other way around. A small script, `pull-metrics.sh`, authenticates and pulls the live ROAS numbers into a plain report. Claude only ever reads the report. The credential never enters its context. That one line is in the README, and it's the whole trust model: the AI can see every dollar coming in, and is structurally incapable of moving one.

Then it earns its keep. This morning it read the report back to me and flagged that one cohort was generating on the order of 100x the revenue per user of another — the kind of gap that's invisible when you're scrolling a dashboard by hand, obvious when something reads every row for you every day.

No new SaaS. No giving away credentials. Just a folder of text files and a guardrail that means the worst case is "it read a number," never "it spent my budget." The AI proposes. I dispose.

**CTA:** If you run paid acquisition and you're still reading these tables by hand, DM me 'AUTOMATE.' I build these in public — yours could be the next one I show.

## 🎯 Impact unlocked from Sahil
- Screen-record the single command run: `./pull-metrics.sh` executing and live ROAS rows scrolling in (blur any account IDs / real revenue figures you don't want public, but keep the structure visible).
- Capture `cat roas-report.md` showing the AI's written diagnosis — specifically the line naming the ~100x revenue-per-user gap between cohorts.
- Frame-grab the README line verbatim: "the credential never enters Claude's context" (or the exact read-only / safety wording you use) — this is the trust flex and must be legible on screen.