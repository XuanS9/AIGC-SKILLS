# Higgsfield 平台指南（Higgsfield AI Prompt Skill）

**当前工作室视频路线：**默认 Seedance 2.5 `omni_reference`。把角色/道具/场景图和参考视频/音频映射到各自的具体属性，并对应真实绑定的槽位；单张图不会变成开场画面。下面快速路径里的模型/模式默认和旧的图生视频示例，不覆盖这条项目规则。执行时对照带日期的 schema 核对平台参数。

**语言规则：**用户用什么语言写，就用什么语言回复。

**按场景分阶段交付：**资产是否建立先按[独立视频提示词门槛](asset-registry.md#资产建立门槛按独立视频提示词计数)，单次对象不默认建资产，无新增资产的阶段跳过；其余遵守 [样本确认流程](sample-approval.md)：统一规划，共享资产先定稿，然后每个场景走「补充基础资产 → 场景 → 视频」。展开一个阶段之前，先确认这个阶段的样本；已确认未变的内容复用。资产/视频联合样本只用于明确要求的快速预览。一个阶段确认了，不代表授权了下游所有阶段。已有的、明确的局部修订授权不需要再次审批。文字、素材可用、绑定和视觉验收是分开的状态。

**工作室规划与加载：**用 [最小加载与规则归属](load-map.md)，不整包加载。视频任务选读相关的 [共享规划](narrative-planning.md) 章节、[导演模板](template-general-director-2-5.md)，首次完整创作/完整改写时读 [完整演出范本](template-full-performance-example.md)。输出是块结构：Higgsfield 块结构（[参考资产]→[角色]…[生成目标]→[具体情节]→[视觉风格]→[镜头]→[声音]→[保持一致]）；规划类别只在内部使用，绝不是第二种交付格式。短格式/原生提交保留它们实际的约定。图像、音频、工具和费用任务只加载各自适用的模块。

---

## 硬规则：交付前检查清单（HARD RULES — pre-delivery checklist）

这些规则适用于每一次 Higgsfield 相关的回复。它们写成助手在发送回复*之前*跑的交付前检查清单，而不是说完就忘的禁令。它们防止的失败模式是**“看起来像就当是”**：产出一个看起来正确的回复，是因为训练数据知道 Higgsfield 工作的大致样子，而不是因为真的读了技能文件、核实了平台的实际情况。

**交付任何 Higgsfield 相关回复之前，按顺序确认：**

1. **有路由说明。**回复的第一行写出你路由到了哪些子模块（例如“路由到 higgsfield-prompt + higgsfield-camera，做一个氛围类推近”）。一行，然后开始工作。缺少路由说明 = 回复不完整；补上。

2. **本轮对话里读过路由到的章节。**用 [最小加载与规则归属](load-map.md)。打开并完整读取选中的适用章节；grep 片段不能替代。截断的章节用 offset/limit 读完。平台相关的提示词工作读本指南和适用的提示词工程章节；限定范围的修订复用未受影响的带版本证据，而不是重读全部模块。记录实际读了什么，而不是笼统声称全读过。

3. **具名词汇经过核实，而不是编造。**运镜预设名、运动预设名、模型名、CLI 参数写法和 MCP 工具参数名，全部来自技能文件或核实。模型参数、枚举和时长，先对照 `model-specs.json` 核实：它由一份带日期的 `models_explore` 快照生成（见文件里的 `snapshot_date`）；快照过期（>30 天）时改为在线核实（CLI 参数 schema 用 `higgsfield model get <model>`；MCP 用 `models_explore`）。如果你发现自己在想“这个参数大概是 X”或“这个预设大概叫 Y”，停下。读文件或跑核实命令。看起来像不等于有效。不要用泛泛的视频提示词词汇代替 Higgsfield 的具名预设；不要编造模型版本、运镜预设或运动预设名。用户点名一个你在技能文件里看不到的，照实说并请他澄清。

4. **视频提示词的 MCSLA 覆盖完整。**模型 · 运镜 · 主体 · 画面 · 动作仍是五项检查。在本项目的块结构演出格式里，模型/设置放在可复制提示词之外，其他层落在各自分配的块里；不要另附一个重复的 MCSLA 块。

5. **检查并挑选了共享约束。**按这个镜头的实际风险查 `negative-constraints.md`。使用适用的正向预防措辞，遵守模型/模式范围。不要整表附上，也不要重复已经确立的锁定；最终的约束只包含剩下的、本任务特有的风险。

6. **适用时提示预检。**如果出现执行意图（提到 CLI / MCP / 内置技能），**并且**点名了视频类或高成本模型，**或者**提到了预算问题，就提示两步预检（先用 `model get` / `models_explore` 查 schema，再估算费用）。生成之前用已安装的工具核对费用和余额。

7. **画幅是枚举值，不是自由值。**写进头部之前，对照 `model-specs.json` 核对模型允许的画幅；快照过期（>30 天）时通过 schema 在线核实（`models_explore` / `model get`）。为什么重要的例子：Seedance 2.0 支持原生 21:9；Seedance 1.5 Pro 的枚举与 2.5 不同。Anamorphic / 2.35:1 / 2.39:1 是画面那一行的*风格语域*词汇，不是输出画幅。见 `vocab.md` § Aspect Ratio: output spec vs. style register。

8. **提示词在 200 词以内：只限短格式。**这个 MCSLA 软上限只在要求短版本时适用，不适用于本项目完整的块结构演出稿，单镜头也一样。块结构制作稿保留它们的结构检查（`higgsfield-seedance.md` § Official Prompt Architecture）；更长的完整稿不违反第 8 条。工作室块结构稿不设字数上限。

**第 1–8 条任何一条缺失或未核实，回复就不完整。发送之前补完，而不是之后。**

---

## Higgsfield 是什么？（What Is Higgsfield?）

Higgsfield 是一个电影感的 AI 视频与图像生成平台。本工作室视频只用 **Seedance 系列**（默认 Seedance 2.5；明确选择时用 2.0 / 2.0 Mini / 1.5 Pro）。其他视频生成模型和后期视频工具（超分、对口型、去背景、去闪烁）已删除（removed）。图像模型保留：Soul 2.0、Soul Cinema Preview、Soul Cast、Nano Banana Pro/2、Kling Image 3.0/Omni、Seedream、GPT Image 2、Flux 2/Kontext。提示词写作之外的平台功能（运动预设、Soul ID、Cinema Studio、Apps、Canvas）本工作室不覆盖。

---

## 输入与输出文件（Input and output files）

在用户提供的路径读取用户素材。把交付物写到用户的项目目录，并报告生成的路径。生成的文件不放进已安装的 Skill 目录；不自动移动源素材。

### 快速路径：简单的创作请求（Fast Path — Simple Creative Requests）

意图清楚时可以不问多余的澄清问题就给样本；但不跳过当前阶段的样本规则和适用的文件读取。用根入口的默认：Seedance 2.5 `omni_reference`、16:9 和用户的语言；按表演估计时长，同时满足项目 30 秒上限和已核实的模型限制。继承项目的风格和图像工具；不要悄悄换成 Seedance 2.0、真人实拍或某个固定的图像模型。没有实际附件时，只描述已知的主体，不虚构参考槽位。

### 完整路径：制作请求（Full Path — Production Requests）

继承已确认的类型、模型、时长预算、画幅、风格和参考。只问执行所必需的缺失信息，最好只问一个窄问题。用户已经授权了范围时，不要再要求一次意图确认。当前阶段的新样本按 [样本确认流程](sample-approval.md) 确认；下游生成和付费执行需要各自的真实输入和授权。模型枚举/时长从实际所选模型的 schema 核实，绝不用示例的默认值。

---

### 路由到正确的模块（Route to the Right Skill）

| 用户想要 | 路由到 |
|------------|----------|
| 写或改进一条提示词 | `higgsfield-prompt` + 相关子模块 |
| 写提示词之前开发角色 / 世界 / 故事 / 前提，做角色表 / 故事圣经，锁定视觉风格（“视觉 DNA”），在很多镜头里保持角色一致，或“我总是得到泛泛的 AI 角色” | `higgsfield-character-design` |
| 生成之前审查或加强一场戏 / 一个段落 / 一份节拍大纲，或“这场戏成立吗”“哪里弱”“为什么不落地” | `higgsfield-scene-engine` |
| 电影感静帧提示词（构图、角度） | `higgsfield-image-shots` |
| GPT Image 2.0 / gpt-image-2 提示词、UI 原型、信息图、角色/参考表、版式密集的图 | `higgsfield-gpt-image-2` |
| 选对模型 | `higgsfield-models` |
| 运镜指导（视频） | `higgsfield-camera` |
| 视觉风格选择 | `higgsfield-style` |
| **一致性的分工：**用参考图在 Higgsfield 里保持角色一致 → 按 [角色资产交付规范](template-character-asset-delivery.md) 做参考图；先开发角色是谁（角色表、故事圣经、视觉 DNA）→ `higgsfield-character-design`。两者可以先后都用：先设计，再锁定参考图。 | — |
| 修复失败的生成 | `higgsfield-troubleshoot` |
| 音频设计、对白提示、音效、环境声 | `higgsfield-audio` |
| **独立音频生成**：配乐、环境声底、多人场景音频、Seed Audio 1.0（`seed_audio`）、作为单独交付物的 TTS 画外音/旁白 | `higgsfield-audio` |
| **延伸 / 续接已有片段**：“加长一点”“接下来/之前发生什么”、前传、尾帧交接、延伸链 | 默认 2.5 模式用 `higgsfield-seedance-2-5`；其他所选模型用它的延伸章节 |
| **视频之前准备资产 / 参考表**：角色表、道具三视图、场景底图、人群的多样性表 | `template-character-asset-delivery.md` + `higgsfield-gpt-image-2`（道具） |
| 在场景生成之前给设计好的角色试镜（看他怎么动、说话、反应） | `higgsfield-character-design`（§ Screen Test / Audition） |
| Seedance 2.0 / Pro 提示词、被标记的提示词、在 Seedance 上浪费额度 | `higgsfield-seedance` |
| **Seedance 2.5**：用户点名 2.5 / Dreamina / 即梦，想要单条超过 15 秒，想**编辑**或**延伸**一段已有视频，或提供很多图/视频/音频参考（最多 30/10/10） | `higgsfield-seedance-2-5` |
| **2.0 还是 2.5**（都叫“Seedance”）：需要 4K、`mode=fast` 或 `genre` 提示 → `higgsfield-seedance`；需要单次生成超过 15 秒、视频编辑、前后向延伸或大量多参考 → `higgsfield-seedance-2-5`。2.5 支持到 1080p | — |
| **角色表演**：表演、行为、习惯动作、小动作、步态、潜台词，“我的角色看起来很木 / 眼神空洞 / 像 AI”，让角色跨很多镜头保持自己，表演母本 | `higgsfield-acting` |
| **Seedance 上的长片制作流程**：角色表、场景表、跨镜头复用的场景地理块、对白构建、迭代纪律、巨物 / 人群 / 门槛转场 | `higgsfield-seedance`（`higgsfield-seedance-hell-grind.md`） |
| **变换用户已有的素材**（视频到视频）：“给这段视频/片段写 Seedance 提示词”，加一个特效元素（让我的头/头发着火、变换我的手、让一条肢体隐形），在保留主体周围换掉世界/背景（沙漠、云、岩浆、霓虹城），在我身后或地标上放一个巨型生物，重新打光/调色以匹配，让急推/推近与一句台词同步：起点是一段**真实的源片段** | `higgsfield-seedance-vfx` |
| **用生成代替视效/三维流程**：“AI 能不能代替视效做这个”、把我放进这个底片、把一个生物放进我的素材、不买也不绑定三维模型做龙/怪兽镜头、“怎么搭一整个视效镜头”、资产表 → 尺寸参照 → 场景 → 镜头作为一条流程；还有“我的视频到视频总失败 / 变成劣质”、两个主体之间的尺度漂移、脸 / 生物 / 服装 / 场景各用哪个图像模型 | `higgsfield-seedance-2-5`（`higgsfield-seedance-2-5-vfx-pipeline.md`） |
| 精确的面部表情 / FACS / 动作单元代码（AU12、AU6……）、勉强或诡异或混合的表情、近景微表演、独白/对白的面部表演、“愤怒/恐惧用哪个 AU”、FACS 参考表 | `higgsfield-facs` |
| “做一张分镜表”，把剧本/说明/大纲拆成很多条相连的 Seedance 提示词，导演分镜表，全局风格前缀 + `@` 资产表 + 带名字的逐场提示词，做成一个可编辑的 HTML | `higgsfield-shotlist-director` |

---

### 加载地图：要读多少（Load Map — how much to read）

详细的任务/范围决定在 [最小加载与规则归属](load-map.md)。这张平台表是可选的能力索引，不是额外的全读关卡。默认的 Seedance 工作加载适用的 2.5 模式；只有选 2.0/Pro 或做相应诊断时才加载 2.0/Pro。多场景工作不自动要求加载所有模块。模型选择只读所选输出模态的 schema，不读全部三份目录。

### 检查题材模板是否匹配（Check Templates for Genre Match）

从零写提示词之前，先看用户的请求是否符合一种常见题材。`template-*.md` 参考里有 9 个带逐行拆解、推荐模型、约束和变体的注释示例模板。

| 用户请求符合 | 查看模板 |
|---------------------|----------------|
| 追逐、追捕、动作、跑酷 | `template-01-cinematic-action-chase.md` |
| 恐怖、吓人、诡异、恐惧 | `template-03-horror-atmosphere.md` |
| 时尚、大片、lookbook | `template-04-fashion-editorial.md` |
| 科幻、赛博朋克、视效、太空 | `template-05-sci-fi-vfx.md` |
| 肖像、人物登场、近景 | `template-06-portrait-character-intro.md` |
| 风景、自然、建立镜头 | `template-07-landscape-establishing-shot.md` |
| 喜剧、社媒、抖音、小品 | `template-08-comedy-social-media.md` |
| 爱情、亲密、情侣、婚礼 | `template-09-romantic-intimate.md` |
| 舞蹈、音乐、表演、演唱会 | `template-10-dance-music-performance.md` |

把模板当作起点：按用户的具体请求改写示例提示词。注释解释每个元素**为什么**有效，帮你做出有依据的替换。工作室交付仍按块结构，模板只提供镜头写法参考。

**技法模板**（Seedance 的 `template-*.md` 参考）：用户请求是技法类而不是题材类时，Seedance 提示词的结构模板：

| 技法需要 | 模板 |
|---|---|
| 写提示词之前预先可视化多人空间几何 | `template-top-down-map.md` |
| 有跨角色关系的多人镜头 | `template-multi-character-anchor.md` |
| 锁定位置 + 姿势 + 接触点的单人镜头 | `template-single-character-position.md` |
| 完整示例：双人锚定从头到尾 | `template-worked-example-two-character.md` |
| 日式动画 / 风格化 2D 动画：分层公式 + 风格块 + 角色转面 | `template-anime-animation.md` |
| 用 FACS 动作单元代码做近景面部表演：按节拍同步的表情表 | `template-facs-expression-beats.md` |
| Seedance **2.5** 多参考说明：职责映射 + 带结束状态的分阶段节拍 | `template-omni-reference-2-5.md` |
| 动作戏：招式因果与破坏累积（当前格式，两条 Clip） | `template-action-example-xianxia.md` |

**文字叠加模板**（字幕和对话气泡模板）：可直接粘贴的字幕 / 对话气泡文字渲染提示；只在用户明确要求画面文字时使用：

| 文字叠加类型 | 模板 |
|---|---|
| 字幕（与对白同步） | `template-subtitle.md` |
| 对话气泡（归属于角色） | `template-speech-bubble.md` |

---

### 用 MCSLA 公式构建提示词（Build the Prompt Using the MCSLA Formula）

完整的 MCSLA 定义和提示词结构 → `higgsfield-prompt.md`

快速概括：五层，每条提示词都有：

| M | C | S | L | A |
|---|---|---|---|---|
| 模型 | 运镜 | 主体 | 画面 | 动作 |

**核心规则：**
- 要具体：写出运镜路径和终点（用预设时写准确名称），具体描述特效
- 提示词控制在 200 词以内（只限短格式；块结构制作提示词遵循自己的结构规则，HARD RULE 8）
- 短格式里，主体 → 动作 → 运镜 → 风格是最可靠的顺序

---

### 输出格式（Output Format）

完整视频按工作室块结构交付（见 [跨类型导演模板](template-general-director-2-5.md)）；平台设置写在代码块外。下面是用户明确要求短格式时的原生写法。

**单条提示词（短格式）：**
```
**Model**: [model name]
**Aspect ratio**: [ratio]  **Duration**: [Xs]  **Style**: [style]

[Prompt]

**Camera**: [camera control name]
```

**两个版本（风格不同时）：**
```
### Version 1 — [Style Name]
[Prompt]

---
### Version 2 — [Style Name]
[Prompt]
```

**输出规则：**
- 输出干净、可直接粘贴的提示词：后面不加元评论
- 除非用户要求，不解释每一行做什么
- 运镜写明路径和终点；用了预设就写出准确的预设名

---

## @ 参考规则（@ Reference Rules）

- 用户上传文档（剧本、圣经、说明、参考笔记）：在提供的路径读取；源文件留在原处。
- 用户上传图像：用 `[reference image]`，或描述为“提供的参考”；工作室格式在开头 `[参考资产]` 写 `@名字 对应 名字。`，只绑定真实槽位
- 视频延伸：写明“extend from [reference video], continue with...”
- 风格迁移：写明“match the visual style of [reference image]”

---

## 共享资源（Shared Resources）

| 资源 | 包含什么 | 何时用 |
|----------|-----------------|-------------|
| `negative-constraints.md` | 按类别的全部生成瑕疵 + 预防措辞 | 每条提示词之前查一下，挑选适用的约束 |
| `template-*.md` | 9 个带示例、模型、注释和变体的题材注释模板 | 用户请求符合常见题材时，作为起点 |
| 角色工作表模板 | 6 个角色设计工作表（九问角色表、故事圣经、视觉 DNA） | 写提示词之前开发角色时，配合 `higgsfield-character-design` |
| Seedance 的 `template-*.md` 参考 | Seedance 技法模板：俯视平面图、多人锚定、单人站位、双人示例、动画、FACS 表情节拍、素材视效变换、全局风格前缀、2.5 多参考、动作演出范本 | Seedance 请求是技法类时（空间站位、多人锚定、动画/风格化 2D、FACS 表演、素材视效、风格前缀、2.5 多参考、动作戏） |
| 字幕和对话气泡模板 | 2 个文字渲染模板：字幕、对话气泡 | 用户请求包含画面文字渲染时 |

---

## 子模块（按需自动加载）（Sub-Skills (auto-loaded as needed)）

| 模块 | 触发 |
|-------|---------|
| `higgsfield-prompt` | 任何写提示词或改进提示词的请求 |
| `higgsfield-image-shots` | 电影感图像提示词：构图、角度、取景 |
| `higgsfield-gpt-image-2` | GPT Image 2.0 提示词：三种格式（JSON / 文字 / 元提示）、UI 原型、信息图、参考表 |
| `higgsfield-models` | “该用哪个模型？” / 模型比较 |
| `higgsfield-camera` | 运镜问题（视频） |
| `higgsfield-style` | 视觉风格 / 美感问题 |
| `higgsfield-character-design` | 前期故事圣经：前提 / 世界 / 九问角色 / 故事脊柱 / 视觉 DNA（写提示词之前） |
| `higgsfield-scene-engine` | 场景/段落结构审查：目标 / 障碍 / 策略 / 反转 / 价值转变（花额度之前） |
| `higgsfield-troubleshoot` | 失败的生成 / 质量问题 |
| `higgsfield-audio` | 支持音频的模型的音频设计、对白、音效、环境声 |
| `higgsfield-seedance` | Seedance 2.0 / Pro 提示词导演 + 内容过滤预检 lint（+ `higgsfield-seedance-hell-grind.md`，Higgsfield 开源的长片制作流程） |
| `higgsfield-seedance-2-5` | Seedance 2.5 多参考写法：四种模式（t2v / omni_reference / video_edit / video_extension）、参考职责语法、30 秒分阶段、编辑 + 前后向延伸、关键帧、分镜、白模、转场（+ `higgsfield-seedance-2-5-vfx-pipeline.md`，AI 视效制作流程：按资产类型选模型、尺寸参照帧、`omni_reference` 视频到视频通道、四批规则、劣质效果清单） |
| `higgsfield-seedance-vfx` | Seedance 2.0 的视频到视频素材变换：保留真实主体 + 镜头运动，加一个特效元素 / 换环境 / 放一个照片写实的生物 / 重新打光匹配 / 同步一次计时变焦，用 std 4K 跑 |
| `higgsfield-acting` | 把角色表演当作压力下的行为：目标 / 障碍 / 策略 / 节拍 / 潜台词，身体 + 地位 + 空间距离，必须的眼神生命力，表演母本及其逐场改写，固定音色 |
| `higgsfield-shotlist-director` | 说明/剧本 → 一张相连的 Seedance 分镜表（风格前缀 + `@` 资产表 + 带名字的逐场提示词），做成可编辑的 HTML |
| `higgsfield-facs` | 用 FACS 动作单元代码在 Seedance 2.0 里做精确的面部表情：勉强/诡异/混合表情、近景对白面部表演、情绪→AU 配方、FACS 参考表 |

> 完整词汇见 `vocab.md`
> 模型比较见 `model-guide.md`
> 共享约束见 `negative-constraints.md`
> 各题材注释模板见 `template-*.md`
