# Shared Negative Constraints Reference

Use this reference as an internal, task-specific prevention and diagnosis menu under
[shared narrative planning](narrative-planning.md). Preserve the techniques below, but
select only applicable risks not already resolved in the prompt. Do not append whole
blocks or turn fallback remedies into mandatory shot design. Model/mode examples and
historical platform observations require the relevant current specification check.
Independent generation blocks need their own identity/state anchors; connected stages
share global locks. User-approved choreography, emotion changes, silence, framing and
reference duties remain intact; diagnose a failure before proposing a changed technique.

---

## Body / Motion Artifacts

These occur when the model can't resolve complex physical actions in a single generation.

| Artifact | Why it happens | Recommended prompt phrasing to prevent it |
|----------|---------------|------------------------------------------|
| **Floating / extra limbs** | Model hallucinates additional appendages when character pose is ambiguous or occluded | "Anatomically correct, all limbs visible and naturally positioned" |
| **Limb merging** | Two characters too close together — model can't distinguish whose arm is whose | Keep characters at arm's length or use separate shots; "distinct body separation between characters" |
| **Unnatural body proportions** | Over-specified conflicting body descriptors (tall + compact) or extreme angles | Pick one body descriptor, keep it consistent; avoid contradictory size cues |
| **Jittery / stuttering motion** | Too many competing actions can overload a clip | Inspect readable action load; one main action plus 1–2 secondary is a simplification example, not a quota. Split overloaded clips with state handoffs |
| **Motion morphing on fast action** | Fast motion may exceed temporal coherence | Optional failure remedy: generate Slow Mo then speed up in post, only if compatible with the approved speed, audio and delivery; not the default for fast action |
| **Specific martial arts failing** | Named techniques may fail to resolve their causal contact | Preserve approved moves and explain direction, contact and response. Broader “general fighting energy” or “struggling” remains an optional abstraction only when the task permits replacing exact choreography |
| **Grappling renders as embracing** | Close-range physical contact is ambiguous to the model | Use plain text (not @ Elements) for action scenes; describe body positions, not grapple names |

---

## Face / Identity Artifacts

These occur when the model loses track of who a character is across frames or generations.

| Artifact | Why it happens | Recommended prompt phrasing to prevent it |
|----------|---------------|------------------------------------------|
| **Face morphing / shifting** | No Soul ID reference, or conflicting appearance descriptions in the prompt | Use Soul ID for multi-shot work; remove contradictory appearance descriptors |
| **Identity drift across shots** | Character description varies between prompts, or identity and motion mixed in one block | Copy-paste exact character description across all prompts; separate Identity Block from Motion Block (see `higgsfield-soul`) |
| **Character swap (two characters)** | @ Elements in action scenes — model confuses which character is which | Use @ Elements only in static/slow scenes; use plain text for action; put hero character first in prompt |
| **Face warping during camera moves** | Identity descriptors mixed with temporal/motion language cause the model to re-interpret the face each frame | Keep identity descriptors (face, clothing, body) in a static Identity Block; keep camera and motion in a separate Motion Block |
| **Wrong expression / frozen face** | No readable response or conflicting cues | Choose a few visible micro-expression/breath cues triggered by the event; an emotional change within a shot is valid and must unfold coherently |
| **Plastic / waxy skin** | Wrong model for character work, or over-smoothed description | Use Kling 3.0 or Soul Cast for realistic skin; add "natural skin texture, subtle imperfections" |

---

## Texture / Lighting Artifacts

These occur when the model misinterprets visual style or rendering instructions.

