# Higgsfield AI Prompt Skill

**Current studio video route:** Seedance 2.5 `omni_reference` by default. Map
character/prop/scene images and reference video/audio to their specific attributes,
with real bound slots; a single image does not become an opening frame. Fast Path
model/mode defaults and legacy image-to-video examples below do not override this
project rule. Check platform parameters against the dated schema when executing.

**Language rule:** Reply in whatever language the user writes in.

**Separate types; sample before every prompt delivery:** Follow [sample approval](sample-approval.md). Write only the requested type: asset prompts or video prompts. A video request may reference existing assets or identify missing inputs, but must not include asset-generation prompts; asset delivery must not automatically start video writing. If both are explicitly requested, keep separate batches, samples, approvals and deliveries. Every new request, rewrite, extension, repair or single-prompt task must first provide a usable sample for the current batch and wait for explicit approval of that version. Prior style or sample approval does not approve a new batch; there is no skip-sample exception. After current-batch approval, deliver that batch fully without restarting approval. This takes precedence over immediate delivery, automatic pipeline expansion and no-commentary defaults below. Text-only samples are not generated or visually validated media. Preserve native output schemas and module capabilities.

**Merged studio planning:** For every video planning, prompt, shotlist, edit, or extension task, read [the shared director planning contract](narrative-planning.md) before the routed modules. Complete video prompts in every genre default to the visible structure and performance detail of the [user-approved full example](template-full-performance-example.md) and [cross-genre director template](template-general-director-2-5.md); read both in full before drafting. This project default takes precedence over short-form length recommendations. Keep concise, scoped and native-format outputs available on request and compile hard-limited submissions from the complete performance plan. Plan assets → goal → global audiovisual/space → behavior → event-driven stages → continuity → final frame/join → constraints, then compile into the module's native output. Stages, shots, and generation clips are distinct; derive their number and duration from events, performance, and legal model limits. Historical shot counts and time envelopes are examples, not universal defaults. Keep the HARD RULES below and every mode-specific capability; static-image, tool, and model-cost tasks retain their own workflows.

---

## HARD RULES — pre-delivery checklist

These rules apply to every Higgsfield response. They are written as a pre-delivery checklist the agent runs *before* sending the response, not as prohibitions stated and then forgotten. The failure mode they prevent is **plausibility-over-verification** — producing a response that looks correct because the agent's training data knows the rough shape of Higgsfield work, rather than because the agent actually read the skill files and verified the platform's ground truth.

**Before delivering any Higgsfield response, confirm in this order:**

1. **Routing line present.** First line of response names which sub-skills you routed to (e.g. "Routing to higgsfield-prompt + higgsfield-camera for an Atmosphere push-in"). One line, then the work. Missing routing line = response is incomplete; add it.

2. **Routed sub-skills opened and read in this conversation.** Match the user's ask to the routing table below, open the matching sub-skill files with the read tool, and READ them. Root `higgsfield-guide.md` and `higgsfield-prompt.md` are mandatory at minimum on any prompt request. Grepped snippets do not satisfy this rule. Full reads do. If your only access to `higgsfield-guide.md` or `higgsfield-prompt.md` in this conversation came from grep results, you have not satisfied this rule — open the file. Platform vocabulary, preset names, and model parameters must come from the files because this platform's lineup changes between releases.

3. **Named vocabulary verified, not invented.** Camera preset names, motion preset names, model names, CLI flag forms, and MCP tool parameter names all come from the skill files or from verification. For model parameters, enums, and durations, verify against `model-specs.json` first — it is generated from a dated `models_explore` snapshot (see `snapshot_date` inside the file); if the snapshot is stale (>30 days), verify live instead (`higgsfield model get <model>` for CLI param schemas; `models_explore` for MCP). If you found yourself thinking "this flag probably looks like X" or "this preset is probably called Y" — stop. Read the file or run the verification command. Plausibility is not validity. Do not substitute generic video-prompt vocabulary for named Higgsfield presets; do not invent model versions, camera presets, or motion-preset names. If the user names one you don't see in the skill files, say so and ask for clarification.

