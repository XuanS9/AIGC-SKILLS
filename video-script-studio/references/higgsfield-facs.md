# Higgsfield FACS Director

Use the authoritative [shared director planning](narrative-planning.md) for full format and the character's event/response arc. AU codes are optional; AU beats, shot cuts and generation clips are distinct. Treat expression/AU counts below as complexity heuristics and derive timing from the actual performance. Preserve pre/during/post-line continuity without fixed pauses. Carry expression, gaze, breath and body state across cuts and extension joins.

Direct a face the way an animator does — by **muscle**, not by mood. FACS (the
Facial Action Coding System) names each facial movement as an **Action Unit**:
`AU12` is the lip-corner puller (smile), `AU6` is the cheek raiser, `AU4` is the
brow lowerer. These codes can request the corresponding action in a Seedance 2.0
prompt, with empirical and variable adherence. They offer optional vocabulary for
forced smiles, uncanny faces, mixed emotions and close-up dialogue; plain visible
behavior remains valid, and neither precise execution nor a close-up is required.

> **This skill is a facial-control layer on top of `higgsfield-seedance.md`.**
> Every FACS prompt is still a Seedance prompt — six-slot formula, Prompt-Craft
> Laws, preflight linter. FACS only changes *how you specify the face*: AU codes
> instead of (or alongside) emotion words. It is the muscle-level case of the
> Voice Rewrite rule "describe physics, not emotion."