| Artifact | Why it happens | Recommended prompt phrasing to prevent it |
|----------|---------------|------------------------------------------|
| **Flickering textures** | Inconsistent style description across frames, or model fighting between two visual styles | Commit to one named style (Cinematic / VHS / Super 8MM / Anamorphic / Abstract); don't mix competing styles |
| **Over-lit / flat lighting** | No lighting specification in prompt — model defaults to even, generic lighting | Always specify lighting source and quality: "single side-light", "golden hour", "practical only" |
| **VFX preset looks cartoonish** | Wrong model for the preset type, or style conflicts with the effect | Grounded presets (Explosion, Freezing) → Kling 3.0/2.6; Stylized presets (Animalization, Multiverse) → Wan 2.5; add "photorealistic, physically accurate" |
| **Product shots look cheap** | No surface/background specification, generic lighting | Specify background surface ("raw concrete", "black velvet"), add texture cues ("surface catches light on edges") |
| **Style ignored / generic output** | Style described too vaguely ("make it look cool") or style not named | Use exact named style + specific color grade: "Style: Cinematic. Cold blue shadows, warm amber highlights, high contrast" |
| **Color grade inconsistency** | Different color descriptions across shots in a sequence | Lock color grade in a Moodboard or repeat exact color language in every prompt |

---

## Whole-Frame Degradation — quality words vs. look choices

Some tokens authors reach for to make an output feel filmic are read as instructions
about the **rendering** rather than about the subject, and a rendering instruction
lands on the entire frame. `film grain` dropped in as a quality note softens
everything in the image; `imperfect focus` takes the frame out of focus, subject
included.

**The governing distinction:** *content* may be imperfect — uneven light, an
asymmetric composition, a messy room, an operator's wobble. *Image quality* must be
sharp. Imperfection is a subject choice; it is never a rendering instruction.

That is why the same word is deliberate craft in one clause and expensive in another.
Three uses are legal and are used on purpose across this repo:

| Legal use | What it is | Where the repo does it |
|-----------|-----------|------------------------|
| **Look choice** | The stock or texture is the piece's declared register, named in the Style / Look slot with what it belongs to | `higgsfield-prompt.md` § Genre Router (a Music Video lead opens on "16mm grain"); `vocab.md` § Film Stock Emulation; `higgsfield-cinema.md` film-stock axis |
| **Optics as content** | A named optical event, happening to a named element, at a named moment | `higgsfield-seedance-production-patterns.md` § Prompted Imperfection as Realism (heat-haze swim, a brief focus hunt before lock) and its targeted motion blur as artifact concealment |
| **Plate matching** | Grain, blur and focus falloff matched to an existing plate so a composited element does not read pasted-in | `higgsfield-seedance-vfx.md` § Lighting integration; `higgsfield-seedance-2-5-vfx-pipeline.md` § Reverse-angle locations |

What degrades is the fourth use: the token dropped in bare, attached to nothing,
trailing the prompt as a general plea for realism.

| Written as a bare quality note | What the model does with it | Write instead |
|--------------------------------|-----------------------------|---------------|
| `film grain` (trailing, unattached) | Noise laid across the whole image; fine detail softens with it | Name it as a look with its stock and its home: "Super 8MM warm grain, soft vignette" — or as a plate match: "grain matched to the reference frame" |
| `imperfect focus` / `soft focus` / `dreamy` | Global sharpness loss — the subject goes soft along with everything else | Name the optical event, its element and its moment: "a brief focus hunt on the badge before it locks" |
| `edges not perfectly sharp` / `slight natural deviation` / `not completely stable` | Effective resolution drops; the frame reads mushy | Drop them, and put the imperfection in the *subject* instead — a crooked frame on the wall, a chipped mug, light reaching only one side of the face |
| `blurry background` | The subject blurs with it | Say which plane stays sharp — see § Depth of field below |
| `hazy` / `foggy` (unquantified) | Whole-frame fog, subject included | Keep for genuine aerial perspective, quantified and located ("haze ramps 20% → 70% behind the ridge"), with the subject's own sharpness stated |

`[UNPROVEN HERE]` — re-derived from a third-party prompting corpus and **not
A/B'd on our own material**. The probe that settles it is a two-arm 480p pair on
one identical shot: arm A ends on a bare `film grain, imperfect focus`, arm B on the
named-look substitute, compared for detail retention on the subject. Until that
runs this is a drafting preference, not a rule — nothing here blocks a prompt, and
no linter enforces it.

### Depth of field — two substitutes, two intents

