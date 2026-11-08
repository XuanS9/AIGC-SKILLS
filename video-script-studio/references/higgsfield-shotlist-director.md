# Higgsfield 分镜表导演（Higgsfield Shotlist Director）

本模块负责用户选择HTML分镜时的交付容器；只要视频提示词时沿根入口交块结构文本，不因调用拆镜方法就额外交HTML。导演判断统一先执行 [导演决策流程](directorial-shot-design.md#导演决策流程)，HTML中的全局风格、资产表和进度不替代场景主次与镜头取舍。

把一份说明变成**一张连贯的分镜表**，而不是一堆零散的提示词。交付物是一个可编辑的 HTML 文件：用户在浏览器里打开，拍完一场勾掉一场，再回来找你修改。这是多镜头影片的文档流程：全局画面锁定一次，演员/道具/场景声明一次，然后输出继承这两者的、带名字的逐场提示词。

> **本模块提供连贯文档的流程。**先读 [根入口](../SKILL.md) 的项目默认、[共享叙事规划](narrative-planning.md)、[完整导演模板](template-general-director-2-5.md) 和 [完整演出范本](template-full-performance-example.md)。它们的块结构契约和演出细节决定提示词内容；HTML 保留全局风格前缀、资产表、编号、进度、复制按钮，以及改一次处处生效 / 场景覆盖。应用所选模型的语法和适用的预检：2.5 用 `higgsfield-seedance-2-5.md`，2.0/Pro 用 `higgsfield-seedance.md`。可选的原生骨架不覆盖完整视频的块结构契约。

**当前项目默认：****Seedance 2.5 · 16:9 · 中文**，除非用户另有指定。时长继承已批准的全片和段落预算；否则按动作和表演估计。没有设预算时，每个**生成片段**默认以所选模型的单次上限为目标（Seedance 2.5 为 30 秒；更短的模型取更短值）：把连续的多阶段动作装进一次接近上限的生成，优先把相邻镜头合进去；时长、连续性、参考容量或生成可控性需要时再拆开，绝不靠注水或慢放凑满。镜头时长和保留的剪辑时长仍跟随内容。编辑继承源时间线；延伸遵循其方向和模式限制。应用 [按内容拆镜与估时](narrative-planning.md#按内容拆镜与估时)：区分镜头时长、生成时长和保留的剪辑时长。

跨独立生成的接缝执行[独立生成与同场切镜](narrative-planning.md#独立生成与同场切镜)：允许同场剧情连续与交叉剪辑；动作匹配保留因果，不把精确首尾相位复现当作默认前提，不强迫停势、换场或逐段闭合整场戏。

## 速查（QUICK FACTS）
- **导演先于拆镜**：先定本段观众先看到什么、后知道什么、情绪转向、视觉命题、空间锚点与主动权，再决定镜头职责、景别、机位和切点；执行规则见 [顶级导演分镜方法](directorial-shot-design.md)。不得用固定秒数、固定镜头数或景别轮换代替导演判断。
- 输出 = **一个自包含的 HTML 文件**（内联 CSS/JS，无依赖），不是零散的提示词 [→](#你要产出什么what-you-produce)
- 从上到下三层结构：**全局风格前缀 → `@` 资产表 → 带名字的逐场提示词** [→](#三层结构the-three-layers)
- 逐场提示词规则：**块结构 → HTML 复制块**；可选的旧版 `Style → Characters → Scene → CUT 1..N` 映射保留完整演出内容。切镜和提示词边界跟随可见事件和状态交接，使用模型支持的时长 [→](#逐场提示词规则per-scene-prompt-law)
- 密度经验（改编自历史来源；以当前共享规划为准）：同一批角色、同一地点、一个情绪单元、一个可控的因果单元时合成一组；在换场、换角色、换机位、表演弧线、插入镜头或状态交接处，清晰度或模型限制需要时再考虑拆开：**不要把悲痛切碎**；说明太薄时有复杂度预算和自动补充默认 [→](#提示词密度把剧本节拍归成叙事单元prompt-density--grouping-script-beats-into-narrative-units)
- **镜头密度跟随所选场景方案**：按重点与支撑决定切/留/镜内交接，等待可保留真实重量；题材不自动决定快切或慢推，连接过程可合并。
- 交付前的整段检查：**节奏预算**（按剧情定的镜头长度对上要求的剪辑时长）+ **单调审计**（重复的构图/运镜要检查是否有意图；停留是可选的）[→](#段落节奏与变化sequence-tempo-and-variety)
- 连续性也要带上离场：每个刚离开的角色写一句**画外**说明（离场方向 + 最后状态），保证重新入画的方向合法 [→](#逐场提示词规则per-scene-prompt-law)
- **改一次处处生效**：前缀改一次，每条提示词都跟着变；**场景覆盖**允许某一场打破全局画面 [→](#改一次处处生效与场景覆盖edit-once-and-per-scene-override)
- 胜过普通分镜生成器的地方：**预检 lint**、**参考职责通道**、**Elements `@` 自动附加**、**失败模式意识**、**镜头复看与挑选** [→](#胜过普通生成器的地方what-makes-this-outclass-a-bare-generator)
- 提示词内容默认中文；继承用户要求的语言。英文旧骨架仍可选 [→](#流程workflow)
- 可选的 [历史校准附录](higgsfield-shotlist-director-historical-calibration.md)：长度、镜头时长和密度参考只是示例，永远不是时间配额

---

## 你要产出什么（What you produce）

一个 `shotlist.html`（保存到用户的输出目录并展示）。它是**自包含的**：内联 CSS、内联 JS、零外部依赖，用户离线打开也能用。结构：

1. **标题栏**：项目名（从说明推断；不清楚就写“Untitled”）。
2. **全局风格前缀**：顶部的可折叠块，作用于每条提示词。
3. **`@` 资产表**：演员/道具/场景声明一次。
4. **场景列表**：编号的场景，每场一个复选框（进度存在 `localStorage`），一行场景描述，以及一个或多个可直接复制的提示词块（`Prompt 3a · {{DURATION_3A}}s`，只在需要时有 `3b` 及后续）。标签显示生成时长；剪短使用时另行记录预定的剪辑用法。
5. 一段简短的“使用说明”（勾选自动保存；让助手修改）。

可折叠的风格前缀是文档唯一的可编辑来源。在每条连贯的提示词里，把全局规则编译**一次**，放进它们在块结构里的归属位置；各阶段只描述变化和继承的状态，不重复整个前缀。每个独立提交的生成块都带上它需要的最少的自包含风格、资产职责、空间锚点、进入状态和约束，这样复制时不需要再拼装，也不依赖一条拿不到的上一条提示词。用户要求旧格式时，完整的旧前缀可以在每个独立块里编译一次。不要再把它加到块结构提示词前面。

---

## 三层结构（The three layers）

### 1. 全局风格前缀（Global Style Prefix）

所有提示词继承的单一可编辑风格来源：改一次，重新编译所有受影响的块。它锁定影片的画面、光照、色彩、构图、表演语域、物理和音频惯例。每条规则编译进它相关的块一次；场景覆盖只替换它点名的字段。分辨率、帧率和其他平台设置单独列出，并按所选模型/模式核对；风格措辞不保证设置。

用 [`template-global-style-prefix.md`](template-global-style-prefix.md) 里可复用的填空块。**总是先看对话**：用户提供了前缀就保留在可编辑来源里，编译适用分句时保留原措辞。如果某个分句与已确认的要求或实际模型限制冲突，把冲突摆出来，而不是悄悄修改。否则按项目已确认的风格和块结构改写模板；它示例里的技术设置和音频惯例不是通用的平台要求。

### 2. `@` 资产表（`@`-asset glossary）

先加载 [项目资产总表](asset-registry.md) 下的共享项目总表。从它已有的条目推出这张资产表；绝不为新一批重建或重命名资产。在资产提示词、视频提示词和样本之间保持完全一致的调用名和显示名。每个片段的平台槽位绑定与项目调用名分开维护。下面的旧名字只示意语法；新的 S/C/B/P 命名遵循 SKILL.md，已有的项目名称优先。

每个反复出现的资产声明一次，给一个稳定的 `@` 名。在支持 **Elements** 的 Higgsfield 平台上，用**同一个名字**注册，粘贴时核实图像自动附加。否则映射到该平台支持的参考槽位。下面的名字是规划示例，不证明素材已上传或已绑定；把条目标为 planned / available / bound / verified，提交前替换或删除未解决的占位符：

```
@hero — main character          @boss — side character
@headphones — product           @sneakers · @bag · @skydancer — props
@kitchen · @stadium · @street — locations
@s_hero — athletic-look hero     @s_hero_wet — sweaty post-run hero
@music_track — beat reference; bind the actual file after model/mode format checks
@staging_street_v1 — front-on position reference, attached LAST
```

（工作室项目的调用名是 `@` + 纯中文名，如 `@林岚`；上面的英文名只示意语法。）

资产表里的位置图永远是**正面站位参考**（[站位参考模板](template-staging-reference.md)：轮廓人形，只表示位置，附在场景和角色参考之后）。俯视图是规划示意：它被转成正面参考或文字站位说明，自己从不被附上（[俯视平面图模板](template-top-down-map.md)）。它旁边不写槽位文件名：槽位按上传顺序分配。`[fix adopted from OSideMedia/higgsfield-ai-prompt-skill v3.38.0]`

**音频格式按模型、模式和上传平台核对。**[音频指南](higgsfield-audio.md#seedance-20) 里的 Seedance 2.0 通道记录的是只接受 MP3 的参考输入；旧的 `audio_1.wav` 示例不能暗示那里兼容 WAV。本地的 2.5 规格开放了音频参考职责，但没有列出接受的音频文件格式。绑定音频之前，核实那条通道实际的上传要求；缺少证据时把格式兼容性标为未核实。WAV 的后期母带或另一个音频模型支持 WAV，都不能证明视频参考输入的情况。需要转换时保留原母带，另做一个兼容副本；不要只凭文件名推断支持。

槽位→职责的纪律（`@Image1` = 角色，`@Image2` = 服装，`@Audio1` = 节奏……）来自 `higgsfield-seedance.md` § Reference Roles → Per-Image Role Convention。**之后需要状态变体时，给它自己一个锁定的总表条目**（例如 `@s_hero_wet`），链接到基础资产，并从基础图衍生。遵循 SKILL.md：基础资产阶段不批量做状态变体；普通的临时状态可以留在视频提示词里。

**每个资产表条目还带一个保真等级**：职责说明资产做什么工作，等级说明它有多少要进入画面：*完整保留* / *部分保留（点名部分）* / *属性迁移（点名迁移到的目标）* / *松散参考*。每行一个词就够了（`@headphones — product, full-preserve`）；等级和它们的提示写法在 `higgsfield-seedance-2-5.md` § Reference Roles → Fidelity。没有等级时，“用 @image4 做外套”悄悄地等于模型那天想保留什么就保留什么。

### 3. 带名字的逐场提示词（Named per-scene prompts）

每场编号（`1`、`2`、`3`……），在戏剧事件、因果转折、表演单元、换场、连续性交接或模型限制需要分开生成的地方，拆成带名字的提示词（`1a`、`1b`、`2a`）。每**场**一个复选框，即使一场需要几条连贯的提示词。没有设预算时，每个生成片段默认以所选模型的单次上限为目标（Seedance 2.5 为 30 秒），把相邻镜头合进一次接近上限的生成，时长、连续性、参考容量或生成可控性需要时再拆；没有固定的提示词数量，片段绝不靠注水或慢放凑满。每个镜头仍有观看目的和有动机的切点；镜头按连续性、复杂度和实际模型约束合并或拆分。

用 [共享叙事规划](narrative-planning.md) 区分**阶段**（一个戏剧事件或状态转变）、**镜头**（两次切镜之间连续的摄影机覆盖）和**生成片段**（一次模型输出）。一个镜头可以跨几个阶段；一个阶段可能需要几个镜头；模型支持时一个片段可以包含多个镜头。这些边界不必重合。

每个阶段按**进入状态 → 主要变化 → 可见反应 → 离开状态**规划，再选择镜头覆盖、映射到生成提示词。跨交接带上身份、位置、道具、情绪和环境变化。生成时长和剪辑里用到的部分分开：本地规格列出 **Seedance 2.5 为 4–30 秒**、**Seedance 2.0 为 4–15 秒**，受各模式规则和当前平台核实约束。两个范围都不定义场景模板。剪辑节拍更短时，生成一条合法片段再裁；场景更长时用连贯的多个片段。

---

## 出分镜表之前的导演关卡（Director gate before the shotlist）

在写行或复制块之前，执行唯一的 [导演决策流程](directorial-shot-design.md#导演决策流程)：场景变化与主次 → 观众的认知与体验 → 调度 → 比较停留、镜内交接与切镜 → 表演时长 → 删并与反向检查。把它的结论复用在已有的项目/分镜表备注里；不另加审批关卡，也不重复整张卡。

HTML 展示所选的主方案和重要取舍。每一行都由场景的核心/支撑/连接功能推出。反应近景或插入镜头只在它改变理解或压力时才用；允许有意义的停留，不需要持续的微动作。缺少细节时可以换一个角度、镜内转焦，或把动作写清楚。由导演来选；不要让用户逐镜指定。

## 逐场提示词规则（Per-scene prompt law）

默认复制块顺序是 **Higgsfield 块结构（[参考资产]→[角色]…[生成目标]→[具体情节]→[视觉风格]→[镜头]→[声音]→[保持一致]）**，HTML 里也一样。用链接的导演模板编译所选方案。`[具体情节]` 各段承载可见动作、景别、视场角、运镜、继承状态和结束状态；接触音效写在各段的 `声音：` 行，对白写在 `[声音]` 的计时行 `起s-止s｜说话人＋状态＋说：{line}`，画面里有人物时由定位行 `0s-1s｜<名字>轻声：{Hm.}` 开头。平台设置和导演推理留在复制文字之外。不另加单独的声音栏或结尾画面栏。

HTML 的资产表和风格前缀是可编辑的文档来源；把它们适用的内容在每条可独立复制的提示词里解析一次：

| 文档来源 | 块落点 |
|---|---|
| 真实的参考与职责 | 开头 `[参考资产]`：每个资产一行 `@名字 对应 名字。介绍/本段状态/参考用途：…`；后续块只补未交代信息；清理说明留在外面 |
| 本片段的主要事件和关键变化/结果 | `[生成目标]`：一个具体的句子；运镜/风格归各段或 `[视觉风格]` |
| 计时的动作、表演、空间、光、接触音效 | `[具体情节]` 各段；最后一段以静止的最终状态结束 |
| 对白与定位 hm | `[声音]` 的计时行 `起s-止s｜说话人＋状态＋说：{line}`，由 `0s-1s｜<名字>轻声：{Hm.}` 开头 |
| 稳定的身份、必要的连续性 | `[保持一致]`；平台设置留在外面 |

完整演出指的是可读的因果和交接，不是对每个小操作都给同等的细节强调。默认 NO BGM。跨片段的混音仍是后期工作，不代表一个复制块能控制前一段的音频。

只有用户要求旧格式或目标平台需要时，才把同样的内容编译成 **Style → Characters → Scene → CUT 1..N**，并加上连续性、结尾画面和约束字段。语言跟随用户，默认中文；骨架里的英文关键词不是只能用英文的模型要求。提交稿需要压缩时，在 HTML 里保留完整母稿；不要只因为用户要了 HTML 就附一份重复的长稿。

旧骨架（来自实地的示例，不是当前默认）：

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

每条提示词在确定戏剧单元之后才分配时长。**不默认以 15 秒为目标，也不为填满一个标准时长而注水。**用所选模型支持的时长范围，给一个节拍足够的时间，让它的动作、反应、揭晓或情绪停留读得出来。只要因果推进仍然清楚，一条提示词可以包含几个简单的切镜或阶段；新的事件、任务、地点、表演弧线或状态交接需要自己的生成时再拆。`3a/3b/3c` 这样的标签表示连贯的续接，不表示预设的时间或必须的份数。

**逐拍编舞，而不是“他在跳舞”。**泛泛的运动动词对 Seedance 没有意义：把动作拼出来：*“两下干脆的点头卡在节拍上，肩膀一边一边向后绕，膝盖轻轻一沉，随手一个响指，最后四分之一转身收住。”*（完整写法：`template-10-dance-music-performance.md`。）

**画外说明让重新入画保持合法。**默认格式里，把必要的离场状态写进最后一个 `[具体情节]` 段的 `→ 结束：` 行或 `[保持一致]`：上一条提示词里在、这一条不在的人，保留他的离场方向和最后可见状态，包括手里的道具、情绪、呼吸和动作相位。把这一句带进下一条提示词；连续缺席两条后可以从复制文字里拿掉，但在场景备注里保留这个状态，这样之后重新入画时仍有已知边界。旧骨架用同样的规则。只带画面内的状态，记录不了谁刚离开；对照这条记录检查重新入画的方向和手上状态。`[EMPIRICAL — third-party skill corpus; re-derived]`

**通过动作相位做匹配剪辑（在一次生成内，或用真实输入做受控续接）。**独立生成的片段，先按 [独立生成与同场切镜](narrative-planning.md#独立生成与同场切镜)；不要求匹配精确的结尾姿势。按 [动作同步与接缝去重](narrative-planning.md#动作同步接缝去重与整场节奏)：在接点继承同一个运动，然后继续它的下一个相位。已经完成的一次敲击、一发射击或一次到达，不在下一条片段里重来。生成的冗余部分可以重叠，但剪辑里的事件只发生一次；实际的剪辑点和声音接点在后期核实。

---

## 提示词密度：把剧本节拍归成叙事单元（Prompt density — grouping script beats into narrative units）

改编自标为 `[OFFICIAL — Higgsfield shotlist-builder + seedance-2-pro-director skills, 2026-07]` 的来源，服从当前共享规划：分镜表最难的判断，是决定哪些剧本节拍属于同一次生成。没有固定比例，也没有通用时长。先找出因果单元和它可见的状态转变；再选一个模型支持的时长，给这个单元足够的空间又不留空白。

**以下条件全部成立时，把剧本节拍归进同一条提示词：**

1. 画面里是同一组角色
2. 同一地点，或连续的空间关系
3. 一个连续的情绪和时间单元
4. 一个因果单元，它的动作、反应和结果在所选时长里能读清楚
5. 合起来的提示词保持在实际长度和模型限制以内

**合在一起会失去清晰度或超出模型限制时，在这些边界考虑分开；单独一个阶段或镜头边界并不要求新的生成：**

1. 换地点的硬切，或有意义的时间变化
2. 一个主要角色的进出场改变了调用名清单
3. 一次镜头或机位变化需要它自己的叙事功能
4. 一段表演弧线需要空间展开和收住；**不要把一次连续的情绪崩溃切碎**
5. 一个插入或切出镜头成了自己的信息事件
6. 一个新的任务、因果事件或状态交接开始

**每条提示词的复杂度预算**是诊断，不是时间规律：超过 2 个强动作、超过 2 个运镜、超过 3 个重要角色、超过 1 个复杂视效事件，或超过 1 次换场，通常说明这个因果单元应该拆开。按表演负荷和平台限制，给拆出来的提示词分配不等或相等的时长。复杂的打斗、追逐、变形、产品演示、对白交锋或安静的揭晓，各自得到它自己的事件需要的空间。

**拿不准时，保护剧情节拍。**事件简单而完整时缩短提示词；反应或揭晓需要空间时在模型限制内延长；到达平台限制时做一条连贯的续接。绝不为了达到常规时长而加切镜、特效或填充。

**说明太薄时用导演判断。**应用共享决策流程：找出场景的变化，选择一个可见行为和一个观众立场，然后比较停留、镜内交接和切镜。继承已确认的身份、剧情、时长、媒介和模式。常规缺失的制作细节可以不问就定，但不要把每场戏都默认成中景缓慢推近，也不要编造动机、道具和反转。在备注里简要说明主要选择，并编译成具体动作。会改变结果的剧情事实缺失时，保持条件性或退回上游；镜头偏好不需要审批。生成分组在剪辑方案之后按共享规划进行，绝不为凑到上限而注水。

可选的对照见 [历史校准附录](higgsfield-shotlist-director-historical-calibration.md)：来源的密度示例、时长阶梯、镜头类型范围和实地长度中位数。这些参考永远不决定阶段数、不强制插入镜头、不切碎情绪弧线，也不恢复 15 秒目标。

---

## 段落节奏与变化（Sequence tempo and variety）

`[EMPIRICAL — third-party director-skill evaluations 2026-08-09; re-derived heuristics, unmeasured here]`：两项整段检查，任何单条提示词规则都抓不到，交付前跑一次：

**节奏预算：算术关卡。**先确定故事的阶段、导演意图和镜头覆盖，再按动作、对白、反应、揭晓、空间阅读和情绪工作量分配镜头长度。不要从时长或等分时间推出切镜数。停留靠调度、关系、揭示信息、压力，或观众体验等待/失落来挣得时间；不一定需要可见的运动。主角停留是可选的，只持续节拍需要的长度；没有必须的“高光时刻”，也不预留 6–8 秒。

要求了总时长时，**最终剪辑时间线必须精确对上**。直切时，把保留的镜头时长相加；适用时计入转场重叠、被裁掉的冗余和任何变速。结尾画面或停留计入最后一个镜头。单独核对每次生成支持的时长：原始片段时长可以超过剪辑后的时长。故事装不下时，在保持因果清楚的前提下修改镜头覆盖或节奏；不要为了片段上限加填充。时间是要在剪辑里核实的计划，不是帧级精确生成的承诺。

**单调审计：读那一列，而不是读提示词。**写完后，只把每个镜头的构图 + 运镜那一行从上到下当作一列读。**连续三个镜头**景别*和*运镜都相同，是一个复查标记，不是禁令。保留有目的的重复、静止或视觉母题；每个镜头都读成“中景，缓慢推近”而没有叙事意图时，改变镜头的*功能和尺度*，而不是只为变化插入切镜。逐条复查完全看不到这种失败；只有把这一列当作段落来读时它才显现，而它正是生成出来的分镜表最常见的破绽。

---

## 改一次处处生效与场景覆盖（Edit-once and per-scene override）

像编辑一份连贯文档那样对待用户的修改，而不是 20 段零散的对话：

- **“改提示词 1a，做 X”** → 只改那一条。
- **“把风格前缀改成 Y，全部应用”** → 一次把改动传播到每条受影响提示词编译后的风格字段，保留明确的局部覆盖，除非用户也要求替换它们。
- **场景覆盖** → 一场戏可以打破全局画面。只替换那条提示词继承的光照字段（例如场景 2 体育场：*“明亮、真正晴朗的正午，强烈的正面阳光，深蓝的天，硬边阴影”*），其他每场保持柔和的全局光照。把覆盖存为局部字段替换；未受影响的字段仍继承之后的全局修改。在块结构里，它出现在相关段落或 `[视觉风格]`；在要求的旧格式块里，它出现在 Style。不要再追加一条相互冲突的光照指令。

修改时，**重新渲染同一个 HTML 文件并应用改动**，不要在对话里描述改动。尽量保留场景编号（不要为改一条提示词就全部重新编号），除非被要求，否则保留风格前缀。用户的勾选状态通过按场景编号存储的 `localStorage` 保留下来，所以编号稳定 = 进度不丢。

---

## 胜过普通生成器的地方（What makes this outclass a bare generator）

一个普通的“剧本 → 提示词”生成器停在文档上。本模块接进了仓库的其余部分，这才是重点：

1. **用实际的模型和模式预检每条提示词。**解析好继承的风格和覆盖之后，在包根目录对每个最终复制块运行。本地 CLI 支持 `--regime block`，从 [`model-specs.json`](model-specs.json) 解析模型；`--profile` 默认 `standard`，只有交付目标是双语 JSON 时才用 `--profile bilingual-json`。一个完整 30 秒、16:9、纯文字的 Seedance 2.5 提交的示例：

   ```bash
   python3 scripts/seedance_lint.py --preflight --regime block \
     --model seedance_2_5 --mode t2v --duration 30 --ar 16:9 \
     --file /path/to/prompt-1a.txt
   ```

   文件必须包含实际导出的复制文字。用每次生成自己的时长，而不是整段剪辑时长。参考生成选 `--mode omni_reference`；编辑选 `--mode video_edit` 并省略时长/画幅覆盖（它们跟随源视频）；延伸用 `--mode video_extension --extension-mode forward` 或 `backward`，配源视频画幅和合法的新增时长。选 2.0 时用它的真实 ID 和模式，例如 `--model seedance_2_0 --mode std`，配那条片段的合法时长。这些是 lint 设置，不是生成命令。

   `--regime block` 暂停短格式的词数上限。中文 1,800 字符的 `zh-overlength` 检查只在 `--profile bilingual-json` 下运行；工作室块结构稿默认 `standard`，不设字数上限。

   脚本检查过滤词、可识别的镜头/时间标记、对照本地规格声明的参数，以及支持的模式组合；在块结构稿上它还调用 `director_contract_lint.py` 的契约检查。它不验证绑定的素材、音频编码或生成的画面/声音。人工检查这些，并对整段剪辑跑 § Sequence tempo and variety。把过期规格和未解决的发现摆出来；快照有效不等于在线核实。把预检结果保留在分镜表备注里；静态检查不等于留下的镜头。对照预定的场景核实生成的画面和声音。
2. **参考职责通道。**保持已登记的项目调用名稳定，核实每个生成片段实际的槽位到文件映射。上传顺序会变；不能假设 `@Image1` 在所有提示词里都指向同一个角色。
3. **失败模式意识。**写作时就按 `higgsfield-seedance-engine-rules.md` 和 `higgsfield-seedance-failure-modes.md` 标出高风险镜头（倒影、同一角色的双胞胎、人群、复合运镜、进门几何），而不是让它们悄悄弄坏一场戏。
4. **对采用率诚实。**一场完成的戏可能需要很多次生成：保留候选，在运动中测试，锁定最好的那条。分镜表是计划；迭代仍然是这项技艺。
5. **音频作为驱动。**`@music_track` 锁定编舞时，在核对参考格式和职责之后，按 `higgsfield-audio.md` § Audio as a Conditioning Input 写节拍同步映射。选择了只用画内声音 / 后期配乐的流程时保留它；要原样输出上传音频时，用那个流程的时间码锚定，避免相互竞争的生成音频。单有节奏参考，并不承诺上传的音轨就是输出。

---

## 流程（Workflow）

1. **像导演一样读说明，而不是像速记员。**读上面链接的根入口/共享规范和完整模板；继承已确认的模型、时长、语言、资产和结局。只在适用处应用当前 2.5 / 16:9 / 中文的默认；未指定的时长从内容推出。找出每场戏在哪里转折、在哪里落地、在哪里呼吸。
2. **锁定风格前缀。**来自对话的定制前缀，或模板默认。
3. **建 `@` 资产表。**每个反复出现的资产一条；多状态变体各自有锁定的条目。
4. **导演这些场景。**用共享决策流程选择主次、信息顺序、调度和切/留取舍；删掉多余的覆盖，再把剪辑方案映射到支持的生成。项目 Clip 编号继承根入口的 批-序 编号；界面上的场景编号不必改名。跨生成边界保持表演的连续。
5. **写每条提示词**，默认用中文写成完整的块结构演出说明，继承用户的语言选择。编译进 HTML 复制块，带上解析好的风格和足够的独立上下文；用户要求旧骨架时用上面的映射。
6. **预检每条提示词**，用它的模型/模式；复查状态、时间、音频兼容性和高风险镜头，未解决的发现留着复查。
7. **生成 HTML**（骨架见下）并展示。
8. **修改时**，重新渲染文件并应用修改；保留编号。

---

## HTML 骨架（HTML skeleton）

自包含，深色导演室风格。全部内联。复选框状态保存在 `localStorage`；每条提示词有一个复制按钮。风格前缀在可折叠的来源块里随修改可编辑；每个 `<pre>` 包含解析好的块结构文字，其中适用的风格只出现一次。渲染器除了提示词，还填写资产表、设置、场景备注和预检结果；复制按钮只复制那一条提示词。插入的文字要做 HTML 转义，让参考标签、对白括号和内联的声音提示作为字面文字保留下来。默认 `lang="zh-CN"`，用户选择其他语言时修改。已有的 JavaScript 继续独立于提示词语法处理复制和场景进度。

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
    复制按钮复制该生成片段的完整提示词（块结构及已合并的风格与连续状态）。可按编号请求修订。</div>
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

`{{SCENES_HTML}}` 里的每个场景块（每场一个复选框，`data-scene` = 场景编号字符串）。提示词块只按需要重复；下面两个块示意一次续接，不是必须成对。交付前把每个时长占位符分别解析成支持的生成时长。保留的剪辑长度或入出点不同时，记在场景备注里：

```html
<div class="scene">
  <div class="scene-header">
    <input type="checkbox" data-scene="3">
    <div class="scene-num">3.</div>
    <div class="scene-desc">主角随节奏穿过厨房，周围声音逐渐淡去。</div>
  </div>
  <div class="prompt-block">
    <div class="prompt-label"><span>Prompt 3a · {{DURATION_3A}}s</span><button class="copy-btn">Copy</button></div>
    <pre class="prompt">[完整块结构提示词：[参考资产]→[角色]…[生成目标]、[具体情节]（按时间段，含 → 结束）、[视觉风格]…[保持一致]；已应用局部覆盖]</pre>
  </div>
  <div class="prompt-block">
    <div class="prompt-label"><span>Prompt 3b · {{DURATION_3B}}s</span><button class="copy-btn">Copy</button></div>
    <pre class="prompt">[场景3下一叙事单元或受模型上限影响的接续提示词：完整块结构、独立生成所需最小上下文、上一片段退出状态及本片段变化]</pre>
  </div>
</div>
```

---

## 相关模块（Related skills）

- [历史校准附录](higgsfield-shotlist-director-historical-calibration.md)：可选的来源表格和密度/镜头时长参考；没有固定的时间或数量配额
- `higgsfield-seedance-2-5`：当前默认模型的职责映射、模式流程和参数约束，从共享块结构演出说明编译
- `higgsfield-seedance`：2.0/Pro 的语法和旧骨架（六槽公式、Prompt-Craft Laws、Reference Roles、预检 lint、引擎与失败模式）
- `higgsfield-audio`：`@music_track` 节拍同步 + 只用画内声音的惯例
- `template-global-style-prefix.md`：可复用的前缀块 + 一个场景覆盖示例
