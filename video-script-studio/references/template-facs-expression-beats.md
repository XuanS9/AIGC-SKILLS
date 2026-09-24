# Template: FACS Expression-Beat Schedule

Paste-ready Seedance 2.0 prompt template for close-up facial acting driven by
**FACS Action Unit codes** — one AU set per beat. Full method, the AU reference
table, and the emotion→AU recipes live in
`higgsfield-facs.md`.

## When to use this template

Close-up shots where the *face* is the content — monologue, dialogue, a forced
smile, a mixed/uncanny expression, an emotion arc across a single continuous
take. Not for shots where blocking or whole-body action dominates (use
`template-single-character-position.md` for those).

> **Plan first.** Follow [shared narrative planning](narrative-planning.md):
> identify the stimulus, realization, or expression-state change and its visible
> response before allocating time. No preset beat count or equal-time schedule.
> Keep AU sets sparse: stacking more AUs degrades accuracy. The original 3–4-beat
> guidance is a per-generation complexity ceiling, not a target or minimum;
> use fewer beats when sufficient and split an overloaded performance at a
> meaningful boundary, preserving dialogue and expression continuity. See
> `higgsfield-facs` § The Plan-First Workflow.

The eight planning layers — assets, goal, global audiovisual/space, behavior,
stages, continuity, final frame, constraints — are semantic checks. Map them into
this AU schedule, identity, mood, dialogue, and camera fields; keep the continuous
close-up format. Record the starting expression and intended final expression/gaze.

## Prompt template

```
**Model:** Seedance 2.0
**Aspect ratio:** [1:1 / 16:9 / 9:16]   **Duration:** [Ns]

[Use the provided character @Image1 as the fixed identity reference. — optional,
 only for identity consistency; codes work without an image]

**Style & Mood:** [framing — tight close-up, face + shoulders], [lighting],
[background], shallow depth of field, [mood].

[Optional dialogue — generates speech + automatic lip-sync, see higgsfield-audio
 § Audio as a Conditioning Input:
 [AUDIO: 0s] "[the spoken line]"]

Beat [n] ([start-end seconds, allocated after planning]): [trigger and inherited expression]
→ [AU codes] ([optional short anatomical description]) → [visible response / end state]
[— delivers "<line>"]
[Repeat only for necessary expression changes; respect the per-generation complexity ceiling.]
Final expression and gaze: [state held into the final frame or next clip].

[One-line mood / subtext — e.g. "the face never fully commits to either; the
 audience reads both at once."]

**Camera:** [one dominant move — slow push-in / static medium close-up]
```

## What goes in each field

- **AU codes** — from `higgsfield-facs.md` § AU Code Reference.
  Specify **codes-only** (`AU12`) for terse beat lists, or **codes + short
  anatomical description** for any unit the model keeps dropping — test both.
- **Emotion → AUs** — for "which code for anger/fear/sadness," see
  `higgsfield-facs` § Emotion → AU Recipes (Duchenne smile = AU6+AU12, sadness =
  AU1+AU4+AU15, etc.). Blend two emotions' AUs in one beat for mixed expressions.
- **Beats are expression changes within a continuous close-up, not cuts.** Keep
  the camera move singular so Seedance doesn't read the schedule as a shot list.
  Beat time ranges must continuously cover **Duration**, including transitions
  and readable holds (`higgsfield-seedance` § Runtime arithmetic). Allocate time
  after the expression/semantic arc is clear; protect complete spoken phrases
  and use the actual audio timing when available. The `[AUDIO: 0s]` anchor above
  is illustrative; place it at the line's actual onset.
- **Dialogue beats** — the `[AUDIO: Xs]` block drives lip/jaw phoneme shaping;
  reserve your explicit AU schedule for the expressive brow/eye/cheek muscles
  around the words.

## See also

- `higgsfield-facs.md` — full FACS method, AU table, emotion
  recipes, worked examples, the not-a-guarantee provenance rule
- `higgsfield-audio.md` § Audio as a Conditioning Input —
  `[AUDIO: Xs]` dialogue + lip-sync
- `higgsfield-soul.md` § Micro-Expressions — named expressions
  that decompose to AU combos
- `template-single-character-position.md` (sibling template) — when blocking, not the
  face, is the content
