# Production checks

## Tier 1 — Workflow Discipline

### Pre-Prompt Confirmation Gate

Confirm intent in short form before composing a long prompt;
when stuck, prefer one narrow question over three open-ended.

**When to apply:** Output longer than a few sentences, or any sub-skill triggering expensive downstream work.


### Explicit-Stop Between Phases

Multi-phase workflows don't collapse into one response; each
phase produces an artifact the next phase consumes.

**When to apply:** Stateful loops where intermediate artifacts need user confirmation.


### Inventory-Extraction Checklist Before Composing

Silently catalog what the user provided — who / where / doing
what / with what camera / mood — before composing.

**When to apply:** Sub-skills authoring prompts from free-form briefs.


### Iteration-is-craft

Iteration is part of production. One historical feature-production case
reported roughly 1% image acceptance and 1.5% video acceptance; these are
case observations, not defaults for other projects. Estimate the current
work from its own scope and evidence, and label uncertain assumptions.

**When to apply:** Any sub-skill that produces generative output; any
budgeting or planning conversation; any post-clip diagnostic.


### Lock-before-generate

Lock subject, scene, camera, lighting, and coverage decisions BEFORE
prompting — not during. Decisions made during the iteration loop drift
from the original intent; decisions made before lock as anchors that
the iteration loop tests against.

**When to apply:** Any multi-shot or multi-character output; any work
that needs to hold consistency across cuts.


### Plausibility-over-verification

When the agent has training-data knowledge of *how a platform usually works* (typical CLI flag shapes, common aspect ratios, generic prompt structure), it can produce output that *looks* correct without actually checking against ground truth. The plausible answer is not the verified answer; the discipline is to run the verification command that is sitting right there.

**When to apply:** Any sub-skill where the agent could pattern-match from training instead of reading the skill files or calling a verification surface. CLI param schemas, MCP tool params, platform-specific vocabulary, model enum values.


### Falsifiable Success Criteria

Define what "good output" looks like in falsifiable terms BEFORE
prompting, so the iteration loop has a stopping criterion. The
discipline prevents the post-hoc rationalization failure mode —
claiming success regardless of outcome because no specific test was
committed to up front.

**When to apply:** Any project-level or scene-level work where
"finished" is not self-evident.


### 跨批次资产名称检查

资产样本、视频样本及完整交付均执行 [项目资产总表](asset-registry.md)：读取同一份项目总表，核对调用名逐字一致、中文名称与身份一致、没有为同一对象重复登记，并如实标记待生成与待绑定项。实际平台槽位按生成片段对照文件，不以槽位替代项目调用名。

含调用名时运行 `seedance_lint.py --preflight --file /path/to/prompt.txt --asset-registry /path/to/project/asset-registry.json`。脚本核对表结构、重复项、未知调用名、大小写和待补齐状态；正文换称、实际文件及平台附件仍需核对。提示词内部声明通过，不等于跨批次名称已通过。

### 电影视觉参考检查

剧情场景资产或视频交付前核对：

- 是否继承用户指定的具体电影主参考，或给出与题材匹配的单一推荐？
- 是否将片名落实为当前场景可见的光色、尺度、空间、材质，而非只写“大片感”“电影级”？
- 日夜、室内外与天气是否服从剧情，是否保留用户既定画幅？
- 是否保持人物身份和服装，避免自动引入参考电影的军队、载具、生物与地标？
- 场景资产是否仍是干净环境图，角色与 B/P 资产是否仍遵守各自背景规范？
- 文字风格参考、实际参考图及已生成结果是否如实区分，未虚构上传或验收？

方法见 [电影视觉参考匹配](higgsfield-style.md#电影视觉参考匹配)。维护文档只核查规则与链接；实际图片质感需待生成后验收。

## Tier 2 — Output Discipline

### Visual-Marker-Only Output Discipline

Describe characters and objects by visible markers (clothing,
build, posture, action, hair), not proper names, age labels, or
unobservable attributes. Visual markers carry across regenerations.

**When to apply:** Any prompt for image or video generation.


### Triple-Redundant Runtime

Runtime appears in title, meta header, and per-shot timing
labels — all three must agree, per-shot labels must sum to total.

**When to apply:** Multi-shot or time-anchored output.


### Single-Variable Iteration

Change exactly one variable per regeneration. Multi-variable
iteration makes diagnosis impossible.

**When to apply:** Iteration on close-but-not-right generations.


### Diagnose From the Current Output

Inspect the supplied image or video against the intended action, framing,
identity and continuity. Describe visible evidence, separate observed defects
from hypotheses, and mark anything you cannot inspect as unverified.

Repeated identical defects suggest a prompt or reference problem: change one
variable. If the prompt and references already satisfy the scene, another take
may help; do not invent acceptance rates or promise a successful reroll.


### BAD/GOOD/GREAT

Show output gradients explicitly — BAD, GOOD, GREAT examples
side-by-side — so the reader sees the difference, not just hears
about it. The contrast is what teaches; a single GOOD example without
a BAD comparison reads as one possibility rather than a chosen
direction.

**When to apply:** Any template, vocabulary, or pattern entry where
quality has a recognizable gradient.


### Anti-Bombast

Production-direction register. Avoid marketing voice, performative
urgency, fake confidence, and adjective stacks that describe what the
output should *be* rather than what the prompt should *do*. Replace
`epic`, `beautiful`, `cinematic masterpiece`, `ultra realistic`,
`dramatic` with named physical mechanisms (`low-angle 35mm anamorphic
medium shot`, `warm practical key light from screen-left`).

**When to apply:** Any prompt-construction surface; any documentation
the model or the user reads.


## Tier 3 — Architectural Discipline

### 3-Stage Chain / 4-Phase Loop Architectural Pattern

Multi-step production decomposes into named stages where each
stage produces an artifact the next stage consumes. Common shapes:
3-stage chain (character → image → video) or 4-phase loop
(script → assets → blocking → prompts).

**When to apply:** Orchestrating multiple generation stages.


### Select Shared Constraints by Shot

Check shared constraints for the shot's actual risks and model/mode scope.
Keep established identity and continuity locks consistent; do not append
an entire library or repeat locks already expressed in the prompt.

**When to apply:** Preparing a prompt or checking consistency across shots.


### Strict-Order Workflow with Refusal-to-Skip Phases

Sequential workflows enforce order — Step N+1 can't start until
Step N is approved. Skipping surfaces drift downstream.

**When to apply:** Numbered sequence where each step depends on the prior step's artifact.


### Pre-Delivery Discipline

Before delivering output to the user, run a self-repair pass against
a checklist of common failure modes — catch preventable issues at
construction time rather than after credit burn. The pass takes
60-90 seconds; the savings compound across iteration loops.

**When to apply:** Any sub-skill that produces a long-form artifact
(prompt, plan, template fill) where issues are easier to fix
pre-delivery than post-generation.


