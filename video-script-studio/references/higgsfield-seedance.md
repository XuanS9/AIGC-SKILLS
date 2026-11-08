# Higgsfield Seedance 导演（Higgsfield Seedance Director）

## 速查（QUICK FACTS）
- 过滤器是一个读取整场意图的大语言模型，不是关键词黑名单：描述一个**场景**，而不是一个主体；先修语气 [→](#过滤器模型先读这个the-filter-model--read-this-first)
- 秒拒（<10 秒）= 过滤器拒绝；迟败（>30 秒）= 基础设施/复杂度问题：秒拒的提示词绝不原样重新生成 [→](#秒拒与迟败诊断instant-fail-vs-delayed-fail--the-diagnostic)
- 六个槽位，按顺序：运镜 + 主体 + 动作 + 环境 + 风格 + 光照；缺 3 个以上槽位就是被标记的来源 [→](#seedance-提示词公式the-seedance-prompt-formula)
- 经验性的提示词写作规律：50–80 词的注意力甜区（把承重元素放最前）、写出导演/镜头而不是“cinematic”、“fast”会让运动降质、正文里不写负面提示、单向运动链 + 具名的运镜终点 + 细节尺度跟随景别 [→](#提示词写作规律prompt-craft-laws)
- 五种提示词模式：Reference-Based / Continuation / Expand Shot / Edit Shot / Transformation：写之前先选模式 [→](#seedance-20-提示词模式seedance-20-prompt-modes)
- 制作提示词的 [OFFICIAL] 块骨架：SCENE CONTEXT → … → POSITIVE LOCKS，独立说明用分布式风格（相连的分镜表改为一字不差地粘贴编译好的风格前缀），视场角只用度数，CAMERA 块放第 3 位，切镜阶梯 oner / CUT n / timed / freestyle [→](#官方提示词结构块骨架official-prompt-architecture--the-block-scaffold)
- [FIELD] 13 个项目语料的校准：词数随语域增长（中位数从 218 词到 2,059 词：50–80 词的甜区只适用于单镜头），视频说明手写（`enhance_prompt` 关闭），风格前缀 = 每个项目的常量，编译进各自的归属块 [→](#实战校准13-个项目的制作语料field-calibration--the-13-project-production-corpus)
- [FIELD] 三种“好心本能”的漂移来源，各有一条常设锁定：环境编造（第 1 号，排在角色漂移之上）、角色身高拉平、远景的尺度漂移 [→](#正向锁定positive-locks)
- 人群/破坏/生物的安全构建：疏散后的城市、受限的打斗（“stays at the sea surface”）、安全的基准场景 [→](#安全构建人群破坏生物build-safe-construction--crowds-destruction-creatures)
- 延伸一段已有片段：作为视频参考附上 + 以“The scene continues.”开头：匹配源分辨率**和**时长；链条上限约 2 次（硬上限 3），之后从**原始**参考重新锚定 [→](#延伸提示视频参考续接extension-prompting--video-reference-continuation)
- **本文件是 Seedance 2.0。**用 **2.5**（四种模式，含 `video_edit` / `video_extension`，4–30 秒，30/10/10 张参考，提示词内或平台的首尾帧（仅 `omni_reference`），最高 1080p）时，读 `higgsfield-seedance-2-5.md`
- 教程演示的模式（参考职责词汇，含 VARIETY 参考、SCREEN REALISM + 时长匹配的合成、60:30:10 调色、红箭头道具标注）：本目录的 `higgsfield-seedance-production-patterns.md`
- [OFFICIAL] 长片制作流程（资产构建、逐场 GEO SPATIAL LAYOUT、固定位置的第一秒、对白构建、禁用词词典、10–15 次迭代规则、人群 / 巨物 / 门槛）：本目录的 `higgsfield-seedance-hell-grind.md`
- 表演（目标、障碍、策略、节拍、潜台词、眼神生命力、表演母本）：`higgsfield-acting.md`
- 引擎规则（不写年龄、出画 = 切镜、画外 = 不存在、不拍反射、追踪 ≤3 个角色）、双重对比技法 + 高风险镜头表：本目录的 `higgsfield-seedance-engine-rules.md`
- 参考职责：Character / Last-Frame / Environment / Prop：职责决定提示词可以重新描述什么 [→](#参考职责reference-roles)
- 工作模式：Exploration / Continuation / Bridging / Repair（和提示词模式不同）[→](#工作模式与提示词模式两套分类working-modes-vs-prompt-modes--two-taxonomies)
- 第 1 层说明 vs 第 2 层制作提示词：绝不把第 1 层粘进提示词框 [→](#两层提示词写作two-layer-prompt-authoring)
- 原生 **4K** 只在 `mode=std` 下可用；`mode=fast`（Seedance 2.0 Fast）最高 480p/720p [→](#预检-lintpre-flight-linter)
- 永远做预检：`python3 scripts/seedance_lint.py --preflight --model seedance_2_0 "<prompt>"`：枚举来自 `model-specs.json`（fast+1080p/4K 会被自动抓到）[→](#预检-lintpre-flight-linter)
- 480p 草稿验证的是提示词，**不是**那条素材：没有 seed 参数；用主画面 + 首尾帧来延续一种画面 [→](#草稿验证提示词而不是那条素材drafts-validate-the-prompt-not-the-take)
- ZH 提示词：1,800 字上限只属于双语 JSON / 旧的团队格式（`--profile bilingual-json`）；工作室块结构稿没有长度上限。ZH 反套话清单由 lint 执行 [→](#多语言提示词的变通办法multi-language-prompt-workarounds)
- 被标记的提示词 → 按 lint 规则查改写手册，然后过一遍语气 [→](#改写手册the-rewrite-playbook)
- 反复被标记 → 诊断确切的提示词，改写失败的指令，并核实修改后的结果 [→](#用户已经陷在失败循环里时when-the-user-is-already-in-a-failure-loop)


用户想要 Seedance 2.0 / Seedance Pro 提示词时，或者 Seedance 生成被拦截、被标记或静默失败时，使用这个模块。这个模块的任务是阻止额度浪费在过滤器拒绝上。本文件是 Seedance 2.0 的历史资料，只在选择 2.0 或做对应诊断时加载；当前项目默认 Seedance 2.5 `omni_reference` 和中文块结构（[跨类型导演模板](template-general-director-2-5.md)）。下面的英文代码块是原版示例。

> **引擎规则（和本文件一起读）：**Seedance 2.0 引擎的硬性渲染约束（不写年龄、出画 = 隐性切镜、画外 = 不存在、不拍反射镜头、追踪 ≤3 个角色、双重对比切镜规则）在本目录的 `higgsfield-seedance-engine-rules.md`，连同高风险镜头表（反射、同一角色的分身、人群、文字渲染）和它的缓解办法。本参考是那个规则核心的 `EN-director` *档位*；`ZH-house` 和 `bilingual-JSON` 档位（`seedance-bilingual-json.md`）遵守同一个核心。写作时就标出高风险镜头类型：绝不悄悄违反一条与项目主画面冲突的规则。

> **制作模式（兄弟参考）：**在 Higgsfield 自己的 Seedance-4K 影片教程里演示有效的模式（参考职责词汇、坐标站位、视频参考屏幕合成、提示出来的瑕疵、60:30:10 调色）在本目录的 `higgsfield-seedance-production-patterns.md`，标为 `[DEMO]`。

---

## 写提示词之前的叙事规划（Narrative planning before prompt writing）

在每种工作模式和提示词模式里都应用 [共享叙事规划](narrative-planning.md)。先规划目标和结局，然后找出值得成为阶段的故事事件、因果转折、揭晓和状态转换；之后才给动作、反应、对白、停顿和转场分配时间。不要预选阶段数，也不要平均分配时长。内容确实需要时，等长也是有效的。**阶段不是切镜或一段生成片段**：一个连续镜头可以跨几个阶段，一个阶段可以用几个镜头，生成边界取决于模式、复杂度、参考和实际模型限制。

把全部八个导演层当作共享的规划语义：**资产/参考职责；总体目标；全局视觉、声音和空间；主体行为和节奏；分阶段的表演；连续性/状态继承；最后一帧/接点；限定范围的约束**。按情况把它们编译进六槽短格式、已有的输出字段或制作块骨架。它们不是八个必须的输出标题，也不替代参考职责语法、正向锁定或预检。每个阶段带着它的起始状态、主要变化、可见反应和结束状态；下一个阶段继承结果。最后一帧和转场都算进时间预算。重复的动作、安静的停顿和复原需要一个故事目的，适用时还需要明确的状态变化。

对 Edit Shot 和局部 Repair，按原时间码标注源素材的事件，保留源时长、节奏和切点，明确要求的编辑除外。向后续接时，继承源素材结尾的姿势、运动相位/方向/速度、构图、光照、道具和情绪状态，以及音频相位。前传/向前延伸必须以源素材的**第一帧状态**结束，包括那些运动中的和可听的状态。只有新素材获得新的时间预算；下面匹配源素材的延伸规则和 4–15 秒的生成/输入限制仍然适用。Expand Shot 保留它空间编辑的目的；Transformation 保留它连续的片内状态变化弧线。

## 过滤器模型：先读这个（The Filter Model — Read This First）

Seedance 2.0 的内容过滤器**不是**关键词黑名单。它是一个语言模型，把整条提示词当作一个场景来读，判断意图和语境。大多数用户花几个小时换单个词：这个循环没用。

过滤器比较两样东西：

- **读起来像电影人在描述一个镜头的提示词** → 往往能过。
- **读起来像给朋友的留言的提示词** → 往往会失败。

一个单独看起来敏感的词，可以放在一条构建良好的电影感提示词里而不出问题：过滤器读的是整幅画面。一条没有画面可读的提示词（没有环境、没有视觉目的、没有叙事逻辑）不给过滤器任何可以依据的东西，它就会偏向谨慎。

**实用规则：**提示词必须描述一个**场景**，而不是一个**主体**。先修语气，再修用词。

---

## 秒拒与迟败：诊断（Instant Fail vs. Delayed Fail — the Diagnostic）

这一条经验规则在每次失败时都能省时间：

| 失败时间 | 含义 | 怎么做 |
|----------------|---------|------------|
| **< 10 秒**（秒拒） | 内容过滤器拒绝：提示词根本没到 GPU | 为语气改写 + 去掉风险词。不要原样重新生成。 |
| **> 30 秒**（迟败） | 基础设施、超时或复杂度：提示词通过了过滤器，但渲染失败了 | 简化动作密度、缩短长度，再试 |

如果用户**循环遇到秒拒**，那是过滤器问题：绝不是 GPU 问题。改写之前先阻止他们重新生成。

---

## Seedance 提示词公式（The Seedance Prompt Formula）

每条 Seedance 提示词都应该按这个顺序覆盖这六个槽位：

```
[Camera movement] + [Subject] + [Action] + [Setting] + [Style] + [Lighting]
```

六个槽位技术上都是可选的：但六个都有的提示词几乎从不被标记，因为过滤器有完整的语境来理解每个词。缺 3 个以上槽位，就是被标记的来源。

### 最小可用的 Seedance 提示词（Minimum viable Seedance prompt）

> **Slow dolly-in on a figure in a dark overcoat standing alone at the end of a rain-slick alley. Cold teal shadows, single practical streetlamp, shallow depth of field.**

运镜 ✓ 主体 ✓ 动作 ✓ 环境 ✓ 风格 ✓ 光照 ✓：六个槽位都有，约 30 词，因为场景完全清楚所以能通过过滤器。

---

## 提示词写作规律（Prompt-Craft Laws）

一组 Seedance 2.0 专用的提示词规则。这些是**经验性的**：实践者的 A/B 发现，从架构上看说得通，但**不在**官方模型规格里。把它们当作很强的经验规则，让仓库的迭代纪律（`higgsfield-prompt.md` § The Iteration Rule）在你自己的素材上确认它们，而不是当作有保证的模型行为。

### 长度和顺序：注意力模型（Length and order — the attention model）

Seedance **从左到右读提示词，注意力权重递减**。第一句影响最大；到第三句你就进入了“细节地带”，模型不再把元素当作主要指令，而是开始分散地取样。

- **甜区：50–80 词（短格式模式）。**一条 70 词的提示词，稳定地胜过同一场景结构相同的 200 词版本：超过约 3 句之后，多出的词买到的是扩散，不是控制。（块骨架制作提示词是另一种模式：§ Official Prompt Architecture。工作室块结构稿不设字数上限。）
- **用三句话组织：**① 主体 + 动作，② 运镜 + 风格，③ 约束 / 正向锁定。
- **以最承重的那一个元素开头。**镜头靠主体成立时，主体打头；靠一次运镜成立时，运镜打头。

**和两个长度数字的关系。**这个 50–80 词的数字是*连贯性最优点*。§ Pre-flight Linter 里 >180 词的数字是*另一个维度*：过滤器/编码器的风险上限（>220 常常让文本编码器直接失败）。50–80 是该待的地方；约 180 是开始坏的地方。它们不冲突。

**和六槽公式的关系。**六个槽位保证过滤器看到一个*完整*的场景（存在）。注意力模型管的是*权重*（顺序 + 长度）。六个槽位都保留，但槽位列表“运镜在前”的顺序是一份完整性清单，不是要求在镜头的身份是主体时也用运镜词开头。

### 写出具体的东西：删掉空洞的形容词（Name the thing — kill empty adjectives）

`cinematic`、`epic`、`beautiful`、`high quality`、`amazing` 是附在大量训练素材上的高频标签（黑暗惊悚片、明亮的爱情喜剧、自然纪录片都读作“cinematic”），所以模型从一个宽而散的分布里取样，它们不会把输出推向任何具体的方向。不要只删掉套话词（Voice Rewrite §6）：**换成一个具名的、训练范围窄的参照**：

| 空洞的形容词 | 具名的替换（从窄分布里取样） |
|---|---|
| “cinematic” / “epic look” | 一位**导演**：“Wes Anderson symmetry”（居中构图、粉彩）· “Kubrick one-point perspective”（几何走廊） |
| “cinematic lighting” | 一种**布光**：“golden-hour backlight, long shadows stretching forward” |
| “beautiful” / “high quality” | 一个**镜头规格**：“anamorphic 2.39:1, lens flare from a practical light source” |

`higgsfield-prompt.md` § Anti-Slop Vocabulary 的正向形式。

> **关于导演名的官方覆盖。**Higgsfield 自己的提示词写作技能直接禁止导演名、代表作引用和器材型号名（见 § Official Prompt Architecture — the Block Scaffold → Measurable-language rules）。上面的导演替换技巧是经验性的短格式退路；在块骨架提示词里，改用可观察的说法描述画面：“centered symmetrical framing, pastel palette”，而不是“Wes Anderson symmetry”。工作室复制正文同样不写片名或导演名。

### “fast”是降质最严重的关键词（"fast" is the highest-degradation keyword）

和复杂动作或运镜一起用时，`fast` 是降质最严重的单个关键词。运动叠加时，时间分支已经在跑多个高速计算；`fast` 要求它们全部同时以最高速度运行。两个互相竞争的快速元素会抖动；三个会叠加成难以挽救的错误。

**修法：描述物理，而不是速度。**`feet striking hard, each stride at full extension, arms pumping at 90 degrees` 产生速度感，却没有降质。一个元素可以承载速度：只是不能所有元素同时承载。（和 Voice Rewrite §3 同一类：描述物理，而不是情绪。）

### 提示词正文里不写负面提示（No negative prompts in the prompt body）

Seedance 的提示词文本**没有负面嵌入架构**：每个标记都被当作*正向*指令来读。`negative: jitter, bent limbs` 被解析成模型试图渲染的场景描述（噪声），而不是约束，让输出变得更差。

用**正向的约束陈述**：直接声明什么必须为真：

```
Face stable. Limbs anatomically natural. Consistent lighting, no flicker.
Body proportions consistent throughout.
```

**范围：**这说的是 Seedance 提示词**正文**，目标是 `negative:` 列表语法 / 光秃秃的否定列表：不是每一个“no”标记。正向声明里的一个短锁定尾巴（“Consistent lighting, no flicker”；风格前缀的“Photorealistic — no 3D render”）没问题，在整个采集语料里经过实战验证。它**不**覆盖 Higgsfield 界面专门的负面提示词栏（一些图像模型有这个栏，`vocab.md` § Composition Vocabulary 用到它）。同样的只用正向的要求记录在 `negative-constraints.md` § Seedance Positive-Constraint Notes。工作室规则更严：Seedance 正文一律写正向目标状态。

### 歧义动词：同形词陷阱（v1.10，Peter 的发现，2026-07-14）（Ambiguous verbs — the homograph trap (v1.10, Peter's find 2026-07-14)）

如果一个词有一个说得通的第二种读法，Seedance 可能会采用它。观察到的情况：*“wind tearing at her coat”*：本意是布料被猛烈拉扯；模型有时把 *tearing* 读成撕裂（布料被撕碎）或流泪（哭），镜头就跟着变了。已知的提示词指南都没覆盖这一点：把它当作一级规律：

**一个动词交出去之前，问：这个词还能看起来像另一样实际的东西吗？如果能，换成只有一样东西能看起来像的说法。**

- `wind tearing at her coat` → `wind whipping violently at her coat` / `her coat flutters violently in the wind`
- 种子同形词清单（每次生成误读一个词时就加进去）：**tearing**（撕 / 哭）· **shoot**（开枪 / 拍摄）· **duck**（蹲下 / 鸭子）· **bolt**（跑 / 闪电 / 螺栓）· **draw**（拉 / 画 / 拔武器）· **wave**（挥手 / 海浪）· **charge**（冲向 / 电）· **rock**（摇晃 / 石头）· **drop**（掉落 / 水滴）· **fire**（火焰 / 开枪 / 解雇）· **strike**（击打 / 火柴 / 闪电）· **break**（打碎 / 休息 / 破晓）· **pound**（锤打 / 心跳）· **snap**（折断 / 拍照 / 打响指）。
- 这份清单是种子，不是规则：规则是那个自检，它永远可以推广到任何词。中文提示词同样有歧义词，按同样的自检处理。

### 社区 v3 精选（Joey 发布，2026-07-14 审核）（Community v3 cherry-picks (Joey drop, audited 2026-07-14)）

采纳的（之前这个模块里确实没有）：

- **摄影机放在阴影一侧，并写明操作者的轴线。**把摄影机放在主光的阴影一侧，并说明操作者站在/移动到哪里：光向镜头包过来，脸保持立体感。
- **远景里的细节（“蛇形镜头”）。**84° 低角度，紧贴一个小的前景物体：有细节镜头的亲密感，又不失远景的语境。
- **亲密的广角。**近脸用 63–84°，而不是长焦：有在场感但没有压缩；房间留在画面里。
- **提示词重置经验。**迭代越改越*差*时，停止叠加修正：把提示词剥回主体 + 动作 + 运镜，只重新加必要的东西。密度是一条钟形曲线；过了峰值，你就分不清模型丢掉了哪个元素。
- **规范参考优先于底片。**每个主体都保留自己的身份参考，即使它在环境底片里可见：底片承载世界，规范参考承载身份；绝不让底片兼作身份来源。
- **对比度曲线用三种方式说。**调色重要时，用色调曲线 + 去除高光 + 具名调色来写：只用一种说法会漂移。

拒绝的（原为：已标记，待测试日）：他们的世界构建器把镜头块放在**底部**（“在顶部，视场角会和身份数据打架”）：这和本模块的 CAMERA 放第 3 位规则、也和他们自己的 seedance 技能矛盾。**2026-07-26 由实战证据而不是测试日解决** `[FIELD — 13-project community harvest]`：在 9 位创作者的约 4,000 条采集的制作提示词里，CAMERA 块在每条最终提示词里都位于文档中部：从不在底部。CAMERA 放第 3 位成立；放底部的说法作废。

### 运动提示词规律（dramaclaw 制作语料，2026-08-09 审核）（Motion-prompt laws (dramaclaw production corpus, audited 2026-08-09)）

`[EMPIRICAL — dramaclaw production corpus, Seedance]`：在 dramaclaw 的 Seedance 制作工作中得出的实践者发现。这门手艺是与模型无关的图生视频运动写法，而不是 Seedance 规格；和本节其余部分同样的认识地位（很强的经验规则：在你自己的素材上确认）。

- **单向运动是一条控制漂移的经验规则。**一个早早完成的短动作，可能让模型通过**倒放**它来填时间。让运动有目的地一直进行到终点；同方向 2–3 个相连的动作是一个例子，不是动作配额。不要为了填时长编造动作。刻意的一来一回需要明确的原因、转折和结束状态；只有在可读性或渲染复杂度需要时才拆分镜头或生成。（失败的样子：`higgsfield-seedance-failure-modes.md` § Action-reversal fill。）
- **写出运镜终点。**一次运镜需要一个目的地，而不只是一个名字：说明**运动结束时画面里是什么**（“slow dolly-in, ending on her hands wrapped around the cup”），而不只是运动的名字。一次在片子结束前就用完指令的运动会漂移或倒退：这是单向规律在运镜上的一面。
- **细节尺度跟随景别。**近景配得上微细节（手指收紧、下颌一动）；远景配得上大弧线（穿过院子、人群分开）。交叉错配（微细节写进远景，或大范围穿越写进近景）在那个景别下渲染不出来，并会让整段片子降质。（远景*里*的细节是构图问题，不是提示词细节问题：见上面的蛇形镜头精选。）

### 已覆盖的兄弟规则（交叉链接，不是新规则）（Already-covered siblings (cross-links, not new rules)）

- **复合运镜**（`dolly in while panning left`）→ 在过渡处抖动，因为模型按顺序执行两个向量。用一个主要运动 + 一个质感修饰（`slow dolly in, slightly handheld`）。完整说明：`higgsfield-seedance-failure-modes.md` § Multi-motion camera overload。
- **图生视频的主体漂移** → 重新描述源图里已有的东西，会给模型同一个主体的两个互相竞争的输入；调和它们会带来漂移。图生视频提示词只写**运动 + 运镜**。见 § Seedance 2.0 Prompt Modes / Reference-Based 和 `higgsfield-prompt.md`（图生视频关键规则）。

---

## 官方提示词结构：块骨架（Official Prompt Architecture — the Block Scaffold）

`[OFFICIAL — Higgsfield prompt-writter.skill, 2026-07]`：Higgsfield 随 Seedance-4K 发布了自己的 Seedance 2.0 提示词写作技能。本节是那套方法，已与本文件其余部分协调。两者有分歧时，在块骨架提示词里以官方规则为准；本模块其他地方的经验规则仍然是短格式模式的规则。

**两种模式，不是矛盾。**六槽公式和 50–80 词的甜区（§ Prompt-Craft Laws）管短格式单镜头。块骨架是制作模式（多镜头、参考多、控制要求高的工作），在这里*结构取代字数上限*：控制重要的地方写得密，不重要的地方写得疏，每件重要的事说一次。预检 lint 会自动识别这种模式（标准块标签 / 镜头标记）并暂停短格式字数上限：识别不到时用 `--regime block` 强制：而每条结构性 lint 规则（镜头数、节拍总和、交接声明、枚举检查）仍然完整适用。同样，Voice Rewrite 里把 Style & Mood 一句放在最前的指示是短格式的过滤器检查：在块提示词里，过滤器从 SCENE CONTEXT、LOCATION MAP 和 LIGHTING 得到完整的场景，风格是分布式的（见下）。工作室的中文块结构是这种模式的中文形式，同样不设字数上限。

### 块的顺序（Block order）

按这个顺序写块，**只用镜头需要的块**：

```
SCENE CONTEXT
ACTIVE REFERENCES
LOCATION MAP
FIRST FRAME / BLOCKING
FORMAT MODE
OPTICS
CAMERA
ACTION
PERFORMANCE      (when acting matters)
PHYSICS
LIGHTING
COLOR GRADE      (when the grade is strong / stylized)
WARDROBE         (when costume matters)
AUDIO
STYLE            (technical-style suffix)
OUTPUT SETTINGS  (when format must be pinned)
POSITIVE LOCKS
```

逻辑：先语境和参考，然后空间和时间，然后动作和物理，然后描述性风格放在各自的归属位置，然后技术后缀，最后锁定。自然主义的单镜头可以完全去掉 COLOR GRADE、WARDROBE 和 OUTPUT SETTINGS，把这些内容并进 LOCATION MAP / LIGHTING。

### 分布式风格：独立块规则（Distributed style — the standalone-block rule）

在**独立的块骨架提示词**里，顶部没有风格前缀块；提示词永远以 SCENE CONTEXT 开头。每个风格方面放在管它的块里：光 → LIGHTING；颜色 → COLOR GRADE，或者自然主义画面时并进 LOCATION MAP + LIGHTING；镜头 / 光学特性 → OPTICS；皮肤真实感和表演 → PERFORMANCE；画幅 / 颗粒 / 帧率 → POSITIVE LOCKS 之前的 STYLE + OUTPUT SETTINGS 后缀。描述性风格在正文里挨着它描述的东西；技术性风格作为结尾后缀；没有任何风格相关的东西放在提示词开头。

**相连分镜表的例外** `[FIELD — 13-project harvest]`：在多场景的分镜表项目里，实战验证的形状正好相反：每个项目编译一个**风格前缀，一字不差地粘在每条场景提示词的顶部**（改一次 → 处处都改），然后是场景正文。在那里，25 个分开生成的场景之间的一致性比分布式的优雅更重要。那种模式归 `higgsfield-shotlist-director.md` § Per-scene prompt law 和 `template-global-style-prefix.md` 管；本节只管独立提示词。

### 视场角锚点 + CAMERA 放第 3 位规则（FOV anchors + the CAMERA-3rd-position rule）

在提示词文字里，视场角**只用下面这些离散锚点的度数**表示：绝不用毫米，绝不用中间值（不写“23°”：用 18° 或 29°）：

| 视场角 | 等效毫米 | 用途 |
|-----|----------|-----|
| 180° | 鱼眼 | 球面畸变：POV、梦境 |
| 107° | 14–16mm | 建筑超广角、史诗建立镜头 |
| 84° | 20–24mm | 广角：建立镜头、群体站位 |
| 63° | 28–35mm | 观察式、纪实 |
| 47° | 40–50mm | 中性的人眼视角 |
| 29° | 75–85mm | 肖像压缩、对白胸像 |
| 18° | 100–135mm | 近距离肖像、保身份 |
| 12° | 180–200mm | 长焦细节：手、物件 |
| 8° | 300–400mm | 极端压缩、观察、转播 |

多镜头里，逐段设定视场角，并加上 `"no drift mid-segment"`。

把 CAMERA 块放在提示词核心层的**第 3 位**（主体 → 动作 → 运镜 → 风格 → 约束）。挪到最后，视场角会被忽略；挪到最前，它会和身份冲突。

### 可测量语言规则（Measurable-language rules）

- **只用正向表述**：官方对“正文不写负面提示”这条经验规律的确认（§ Prompt-Craft Laws）。
- **速度用 km/h**：“moves at 40 km/h”，而不是“fast”（它也是降质最严重的关键词，§ Prompt-Craft Laws）。
- **氛围用 % / 米**：“fog density 40%”、“haze visible at 15 meters”；跨镜头分步建立（20% → 40% → 60%）。
- **巨大尺度用人身高比较**：“as tall as four humans stacked head to toe”，而不是“huge”或“three meters”。
- **左右永远以摄影机为准。**
- **情绪通过肌肉运动，而不是标签**：和 Voice Rewrite §3 同一条规则；肌肉层面的极致是 `higgsfield-facs.md`。
- **白平衡用开尔文**，一场戏内固定：3200K / 4000K / 5600K / 8500K。
- **物理用真实单位写质量和尺寸** `[FIELD]`：PHYSICS 块写上重量，让重力读起来正确：`"the spider is 10–12 centimeters, 50–70 grams — it falls gently; the man is 70–80 kg — the drop lands hard."` 材料行为同样处理（`"the liana stretches slightly under load and creaks like fibrous wood"`）。
- **有因果的道具互动** `[FIELD]`：物体从不自己动；每个道具事件都需要一个可见的物理原因，并有事件顺序：`"the cup tips only from visible sleeve contact"` · `"a button press is a full mechanical event — contact, 2–3 mm of travel, click, spring-back; the screen lights only AFTER the click."`
- **不写导演名、代表作或器材型号名**：它们会被忽略，或者打乱复杂运动；改为描述画面。（在这种模式里覆盖 § Prompt-Craft Laws 里经验性的导演替换。）
- **只用英文提示词**（历史上的中文例外见 § Multi-Language Prompt Workarounds；工作室当前交付用中文块结构，台词用 `{}` 内的原语言）。

### 正向锁定（POSITIVE LOCKS）

**锁定**是一句短的硬性固定语，放在它保护的东西旁边：`"headlights stay glowing in every shot"`。POSITIVE LOCKS 块为提示词收尾：连续性（角色、道具、环境在切镜之间完全一致）加上对关键信息的一次正向重申。这是 § Prompt-Craft Laws 里的正向约束陈述在块提示词里的位置。（工作室格式对应 `[保持一致]`。）

**三种具名的“好心本能”漂移来源** `[FIELD — 13-project harvest]`：模型自己的本能，各需要一条常设锁定：

1. **环境编造：第 1 号漂移来源，排在角色漂移之上。**只要附了场景参考，模型就会“好心”地把房间加宽、添上没给它看过的家具；多位创作者称这是片段之间最大的单一漂移来源。常设锁定：`"the set contains only what the reference shows — no added furniture, rooms, or geography beyond the reference"`，在重要的地方加上明确的“没有”（`"nothing on the floor, nothing on the bed"`）。工作室中文稿写成正向：“场景只包含参考中的陈设”“地面空着，床上空着”。
2. **角色身高拉平。**画面里有两个人时，模型会往同样的身高漂。在**每一条**有 2 个以上角色的提示词里写真实身高（`"she is 165 cm, he is 178 cm"`），让相对尺度永远不飘。
3. **远景里的尺度漂移。**人形锚点在切镜之间缩成一个点。锁定它：`"the rider stays the calm human-sized anchor — never shrunk to a tiny distant dot."`

### 切镜格式阶梯（Cut-format ladder）

四个精度级别：一个刻度上的点，选镜头需要的那一个：

1. **一镜到底**：`"one continuous shot, the camera does not cut on its own."`
2. **有顺序的切镜，不带时间码**：`CUT 1 … CUT 2 … CUT 3`，按顺序描述，切镜重要但精确时间不重要时用。
3. **计时多镜头**：在写明的秒数处明确切镜（`1.0s HARD CUT`），节拍必须按时钟落下时用。
4. **自由空镜**：不锁定切镜；让模型自己找角度。

只要指定了切镜（计时或不计时），就加上：`"cuts only at the specified points, the camera does not cut on its own."` 切镜词汇：`HARD CUT`、`SMASH CUT`、`MATCH CUT`、`INSERT CUT`、`REVERSE CUT`、`WHIP CUT`；淡入淡出/交叉淡化只在明确要求时用。这个阶梯解决了 § Output Format 里的“选边”反模式（本想一镜到底却写了逐秒标签，会被读成切镜指令），而计时节拍加起来仍然必须等于声明的时长（4–15 秒），按那里的时长算术。

### 标签命名 + 最少的参考文字（Tag naming + minimal reference text）

- 用户指定的标签原样使用；否则按加载顺序 `@image1 @video1 @audio1`：与 § Reference Roles → Per-Image Role Convention 一致。（工作室项目的调用名是 `@` + 纯中文名，以资产总表为准。）
- `@TAG:` 参考行 = 职责/体型 + 当前状态 + 独特的可见特征 + 动作关键细节 + 音色（只在有台词时）+ `"100% matches the reference"`。**不写年龄。**官方技能自己的模板用一个年龄词开头；引擎规则 1（`higgsfield-seedance-engine-rules.md`）在两种语言里都禁止它，而 Higgsfield 的长片说明给出了原因：内容过滤器一读到未成年人就会急剧收紧（`higgsfield-seedance-hell-grind.md` § Wording rules）。用体型、穿着和姿态承载同样的信息。
- **参考角色的文字保持最少**：长的外貌文字会和图像打架并让它降质（和 § Prompt-Craft Laws 里图生视频主体漂移规则同一个机制）。
- **关键细节无论如何用文字写出来**：小字、标识、颜色：即使在参考里看得见；模型可能会丢掉它们。
- **绝不在那个物体不在场的镜头里放它的 `@tag`**：模型会把它硬塞进画面。

**给标签本身命名** `[FIELD — Higgsfield Studio, ONEIRIC breakdown, 2026-08-13]` 上面几条说的是标签*行*包含什么；在任何规模的项目里，*名字*也需要一套约定，背后的规则是**一个元素，一个名字**。没有它，项目会长出重复：同一张沙发住在三个名字下面，没人分得清哪张参考才是真的：

```
@loc_ON_dorm_commonroom_front_s2     type + project + name + [angle] + scene
@char_ON_Rudy_s2_v1                  type + project + name + scene + version
@prop_ON_pizza                       type + project + name
```

- **场景后缀把资产绑到它所在的地方**，所以一个房间的两种陈设，或者一个场景跨时间跳跃的两个版本，不会撞车。
- **状态变化时出现版本后缀**：而变化后的状态是**一个有新名字的新资产，绝不覆盖旧的**。宿舍里的一个角色和病床上的同一个角色，是同一个人的两个资产。这一条是身份纪律在命名上的一半。
- 标签是任意字符串，所以大小写混用是安全的，**一致是唯一的规则**。让相关的名字看得出配对（场景和它的站位参考共用一个词干），一眼就能看出哪些资产属于一起：站位侧的写法见 `template-staging-reference.md` § Tag naming。

### 上下文隔离（Context isolation）

每次生成都是一张白纸，不记得之前的镜头。绝不带入场号、剧本标题、前一场的概述、没用到的标签或角色，或者“as above / continues”这类说法。这就是为什么下面的续接提示词公式要求一字不差地重新粘贴身份，而不是回指先前的提示词。

### 特殊协议（Special protocols）

- **四机制的极端视场角多镜头组合**（8° / 107°）：① 整段的身份锁定（所有节拍用同一张场景参考），② LENS LOCK 开头：每个节拍开头写明确的视场角短语，③ LENS CHECK 结尾：每个节拍结尾确认视场角，④ 颜色通过材质 + 光来写，而不是一份清单。**四个都要，否则极端视场角多镜头在 2–3 个节拍后就会崩。**
- **甩镜需要 ≥0.8 秒的模糊行程**：少于 0.8 秒会渲染成没有模糊的硬切（稳定 → 0.8 秒甩镜 → 稳定）。
- **实时 / 慢动作混合：**速度模式之间只用硬切；每个镜头从头到尾一种速度。
- 裂缝/破碎的**反撞击锁定**：`"crowd PRESSES, not strikes"` · `"fracture originates from edge stress, not center impact"` · `"no impact point — pressure-based crack"` · 时间上从边缘到中心依次发生，而不是从一点放射。
- **观察模式**（偷拍效果），三样同时用：前景遮挡占画面 20–30% + 摄影机和主体之间的大气雾 + 8–12° 的远距离机位。节拍之间换遮挡的类型；机位保持一个。

这些协议在真实素材上的应用（逐段 LENS LOCK、计时的 SMASH/MATCH 切镜、屏幕合成）见本目录的 `higgsfield-seedance-production-patterns.md`。

### 实战校准：13 个项目的制作语料（Field calibration — the 13-project production corpus）

`[FIELD — community harvest 2026-07-18: 13 shared Higgsfield projects, 9 creators, ~4,000 production prompts pulled via API with full params]`。语料对块骨架确认和校准了什么：

- **骨架在整个平台上都成立。**每个项目（写实冒险、韩剧爱情、电视剧、日式动画、定格民间故事）都用同样的“风格前缀 + 约束 + 可变 SHOT”结构，块的构成相同。旗舰项目 1,240 条 Seedance 提示词里 95% 出现了“SHOT”标记；15 秒是主导时长（他们生成长的多镜头片段，再剪出最好的几秒）。
- **按语域的词数阶梯。**Seedance 提示词长度的中位数跟随语域和野心，而不是固定上限：技术演示 218 词 → 电视剧 538 词 → 广告 779 词 → 类型选集 955 词 → 冒险电影 1,433 词（p90 2,648）→ 定格情感剧 2,059 词。50–80 词的甜区（§ Prompt-Craft Laws）是*单镜头*方法；制作多镜头说明比它高一个数量级。长度随表演复杂度增长：绝不为了整齐截断一段反应弧线。
- **语域收缩模板。**写实保留每个块（带真实质量的 PHYSICS、毛孔级的 PERFORMANCE）；风格化的工作（日式动画、定格）去掉 PHYSICS/皮肤真实感，保留 SHOT 节拍 + 连续性 + 严格的媒介锁定。见 `higgsfield-style.md` § Register Poles。
- **风格前缀是每个项目编译的常量。**在相连的分镜表项目里，语料把它**一字不差地放在每条场景提示词的顶部**（第一条里的“风格前缀 + 约束 + SHOT”结构：那是交付的形式，不只是写作笔记）。独立块提示词则把这些方面*分布*进各自的归属块（§ Distributed style — the standalone-block rule）。交付哪种形式由流程决定，而不是由喜好：见 `higgsfield-shotlist-director.md` § Per-scene prompt law。
- **视频提示词是手写的。**每个采集到的 Seedance 任务里 `enhance_prompt` 都不存在/关闭，而 1,022 个图像任务里是打开的：让增强器扩展图像提示词，绝不扩展视频说明。
- **Seedance 任务上观察到的平台层参数**（Higgsfield 入口，不一定是原始模型 API）：`multi_shot_mode: "custom"`（计时多镜头模式）、`genre: "auto"`、`speedramp: "auto"`、`mode: "std"`、`bitrate_mode: "high"`、`generate_audio: true`、4K 下 21:9。
- **迭代经济学**（先测试的文化、每个留下的镜头 65–100 次生成、五个文件夹的纪律）：`production-benchmarks.md` § Community-corpus anchors。

---

## Seedance 2.0 提示词模式（Seedance 2.0 Prompt Modes）

Seedance 2.0 提供五种生成模式，每种都接受六槽公式，但把它应用到不同的起点上。选对模式在写提示词之前：同一个句子在不同模式里会产生不同的结果，因为每种模式把提示词读成不同类型的指令。

### 基于参考（Reference-Based）

提示词围绕一张承载视觉身份（角色、服装、色板，有时还有构图）的源图搭建场景。提示词的任务**不是**重新描述图里已经显示的东西；而是把主体放进一个新的动作、环境或运动语境里。这是任何需要角色在不同镜头间保持一致的段落的主力模式。

```
[Source image role: "as the main character" / "as the starting frame"].
[Action the subject performs]. [Environment and atmosphere if not visible in source].
[Camera movement]. [Lighting cue if different from source].
```

### 续接（Continuation）

提示词把之前的一次 Seedance 生成在时间上往后延伸，从上一段片子的最后一帧接起。身份、服装、环境和情绪状态全部延续。提示词应该描述**接下来**发生什么：绝不描述刚才发生了什么。完整的五规则构建方式见紧接着的“续接提示词公式”一节。

```
[Continuing from prior clip]. [New action that follows from the last frame].
[Camera direction for the continuation]. [Any state change — light shift, new beat].
```

### 扩展画面（Expand Shot）

提示词扩大一个已有画面的画布或空间范围：把画面边界往外拉，揭示原来边缘之外的东西。这**不是**时间延伸（那是 Continuation），也**不是**原生成里的一次拉远运镜。它重写画面本身以包含更多场景。适合把一个紧的构图变成更宽的建立镜头，而不用从头重新生成。

```
[Source frame reference]. Extend the scene [direction: outward / upward / leftward].
[What appears in the newly revealed area]. [Preserve the original subject/composition].
```

### 编辑画面（Edit Shot）

提示词修改一次已有生成里的特定元素，其他一切完全保持原样。把它想成一个定向补丁：换夹克颜色、去掉一个背景人物、换一个道具、调整一个面部表情。身份、运镜、构图和光照保持锁定，除非你在改动清单里明确点名它们。保留规则在这里很重要：永远在写要改什么的同时写明要保留什么。

```
Change [specific element] to [new state]. Keep [everything else] unchanged.
[Preserve identity, composition, lighting, and camera behavior from the original.]
```

### 变形（Transformation）

提示词描述单个片段内的一次明确状态变化：主体、物体或环境在镜头时长内可见地变成别的东西。不同于 Continuation（跨两个片段延伸时间），也不同于 Edit Shot（事后修改一个生成的片段）。Transformation 发生在生成*过程中*，在一个连续镜头里。

> **不要和素材变换（视频到视频）混淆。**这个 Transformation *提示词模式*是从零生成的片内变形。当用户从一段**他们已经拍好的真实片段**开始，想在保留主体 + 镜头运动的同时加一个视效元素、换掉世界或放进一只生物时，那是 `higgsfield-seedance-vfx.md` 里的视频到视频流程（`@source` 语法、锁定句、光照融合、std-4K）。镜头的核心想法就是变化本身时用这个模式：一个角色变形、一个物体腐坏、一片风景从一个季节转到另一个季节。下面的骨架是为角色 → 角色写的；物体 → 物体和环境 → 环境套用同样的模式，换掉相应的名词。

```
[Subject in starting state — full identity descriptors]. [Triggering moment or
cue]. [Subject mid-transformation — what visibly changes, in observable
physical terms]. [Subject in ending state — new identity descriptors].
[Camera behavior across the change]. [Lighting / palette shift if any].
```

变形必须是一条连续的弧线，而不是一次切镜。明确描述中间状态：模型需要一个中点锚点，否则它要么从开始直接跳到结束（看起来像切镜），要么渲染出含糊的模糊。对简单的变形，5–8 秒是一个经验上可控的窗口示例，不是必须的阶段长度。按触发、物理变化和可读的结果分配时间，在实际模型限制之内；更长的复杂变形可能会漂移。

### 模式选择规则（Mode Selection Rule）

已有角色的新动作用 Reference-Based。时间上的下一个节拍用 Continuation。在空间上加宽画面用 Expand Shot。修补特定细节用 Edit Shot。镜头的核心想法是单个片段内的状态变化（变化就是内容）时，用 Transformation 提示词模式。如果你发现自己在一条提示词里跨多种模式写：停下，选一种，生成，然后把输出作为下一种模式的输入。

---

## 续接提示词公式（Continuation Prompt Formula）

写 Continuation 模式的提示词时，应用这五条规则。跳过任何一条，是续接失败最常见的原因：身份跨边界漂移、动作重播、环境变化、情绪线断开。

### 五条规则（The Five Rules）

1. **最后一帧锚点。**以对上一段片子最后一帧里摄影机看到什么的简短描述开头：姿势、在画面里的位置、角色在看哪里。这告诉模型从哪里开始渲染。一句就够。

2. **身份锚点。**把角色的身份块（你在原始提示词里用的同一段）一字不差地粘进续接提示词。不要改写。不要缩短。续接边界是身份漂移的地方：一字不差地重新粘贴，不给模型重新解释的余地。

3. **上一段作为次要记忆。**用一行点明刚才发生了什么：“following the door opening”、“after the punch lands”、“continuing from her turn toward the window”。不要详细重新描述动作。一个指代短语，然后往下走。

4. **立即续接。**新动作从上一段最后一帧之后的那一帧开始。没有时间跳跃、没有淡化、没有暗示的切镜：除非用户明确要求。如果他们要跳跃，把它描述成一个新镜头。

5. **不重复动作。**新提示词必须延伸，而不是循环。如果上一段以她拔出武器结束，续接**不**描述她拔出武器：它描述她接下来用武器做什么。重复一个描述过的动作，就是造成“上一个节拍重播”症状的原因。

### 必须延续的东西（What Must Carry Over）

跨续接边界，保留：角色身份（脸、体型、辨识标记）、服装（每件衣服和配饰）、环境（建筑、光的质感、色彩处理、空气中的粒子），以及情绪延续（角色在最后一帧时的状态：紧张、疲惫、警觉：在续接开头仍然应该在身体上读得出来）。

> “情绪延续”分解成的八个具名的底层通道，见 `vocab.md` § Emotion as Visible Behavior — Channels。

### 示例（Example）

上一段片子结束在一位侦探站在门口、身后下着雨、回头瞥了一眼。续接提示词：

```
Continuing from the prior clip — the detective framed in the doorway, head
turned, rain behind her. [Identity block verbatim: weathered woman, mid-40s,
short dark hair, charcoal trench coat, leather gloves, tired but alert.]
Following her glance back, she steps fully into the corridor, lets the door
swing shut behind her, and begins walking toward camera. Slow dolly-back
matching her pace. Same cool blue-grey palette, same overhead practical light.
Tense, controlled energy carrying over from the prior clip.
```

五条规则都在：最后一帧锚点（框在门口、头转过去、身后下雨）、身份锚点（方括号里的块，一字不差）、上一段作为次要记忆（“following her glance back”）、立即续接（完全迈进走廊：下一帧的动作）、不重复动作（那一瞥被提到，而没有重演）。

### 延伸提示：视频参考续接（Extension Prompting — Video-Reference Continuation）

`[EMPIRICAL — cross-surface, verified on Dreamina]`：没有任何 Seedance 入口提供专门的“延伸”按钮。有效的延伸路径：把已有片段作为**视频参考**附上（`video_references` 媒体职责），并以 **“The scene continues.”** 开头。模型从片段结尾接上，延续运动、角色、环境，甚至声音。上面的五条规则仍然适用：附上的片段只是用真实的东西代替了文字描述的最后一帧锚点。

- **前传：**改用 **“Show me what happens before”** 开头：模型生成*通向*源片段的片子。从源片段的第一帧倒着规划：新片段的最后一帧必须和它的构图、主体/道具状态、运动相位、方向、速度、光照和音频接点一致。过去 / 现在 / 未来都可以围绕一个锚点片段串起来。
- **支持时匹配源分辨率；按下一个事件预算时长。**1080p 源 → 1080p 续接，避免画质跳变。在 4–15 秒内选一个合法时长（1080p/4k 需要 `mode=std`）；15 秒→15 秒的匹配是一个可选的历史工作流选择。有原生延伸模式时遵守它的实际约束。同步的屏幕合成仍然需要它自己的时长锁定（`higgsfield-seedance-production-patterns.md` § Video-Reference 1:1 Lock + SCREEN REALISM）；那个要求不管自由续接。
- **喂尾巴，而不只是一帧** `[FIELD — 13-project harvest]`：制作实践把完成素材的**最后 3–4 秒**作为 `@video` 参考喂回去，而不是一张最后一帧静帧：片段把*运动*带进接点，所以下一个镜头从上一个停下的地方接上确切的姿势、构图、光和运动，而不是从一个冻住的姿势重新开始。
- **被遮挡的身份绑定：**如果某个身份特征在源片段结尾被挡住（一颗痣在手后面），把角色图作为第二参考加上并明确绑定：`"The woman's identity is @Image1."`
- **链条会退化。**每次延伸都重新喂入一次生成的生成，累积瑕疵。`[FIELD — community, seedance-2.0 repo v6.6.0]`：预计到第 4–5 次链式生成时出现可见漂移；**无缝链条上限约 2 次（硬上限 3），之后从原始的规范参考重新锚定**：场景边界是从规范参考重新打开的刻意切镜，而不是第 4 次延伸。必须更长的段落：在延伸之间插一个空镜切出，打断链条。
- **用提示词设计的切点（可选的覆盖）：**故事需要切镜时，一次延伸可以以一次机位变化结束（`"the scene from the character's perspective"`）。不要把这个强加在无缝续接上，也不要用它代替向前延伸的第一帧接点。
- **源素材承载状态：**附上的片段承载状态；延伸文字只承载变化：写开头那句之前，看 § Reference Roles → Load-Bearing Rule 下的 `[FIELD]` 补充。
- **延伸对白：**写下一句台词之前，查 `higgsfield-audio.md` 里按语言分的对白同步预算表：可靠的口型同步词数在不同语言之间差别很大。

---

## 工作模式与提示词模式：两套分类（Working Modes vs Prompt Modes — Two Taxonomies）

上面的 Seedance 2.0 提示词模式一节点名了平台提供的五样东西：Reference-Based / Continuation / Expand Shot / Edit Shot / Transformation。这些是平台机制：Seedance 接受提示词的不同通道。下面的参考职责和工作模式两节点名了两个相邻的概念，平台词汇里没有：

- **工作模式**：用户意图。你坐下来写提示词时，想用这门手艺**做**什么。
- **提示词模式**：平台机制。Seedance 通过 5 个输入通道中的哪一个接受提示词。
- **参考职责**：提示词里每张参考代表什么。一个语义职责层，不同于输入模态的用例模式（按场景的 `@Image1` / `@Video1` / `@Audio1`）。

这三套分类是平级的，不是层级的。一个 Seedance 镜头同时用到三者：一个工作模式的意图选择一个提示词模式；提示词里的参考扮演特定的职责。

### “Continuation”一词的撞名（The "Continuation" Word Collision）

“Continuation”在两套分类里都有：

- **Continuation 工作模式** = 用户意图：“我在接着上一个镜头停下的地方往下做。”
- **Continuation 提示词模式** = 平台机制：把之前的生成在时间上往后延伸的那个特定 Seedance 输入通道（见上面的 Seedance 2.0 提示词模式一节）。

处于 Continuation 工作模式的用户几乎总是用 Continuation 提示词模式：意图和机制对得上。但 Bridging 工作模式也可能用 Continuation 提示词模式（桥接锚定在上游镜头的最后一帧上时），Repair 工作模式也可能用 Continuation 提示词模式（修复是从失败片段的同一个最后一帧开始重拍时）。名字重叠；意思不重叠。

在本模块里，章节语境会消除歧义：如果周围内容在工作模式一节里，“Continuation”指意图；如果在 Seedance 2.0 提示词模式一节或续接提示词公式一节里，“Continuation”指机制。如果仍然有歧义，总可以用更长的形式：“Continuation 工作模式”和“Continuation 提示词模式”。

### 工作模式 → 提示词模式映射（Working Mode → Prompt Mode Mapping）

| 工作模式  | 典型的提示词模式                | 起作用的参考职责                |
|---------------|---------------------------------------|----------------------------------------|
| Exploration   | Reference-Based，或纯文生视频          | Character（可选）                   |
| Continuation  | Continuation                          | Character + Last-Frame                 |
| Bridging      | Reference-Based 或 Continuation       | Character + Last-Frame + Environment   |
| Repair        | Edit Shot，或重新 Reference-Based   | Character +（失败镜头的参考）    |

不是严格的映射。一个工作模式根据镜头需要走一个或多个提示词模式；这张表锚定典型情况，不声称是一一对应。

---

## 参考职责（Reference Roles）

Seedance 提示词用参考（`@Image`、`@Video` 和 `@Audio`）跨镜头锁定特定的属性。每张参考根据它锁定什么，扮演四种职责之一。这是一套语义职责分类：参考在提示词里**是用来做什么的**。它和输入模态的用例模式（按文件类型的具体提示词写法）并列，而不是叠在它上面。工作室当前的职责映射写法以 [Seedance 2.5 多参考说明](template-omni-reference-2-5.md) 为准。

如果一个属性必须在多个镜头之间一致，就把它分配给一个参考职责。如果它只对一个镜头重要，就写在行内。

Higgsfield 的 Seedance-4K 教程里演示过的三个提示词内职责*短语*（`"100% matches the reference"`（身份锁定）、`"STYLE REFERENCE ONLY"`（模型可以扩展的环境）和 `"VARIETY reference"`（人群阵容表，克隆军团的修法））收录在 `higgsfield-seedance-production-patterns.md` § Reference-Role Vocabulary。

### 角色（Character）

跨镜头锁定主角身份：脸、体型、辨识标记。几乎总是图像参考；要最高的一致性，用工作室 [角色资产交付规范](template-character-asset-delivery.md) 的组板。

Seedance 提示词里的写法：

```
@Image1 as the main character. [Identity block verbatim.] [Action the
subject performs.] ...
```

### 最后一帧（Last-Frame）

把一段新片子的开头锚定到上一段的一个特定画面上。这个职责告诉模型从哪里开始渲染。用于 Continuation 提示词模式和 Bridging 工作模式里。完整的五规则构建方式见上面的续接提示词公式一节。

Seedance 提示词里的写法：

```
Continuing from the prior clip — [short description of what the camera
sees in the final frame of the prior clip]. [New action that follows.]
```

### 环境（Environment）

跨镜头锁定世界和环境：建筑、光的质感、空气中的粒子、天气状态。这个职责告诉模型动作发生的具体空间，和空间里的任何角色分开。同一个环境在足够多的镜头里反复出现、值得做一张设定表时使用。

Seedance 提示词里的写法：

```
@Image1 as the environment. [Subject + action.] [Lighting / atmospheric
cues consistent with the environment reference.]
```

### 道具（Prop）

锁定特定的反复出现的物件：一件主打服装、一把标志性武器、一个品牌产品、一辆在多个镜头里出现的载具。这个职责告诉模型这个特定的物件（不是它所属类别的一个泛泛实例）必须在切镜之间读起来完全一样。

Seedance 提示词里的写法：

```
@Image1 as the prop. [Subject interacts with the prop.] [Camera
behavior.] [How the prop appears in the new shot — same geometry and
material as the reference.]
```

### 深度图（Depth Map）

`[FIELD — Higgsfield Studio, ADILIADA breakdown, 2026-08-14]` 一张灰度图，**亮的区域近，暗的区域远**。模型把它读作场景的深度骨架：一种明确的三维读法，固定构图、体积和比例。它防止的失败是一个**在镜头之间自己重新布置的空间**：没有深度锚点，几何会漂移，一个场景每隔几秒就悄悄重新规划一次。

在空间本身必须保持的地方用它：特定房间里的一场打斗，必须保持同一套建筑的一场追逐。它是*几何*输入，不带风格：和负责表面和光的环境参考配对使用。

### 提示词留不住时，把它烤进资产（Bake it into the asset when the prompt will not hold it）

`[FIELD — Higgsfield Studio, ONEIRIC breakdown, 2026-08-13]` 一个通用的做法，也是本文件里最有用的之一：**当一个属性不管写得多好都会漂移时，停止写它，把它往前挪一步：把它生成进资产里。**参考图于是承载这个属性，模型从底片上读出它，它就不再是文字每个镜头都得打赢的东西。

实例是**变形宽银幕光学**。在视频提示词里要求时，镜头特性在镜头之间漂移。在*图像*阶段要求时，它保持住：因为底片本身变成了镜头。图像模型里也没有“anamorphic”开关，所以效果是用镜头的几何拼出来的，写在场景图提示词的末尾：

```
STRONG anamorphic lens character: horizontal squeeze and compression,
oval elliptical bokeh, horizontally stretched highlights, curved barrel
edge distortion, chromatic aberration toward the edges.
NO lens flares, NO light streaks, NO floating bokeh circles. 2.39:1.
```

用 *subtle / gentle / moderate / strong / maximum* 控制剂量。跟着来的垃圾（光晕、拉丝、漂浮的焦外光球）**只在图像阶段**禁止。

> **然后再也不提这些词。**视频提示词里光学词汇完全不出现：**连禁止都不写**：因为在否定下点名一样东西会把它召唤出来（`negative-constraints.md`）。视频提示词只描述干净的镜片和收敛的光晕；变形宽银幕的特性随资产一起到来。

这可以推广到光学之外：一种颗粒结构、一种镜头特性、一种偏色、一群要花一段话才能写清的人群：文字总是丢掉的任何东西，都是烤进底片的候选。注意代价：烤进去的属性不再能逐镜头指导，所以只烤应该在整段里*恒定*的东西。

### 逐张图的职责约定（Per-Image Role Convention）

参考调用名（`@Image1`、`@Image2`、`@Video1`、`@Audio1`）按上传顺序分配：附上的第一张图成为 `@Image1`，第二张成为 `@Image2`，依此类推。制作实践给每个槽位锁定一个稳定的职责分配，在分镜表的每条提示词里保持一致，这样团队和模型都知道哪张参考承载哪个属性，而不用重读提示词正文。

| 槽位       | 职责                          |
|------------|-------------------------------|
| `@Image1`  | 角色身份            |
| `@Image2`  | 服装                       |
| `@Image3`  | 环境 + 光照        |
| `@Image4`  | 构图                   |
| `@Video1`  | 只取运动                   |
| `@Video2`  | 只取运镜          |
| `@Audio1`  | 节奏 + 氛围           |

`@Audio1` 在**时间上是承重的**，不只是氛围：上传的音频文件是一个条件输入，驱动切镜时间、运镜加速和动作节奏（节拍同步），而提示词正文里的 `[AUDIO: Xs]` 剧本块生成对白 + 音效 + 口型同步。两者，加上“只提取前 15 秒”的陷阱，记录在 `higgsfield-audio.md` § Audio as a Conditioning Input。下面的时间兼容性约束（`@Video1` 的运镜风格不能和 `@Audio1` 的节奏打架）是 Load-Bearing Rule 在音频上的情况。

槽位顺序不是模型强制的：它是团队侧的纪律。回报是长分镜表里的参考稳定性：一旦项目里 `@Image1 = 角色`，每条提示词都成立，没人需要在第 47 个镜头重新检查模型期待哪张脸。

参考和提示词文字冲突时（服装参考是红色，文字说蓝色），在提示词正文里明确解决它：`@Image2 as costume reference, but recoloured to blue for this shot`。不要让一个没解决的冲突到达模型。

### 承重规则（Load-Bearing Rule）

**参考支持记忆，文字定义动作。**Seedance 提示词里的参考承载跨镜头一致的持久属性；提示词文字指导这一次生成里发生什么。参考不能驱动新动作；文字不能替代参考承载的东西。两层各走各的道。

这是 v3.7.1 运镜侧规则的兄弟表述（“动作上提示词赢，质感和世界感上参考赢”：见 `higgsfield-camera.md` § Video Reference — What It Reads, and What It Can't, § Load-Bearing Rule）。同一个底层原理，来自不同的入口。运镜侧规则点明冲突时谁赢；Seedance 侧规则点明各自覆盖的道。

> `[FIELD — community, seedance-2.0 repo v6.6.0]` **源素材承载状态。**当一段已采用的片段或最后一帧作为参考附上时，源素材承载状态：提示词文字只承载*变化*。删掉重复附上的源素材已经显示内容的开场状态描述；参考和文字冲突时，**参考优先于文字**。有一类状态无论如何都留在文字里：静帧承载不了进行中的运动向量、运镜相位或音频相位：即使附了画面，进行中的运动和时间也必须用文字重述。在 § Continuation Prompt Formula → Extension Prompting 里应用于延伸。

同样的区分适用于更上一层：在提示词构建流程上，而不只是在提示词内部。当一段 Seedance 片子成功了、你想让下一条提示词匹配它的画面时，截下那一帧，上传**给 Claude，而不是给 Seedance**。Claude 需要看到画面才能写出匹配它的提示词；Seedance 接收得到的文字提示词，渲染下一段片子时不附截图。截图是参考（给构建提示词的模型）；文字提示词是动作（给生成模型）。

---

## 画面坐标系（Frame Coordinate System）

**画面坐标系**锁定主体、道具和构图元素在画面里的位置。

### 定性锚点（Qualitative anchors）

标准的电影语言位置说法，因为在训练数据里大量出现，所以机器可读：

- **水平：**`left third`、`center`、`right third`
- **垂直：**`upper third`、`lower third`（垂直居中是默认，很少需要说）
- **纵深：**`foreground`、`midground`、`background`

### 百分比记法（Percentage notation）

定性锚点不够具体时用数字坐标：

- **x 位置：**`0%`（画面最左边缘）到 `100%`（画面最右边缘）
- **y 位置：**`0%`（画面顶部）到 `100%`（画面底部）
- **画面占比：**主体填满画面面积的百分比，用来钉住景别（紧的近景在 `60-80%` 占比附近；远的建立镜头主体在 `15%` 以下）

定性锚点不够明确时用百分比：例如两个角色在画面同一半。

### 两种记法配对使用（Pair the two notations）

在**同一条提示词里**同时给出定性锚点和百分比记法，而不是二选一。定性词给模型电影语言的钩子；百分比给它精度目标。例：

```
Character A stands in the right third, x-position 70%, y-position
50%, frame occupancy 25%. Character B stands in the left third,
x-position 25%, y-position 55%, frame occupancy 22%.
```

### 不是数学保证（Not a mathematical guarantee）

画面坐标是**很强的构图锚点，不是几何保证**。模型把它们当作导演意图（就像摄影指导在分镜上读到“right third”），而不是像素级精确的目标。和其他标准构图词汇（`over-the-shoulder`、`eye line`、`ground contact`、`headroom`、`nose room`、`crossing rule`：最后一个在 [vocab.md](vocab.md) § Composition Vocabulary → Crossing rule 里正式定义）一起用，而不是替代它们。

输出里一个坐标漂移了，那是预期的行为类别：坐标设定了意图；模型按它的最佳理解渲染。调整提示词的办法是收紧定性锚点，或者加一个接触点句（`feet on the marked floor mark`、`right hand resting on the table edge`）从物理上让位置落地，而不是更用力地重新指定百分比。

---

## 空间布局块（Spatial Layout Block）

**空间布局块**是 Seedance 提示词里一个具名的结构单元，把 § Frame Coordinate System 里的空间词汇字段合并成一个块，让模型能读作一份连贯的空间说明。画面坐标系提供*词汇*，空间布局块提供使用它的*结构*。工作室格式里，这些内容写进第一段定位秒的 `摄影：` 行和 `[保持一致]`（见 [空间布局](spatial-layout.md)）。

零散的空间指令迫使模型从碎片里重新拼出场景几何：而它常常拼错。

### 块里放什么（What goes in the block）

一个完整的空间布局块，对画面里的每个主体写出：

- **身份**：这是哪个角色/道具/元素（有参考时和参考职责的调用名一致）
- **画面位置**：按上面 § Frame Coordinate System 配对的定性锚点 + 百分比记法
- **纵深层**：前景 / 中景 / 背景
- **画面占比**：主体填满画面面积的百分比
- **身体朝向**：主体面向的方向（朝镜头、背对、左侧面、右侧面、四分之三朝镜头）
- **接触点**：主体落在什么实际表面或物体上（`feet on wet asphalt`、`back pressed against the wall`）

多人块再加上跨主体的关系：相对距离、主体之间的视线方向、画面左右的一致性、主体是否越过中央垂直轴、什么遮挡什么。

### 何时用空间布局块（When to use a Spatial Layout Block）

三个触发条件：

1. **画面里有一个以上的主体。**双人戏是模型最常在没有指示时互换画面位置或越过中轴的地方。一个块能防止这种情况。
2. **一个需要跨镜头读得出的特定构图意图。**同样的站位必须保持几个节拍时（一个角色锚在左，另一个锚在右），块让锚点明确并可复用。
3. **容易出失败模式的镜头。**进门镜头、走廊方向镜头，以及任何模型历来会拼错空间的镜头，都受益于在前面放一个块，而不是行内的空间碎片。

单个主体在清楚位置上的镜头很少需要完整的块；在 Dynamic Description 里放一个定性加百分比的锚点就够了。

### 块和提示词的配合（Block-and-prompt fit）

空间布局块在输出格式里位于 Dynamic Description **之前**（见下面的 § Output Format for Seedance Prompts）。它先给模型完整的几何；Dynamic Description 再描述在那个几何里发生的动作。

块不替代六槽公式：运镜、镜头、光照和镜头时间留在各自的槽位里。

---

## 工作模式（Working Modes）

工作模式是平台机制之上的用户意图层。它点明你坐下来写一条 Seedance 提示词时想**做**什么：和你最终走哪个提示词模式无关。工作模式（意图）和提示词模式（机制）的关系见上面的消歧一节。那里的映射表显示了典型路线。

### 探索（Exploration）

开放式的发现。没有之前的镜头可以锚定；没有要匹配的约束。你生成是为了弄清这个镜头想成为什么。这里短提示词有效：模型有空间带入自己的理解。通常走 Reference-Based 提示词模式（带一个角色锚点）或纯文生视频（完全没有参考）。

### 续接（Continuation）

从上一个镜头停下的地方接着做。之前的片子是锚点；新片子从它的最后一帧继续。工作模式和提示词模式对得上：Continuation 工作模式几乎总是走 Continuation 提示词模式。五规则构建方式见上面的续接提示词公式一节。

### 桥接（Bridging）

连接两个目前接不顺的已有镜头。镜头本身没问题；它们之间的切镜感觉不对：空间地理不清楚，或者情绪能量不匹配，或者镜头性质跳变。Bridging 用两端的参考（上游镜头的最后一帧和下游镜头的第一帧）来走通中间。通常走 Continuation 提示词模式（上游最后一帧是主导锚点时）或 Reference-Based（两端分量相同时）。常见的参考职责配置：Character + Last-Frame + Environment。

### 修复（Repair）

修一个失败的镜头。不同于改一下提示词重新生成：Repair 承认失败的片子是数据：它告诉你模型理解错了什么，而那个理解需要被直接处理。通常走 Edit Shot 提示词模式（失败是局部的时候：夹克颜色错了、少了一个道具）或者带纠正性提示词文字的全新 Reference-Based 生成（失败是结构性的时候：动作节拍错了、身份漂移了）。在纠正性提示词上迭代时，配合 `higgsfield-prompt.md` § The Iteration Rule。

### 决策树：选一个工作模式（Decision Tree — Picking a Working Mode）

你选哪个模式，取决于你在作品里注意到了什么。按症状诊断，然后选合适的模式：

| 你看到的情况 | 工作模式 | 原因 |
|---|---|---|
| 一张白纸，还没有锚点 | Exploration | 没有之前的镜头可以续接或桥接；先自由发现。 |
| 一个很强的镜头需要后续 | Continuation | 这个镜头值得一个续集；从它停下的地方接上。 |
| 两个很强的镜头接不上 | Bridging | 镜头都行；它们之间的接缝不行。 |
| 镜头很强但感觉弱 | Continuation（换职责） | 用不同的参考职责承载分量重拍同一个节拍：例如原来是远景的地方改用近景。 |
| 段落中途空间逻辑感觉不对 | Bridging（澄清地理） | 段落需要一个重新建立谁在哪里的节拍。 |
| 一个你一直绕着生成的失败镜头 | Repair | 停止在提示词上迭代。直接针对失败。 |

决策树是症状优先，不是模式优先。模式是治疗；你作品里的症状是诊断。如果你发现自己伸手去拿一个模式，却说不出是什么症状驱动了这个选择，那就是该退一步的信号。

---

## 两层提示词写作（Two-Layer Prompt Authoring）

骨架提示词不是用来盲目复制进 Seedance、期望它自己就能用的。骨架是一个结构：提示词的逻辑，而不是完成的提示词。这对 Bridging、Continuation 和 Repair 工作模式（见上面的 § Working Modes）最重要，因为这三类任务严重依赖语境：之前发生了什么、之后必须是什么、这个镜头究竟要解决什么。

这个流程里每个实用骨架都有两层，各自面对不同的读者、承担不同的任务。第 1 层使用 [共享叙事规划](narrative-planning.md)，包括八个导演语义；第 2 层把相关决定编译进这个模式原生的骨架。两个写作层不是阶段数或镜头数。

### 两层的区分（The Two-Layer Distinction）

- **第 1 层：任务定义 / 说明块。**写给自己，或者在起草制作提示词之前粘进一个 ChatGPT 式的助手。用平实的文字解释实际问题：已经有什么场景、下一个场景是什么、它们之间缺了什么、什么必须保持不变、桥接或修复必须达成什么。第 1 层是规划步骤：它迫使写提示词的人在写面向模型的提示词之前清楚地定义问题。

- **第 2 层：给 Seedance 的制作提示词。**更短、更干净、更面向执行。把第 1 层的决定翻译成模型友好的结构：参考职责先声明，保留条款，那一个动作，防重复的措辞，运镜提示，音频提示。第 2 层是粘进生成框的东西。

这个区分让流程可行。没有第 1 层，桥接会失败，因为写提示词的人还没决定桥要解决什么；续接会变成重新调度而不是续接，因为写提示词的人没点明要保留什么；修复会改过头，因为写提示词的人没隔离出要改什么。两层的存在就是为了通过把规划步骤和执行步骤分开，防止这三种失败模式。

### 桥接骨架（Bridge Skeleton）

Bridging 工作模式（见上面的 § Working Modes / Bridging）是解决问题的模式：桥不是泛泛的电影感填充。两个场景块都没问题、但它们之间的连接不行时用这个骨架。

**第 1 层：桥接说明块。**具名字段：

```
Scene A ends with:
[final visible state of upstream scene]

Scene B begins with:
[opening visible state of downstream scene]

The missing thing between them is:
[reaction / movement into a new space / prop action /
emotional beat / spatial clarification]

The bridge must preserve:
[same character, same outfit, same location logic,
same emotional residue, same prop continuity]

The bridge must not do:
[no new subplot, no repeat of previous action,
no extra threat, no random spectacle]

The purpose of the bridge is:
[explain the transition / make the cut readable /
carry emotion / reposition the viewer in space]
```

**第 2 层：桥接制作提示词骨架。**参考职责先声明，然后是桥接条款：

```
[Reference roles]
@Image1 = character identity reference
@Image2 = continuity start or location anchor (omit if neither is needed)

This is a bridging shot between the previous beat and the next scene.
Its purpose is continuity, not spectacle.

Keep the same character, same outfit, same space logic, same emotional
carryover, and same prop continuity.
Show one readable action that explains the transition.
Do not repeat the previous action beat.
Do not introduce a new threat or subplot.

Scene: [where the character is in this transition moment]
Bridge action: [one small but meaningful movement or reaction]
Camera: [restrained and readable]
Audio: [live sound only if needed]
```

一座好桥和动作戏比起来常常显得“小”，但承担了重要的结构工作。如果第 2 层提示词产出的东西感觉事件太多，那第 1 层说明里的“must not do”条款可能写得太薄：修改说明，再重新推出制作提示词。

### 续接骨架（Continuation Skeleton）

Continuation 工作模式（见上面的 § Working Modes / Continuation）解决的是时间问题，不是连接问题：下一段片子必须紧接着上一段开始，而不是一次新的重新调度。这个骨架执行上面续接提示词公式一节的五条规则：特别是第 5 条“不重复动作”。

**第 1 层：续接说明块。**具名字段：

```
The previous clip ends on:
[end pose / camera direction / emotional state /
visible props]

The next clip must begin immediately after that.

Keep:
[identity / body direction / location / emotional
carryover / props]

Change:
[the new beat that begins now]

Do not repeat:
[the previous action phase]
```

**第 2 层：续接制作提示词骨架。**典型配置是三个参考职责：

```
[Reference roles]
@Image1 = exact last-frame continuity anchor
@Image2 = character identity reference
@Image3 = optional environment or prop continuity reference

Use @Image1 as the exact continuity start anchor.
Keep the same character, same lighting logic, same spatial continuity,
same emotional carryover.
Start immediately after the final frame.
Do not repeat the previous beat.

Scene: [what remains unchanged]
New action: [what starts now]
Camera: [how the viewer reads the continuation]
Audio: [live sound only if needed]
```

**如果结果总是重播上一个节拍，**纠正办法不是“把提示词写长”。纠正办法是加强时间和防重复的措辞。有用的短语变体：

- start immediately after the final frame
- do not repeat the previous fight
- do not restage the earlier beat
- continue forward into the new action
- preserve the same fatigue state and emotional carryover

这些可以互换：选动词和上一段内容匹配的那个。打斗戏之后的续接要用“do not repeat the previous fight”；安静时刻之后的续接要用“do not restage the earlier beat”。（工作室中文稿写成正向：“紧接上一段最后一帧，继续向前进入新动作”。）

### 修复骨架（Repair Skeleton）

Repair 工作模式（见上面的 § Working Modes / Repair）不是“把这场戏再生成一遍，但更好”。那会破坏连续性、改动太多。真正的问题永远是：我究竟要保留什么，我究竟要改变什么？一条可用的修复提示词有两部分，直接对应这个问题：一个保留块和一个修改块。

**第 1 层：修复说明块。**具名字段：

```
Current clip / image state:
[what already works and must remain stable]

The exact problem:
[what is wrong]

Preserve:
[identity / framing / pacing / space / continuity /
lighting / emotion / prop logic]

Change only:
[one or two specific elements]

Do not damage:
[what tends to drift if the edit is too broad]
```

**第 2 层：修复制作提示词骨架。**紧凑、外科手术式，没有描述性装饰：

```
Keep the original framing, pacing, duration, event timestamps, cuts, environment,
and character identity, except where the scoped edit explicitly changes one.
Preserve the same outfit, same lighting logic, same scene layout,
same emotional state.
Change only [the exact element that needs fixing].
Do not alter the rest of the shot.
```

第 1 层里的“do not damage”字段最常被跳过，也最常是修复失败的来源。点明编辑范围太宽时通常会漂移的属性：那些就是模型需要明确保护的属性，即使它们不是编辑针对的属性。

---

## 关键帧流程（Keyframe Workflow）

关于精细 Seedance 编辑最有用的官方指导，来自 BytePlus VideoPilot：字节跳动 / BytePlus 官方的 Seedance 编辑式界面。VideoPilot 不把精细视频编辑当作一条含糊的“修好这段片子”提示词，而是当作一个**参考 + 关键帧 + 局部修改**的流程。三个具名的组成部分，各有各的任务。

本节点明 VideoPilot 界面提供什么（能力范围），在不用专门界面时怎么把这些基本操作翻译成纯提示词的 Seedance 工作（翻译成 Seedance 提示词），以及让整个方法起作用的底层思维（做剪辑师，而不是重新生成者）。

> **来源：**下面的关键帧编辑能力范围来自 BytePlus VideoPilot 微调文档（`docs.byteplus.com`）和字节跳动官方的 Seedance 发布材料（`seed.bytedance.com`）。和 Rule of 12 引用同一组官方来源：历史上的 Seedance 2.0 资产预算。

### 能力范围（Capability Surface）

VideoPilot 提供五种具名的编辑基本操作。这些是官方界面让你做的事；下一节的提示词侧翻译，是只用提示词工作时最接近的等价物。

- **连续关键帧切分。**VideoPilot 把一段参考视频解析成连续的关键帧段。切分由系统完成，不是手工拼装。编辑的单位是关键帧，不是整段片子。
- **精细的关键帧编辑。**编辑一次针对一个关键帧。在时间轴上是外科手术式的：改一帧的内容，不重写任何其他帧的指令。
- **自定义关键帧。**编辑者可以添加系统没自动检测到的关键帧。一个重要节拍落在自动切分的关键帧之间时有用。
- **局部重绘选中区域。**关键帧内的空间局部编辑：遮住区域，只重绘遮罩里面的东西。在空间轴上是外科手术式的（相对于精细关键帧编辑在时间轴上的手术）。
- **改写关键帧描述。**改写一个关键帧的描述，会让系统重新生成那一帧**以及**它和相邻关键帧之间的过渡逻辑。这是最接近 Seedance Edit Shot 提示词模式的官方基本操作（见上面的 § Seedance 2.0 Prompt Modes / Edit Shot）。

### 翻译成 Seedance 提示词（Translating to Seedance Prompts）

通过提示词和参考工作、而不是专门的 VideoPilot 关键帧界面时，最接近的实际等价物是六条操作规则。它们都不保证在每个界面里都能完美地外科手术式编辑：它们把官方编辑流程翻译成基于提示词的用法。

1. **用一张截图或最后一帧作为稳定锚点。**
2. **让身份参考和连续性锚点分开。**
3. **确切写明什么必须保持不变。**
4. **确切写明什么在变。**
5. **如果是续接，禁止重复上一个节拍。**
6. **如果编辑是局部的，只描述局部改动，并明确保护其余部分。**

这些对应仓库里已有的内容：第 3、4、6 条对应修复骨架的保留 / 修改块（见上面的 § Two-Layer Prompt Authoring / Repair Skeleton）；第 1、2 条对应参考职责分类（见上面的 § Reference Roles / Last-Frame 和 § Reference Roles / Character）；第 5 条对应续接骨架的防重复短语库（见上面的 § Two-Layer Prompt Authoring / Continuation Skeleton）。

### 做剪辑师，而不是重新生成者（The Editor-not-Regenerator Mindset）

整个关键帧流程的概念根源：如果目标是外科手术式的编辑，像剪辑师一样思考，而不是像全部重新生成的人。冻住必须保持稳定的部分。隔离必须改变的部分。然后让指令局部而明确。

这也是修复骨架的概念根源：保留 / 修改的划分，是“做剪辑师而不是重新生成者”立场在提示词侧的执行，和 VideoPilot 界面基本操作在界面层面表达的是同一种纪律。

---

## 预检 lint（Pre-flight Linter）

用户生成之前，把提示词跑一遍完整的预检：

```
python3 scripts/seedance_lint.py --preflight --model seedance_2_0 "<prompt text>"
```

lint 在仓库的 scripts/ 目录里（`../scripts/seedance_lint.py`）。`--preflight` 把两遍检查串成一份 PASS/WARN/FAIL 报告：

**1. 过滤器 lint**（始终开启）：

- 公众人物 / 名人 / 政治人物的**真名**
- **品牌、IP、系列名**（Nike、Marvel、Spider-Man、Pokémon 等）
- **直白的暴力动词**（fight、attack、kill、shoot、blood、gore、stab）
- **年龄标记**（child、kid、young、teen、boy、girl：Seedance 不写年龄）
- **给朋友留言的语气**（没有 Style/Mood、没有 Camera、没有 Lighting 部分）
- **超长**（>180 词是风险区；>220 词常常在文本编码器而不是过滤器上直接失败。块结构稿自动暂停这条字数检查）
- **互相冲突的指令**（moving + frozen、bright + dark 等）

**2. 结构 lint**（带 `--model <id>`；由 `model-specs.json` 驱动，从不猜）：代价高的失败类别：

- 声明的镜头数（“strictly N shots” / 严格N个镜头）vs 实际的 `【镜头N】`/`[Shot N]` 块数
- 计时节拍（`[0-4s]`）加起来超过声明的时长 / 模型上限
- ZH 提示词超过 1,800 字上限（仅双语 JSON 档位）；ZH 反套话短语
- `@handle` 在声明行之前被使用
- 画幅 / 分辨率 / 模式 / 时长超出模型的枚举：抓住 Seedance `fast`+1080p（fast 输出不了 1080p）

设置从提示词自己的头部行读取（`**Aspect ratio**: …`、`Resolution: …`、`mode: …`、`Duration: Ns`）；用 `--ar / --resolution / --mode / --duration` 逐字段覆盖。

输出是 `PASS`、`WARN` 或 `FAIL`，并给出每条命中规则的具体修法。把 `FAIL` 当作“不要点生成”。把 `WARN` 当作“大概能过，但这里是要加固的地方”。退出码：0 通过/警告，1 失败，2 用法错误：可以安全地用在脚本里。工作室块结构稿还要先跑 `director_contract_lint.py`。

---

## 草稿验证提示词，而不是那条素材（Drafts Validate the Prompt, Not the Take）

480p 档是用来**迭代提示词**的，不是用来批准素材的。Seedance 2.0 **没有 seed 参数**（已核实：`model-specs.json` 列出了 `resolution`、`mode`、`genre`，没有别的），所以把一条批准过的 480p 草稿用 1080p 重新跑，是一次**全新的抽签**：新的表演、新的运镜微轨迹、新的时间。“便宜地批准，再按质量重新渲染”不是 Seedance 支持的流程。

| 跨抽签保持（由提示词驱动：草稿**能**验证它） | 每次生成都重新抽（草稿**不能**验证它） |
|---|---|
| 镜头数和结构的遵循 | 表演：表情、手势的细微差别、微时间 |
| 站位的遵循（位置、方向、入画/出画） | 具名运动之内的运镜微轨迹 |
| @handle / 身份污染 | 片子内部的节拍时间 |
| 对白位置 | 细节（烟丝、铭文的可读性、反射） |
| 内容过滤器通过/失败 | |

要把你批准的画面带进最终渲染，用记录在案的转移机制：**主画面**加上**首/尾帧钉住**（start_image / end_image 参考职责：见上面的 § Reference Roles；当前项目走 `omni_reference`，把批准的画面作为场景/风格参考）。钉住画面，而不是抽签。细节判断必须**在最终分辨率下重新检查**：480p 遮住了它们关心的细节。

---

## 改写手册（The Rewrite Playbook）

lint 触发时，在保留预定场景的前提下，应用下面相应的替换。对照实际结果核实改写后的提示词。

### 真名 → 原型描述（Real names → archetype description）

❌ “Keanu Reeves walking into a boardroom”
✅ “A lean man in his late 50s, dark shoulder-length hair, stubble, intense calm expression, in a dark suit, walking into a modern glass boardroom”

（引擎规则 1 禁止年龄词；这条示例里的“late 50s”要换成体型和穿着，例如“a lean man with silver-streaked shoulder-length hair”。）

### 品牌 / IP → 只写视觉属性（Brand / IP → visual attributes only）

❌ “Spider-Man swinging through New York”
✅ “A figure in a red and blue form-fitting suit, masked, swinging between skyscrapers on a tensile white line”

❌ “Nike shoes on a running track”
✅ “White athletic shoes with a dark swoosh-free silhouette on a red rubber running track”

### 暴力 → 余波 / 张力 / 物理（Violence → aftermath / tension / physics）

❌ “Two people fighting in an alley”
✅ “Two figures locked in a tense physical confrontation, rain-slick alley, dramatic low-key lighting, camera shuddering on each impact”

❌ “An explosion destroys the car”
✅ “A burst of orange light and smoke billowing out from the car, metal buckling outward, glass fragments catching the light”

❌ “Blood drips from his hands”
✅ “His hands tremble at his sides, something dark staining his cuffs”

### 武器 → 道具 + 目的（Weapon → prop + purpose）

❌ “A man holds a gun to another man's head”
✅ “A standoff in a concrete stairwell — one figure's arm extended, the other perfectly still, both silhouettes hard-edged against a single overhead fluorescent”

### 恐怖 / 黑暗 → 氛围，而不是行为（Horror / dark → atmosphere, not acts）

❌ “A monster tears a victim apart”
✅ “The aftermath of something wrong — an empty room, overturned furniture, a single smear trailing toward the door, ambient dread, flickering practical lamp”

### 安全构建：人群、破坏、生物（Build-safe construction — crowds, destruction, creatures）

`[OFFICIAL — Higgsfield cinematic-prompt-builder skill, 2026-07]`：不要描述有风险的东西再指望它通过；从一开始就把场景搭得安全。替换后的版本通常读起来*更*有电影感，而不是更少：对峙比屠杀更紧张，疏散后的城市比惊慌的人群更诡异，一声咆哮比一次杀戮更有力量。

| 避免 | 改为搭建 |
|---|---|
| 惊慌的平民、在碎片下逃跑的人群 | 一座**疏散后 / 空荡**的城市；被遗弃的街道；一个孤独的人形作为尺度 |
| 武器向建筑 / 向人开火 | 能量释放的对峙、扫过的探照灯、充能的光环、没有枪口火焰的冲击波 |
| 生物互相撕咬 / 血腥 | 扭打 / 对峙 / 险些擦过 / 绕圈 / 能量对撞：战斗是**受限的** |
| 有人身处危险的破坏 | **无人区域**里的破坏：冰川、沙漠、废墟、开阔海面、疏散区；人形对崩塌的地形*做出反应*，绝不是受害者 |

**限制同时也是物理。**给每一场生物打斗一条限制规则：`"the fight stays at the sea surface — breach, dive, grapple, submerge, never airborne"` · `"boss scale locked at ~2.5 human-heights, not kaiju-giant"`。让场景安全的同一句话，也让物理落地，并阻止尺度升级。

**安全的基准场景**：场景偏向风险时，把它拉回这个确认能通过的形状：一只原创生物（不是系列 IP），在一个泛化的纪念碑/圆形剧场场景里，白天，没有武器，做富有表现力的动作（升起、咆哮、展开翅膀）：有表现力而不是暴力。

---

## 语气改写：“电影人而不是朋友”这一遍（Voice Rewrite — the "Filmmaker not Friend" Pass）

即使去掉了所有风险词，语气不对的提示词仍然会被标记。对每条 Seedance 提示词做这一遍：

1. **在前面加一句 Style & Mood。**色板、镜头、光照、氛围。绝不跳过。它告诉过滤器“这是一个镜头”。
2. **点明运镜。**“Slow dolly-in”、“low-angle tracking”、“static medium”。而不是“the camera moves forward”。
3. **描述物理，而不是情绪。**“Jaw clenches, nostrils flare”而不是“looks angry”。过滤器把物理读作电影感；把情绪语言读作含糊的意图。这条规则在肌肉层面的极致（近景和对白里用 FACS 动作单元代码表示面部表情，例如愤怒用 AU4+AU5+AU7）见 `higgsfield-facs.md`。
4. **描述力量和方向，而不是破坏顺序。**“Driven into the car, metal buckling”而不是“thrown into side door, glass shatters, uses rebound to sweep leg”。
5. **现在时，主动语态。**“She turns”而不是“she is turning”。
6. **删掉套话词。**Breathtaking、stunning、epic、masterfully、cinematic masterpiece：这些是营销文案的信号，不是镜头描述，并且和被标记相关。

> “描述物理，而不是情绪”分解成的八个具名的底层通道，见 `vocab.md` § Emotion as Visible Behavior — Channels。

---

## Seedance 提示词的输出格式（Output Format for Seedance Prompts）

为用户生成 Seedance 2.0 原生提示词时，用这个结构。它对应 Seedance 过滤器读得最清楚的形式（工作室当前交付用中文块结构，见 [跨类型导演模板](template-general-director-2-5.md)）：

```
**Model:** Seedance 2.0
**Aspect ratio:** 16:9   **Duration:** 10s

**Style & Mood:** [palette, lens, lighting, atmosphere — 1 sentence]

**Dynamic Description:** [camera move + subject + action, present tense,
shot-by-shot if multi-cut. This is the main block.]

**Static Description:** [location, props, ambient details — 1-2 sentences]

**Camera:** [exact movement name]
```

完整的双语 EN+ZH 导演输出格式（用在 Seedance 的网页界面里），见扩展参考 `seedance-bilingual-json.md`。

### 多镜头提示词的时长算术（Runtime arithmetic for multi-shot prompts）

时长在交付的 Seedance 提示词里出现在三个地方：标题行、元信息头（`**Duration:** Xs`），以及 Dynamic Description 里的逐镜头时间标签。三者必须一致。

计时多镜头提示词里，每个镜头在行内标出它的时间范围（例如 `Shot 1 (0-3s): ... hard cut to Shot 2 (3-8s): ... hard cut to Shot 3 (8-15s): ...`）。这是一个例子，不是三镜头或 15 秒的默认；有顺序切镜和自由模式可以省略逐镜头时间码。逐镜头标签加起来必须*等于*标题和元信息头里写的总时长；这两处之间的偏差，是“我的多镜头提示词被渲染成了单镜头”失败最常见的来源。

用已确认的时长或模式的源时间。两者都没有时，按规划的事件估算，并在生成前确认交付时长；不要悄悄假定 5 秒、10 秒或 15 秒。固定时长约束的是节奏，不是阶段数。

### 多场景提示词的镜头密度（Shot density for multi-scene prompts）

把多个镜头行合进一条 Seedance 提示词时，按它们的因果连续性、表演负荷和时长来分组。每 4–5 个镜头行一条提示词是一个来自项目的例子，不是起始配额，也不是平台要求。

以下**全部**成立时，把镜头行合进一条提示词：

- 画面里是同一组角色
- 同一个场景，或一个场景里相连的一部分
- 连续的情绪 / 时间单元（没有时间跳跃，没有大的情绪转折）
- 合并时长在 Seedance 15 秒上限之内
- 合并后的提示词文字在实际生成限制之内：双语 JSON 档位的 ZH 提示词是 1,800 字上限（工作室块结构稿没有）；EN 块提示词没有对应的字数限制（制作中位数长得多：§ Field calibration）。曾经流传的“约 2,500 字符”预算是从 ZH 推出来的方法，不是 EN 的限制。

合并时长超过 15 秒，或者场景/时间变化、改变的角色调用名清单，在模型支持的镜头和复杂度预算内没法清楚表示时，拆成分开的提示词。受支持的多镜头场景切换或可读的入场可以留在一次生成里；保留必要的逐镜头重新锚定和引擎特有的出画/再入画处理。更完整的制作经验（五条分组标准、五个拆分触发、复杂度预算、“不要把哀伤切碎”规则）在 `higgsfield-shotlist-director.md` § Prompt density。

其他经验例子包括每 2–3 个密集动作行或 8 个以上安静情绪行一条提示词。没有一条决定阶段数。按实际内容分组，然后检查复杂度和生成预算。

### 单镜头还是多镜头（Single-vs-multi-shot decision）

默认是单镜头。内容是动作、动态对白，或者任何切镜本身在做单镜头做不到的事的地方，才用多镜头。其他一切作为单个连续镜头会更紧凑。

对连续运动，在一镜到底里描述由事件触发的阶段。时间重要时，`[0-3s] subject enters frame, [3-7s] camera pushes in` 是一个示意预算，配上 `one continuous shot; no cut at stage boundaries`。时间标签可能引发意外的切镜；出现这种情况时优先用相对的事件提示。它们是时间目标，不是帧级精确的保证。记法参考是 `vocab.md` § Editing Syntax。

计时多镜头用上面的时长算术并明确标出切镜；没有时钟的有顺序切镜，按叙事顺序用 `CUT n`。每次动作切镜都写明参与者、地点、器具和有因果的动作编排。不要把每个阶段或每个固定时间间隔都变成切镜。故事边界定下之后，再为了可读性选择镜头对比；对比指导不提供阶段数，也不要求在连续表演里切镜。

---

## 片段之后的决定（Post-Clip Decisions）

一段生成的片子在它周围引出问题时，测试就变成了叙事工作：不是“它好不好？”，而是“它做了什么？”和“之后是什么？”下面的诊断问四个关于场景功能的问题；决策树把答案映射到下一个镜头的类型。

### 四个问题（The Four Questions）

任何一段强的片子之后，按顺序问这四个。它们揭示这段片子在这一集里在做什么，以及接下来应该是什么。

1. 这场戏有什么功能？
2. 要让它感觉连得上，还缺什么？
3. 什么镜头能让这个连接读得出来？
4. 下一步是续接、桥接、对比，还是重置？

这些问题的范围是下一步，而不是“解决整集”。更窄的范围让它们保持实用。

### 下一个镜头的决策树（Next-Shot Decision Tree）

正确的问题不是“下一个最酷的镜头是什么？”，而是“这一集现在有什么问题？”把问题映射到镜头类型：

- **强但孤立** → 续接，或之前/之后
- **两场戏接不上** → 桥接
- **空间逻辑不清楚** → 澄清地理
- **结构可以但感觉弱** → 近景或反应插入镜头
- **有东西坏了** → 定向修复

下一个镜头按功能选，而不是按兴奋程度。

> 注意：这里的“续接”“桥接”和“定向修复”指的是生成之后决定的下一个镜头类型。上面 § Working Modes 里的“Continuation”“Bridging”和“Repair”指的是创作时每段片子的意图：不同的生命周期阶段，不同的决定。

---

## 用户已经陷在失败循环里时（When the User Is Already in a Failure Loop）

本节处理**过滤器拒绝**：Seedance 过滤器在生成之前拦截的提示词。**渲染失败**（帧率漂移、NSFW 误判、关键帧编造、物理状态漂移、空间感知失败、多重运动过载）见本目录的 `higgsfield-seedance-failure-modes.md`：兄弟目录，每种具名失败都有症状 + 机制 + 对策。

如果用户告诉你 Seedance 连续多次标记了他们：

1. **要被标记的确切提示词文字。**不要猜。
2. 对那段确切的文字**跑预检 lint**。
3. 对 lint 命中的每条规则**应用改写手册**。
4. **做一遍语气改写**（加 Style & Mood、点明运镜、现在时的物理）。
5. **核实修改后的结果。**检查预定的动作、身份、站位和音频在修复后是否保留下来。光是 lint 通过并不能确定生成成功了。

不要让用户只改一个词就重新生成同一条提示词。那就是浪费几个小时的循环。

---

## 多语言提示词的变通办法（Multi-Language Prompt Workarounds）

Seedance 提示词默认是英文。本节记录针对特定 Seedance 平台状态的历史语言层面变通办法。工作室当前交付用中文块结构，台词在 `{}` 里保留原语言。

### 中文（截至 2026-05-17）（Chinese (as of 2026-05-17)）

Seedance 2.0 发布时，模型对中文提示词表现更好，并且每条提示词有 3,000 字符的硬上限。英文大约每个词 5–10 个字符；中文 1–2 个。制作团队用中文提示词把约 5 倍的指令内容压进同样的字符预算：这是长的多镜头提示词在本会撞上限时的决定性变通办法。

这个变通办法是发布窗口期的优化，不是永久的约定。如果一条长的 Seedance 提示词总是撞上限，而英文压缩已经用尽，中文密度的路子以前交付过：用它之前，在当前的 Seedance 界面里核实上限状态。

---

## 相关模块（Related Skills）

- `higgsfield-seedance-2-5.md`：**Seedance 2.5**，全参考写法：四种模式（`t2v` / `omni_reference` / `video_edit` / `video_extension`）、4–30 秒、30/10/10 份参考素材、提示词内的首尾帧、视频编辑和前后向延伸。最高 1080p，平台首尾帧只在 `omni_reference` 里：任务长、是编辑形态或参考多时路由到那里；需要 4K、`mode=fast` 或题材提示时留在这里
- `higgsfield-acting.md`：填充 PERFORMANCE / CHARACTER ACTING 块的表演层：目标、障碍、策略、节拍、潜台词、地位、必须的眼神生命力、表演母本
- `higgsfield-seedance-hell-grind.md`（本目录）：Higgsfield 开源的长片制作流程：资产构建、逐场 GEO SPATIAL LAYOUT 块、固定位置的第一秒、对白构建、迭代纪律
- `higgsfield-seedance-vfx`：视频到视频的兄弟模块：变换用户已经拍好的素材（保留主体 + 运镜，加一个视效元素 / 换掉世界 / 放进一只生物 / 重新打光匹配 / 同步一次计时变焦），std-4K
- `higgsfield-prompt`：MCSLA 公式、原型路由、通用提示词结构；生成偏离目标又说不出原因时用的迭代规则和六遍诊断顺序
- `higgsfield-troubleshoot`：非过滤器失败的诊断（渲染质量等）
- `negative-constraints.md`：完整的共享约束参考，包括内容过滤 / 安全一节
- `seedance-bilingual-json.md`：扩展的双语导演参考（原型、切镜规则、镜头语言附录）