"No blur" is two different requests and the positive substitute differs. Both
spellings used in this repo are correct; they are not interchangeable.

| What the author actually wants | Positive phrasing | Reach for it when |
|--------------------------------|-------------------|-------------------|
| Everything in frame sharp, front to back | "sharp focus throughout, deep depth of field" | Landscapes, establishing shots, group blocking, product-on-set where the background is information |
| The subject crisp and the background soft **on purpose** | "subject in sharp focus, background falling into soft bokeh" | Portraits, dialogue coverage, isolating one figure in a busy set |

The first answers "the whole image is mushy"; the second answers "the background
blur ate my subject." `blurry background` on its own answers neither, because it
never says which plane is meant to stay sharp.

---

## Temporal / Consistency Artifacts

These occur across frames in video or across multiple generations in a sequence.

| Artifact | Why it happens | Recommended prompt phrasing to prevent it |
|----------|---------------|------------------------------------------|
| **Static I2V output (barely moves)** | Prompt re-describes the static image instead of what should animate | Only describe what CHANGES or MOVES; add explicit camera movement and atmospheric motion ("dust floats", "steam rises") |
| **Camera movement not working** | Vague movement or mismatched preset | Write starting view, tracked subject, physical path and final framing. When using a platform preset, name it exactly in settings |
| **Contradictory camera movements** | Opposing simultaneous instructions | Distinguish sequential moves from simultaneous combinations; use a readable path, splitting clips only when complexity or mode requires it |
| **Scene continuity breaking** | Inconsistent identity/environment or missing entry state | Reuse identity anchors in independently generated clips; within one complete prompt keep global locks once and carry changed state |
| **Motion preset not visible** | Preset misnamed or unsuitable context | When a preset is actually selected, retain its exact name and define target, trigger and result |
| **Lip-sync desync** | Speech length, head motion, track format or mode can interfere | Use [audio diagnostics](higgsfield-audio.md) for the selected model/mode. A 3–8s window and reduced head motion are repair options; preserve approved dialogue and reaction time and check accepted file types |
| **Background music overriding dialogue** | Unwanted generated sound replaces a supplied output track | For an exclusive original-track task, anchor its playback/time range and remove competing generated sound. Rhythm or performance references follow their separate audio-use rules |

---

## Content Filter / Safety Artifacts

These cause generations to be blocked or produce sanitized output.

| Artifact | Why it happens | Recommended prompt phrasing to prevent it |
|----------|---------------|------------------------------------------|
| **Generation blocked (horror/dark content)** | Platform safety filters triggered by explicit content descriptions | Describe atmosphere, not explicit acts: "unsettling", "something is wrong", "dread"; use motion presets for horror effects |
| **Named real person blocked** | Content filter on celebrity / public figure names | Use character descriptions instead of real names; create original characters with Soul Cast |
| **Brand / IP name blocked** | Trademark/copyright filter on brand names | Describe the product by appearance ("a matte black insulated mug, minimal design, no branding") — never use brand names |
| **Weapon / violence filtered** | Explicit weapon or injury language triggers moderation | Describe "tension", "aftermath", or "impact" rather than graphic injury; use motion presets for VFX |

---

## Cinema Studio–Specific Artifacts

These only apply when working in Cinema Studio 2.5.

| Artifact | Why it happens | Recommended prompt phrasing to prevent it |
|----------|---------------|------------------------------------------|
| **Prompt rejected (too long)** | Cinema Studio has a 512-character hard limit; @ Element chips consume ~80–100 hidden chars each | Max 2 @ tags per prompt; keep visible text under ~250 chars with 2 tags, ~350 with 1, ~450 with 0 |
| **@ Elements cause character swap in action** | AI re-processes reference data per @ tag, competing with action choreography | Use @ Elements in Scene 1 to lock characters, then use plain text descriptions in subsequent scenes |
| **3D Mode geometry holes** | Gaussian splatting can't reconstruct fully occluded areas | Use 3D Mode on images with clear depth and minimal occlusion; avoid extreme angles from the original generation |
| **Optical stack mismatch** | Camera/lens/aperture names put in the prompt field instead of the UI dropdowns | Never put optical stack language in the prompt — it belongs in the UI settings only |

