# Higgsfield Seedance 2.5 导演（Higgsfield Seedance 2.5 Director）

> **工作室格式（Studio form）。**本文件记录 Higgsfield 原版英文块模板；代码块里的英文骨架保留原文作对照。工作室交付用同样的块顺序、中文块标签与字段：`[角色]` `[道具]` `[场景]` `[动作与声音参考]` `[生成目标]` `[具体情节]`（段头 `起s-止s｜景别｜视场角N°｜运镜`，分项 `画面/运镜/动作/表情/听者/声音/→ 结束`）`[视觉风格]` `[镜头]` `[声音]`（对白为计时行，第一秒定位 `{Hm.}`）`[保持一致]`，只有对白原句用英文。英文块标签在 `director_contract_lint.py` 中报 FAIL。格式归属：[跨类型导演模板 §1](template-general-director-2-5.md#1-块结构higgsfield--dreamina-seedance-25-标准)。

Seedance 2.5 是**与 Seedance 2.0 不同的写法体系**，不是可以凭习惯沿用的小版本升级。2.0 是参考驱动的镜头生成器，有首尾帧和 4K 通道。2.5 是**多参考制作模型**：最多 50 个参考素材、原生 30 秒时长，还有三种非生成模式：可以编辑你已有的视频，也可以从边界帧向前或向后延伸。

提示词语法也随之改变。参考职责用文字声明（`@Image 1 defines …`），音频和文字有括号语法，长视频用明确的结束状态分阶段。**当前工作室规则：**生成用 `omni_reference`；角色、道具和场景图、参考视频和音频各有属性职责，而不是帧锚点职责。哪怕只有一张图也只是普通参考。下面的旧关键帧示例是存档的模型示例，不约束当前项目的提示词。

> **模型分工：写任何东西之前先读这条。**2.5 最高 **1080p**（没有 4K 通道），也没有 `genre` 提示。自 2026-09-26 快照起，它开放了 `start_image` / `end_image` 媒体职责，**仅限 `omni_reference`**。任务需要 4K、`mode=fast` 或 genre 提示时，那就是 **Seedance 2.0** 的活：`higgsfield-seedance.md`。见 § Choosing 2.0 vs 2.5。工作室规则不变：项目提示词默认不用首尾帧；除非用户明确要求钉帧，图像一律是属性参考。

## 速查（QUICK FACTS）
- 当前工作室生成：只要附了至少一个真实参考就用 `omni_reference`，一个都没有就用 `t2v`（自 2026-09-26 快照起的平台规则：`omni_reference` 至少要 1 个参考，`t2v` 不带参考）；绝不虚构槽位。原生 `video_edit`/`video_extension` 需要另行核实的源时间线需求；平台也列出了 `t2v` [→](#模式路由the-mode-router)
- Higgsfield 参数面：**480p/720p/1080p**（无 4K），时长 **4–30 秒**，`start_image`/`end_image` **仅限 `omni_reference`**，`t2v` 不带参考，无 genre 提示，`bitrate_mode` standard/high，`extension_mode` 是 `video_extension` 必填、其他模式不可用 [→](#higgsfield-参数面the-higgsfield-parameter-surface)
- `video_edit` **忽略** `duration` 和 `aspect_ratio`，按源视频长度计费；`video_extension` 继承源视频的画幅 [→](#higgsfield-参数面the-higgsfield-parameter-surface)
- 每个参考素材都要有明确职责**和**排除项：“用什么”加“不用什么”；绝不让模型自己推断映射 [→](#参考职责说清用什么也说清不用什么reference-roles--say-what-to-use-and-what-not-to-use)
- 每个素材还要声明**保真等级**：完整保留 / 部分保留 / 属性迁移（写明目标）/ 松散参考；节拍文字用角色名（名字加一个可见标记），不用调用名 [→](#保真度说清每个素材要保留多少fidelity--say-how-much-of-each-material-must-survive)
- 素材预算：30 张图 / 10 段视频合计 ≤30 秒 / 10 段音频合计 ≤30 秒，最多 50 个素材（这是 Dreamina 的数字，平台只执行 30 张图和 50 个素材两条上限，平台的 `start_image`/`end_image` 两条都计入）；稳定范围是 1–8 个主体（图像），5–10 秒内 1–5 个主体（视频/音频）[→](#素材预算material-budget)
- 多参考是 5 步流程：映射 → 分组 → 档案 → 按场景选用，每个主体一行；`@Images 1 through 4 define four characters` 是标准反例 [→](#多参考五步流程multi-reference--the-five-step-workflow)
- 长视频要**分阶段**，不要写成段落：每个阶段一个主要变化加一个明确的**结束状态**；时间码分配的是预算，不是逐帧精确的剪辑点 [→](#长视频阶段与结束状态long-video--stages-and-end-states)
- 失败的镜头里物理和表演互相挤压时，拆开再拼接是一个可选补救；兼容的动作与反应仍放在一起 [→](#按任务拆而不只按长度拆split-by-job-not-only-by-length)
- 括号语法：`()` 音乐 · `<>` 音效 · `{}` 对白 · `【】` 字幕；非中文对白要在台词前写语言行 [→](#音频与文字括号语法audio-and-text--bracket-syntax)
- 当前制作：图像/视频/音频按属性分配职责；开场动作和最终状态用文字描述，不用帧锚点图。见当前职责映射 [→](#参考图视频与音频的职责reference-image-video-and-audio-roles)
- 编辑需要**唯一编辑母片**加编辑范围加时间线继承；延伸需要在写任何新内容**之前先对齐边界帧**：`higgsfield-seedance-2-5-mode-playbooks.md`
- 分镜网格、粗/细白模、一键成片、无缝转场：`higgsfield-seedance-2-5-mode-playbooks.md`
- **AI 视效制作流程**：按资产类型选模型、尺寸参照帧、场景批处理、`omni_reference` 的视频到视频通道（源 ≥4 秒，时长 = 源时长）、四批规则、劣质效果清单：`higgsfield-seedance-2-5-vfx-pipeline.md`
- 情绪用挑选过的**可观察**线索（2–4 个只是示例，不是配额）；小众运镜术语要翻译成可见结果 [→](#情绪引导与运镜术语emotional-direction-and-camera-terms)
- 真人角色公式有 7 个槽位，第 1 槽是**角色身份，绝不写年龄**：引擎的“不看年龄”规则优先于原指南的 `[Age/Race]` 标签 [→](#真人角色公式the-real-person-character-formula)
- 不能过度承诺的硬限制（帧精度、锁定参数、像素级一致的转场）[→](#硬限制不要过度承诺hard-limits--do-not-over-promise-these)
- Higgsfield 上**没有**的 Dreamina 产品功能：Ultra Long Video 180 秒、标注式编辑、Clay Renderer [→](#仅-dreamina-有higgsfield-没有开放的功能dreamina-only--what-higgsfield-does-not-expose)

---

## 来源（Provenance）

两个独立来源，全文都有标注：

| 标签 | 来源 |
|---|---|
| `[OFFICIAL — Dreamina]` | 字节跳动《Dreamina Seedance 2.5 提示词指南》与《用户指南》：模型厂商自己的提示词规则。提示词语法在模型端，所以在 Higgsfield 托管时同样适用。 |
| `[OFFICIAL — platform]` | Higgsfield 在线 `models_explore` 目录，快照 **2026-08-07**（`model-specs.json`）。参数、枚举和媒体职责只以这里为准。 |
| `[DREAMINA-ONLY]` | 背后没有 Higgsfield 参数的 Dreamina *产品*功能。绝不把它们说成用户在这里能做的事。 |

两者在“能设置什么”上不一致时，以平台快照为准：那才是 API 实际接受的。

---

## 共享叙事规划（Shared narrative planning）

在全部四种模式里应用 [共享叙事规划](narrative-planning.md)，包括首尾帧、关键帧、分镜、白模、一键成片和转场。先确定目标和结局，再从剧情事件、因果、揭晓和状态转变推出阶段，最后分配时长。不预设阶段数，不用等长区间。**阶段不是一次切镜，也不是一个生成片段**：一个镜头可以跨多个阶段，一个阶段可能需要几个镜头，一次生成在实际模式、复杂度和参考限制内可以承载几个阶段。

完整视频稿用中文的工作室块结构（`[角色]` … `[生成目标]` → `[具体情节]` → `[视觉风格]` → `[镜头]` → `[声音]` → `[保持一致]`），对白用英文。七个规划类别映射进这些块，不是七个输出标题。直接引用已登记的参考，不重复资产外观。对白 `{}` 写在 `[声音]` 的计时行里（`起s-止s｜说话人＋状态＋说：{line}`）；接触音效 `<>` 写在各段的 `声音：` 行；下面的 Dreamina 括号语法就是工作室格式。说话角色已登记的简短音色描述可以写进 `[角色]`。连续性体现在计时动作和必要的全局事实里。起稿前先读 [完整演出范本](template-full-performance-example.md) 和 [导演模板](template-general-director-2-5.md)。每个阶段都有时间/事件标题、展开的因果动作、对象或对手的响应、主体的接续、视觉结果、运镜路径和声音，以及继承的结束状态。单镜头和安静的戏也保留这种细节。明确要求原生格式时，把这些内容编译进职责映射、括号音频和各模式特有的指令，不另附重复的长文；局部编辑只改其范围。平台设置单独写。为转场和结尾画面留出预算，结果一直保留到有动机的改变为止。

`video_edit` 由源视频的事件和时间码决定编辑标注：保留母片的时长和时间线（允许文档记录的渲染误差），不把 `duration`/`aspect_ratio` 当控制项。`video_extension` 在分配新内容的预算之前，先锁定源视频接点的姿势、道具、动作相位/方向/速度、摄影机、光照和音频。向前延伸接源视频的结束状态；向后延伸接它的**开场状态**。源时间线保持不变。下面的参数限制仍是权威依据。

## 模式路由（The Mode Router）

当前工作室视频生成默认 Seedance 2.5 时，设置 `omni_reference`，把实际素材按属性映射。用户另选模型时，按该模型已核实的能力走；绝不声称不相关的模型支持 `omni_reference`。不要把单张图自动路由到帧锚点流程。无参考的文字走 `t2v`，因为平台会拒绝零参考的 `omni_reference`。用户要求精确的源时间或边界续接、且模式支持时，原生编辑/延伸是另一个选择；下面的平台模式目录是事实陈述，不是项目的默认选择器。

| 用户想要 | 模式 | 提示词是什么 |
|---|---|---|
| 只有描述、没有素材的片段（当前工作室） | `t2v` | 同样的块结构场景说明；`[角色]` 写明没有参考。`omni_reference` 至少要 1 个参考 `[OFFICIAL — platform, CLI rules 2026-09-26]` |
| 用他们提供的图/视频/音频构建片段（当前工作室） | `omni_reference` | 一份**职责映射**加场景说明，没有输入帧锚点 |
| 改动他们已有视频里的某样东西 | `video_edit` | 一份**编辑指令**：母片 + 范围 + 保留清单 |
| 在已有视频之前或之后补更多画面 | `video_extension` | 一份**边界约定**加新内容 |

由此得出两条规则：

1. **当前项目生成对所有提供的图像、视频和音频都用 `omni_reference`。**每个输入都有属性职责和排除项。单张参考图不决定开场构图；阶段顺序和结局写成动作和状态，绝不写成输入图帧锚点。需要严格保留时间线的源编辑/延伸，在核实实际模式支持后另行路由。
2. **编辑不是重新生成。**用户要重建镜头，那就是把旧片段作为动作参考的 `omni_reference`，不是 `video_edit`。`video_edit` 保留母片的时间线，只改其中一处有范围的东西。

> **视频到视频不自动等于 `video_edit`。**实地视效流程（换掉这条素材里的人，其余像素都不动）跑在**把源视频作为视频参考附上的 `omni_reference`** 里，因为这条通道的 `duration` 可设置，而且必须**与源视频一致**（因此源视频必须 **≥4 秒**，这是 `duration` 下限）。`video_edit` 是给时间线必须原封不动的母片做局部修改的通道。完整路由表和表演继承条款：`higgsfield-seedance-2-5-vfx-pipeline.md` § Stage 4。`[FIELD — AI-vs-VFX, 2026-08-08]`

---

## Higgsfield 参数面（The Higgsfield Parameter Surface）

`[OFFICIAL — platform, snapshot 2026-09-26]` · 引用前先对照 `model-specs.json` 核实（HARD RULE 3）。

| 参数 | 取值 | 说明 |
|---|---|---|
| `mode` | `t2v` · `omni_reference` · `video_edit` · `video_extension` | 默认 `t2v` |
| `duration` | 4–30 秒 | 默认 5，**`video_edit` 中忽略** |
| `resolution` | `480p` · `720p` · `1080p` | 默认 720p，**2.5 没有 4K**（1080p 由 2026-09-26 快照加入，尚无实地评分） |
| `generate_audio` | 布尔 | 默认 true |
| `bitrate_mode` | `standard` · `high` | 默认 standard |
| `extension_mode` | `backward` · `forward` | `video_extension` **必填**，其他模式**不允许** |
| 画幅 | `auto` · `21:9` · `16:9` · `4:3` · `1:1` · `3:4` · `9:16` | `video_edit` 中忽略；`video_extension` 中跟随源视频 |
| 媒体职责 | `start_image` · `end_image` · `image_references` · `video_references` · `audio_references` | `start_image` / `end_image` **仅限 `omni_reference`** |

目录里还有表格表达不了的**参考数量规则** `[OFFICIAL — platform, CLI rules 2026-09-26]`：

- `t2v` **不带任何**参考：没有图像/视频/音频参考，也没有首尾帧。
- `omni_reference` **至少要一个**参考（首帧或尾帧也算）。
- `start_image` / `end_image` **只**在 `omni_reference` 中接受。
- 图像参考 + 首帧 + 尾帧 **≤ 30**；全部参考 + 首帧 + 尾帧 **≤ 50**。

用户花额度之前值得先说明的三点：

- **`video_edit` 按源视频时长计费**，`duration` 和 `aspect_ratio` 都不能设：20 秒的母片无论改动多小，都按 20 秒渲染计费。
- **`video_extension` 继承源视频的画幅**；你只能设置延伸部分的*时长*。
- **没有 `genre` 参数。**2.0 的 genre 提示在这里不存在，题材写在提示词的视觉风格句里。

预检方式与 2.0 相同：

```
python3 scripts/seedance_lint.py --preflight --model seedance_2_5 "<prompt>"
```

lint 从 `model-specs.json` 读取枚举，所以超范围的时长、4K 请求、缺 `extension_mode` 的 `video_extension` 都会在渲染前被抓出来。

---

## 核心提示词公式（The Core Prompt Formula）

`[OFFICIAL — Dreamina]` 这个紧凑公式用于可选的短提交和原生字段编译。用镜头需要的部分，不注水；完整演出母稿保留共享格式和详细的因果展开。

```
<Subject> performs <primary action or event> in <scene and environment>.
The visuals feature <visual style>.
Use <shot size, camera angle, camera movement, or cuts>.
Audio includes <dialogue, ambience, sound effects, or music>.
```

- **主体加动作**是承重部分，要写具体。“男人在跑” → “男人加速冲刺，夹克被气流掀动”。
- **场景与环境**：地点、时间、天气、空间关系、背景状态。
- **视觉风格**：光照、色彩、材质、质感、氛围。只写增加信息的描述词。8K、高清细节之类的质量词可以保留；它们提供质量提示，但不能替代具体描述。`higgsfield-seedance.md` § Prompt-Craft Laws 的“用具名替代”规则照常适用。
- **运镜**：景别、角度、运动、焦点主体、转场。运动跟随动作，不是装饰。
- **音频**：对白、音色、环境声、音效、音乐，与画面同步。

**生成参数与提示词文字分开。**在生成页面或 API 上设置支持的分辨率、时长和画幅；在相应模式里尊重继承或锁定的值。文字里的时间段仍然用于分配表演和交接，但不设置 API 时长，也不承诺精确到帧的时机。

---

## 参考职责：说清用什么，也说清不用什么（Reference Roles — Say What to Use *and* What Not to Use）

只要有一个以上的素材，或者素材旁边还有文字描述，提示词就必须说明每个素材贡献什么。`[OFFICIAL — Dreamina]`

```
@Image 1 defines <subject>'s <appearance, clothing, structure, or material>.
@Video 1 defines <motion, camera movement, or pacing>.
@Audio 1 defines <character or sound type>'s <voice, dialogue, ambience, or music>.
```

任何可能泄漏不想要内容的素材，都在同一句里写明排除项：

```
@Image 2 defines the workbench and window light. Do not use the people in the image.
```

规则：

- **映射写在提示词里。**画在图里的文字标签不算映射，模型也不会推断一个素材代表哪个人或哪件道具。
- **只有视频的参考默认是动作/节奏参考**，不是身份参考；另有用意时明确说明。
- **同一主体的多张视图必须说明它们是同一个主体**：“All four images define one folding desk lamp. The output must contain only one lamp throughout.”不写的话模型会复制出多个主体。
- **参考视频已经准确承载了动作时，在职责映射里写明要继承哪些属性。**提交稿里避免相冲突的重新编排；母稿里保留继承来的因果动作、反应和接点状态。白模或动作视频承载的是动作和空间结构，不是身份，所以提示词仍要定义主体、场景、动作和视觉风格。
- **主体不在的镜头里绝不放它的参考调用名**：与 2.0 的标签纪律相同，模型会把它硬塞进画面。
- **角色设定板会泄漏它的布景。**设定板的中性背景和多视图排版是最常见的角色素材泄漏：灰色摄影棚会被渲染成真实场景。每个角色设定板职责都配上自己的排除项：*“Do not take the gray backdrop, the panel borders, or the multi-view layout.”*
- **节拍文字写角色名，不写调用名。**在动作/节拍文字里，角色第一次出现时写名字加一个可见标记：*“Mira — silver streak, rust-red jacket — crosses the stall line”*，而不是 `@Image 2`。模型按它在素材里看到的东西绑定；把调用名当句子主语，正是一个角色回来变成两个人的典型原因。`[OFFICIAL — SD25-PE mapping priority: material content outranks upload order]`

### 保真度：说清每个素材要保留多少（Fidelity — say how much of each material must survive）

`[EMPIRICAL — third-party skill corpus, re-derived; cross-model structure, unmeasured on Seedance]` 职责说明素材做什么工作，但仍没说明素材有多少要进入画面。每个素材在职责的同一句里声明一个保真等级：

- **完整保留（full-preserve）**：主体原样出现：脸、体型、服装，全部。
- **部分保留（partial-preserve）**：点名的部分保留，其余自由：*“the jacket and the scar; hairstyle may change.”*
- **属性迁移（attribute-transfer）**：点名的特征迁移到一个**不同的、点名的目标**上：*“apply this fabric's weave and sheen to Mira's coat.”*必须点名目标：这是单纯一句职责表达不了的唯一情况，也是会悄悄出错的那一种。
- **松散参考（loose-guide）**：只取氛围、配色或能量，不照搬任何东西。

```
@Image 4 defines the brocade fabric — attribute-transfer onto Mira's coat only.
Do not carry the garment's cut, the mannequin, or the studio backdrop.
```

### 素材预算（Material budget）

`[OFFICIAL — Dreamina]` 硬上限与真正稳定的范围：

| 类型 | 硬上限 | 稳定范围 |
|---|---|---|
| 图像 | 30 张，每张 ≤4K | 1–8 个不同主体 |
| 视频 | 10 段，合计 ≤30 秒 | 1–5 个主体，每段 5–10 秒 |
| 音频 | 10 段，合计 ≤30 秒 | 只放直接相关的片段 |
| 视频编辑源 | 1 段视频 + 参考图 | 源 ≤20 秒，1–5 张参考图 |

参考素材总共 50 个。在 Higgsfield 上，平台只执行其中**两条**上限，并把 `start_image` / `end_image` 计入两条：图像参考 + 首帧 + 尾帧 ≤ 30，全部素材 + 首帧 + 尾帧 ≤ 50 `[OFFICIAL — platform, CLI rules 2026-09-26]`。10 段视频、10 段音频和合计 ≤30 秒是 Dreamina 的数字，没有平台规则写明它们：把它们当作厂商的模型限制，在 Higgsfield 上未经核实。超出稳定范围（图像 9–12 个主体、音频/视频 6–10 个、编辑参考图 6–8 张）仍能生成，但稳定性下降，镜头可能要试几次：为此留预算，或者把场景拆开。

**超过五个主体、每个都需要多视图 → 每张图一个视图。**独立的视图图像胜过一张多视图拼贴；拼贴是更不稳定的形式。

**把一个视图花在强烈表情上，而不是四张静止的脸。**`[OFFICIAL — Higgsfield Seedance 2.5 deck, PART 2]` 一组中性视图只教会模型脸静止时的样子，所以第一句台词就会凭空编出一张嘴。在中性浅灰底上生成视图，并让**其中一张是强烈表情**（愤怒或大笑），让模型学到角色的**面部动态和牙齿结构**，而不只是静止的脸。标准四张：正面 · 背面 · 中性面部细节 · 强烈情绪下的面部动态与牙齿。最后用身份句（§ Reference Roles）收尾，让四张被读成同一个人。本工作室的角色参考板版式以 [角色资产交付规范](template-character-asset-delivery.md) 为准。

---

## 多参考：五步流程（Multi-Reference — the Five-Step Workflow）

`[OFFICIAL — Dreamina]` 目标**不是**把所有参考塞进一句话，而是定义角色、道具、场景、动作和音频之间的关系，让模型在对的时刻选对素材。

**第 1 步：逐个命名并映射每个主体。**每个主体一行：

```
<Character A> corresponds to @Image 1. Use only the appearance, hairstyle, and clothing.
<Character B> corresponds to @Image 2. Use only the appearance, hairstyle, and clothing.
<Prop A> corresponds to @Image 3. Use only the structure, material, and color.
<Scene A> references @Image 4. Use only the spatial layout, architecture, and lighting.
Do not use the people in the image.
```

> **标准反例：**`@Images 1 through 4 define four characters respectively.`这句话没说哪张图是哪个角色，模型只能猜。

**第 2 步：主体多了以后按类型分组**：`[Characters]` → `[Props]` → `[Scenes]` → `[Motion and Audio]`（工作室格式：`[角色]` → `[道具]` → `[场景]` → `[动作与声音参考]`）。在角色组加上不可互换锁定：“Do not interchange these characters' appearances, clothing, actions, positions, or dialogue.”

**第 3 步：给反复出现的主体建档案。**跨多个场景、或带多个素材的角色，合并成一个块：

```
[Subject Profile: Conservator]
Appearance and clothing: @Image 1.
Fixed prop: <Sample Case> from @Image 5.
Locations: <Conservation Lab> and <Gallery>.
Motion references: the case-opening motion from @Video 1.
Do not use: other characters' clothing. Do not give this character other equipment.
```

**第 4 步：按场景选用参考。**每个场景只列实际用到的子集，然后写事件和结束状态：

```
Scene 1 | Inspection in the Conservation Lab
Use: <Conservator>, <Sample Case>, <Conservation Lab>, and the case-opening motion from @Video 1.
Event: <Conservator> opens <Sample Case> at the workbench and inspects the sample inside.
End state: <Conservator> remains on the inner side of the workbench. <Sample Case> stays
beside the conservator's right hand.
```

**第 5 步：检查归属。**每个道具只属于一个角色（“belongs only to <Conservator>”）；角色数量、服装和空间方向跨场景保持不变。

---

## 长视频：阶段与结束状态（Long Video — Stages and End States）

`[OFFICIAL — Dreamina]` 2.5 原生生成最长 30 秒。任何包含多个事件的内容都要**分阶段**：一整段平铺的文字正是节拍丢失的来源。

每个阶段承载**一个主要状态变化**、它的可见反应，以及一个**明确、直接可见的结束状态**。辅助反应和微动作服务于这个变化。每个新阶段重述要继承的内容。先推出必要的阶段，再估计它们的时长；30 秒和这个例子都不意味着三个阶段或三等分。下面的骨架只示意一种可能的推进；按需增删阶段。它是规划/编译骨架，不是完整交付物：把每个事件展开成共享的阶段文字，写清动作、响应、接续、运镜、声音和交接。

```
[Generation Goal]
Generate a <video type>. The central subject is <subject>, and the primary event is <story summary>.

[Stage 1]
Initial state: <initial state of characters, props, and scene>.
Primary event: <one primary action or event>.
End state: <character positions, prop ownership, or visible scene state>.

[Stage 2]
Continue from the previous stage: <state that must remain unchanged>.
Primary event: <one primary action or event>.
End state: <observable state>.

[Stage 3]
Primary event: <closing event>.
End state: <final visible state>.

[Maintain Consistency]
Keep <character identity, number of characters, clothing, prop ownership, spatial direction,
and audio relationships> consistent.
```

### 按任务拆，而不只按长度拆（Split by JOB, not only by length）

分阶段解决的是*一段里事件太多*。它解决不了**一次生成里两个不相容的任务**，这时可以单独生成一次、在剪辑里切开 [DEMO — Higgsfield "AI Love Stories" tutorial, 2026-08]。

报告的案例：一场竞技场戏，同一个节拍里既有打斗（巨力投掷、夺剑、放倒），又有围绕打斗的表演（藏起来的担忧、调情式的退场、希望从脸上褪去）。作为一条提示词跑，它“撑住了”，但两头都变差：*“打斗变软了，脸变平了。”*模型的注意力预算只能花一次。要它在一次生成里同时把物理和微表演做到位，它两样都只做一半。

那个案例里，拆成**两条提示词，各做一件事，在剪辑里拼接**。这是一个实际的补救，不是通用的“两条提示词”构图规则：

| 在这里切 | 因为 |
|---|---|
| **物理 ↔ 表演** | 质量、接触和惯性跟随，对比眼神、呼吸和微表情。注意力不同、光学不同，通常景别也不同 |
| **动作 ↔ 对白** | 同一种拆分换了个样子 |
| **需要空间的节拍** | 报告的第二个案例：一场 30 秒的嘉年华戏作为一条提示词*撑住了*，仍被拆成 3×15 秒，因为第一次触碰的节拍需要空间：*“这些节拍感觉完全被赶着走”*。限制不是长度，而是**节奏** |

**怎么判断需要哪种拆分。**按时长拆，依据事件、反应、对白和转场所需的时间，并对照模型上限检查。按复杂度拆，问的是这次生成能否把它的几件任务一起清楚地呈现。两件任务不自动等于两个镜头：兼容的动作和反应可以留在一个镜头里。在因果/状态交接或镜头覆盖改变能保护表演的地方拆，并记录继承的接点状态。

注意第二个案例的方向：它装得下，仍然拆了。“生成出来了”不是标准：一场戏渲染出了每个节拍，却把最重要的那个赶着走过去，在你做它的目的上就已经失败了。

同一个制作还报告说没能拿到一条完美的 30 秒渲染；这是制作观察，不是模型禁令。按兼容的任务分别生成素材，内容需要拆分时再组装。那部片的几场成片，背景来自一条，前景动作来自另一条。

### 时间码与节奏（Timestamps and pacing）

默认用阶段。在事件/状态规划之后再分配各阶段时长，依据表演和阅读时间，而不是平均分配。完整演出的阶段用时间/事件区间；某个交接、进出画、转场或节拍需要提示点时，再加精确目标，但不声称帧级精度。编辑时保留源时间码，不另建阶段时钟；附加的音频保留自己的时间。切镜与阶段分开写。

| 写法 | 用途 | 例子 |
|---|---|---|
| 时间区间 | 给一个片段分配节奏 | `0-3 seconds… 3-7 seconds… 7-12 seconds…` |
| 精确时间点 | 一个关键事件 | `At 5 seconds, the camera whip-pans rapidly to the left and completes the transition.` |
| 相对时间 | 两个事件之间的延迟 | `Three seconds after the character presses the button, the room lights gradually turn off.` |

- 区间**连续且不重叠**，它们是**时间预算**，不是逐帧精确的剪辑点：动作可能落在边界前后一点。
- 区间里内容太少，会把你不想给的自由交给模型；太多则会导致过度切镜或丢事件。
- **不要从时间码推出每秒动作配额。**把用户要求的节奏和因果编排当作时间目标，评估可读性和实际模式限制，再核对渲染或后期的时间；文字不保证精确节奏。
- 每个带时间码的片段仍然以明确的结束状态收尾，和阶段完全一样。

> **与 2.0 节拍算术的关系。**`higgsfield-seedance.md` § Output Format 要求计时节拍之和等于声明时长。这一条仍然成立，但这里的总和是 4–30 秒；并且记住在 2.5 上，这个总和是模型会近似遵守的预算，不是它逐帧执行的切点表。

---

## 音频与文字：括号语法（Audio and Text — Bracket Syntax）

`[OFFICIAL — Dreamina]` 提示词可以完全用自然语言写。需要明确区分音乐、音效、对白和字幕时用括号：

| 内容 | 语法 | 例子 |
|---|---|---|
| 音乐 | `()` | `(Soft, rhythmic piano music plays in the background)` |
| 音效 | `<>` | `<A bell rings in the distance>` |
| 对白 | `{}` | `{Hello, welcome back.}` |
| 字幕 | `【】` | `【Chapter One: Departure】` |

**对白语言强化。**非中文对白（或英文台词被念成了中文，或想要特定地区口音）时，在台词前写明：

```
Dialogue language + regional variety or accent + delivery style + speaker + {dialogue}
```

```
Dialogue language: authentic Los Angeles English. The man says in natural Los Angeles
vernacular: {No way, you actually made it.}
```

工作室格式：`[声音]` 首行写 `对白语言：英语。`，随后每句一行 `起s-止s｜说话人＋状态＋说：{English line}`；有人物时第一行是定位秒的 `0s-1s｜<名字>轻声：{Hm.}`。

从 `higgsfield-audio.md` 和 `higgsfield-seedance-hell-grind.md` 的电影流程沿用两条内部规则：

- **台词只写在音频部分**：动作描述里一个字的台词都不写，否则模型会把它当成行为演出来。陷阱在于写作者不把*潜台词*当成台词：`they exchange a look that says "you too?"` 是剧本从没写过的一句话，结果它会被念出来。`[HOUSE — the failing take is timecoded in the nutllwhy/seedance-tvc-director evaluation, MIT, 2026-08-09.]` 任何可读的文字都是配音请求：引号里的潜台词、回忆中的台词、口号、念出来的招牌。改写成可见行为（*下颌绷紧，目光停住*）；还要注意加上“no dialogue”并不能抵消：那段可读的文字仍然在那里被请求。
- **只用画内声音是项目选择，而 2.5 终于听话了。**随机字幕和没要求的 BGM 是 2.0 被抱怨最多的问题；字节跳动把同时压制两者列为 2.5 的主要修复 `[OFFICIAL — Dreamina]`。仍然要写明（并且不写 `【】` 块），而不是信任这项改进。压制写成 **`NO BGM`**，不写 `(no music)`：制作术语读起来是硬规格，裸否定读起来是偏好；并在它前面先列出正向的画内声音（`higgsfield-audio.md` § Suppressing music）。

---

## 参考图、视频与音频的职责（Reference image, video and audio roles）

当前视频生成用 `omni_reference`。只映射提供了且真实绑定的素材。职责句写明要用的具体属性、保真程度和排除项；没有图像充当必须的开场或结尾帧。

```text
@Image 1 defines <Character A>'s identity and outfit only. Ignore its background,
pose and panel layout.
@Image 2 defines <Prop A>'s structure and material only; it belongs to <Character A>.
@Image 3 defines the scene layout and lighting only; ignore incidental people.
@Video 1 supplies the timing and body trajectory of <action> only; do not copy
its performer, costume or location.
@Audio 1 supplies <voice, spoken words, music rhythm or ambience> only; do not
introduce unrelated voices or sounds.
Open with <story-driven action and staging>, then <causal event and response>.
Finish with <visible character, prop and scene state plus sound and handoff>.
```

把示例槽位替换成实际的附件绑定。引用的文件或当前槽位缺失时，在规划清单里保留它的逻辑名，用文字描述主体；不虚构 `@Image`/`@Video`/`@Audio` 绑定。单张图用同样的规则；不需要特殊的图像模式或额外的开场构图。结局是叙事上的输出状态，不是第二张参考图。

---

## 编辑、延伸与组合模式（Editing, Extension, and the Composite Modes）

长模板在同目录的 **`higgsfield-seedance-2-5-mode-playbooks.md`** 里。打开之前需要知道：

- **视频编辑**：把源视频定为**唯一编辑母片**，然后写编辑目标、编辑范围、目标素材和保留清单，包括原有事件的时间码、时长、切点和音频时间（明确编辑的除外）。替换主体还需要一条**时间线继承**条款，让新对象继承旧对象精确的时机、路径、遮挡和离场。替换背景时把编辑范围限定在*主体轮廓之外*。音频类别（对白、语言、音色、BGM、音效）各自独立编辑。
- **视频延伸**：决定成败的唯一规则：**在描述新内容之前先对齐边界帧。**向前延伸从源视频的最后一帧继续；向后延伸必须接上源视频开场的动作、空间和声音状态。在任一接点继承姿势、道具归属、动作相位/方向/速度、构图、光照和音频相位；新阶段不能重演或重新定时源内容。“Then connect to the source video”是文档记录的失败写法：它会把后面的元素提前漏进来，并让画面在到达之后漂移。
- **一键成片**（多张图 → 一条剪好的视频）：`素材职责 → 图片顺序 → 运动量 → 剪辑风格 → 视觉处理 → 音频`。“把这些做成视频”永远不够。
- **无缝转场**（在两个片段之间补桥接内容）：`前一段视频 → 后一段视频 → 触发动作 → 摄影机运动 → 视觉变换 → 到达状态 → 音频`。
- **转场词汇**：自然切换 · 淡入淡出 · 叠化 · 白/黑闪 · 擦除 · 遮罩 · 相似物转场 · 动作转场 · 动态接力 · 推近/拉远 · 水墨。每种都写明自己的触发和到达构图。

---

## 情绪引导与运镜术语（Emotional Direction and Camera Terms）

`[OFFICIAL — Dreamina]`

**情绪。**抽象词（“紧张”“温暖”“压抑”）只定了方向，其余留给解读。给它们配上直接可见或可听的线索：眼动、眉间紧张、嘴部动作、呼吸、视线方向、手部动作。**两到四个线索是可选的示例，不是配额**；选当前景别下看得见、由事件触发的有意义的线索。保留完整的动作/反应弧线，不罗列所有面部细节，也不强行用近景。

```
The overall emotion shifts from <starting emotion> to <ending emotion>.
After <triggering event>, <subject> first shows <immediate observable reaction>.
Then, <eyes, brows, mouth, breathing, gaze, or hand movement> gradually <changes>.
Finally, <subject> expresses <target emotion> through <restrained or explicit outward behavior>.
```

只有情绪真的变化好几次时，才用事件触发的多阶段写法。需要更细的肌肉级控制，见 `higgsfield-facs.md`（AU 代码）；让这些线索*有意义*的“压力下的行为”这一层，见 `higgsfield-acting.md`。

**运镜术语。**基础语言直接可用：景别（大远景 / 远景 / 中景 / 近景 / 大特写）、运动（推近、拉远、摇、横移、跟随、环绕、俯冲、后退、上摇、手持晃动）、机位（低角度、俯拍、第一人称）。

流行技法（一镜到底、滑动变焦、航拍、FPV、子弹时间、手持、弹跳变速）也直接可用；但画面里有几个主体时，仍要说清摄影机跟随或环绕**哪一个**主体、从哪里开始、在哪里结束。

**小众或有歧义的术语**，保留术语，再翻译成可观察的结果：

```
Cinematography term + target subject + visual change + foreground/background relationship + direction or speed
```

```
Rack focus: shift focus smoothly from the leaves in the foreground to the person in the
background. The leaves gradually blur while the person's face changes from soft to sharp.
```

需要精确的转场时刻时，加上触发时间、遮挡物、方向和之后继续的内容。光圈/焦距/快门数值可以写，但预期的可见结果比单纯一个数值更清楚。

> **视场角度数仍然胜过毫米数。**`higgsfield-seedance.md` § FOV anchors 里的离散视场角锚点是整个 Seedance 系列的内部规则，在这里照常适用。

---

## 真人角色公式（The Real-Person Character Formula）

`[OFFICIAL — Dreamina]` 厂商对“我的角色看起来像 AI，或者像双胞胎”的回答是一个七槽位角色块。风格化角色也适用。

```
[Role]  [Skin color / skin texture]  [Facial details]  [Eyes / soul]
[Hairstyle / hair color]  [Clothing / clothing texture]  [Body type / mood / temperament]
[Other requirements, if any]
```

槽位说明：

- **皮肤**：带上真实质感：可见的微毛孔、通透感、毛细血管红晕。这是最能把“一个人的照片”和“AI 渲染”区分开的那个槽位。
- **面部细节**：眼型、眉线、鼻梁、嘴唇、下颌线。具体胜过漂亮。
- **眼神 / 灵魂**：目光在*做*什么、带着什么。死眼是头号破绽；见 `higgsfield-acting.md` § Eye life。
- **体型 / 情绪 / 气质**：身体就是履历，不是恭维。

> **对第 1 槽的内部覆盖。**原指南把第一个槽位标为 `[Age/Race]`。**不要写年龄。**`higgsfield-seedance-engine-rules.md` 的引擎规则 1 是“角色不看年龄”，Higgsfield 自己的长片说明给出了理由：内容过滤一读到未成年人就会急剧收紧。改写**角色身份、体格、服装和动作**：“a lean courier in a soaked parka”，而不是“a 22-year-old”。族裔仍是正常的描述槽位；年龄不是。

---

## 选 2.0 还是 2.5（Choosing 2.0 vs 2.5）

| 任务需要 | 模型 |
|---|---|
| 4K 输出 | **2.0**（`mode=std`），2.5 最高 1080p |
| 1080p 输出 | 都可以：2.5 自 2026-09-26 快照起支持（尚无实地评分），或 2.0 `mode=std` |
| 平台钉住的首/尾帧媒体职责 | 都可以：2.5 仅在 `omni_reference`；2.0 任何模式 |
| `mode=fast`（更便宜的 480p/720p） | **2.0** |
| `genre` 提示参数 | **2.0** |
| 单次生成超过 15 秒的片段 | **2.5**（最长 30 秒） |
| 编辑已有视频 | **2.5**（`video_edit`） |
| 向前*或向后*延伸片段 | **2.5**（`video_extension`） |
| 超过 9 张参考图，或超过 3 段参考视频/音频 | **2.5**（30 / 10 / 10，2.0 是 9 / 3 / 3） |
| 便宜的 480p 提示词验证 | 都可以：两者草稿通道都是 480p |

**实在的默认：**任务长、参考多或属于编辑类时，用 2.5（现在最高 1080p）；只有 4K、`mode=fast` 或 genre 提示才换到 2.0。2.5 1080p 和 2.0 1080p 哪个细节保持得更好，没有测量过。它们不能互换：2.5 草稿验证的是*提示词*，不是 2.0 的渲染，原因与 `higgsfield-seedance.md` § Drafts Validate the Prompt 给出的相同：没有 seed 可以钉住。

### 从 2.0 原样沿用的内容（What carries over from 2.0 unchanged）

把 `higgsfield-seedance-engine-rules.md` 当作旧版提示与补救指南使用，服从 [共享叙事规划](narrative-planning.md) 和 2.5 的实际模式限制。它关于出画/重新入画、画外、倒影、追踪人数和双重对比的建议，不会变成 2.5 的通用禁令或强制切镜。保留明确的身份、因果动作和画外状态交接。可观察的微表情线索、正向表述、同形词检查和制作块结构仍然有用；它们都不能替代共享的完整演出格式，也不保证渲染效果。

---

## 硬限制：不要过度承诺（Hard Limits — Do Not Over-Promise These）

`[OFFICIAL — Dreamina]`

- **时间码分配时间，不是逐帧精确的剪辑点。**绝不暗示某个节拍会落在某一确切帧上。
- **视频编辑提示词提高**关键事件与源视频对齐的概率，但不能保证逐帧重合。
- **多参考按场景选择并组合**合适的素材；它不会让所有素材同时出现。
- **不承诺帧级文字准确。**字幕、公式、招牌和产品规格需要准备好的参考素材加后期，与 2.0 文字渲染高风险项的结论相同。
- **视频编辑锁定输入的画幅和大致时长**；由于转场帧处理，输出可能相差约 0.3 秒。
- **首尾帧生成把画幅锁定为第一张图**；画幅不一致会拉伸最后一帧。
- **视频延伸把画幅锁定为源视频**；延伸部分的音量可能略有不同。
- **边界帧是自然衔接，不是完全相同**：检查接缝两侧和整个延伸段。
- **无缝转场追求视觉和听觉的连续**，不是像素级保留任一源片段。

---

## 仅 Dreamina 有、Higgsfield 没有开放的功能（Dreamina-Only — What Higgsfield Does Not Expose）

`[DREAMINA-ONLY]` 这些功能存在于字节跳动自己的 Dreamina/即梦产品里，指南中也提到了，但在 2026-09-26 快照上**背后没有 Higgsfield 参数**。不要在这里提供。

| Dreamina 功能 | 在 Higgsfield 上的状态 | 最接近的可用做法 |
|---|---|---|
| **Ultra Long Video**：单次生成 30–180 秒 | 未开放；`duration` 上限 30 | 分阶段生成 30 秒，再串接 `video_extension` |
| 通过反复界面操作**嵌套延伸到 60 秒** | *模型*规则（源 ≤30 秒 → 最多延伸 30 秒）成立；一键嵌套的界面不存在 | 串接 `video_extension` 调用，每次重新检查边界 |
| **标注编辑 / 高级编辑**：在画面上用框、箭头、画笔、锚点标注 | 未开放；没有标注通道 | `video_edit` 加文字范围：对象 + 改动 + 生效时间区间 |
| **Clay Renderer 插件**：白模渲染流程 | 未作为插件开放 | 通过 `omni_reference` 的粗/细白模提示（`higgsfield-seedance-2-5-mode-playbooks.md` § Blockout references） |
| 原生 180 秒 / 数分钟的成片 | — | 按事件和接点状态拆成若干段，每段在 4–30 秒生成范围内，后期组装 |

**延伸链算术。**模型端规则：**30 秒以内**的源视频一次可以延伸 4–30 秒，所以 30 秒源加 30 秒延伸就是单条链的 60 秒上限。再往后，从原始参考重新锚定，而不是延伸一段延伸出来的视频：与 2.0 链上限的退化曲线相同，见 `higgsfield-seedance.md` § Extension Prompting。

---

## 提交前检查（Pre-Submission Checklist）

`[OFFICIAL — Dreamina]`，加上内部预检。只看实际用到的技法对应的行：

- [ ] 直白写出主体和主要动作或事件
- [ ] 每个参考都写明用什么**和**不用什么
- [ ] 每个角色、产品和道具都有名字，并绑定到具体素材
- [ ] 参考**按场景**选用，不要求同时全部出现
- [ ] 阶段跟随事件/因果/揭晓/状态转变；时长按表演需要，不预设数量、不平均分配
- [ ] 阶段、切镜和生成边界各自有理由；结尾画面和转场都装得进总长
- [ ] 每个阶段有一个主要变化、可见反应、继承状态和清楚的结束状态
- [ ] 角色数量、服装、道具归属和空间关系全程一致
- [ ] 编辑提示词写明唯一母片、编辑范围、目标数量和保留清单
- [ ] 抽象情绪和小众运镜术语都配了可观察线索
- [ ] 首尾帧：每张图一个职责，画幅一致，锚点不合并
- [ ] 分镜：写明继承哪个结构，而不是照搬画格
- [ ] 白模：先判断粗还是细，写明继承清单
- [ ] 编辑 / 首尾帧 / 延伸的自动锁定参数得到尊重
- [ ] 延伸：边界帧、运动趋势和音频连续都已检查
- [ ] 一键成片：职责、顺序、运动量、剪辑风格、音频都已定义
- [ ] 转场：两段的职责、触发、过程和到达状态都已定义
- [ ] 调用名只出现在参考块里；节拍文字用角色名（名字加一个可见标记）`[EMPIRICAL — sd25-pe]`
- [ ] 角色设定板的职责排除背景、画格排版、去头取景和图底文字条
- [ ] 上下文隔离：复制的提示词里没有镜头编号、场次/批次号、“同上 / 上一镜”或编辑说明（省略、理由）`[OFFICIAL — Higgsfield prompt-writter.skill]`
- [ ] 每个带时间码的片段以可见的结束状态收尾，而不是理由
- [ ] 指定了切镜时写明切镜锁定：`cuts only at the specified points, the camera does not cut on its own`（工作室格式：只在指定处切镜，镜头不会自行切换）
- [ ] 一次生成一件任务：物理与表演、动作与对白相互挤压时拆开（§ Split by JOB）
- [ ] 工作室块结构稿不设字数上限；每件重要的事只说一次
- [ ] 全文不写年龄词（引擎规则 1）
- [ ] `seedance_lint.py --preflight --model seedance_2_5` 已运行且无问题

---

## 相关模块（Related Skills）

- `higgsfield-seedance.md`：Seedance 2.0 导演：过滤模型、块结构、视场角锚点、提示词写作规律、引擎规则。**所有与模型无关的内容都在那里。**
- `higgsfield-seedance-engine-rules.md`：共享的硬性渲染约束
- `higgsfield-seedance-hell-grind.md`：Higgsfield 开源的长片制作流程（资产、GEO 空间布局、对白构建、迭代纪律）
- `higgsfield-acting.md`：表演：目标、障碍、策略、节拍、眼神生命力
- `higgsfield-facs.md`：用动作单元代码控制面部
- `higgsfield-seedance-vfx.md`：2.0 上的视频到视频素材变换
- `higgsfield-models.md`：对照规格层选模型
- `higgsfield-seedance-2-5-mode-playbooks.md`：编辑 / 延伸 / 一键 / 转场 / 白模模板
- `higgsfield-seedance-2-5-vfx-pipeline.md`：AI 视效制作流程：按资产类型选模型、尺寸参照帧、场景批处理、`omni_reference` 视频到视频通道、四批规则、劣质效果清单

## 整合版：人物身份与表情参考的职责

角色参考板按 [角色资产交付规范](template-character-asset-delivery.md) 制作。视频里面部格负责身份，全身格负责比例、体型、服装和穿戴配饰，均属于同一角色；已登记的完整音色描述可写入 `[角色]`。参考板的排版、背景、图底条和去头取景不进入成片，视频人物五官自然完整。

提示词必须说明各素材属于谁、负责什么、排除什么；灰底、多视图排版和身体图裁切不进入成片。中性资产用于固定形体与材质，视频场景自行定义光照；写实质感从通过视觉验收的主参考延续，不靠视频提示词反复描述五官来重造身份。继续执行原阶段状态、参考映射、模式参数及 preflight；静态 lint 通过不能证明面部一致性或视觉真实感。

## 项目约定：跨类型导演骨架（Project convention — cross-genre director scaffold）

本项目写 Seedance 2.5 提示词时，在每种模式里应用 [共享叙事规划](narrative-planning.md)，然后读 [跨类型导演模板](template-general-director-2-5.md) 和完整的 [完整演出范本](template-full-performance-example.md)。默认交付完整、可复制的演出说明：资产职责、整体目标、全局视听与空间规则、行为与节奏、详细的分阶段演出、状态继承、结尾画面和有范围的约束。每个阶段里用具体文字展开动作、可见响应和主体接续；写清视觉层次、运镜路径、声音、结果状态和到下一阶段的交接。单镜头工作沿用同样的可见标题，保留完整的演出细节。只有明确的精简请求、局部编辑或目标格式的硬限制才需要更短的交付或提交稿；完整任务保留完整母稿。时长、阶段数、速度、运镜、特效和题材都按任务而定。这个完整演出的默认优先于短格式的风格建议，同时保留所有原生格式和能力。

只绑定实际上传的参考；动作文字里用稳定的主体名。这些规则在工作室块结构里的落点（`@` 只出现在 `[角色]`/`[道具]`/`[场景]`/`[动作与声音参考]`，每份素材有使用/排除说明；不写镜头编号或编辑说明；结束状态；切镜锁定；对白写在 `[声音]`；不设字数上限）归 [narrative-planning § 模型可读性](template-general-director-2-5.md#模型可读性higgsfield--dreamina-seedance-25-标准) 所有，由 `director_contract_lint.py` 检查。累积的结果一直保留到有明确的叙事改变为止，包括交接、清理、换场和必要的复原。区分场内符号与用户要求的品牌/字幕和不想要的叠加。平台设置与文字分开，核实实际托管平台，把节拍时间码当作时间目标，而不是帧级保证。编辑和延伸保留 MODE-PLAYBOOKS.md 里各自模式的母片/范围和边界约定。这是由用户确立的编排约定，不是新的模型能力声明，也不是测得的生成结果。

项目时长偏好：继承明确的全片和段落预算；否则按表演工作量估计自然时长。镜头没有默认长度；生成片段通过合并兼容的完整事件接近所选模型的单次上限，绝不靠注水，也不把一个事件切在边界上（narrative-planning § Clip 边界隔离）。按 narrative-planning.md 的内容驱动分段：选择观看目的和有动机的切点，估计保留的镜头时长，然后合并或拆分合法的生成，同时保留动作相位和连续性。生成时长与保留的剪辑时长分开；绝不为凑满模型上限而注水。编辑保留源时间线；延伸只为新素材做预算。实际平台/模式限制独立存在，需要核实。