4. **MCSLA coverage intact on video prompts.** Model · Camera · Subject · Look · Action remain the five checks. In this project's eight-section performance format, model/settings live outside the copyable prompt and the other layers occupy their assigned sections; do not append a duplicate MCSLA block.

5. **Shared constraints checked and selected.** Consult `negative-constraints.md` for this shot's actual risks. Use applicable positive prevention phrases, respecting model/mode scope. Do not append whole tables or repeat locks already established; the final constraints section contains only remaining task-specific risks.

6. **Preflight surfaced when applicable.** If execution intent is signaled (CLI / MCP / bundled-skills mentioned) AND a video-class or high-cost model is named OR a budget concern is named, surface the two-step preflight (`model get` / `models_explore` for schema, then cost estimate). See `higgsfield-stack.md` § Preflight discipline.

7. **Aspect ratio is an enum, not a free-form value.** Check the model's allowed ratios against `model-specs.json` before writing them into the header; if the snapshot is stale (>30 days), verify live via schema (`models_explore` / `model get`). Example of why this matters: Seedance 2.0 supports native 21:9, Kling 3.0 does not. Anamorphic / 2.35:1 / 2.39:1 are *style register* vocabulary for the Look line, not output ratios. See `vocab.md` § Aspect Ratio: output spec vs. style register.

8. **Prompt under 200 words — short-form regime only.** This soft MCSLA cap applies when a short version is requested, not to the project's complete eight-section performance draft, even for a single shot. Production block scaffolds retain their structural checks (`higgsfield-seedance.md` § Official Prompt Architecture); a longer complete draft is not a rule-8 violation. Compile actual platform character limits into the submission version without losing the full causal plan.

**If any of items 1–8 are missing or unverified, the response is incomplete. Complete them before sending, not after.**

---

## What Is Higgsfield?

Higgsfield is a cinematic AI video and image generation platform built for filmmakers and
creators. Unlike single-model tools, Higgsfield hosts **multiple generation engines** on one
platform — Kling 3.0/3.0 Omni/3.0 Motion Control, Sora 2 incl. Pro/Max/Pro Max tiers (UI-only — confirmed in the UI 2026-07-06, absent from the API/MCP catalog), Google Veo 3.1/3.1 Lite, Wan 2.7/2.6/2.5,
Seedance 2.5/2.0/Pro, FLUX 3 Video, Minimax Hailuo 2.3/02, Higgsfield DoP (Lite/Standard/Turbo) for video; Soul 2.0, Soul Cinema Preview,
Soul Cast, Nano Banana Pro/2, Kling Image 3.0/Omni, Seedream 4.0, GPT Image 2.0,
Flux 2/Kontext for images — plus a library of 100+ named **Motion Presets**, a **Soul ID**
character consistency system, **Cinema Studio 2.5**, **Cinema Studio 3.0** (Business/Team plan), and **Cinema Studio 3.5** with Soul Cast AI actors, native dual-channel stereo audio, and 80+
one-click **Apps**.

---

## Input and output files

Read user materials at their supplied paths. Write deliverables to the user's project directory and report the resulting path. Keep generated files outside the installed skill; do not move source materials automatically.

### Fast Path — Simple Creative Requests

If the user provides a clear creative intent ("write me a prompt for a car chase at night")
with no specific constraints, **generate immediately** using these sensible defaults:

> **Fast Path still requires reading `higgsfield-prompt.md` first — Fast Path means skip clarifying questions, NOT skip the file read.**

| Parameter | Default |
|-----------|---------|
| Aspect ratio | 16:9 |
| Duration | 8s (Kling lanes — see Seedance exception below) |
| Style | Cinematic |
| Video model | Kling 3.0 (character-focused) or Seedance 2.0 (action/scale/references) |
| Image model | Soul 2.0 (portrait) or Nano Banana 2 (everything else) |