---

## Cinema Studio 3.0 Notes

> **No negative prompt support:** Cinema Studio 3.0's generation engine does not support negative prompt syntax. Do not write "no blur", "avoid shaky camera", or any negation-based constraints. Instead, use positive alternatives:

| Negative (don't use with 3.0) | Positive alternative |
|-------------------------------|---------------------|
| "no shaky camera" | "locked-off static camera, no movement" |
| "no blur" — meaning the whole frame is mushy | "sharp focus throughout, deep depth of field" |
| "no blur" — meaning the background blur ate the subject | "subject in sharp focus, background falling into soft bokeh" |
| "don't make it dark" | "bright, evenly lit, overcast daylight" |
| "avoid jittery motion" | "smooth, fluid motion, one action per shot" |
| "no extra limbs" | "anatomically correct, all limbs naturally positioned" |
| "don't change the character" | "consistent character appearance, same outfit and features throughout" |

> **Prevention phrasing for 3.0:** All the prevention phrases in the tables above still work with Cinema Studio 3.0 — they are written as positive constraints by design. The key difference is that Cinema Studio 3.0 requires ALL constraints to be positive. The constraint blocks in this file are already compatible.

---

## The words you write are the words you summon

`[FIELD — Higgsfield Studio, RED FLAG + ONEIRIC + ADILIADA breakdowns, 2026-08]` The studio
that publishes these models states the rule as one of four things that hold a production
together: **"Say what you want, not what you avoid — the words you write are the words you
summon, including the ones inside a 'no'."** Two field cases make it concrete.

**The colour war.** A film committed to cold teal-green corridors kept having them flipped
warm yellow, because the references themselves leaked it — a lit window here, warm globe
lamps there — and the model amplified it. **Negative lists ("no yellow") did nothing.**
What worked was positive, with a budget and a failure condition:

```
The dominant color must be cold teal-green. Yellow exists only inside
the lamp bulb and a palm-sized halo beneath it. If the frame turns
yellow, the frame is wrong.
```

Note the shape: it does not forbid yellow, it **allocates** it — one named source and a
stated size — and then gives the model a test it can apply to its own output.

**Overriding a reference in prose.** When a reference photo carried a glowing red window
that could not be cropped out, the fix was not a ban but a statement of fact about the
film's world:

> *"That window glowing in the reference is switched off in our film."*

The model accepted it. A reference is not a contract — you can tell it what is different in
the shot, and saying so positively beats forbidding what the reference shows.

**Where this collides with a legitimate ban.** Two exceptions already documented elsewhere
in the repo: a property baked into an asset gets its garbage banned **at the asset stage
only** and then never mentioned again downstream
(`higgsfield-seedance.md` § Bake it into the asset), and a default the model
actively reaches for — slow motion in a fight — is worth naming because the untouched
default is already the failure (`higgsfield-seedance-failure-modes.md` § A fight
generated as separate clips). Outside those, prefer the positive form.

## How to Use This File

When building a prompt, scan the categories above that match the prompt's content:

1. **Character-focused prompt** → check Face/Identity + Body/Motion
2. **Action/chase prompt** → check Body/Motion + Temporal/Consistency
3. **Horror/dark prompt** → check Content Filter/Safety + Face/Identity
4. **Product/commercial prompt** → check Texture/Lighting
4b. **Prompt reaching for a filmic / imperfect / analog feel** → check Whole-Frame Degradation before writing the texture words
5. **Multi-shot sequence** → check Temporal/Consistency + Face/Identity
6. **Cinema Studio prompt** → check Cinema Studio–Specific + all relevant categories
6b. **Cinema Studio 3.0 prompt** → check Cinema Studio 3.0 Notes + all relevant categories (use positive alternatives only)
7. **Audio/dialogue prompt** → check Temporal/Consistency (lip-sync section)

Append the relevant prevention phrases to your prompt, or use them to catch and fix issues before the user generates.
