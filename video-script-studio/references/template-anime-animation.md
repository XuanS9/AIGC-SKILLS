# Template: Anime Animation (Seedance 2.0)

Paste-ready workflow + prompt scaffolding for anime and stylized 2D
animation in Seedance 2.0 — fight scenes, peaceful beats, transformations,
and consistent-character sequences. Built around the layered
director's-grammar formula, with a reusable anime style block and a
character-turnaround prompt for identity locking.

## When to use this template

Reach for this when the user wants anime or stylized-2D motion — sakuga
action, transformation reveals, calm character moments, or multi-shot
anime sequences with stylized characters and environments. The
identity-lock and style-block pieces matter most when the same character
must stay consistent across shots.

---

## The layered prompt formula

Plan the video with [shared narrative planning](narrative-planning.md):
assets/references → goal and ending → global audiovisual and spatial rules → behavior
and rhythm → stages → continuity → final frame/handoff → constraints. These eight
layers organize meaning; compile them into the compact formula below, with the
constraint line last. Keep the reusable style, constraint, and static turnaround
blocks in their native formats.

Choose stage boundaries from events, causal turns, reveals, or state changes, then
choose shots for visibility and estimate action, reaction, dialogue, and transition
time. There is no preset stage count or equal-duration rule. A continuous shot may
span stages; a stage may need several shots or generations. Carry identity, pose,
prop ownership, transformation state, and sound across boundaries to the planned ending.

```text
SUBJECT + ACTION + ENVIRONMENT + CAMERA MOVEMENT + VISUAL STYLE + CONSTRAINTS
```

- **Subject** — who or what is in the scene. Feed Seedance the character
  visually (reference image or the turnaround sheet below) rather than
  describing them in words alone.
- **Action** — what changes or moves. One dominant action per shot. Request
  multiple shots when the event, reveal, or spatial readability needs them;
  allocate their durations after planning the changes.
- **Environment** — where it happens. A Soul 2.0 or GPT Image reference
  image for the location helps consistency.
- **Camera** — how the viewer sees it: low-angle, high-angle, dolly-zoom,
  pan, tilt, POV shots, multiple face close-ons.
- **Visual style** — the final identity (the anime style block below).
- **Constraints** — the IP-safe / format guardrails (last line, verbatim).

> Keep the subject consistent by repeating stable traits every shot (hair,
> outfit, posture, expression). For anime, consistency matters even more —
> the turnaround sheet gives the model far more geometry to hold onto than
> text descriptors do.

---

## Reusable anime style block (paste verbatim)

Drop this block into the **Visual style** layer of any anime prompt. It is
preserved as a single reusable string:

```text
2026 animation style anime animation, post time skip. 2d anime glow subtle
effect anime animation studios. subtle non precise cartoony. subtle non
precise animation style with clean, uniform-weight linework and simple, flat
cel-shading. The color palette is soft, muted, and classic animated. The
lighting is soft and even, with minimal directional influence from power
effects. Gradient shifts are minimized. The overall composition is
simplified. Make sure to get characters consistent. Give multiple faces
close-ons and different POV shots.
```

**IP-safe constraint line (always append, verbatim):**

```text
NO NSFW, NO COPYRIGHTED Content. NO TEXT, 16:9 video (no black stripes on
the borders), NO LOGO(S). RESPECT THE MANGA IMAGE PANELS. DO NOT USE IMAGES
AS STARTING FRAMES, BUT AS STYLE LOOKS.
```

The constraint line both fixes format (16:9, no borders/text/logos) and
keeps the generation inside content policy — it tells Seedance to treat any
uploaded manga panels as *style references*, not literal starting frames.

---

## Character turnaround sheet prompt (identity lock)

Generate a character spreadsheet first, then feed it as the subject
reference for every shot. Paste this prompt into an image model (Soul 2.0,
GPT Image 2.0, or Nano Banana Pro):