Do not ask clarifying questions. Deliver a ready-to-paste prompt. Mention the defaults
used so the user can adjust if they want something different.

> **Seedance exception:** Seedance 2.0 never gets a silently defaulted runtime
> (`higgsfield-seedance.md` — always ask, never default). On Fast
> Path that means: if the user named no duration, route video to Kling 3.0;
> pick Seedance 2.0 only when the request names a duration — or when the user
> asked for Seedance by name, in which case state the assumed runtime as the
> first adjustable default in the delivery.

> If you did not read `higgsfield-prompt.md` earlier in this conversation, read it now before writing the prompt.

### Full Path — Production Requests

When the user signals production-grade intent (Cinema Studio, multi-shot, specific model,
budget constraints, client work), **confirm before generating:**

**Required:**
- **Generation type**: Image / Video / App (one-click)
- **Video duration**: model-dependent enum — check the model's `duration` values in `model-specs.json` before offering choices (e.g. Seedance 2.0 4–15s, Veo 3.1 4/6/8s; image-to-video clips trend short)
- **Aspect ratio**: 16:9 / 9:16 / 1:1 / 4:5 / 4:3 / 21:9-where-supported (default: 16:9) — enums per model in `model-specs.json` (HARD RULE 7); anamorphic / 2.35:1 / 2.39:1 are **Look-line style register**, never output ratios
- **Model preference** (or ask Claude to recommend — see `higgsfield-models.md`)

**Optional (skip if user already provided):**
- Visual style: Cinematic / VHS / Super 8MM / Anamorphic / Abstract
- Soul ID character reference (if character consistency needed)
- Reference image for image-to-video
- Motion preset preference

> Ask everything in one message — do not split across multiple rounds.

---

### Route to the Right Skill

