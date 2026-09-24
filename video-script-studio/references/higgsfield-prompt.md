# Higgsfield Prompt Engineering

Current studio video generation defaults to Seedance 2.5 `omni_reference` for role-based
character, prop and scene images plus motion/camera video and sound/audio references.
Even a single picture is an attribute reference, never a forced opening image.
The I2V section below describes a legacy alternative for other model workflows and
must not route current studio video tasks. Describe opening motion and final state
in words, using real reference slots and avoiding invented attachments.

Follow [sample approval](sample-approval.md) for every prompt-writing request, including rewrites, repairs and single prompts. Write only the requested type: assets or video. If both are requested, use separate batches with their own samples and approvals. First provide a representative, usable sample for the current batch, wait for explicit approval of that version, then deliver all prompts in that batch. Prior approval does not approve a new request; there is no skip-sample exception. Apply the methods below only to the sample's scope until approval; after approval complete the batch without another sample loop. Never append asset-generation prompts to a video request, automatically continue from assets into video, or present intended effects as generated results.

## QUICK FACTS
- MCSLA = Model, Camera, Subject, Look, Action — the five layers of every prompt [→](#the-mcsla-formula)
- For this project, images own only their assigned appearance, prop or scene attributes; retain causal motion and state handoffs in the `omni_reference` prompt. I2V below is legacy context [→](#image-to-video-i2v)
- Keep prompts under 200 words — **short-form MCSLA regime only**; block-scaffold production prompts replace the cap with structural lint (HARD RULE 8 carve-out); Cinema Studio has a hard 512-character cap [→](#high-performing-prompt-patterns)
- One primary change per narrative stage; compatible stages may share a shot or clip. Action counts are complexity examples, not quotas; Fast Motion Trick: render in Slow Mo, speed up in post [→](#one-action-per-scene)
- Never leave a generic emotion ("sad"/"angry") in a prompt — decompose into muscle movements, breath, eyes, skin [→](#generic-emotion-decomposition--which-kind-of-x)
- Soul ID / recurring characters: separate identity locks from temporal performance within the chosen output format [→](#identity-vs-motion-separation-rule)
- Conflict order: user direction within actual platform limits → shared director contract → local archetype/emotion options [→](#conflict-resolution-between-sub-skills)
- Aspect ratio is a per-model enum set in the UI/header, never in the prompt body — verify via `model-specs.json` [→](#common-prompt-mistakes)
- Avoid conflicting simultaneous camera moves; motivate sequential reversals; use stable action names and mode-specific reference bindings [→](#common-prompt-mistakes)
- Iterate by changing exactly ONE variable per regeneration [→](#the-iteration-rule--change-one-variable-at-a-time)
- 6-Pass Diagnostic order: Subject → Action → Camera → Style → Audio → Output; most failures land on Pass 1–2 [→](#when-you-dont-know-whats-wrong-yet--the-6-pass-diagnostic-sequence)
- Seedance short-form: 30–100 words win; Subject + Action in the first 20–30 words. Block-scaffold production briefs run 218–2,059-word medians by register — see `higgsfield-seedance.md` § Official Prompt Architecture [→](#the-directors-formula--mcsla-mapping)
- Optional short-form genre targets: Product 30–50w, Lifestyle 40–60w, Drama 60–100w, Music Video 50–80w, Anime 50–90w [→](#genre-router--prompt-length--lead-with-targets)
- Kill slop words (beautiful, stunning, epic, amazing) — replace with concrete visuals/physics [→](#anti-slop-vocabulary)
- Seedance/CS 3.0 has NO negative-prompt syntax — phrase as positive constraints [→](#no-negative-prompts)
- Dialogue pacing example: ~25–30 spoken words in 15 seconds; preserve approved lines and budget actual delivery plus responses [→](#dialogue-archetypes)
- Legacy Seedance 2.0 remediation: simplify tracked casts, re-entry and reflections when they fail; keep off-screen continuity explicit [→](#character--spatial-rules)
- Double contrast changes shot size and camera character when contrast serves the event; intentional repeated coverage remains valid [→](#double-contrast-cut-technique)
- Age-blind rule: never boy/girl/child/kid/young/teen/little — describe by role, clothing, action [→](#age-blind-character-rule)
- In medias res is an optional opening tactic; preserve setup needed for causality or a reveal [→](#default-in-medias-res)


## Shared narrative planning before MCSLA

Apply [shared narrative planning](narrative-planning.md) to every prompt type,
archetype, and revision. Establish the goal and ending, identify story events, causality,
reveals, and state transitions, then estimate time for actions, dialogue, responses,
reading, holds, and transitions. Do not preset stage counts or divide runtime equally.
A **stage is not a cut or a generation clip**: one continuous shot can span stages, a stage
can need several shots, and a generation can contain several compatible stages. Split
calls only for mode, complexity, references, or actual duration limits, carrying join states.

Plan the eight director layers semantically: **assets/reference locks; overall goal;
global sight/sound/space; subject behavior and pacing; staged performance;
continuity/state inheritance; final frame/join; scoped constraints**. Compile into MCSLA,
Identity/Motion blocks, fluid narrative, timestamped prose, or the chosen model's native
format. For this project, complete prose video prompts in every genre visibly follow
[the shared full-director format](template-general-director-2-5.md):
assets, goal, audiovisual/space, behavior, staged performance, continuity, final frame,
and constraints. Each stage uses a time/event heading, developed performance prose,
visual results, camera and sound. Explicit native-format or scoped requests retain their
output contracts without a duplicate long-form document. Each stage has
an initial state, primary change, visible response, and end state inherited by the next.
Count the final frame and transitions inside the runtime; preserve results until a
motivated change, cleanup, restoration, or time/location transition.

For source edits, retain original timestamps, duration, cut structure, performance, and
audio timing outside the requested change. For extensions, inherit pose, props, motion
phase/direction/speed, camera/framing, light, and sound at the join: forward starts from
the source tail; reverse extension ends at the **source first-frame state**. Budget only
new material under the selected mode's rules. Preserve I2V's reference-owned appearance,
all parameter/input limits, and the downstream edit/extension workflows.

For this project, before writing or fully rewriting video prompts, read the entire
[user-approved full performance example](template-full-performance-example.md).
Default to a complete performance brief with concrete action development, object/opponent
response, subject follow-through, visual layers, motivated camera paths, sound, persistent
results and final-frame detail. Short-form word targets elsewhere in this guide do not
truncate this master brief. A single shot or quiet event does not imply a short answer.
Use concise delivery only for an explicit concise request, a scoped edit or a target's
hard limit; retain the full master for complete tasks and compile a legal submission
where necessary. Preserve all native formats, image-only workflows, I2V reference ownership,
variants and model/mode capabilities. Transfer the example's specificity, not its fantasy
genre, six stages, thirty seconds, colours or effects.

## The MCSLA Formula

Every high-performing Higgsfield prompt is built on five layers. Think of it as the
cinematographer's checklist — fill in each layer and the model has everything it needs.

| Letter | Element | Description | Example |
|--------|---------|-------------|---------|
| **M** | Model | Which generation engine | "Use Kling 2.6" |
| **C** | Camera | Explicit viewpoint/path; exact name when using a platform preset | "FPV Drone shot weaving through the alley" |
| **S** | Subject | Who/what + appearance | "A woman in a sand-colored suit, sharp eyes" |
| **L** | Look | Style + color + lighting | "Cinematic, golden hour, anamorphic flare" |
| **A** | Action | What happens in the scene | "She turns slowly, wind lifting her coat" |

---

## Prompt Types

### Text-to-Video (T2V)
Start from nothing — describe the entire scene from scratch.
Best for: establishing scenes, abstract concepts, environments without a specific character.

```
[Subject + appearance].
[Environment — location, time, weather, atmosphere].
[Action — what happens and how].
[Camera — viewpoint, subject, path and endpoint; exact preset name if used].
[Look — style + color grade].
```

**Example:**
```
A lone astronaut stands on the surface of a red desert planet, helmet visor reflecting
twin moons rising on the horizon. Dust spirals slowly in the thin atmosphere.
She turns to face the camera, gloved hand raised in a slow salute.
Camera: slow Crane Up revealing the vast emptiness behind her.
Style: Cinematic, desaturated orange and deep blue, 2.35:1 anamorphic.
```

---

### Image-to-Video (I2V) — legacy model context, not the current studio route
Animate a provided still image. In legacy I2V models the image defines the starting frame; for this project's Seedance 2.5 video tasks, assign it an attribute reference role instead.
Best for: character consistency, product shots, portrait animation, storyboard bring-to-life.

```
[Reference the input image as the first frame].
[Describe what should move, change, or animate — let the image own appearance].
[Camera — viewpoint, subject, path and endpoint; exact preset name if used].
[Style/atmosphere cues].
```

**Example:**
```
Starting from the provided image as the first frame.
The woman's hair lifts gently in the wind. She blinks slowly and turns her gaze
slightly to the left, a faint smile forming.
Camera: subtle Dolly In toward her face.
Style: Cinematic, warm afternoon light, shallow depth of field.
```

**Key rule for I2V:** Let the image own appearance and avoid redundant visual reconstruction.
Still declare reference roles, necessary starting/ending states and continuity locks.
Develop what changes through action, response and follow-through, including camera and sound.
For @ Image references, distinguish an identity reference from an actual first-frame anchor.

---

## Narrative Structure

Use the event/state plan above in either format. Stage count comes from the content;
shot and generation boundaries are separate decisions. Timing examples below illustrate
specific performances, not a default three-stage composition.

### Fluid Narrative (preferred for most use cases)
For an optional short-form or explicitly untimed submission, write continuous action
without timestamps. Full performance delivery retains the shared time/event headings
and developed prose within each stage.

```
A detective pushes open the door to the rain-soaked rooftop, coat whipping in the wind.
She steps to the edge and looks down at the city below — a thousand lights blurring
through the downpour. Camera dollies slowly behind her, then cranes up to reveal the
skyline. Cinematic style, cold blue tones, 16:9.
```

### Timestamped (use only for precise multi-beat sequences)
Use time/event ranges in the default full performance format, and timing targets in
short submissions when separate actions need them — e.g., a transformation,
a multi-phase action sequence, or a beat-synced music video. Choose Cinema Studio 3.0's
Custom multi-shot mode when cuts are intended. Stages inside an oner need an explicit
continuous-shot instruction; a timestamp alone is not a cut. Generated timing is not a
frame-accurate guarantee, and source/audio timestamps remain authoritative for edits.

```
0–3s: Wide establishing shot. The fighter stands alone in the ring, chest heaving.
3–6s: Crash Zoom In on his face. Sweat on his brow, jaw clenched.
6–10s: 360 Orbit as he raises his fists. Crowd noise rises.
```

---

## High-Performing Prompt Patterns

> **The #1 mistake in video prompting**: over-describing appearance and under-describing
> behavior. Give your subject something to DO. Give them an internal state that creates
> visible behavior. A verb that describes motion or intention is more important than
> adjectives.

**Specificity beats generality:**
- ❌ "the camera moves dramatically"
- ✅ "camera Dolly Zoom In — subject stays the same size as the background rushes forward"

**Active verbs carry the scene:**
- ❌ "a woman is in an alley"
- ✅ "a woman darts through a rain-soaked alley, coat flapping, boots splashing"

**Make the camera path explicit:**
Use the exact catalog name when selecting a supported platform preset; free prose is valid.
- ❌ "the camera slowly circles" (subject, arc and endpoint unclear)
- ✅ "360 Orbit around the subject at eye level, returning to the frontal view" (preset example)

**For short-form MCSLA, lead with subject, end with style:**
Subject → Action → Camera → Style is a useful compilation order; full delivery keeps
the shared eight-section order.

**Keep it under 200 words (short-form regime):**
Focused prompts outperform exhaustive ones. One clear intention > ten vague details.
**Regime exception (HARD RULE 8):** block-scaffold production prompts —
`higgsfield-seedance.md` § Official Prompt Architecture — replace the
word cap with structural lint; harvested production briefs run 218–2,059-word
medians by register. The soft cap governs optional short-form MCSLA submissions only, not a complete single-shot performance brief.

**Cinema Studio: Keep it under 512 characters:**
Cinema Studio has a hard 512-character limit on prompts (both 2.5 and 3.0).
- **2.5:** @ Element chips consume ~80–100 hidden characters each. With 2 @ tags, keep visible text under ~250 chars.
- **3.0:** @ references (images/video/audio) are media attachments, not inline metadata — they consume less hidden space. Keep visible text under ~350–400 chars with references, ~450–500 without.
See the Cinema Studio skill for full character budget details.

---

## The Pre-Prompt Checklist

Before writing any prompt, answer these five questions. Vague prompts like "give me
something cinematic" tell the AI nothing.

| Question | What to specify |
|----------|----------------|
| **Who?** | Subject + appearance (e.g. "a man in a leather jacket") |
| **Where?** | Environment + atmosphere (e.g. "in a narrow aircraft galley, cold blue light") |
| **What's happening?** | Goal, causal events, and one primary change per stage (e.g. a strike and its visible response) |
| **Camera movement?** | Viewpoint, subject, path and endpoint; exact preset name or Director Panel setting when used |
| **Mood/Genre?** | Style + color grade, or Cinema Studio genre selection |

---

## One Action Per Scene

AI models can replicate real-life physics — but only so much at once. Asking for
multiple complex actions in one clip overwhelms the model.

**Planning rule:** one primary change per narrative stage, with supporting actions and
responses serving it. A single action with 1–2 secondary motions is a useful short-shot
example, not a universal clip limit. Compatible stages may share a shot or generation.

Split complex sequences where causal readability, performance load, or model limits
require it, then stitch in an editor or use Multi-Shot Manual mode when actual cuts are
needed. Preserve the outgoing state at each join; do not fragment a complete performance
or invent extra beats to meet a count.

**Fast Motion Trick:** If fast motion keeps morphing or breaking, generate the scene
in Slow Mo first, then speed it up in post (CapCut, Premiere, DaVinci). The model
renders cleaner physics in slow motion.

---

## Generic-Emotion Decomposition — Which kind of X?

Never leave a generic emotion in a prompt. "Sad" / "angry" /
"surprised" / "scared" / "thoughtful" / "in love" — each is at least
three or four distinct physical realizations, and the model renders
a different version depending on which one your prompt invites. A
prompt that says only "she looks surprised" produces a different
shot every regeneration and degrades adherence across batches.

The rule: ground the emotion in its trigger and a few meaningful visible cues,
selected for the framing and performance. Muscle, breath, eye and skin cues are a
menu, not a required stack. Use the scene context to choose; clarify only when an
unresolved interpretation would materially change the user's intended performance.

Clarification template — offer when the script or user supplies a
generic emotion you cannot decompose without inventing detail:

> Which kind of surprise?
> (a) Light positive — eyebrows lift, lips part softly, slow inhale
>     through the nose, no other movement.
> (b) Shock — sharp inhale through the mouth, eyes widen, body
>     freezes in place, hand involuntarily lifts to chest.
> (c) Disbelief — slow blink, head tilts a fraction, lips press
>     together, only one eyebrow lifts.
> (d) Surprise-with-joy — eye light shifts (catchlight reads),
>     smile builds gradually, shoulders relax.

Same shape applies to any generic adjective — "tense" / "sad" /
"angry" / "scared" / "thoughtful" / "in love" each decomposes into
3-5 distinct physical realizations. The decomposed prompt produces
a performance; the generic prompt produces AI-video.

> **Preset library alternative.** For named micro-expression presets
> that drop into a prompt without first-principles decomposition,
> see `higgsfield-soul.md` § Micro-Expressions. The catalog
> covers most common emotional registers with locked physical
> descriptors. Use the decompose-from-first-principles rule above
> when no preset matches; use the preset library when one does.

### Layered emotion states

Single-axis decomposition (above) names one register: angry / sad /
surprised. **Layered emotion** names a composite state where two
registers stack — *anxious determination*, *tired tenderness*,
*bitter amusement*, *cornered calculation*. Production-team practice
finds the model renders layered states better than single registers
when the layering is described as *one channel modulating another*:
the dominant state plus the underlying state plus the visible tell.

- **Anxious determination** — set jaw + locked gaze (determination)
  with shallow chest breath and a single hand at the side flexing
  open-closed (anxiety underneath).
- **Tired tenderness** — soft micro-smile + half-closed eyes
  (tenderness) with the body weight settled, slow blink interval
  (tiredness underneath).
- **Bitter amusement** — one-sided smirk + eye-shine (amusement)
  with no smile crinkles at the eye corners (bitterness underneath).

Compose layered states by stacking decomposed physical realizations
from the single-axis catalog. The dominant state goes in the face;
the underlying state goes in breath, posture, and hand-state; the
visible tell sits in the eyes.

For finer control, layer a **tiny detail** on top of an existing
emotional cue: `Roco is very upset, and his lower lip trembles`.
The base emotion gets the broad performance; the tiny detail gives
the model a specific physical cue to render. Production-team
discipline holds that the model renders the simple-emotion-plus-
tiny-detail compound better than either an over-decomposed prompt
or a too-generic one.

---

## Identity vs. Motion Separation Rule

When a prompt involves Soul ID or any character who must stay consistent across shots,
**separate stable identity information from temporal performance**. The two labeled
blocks below are the optional short-form layout; in the full director format, identity
belongs in assets/reference locks and motion in staged performance and continuity:

### Identity Block — Static visual descriptors ONLY
- Face features, skin tone, body type, distinguishing marks
- Clothing, accessories, color palette
- NO motion, NO camera, NO temporal language

### Motion Block — Temporal and camera ONLY
- Camera movement, action choreography, speed
- Environmental motion, atmospheric changes
- NO character appearance repetition

**Bad (mixed) — identity drifts:**
```
A woman with sharp cheekbones and auburn hair in a blue trench coat runs through
a rain-soaked alley, her coat flapping, sharp cheekbones catching the neon light,
camera chasing her at full speed, her auburn hair streaming behind her.
```

**Good (separated) — identity stays locked:**

**Identity Block:**
```
The Soul ID character — sharp cheekbones, auburn hair shoulder-length,
wearing a blue trench coat with silver buttons, lean athletic build.
```

**Motion Block:**
```
She runs through a rain-soaked alley, coat flapping behind her.
Camera: Action Run — low behind, matching pace.
Neon reflections streak across wet concrete.
Style: Cinematic, cold blue shadows, warm neon accents. 16:9.
```

**When to apply this rule:**
- Always when Soul ID is active
- Always in multi-shot sequences where the same character appears
- Always when camera movement is involved alongside a character
- In Cinema Studio, identity goes in the @ Element definition; motion goes in the prompt

> **Camera-emotion sync is optional.** The Motion Block describes WHAT the character
> does and HOW the camera moves. Jittery handheld for anger, smooth handheld for calm
> or a slow push for revelation are choices, not mappings to enforce. Choose coverage
> for user direction, viewpoint and event readability. See
> `higgsfield-camera.md` § Camera-Emotion Sync for its examples. For decomposing the underlying
> generic emotion before picking a camera prescription, see § Generic-Emotion
> Decomposition above.

---

## Conflict resolution between sub-skills

Sub-skills can legitimately nominate different things for the same shot. `higgsfield-camera § Camera-Emotion Sync` nominates handheld-slow-low for sadness; `higgsfield-prompt § Scene Archetype Router` permits locked dolly-in for the Atmosphere archetype where mood-is-the-content. When two sub-skills nominate different camera moves (or motion presets, or style registers) for the same scene, resolve in this order:

1. **Explicit user direction wins.** If the user said "slow push-in," that's the camera move. The agent's job is to make that direction work with the rest of the structure, not to override it.
2. **Actual platform limits and the shared director contract govern.** Satisfy verified mode constraints; apply [shared narrative planning](narrative-planning.md) for full format, causal performance and continuity before local creative suggestions. If user direction exceeds a real limit, resolve the conflict without silently discarding it.
3. **Scene archetype and emotion-sync are optional choices.** Use them when they help the viewer read the event (Atmosphere → static / slow push-in; Action → tracking / FPV; Dialogue → shoulder coverage). Neither forces a move, close-up, cut or emotion-camera mapping.

When the resolution is non-obvious, surface it. Tell the user which sub-skill nominated what and why you picked one over the other — this is meta-correct behavior and lets the user override. Silent picking is the failure mode; transparent picking is the discipline.

---

## Common Prompt Mistakes

| Mistake | Fix |
|---------|-----|
| Re-describing the image in I2V | Let the image own appearance; retain reference locks, action process and inherited states |
| Generic camera language | Specify viewpoint, subject, path and endpoint; use exact preset names only when using presets |
| No style specified | Always include visual style + color grade |
| Too many competing actions in one shot | Clarify the primary change and responses; split shots/generations only if complexity or limits require it |
| Contradictory movements | Avoid simultaneous opposing moves; a sequential Dolly In → Dolly Out needs a motivated turn and explicit endpoints |
| Prompt over 512 chars (Cinema Studio) | Cut text, reduce @ tags, use pronouns |
| Describing impact before its cause | Write setup, action, contact/miss, response, follow-through and persistent result in causal order |
| A specific martial arts move fails | Retain the intended technique and explain visible mechanics; simplify redundant joint detail during remediation without dropping the exchange |
| Multiple @ Elements cause identity swaps | For affected Cinema Studio Element submissions, bind identity separately and use stable names in action; retain required reference mappings in other modes |
| Mixing identity + motion in one block | Separate into Identity Block + Motion Block (see above) |
| Aspect ratio inside the prompt body | Set aspect in the Higgsfield UI / output-format header (per-model enum: e.g. Kling 3.0 accepts 16:9 / 9:16 / 1:1 only — check `higgsfield model get <model>` or MCP `models_explore`). Describe framing in plain language ("full body" / "chest-up" / "wide establishing") not numerical ratios. |

> **Output ratio is an enum, not a free-form value — and anamorphic is a style register, not an output dimension.** Output aspect ratio is a hard, enumerated platform spec — Kling 3.0 emits `16:9 / 9:16 / 1:1` and nothing else. "Anamorphic" is a *cinematography register* (anamorphic lens flares, letterboxed compositional read, >2:1 framing aesthetic) that the model can render *within* a 16:9 output. "16:9 anamorphic" written as a single phrase in the prompt body is incoherent — pick one. Output ratio belongs in the header (and must be one of the enum values for the chosen model — check `higgsfield model get <model>` or the MCP `models_explore` equivalent before assuming). Anamorphic style cues belong in the Look line ("anamorphic-style flares, letterboxed composition") *as a style request*, not as an output dimension.

> **Negative constraints:** For a comprehensive list of artifacts to avoid (floating limbs,
> face warping, flickering textures, etc.) and the prompt phrasing to prevent them, see
> `negative-constraints.md`. Always check the relevant categories for your prompt type.

---

## Before You Iterate — Is the Miss Systematic or Stochastic?

At a ~1.5% video / ~1% image acceptance bar, **most misses are variance, not a
broken prompt.** Serial single-variable iteration is the right tool for a
*systematic* miss — the prompt is genuinely wrong. Run it on a *stochastic*
miss and you're "fixing" a prompt that was already right, burning credits to
re-roll the same dice one at a time. So decide the fork **before** you touch the
prompt:

- **Are the misses all failing the same way?** (identity drifts every time,
  wardrobe contaminates every time, the cut count is always wrong) →
  **systematic.** The prompt is wrong. Iterate it, one variable at a time (next
  section).
- **Are they failing in varied ways, with the occasional near-hit?**
  (performance flat on one roll, camera off on another, physics odd on a third)
  → **stochastic.** The prompt is right; the roll wasn't. **Stop touching the
  prompt. Lock it, fire a batch, and cull.**

### Batch-and-Select (Variance-Harvesting) — Not the Same as Stylistic Fan-Out

When the verdict is stochastic, the move is **variance-harvesting**: hold the
**same locked prompt** constant, roll N at once (grid generation / Batch Size in
Cinema Studio, DoP Lite for cheap rolls), and cull to the keeper. This is the
opposite of the stylistic-fan-out exception in the next section — that varies N
*different looks*; this rolls N *identical* attempts because the prompt is right
and only the dice are the problem. They read alike and are economically
distinct: fan-out explores, harvest exploits.

**The cull rubric — how to pick the keeper from a batch.** Batching is worthless
without a disciplined select. Don't pick "the prettiest"; select against the
**falsifiable success criteria** you locked before generating:

1. **Hard-gate on the invariants first.** Identity, wardrobe, cut count, text
   legibility, named physics anchors — any roll that fails one is *out*, however
   nice it looks. (These are your structural failure modes; a batch can't fix a
   structural miss, only dodge a stochastic one.)
2. **Among survivors, score the stochastic axis that was failing** — the
   performance, camera, or composition you were re-rolling for. Best one wins.
3. **Choose one keeper.** Retain the take that best meets the locked criteria
   and use it as the accepted source for editing or continuation.
4. **If the whole batch fails the hard gate**, the miss was systematic after
   all — stop harvesting and go iterate the prompt.

---

## The Iteration Rule — Change One Variable at a Time

When a prompt is close-but-not-right and you're about to regenerate, change
**exactly one variable** per attempt. Subject detail, composition, motion
behavior, lighting, or style — pick the one that's wrong, change only that,
regenerate.

**Why it matters:** if you change two variables and the result improves, you
don't know which change drove the improvement. If the result regresses, you
don't know which change broke it. Either way you've spent a generation and
learned nothing about the prompt. Single-variable iteration gives every
regeneration a clean cause-and-effect signal — you keep what works, drop what
doesn't, and converge on the right prompt fast.

**The exception:** once the prompt is locked and you're varying purely for
stylistic exploration (e.g., five lighting variants of an already-approved
scene), batching changes is fine. The rule applies during *refinement*, not
during fan-out. (Don't confuse this stylistic fan-out — N *different* looks —
with variance-harvesting above, which rolls N *identical* locked prompts to beat
a stochastic miss. Both batch; only one changes the prompt.)

**Workflow:**

1. Generate the baseline.
2. Identify what's wrong — pick **one** specific thing.
3. Change only that variable in the prompt; leave everything else untouched.
4. Regenerate.
5. Compare against the baseline — did the targeted change move the result the
   way you expected?
6. Lock that change. Identify the next problem. Repeat.

If you find yourself wanting to "fix everything at once," stop and ask which
fix matters most. That one goes in this regeneration; the rest wait their turn.

### Prompt-window hygiene

Iteration also accumulates clutter — old prompt edits that no longer apply,
stale reference images attached from earlier shots, contradictory clauses
layered atop one another, prompts that have grown so long the model loses
the load-bearing pieces inside the noise. Four hygiene patterns from
production practice:

- **Delete obsolete prompt blocks.** When a previous prompt section was about
  the sticky-note prop but you've moved to character generation, delete the
  sticky-note block. Otherwise the model occasionally pulls the stale prop
  into the new generation.
- **Editor-adds-atop-existing-prompt creates contradictions.** When edits
  accumulate by appending rather than replacing, the prompt collects
  contradictory clauses (`tight close-up` from the old version, `wide
  establishing` from the new one). Symptom: output degrades into model-confusion
  artifacts. Counter: when iterating, replace the relevant clause in place
  rather than appending a new one.
- **Remove stale reference images.** When assets change between shots (the
  Polaroid was on the fridge in shot 1 but pulled off in shot 2), remove the
  now-stale reference from the prompt window so the model is not still
  trying to place it.
- **Prompt-overload sanitize pass.** When the prompt has grown beyond ~2-3k
  characters from accumulated detail, ask Claude (or whatever prompt-
  construction surface you use) to **optimize / study the context / sanitize
  the prompt** — consolidate redundant clauses, drop now-obsolete
  qualifiers, preserve the load-bearing structure and full causal performance.
  This is a cleanup trigger for accumulated clutter, not a 2–3k-character cap on
  the master brief. Compile separately for a verified platform field limit.

### When You Don't Know What's Wrong Yet — the 6-Pass Diagnostic Sequence

The Iteration Rule above assumes you can identify which one variable to change.
When you can't — the prompt produces output that's vaguely off and you can't
name why — run the 6-Pass Diagnostic Sequence to find it. Each pass isolates
one variable, in order, and tests it before moving on.

The order is not arbitrary. Subject and action carry the heaviest token weight
(early-prompt positioning); camera and style come next; audio and output
controls sit at the periphery. Diagnosing in this order surfaces the highest-
leverage problem first and stops you from chasing a style-pass fix when the
real issue was the subject description three layers up.

| Pass | Variable | Question |
|------|----------|----------|
| 1 | Subject | Is the character / object / focal element described unambiguously? |
| 2 | Action | Is each stage's primary change concrete, with a readable cause, response, and inherited end state? |
| 3 | Camera | Is the camera move named (Director Panel preset or specific verb), not implied? |
| 4 | Style | Is the look anchored (palette, grade, lens, lighting), not adjective-only? |
| 5 | Audio | If audio is part of the output, is it described as a parallel track with concrete sounds? |
| 6 | Output | Are aspect ratio, duration, and resolution set deliberately for the shot's needs? |

**How to use it:** start at Pass 1. If the result improves when you sharpen the
subject, you've found your variable — return to the Iteration Rule loop and
keep going. If Pass 1 doesn't move the result, lock the subject, advance to
Pass 2, and so on. The sequence is a finder, not a refinement loop. Once you
know which variable is wrong, the Iteration Rule takes over.

**Don't run all six passes blindly.** Six regenerations cost six credits. The
sequence's value is the *order* — most prompt failures land on Pass 1 or Pass 2
because early-prompt tokens dominate. If you reach Pass 4 without moving the
result, the prompt may need a structural rewrite, not iteration.

---

## Seedance 2.0 Prompting Best Practices

These best practices apply to Cinema Studio 3.0's generation engine (Business/Team plan) and complement the MCSLA formula above. They are not a replacement — use MCSLA as the primary framework, then apply these refinements.

> For the user-intent layer that sits above MCSLA — what working mode
> you're in (Exploration / Continuation / Bridging / Repair) and how each
> routes through Seedance's prompt modes — see
> `higgsfield-seedance.md` § Working Modes. The disambiguation
> between working modes and prompt modes lives in the same file,
> immediately above.

### Intent over Precision

Tell the model WHAT you want and HOW it should FEEL, not every micro-detail. In the short-form regime, short prompts (30–100 words) consistently outperform long ones. (Block-scaffold production briefs are the other regime — structure replaces the cap there; see `higgsfield-seedance.md` § Official Prompt Architecture.) The model is an AI director you collaborate with, not a render engine you command.

### The Director's Formula → MCSLA Mapping

The Director's Formula maps directly to MCSLA:

| Director's Formula | MCSLA Layer | Priority |
|-------------------|-------------|----------|
| Subject | S (Subject) | First 20–30 words (early tokens carry heavy weight) |
| Action | A (Action) | First 20–30 words |
| Scene | — (Context) | Supporting detail |
| Camera | C (Camera) | After subject + action |
| Style | L (Look) | After camera |
| Constraints | — (Guardrails) | End of prompt |

**Short-form insight:** Subject + Action can lead the first 20–30 words of an optional compact submission; the complete master retains its shared section order. Early tokens carry disproportionate weight in the generation engine.

### Genre Router — Prompt Length & Lead-With Targets

For optional short-form compilation, these genre lengths and lead elements are
starting targets. They do not cap or reorder the complete performance master:

| Genre | Lead With | Target Length | Example Lead |
|-------|-----------|---------------|-------------|
| Object study | Subject | 30–50 words | "A matte-black wireless earbud case rotates slowly on a marble pedestal..." |
| Lifestyle / Social | Action | 40–60 words | "She reaches for the coffee mug, steam curling upward..." |
| Drama / Narrative | Scene | 60–100 words | "Rain hammers a narrow Tokyo alley at 2 AM, neon signs reflecting in puddles..." |
| Music Video | Style | 50–80 words | "Anamorphic flares, crushed blacks, 16mm grain..." |
| Landscape / Travel | Scene | 30–60 words | "Dawn breaks over a volcanic ridge, mist pouring through the caldera..." |
| Anime / Artistic | Style | 50–90 words | "Cel-shaded lines, saturated palette, Studio Ghibli cloud physics..." |

> A texture word in a Style lead ("16mm grain") is a **look choice** and belongs
> there. The same word trailing a prompt as a bare quality plea softens the whole
> frame instead — the distinction lives in `negative-constraints.md`
> § Whole-Frame Degradation.

### Anti-Slop Vocabulary

Kill these words — they add zero information and waste tokens:

| Slop Word | Replace With |
|-----------|-------------|
| beautiful | (delete — describe the specific visual instead) |
| stunning | (delete — describe what makes it striking) |
| epic | large-scale, sweeping, towering |
| amazing | (delete — show, don't tell) |
| dynamic | fast-tracking, whip-pan, handheld |
| energetic | sprinting, jumping, arms pumping |
| cinematic camera movement | slow dolly push / crane up / tracking shot |
| cool transition | match-cut / whip pan / smash cut |
| cinematic / cinematic lighting | a **named referent** — a director ("Wes Anderson symmetry"), a lighting setup ("golden-hour backlight, long shadows"), or a lens spec ("anamorphic 2.39:1, lens flare from a practical light") |
| high quality / high-res / 4K look | (delete — resolution is a render setting, not a prompt word) |

> **Why the substitute matters, not just the deletion:** generic adjectives are
> high-frequency labels spread across a huge, diffuse slice of training data, so
> they pull the output toward nothing in particular. A director name, a lighting
> setup, or a lens spec samples a *narrow, well-trained* distribution and
> actually moves the result. For the Seedance-specific treatment of this, see
> `higgsfield-seedance.md` § Prompt-Craft Laws → Name the thing.

### Physics Language

Use concrete physics consequences instead of mood words. The model responds to observable, physical details:

- ~~"powerful punch"~~ → `fist connects, sweat flies off in slow motion, opponent's head snaps back`
- ~~"dramatic entrance"~~ → `door slams open, dust erupts from the frame, light floods the dark room`
- ~~"fast car"~~ → `tires spin, gravel sprays backward, chassis drops as acceleration kicks in`

### Degree Adverbs

The model cannot infer intensity from images alone. Use adverbs to guide interpretation:

`slowly`, `dramatically`, `violently`, `gently`, `frantically`, `deliberately`, `cautiously`, `explosively`

**Example:** "She turns **slowly**, eyes narrowing **deliberately**, then **explosively** lunges forward."

### Three-Act Rhythm for Action

One optional rhythm for an impact event is the arc below. Use it when its cause and result
fit the story; it is not a required three-stage structure. A scene may open mid-action,
hold on a consequence, or develop through a different number of changes. Durations follow
the event and response, not equal thirds:

1. **Charge-up** — tension builds, energy gathers
2. **Burst** — the action explodes
3. **Aftermath** — physics consequences play out

**Example:** "The fighter plants her feet, fists clenching (charge-up). She throws a spinning kick that connects with the sandbag (burst). The bag swings violently, chain rattling, sand dust puffing from the seams (aftermath)."

### No Negative Prompts

Cinema Studio 3.0's generation engine does not support negative prompt syntax. Do not write "no blur" or "avoid shaky camera." Instead, use positive constraints — describe what you WANT:

- ~~"no shaky camera"~~ → `locked-off static camera, no movement`
- ~~"no blur"~~, meaning the whole frame is mushy → `sharp focus throughout, deep depth of field`
- ~~"no blur"~~, meaning the background blur ate the subject → `subject in sharp focus, background falling into soft bokeh`
- ~~"don't make it dark"~~ → `bright, evenly lit, overcast daylight`

The two depth-of-field spellings are not interchangeable — pick by which plane has to stay sharp (`negative-constraints.md` § Depth of field — two substitutes, two intents).

### Audio as First-Class Element

Describe audio separately in prompts. BGM, ambient SFX, and dialogue are handled as parallel tracks via dual-channel stereo generation:

```
A barista grinds coffee beans, pours steaming water over the filter.
Camera: tight close-up, slow dolly across the counter.
Style: warm tones, shallow depth of field.

Audio: the whir of the grinder, water bubbling through the filter,
ceramic mug placed on a wooden counter with a soft clink.
Soft jazz piano in the background, barely audible.
```

Sound design descriptions like "the scratch of frosted glass, rustling plush fabric, gentle tapping on acrylic" directly influence the generated audio output.

---

## Seedance 2.0 Scene Archetype Router

After the narrative plan and before filling MCSLA, identify a useful scene archetype.
It suggests camera behavior and spatial logic; it does not dictate stage counts,
durations, forced reversals, or a cut at every beat. Adapt the archetype to the actual
causal chain and ending.

### Action Archetypes

| Archetype | Camera focus | Space dynamic |
|-----------|-------------|---------------|
| **Pursuit** | Distance closing/opening. Pursued ahead in frame, pursuer behind | Path narrows/opens |
| **Duel** | Camera can favor the currently dominant side; shifts follow the actual exchange | Fighters contest position |
| **Impact** | Build-up slow → hit fast → aftermath slow | Point of contact = center |

**Decision tree:** Chase? → Pursuit. Two opponents trading advantage? → Duel. Single decisive contact moment? → Impact. None → default Duel.

**Duel heuristic:** changing advantage can make an exchange readable, but neither side
must lose dominance on a fixed beat schedule. A sustained advantage or one-sided assault
is valid when the story calls for it; name the actual dynamic instead of inventing reversals.

### General Archetypes

| Archetype | What changes | Camera signature |
|-----------|-------------|-----------------|
| **Journey** | Position in space — road, flight, walking | Tracking, aerial, traveling alongside. Landscapes pass. |
| **Atmosphere** | Nothing — mood IS the content. Rain on glass, empty street. | Minimal movement. Slow push-in or static hold. Micro-changes carry all drama. |
| **Reveal** | Hidden → visible. Door opens, fog lifts, camera rounds corner. | Pan, crane, dolly reveal. Camera controls WHEN viewer sees the subject. |

**Decision tree:** Subject moves through space? → Journey. Something hidden becomes visible? → Reveal. Nothing changes, mood is the content? → Atmosphere. None → default Atmosphere.

### Dialogue Archetypes

| Archetype | Power dynamic | Camera signature |
|-----------|--------------|-----------------|
| **Confrontation** | Both push; dominance shifts when an exchange earns it. | Tight OTS; motivate any axis crossing with a readable power shift. |
| **Interrogation** | Asymmetric — one extracts, one resists. | Low-angle on questioner, push-in on silence. |
| **Negotiation** | Balanced — both need something. | Symmetrical framing, matching shot sizes. |

**Decision tree:** Both pushing, dominance trading? → Confrontation. One extracting, one resisting? → Interrogation. Both need something, balanced? → Negotiation. None → default Confrontation.

**Dialogue pacing example:** ~25–30 spoken words may fit acoustically into 15 seconds;
reliable lip-sync budgets vary by model, language, and delivery (see
`higgsfield-audio.md`). Estimate the actual speech and reaction time. For an
explicitly requested compression, a power-shift line with setup and reaction is one
possible edit, not a mandatory three-line structure. Preserve approved dialogue and
source timing; if it does not fit, identify the conflict and use an authorized longer
runtime, multiple clips, or script revision.

---

## Seedance 2.0 Engine Constraints

These legacy Seedance 2.0 observations are remediation guidance, not verified universal
platform limits. Apply them to observed failures while retaining user direction and the
shared causal performance plan; verify actual model/mode limits separately.

### Character & spatial rules
- **Tracked-cast remediation.** If identities drift, try focusing coverage on a pair or trio with named interaction vectors; ≤3 is a legacy reliability suggestion, not a universal cast ceiling.
- **Exit/re-entry remediation.** If a returning character drifts, anchor their route, timing, identity and re-entry state or use matched coverage. Do not ban an intended continuous exit/re-entry.
- **Off-screen continuity.** State where a character goes, what changes and why, and what state returns. Show the cause when the viewer needs it; an explicit off-screen event may also carry continuity.
- **Spatial continuity breaks on cuts.** Re-anchor positions and facing direction after any cut. State movement direction explicitly ("moving left-to-right").
- **Avoid reflection shots** (blades, puddles, mirrors) — Seedance breaks scene geography when rendering reflections.

### Sensory rules
- **Only describe what can be seen or heard.** No smell, taste, or internal thoughts.
  - ❌ "The air smells of pine." ✅ "Pine needles covering the ground, wind moving through branches."
- **Micro-expressions work as physics.** ✅ "jaw clenches, nostrils flare." ❌ "looks angry."

> For the eight named substrate channels that micro-expressions
> decompose into, see `vocab.md` § Emotion as Visible Behavior —
> Channels.

### Action rules
- **Intent + named technique + visible mechanics.** Preserve a user-named move and the setup, force, direction, contact/miss and recovery that make it readable. During short-form remediation, simplify unsupported joint-angle precision without reducing the action to a state label.
- **Consequences and responses stay explicit.** "Thrown into the side door, metal buckling and glass scattering; she braces against the rebound and sweeps the attacker's leg" preserves the causal exchange. Keep object response, subject follow-through and lasting damage; remove only redundant description.

### Double-contrast cut technique

When an event benefits from a strong visual contrast, change **both** shot size and camera character. The scale runs `extreme wide → wide → medium → MCU → close-up → ECU`. Camera character: `Handheld | Static | Stabilized tracking | Crane | Aerial`.

**Single contrast:** MS handheld → CU handheld.
**Double contrast:** MS handheld → ECU static-locked.

Choose by narrative and spatial purpose. Repeated static dialogue coverage, match cuts and deliberate repeated compositions are valid; do not add a cut or change approved camera direction just to create variation.

### Inserts — causally motivated, named subject

Inserts focus attention on a detail at any shot size. A 0.3–0.5s static punctuation is
one example; a clue reveal or prop-state change needs enough time to read. Rules:
- **Give the insert a function** — punctuation, information reveal, or a visible state change;
  it need not become a new narrative stage unless the information changes the progression
- **Causally motivated** — the viewer must understand WHY they see this detail. Hero slammed onto hood → HIS hand gripping metal. Not: generic boot in a puddle.
- **Name the subject** — specify WHOSE body part or detail. Without attribution, Seedance renders wrong content.
- **Choose motivated contrast** — use double contrast when it improves the insert; retain intentional continuity and approved camera direction.

### Age-blind character rule

Never describe characters by age in Seedance prompts. Trigger words to avoid: *boy, girl, child, kid, young, teen, little*. Seedance age inference is unreliable and drifts across shots.

- **With image input:** describe by **role** (rider, figure, traveler, speaker), **clothing**, and **action**. Never label who they are — label what they do.
- **Without image input:** use functional labels: "a figure in a wool cloak," "a silhouette against the horizon."

### Default: in medias res

Starting already in progress can remove redundant setup. Use it when the cause, geography,
and stakes remain legible; preserve an opening setup or quiet hold when it earns a reveal
or reaction. Do not reserve or remove a fixed number of opening seconds. The user's
specified opening and ending remain constraints.

> Full Seedance director reference including bilingual EN+ZH JSON output format is available in `seedance-bilingual-json.md` — use it when you need the standalone director-mode prompt with scene-archetype routing and age-blind rules baked in.

---

## Related skills
- `higgsfield-soul` — Character consistency, Soul ID, micro-expressions
- `higgsfield-camera` — All named camera controls
- `higgsfield-style` — Visual styles, color grades, lighting
- `higgsfield-models` — Model selection
- `higgsfield-troubleshoot` — Fix failing generations
- `template-*.md` — Annotated genre-specific prompt templates