```text
A high-definition, clean, minimalist character design board / character
turnaround reference sheet, set against a pure white background. The overall
presentation should resemble a professional game art character modeling
sheet, fashion design reference page, character design sheet, or character
turnaround board. The layout should be neat and well-organized, with clearly
divided information sections, a realistic and premium visual quality,
consistent lighting, and strict character consistency throughout. colored.

On the left side of the composition, show the character's full-body
three-view turnaround (front, left-side, back full-body standing poses) as
the main visual area. All three figures must be the exact same character,
with identical facial features, hairstyle, clothing, body shape, and height
proportions. Arms hang naturally at the sides. Eye-level camera, neutral
studio lighting, no obstruction, no exaggerated perspective, no complex
background.

The upper-right section holds six headshot / head-angle references of the
same character (front portrait, slight downward angle, back-of-head, left
profile, near-side angle, 3/4 profile) with clear facial features and
consistent facial structure.

The lower-right section holds six close-up detail images in a clean grid
(upper-garment fabric texture, front lower-body clothing, hip/tailoring
detail, leg or skin texture, eyes/facial detail, shoes as a standalone
item). All detail images must match the main character's outfit and
appearance exactly.

Overall style: minimalist, professional, realistic, unified, clean, and
premium — sharp character edges, clearly defined garment shapes, natural
hair strands, refined skin, accurate material rendering, generous white
space, as if made by a professional concept art team.

Output: landscape composition, white background, full character visible, no
cropping, no extra props, no explanatory text, no logo, no watermark, no UI
elements, no like/save buttons, no social-media-screenshot appearance.
```

[Character appearance description] — or, better, swap in the turnaround sheet
you generated as the subject reference.

---

## Worked anime prompts

Shot counts and timings in source examples are illustrative, not mandatory:
"around 7 scenes, average ~2 seconds" describes one possible treatment, not a
stage count or a rule to make shots equal. Derive the actual schedule from the
chosen events and supported runtime before filling the prompt.

**Anime action / transformation:**

```text
In an epic sakuga anime animation, generate an unexpected transformation of
[character] into [describe]. Professional sound effects and motion, accurate
lighting, detailed close-ons. [Describe the necessary events and visible responses,
with each resulting transformation state carried into the next stage. Add shot
changes and timings only after estimating their performance needs. End on the
confirmed final form and composition.] Background should be [..] (check reference images).

[paste anime style block]
[paste IP-safe constraint line]
```

**Realistic handheld scene (for contrast with anime):**

```text
Generate a handheld shot of [character from reference image] but giant
(at least one skyscraper tall) doing the moonwalk down a famous city street,
destroying every high building as he dances, then kicking the buildings.
Continuous low-angle view recorded by a citizen. Dynamic composition and
intense action, handheld shaky shot. Dynamic music. Detailed realism,
lifelike video recorded on iPhone (no phone visible).
```

---

## Motion, style, and iteration notes

- **Control motion explicitly.** Specify how the body moves, how the camera
  moves, and how the environment reacts (wind in hair, drifting dust, light
  flicker). Combine a subject action with a camera move for energy — "the
  character turns sharply toward camera while the camera zooms forward
  slightly" reads far more alive than "dynamic."
- **Request shots explicitly when needed.** State what each view reveals and
  its entry/exit state. The source's "10 different shots from 10 perspectives
  in the first 10s" is an illustrative montage, not a pacing quota. Preserve a
  continuous take when the action reads clearly; vary shot lengths with the
  performance and music rather than adding cuts to fill time.
- **Match style language to the goal.** Anime → clean linework, flat cel
  shading, subtle glow, soft gradients, consistent design. Live action →
  natural skin texture, realistic depth, lens behavior. Prop close-ups →
  controlled lighting, reflections, material detail.
- **Iterate one variable at a time.** First pass: composition + motion.
  Second: camera + pacing. Third: style + consistency. Final: polish the
  strongest result. Faster than rewriting from scratch each time.

## Common mistakes

- Overloading the prompt with conflicting styles (realistic + cartoon +
  watercolor + toy-like at once → unstable output).
- Not describing motion; forgetting the camera; mixing too many characters
  in one shot; asking for too many unrelated actions.
- Vague words ("awesome," "insane," "beautiful") with no specifics.
- Changing style mid-prompt. One good prompt beats five messy ones.