| User wants | Route to |
|------------|----------|
| User unsure which workspace/tool fits, or asks "what should I use for X" | `higgsfield-workspaces` |
| Write or improve a prompt | `higgsfield-prompt` + relevant sub-skills |
| Develop a character / world / story / premise before prompting, build a character sheet / story bible, lock a visual style ("visual DNA"), keep a character consistent across many shots, or "I keep getting generic AI characters" | `higgsfield-character-design` |
| Audit or strengthen a scene / sequence / beat outline before generating it, or "is this scene working", "what's weak here", "why doesn't this land" | `higgsfield-scene-engine` |
| Cinematic still image prompt (shot framing, angles) | `higgsfield-image-shots` |
| GPT Image 2.0 / gpt-image-2 prompt, UI mockup, infographic, character/reference sheet, layout-dense image | `higgsfield-gpt-image-2` |
| Choose the right model | `higgsfield-models` |
| Camera movement guidance (video) | `higgsfield-camera` |
| Named motion preset (Explosion, Werewolf, etc.) | `higgsfield-motion` |
| Visual style selection | `higgsfield-style` |
| Character consistency across shots | `higgsfield-soul` |
| **Consistency tie-break:** character consistency via a live Soul ID / reference images inside Higgsfield → `higgsfield-soul`; developing WHO the character is first (sheet, story bible, visual DNA) → `higgsfield-character-design`. Both may apply in sequence: design first, then lock with Soul. | — |
| VFX presets (Air Bending, Plasma, etc.) | `higgsfield-motion` |
| One-click App workflow | `higgsfield-apps` |
| Genre recipe (action, horror, romance, etc.) | `higgsfield-recipes` |
| Fix a failing generation | `higgsfield-troubleshoot` |
| Moodboard, style direction, Soul Hex color | `higgsfield-moodboard` |
| Visual consistency across a project | `higgsfield-moodboard` |
| Mixed Media presets (Noir, Sketch, Particles, etc.) | `higgsfield-mixed-media` |
| Photodump style preset / social-feed photo-dump aesthetic | `photodump-presets.md` (root reference) |
| Artistic style transformation, preset stacking | `higgsfield-mixed-media` |
| Higgsfield Assist (GPT-5 copilot) | `higgsfield-assist` |
| Credit optimization, plan selection, budget strategy | `higgsfield-assist` |
| Cinema Studio 2.5 / Cinema Studio 3.0 / Cinema Studio 3.5 / multi-shot sequence workflow / Soul Cast | `higgsfield-cinema` |
| Optical physics, camera bodies, lenses, Hero Frame | `higgsfield-cinema` |
| Elements system (@Characters/@Locations/@Props) | `higgsfield-cinema` |
| Director Panel, Speed Ramp, shot modes, Popcorn | `higgsfield-cinema` |
| Cinema Studio 3.0 Smart mode, @ references, native audio | `higgsfield-cinema` |
| Cinema Studio 3.5 — three-pill UI, Style Settings, Camera Settings, Manual Style, AI director toggle | `higgsfield-cinema` |
| User mentions Higgsfield Canvas, a node-based / node-graph workspace, an infinite board, chaining prompts→images→videos into a pipeline, Shared Canvas, or a ComfyUI-style node workflow | `higgsfield-canvas` |
| Multi-shot workflow, chaining tools, full production pipeline | `higgsfield-pipeline` |
| Short film, narrative sequence, Popcorn → video → assembly | `higgsfield-pipeline` |
| Vibe Motion, kinetic typography, animated text, infographic/data/presentation animation as **code** (Remotion — crisp text, exact colors, deployable, real-time edits) | `higgsfield-vibe-motion` |
| Audio design, dialogue cues, SFX, ambient sound | `higgsfield-audio` |
| **Standalone audio generation** — soundtrack, ambience bed, multi-speaker scene audio, Seed Audio 1.0 (`seed_audio`), TTS voiceover / narration as its own deliverable | `higgsfield-audio` |
| **Extend / continue an existing clip** — "make it longer", "what happens next / before", prequel, last-frame handoff, extension chains | `higgsfield-seedance` (§ Extension Prompting) + `higgsfield-pipeline` (§ Continuation & Extension Handoff) |
| **Prep assets / reference sheets before video** — character sheet, prop three-view, location plate, variety sheet for crowds | `template-character-asset-delivery.md` + `higgsfield-gpt-image-2` (props) + `higgsfield-soul` (people & crowds) |
| Audition / screen-test a designed character (how they move, speak, react) before scene generation | `higgsfield-character-design` (§ Screen Test / Audition) |
| Seedance 2.0 / Pro prompt, flagged prompt, credit waste on Seedance | `higgsfield-seedance` |
| **Seedance 2.5** — user names 2.5 / Dreamina / Jimeng, wants a single clip longer than 15s, wants to **edit** or **extend** a video that already exists, or supplies many image/video/audio references (up to 30/10/10) | `higgsfield-seedance-2-5` |
| **2.0 vs 2.5** (both say "Seedance"): needs 4K/1080p, a platform start/end frame, or a `genre` hint → `higgsfield-seedance`; needs >15s in one generation, video editing, forward/backward extension, or heavy multi-reference → `higgsfield-seedance-2-5`. 2.5 caps at 720p | — |
| **Character performance** — acting, behavior, mannerisms, tics, a gait, subtext, "my characters look wooden / dead-eyed / AI", keeping a character themselves across many shots, an acting master profile | `higgsfield-acting` |
| **Feature-film production pipeline on Seedance** — headless character sheets, location sheets, a scene geography block reused across shots, dialogue construction, iteration discipline, giants / crowds / threshold transitions | `higgsfield-seedance` (`higgsfield-seedance-hell-grind.md`) |
| **Transform footage the user already has** (video-to-video): "make a Seedance prompt for this video/clip", add a VFX element (set my head/hair on fire, transform my hand, make a limb invisible), swap the world/background around a preserved subject (desert, clouds, lava, neon city), put a giant creature behind me or on a landmark, relight/regrade to match, sync a crash-zoom/push-in to a line — a **real source clip** is the starting point | `higgsfield-seedance-vfx` |
| **Replace a VFX/3D pipeline with generation** — "can AI do this instead of VFX", put myself in this plate, put a creature in my footage, a dragon/monster shot without buying or rigging a 3D model, "how do I build a whole VFX shot", asset sheets → size-ref → locations → shots as one pipeline; also "my v2v keeps failing / turns to slop", scale drift between two subjects, which image model for faces vs creatures vs clothing vs locations | `higgsfield-seedance-2-5` (`higgsfield-seedance-2-5-vfx-pipeline.md`) |
| Precise facial expression / FACS / Action Unit codes (AU12, AU6…), forced or uncanny or mixed expression, close-up micro-performance, monologue/dialogue facial acting, "which AU code for anger/fear", FACS reference sheet | `higgsfield-facs` |
| "Make a shotlist", break a script/brief/treatment into many connected Seedance prompts, director's shotlist, global style prefix + `@`-glossary + named per-scene prompts as one editable HTML | `higgsfield-shotlist-director` |
| User has Higgsfield CLI / MCP / bundled skills installed and asks how this skill works alongside them | `higgsfield-stack` |
| User mentions `higgsfield auth login`, `higgsfield generate create`, `mcp.higgsfield.ai/mcp`, `/higgsfield:generate`, or asks "do I need both" | `higgsfield-stack` |
| User asks where the prompt construction ends and the CLI/MCP execution begins (handoff questions) | `higgsfield-stack` |