## QUICK FACTS
*Routing aids — read the linked sections for the actual rules.*
- FACS = facial expressions as **Action Unit codes** (muscle movements), not emotion labels; you write the codes into the prompt [→](#what-facs-is)
- **Provenance split:** the AU vocabulary is standard human science; Seedance's *interpretation* of codes in a prompt is **[EMPIRICAL]** — high success rate, **not a guarantee** [→](#provenance-and-the-not-a-guarantee-rule)
- **Plan first.** Decide the expressions the performance needs (within the per-generation complexity guidance below) → generate a FACS sheet for *only those* → write the codes. Generating the full 49-AU sheet and cherry-picking is the anti-pattern [→](#the-plan-first-workflow)
- **3–4 expressions is an optional complexity starting point.** Diagnose AU overload without capping the full performance [→](#step-2--put-au-codes-in-the-seedance-prompt)
- Two specification styles — **codes-only** (`AU12`) vs **codes + short anatomical description**; test both, neither is universally better [→](#step-2--put-au-codes-in-the-seedance-prompt)
- The reference sheet is a **labelled-grid image** (GPT Image 2 / Nano Banana Pro); the LLM can **mislabel AUs**, so iterate and verify [→](#step-1--generate-the-facs-reference-sheet)
- The character photo is **optional** — codes work without it; attach it only for identity consistency [→](#step-2--put-au-codes-in-the-seedance-prompt)
- Common emotions decompose to standard AU recipes (Duchenne smile = AU6+AU12; sadness = AU1+AU4+AU15) [→](#emotion--au-recipes)
- The payoff is **dialogue / monologue**: optional AU schedules with `[AUDIO: Xs]`; preserve pre / during / post-line continuity without mandatory gestures or pauses [→](#dialogue--monologue-facial-acting)
- [OFFICIAL] Body micro-beat menu (throat, breath, skin, posture); stagger reactions by perception, with 0.3–0.5s only an example; keep listeners alive at readable scale [→](#physical-micro-beats--the-body-beyond-the-face)

---

## What FACS Is

The Facial Action Coding System (Ekman & Friesen) breaks the face into
**Action Units** — the smallest visually distinguishable muscle movements.
Instead of asking for "happy" (which the model samples diffusely across an
enormous range of footage), you ask for the muscles that *produce* the
expression:

- `AU6` — cheek raiser (orbicularis oculi tightens, crow's feet appear)
- `AU12` — lip-corner puller (zygomaticus major pulls the corners up and out)
- Together, `AU6 + AU12` = a **Duchenne smile** (the genuine, eyes-involved one)

A smile that uses only `AU12` reads as *polite/forced* — the eyes don't
participate. That distinction is invisible to "smile" as a prompt word and
trivial to specify in FACS. This is why it's the tool for **forced smiles,
suppressed expressions, mixed emotions, and the uncanny** — the cases where the
*difference between two similar expressions* carries the meaning.

FACS is used by professional facial animators in film; here it is repurposed as
a **prompt vocabulary** for Seedance 2.0.

### Where it sits among the repo's facial tools

Three layers, increasing resolution:

| Layer | Surface | Granularity |
|---|---|---|
| Named expression | `higgsfield-soul.md` § Micro-Expressions (Suppressed Smile, Cold Calculation…) | A whole emotion in one label |
| Behavior channel | `vocab.md` § Emotion as Visible Behavior — Channels (breath, jaw tension, eye behavior…) | Emotion → observable behavior |
| **Action Unit (this skill)** | AU codes | Emotion → **named muscle** |

The channels are the *behavioral* substrate; AUs are the *anatomical* substrate.
A named expression like "Quiet Devastation" = a channel mix (glassy eyes + tight
jaw) = an AU combo (AU1 + AU15 + AU17 + AU24). Reach for FACS when a named
expression is too coarse and you need the specific muscles.

---

## Provenance and the "Not a Guarantee" Rule

Two different kinds of claim live in this skill — keep them apart:

- **The AU vocabulary is standard science.** Which code means which muscle, and
  the classic emotion→AU prototypes (EMFACS), are stable, citeable ground truth.
  Treat the AU reference table and the emotion recipes as reliable.

- **Seedance's interpretation of AU codes is [EMPIRICAL].** The `seedance_2_0`
  spec exposes **no FACS field, no expression enum, nothing facial** (verified
  against the spec snapshot, 2026-06-27). So "write `AU12` and get a smile" is a
  *prompt convention the model happens to interpret well* — not a documented
  capability. Practitioner report: success rate is **high**, but **codes do not
  guarantee** the exact expression, and a multi-AU prompt may render most but
  not all of the units.

**The rule:** present FACS as a strong heuristic, and let the repo's iteration
discipline (`higgsfield-prompt.md` § The Iteration Rule) confirm it on
the user's own material. Same provenance class as the Seedance Prompt-Craft Laws
(`higgsfield-seedance.md` § Prompt-Craft Laws). Never tell the user a
FACS prompt is deterministic.

> If a future Seedance spec adds a real facial/expression parameter, the
> spec-drift tripwire should catch it — at which point this "no model field"
> claim is what needs updating.

---

## The Plan-First Workflow

The single most important discipline, and the one practitioners get wrong:

> **Plan the expressions you need → generate a FACS sheet for *only those* →
> write the codes into the prompt.**

**Do not generate the full 49-AU reference sheet and then cherry-pick a few.**
That is explicitly the wrong move: a sheet asked to render all 49 units spreads
the image model thin, captions come out unreadable, and you've paid for 45
panels you'll never use. You get better identity consistency and cleaner labels
by generating a *small* sheet of exactly the 3–6 expressions the scene calls
for.

The three steps:

1. **Plan** — name the emotional beats of the shot. "She masks fear as
   reassurance" → fear (AU1+AU2+AU4+AU5) flickering under a forced smile
   (AU12 alone, no AU6). Decide the AU set *before* touching an image model.
2. **Generate the sheet** (optional but recommended for consistency) — a small
   labelled grid of just those expressions, on the actual character. See
   § Step 1.
3. **Write the prompt** — codes into the Seedance prompt, beat-synced if the
   shot has a time structure. See § Step 2.

The sheet is **optional**. Codes work in a text-to-video prompt with no image at
all (the practitioner generated whole videos from codes alone). Generate a sheet
when you need the *character's* face to stay consistent across shots — same
reason you'd use a Soul ID sheet.

---

## Step 1 — Generate the FACS Reference Sheet

A FACS sheet is a **labelled-grid image** — the character's face in each target
expression, captioned with its AU code — used as an identity + expression
reference. It is a reference-sheet image task; the image-model mechanics live in
`higgsfield-gpt-image-2.md` (Format A — structured grids) and the
`higgsfield-gpt-image-2-reference-sheet-workflow.md` satellite there. This section owns the
**FACS-specific** prompt.

**Models:** GPT Image 2 and **Nano Banana Pro** both work; Nano Banana Pro tends
to read more cleanly. Captions sometimes come out unreadable — **iterate**.

### The sheet prompt (parameterize the character + the AU list)

Upload the character image, then prompt the image model. Replace the character
description and **trim the AU list to only the units you planned** — do not paste
all 49 unless you genuinely need them:

```
Create a clean educational FACS Action Unit expression grid featuring
[CHARACTER — e.g. a realistic adult female character]. Use minimal studio
lighting, neutral white background, high readability, professional facial
anatomy reference-sheet aesthetic, realistic skin texture, consistent identity
across all panels.

COLOR SYSTEM: soft pastel color coding by category, sheet kept minimal and
elegant —
  Forehead & Brow AUs: soft pastel blue
  Eye & Eyelid AUs: soft pastel lavender
  Nose & Cheek AUs: soft pastel peach
  Lip & Mouth AUs: soft pastel pink
  Head Movement AUs: soft pastel mint
  Eye Direction AUs: soft pastel cyan
  Special / Misc AUs: soft pastel beige
Apply color subtly: panel background tint, thin borders, small label accents.
Keep colors soft, muted, professional.

Include these Action Units (one captioned panel each):
[PASTE ONLY THE AUs YOU PLANNED — e.g.
  AU6 Cheek Raiser, AU12 Lip Corner Puller, AU1 Inner Brow Raiser,
  AU4 Brow Lowerer, AU15 Lip Corner Depressor]
```

(The full category→AU list to draw from is in § AU Code Reference below.)

### The LLM can mislabel AUs — verify

The image model is *an LLM* — it can put the wrong muscle under a code. The
sample sheet that circulates labels nostril dilation **`AU82`**, while standard
FACS (and the practitioner's own dialogue example) uses **`AU38`** for the same
action; `AU8` (lips toward each other) appears in real prompts but is absent from
that sheet entirely. Treat any auto-generated sheet as a *draft*: check the
panels against the § AU Code Reference table, and against a trusted external
reference such as the **FACS cheat sheet at melindaozel.com/facs-cheat-sheet**.
This mislabeling risk is the strongest reason to plan a *small, verifiable* sheet
rather than trust a 49-panel dump.

---

## Step 2 — Put AU Codes in the Seedance Prompt

Once you know the AUs, they go into an ordinary Seedance 2.0 prompt. Everything
in `higgsfield-seedance.md` still applies — six slots, Prompt-Craft
Laws, preflight linter. FACS only changes the face specification.

### Two specification styles — test both

| Style | Looks like | When |
|---|---|---|
| **Codes only** | `AU10, AU20, AU27, AU45` | Beat lists, dense schedules; the practitioner ran whole videos this way and the model interpreted most units well |
| **Codes + short anatomical description** | `AU6 (cheek raiser, orbicularis oculi tightens, crow's feet) + AU12 (zygomaticus pulls corners up)` | When a unit keeps getting missed; the description gives the model a second, redundant signal |

Neither is universally better. **Test both on your material** — codes-only is
terser and often enough; add descriptions for the units the model drops.

### The hard limits

The legacy heading does not make AU counts platform limits: the following are
optional complexity guidance, reference choices and scene-context checks.

- **3–4 expressions is a remediation heuristic, not a hard maximum.** Stacking
  many AU requests can lower adherence. When a test shows overload, try fewer
  competing cues or give the necessary arc more time/coverage; preserve its causal
  development. The 14-beat example below is an expression study whose short,
  singular beats may render only partially, not a capacity guarantee.
- **The character photo is optional.** Codes function with no image (text-to-
  video). Attach `@Image1` only when you need the *character's* identity to stay
  consistent across shots — it changes consistency, not whether the AUs fire.
- **Still describe a scene, not just a face.** The Seedance filter reads full-
  scene intent (`higgsfield-seedance.md` § The Filter Model). Keep the
  framing/lighting/mood slots present — a bare list of AU codes with no scene is
  thin. The examples below all carry a Style/Mood header for this reason.

### Beat-synced structure

For a timed performance, give each beat a number or a time range and its AU set:

```
1: AU10
2: AU20
3: AU22
4: AU45
```

or with time ranges and descriptions:

```
2-4s: Happy — AU6 (cheek raiser, crow's feet) + AU12 (lip corners up), Duchenne smile
4-6s: Sad — AU1 (inner brow raise) + AU4 (brow knit) + AU15 (lip corners down)
```

The per-beat time labels obey the same runtime arithmetic as any multi-beat
Seedance prompt (`higgsfield-seedance.md` § Runtime arithmetic): the
beats must account for the stated duration, including inherited holds. In these
close-up studies, label the schedule as **expression beats within a continuous take**,
not hard cuts. A static camera or slow push is an option; the actual framing and
camera path follow the event and user direction.

---

## AU Code Reference

The Action Units from the standard sheet, grouped by facial region. Use this to
build a sheet prompt and to verify an auto-generated sheet's labels.

### Forehead & Brow
| Code | Action |
|---|---|
| AU1 | Inner Brow Raiser |
| AU2 | Outer Brow Raiser |
| AU4 | Brow Lowerer |
| AU71 | Brow Furrow |
| AU72 | Brow Bulge |

### Eye & Eyelid
| Code | Action |
|---|---|
| AU5 | Upper Lid Raiser |
| AU7 | Lid Tightener |
| AU41 | Lid Droop |
| AU42 | Slit Eyes |
| AU43 | Eyes Closed |
| AU44 | Squint |
| AU45 | Blink |
| AU46 | Wink |

### Nose & Cheek
| Code | Action |
|---|---|
| AU6 | Cheek Raiser |
| AU9 | Nose Wrinkler |
| AU11 | Nasolabial Deepener |
| AU82 | Nostril Dilator |
| AU83 | Nostril Compressor |

### Lip & Mouth
| Code | Action |
|---|---|
| AU10 | Upper Lip Raiser |
| AU12 | Lip Corner Puller |
| AU13 | Sharp Lip Puller |
| AU14 | Dimpler |
| AU15 | Lip Corner Depressor |
| AU16 | Lower Lip Depressor |
| AU17 | Chin Raiser |
| AU18 | Lip Pucker |
| AU20 | Lip Stretcher |
| AU22 | Lip Funneler |
| AU23 | Lip Tightener |
| AU24 | Lip Pressor |
| AU25 | Lips Part |
| AU26 | Jaw Drop |
| AU27 | Mouth Stretch |
| AU28 | Lip Suck |
| AU84 | Tongue Up |
| AU85 | Tongue Out |

### Head Movement
| Code | Action |
|---|---|
| AU51 | Head Turn Left |
| AU52 | Head Turn Right |
| AU53 | Head Up |
| AU54 | Head Down |
| AU55 | Head Tilt Left |
| AU56 | Head Tilt Right |
| AU57 | Head Forward |
| AU58 | Head Back |

### Eye Direction
| Code | Action |
|---|---|
| AU61 | Eyes Turn Left |
| AU62 | Eyes Turn Right |
| AU63 | Eyes Up |
| AU64 | Eyes Down |

### Special / Misc
| Code | Action |
|---|---|
| AU81 | Chewing |

> **Numbering caveat.** Some codes on the circulating sheet are **non-standard or
> reassigned** relative to canonical FACS — notably the AU82 (vs standard AU38)
> nostril dilator noted in § Step 1, the AU71/AU72 brow codes, and the AU82–AU85
> range. Canonical FACS also has codes this sheet omits (e.g. `AU8` lips toward
> each other, used in real prompts). Use this table for *this sheet's* convention,
> but when a code's behavior surprises you, cross-check melindaozel.com/facs-cheat-sheet.

---

## Emotion → AU Recipes

When the user asks "which code for anger / fear / disgust," these are the
standard **EMFACS emotion prototypes** — the canonical AU combinations behavioral
science maps to each basic emotion. Reliable as recipes; the Seedance *rendering*
of them is still [EMPIRICAL].

| Emotion | Core AUs | Reads as |
|---|---|---|
| **Happiness (genuine / Duchenne)** | AU6 + AU12 | Eyes-involved smile, crow's feet |
| **Happiness (polite / forced)** | AU12 only (no AU6) | Mouth smiles, eyes don't — the uncanny/forced smile |
| **Sadness** | AU1 + AU4 + AU15 | Oblique brows, down-turned mouth |
| **Surprise** | AU1 + AU2 + AU5 + AU26 | Raised brows, wide eyes, jaw drop |
| **Fear** | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 | Raised+knit brows, wide eyes, stretched lips |
| **Anger** | AU4 + AU5 + AU7 + AU23 | Lowered brow, hard stare, tightened lips |
| **Disgust** | AU9 + AU15 + AU16 | Nose wrinkle, lowered lip corners |
| **Contempt** | AU12 + AU14 (one-sided) | Unilateral smirk |

**Mixing for nuance.** The interesting expressions are *blends*: a forced-warmth
mask is genuine-smile muscles (AU6+AU12) fighting fear muscles (AU1+AU7) in the
same frame; "bitter amusement" is AU12 with no AU6 plus a faint AU4. Build a
blend by listing the AUs of both emotions and letting the conflict read — that is
the FACS path to `higgsfield-soul.md` § Micro-Expressions like
Suppressed Smile and Nervous Composure.

---

## Physical Micro-Beats — the Body Beyond the Face

`[OFFICIAL — Higgsfield shotlist-builder skill, 2026-07; re-authored from the
Chinese source]` — AU codes stop at the face. Production performance direction
extends the same muscle-level discipline to **throat, breath, skin, and
posture**. These recipes drop into the PERFORMANCE section of a block prompt
alongside (or instead of) AU codes.

**These are menus, not checklists.** Select only cues that express the current
trigger and remain visible or audible at the chosen scale. **2–4 tells** is an
optional example, not a minimum or maximum; facial AU heuristics do not impose a
body-action quota. Preserve the full action/response chain and select meaningful
breath or microexpression details without adding an each-second schedule:

| Register | Physical recipe |
|---|---|
| **Anger / determination** | Masseter visibly pulsing at the jaw · carotid pulse visible at the neck · temple veins rising · nostrils flaring on stressed words · pupils tightening · outer eye corners hardening (genuine intensity, not a cheap squint) · **no blink at the climax** · faint sweat beads at brow and nostrils |
| **Anxiety / nervousness** | One visible swallow (Adam's apple) · a short shallow nasal inhale before the line · tongue wetting a dry lower lip · lower lip pulled slightly in · capillary flush on the cheeks · pupils dilating on the key word |
| **Sadness without tears** | Outer eye corners dropping · eyes wet with catchlight — **but never spilling** · corrugator knit between the brows · a faint lip tremble · head sinking a few degrees |
| **Control / calm / superiority** | Even, steady breathing (contrast against a tense scene partner) · relaxed fingers · slow deliberate blinks · slight chin lift · a Duchenne smile that **builds gradually** — never opening on the finished smile |
| **Heaviness / weighed down** | Shoulders sinking · head dropping slightly · deep slow breathing · a small 5–15° head tilt when answering |
| **Shock / freeze** | Optional brief stillness at the trigger (0.3–0.5s is one example, not a fixed duration) · pupils dilating if visible · lips parting silently · delayed sharp inhale as the freeze breaks · gaze held on the trigger |
| **Suppressed emotion** (the hardest) | Written as *physical resistance*: every facial muscle fighting the rising emotion · masseter slowly tightening · one delayed, effortful swallow · eyes gradually welling until they shine — tears never falling · one slow, deep, controlled inhale with visible chest rise · a single jaw tremor, instantly re-clenched |

**Defaults that prevent AI-video tells:**

- **No tears unless the script explicitly calls for them** — wet-with-catchlight
  is the default sadness read.
- **No cartoon grimaces**; no "eyes to the ceiling" for thinking — name a
  specific gaze direction instead.
- **Give speakers and listeners a task.** A meaningful held posture or gaze can
  carry it; continual micro-movement is not required.
- **Reactions follow perception and motivation.** Vary onset and strength with
  distance, information and character. A 0.3–0.5s stagger (`"Roko turns first;
  0.4s later, Rein; another 0.4s, Jax"`) is an optional example, not a timing rule;
  deliberate synchronized performance remains available.
- **Listeners in bokeh retain behavior.** Use readable head/shoulder orientation,
  posture or an event-driven response; do not prescribe invisible pupil or facial
  detail in fully defocused or distant figures.

**The anti-AI test.** Before delivering, re-read the performance section and
ask: *could this have come from a prompt template, or does it read like notes
from a director who watched the actor rehearse?* If it reads templated,
rewrite — micro-beats should feel observed, not generated.

---

## Dialogue & Monologue Facial Acting

The reason FACS matters: facial expressions in isolation are a parlor trick; the
payoff is **acting during speech** — close-up monologue and dialogue where the
face carries subtext the words don't say. This is where forced smiles, leaking
fear, and mixed emotions during a line land.

### The structure

Schedule **one AU set per spoken beat**, aligned to the line being delivered:

```
Beat 1 (0-1s): AU5 + AU38 (upper lid raiser + nostril dilator — genuine fear, pre-dialogue)
Beat 3 (2-4s): AU12 + AU6 (Duchenne smile — forced warmth) — delivers "everything's fine"
Beat 5 (5-6s): AU7 (lid tightener — eyes betraying the fear the smile hides)
Beat 7 (8-10s): AU4 + AU24 (brow lowerer + lip presser — seriousness cracking through)
```

The art is the **contrast within a beat**: the mouth performs safety (AU12) while
the eyes leak terror (AU7) — the audience reads both at once. **1–2 AUs** is an
optional starting point for legibility, not a per-beat limit or a required code count.

### Every line gets three beats

`[OFFICIAL — shotlist-builder]` — consider preparation, delivery and aftermath
as continuous performance. Write the changes needed for the line and listener;
these are not three mandatory new gestures or separately timed beats:

- **Pre-line beat** — what happens before the first word: a swallow, an
  inhale, a lip lick, a posture shift.
- **During the line** — which words carry the emphasis, and through what:
  nostril flare, intonation, pupil shift.
- **Post-line beat** — the resulting gaze, breath or body state carries into the
  next response. A ~0.5s hold is one example; overlaps, immediate replies and
  longer assessments follow the actual dialogue and event.

> Pre-line: one short nasal inhale, one visible swallow.
> Line: "Don't ask me again." — the stress lands on *again*, nostrils
> flaring on the word.
> Post-line: gaze stays locked on the opponent for 0.5 seconds — then
> drifts away.

### Combine with audio + lip-sync

A dialogue FACS prompt pairs naturally with the audio conditioning layer:

- Use the **`[AUDIO: Xs]` script block** (`higgsfield-audio.md` § Audio
  as a Conditioning Input) to place the spoken lines — quoted text generates
  speech **with automatic lip-sync**, so the mouth shapes the words while your AU
  schedule drives the *expressive* muscles around them.
- A tight close-up + a strong `@Image1` identity reference can help inspect or
  repair lip-sync (the audio skill's Lip-Sync Rules). Use that coverage when it
  serves the scene; wider dialogue remains valid and uses readable cues.
- Keep the FACS schedule to the brow/eye/cheek units during spoken beats; let the
  audio block drive the lip/jaw shaping for the words, and reserve explicit
  lip/jaw AUs (AU12, AU15, AU24) for the *expressive* overlay, not the phonemes.

---

## Worked Examples

All three are lightly normalized from practitioner prompts. Run each through the
preflight linter before generating (`python3 scripts/seedance_lint.py --preflight --model
seedance_2_0 "<prompt>"`).

### A — Beat-synced expression sweep (codes-only)

```
**Model:** Seedance 2.0
**Aspect ratio:** 1:1   **Duration:** 15s

Use the provided character @Image1 as the fixed identity reference.
Cinematic tight close-up, subtle neutral background, high facial clarity, slow
micro push-in, shallow depth of field. 14 beats, beat-synced:

1: AU10   2: AU20   3: AU22   4: AU23   5: AU27   6: AU28   7: AU45
8: AU53   9: AU61   10: AU62  11: AU64  12: AU85  13: AU84  14: AU46

Uneasy, hypnotic, controlled mood.

**Camera:** slow push-in
```

(Codes-only, one AU per beat — expect most to land, some only partially; that is
the documented behavior, not a failure to fix by over-prompting.)

### B — Emotion arc (codes + anatomical description)

```
**Model:** Seedance 2.0
**Aspect ratio:** 16:9   **Duration:** 15s

**Style & Mood:** photoreal, face and shoulders only, bare skin no makeup, soft
diffused light, plain white background, shallow depth of field.

Timeline:
0-2s: Neutral resting face, eyes forward, relaxed brow and lips.
2-4s: Happy — AU6 (cheek raiser, crow's feet) + AU12 (lip corners up and out),
  Duchenne smile, slight eye squint from cheek push.
4-6s: Sad — AU1 (inner brow raise, oblique brow) + AU4 (brow knit) + AU15 (lip
  corners down), eyes slightly glassy.
6-8s: AU61 then AU62 — gaze shifts left, then right, head still.
8-11s: AU46 left wink, then AU46 right wink, subtle smirk between.

**Camera:** static medium close-up
```

### C — Fear masked as reassurance (dialogue + FACS beats)

```
**Model:** Seedance 2.0
**Aspect ratio:** 16:9   **Duration:** 15s

Use the provided character @Image1 as the fixed identity reference.
Dim interior, single warm lamp, slight low angle, handheld micro-sway, shallow
depth of field.

[AUDIO: 0s] "Hey, hey — everything's fine, okay? We're just gonna play a game
where we stay really quiet. Can you do that for me?"

Beat 1 (0-1s): AU5 + AU38 (upper lid raiser + nostril dilator — genuine fear, pre-dialogue)
Beat 2 (1-2s): AU45 (blink — composing the mask)
Beat 3 (2-5s): AU12 + AU6 (forced Duchenne warmth) — "everything's fine, okay?"
Beat 4 (5-8s): AU2 + AU12 (smile + outer brow raise — performing fun) — "we're just gonna play a game"
Beat 5 (8-10s): AU4 + AU24 (brow lowerer + lip presser — seriousness cracking) — "where we stay really quiet"
Beat 6 (10-15s): AU6 + AU17 + AU1 (eyes smiling while chin trembles, desperation) — "can you do that for me?"

Devastating contrast between performed safety and visible terror — the face never
fully commits to either; the audience reads both at once.

**Camera:** handheld micro-sway, slow push-in
```

> Template version of this beat structure: `template-facs-expression-beats.md`.

---

## Related Skills

- `higgsfield-seedance.md` — the base prompt grammar every FACS prompt
  obeys (six slots, Prompt-Craft Laws, preflight linter, § Voice Rewrite "physics
  not emotion" — FACS is its muscle-level case)
- `higgsfield-soul.md` § Micro-Expressions — 19 named expressions; FACS
  is the precise-control layer beneath them
- `higgsfield-audio.md` § Audio as a Conditioning Input — the
  `[AUDIO: Xs]` block + lip-sync for dialogue FACS
- `higgsfield-gpt-image-2.md` — Format A reference-sheet image mechanics
  for the FACS sheet
- `vocab.md` § Emotion as Visible Behavior — Channels — the behavioral
  sibling of the AU vocabulary
- `template-facs-expression-beats.md` — beat-synced AU schedule template
</content>
