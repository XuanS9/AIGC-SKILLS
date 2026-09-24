# Higgsfield Camera Controls

When using a supported platform camera preset, cite its **exact preset name**.
Free-prompted camera direction does not require a preset. In either case, make the
viewpoint, tracked subject, movement path and end framing explicit.

Plan coverage under [shared narrative planning](narrative-planning.md),
which governs full performance format and takes precedence over local creative defaults: a
**stage** is a dramatic event or state transition, a **shot** is continuous camera
coverage between cuts, and a **generation clip** is one model output. One shot
may span several stages; a stage may need several shots; a supported multi-shot
clip can contain several shots. Choose cuts and durations from what the viewer
must see and feel, then fit the coverage to the model's generation limits. A new
stage does not automatically require a cut or a new clip.

## QUICK FACTS
*Routing aids — read the linked sections for the actual rules.*
- Named preset tables by family: dolly / crane / orbit / zoom / follow / specialty / time-based / through-object / vehicle, plus angles and shot sizes — cite the **exact preset name when using a platform preset** [→](#dolly-movements)
- Compatible move combinations and static-pan/glide choices are coverage options; sequenced combos get explicit timing [→](#combining-camera-controls)
- **Emotion-sync is an optional camera strategy** — 7 registers offer examples; viewing needs and user direction determine coverage [→](#camera-emotion-sync--movement-per-focal-character-emotion)
- [OFFICIAL] Lens + aperture chosen by shot *purpose* (85/100mm F1.4 tight emotional CU … 45mm macro F2.8), with standing focus-lock and distortion-forbid clauses [→](#lens--aperture-by-shot-purpose)
- Shot duration by type: optional pacing examples from the [OFFICIAL] source, not quotas or generation limits; action, dialogue, and emotional readability set the length [→](#shot-duration-by-type)
- Micro-moves need exact distances — state total travel + time ("10–15 cm over 7 seconds"); never write `zoom` for a physical move [→](#micro-moves-need-exact-distances)
- Cinema Studio 3.0: One-Move Rule, genre presets, reliable phrasing library, camera transfer via `@Video` [→](#cinema-studio-30-camera-best-practices-businessteam-plan)
- What a `@Video` reference reads reliably (world, materials, physics, camera character) vs cannot do (frame-accurate continuation, identity) [→](#video-reference--what-it-reads-and-what-it-cant)

---

## Dolly Movements

| Control | What it does | Best for | Prompt phrase |
|---------|-------------|----------|---------------|
| **Dolly In** | Smooth linear move toward subject | Intimacy, revelation, tension build | "Camera Dolly In toward her face" |
| **Dolly Out** | Smooth linear move away from subject | Isolation, departure, widening context | "Camera Dolly Out revealing the empty square" |
| **Dolly Left** | Lateral track to the left | Following horizontal movement, revealing scene | "Camera Dolly Left tracking alongside the runner" |
| **Dolly Right** | Lateral track to the right | Following horizontal movement, revealing scene | "Camera Dolly Right as the car accelerates" |
| **Dolly Zoom In** | Dolly forward + zoom out simultaneously | Vertigo, shock, realization (Hitchcock effect) | "Dolly Zoom In — subject stays size as background rushes away" |
| **Dolly Zoom Out** | Dolly back + zoom in simultaneously | Overwhelm, isolation, world closing in | "Dolly Zoom Out — city swallows the figure" |
| **Super Dolly In** | Exaggerated fast rush toward subject | Sudden shock, urgent revelation | "Super Dolly In on the handprint on the window" |
| **Super Dolly Out** | Exaggerated fast pull back | Dramatic reveal of scale, sudden context shift | "Super Dolly Out to reveal the entire burning city" |

---

## Crane / Vertical Movements

| Control | What it does | Best for | Prompt phrase |
|---------|-------------|----------|---------------|
| **Crane Up** | Camera rises from ground/subject level upward | Reveal scope, transition intimate→grand | "Crane Up from the soldier's hands to the war-torn landscape" |
| **Crane Down** | Camera descends from high position | Introduce location from above, personalize | "Crane Down from the skyline to the lone figure on the street" |
| **Crane Over The Head** | Overhead god-like perspective, directly above | Vulnerability, surveillance, choreography | "Crane Over The Head — top-down view of the crowd" |
| **Levitation** | Smooth upward float, dreamlike | Mystical, transcendence, out-of-body | "Camera Levitates from her feet to her serene face" |

---

## Orbit / Arc Movements

| Control | What it does | Best for | Prompt phrase |
|---------|-------------|----------|---------------|
| **360 Orbit** | Full circle around the subject | Emotional isolation, dramatic emphasis | "360 Orbit around the boxer in the ring" |
| **Arc** | Semi-circular sweep around subject | Revelations, emotional turning points | "Camera Arcs slowly around the two detectives" |
| **Lazy Susan** | Slow turntable rotation, subject centered | Product shots, character intros, costume reveal | "Lazy Susan around the antique watch on the table" |
| **Robo Arm** | Precision mechanical arc, complex path | Choreographed scenes, product reveals | "Robo Arm sweeps from headlights over the roof of the car" |

---

## Zoom Effects

| Control | What it does | Best for | Prompt phrase |
|---------|-------------|----------|---------------|
| **Crash Zoom In** | Rapid sudden zoom toward subject | Shock, realization, emphasis on a detail | "Crash Zoom In on the bloody handprint" |
| **Crash Zoom Out** | Rapid sudden zoom away from subject | Disconnection, sudden wider context | "Crash Zoom Out revealing the battlefield" |

---

## Follow / Action Movements

| Control | What it does | Best for | Prompt phrase |
|---------|-------------|----------|---------------|
| **FPV Drone** | Fast agile drone-like weaving motion | Chase sequences, aerial action, kinetic energy | "FPV Drone chasing the motorcycle through the warehouse" |
| **Action Run** | Low follow shot behind running subject | Chase, escape, pursuit | "Action Run — camera low behind him, matching his sprint" |
| **Handheld** | Organic shaky hand-held feel | Documentary realism, intimacy, chaos | "Handheld camera jostling with the crowd" |
| **Head Tracking** | Camera locked to character's head movement | First-person intensity, disorientation | "Head Tracking as the boxer staggers after the punch" |
| **Snorricam** | Camera mounted on actor, background sways | Stress, drunkenness, heightened emotion | "Snorricam locked on her face as the room spins" |

---

## Specialty / Cinematic

| Control | What it does | Best for | Prompt phrase |
|---------|-------------|----------|---------------|
| **Bullet Time** | Subject frozen/slow-mo, camera sweeps around | Action climax, impact moments | "Bullet Time around the leaping assassin" |
| **Dutch Angle** | Camera tilted diagonally | Psychological tension, instability, dread | "Dutch Angle as the conspirators whisper" |
| **Fisheye** | Wide lens distortion, curved perspective | Surreal, skateboarding, experimental | "Fisheye lens capturing the skateboarder's trick" |
| **Whip Pan** | Fast lateral blur pan | Dynamic transitions, follow rapid action | "Whip Pan from the thief to the officer" |
| **Overhead** | Direct top-down bird's-eye | Choreography, spatial relationships, vulnerability | "Overhead shot of the dancers forming patterns" |

---

## Time-Based

| Control | What it does | Best for | Prompt phrase |
|---------|-------------|----------|---------------|
| **Hyperlapse** | Moving camera + time-lapse combined | City transformation, travel sequences | "Hyperlapse down the boulevard from dawn to dusk" |
| **Timelapse Human** | Fixed camera, human activity fast-forwarded | Daily routines, urban pulse | "Timelapse Human — subway platform, people rushing" |
| **Timelapse Landscape** | Fixed camera, nature/landscape over time | Weather change, seasons, sunrise/sunset | "Timelapse Landscape — mountain valley sunrise to dusk" |
| **Low Shutter** | Slow shutter, motion blur on fast movement | Speed, urgency, intoxication | "Low Shutter on the spinning dancer — silhouette blurs" |

---

## Through-Object

| Control | What it does | Best for | Prompt phrase |
|---------|-------------|----------|---------------|
| **Through Object In** | Camera passes through a narrow object into a new space | Reveal secrets, creative transition | "Camera glides Through Object In — through the keyhole into the dusty study" |
| **Through Object Out** | Camera exits through a narrow space revealing exterior | Confined-to-open transition | "Through Object Out — pulls back through the cabin window into the blizzard" |
| **Mouth In** | Camera zooms into a character's open mouth | Surreal transitions, entering memory/dream | "Mouth In transition — camera enters the storyteller's mouth into the fantasy world" |

---

## Specialty Vehicle / Action

| Control | What it does | Best for | Prompt phrase |
|---------|-------------|----------|---------------|
| **Car Chasing** | Low ground-level follow of speeding vehicles | High-speed pursuits | "Car Chasing — camera hugs the side of the black car through the streets" |
| **Car Grip** | Camera mounted on vehicle, rides with it | Immersive vehicle sequences | "Car Grip — fixed to the hood, shaking on every bump" |
| **Buckle Up** | Jarring, turbulent shaking camera | Rough rides, turbulence, loss of control | "Buckle Up as the car skids around the corner" |

---

## Pitch & Perspective — Camera Angles

| Control | What it does | Best for | Prompt phrase |
|---------|-------------|----------|---------------|
| **Low Angle** | Camera looks up at subject | Power, dominance, heroism | "Low angle looking up at the general on horseback" |
| **High Angle** | Camera looks down at subject | Vulnerability, smallness, exposure | "High angle looking down at the child in the empty hall" |
| **Eye Level** | Neutral height, conversational | Dialogue, documentary, grounded scenes | "Eye level, two characters facing each other" |
| **Bird's-Eye View** | Directly overhead, looking straight down | Maps, choreography, god-like perspective | "Bird's-eye view of the marketplace from above" |
| **Worm's-Eye View** | Extreme low, looking straight up | Towering scale, surreal, otherworldly | "Worm's-eye view looking up through the forest canopy" |
| **Ground Level** | Camera resting on the ground surface | Intimacy with terrain, small subjects, impact | "Ground level — ants marching across cracked earth" |
| **Canted Angle Left** | Tilted horizon, left lean (Dutch Tilt) | Unease, tension, psychological distortion | "Canted angle left as the hallway stretches ahead" |
| **Canted Angle Right** | Tilted horizon, right lean (Dutch Tilt) | Unease, tension, psychological distortion | "Canted angle right — the interrogation room feels wrong" |
| **Static Oblique** | Angled perspective, off-axis framing | Stylized composition, unease, visual interest | "Static oblique angle on the staircase" |
| **Over-the-Shoulder (OTS)** | Camera behind one subject's shoulder, facing the other | Conversation framing, shot-reverse-shot | "OTS from behind the detective, facing the suspect" |
| **POV / First Person** | Camera IS the character's eyes | Immersion, horror, subjective experience | "POV — hands push open the heavy wooden door" |
| **Two-Shot** | Two subjects framed together | Relationship, confrontation, dialogue | "Two-shot of the couple walking along the pier" |
| **Cowboy Shot** | Framed from mid-thigh up | Western standoffs, character swagger, action-ready | "Cowboy shot — hands hovering near the holster" |

---

## Shot Sizes

| Control | What it does | Best for | Prompt phrase |
|---------|-------------|----------|---------------|
| **Extreme Long Shot (ELS)** | Vast landscape, subject tiny or absent | Establishing location, isolation, epic scale | "Extreme long shot — lone figure crossing the salt flat" |
| **Long Shot / Wide Shot (LS/WS)** | Full body visible + surrounding environment | Establishing character in context, action scenes | "Wide shot of the dancer on the empty stage" |
| **Medium Long Shot / Cowboy (MLS)** | Mid-thigh up | Character stance, western standoffs, group dynamics | "Medium long shot — the three outlaws face the sheriff" |
| **Medium Shot (MS)** | Waist up | Dialogue, interviews, general narrative | "Medium shot — she leans against the bar, arms crossed" |
| **Medium Close-Up (MCU)** | Chest up | Emotional conversation, reaction shots | "Medium close-up as he reads the letter aloud" |
| **Close-Up (CU)** | Face fills the frame | Raw emotion, intensity, intimacy | "Close-up on her face — tears welling, jaw tight" |
| **Extreme Close-Up (ECU)** | Single feature (eye, hand, mouth) | Tension, detail, psychological intensity | "Extreme close-up on the twitching eye" |
| **Insert Shot** | Detail of an object or action | Plot detail, time pressure, texture | "Insert shot — the clock hand ticking past midnight" |

---

## Combining Camera Controls

Layering two compatible movements creates richer shots:

| Combination | Effect | Example |
|-------------|--------|---------|
| Dolly In + Dutch Angle | Closing tension + instability | Villain reveal |
| Crane Up + 360 Orbit | Epic reveal of scale + isolation | Final battle end |
| FPV Drone + Crash Zoom In | Kinetic energy + sudden focus | Chase climax |
| Handheld + Action Run | Raw realism + pursuit urgency | Escape sequence |

**Avoid conflicting simultaneous moves:** Don't request Dolly In and Dolly Out, or Crane Up and Crane Down at the same instant. A continuous shot may reverse direction at a motivated event with an explicit path and endpoint.

**Sequenced vs simultaneous combinations.** The table above lists *simultaneous* combinations (two motions happening at once). Production practice also uses *sequenced* combinations: pan to follow the character through phase one, then push-in on the face when the character stops. State the sequence with timing in the prompt — `Camera pans left from 0-3s tracking the character, holds, then pushes in on the face from 4-8s` — so the model renders the motions as discrete phases rather than collapsing them into a single ambiguous move.

**Static pan vs glide.** A camera that *pans* rotates from a fixed position; a camera that *glides* translates through space. Production practice prefers static-pan over glide for most coverage — the static-pan reads as a chosen viewpoint with directed attention, the glide reads as untethered. State which you mean: `the camera stays in position and pans to follow him` is distinct from `the camera glides alongside him as he walks`.

> **Negative constraints:** For temporal/consistency artifacts related to camera (contradictory
> movements, camera not working, static I2V) and their prevention phrases, see
> `negative-constraints.md` — Temporal/Consistency Artifacts section.

---

## Camera-Emotion Sync — Movement per Focal Character Emotion

The camera can act as the emotional double of the focal character when that
serves the scene. This is an optional strategy: choose movement, lens and duration
from user direction, viewpoint, spatial readability and the event. Deliberate
emotional distance, contrast or a held camera through an emotional change are valid.

Seven registers offer optional examples; timings and capture settings are not universal:

| Focal character emotion | Camera prescription |
|---|---|
| Anger / rage / tension / on edge | Handheld breathing, jittery and unstable — broken breath rhythm, visible micro-twitches in both axes, small amplitude, irregular rhythm. Avoid stabilizers. |
| Calm / control / confidence | Handheld breathing, smooth — steady breath rate, regular micro-amplitude. Stabilizer-light, but still alive. |
| Sadness / vulnerability | Handheld, slow, low — lower breath frequency, slight downward camera drift, weight feels heavier on the operator. |
| Shock / revelation | Optional static hold + slow push-in or pull-out; a 0.5–2s pause is one example, with duration set by the actual revelation and response. |
| Action | Optional 60fps / 180° shutter treatment for clean motion where supported; choose frame rate and blur for the intended look and actual platform. Put supported settings separately from prose. |
| Final beat / verdict | Optional top-shot freeze — directly from above, time stops, all positions locked. A 0.3–0.5s punctuation is one example; choose framing and length for the ending. |
| Emotional breakdown / character needs space | Slow pull-back from medium/close to wide — "leave the character alone." Production-team named technique for emotional moments (a character sobs, curls up, or otherwise needs to be witnessed-but-not-pressured); pulling the camera back gives the audience visual distance that registers as emotional space rather than abandonment. |

### Emotional arcs within a single shot

When the focal character's emotion *changes* across a continuous
take (e.g. rage → controlled in a single shot), the camera may
change with it if emotion-sync is chosen. Write that option as named phases:

- Opening phase: prescribe the camera for the entry emotion
- Transition phase: describe how the camera character shifts
  (handheld amplitude reduces, drift settles, push-in slows)
- Closing phase: prescribe the camera for the exit emotion

Tie any chosen camera change to a visible event; a steady viewpoint can also hold the arc.

> **For emotion-sync, clarify the emotion before picking the camera.** The 7
> emotional registers above are tracked by *named* emotions (anger,
> calm, sadness, shock). If the user supplies a generic emotion
> ("surprised", "tense") the first step is decomposing it into a
> specific named register — see `higgsfield-prompt.md` §
> Generic-Emotion Decomposition for the "which kind of X?"
> clarification template.

### Lens + aperture by shot purpose

`[OFFICIAL — Higgsfield shotlist-builder skill, 2026-07; re-authored from
the Chinese source]` — pick the glass from the shot's *purpose*, then say
both lens and aperture in the prompt:

| Purpose | Lens | Aperture |
|---|---|---|
| Extreme tight emotional close-up (forehead-to-chin fills frame) | 85mm or 100mm (FOV 29° or 18°) | F1.4 |
| Mid dialogue, two-shot | 50mm (FOV 47°) | F2.0–F2.8 |
| Wide / establishing | 35mm (FOV 63°) | F4–F5.6 |
| Insert / object detail (focus locked on the object) | 50mm or 85mm (FOV 47°/29°) | F1.4 |
| Macro (pores, droplets, fabric) | 45mm macro — no FOV-anchor equivalent; macro framing is described by subject scale in block prompts | F2.8 |

Two optional prevention clauses for a shot intended to hold focus and rectilinear
geometry; omit or adapt them when user direction calls for focus changes or distortion:

- **Focus lock on inserts and tight close-ups:** `"focus plane locked on
  [object] from first frame to last — no focus drift, no rack focus, no
  autofocus hunting."`
- **Distortion forbid on wide/fast glass:** `"straight rectilinear lines,
  no barrel or pincushion distortion, no fisheye, no wide-angle warp."`
  (For Seedance block prompts, FOV is stated in degrees instead of mm —
  `higgsfield-seedance.md` § FOV anchors; this table's mm/aperture
  vocabulary serves Cinema Studio and non-Seedance surfaces, and the
  *purpose→glass* logic transfers either way.)

### Shot duration by type

Assign shot duration after identifying the event, dialogue delivery, visible
response, or emotional arc. The ranges below are **optional pacing heuristics**
from the shotlist-builder source, not required lengths or a recipe for dividing
a 15s envelope. Hold a performance as long as it needs to read; cut when attention,
information, or causality calls for it. No fixed cut count or hero hold is required.

| Shot type | Illustrative edit duration |
|---|---|
| Flash establishing / hard-cut intro (split-second wide) | 0.3–0.5s for a flash; allow longer when the geography needs to register |
| One mid-length dialogue line | 3–7s |
| Wordless reaction with an emotional arc | 5–10s |
| Insert / wide / freeze | 0.3–2s |
| Emotional close-up with a full arc (e.g. 5–7 performance beats) | 8–15s |

These are editorial shot lengths, not API duration settings. A brief insert can
be trimmed from a legal generation; a longer take may need a supported extension
or connected clips with matched exit/entry state. Seedance 2.0's **4–15s** range
applies per generation, while other models and modes have their own limits.
Keep camera-move timing consistent with the chosen shot duration and verify the
result in the edit.

### Micro-moves need exact distances

For very slow dollies, state total travel **and** time, or the model
oversells the move: `"over the full 7 seconds the camera pulls back only
10–15 centimeters — slow enough to barely register. No zoom, no sudden
push."` Never write `zoom` for a physical move — name dolly / track /
push-in / pull-out.

**And run the check in reverse: the stated move must be able to produce the
stated end framing.** "A slow push" cannot end on an extreme close-up from a
wide, and a 10cm pull cannot land a full-body reveal. When move and end frame
disagree, the prompt is internally impossible — the model picks one and
improvises the other. Fix it on whichever side is cheaper: enlarge the move
(name the bigger travel) or shrink the framing change. `[EMPIRICAL —
third-party director-skill evaluations 2026-08-09; re-derived]`

---

## Cinema Studio 3.0 Camera Best Practices (Business/Team Plan)

> These best practices apply to Cinema Studio 3.0's generation engine, available exclusively on **Business and Team plans**.

### The One-Move Rule

For Cinema Studio 3.0 text-driven camera remediation, try **ONE primary camera move** per shot when stacked moves cause jitter, unwanted rotation or failures. This is a mode-specific reliability heuristic, not a universal ban on a continuous camera path.

**Wrong:** `Camera: dolly push forward while panning left and tilting up to reveal the skyline`
**Right:** `Camera: slow dolly push from medium shot to tight close-up over 8 seconds`

If that remediation needs separate coverage, use Cinema Studio 3.0's Custom multi-shot mode with explicit continuity; preserve an approved continuous take when the selected mode can render it.

### Genre-Based Camera Presets

Optional starting choices for this mode; the Avoid column flags common mismatches,
not bans on user-directed or motivated coverage.

| Genre | Primary Camera | Secondary | Avoid |
|-------|---------------|-----------|-------|
| Product / E-commerce | Orbit, slow push-in, static | Crane down reveal | Handheld, whip pan |
| Lifestyle / Social | Handheld, static, slow pan | Dolly alongside | Dutch angle, crash zoom |
| Drama / Narrative | Slow push-in, dolly pull-out, tracking | Crane up | Fast moves, snap zoom |
| Music Video | Whip pan, snap zoom, fast tracking | 360 orbit | Static (too boring) |
| Horror | Slow creep (dolly in), static hold, Dutch angle | Crane down | Fast tracking (breaks tension) |
| Action / Chase | FPV drone, tracking, handheld run | Crash zoom | Static, slow orbit |
| Landscape / Travel | Crane up, slow pan, drone flyover | Dolly out reveal | Handheld, tight shots |
| Comedy / Social | Static (deadpan), snap zoom | Whip pan | Slow dramatic moves |

### Reliable Phrasing Library

These phrases produce consistent, predictable results:

| Intent | Reliable Phrase |
|--------|----------------|
| No camera motion | `locked-off static camera, no movement` |
| Slow approach | `slow dolly push from medium shot to tight close-up over 8 seconds` |
| Follow subject | `handheld tracking following the subject, subtle shake, not chaotic` |
| Reveal scale | `crane shot rising from ground level to overhead` |
| Circle subject | `smooth 180-degree orbit at eye level, constant distance` |
| Dramatic zoom | `crash zoom from wide to extreme close-up on impact` |
| POV movement | `FPV camera weaving through the environment at walking pace` |

### Camera Transfer via @Video Reference

The safest way to achieve complex camera motion is to clone it from a reference:

```
Match the camera movement from @Video1. A dancer performs on a rooftop at sunset.
```

This bypasses the One-Move Rule because the model extracts camera data directly from the reference rather than interpreting text instructions.

### Dual Video Reference

Action reference and camera reference can come from DIFFERENT videos. Separate them clearly:

```
Reference @Video1 for the character's movement and choreography.
Reference @Video2 for camera movement only.
A martial artist performs a spinning kick in a dojo.
```

### Smart Mode (Cinema Studio 3.0)

Cinema Studio 3.0's "Smart" shot control delegates camera planning to the model. When you select Smart mode:

- The model auto-plans camera language based on the genre and scene description
- Trust it for genre-appropriate camera work — describe the **feeling** or **genre** rather than specific camera moves
- Best for: users who want professional-looking camera work without manual specification
- Override by switching to Custom multi-shot for per-scene camera control

**Smart mode prompt example:**
```
Genre: Drama. A woman sits alone at a café table, stirring her coffee absently.
She notices someone through the window and her expression shifts from sadness to surprise.
```
(No camera instruction needed — Smart mode will select genre-appropriate drama camera work.)

---

## Video Reference — What It Reads, and What It Can't

The repo documents `@Video` reference usage in several places (Camera Transfer above,
`higgsfield-motion` for action choreography, `higgsfield-style` for grade carryover,
`higgsfield-audio` for voice timbre, `higgsfield-cinema` for the Motion/Camera Sheet).
The capability boundary — what a video reference reads reliably, where it falls short,
and what it cannot do at all — is documented once here and applies across all those
use cases.

### What It Reads Reliably

A `@Video` reference reliably carries these properties from the source clip into the
generation:

- **World design** — the overall environment, set construction, lighting logic, color
  palette, atmosphere.
- **Material and texture** — how surfaces look (wet wood, rope, water behavior, fabric
  weight).
- **Physics and motion style** — how objects move, how water behaves, the weight and
  energy of action.
- **Camera character** — the overall feel of how the camera operates, its proximity to
  subjects, its movement vocabulary.
- **Production quality level** — high-budget vs. low-budget feel, the overall cinematic
  register.
- **Color grade** — tonal treatment, contrast, saturation level.
- **Weather and environmental conditions** — storm intensity, rain density, fog, light
  quality.

### What It Reads Less Reliably

These properties carry across inconsistently. Don't depend on them when designing the
prompt:

- **Frame-accurate action continuation** — asking the model to pick up exactly where
  the last frame ended is unreliable. The reference understands the energy and world of
  what was happening, not the precise final position of every element.
- **Exact character identity** — use an image reference for character identity locks,
  not a video reference. Video references read world and energy better than face or
  costume precision.
- **Specific dialogue or audio** — voice character can carry over but exact vocal
  performance is not guaranteed.

### Four Reference Patterns by Purpose

Make the reference's job explicit in the prompt. Pick the pattern that matches what you
want the reference to do:

| Purpose | Pattern |
|---|---|
| World continuity | `@Video1 — use for world continuity: same set construction, same lighting logic, same atmosphere, same production quality level` |
| Action energy continuity | `@Video1 — use for action energy continuity: same event still in progress, same intensity of impact, same physical weight and momentum` |
| Camera character + production feel | `@Video1 — use for camera character and production feel: same cinematic register, same operator presence, same overall quality` |
| Voice + performance style | `@Video1 — use for character voice and performance style: same vocal character, same delivery register, same performance energy` |

The pattern works because it tells the model which axis of the reference matters and
lets the rest of the prompt drive the new content.

### Hard Limits

This section concerns ordinary `@Video` reference conditioning, not Seedance 2.5's
native edit/extension or first/last-frame workflows. Those retain their master and
boundary contracts. Do not promise these outcomes from a generic reference alone:

- **Cannot continue a specific action from the last frame.** If the reference clip
  ends on a wave hitting a ship, the new clip will not automatically start with that
  wave still hitting. The reference supplies world context; write the new clip's
  opening action explicitly, inheriting the source tail state when continuity is intended.
- **Cannot override your prompt.** The reference informs the generation — it does not
  replace prompt instructions. Where prompt and reference conflict, the prompt
  generally wins on action and the reference wins on texture and world feel.
- **Cannot supply character identity alone.** Always pair a video reference with an
  image reference if character consistency matters.

### Load-Bearing Rule

**Prompt wins on action, reference wins on texture and world feel.** Write the prompt
for what happens; let the reference carry how it looks. Pair with an image reference
when character identity must hold.

---

## Related skills
- `higgsfield-seedance-vfx` — Video-to-video footage transforms: preserve a real handheld/driving camera move frame-for-frame while swapping the world or adding an effect, and add a timed camera move (crash-zoom, push-in, reveal pull-back) you never actually filmed
- `higgsfield-motion` — Named motion presets (VFX overlays applied with camera moves)
- `higgsfield-cinema` — Director Panel (18 Cinema Studio camera movements)
- `higgsfield-image-shots` — Camera angles and implied movement for still images
- `higgsfield-prompt` — MCSLA formula, prompt structure
- `higgsfield-style` — Visual styles to pair with camera choices
- `template-*.md` — Annotated genre-specific prompt templates demonstrating camera use