---

### Load Map — how much to read

The routing table says *where*; this says *how much*. Loads are cumulative — every path starts from HARD RULE 2's mandatory reads.

| Situation | Load |
|-----------|------|
| Simple creative prompt (Fast Path) | `higgsfield-guide.md` + `higgsfield-prompt.md` — nothing else |
| Any Seedance prompt | + `higgsfield-seedance.md` (+ the matching the Seedance `template-*.md` references file when the request is technique-shaped) |
| Multi-scene / sequence / script breakdown | + `higgsfield-shotlist-director` + `higgsfield-pipeline` |
| Model choice unclear or contested | + `higgsfield-models` + `model-specs.json`, `image-model-specs.json`, and `audio-model-specs.json` (the generated spec for the output type) |
| Budget / credits / plan question | + `higgsfield-assist` |
| Anything else | one routing-table row → that sub-skill; resist loading more than the row names |

### Check Templates for Genre Match

Before writing a prompt from scratch, check if the user's request matches a common genre
pattern. The `template-*.md` references contain 9 annotated example templates with line-by-line
breakdowns, recommended models, negative constraints, and variations.

| User request matches | Check template |
|---------------------|----------------|
| Chase, pursuit, action, parkour | `template-01-cinematic-action-chase.md` |
| Horror, scary, creepy, dread | `template-03-horror-atmosphere.md` |
| Fashion, editorial, lookbook | `template-04-fashion-editorial.md` |
| Sci-fi, cyberpunk, VFX, space | `template-05-sci-fi-vfx.md` |
| Portrait, character intro, close-up | `template-06-portrait-character-intro.md` |
| Landscape, nature, establishing shot | `template-07-landscape-establishing-shot.md` |
| Comedy, social media, TikTok, skit | `template-08-comedy-social-media.md` |
| Romance, intimate, couple, wedding | `template-09-romantic-intimate.md` |
| Dance, music, performance, concert | `template-10-dance-music-performance.md` |

Use the template as a starting point — adapt the example prompt to the user's specific
request. The annotations explain WHY each element works, helping you make informed
substitutions.

**Technique templates** (the Seedance `template-*.md` references) — structure templates for Seedance
prompts where the user request is technique-shaped rather than genre-shaped:

