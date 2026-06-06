# TEST REEL — Higgsfield channel validation

**Script:** `scripts/4-bigticket/02 — I built a factory that builds factories`
**Goal:** prove the Soul-ID pipeline end-to-end on ONE reel before any batch use — generate face-locked cinematic Sahil b-roll to intercut with his real terminal footage, validate the hardest motion shot, reconcile spend. **This is the test + review Sahil asked for.**

**Why this script:** highest cinematic payoff and brand-defining. The terminal proof (council playbook, `runs.jsonl`) Sahil screen-records himself; Higgsfield supplies the **cinematic connective b-roll** that makes it feel like a film, not a screencast.

---

## Prereq (Sahil supplies)
- `SOUL_UUID` = Sahil's Soul reference id (from the reel-factory setup). Paste it where marked.
- Confirm balance: `higgsfield account status`

## Step 1 — Cost estimate FIRST (free, no spend)
```
higgsfield generate cost text2image_soul_v2 --aspect_ratio 9:16 --quality 2k     # ~0.12 cr each × 4 stills
higgsfield generate cost kling3_0 --mode pro --duration 5 --aspect_ratio 9:16    # ~8.75 cr (motion test only)
```
Expected board cost ≈ **0.5 cr stills + 8.75 cr one motion clip ≈ ~9.3 cr** for the full test. Confirm against balance before proceeding.

## Step 2 — Cheap-still board (4 stills, Soul ID, ~0.12 cr each) — DO THIS FIRST
One still per beat. Lock the look here before ANY video.

1. **Hero / cold-open** — *"the operator."* Sahil, face-locked, lit like a founder portrait, dark room, single screen glow on his face, calm and three-moves-ahead.
2. **Command center** — wide-ish, Sahil at a terminal in a minimal high-end workspace; the room reads as a control room, not a desk.
3. **Factory-of-factories visual** — stylized: identical glowing "factory" modules receding into depth, one assembling another (the metaphor as a single striking frame). `soul_cinematic` ok here (no face needed).
4. **Turn-to-camera** — Sahil mid-turn toward lens, slight earned smirk — the Beat-4 "it gets smarter every run" payoff frame.

```
higgsfield generate create text2image_soul_v2 --prompt "<beat-1 scene + explicit feature description of Sahil>" --aspect_ratio 9:16 --quality 2k --custom_reference_id <SOUL_UUID> --wait
# repeat for beats 2 and 4 (face-locked).
higgsfield generate create soul_cinematic --prompt "<beat-3 factory-of-factories, no face>" --aspect_ratio 9:16 --quality 2k --wait
```

### ⛔ REVIEW GATE 1 — Sahil reviews the 4 stills
Does the look hold? Is the face unmistakably Sahil and never creepy? Is the factory frame striking? **No video until this is a yes.**

## Step 3 — Animate the HARDEST motion shot first (one clip, ~8.75 cr)
The hardest motion here = **the turn-to-camera (beat 4)** — human facial motion is where image→video breaks. Animate THAT one first, not an easy push-in.
```
higgsfield generate create kling3_0 --mode pro --duration 5 --aspect_ratio 9:16 --sound off --start-image <beat-4-still-path-or-uuid> --wait
```

### ⛔ REVIEW GATE 2 — Sahil reviews the motion + the running cost
Does the turn read as real, or does the face warp? Judge motion as harshly as the stills.
- **Pass** → proceed to animate the remaining beats, then Sahil lays his **real VO** over the cut and intercuts the live terminal footage.
- **Fail** → do NOT spend more on `kling3_0`. Switch toolchain (`seedance_2_0` / `veo_3_1`, or start+end-frame interpolation), or restyle to a slow push-in that hides facial motion. A passing still ≠ a passing clip.

## Step 4 — Reconcile
```
higgsfield account transactions --size 10
```
Log actual spend in `invoice.md` here. Deleting files does not refund credits — decide before rendering, not after.

---

## Verdict log (Sahil fills in)
- [ ] Stills look-locked (Gate 1): ____
- [ ] Motion holds at bar (Gate 2): ____
- [ ] Final spend vs estimate: ____
- **Channel decision:** ☐ promote Higgsfield to a standing channel  ☐ needs toolchain change  ☐ shelve for now
