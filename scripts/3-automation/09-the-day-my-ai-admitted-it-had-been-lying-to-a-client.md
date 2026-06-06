# The day my AI admitted it had been lying to a client
**Angle:** automation · **Leverage:** high · **Sells via:** the owner who's been burned by automation that sounds confident and is wrong — this is trust built into the code, not promised in a pitch.
**Receipt:** shikshalokam — the brain kept telling a nonprofit's comms lead her invitations were "live in 60 seconds" while the page never moved. Root cause: a hand-copied mirror that drifted from the real page. The fix: faithfulness_gate.py, which refuses to publish unless every prior timeline entry survives — it exits with an error and blocks the merge. The system is now physically incapable of saying "published" unless the page can prove it.
**Hook (0-3s):** "My AI kept telling a client her page was live. It wasn't. So I made it physically incapable of lying."

## 🎬 REEL CUT (9:16, ~35s)
| Sec | On-screen text | What you say (VO) | What we show |
|-----|----------------|-------------------|--------------|
| 0–3 | IT KEPT SAYING "LIVE." IT WASN'T. | "My AI kept telling a client her page was live. It wasn't. Every time." | Sahil to camera, then the AI's confident "live in 60 seconds" message. |
| 3–12 | confident and wrong | "It said 'live in 60 seconds,' over and over, while the actual page never moved. A copy had drifted from the real thing — and the AI didn't know the difference." | The message next to the page that didn't change. |
| 12–22 | so I built a gate | "Confidence isn't proof. So I built a faithfulness gate. Before anything publishes, it checks the live page against what it claims — and if a single fact doesn't survive, it refuses." | faithfulness_gate.py running; a failed check exiting with an error. |
| 22–30 | it can't say "published" unless it's true | "Now it is physically incapable of saying 'published' unless the page can prove it. The gate blocks the merge. The lie can't ship." | The blocked merge; then a clean PASS with the page actually updated. |
| CTA 28–35 | DM "AUTOMATE" / "BUILD" | "If you've been burned by automation that sounds sure and is wrong, DM me 'BUILD.'" | DM card. |

**Caption:** My AI kept telling a client her page was live. It wasn't. So I built a gate that makes it physically incapable of saying "published" unless the live page can prove it. If a single fact doesn't survive, the merge is blocked — the lie can't ship. Trust built into the code, not promised. DM "BUILD." #buildinpublic #aiagents #founders #automation #trust #aisafety

## 💼 LINKEDIN CUT
**Hook line:** My AI kept telling a client her page was live. It wasn't. So I made it physically incapable of lying.
**Body:**
Here's the failure nobody markets: my system kept telling a nonprofit's comms lead her invitations were "live in 60 seconds." Confident, repeated, and wrong. A copy of the page had drifted from the real one, and the AI was reporting on the copy. It had no idea it was lying.

You can't fix that with a better prompt. A more eloquent model just lies more smoothly. So I fixed it structurally. I built a faithfulness gate: before anything publishes, it checks the live page against every claim the system is about to make. If a single prior fact doesn't survive the check, the gate exits with an error and blocks the merge.

The result is that the system is now physically incapable of saying "published" unless the published page can prove it. Not "we try to be accurate." Cannot ship the lie. The trust isn't a promise in my pitch — it's enforced in the code.

This is the anti-bullshit flex, and I think it's the most important thing about putting AI in front of your customers. Confidence is cheap. Make the truth a precondition for shipping.

**CTA:** If you've been burned by automation that sounds certain and turns out wrong, DM me "BUILD." I build these in public — trust by construction, not by promise.

## 🎯 Shoot notes (what only Sahil can capture)
- Show the AI's confident "live in 60 seconds" message next to the page that visibly didn't change — the lie has to be felt.
- Capture faithfulness_gate.py failing a check and exiting with an error that blocks the merge — that's the receipt for "can't ship the lie."
- Then a clean PASS with the page actually updated, so the viewer sees the gate let truth through.