| Technique need | Template |
|---|---|
| Pre-visualize multi-character spatial geometry before prompting | `template-top-down-map.md` |
| Multi-character shot with cross-character relationships | `template-multi-character-anchor.md` |
| Single-character shot with position + pose + contact-point locks | `template-single-character-position.md` |
| Worked example: two-character anchoring end-to-end | `template-worked-example-two-character.md` |
| Anime / stylized-2D animation — layered formula + style block + character turnaround | `template-anime-animation.md` |
| Close-up facial acting via FACS Action Unit codes — beat-synced expression schedule | `template-facs-expression-beats.md` |
| Seedance **2.5** multi-reference brief — role map + staged beats with end states | `template-omni-reference-2-5.md` |

**Text-overlay templates** (the subtitle and speech-bubble templates) — paste-ready text-rendering
prompts for subtitle / speech-bubble overlays:

| Text overlay type | Template |
|---|---|
| Subtitle (dialogue-synchronized) | `template-subtitle.md` |
| Speech bubble (character-attributed) | `template-speech-bubble.md` |

---

### Build the Prompt Using the MCSLA Formula

Full MCSLA definition and prompt structure → `higgsfield-prompt.md`

Quick summary — five layers, every prompt:

| M | C | S | L | A |
|---|---|---|---|---|
| Model | Camera | Subject | Look | Action |

**Core rules:**
- Be specific — name camera presets, describe VFX concretely
- Keep prompts under 200 words (short-form regime — block-scaffold production prompts follow their own structural rules, HARD RULE 8)
- Subject → Action → Camera → Style is the most reliable order

---

### Output Format

**Single prompt:**
```
**Model**: [model name]
**Aspect ratio**: [ratio]  **Duration**: [Xs]  **Style**: [style]

[Prompt]

**Camera**: [camera control name]
**Motion preset** (if used): [preset name]
```

**Two versions (when style varies):**
```
### Version 1 — [Style Name]
[Prompt]

---
### Version 2 — [Style Name]
[Prompt]
```

**Output rules:**
- Output a clean, ready-to-paste prompt — no meta-commentary after
- Do not explain what every line does unless the user asks
- Always name the camera control and motion preset explicitly

---

## @ Reference Rules

- User uploads a document (script, bible, brief, reference notes): read it at the supplied path; keep the source in place.
- User uploads image: use `[reference image]` or describe it as "the provided reference"
- For Soul ID character: note "using Soul ID character reference" in the prompt
- For video extension: note "extend from [reference video], continue with..."
- For style transfer: note "match the visual style of [reference image]"

---

## Shared Resources

| Resource | What it contains | When to use |
|----------|-----------------|-------------|
| `negative-constraints.md` | All generation artifacts + prevention phrases, by category | Check before every prompt — append relevant constraints |
| `template-*.md` | 9 annotated genre templates with examples, models, annotations, variations | When user request matches a common genre — use as starting point |
| the character worksheet templates | 6 character-design worksheets (9-question sheet, story bible, visual DNA) | With `higgsfield-character-design` when developing characters before prompting |
| the Seedance `template-*.md` references | 9 Seedance technique templates: top-down-map, multi-character-anchor, single-character-position, worked-example-two-character, anime-animation, facs-expression-beats, footage-vfx-transform, global-style-prefix, omni-reference-2-5 | When Seedance request is technique-shaped (spatial blocking, multi-character anchoring, anime/stylized-2D, FACS acting, footage VFX, style prefix, 2.5 multi-reference) |
| the subtitle and speech-bubble templates | 2 text-rendering templates: subtitle, speech-bubble | When user request includes on-screen text rendering |

---

## Sub-Skills (auto-loaded as needed)

