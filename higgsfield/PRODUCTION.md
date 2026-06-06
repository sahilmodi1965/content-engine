# Higgsfield Production Channel — Soul ID reels

> This turns a banked script into a high-quality AI reel using Sahil's **Soul ID** (face-locked) with his **real VO** over the top — "clipper vibes." It spends real credits, so it runs behind a hard gate. The CLI is already wired and proven in `~/stratos-reel-factory`; the operational facts and scar-tissue below come from that studio's memory.

## The CLI (proven facts — run foreground)

- **Balance / ledger (truth):** `higgsfield account status` · `higgsfield account transactions --size N`
- **Cost first, always:** `higgsfield generate cost <model> ...` — estimate spend for free *before* committing.
- **Face-locked still (~0.12 cr):**
  `higgsfield generate create text2image_soul_v2 --prompt "<scene + explicit feature description>" --aspect_ratio 9:16 --quality 2k --custom_reference_id <SOUL_UUID> --wait`
  - `custom_reference_id` takes the **bare Soul UUID string** (not JSON).
  - `text2image_soul_v2` for identity-locked shots; `soul_cinematic` renders wardrobe/action best but under-weights the face (use for masked/wide/action shots).
- **Video (~8.75 cr / 5s):**
  `higgsfield generate create kling3_0 --mode pro --duration 5 --aspect_ratio 9:16 --sound off --start-image <path|uuid> --wait`
  - Model id is `kling3_0` (not `kling3_0_pro`); `--mode pro`.
- **No ffmpeg/ImageMagick on this machine.** Pillow (PIL 11.3) is available for building still-boards.

## The spend-gate (LAW — this is the "test + review" Sahil asked for)

Sahil is a demanding client who judges hard and tracks spend. Three scars, encoded as gates:

1. **Lock the look on cheap stills before any video.** Deliver a single visual board — one ~0.12 cr still per beat — and get the look approved BEFORE spending ~8.75 on a clip. *(Scar: shot an 8.75 cr video before the bar was raised; superseded; wasted.)*
2. **Validate the hardest MOTION shot first.** A passing still ≠ a passing clip. Animate the single hardest action shot first and judge motion as harshly as stills. If it can't hit bar, change the toolchain (`seedance_2_0` / `veo_3_1`, start+end-frame interpolation) or restyle to hide the weakness — don't spend big to find out last. *(Scar: web-slinger reel — stills were strong, the animated swing physics read as fake, the client killed all ~95 credits of content.)*
3. **Deleting files does not refund credits.** Reconcile every render against `higgsfield account status`. Keep a running invoice.

**Therefore the channel NEVER batch-renders.** Sequence for any reel:
`pick script → cheap-still storyboard (Soul ID) → STOP, Sahil reviews look → animate hardest shot → STOP, Sahil reviews motion + cost estimate → only then render remaining clips → VO over top → reconcile spend.`

## Voice

- **Test phase:** Sahil's **real recorded VO** over Soul-ID visuals. On-brand, zero risk, fastest path to a shippable reel.
- **Later upgrade (not in the first test):** voice-clone for fully-generated narration. Flagged, not enabled.

## What's Higgsfield-fit (and what isn't)

AI b-roll wins for **cinematic / conceptual / flex** scripts — the "factory that builds factories," the command-center, the swarm. It LOSES for scripts whose proof is a **real screen-recording or live URL** (most PDF scripts) — those must be shot for real, because the receipt is the point. See `ready-for-soul.md` for the per-script tags.

## Output location

Boards and renders for a given reel live under `higgsfield/<script-slug>/` (stills/, clips/, invoice.md). The first one is staged in `test-reel/`.
