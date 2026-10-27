# Higgsfield Shotlist Director

本模块负责用户选择HTML分镜时的交付容器；只要视频提示词时沿根入口交四段式文本，不因调用拆镜方法就额外交HTML。导演判断统一先执行 [导演决策流程](directorial-shot-design.md#导演决策流程)，HTML中的全局风格、资产表和进度不替代场景主次与镜头取舍。

Turn a brief into **one connected shotlist** — not a pile of separate prompts.
The deliverable is a single editable HTML artifact the user opens in a browser,
ticks scenes off as they shoot, and comes back to you to revise. This is the
document workflow for a multi-shot film: lock a global
look once, declare the cast/props/locations once, then emit named per-scene
prompts that all inherit both.

> **This module supplies the connected document workflow.** Read the project
> defaults in [the root skill](../SKILL.md), [shared narrative planning](narrative-planning.md),
> the [full director template](template-general-director-2-5.md), and the
> [full performance example](template-full-performance-example.md).
> Their four-section contract and performance detail drive prompt content;
> HTML retains the global Style Prefix, glossary, numbering, progress, copy
> buttons, and edit-once / per-scene overrides. Apply the selected model's
> grammar and applicable preflight checks: `higgsfield-seedance-2-5.md`
> for 2.5, `higgsfield-seedance.md` for 2.0/Pro. Optional native scaffolds
> do not override the full-video four-section contract.

**Current project defaults:** **Seedance 2.5 · 16:9 · Chinese**, unless the user has specified otherwise. Runtime inherits the approved film and sequence budgets; otherwise estimate it from action and performance. When no budget is set, each **generation clip** defaults to targeting the model's single-generation cap (~30s for Seedance 2.5): pack continuous multi-stage action into one near-30s generation and prefer merging adjacent shots into it, splitting when runtime, continuity, reference capacity or generation controllability requires it — never pad or slow motion to reach it. Shot and retained edit durations still follow content. Editing inherits the source timeline; extension follows its direction and mode limits. Apply [content-led shot segmentation](narrative-planning.md#按内容拆镜与估时): distinguish shot duration, generation duration and retained edit duration.

## QUICK FACTS
- **导演先于拆镜**：先定本段观众先看到什么、后知道什么、情绪转向、视觉命题、空间锚点与主动权，再决定镜头职责、景别、机位和切点；执行规则见 [顶级导演分镜方法](directorial-shot-design.md)。不得用固定秒数、固定镜头数或景别轮换代替导演判断。
- Output = **one self-contained HTML file** (inline CSS/JS, no deps), not loose prompts [→](#what-you-produce)
- Three structural layers, top to bottom: **Global Style Prefix → `@`-asset glossary → named per-scene prompts** [→](#the-three-layers)
- Per-scene prompt law: **four Chinese sections → HTML copy-blocks**; optional legacy `Style → Characters → Scene → CUT 1..N` mapping retains the full performance content. Cut and prompt boundaries follow visible events and state handoffs, with model-supported durations [→](#per-scene-prompt-law)
- Density heuristic (adapted from the historical source; current shared planning governs): group rows when they share cast, location, one emotional unit, and a manageable causal unit; consider splits at location cuts, cast changes, setup changes, performance arcs, inserts, or state handoffs when clarity or model limits require them — **don't fragment grief**; complexity budget + auto-enrichment defaults for thin briefs [→](#prompt-density--grouping-script-beats-into-narrative-units)
- **Shot density follows the selected scene scheme**：按重点与支撑决定切/留/镜内交接，等待可保留真实重量；题材不自动决定快切或慢推，连接过程可合并。
- Whole-sequence checks before delivery: **tempo budget** (story-led shot lengths reconcile to the requested edit runtime) + **monotony audit** (review repeated framing/moves for intent; holds are optional) [→](#sequence-tempo-and-variety)
- Continuity carries exits too: an **Off-screen line** (exit side + last state) per just-departed character keeps re-entry direction legal [→](#per-scene-prompt-law)
- **Edit-once-propagates**: change the prefix once → it changes in every prompt; per-scene **override** lets one scene break the global look [→](#edit-once-and-per-scene-override)
- Differentiators over a bare shotlist generator: **preflight linter**, **reference-role lanes**, **Elements `@`-auto-attach**, **failure-mode awareness**, **take review and selection** [→](#what-makes-this-outclass-a-bare-generator)
- Chinese prompt content by default; inherit the user's requested language. English legacy scaffolds remain optional [→](#workflow)
- Optional [historical calibration appendix](higgsfield-shotlist-director-historical-calibration.md): length, shot-duration and density references are examples, never timing quotas

---

## What you produce

A single `shotlist.html` (saved to the user's outputs and presented). It is
**self-contained** — inline CSS, inline JS, zero external dependencies — so the
user can open it offline and it just works. Structure:

1. **Title bar** — project name (infer from the brief; "Untitled" if unclear).
2. **Global Style Prefix** — collapsible block at top, applied to every prompt.
3. **`@`-asset glossary** — the cast/props/locations declared once.
4. **Scene list** — numbered scenes, each with a checkbox (progress saved in
   `localStorage`), a one-line scene description, and one or more copy-ready
   prompt blocks (`Prompt 3a · {{DURATION_3A}}s`, with `3b` and further continuations only as needed). Labels show generation duration; record intended edit use separately when trimmed.
5. A short "how to use" note (checkboxes auto-save; ask Claude to revise).

The collapsible Style Prefix is the document's single editable source. In each
connected prompt, compile global rules **once**, into their four-section homes;
individual stages describe changes and inherited state instead of repeating the
whole prefix. Each independently submitted generation block carries the minimum
self-contained style, asset roles, spatial anchors, entry state and constraints
it needs, so copying it requires no reassembly or reference to an unavailable
previous prompt. A full legacy prefix may be compiled once per independent block
when that format is requested. Do not prepend it again to a four-section prompt.

---

## The three layers

### 1. Global Style Prefix

A single editable style source inherited by all prompts — edit it once and
recompile all affected blocks. It locks the film's look, lighting, colour,
composition, acting register, physics and audio convention. Compile each rule
into its relevant section once; scene overrides replace only their named fields.
Resolution, frame rate and other platform settings are listed separately and
checked for the selected model/mode; style wording does not guarantee settings.

Ship the reusable fill-in-the-blanks block from
[`template-global-style-prefix.md`](template-global-style-prefix.md).
**Always check the conversation first** — preserve a user-supplied prefix in the
editable source, retaining its wording when compiling applicable clauses. If a
clause conflicts with confirmed requirements or actual model limits, surface that
conflict rather than silently changing it. Otherwise adapt the template to the
project's confirmed style and four-section structure; its sample technical
settings and audio convention are not universal platform requirements.

### 2. `@`-asset glossary

First load the shared project registry under [项目资产总表](asset-registry.md).
Derive this glossary from its existing entries; never rebuild or rename assets
for a new batch. Preserve exact handles and display names across asset prompts,
video prompts and samples. Keep per-clip platform-slot bindings separate from
project handles. The legacy names below illustrate syntax only; new S/C/B/P
names follow SKILL.md, and existing project names take precedence.

Declare every recurring asset once, with a stable `@`-name. For a Higgsfield
surface supporting **Elements**, register it with the **same name** and verify
the automatic image attachment when pasting. Otherwise map it to that surface's
supported reference slots. The names below are planning examples, not proof of
uploaded or bound assets; mark entries as planned / available / bound / verified,
and replace or remove unresolved placeholders before submission:

```
@hero — main character          @boss — side character
@headphones — product           @sneakers · @bag · @skydancer — props
@kitchen · @stadium · @street — locations
@s_hero — athletic-look hero     @s_hero_wet — sweaty post-run hero
@music_track — beat reference; bind the actual file after model/mode format checks
@street_schematic (image_1.png) — top-down position map
```

**Audio format is checked per model, mode and upload surface.** The Seedance 2.0
lane in [the audio guide](higgsfield-audio.md#seedance-20) documents MP3-only
reference input; the old `audio_1.wav` example must not imply WAV compatibility
there. The local 2.5 specs expose an audio-reference role but do not enumerate
accepted audio file formats. Verify that lane's actual upload requirements before
binding audio; mark format compatibility as unverified when evidence is missing.
A WAV post-production master or another audio model's WAV support proves nothing
about video-reference input. Keep the original master and make a compatible copy
when conversion is needed; do not infer support from a filename alone.

The slot→role discipline (`@Image1` = character, `@Image2` = costume, `@Audio1`
= rhythm…) comes from `higgsfield-seedance.md` § Reference Roles →
Per-Image Role Convention. **When a state variant is needed later, give it its
own locked registry entry** (for example `@s_hero_wet`) linked to the base asset,
and derive it from that base image. Follow SKILL.md: do not batch-create state
variants during the base-asset phase; ordinary transient states can remain in
the video prompt.

**Each glossary entry also carries a fidelity grade** — a role says what job the
asset does, the grade says how much of it must survive into the pixels:
*full-preserve* / *partial-preserve (name the parts)* / *attribute-transfer (name
the target it lifts onto)* / *loose-guide*. One word per line is enough
(`@headphones — product, full-preserve`); the grades and their prompt phrasing
live in `higgsfield-seedance-2-5.md` § Reference Roles → Fidelity.
Without a grade, "use @image4 for the coat" silently means whatever the model
felt like keeping that day.

### 3. Named per-scene prompts

Every scene is numbered (`1`, `2`, `3`…) and split into named prompts where dramatic events, causal turns, performance units, location changes, continuity handoffs, or model limits require separate generations (`1a`, `1b`, `2a`). One checkbox per **scene**, even when a scene needs several connected prompts. When no user budget is set, each generation clip defaults to targeting the model's single-generation cap (~30s for Seedance 2.5), merging adjacent shots into one near-30s generation and splitting when runtime, continuity, reference capacity or generation controllability requires it; there is no fixed prompt count, and clips are never padded or slowed to reach the cap. Each shot still has a viewing purpose and motivated cut; shots group or split according to continuity, complexity and actual model constraints.

Use [shared narrative planning](narrative-planning.md) to distinguish a **stage** (a dramatic event or state transition), a **shot** (continuous camera coverage between cuts), and a **generation clip** (one model output). A shot can span several stages; a stage can need several shots; a clip can contain multiple shots where the model supports them. These boundaries need not coincide.

Plan each stage as **entry state → main change → visible response → exit state**, then choose coverage and map it to generation prompts. Carry identity, position, props, emotion, and environmental changes across handoffs. Keep generation duration separate from the portion used in the edit: the local specs list **4–30s for Seedance 2.5** and **4–15s for Seedance 2.0**, subject to mode-specific rules and current platform verification. Neither range defines a scene template. Generate a legal clip and trim for a shorter editorial beat; use connected clips for longer scenes.

---

## Director gate before the shotlist

Use the single [导演决策流程](directorial-shot-design.md#导演决策流程) before rows or copy-blocks: scene change and priorities → audience knowledge and experience → blocking → compare hold, in-shot handoff and cut → performance timing → deletion/merge and reverse review. Reuse its brief in the existing project/shotlist notes; do not add another approval gate or duplicate the whole card.

HTML exposes the selected main scheme and important tradeoffs. Each row derives from the scene's core/support/connective function. A reaction close-up or insert is optional when it changes understanding or pressure; a meaningful hold is allowed without constant micro-actions. Missing detail can require another angle, an in-shot focus change, or a clearer action. The director chooses; do not ask the user to specify every shot.

## Per-scene prompt law

Default copy-block order is **【参考素材职责】→【一句话概述】→【具体情节】→【全局补充】**, including inside HTML. Use the linked director template to compile the selected scheme. 秒级时间轴 carries visible action, framing/viewpoint, light, camera path, inherited state and outcome; dialogue stays inline as speaker + delivery + `「台词」`, effects and ambience stay at their causes. Platform settings and director reasoning remain outside the copy text. Do not append a separate sound or final-frame column.

The HTML glossary and style prefix are editable document sources; resolve their applicable content into each independently copyable prompt once:

| Document source | Four-section destination |
|---|---|
| Real references and roles | 参考素材职责; directly reference independent assets, adding only necessary role/state/version; cleanup notes stay outside |
| Main event and key change/outcome of this Clip | 一句话概述; one concrete sentence explaining the segment; camera/style belong in timed action or global supplements |
| Timed action, performance, space, light and sound | 具体情节; the last timed beat includes final visible state |
| Stable identity, necessary continuity, sound/subtitle switches | 全局补充; settings remain outside |

Full performance means readable causality and handoffs, not equal detail emphasis on every small operation. NO BGM is the default. Cross-clip mixes remain post-production work, not a claim that one copy-block controls previous audio.

Only when the user requests the legacy format or the target requires it, compile
the same content into **Style → Characters → Scene → CUT 1..N**, adding the
continuity, final-frame and constraints fields. Language follows the user, Chinese
by default; English keywords in a scaffold are not an English-only model mandate.
Keep the full master in the HTML when a submission needs compression; do not attach
a duplicate long draft merely because the user requested HTML.

Legacy scaffold (field-derived example, not the current default):

```text
[STYLE — applicable global clauses once, with per-scene overrides resolved]

Characters:
[Only the characters in this prompt. @names + locked physical descriptors +
carried state — wet hair from the prior scene, strap on one shoulder, same
wardrobe unless it changed on screen.]

Off-screen (only when someone just left):
[Anyone in the PREVIOUS prompt but absent here: exit side + last visible state —
"Bo — exited frame-left, still carrying the crate." Carry for one prompt, drop
after two consecutive absent prompts.]

Scene:
[1–2 sentences. Where, when, and the geo-spatial blocking — where each character
sits relative to the location and to each other. "Hero at the kitchen island,
back to camera; the moka pot is on the left burner."]

CUT 1 — [framing, lens/FOV, camera move]:
[Beat-accurate action: gesture, eye-line, breath, micro-pause; what the camera
does; what the light does; diegetic SFX if relevant.]

CUT 2 — …

Continuity:
[Persistent state, performance, prop ownership and any explicit change nodes.]
Final frame / handoff:
[Visible exit state, framing, motion phase and sound carried into the next clip.]
Constraints:
[Only the exclusions relevant to this submission.]
```

Each prompt receives a duration after the dramatic unit is identified. **Do not target 15s by default and do not pad a prompt to fill a standard envelope.** Use the selected model's supported duration range and give a beat enough time for its action, reaction, reveal, or emotional hold to read. A single prompt may contain several simple cuts or stages when their causal progression remains clear; split when a new event, job, location, performance arc, or state handoff needs its own generation. Labels such as `3a/3b/3c` mean connected continuations, not preset timing or a required number of parts.

**Beat-by-beat choreography, not "he dances."** Generic motion verbs mean nothing
to Seedance — spell the move out: *"two crisp head nods on the beat, shoulders
rolling back one at a time, a soft knee-dip, a loose finger-snap, finishing on a
quarter-spin."* (Full pattern: `template-10-dance-music-performance.md`.)

**The Off-screen line is what keeps re-entries legal.** In the default format,
place the necessary exit state inside 【具体情节】 or 【全局补充】: anyone present in the previous prompt
but absent here retains their exit side and last visible state, including held
props, emotion, breath and motion phase. Carry this line into the next prompt;
after two consecutive absences it may leave the copy text, but retain the state
in scene notes so later re-entry still has a known boundary. The legacy scaffold
uses the same rule. Carried in-frame state alone does not record who just left;
check the re-entry side and hand-state against that record. `[EMPIRICAL — MiniMax H3 skill corpus; re-derived]`

**Match-cut via action phase.** Follow [动作同步与接缝去重](narrative-planning.md#动作同步接缝去重与整场节奏): inherit the same movement at the join, then continue its next phase. An already completed tap, shot or arrival does not restart in the next clip. Generation handles may overlap, but the edited event occurs once; actual cut and sound joins are verified in post.

---

## Prompt density — grouping script beats into narrative units

Adapted from the source labeled `[OFFICIAL — Higgsfield shotlist-builder + seedance-2-pro-director skills, 2026-07]`, under current shared planning: the shotlist's hardest judgment call is deciding which script beats belong to one generation. There is no fixed ratio or universal duration. First identify the causal unit and its visible state transition; then choose a model-supported duration that gives the unit enough room without dead air.

**Group script beats into ONE prompt when ALL of these hold:**

1. Same character set in frame
2. Same location or continuous spatial relationship
3. One continuous emotional and temporal unit
4. One causal unit whose action, response, and result can read clearly in the selected duration
5. The combined prompt stays inside practical length and model limits

**Consider separate prompts at these boundaries when the combined unit would lose clarity or exceed model limits; a stage or shot boundary alone does not require a new generation:**

1. Hard cut between locations or a meaningful time change
2. A major character entrance or exit changes the handle list
3. A lens or setup change needs its own narrative function
4. A performance arc needs room to develop and resolve; **do not fragment one continuous emotional collapse**
5. An insert or cutaway becomes its own information event
6. A new job, causal event, or state handoff begins

**Complexity budget per prompt** is a diagnostic, not a timing law: more than 2 strong actions, more than 2 camera moves, more than 3 important characters, more than 1 complex VFX event, or more than 1 location change usually indicates that the causal unit should be split. Assign the resulting prompts unequal or equal durations according to performance load and platform limits. A complex fight, chase, transformation, product demonstration, dialogue exchange, or quiet reveal each gets the space its own events require.

**When in doubt, protect the story beat.** Shorten a prompt when the event is simple and complete; extend it within the model limit when the reaction or reveal needs room; create a connected continuation when the platform limit is reached. Never add cuts, effects, or filler solely to reach a conventional duration.

**Thin briefs use director judgment.** Apply the shared decision flow: identify the scene's change, choose a visible behavior and an audience standpoint, then compare hold, in-shot handoff and cut. Inherit confirmed identities, plot, timing, medium and mode. Routine missing production details can be resolved without asking, but do not default every scene to a medium slow push or invent motives, props and reversals. Explain the main choice briefly in notes and compile concrete action. A missing plot fact that changes the result stays conditional or returns upstream; a lens preference does not require approval. Generation grouping follows shared planning after the edit scheme, never pads the scene to a cap.

For optional comparison, see [historical calibration](higgsfield-shotlist-director-historical-calibration.md):
source density examples, the duration ladder, shot-type ranges and field length
medians. These references never set stage count, force inserts, fragment an
emotional arc or reinstate a 15s target.

---

## Sequence tempo and variety

`[EMPIRICAL — third-party director-skill evaluations 2026-08-09; re-derived
heuristics, unmeasured here]` — two whole-sequence checks that no per-prompt
rule can catch, run once before delivery:

**Tempo budget — the arithmetic gate.** Identify the story's stages, director intention and coverage first, then assign shot lengths from action, dialogue, reaction, reveal, spatial reading and emotional workload. Do not derive cut count from runtime or equal time slices. A hold earns time through blocking, relationship, revealing information, pressure, or the audience experiencing waiting/loss; visible movement is not mandatory.
A hero hold is optional and lasts only as long as the beat needs; there is no
required money moment or 6–8s reservation.

When a total runtime is requested, the **final edit timeline must match it
exactly**. For straight cuts, sum the retained shot durations; account for
transition overlaps, handles trimmed away, and any retiming when applicable.
Count the final frame or hold within the last shot. Check each generation's
supported duration separately: raw clip durations can exceed the edited runtime.
If the story does not fit, revise coverage or pacing while preserving causal
clarity; do not add filler to hit a clip limit. Timing is a plan to verify in the
edit, not a promise of frame-accurate generation.

**Monotony audit — read the column, not the prompt.** After drafting, read only
the framing + camera-move line of every cut, top to bottom, as one column. A
run of **three consecutive cuts** sharing the same shot size *and* camera move
is a review flag, not a ban. Keep purposeful repetition, stillness, or a visual
motif; when every cut reads "medium, slow push-in" without narrative intent,
vary the shot's *function and scale* rather than inserting cuts just for variety. Per-prompt review can't see this
failure at all; it only shows when the column is read as a sequence, and it is
the single most common tell of a generated shotlist.

---

## Edit-once and per-scene override

Talk to the user's revisions like an editor of one connected document, never 20
loose chats:

- **"Edit prompt 1a, do X"** → change only that prompt.
- **"Change the style prefix to Y, apply everywhere"** → propagate to every
  affected prompt's compiled style fields in one pass, retaining explicit local
  overrides unless the user also asks to replace those overrides.
- **Per-scene override** → one scene can break the global look. Replace just that
  prompt's inherited lighting field (e.g. Scene 2 stadium: *"bright, genuinely
  sunny midday, strong frontal sun, deep blue sky, hard-edged shadows"*) while
  every other scene keeps the soft global lighting. Store the override as a local
  field replacement; unaffected fields still inherit future global edits. In a
  four-section block it appears in the relevant beat or 【全局补充】; in a requested legacy block
  it appears in Style. Do not append a second conflicting lighting instruction.

When revising, **re-render the same HTML file with the change applied** — don't
describe the change in chat. Preserve scene numbering where possible (don't
renumber everything for a one-prompt edit), preserve the Style Prefix unless told
to change it. The user's checkbox state survives via `localStorage` keyed by
scene number, so stable numbering = no lost progress.

---

## What makes this outclass a bare generator

A plain "script → prompts" generator stops at the document. This skill is wired
into the rest of the repo, which is the whole point:

1. **Preflight every prompt using its actual model and mode.** Run from the
   package root on each final copy-block, after resolving inherited style and
   overrides. The local CLI supports `--regime block` and resolves models from
   [`model-specs.json`](model-specs.json); it has no separate `--profile` flag. A supported
   example for a complete 30s, 16:9, prompt-only Seedance 2.5 submission is:

   ```bash
   python3 scripts/seedance_lint.py --preflight --regime block \
     --model seedance_2_5 --mode t2v --duration 30 --ar 16:9 \
     --file /path/to/prompt-1a.txt
   ```

   The file must contain the actual exported copy text. Use each generation's
   own duration, not the full edit runtime. For reference generation select
   `--mode omni_reference`; for editing select `--mode video_edit` and omit
   duration/aspect overrides (they follow the source); extension uses
   `--mode video_extension --extension-mode forward` or `backward`, with the
   source aspect and a legal added duration. When 2.0 is selected, use its real
   ID and mode, e.g. `--model seedance_2_0 --mode std`, with that clip's legal
   duration. These are lint settings, not generation commands.

   `--regime block` suspends short-form word caps, **not** the structural
   `zh-overlength` check: the current script flags Chinese-containing text over
   1,800 characters for every model, citing the older Seedance 2 house format.
   Record that finding honestly; it is not evidence of a 2.5 platform limit.
   Preserve the full performance master. Compile a shorter submission only for
   a verified target constraint or an explicit request; otherwise report the
   legacy-check mismatch without claiming a clean lint pass or forcing English.

   The script checks filter terms, recognized shot/time markers, declared
   parameters against local specs, and supported mode pairings. It does not validate all Chinese stage headings, the four-section
   content, bound media, audio codecs or generated pixels/sound. Manually check
   those and run § Sequence tempo and variety for the whole edit. Surface stale
   specs and unresolved findings; snapshot validity is not live verification.
   Retain preflight results in the shotlist notes; a static check is not a kept
   take. Verify the generated picture and sound against the intended scene.
2. **Reference-role lanes.** Keep registered project handles stable, and verify each generation
   clip's actual slot-to-file mapping. Upload order can change; `@Image1` must not
   be assumed to point to the same character across all prompts.
3. **Failure-mode awareness.** Flag high-risk shots at authoring time (reflections,
   same-character doubles, crowds, compound camera moves, door-entry geometry) per
   `higgsfield-seedance-engine-rules.md` and
   `higgsfield-seedance-failure-modes.md`, rather than
   letting them silently break a scene.
4. **Acceptance-rate honesty.** A finished scene may require many takes — keep
   candidates, test in motion, and lock the winner. The shotlist is the plan;
   iteration is still the skill.
5. **Audio as a driver.** When a `@music_track` locks the choreography, write the
   beat-sync mapping per `higgsfield-audio.md` § Audio as a Conditioning
   Input after checking reference format and role. Preserve the diegetic-only /
   score-in-post workflow where selected; for exact uploaded-audio output use
   that workflow's timestamp anchoring and avoid competing generated audio.
   A rhythm reference alone does not promise that the uploaded track is the output.

---

## Workflow

1. **Read the brief as a director, not a transcriber.** Read the root/shared
   norms and full templates linked above; inherit confirmed model, runtime,
   language, assets and ending. Apply the current 2.5 / 16:9 / Chinese
   defaults only where applicable; derive unspecified runtime from the content. Find where each scene turns, lands, and breathes.
2. **Lock the Style Prefix.** Custom from the conversation, or the template
   default.
3. **Build the `@`-glossary.** One entry per recurring asset; multi-state variants
   get their own locked entry.
4. **Direct the scenes.** Use the shared decision flow to select priorities, information order, blocking and cut/hold tradeoffs; remove redundant coverage, then map the edit scheme to supported generations. Project Clip IDs inherit root 批-序 numbering; UI scene numbers need not rename them. Preserve continuous performance across generation boundaries.
5. **Write each prompt** as the complete four-section performance brief in
   Chinese by default, inheriting the user's language choice. Compile it into
   HTML copy-blocks with resolved style and sufficient independent context;
   use the mapping above for a requested legacy scaffold.
6. **Preflight every prompt** with its model/mode; review state, timing, audio
   compatibility and high-risk shots, retaining unresolved findings for review.
7. **Generate the HTML** (skeleton below) and present it.
8. **On revisions**, re-render the file with edits applied; preserve numbering.

---

## HTML skeleton

Self-contained, dark directing-room aesthetic. Inline everything. Checkbox state
persists in `localStorage`; each prompt has a Copy button. The Style Prefix is
editable through revisions in the collapsible source block; each `<pre>` contains
resolved four-section text, including its applicable style once. The renderer
fills the glossary, settings, scene notes and preflight results as well as prompts;
the Copy button copies only that prompt. HTML-escape inserted text so reference
labels, `「」` dialogue and inlined sound cues survive as literal text. Use `lang="zh-CN"` by default
and change it when the user selects another language. The existing JavaScript
continues to handle copying and scene progress independently of prompt grammar.

```html
<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8">
<title>{{PROJECT_TITLE}} — Director's Shotlist</title>
<style>
  :root{--bg:#0e0e10;--panel:#17171a;--panel-2:#1d1d21;--border:#2a2a30;
        --text:#e8e8ea;--dim:#9a9aa2;--accent:#d4a259;--done:#4ade80}
  *{box-sizing:border-box} body{margin:0;background:var(--bg);color:var(--text);
    font-family:-apple-system,system-ui,sans-serif;line-height:1.5;padding:32px 24px 80px}
  .container{max-width:980px;margin:0 auto} h1{font-size:28px;margin:0 0 4px}
  .howto,details.style-prefix,.scene{background:var(--panel);border:1px solid var(--border);
    border-radius:8px;padding:14px 18px;margin-bottom:18px}
  details.style-prefix summary{cursor:pointer;font-weight:600;color:var(--accent)}
  pre{white-space:pre-wrap;font-family:"SF Mono",Menlo,monospace;font-size:12.5px;margin:0}
  .scene-header{display:flex;gap:12px;align-items:flex-start;margin-bottom:14px}
  .scene-num{font-weight:700;color:var(--accent);min-width:48px}
  .scene.done .scene-desc{text-decoration:line-through;color:var(--dim)}
  .prompt-block{background:var(--panel-2);border:1px solid var(--border);
    border-radius:6px;margin-top:12px;overflow:hidden}
  .prompt-label{display:flex;justify-content:space-between;padding:8px 14px;
    border-bottom:1px solid var(--border);font-size:12px;color:var(--dim);text-transform:uppercase}
  .copy-btn{background:transparent;color:var(--accent);border:1px solid var(--border);
    border-radius:4px;padding:4px 10px;font-size:11px;cursor:pointer}
  .copy-btn.copied{color:var(--done);border-color:var(--done)}
  pre.prompt{padding:14px 16px}
</style></head><body><div class="container">
  <h1>{{PROJECT_TITLE}}</h1>
  <div class="howto">完成后勾选场景，进度自动保存。
    复制按钮复制该生成片段的完整提示词（四段式及已合并的风格与连续状态）。可按编号请求修订。</div>
  <details class="style-prefix"><summary>全局风格源（修改后同步到各提示词，保留局部覆盖）</summary>
    <pre>{{STYLE_PREFIX_TEXT}}</pre></details>
  <div class="howto">{{ASSET_GLOSSARY_HTML}}</div>
  <div class="howto">{{PLATFORM_SETTINGS_AND_PREFLIGHT_HTML}}</div>
  {{SCENES_HTML}}
</div><script>
  document.querySelectorAll('.scene input[type=checkbox]').forEach(cb=>{
    const k='shotlist-scene-'+cb.dataset.scene+'-done';
    if(localStorage.getItem(k)==='1'){cb.checked=true;cb.closest('.scene').classList.add('done')}
    cb.addEventListener('change',()=>{localStorage.setItem(k,cb.checked?'1':'0');
      cb.closest('.scene').classList.toggle('done',cb.checked)})});
  document.querySelectorAll('.copy-btn').forEach(b=>b.addEventListener('click',()=>{
    const p=b.closest('.prompt-block').querySelector('pre.prompt');
    navigator.clipboard.writeText(p.textContent).then(()=>{b.classList.add('copied');
      const t=b.textContent;b.textContent='Copied';
      setTimeout(()=>{b.classList.remove('copied');b.textContent=t},1500)})}));
</script></body></html>
```

Each scene block in `{{SCENES_HTML}}` (one checkbox per scene, `data-scene` =
scene number as a string). Repeat prompt blocks only as needed; the two blocks
below illustrate a continuation, not a required pair. Resolve each duration
placeholder independently to a supported generation duration before delivery.
Record retained edit lengths or in/out points in the scene notes if they differ:

```html
<div class="scene">
  <div class="scene-header">
    <input type="checkbox" data-scene="3">
    <div class="scene-num">3.</div>
    <div class="scene-desc">主角随节奏穿过厨房，周围声音逐渐淡去。</div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label"><span>Prompt 3a · {{DURATION_3A}}s</span><button class="copy-btn">Copy</button></div>
    <pre class="prompt">[完整四段式提示词：参考素材职责、一句话概述、具体情节（按时间轴分镜、含段间承接与结束状态）、全局补充；已应用局部覆盖]</pre>
  </div>
  <div class="prompt-block">
    <div class="prompt-label"><span>Prompt 3b · {{DURATION_3B}}s</span><button class="copy-btn">Copy</button></div>
    <pre class="prompt">[场景3下一叙事单元或受模型上限影响的接续提示词：完整四段式、独立生成所需最小上下文、上一片段退出状态及本片段变化]</pre>
  </div>
</div>
```

---

## Related skills

- [Historical calibration appendix](higgsfield-shotlist-director-historical-calibration.md) — optional source
  tables and density/shot-duration references; no fixed timing or count quotas
- `higgsfield-seedance-2-5` — current default model's role map, mode workflows and
  parameter constraints, compiled from the shared four-section performance brief
- `higgsfield-seedance` — 2.0/Pro grammar and legacy scaffolds (six-slot formula,
  Prompt-Craft Laws, Reference Roles, preflight linter, engine + failure modes)
- `higgsfield-pipeline` — upstream multi-shot production planning the shotlist
  slots into
- `higgsfield-audio` — `@music_track` beat-sync + diegetic-only convention
- `higgsfield-soul` — locked character sheets the `@`-glossary points at
- `template-global-style-prefix.md` — the reusable prefix block +
  a per-scene override example