| Skill | Trigger |
|-------|---------|
| `higgsfield-workspaces` | User is choosing a workspace / asking "what should I use for X" / hasn't picked a tool yet |
| `higgsfield-prompt` | Any prompt writing or refinement request |
| `higgsfield-image-shots` | Cinematic image prompts — shot framing, angles, composition |
| `higgsfield-gpt-image-2` | GPT Image 2.0 prompts — three-format taxonomy (JSON / prose / meta-prompt), UI mockups, infographics, reference sheets |
| `higgsfield-models` | "Which model should I use?" / model comparison |
| `higgsfield-camera` | Camera movement questions (video) |
| `higgsfield-motion` | Named preset requests (Explosion, Werewolf, VFX, etc.) |
| `higgsfield-style` | Visual style / aesthetic questions |
| `higgsfield-soul` | Character consistency / Soul ID |
| `higgsfield-character-design` | Pre-production story bible — premise / world / 9-question character / story spine / visual DNA (before prompting) |
| `higgsfield-scene-engine` | Scene/sequence structural audit — Goal / Obstacle / Tactic / Reversal / Value Shift (before spending credits) |
| `higgsfield-apps` | One-click app recommendations |
| `higgsfield-recipes` | Genre scene templates |
| `higgsfield-troubleshoot` | Failed generations / quality issues |
| `higgsfield-moodboard` | Moodboard / Soul Hex / project-level style consistency |
| `higgsfield-mixed-media` | Artistic preset overlays (Noir, Sketch, Particles, etc.) |
| `higgsfield-assist` | Higgsfield Assist copilot / credit optimization / plan selection |
| `higgsfield-cinema` | Cinema Studio 2.5 + 3.0 + 3.5 / Soul Cast / color grading / optical physics / multi-shot / Elements / Smart mode / @ references / Style Settings / Camera Settings / Manual Style |
| `higgsfield-canvas` | Node-based Canvas workspace / infinite board / chain prompts→images→videos / named canvas patterns / build-free generate-paid cost model / Shared Canvas live collaboration |
| `higgsfield-pipeline` | Multi-shot workflow / tool chaining / full production pipeline |
| `higgsfield-vibe-motion` | Vibe Motion — motion graphics / kinetic typography / data animation as **Remotion code** (crisp text, exact colors, deployable) |
| `higgsfield-audio` | Audio design, dialogue, SFX, ambient sound for audio-capable models |
| `higgsfield-seedance` | Seedance 2.0 / Pro prompt director + content-filter preflight linter (+ `higgsfield-seedance-hell-grind.md`, Higgsfield's open-sourced feature-film pipeline) |
| `higgsfield-seedance-2-5` | Seedance 2.5 omni-reference dialect — the four modes (t2v / omni_reference / video_edit / video_extension), reference-role grammar, 30s staging, editing + forward/backward extension, keyframes, storyboards, blockouts, transitions (+ `higgsfield-seedance-2-5-vfx-pipeline.md`, the AI-VFX production pipeline: asset-class model routing, size-ref frame, the `omni_reference` v2v lane, the four-batch rule, the slop catalog) |
| `higgsfield-seedance-vfx` | Video-to-video footage transformation for Seedance 2.0 — preserve a real subject + camera move, add a VFX element / swap the environment / drop a photoreal creature / relight to match / sync a timed zoom, run in std 4K |
| `higgsfield-acting` | Character performance as behavior under pressure — objective / obstacle / tactics / beats / subtext, body + status + proxemics, mandatory eye life, the 150–220-word acting master profile and its per-scene rewrite, locked voice prompt |
| `higgsfield-shotlist-director` | Brief/script → one connected Seedance shotlist (style prefix + `@`-glossary + named per-scene prompts) as editable HTML |
| `higgsfield-facs` | FACS Action Unit codes for precise facial expressions in Seedance 2.0 — forced/uncanny/mixed expressions, close-up dialogue facial acting, emotion→AU recipes, FACS reference sheets |
| `higgsfield-stack` | User mentions the Higgsfield CLI / MCP connector / bundled skills, or asks how this skill coexists with those execution surfaces |

> Full vocabulary in `vocab.md`
> Full motion preset library in `higgsfield-motion.md`
> Model comparison in `model-guide.md`
> Example prompts in `prompt-examples.md`
> Shared negative constraints in `negative-constraints.md`
> Genre-specific annotated templates in `template-*.md`
