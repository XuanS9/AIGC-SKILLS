# Higgsfield Seedance 视效：素材变换（Higgsfield Seedance VFX — Footage Transformation）

**旧的 Seedance 2.0 通道。**当前工作室的视频工作默认用 Seedance 2.5 `omni_reference`，把已有片段作为限定职责的视频参考。本文件里的首/尾帧写法是历史平台说明，不是当前项目的要求或路线。如果用户明确选了别的模型，单独核实它的实际输入并按请求执行。

这个模块用于**编辑用户已有的片段**：保留真实的主体和真实的镜头运动，只改他们要求改的东西。它是 `higgsfield-seedance.md`（通用 Seedance 导演）的视频到视频兄弟模块。它**原样复用那个模块的语法**（六槽公式、提示词写作规律、预检 lint），再加上下面的变换层。不要和上层模块矛盾；镜头需要过滤安全、模式选择或引擎规则时，以它为准。

> **本文件是 Seedance 2.0 的视频到视频通道。**任务需要 **4K**、`mode=std` 或 `genre` 提示时，它仍是正确的选择。如果底片任务跑在 **Seedance 2.5** 上（最高 1080p、最长 30 秒、很多参考），通道是把片段作为视频参考附上的 `omni_reference`，它的制作方法（源素材 ≥ 4 秒、时长 = 源素材、四批规则、表演继承条款）在 `higgsfield-seedance-2-5-vfx-pipeline.md`。

> **这个模块是 `higgsfield-seedance.md` 之上的视频到视频层。**每一次视效变换仍然是一条 Seedance 提示词。这个模块只改变*起点*：一段真实的源片段，它的主体、表演和镜头运动必须在编辑后保留下来。`higgsfield-seedance` § Seedance 2.0 Prompt Modes / Transformation 覆盖*片内变形*（一个角色在一个镜头里可见地变成别的东西）；**这个**模块覆盖*保留型视效*：锁定真实底片，把特效叠进去。

## 速查（QUICK FACTS）
*路由辅助：实际规则读链接的章节。*
- 唯一的任务：**保留**让源素材可辨认的一切，只**改变**点名的元素；在结尾重复最脆弱的护栏（“face and identity unchanged”）[→](#核心思路保留然后只改一样东西the-core-idea-preserve-then-change-one-thing)
- 用 **Seedance 2.0、mode std、4K** 跑：脸、口型和细节在 4K 下保得住，在 1080p 下会变形（`fast` 做不了 4K）[→](#分辨率用-4k-跑resolution-run-it-in-4k)
- `@source` 把片段声明为底（不是风格参考）；只在某种真实质感总被做假时才加 `@creature`/`@element` [→](#提示词结构变换版prompt-anatomy-transform-variant)
- **三个难度级别**：L1 换掉世界 · L2 改画面里的一个元素 · L3 全程手持的电影镜头 [→](#三个级别three-levels)
- 两种模式：往底片里**加一个元素**，或者在保留的主体周围**替换环境** [→](#两种变换模式two-transformation-modes)
- **只匹配颜色看起来像贴上去的**：要匹配主光方向、反射光、光学/雾气、边缘/落地 [→](#光照融合成败在此lighting-integration-the-part-that-makes-or-breaks-it)
- 照片写实的生物需要**生物学准确**（有褶皱、有裂纹、不对称、哑光：绝不光滑/有光泽/像充气）+ 真实的接触阴影；参考图胜过描述 [→](#照片写实的生物--元素融合photoreal-creature--element-integration)
- 与台词同步的计时变焦：锚定**两次**：语义（`On the line "…"`）+ 数字（`At about Ts`）；见 `higgsfield-seedance-vfx-dialogue-timing.md` [→](#与台词同步的计时运镜timed-camera-moves-synced-to-dialogue)
- 加在前面的开场的预算：源表演的 `总长 − 开场 = 保留窗口`；每次改动都重算 [→](#时长纪律duration-discipline)
- 先生成一张变换后的画面开发静帧，作为场景/风格参考传入 [→](#首帧--起始帧流程first--start-frame-workflow)
- 输出是**纯文本英文**，提示词里不用 markdown，便于复制 [→](#输出格式output-format)

---

## 在源时间线上做叙事规划（Narrative planning on the source timeline）

起草任何一种变换模式或任何难度级别之前，应用 [共享叙事规划](narrative-planning.md)。先检查源素材，确定要求的特效的目标和最终状态，然后在源时间线上找到它的触发事件、原因、揭示和状态转换。这些决定阶段；之后才分配任何新特效的时间。绝不预选阶段数，也不平均切分底片。**阶段不是切镜或一段生成片段**：特效可以在一个保留的镜头里经过几个阶段发展，已有的源切点保持原来的时间。

从语义上规划全部八个导演层：**资产**（`@source`、可选的元素参考）；**目标**（限定范围的变换）；**全局视觉/声音/空间**（底片几何、光照、光学和音频）；**行为/节奏**（保留的表演和特效物理）；**阶段**（触发 → 变化 → 可见的反应 → 结果状态）；**连续性**（身份、道具、接触和累积的特效）；**最后一帧/接点**；**约束**（保留清单和允许的改动）。编译进已有的纯文本英文源声明、规格行、连续动作描述、锁定句和 SFX 行。不要加八个标题。

保留型编辑继承源素材的时间码、时长、切点、运镜轨迹和对白时间，明确要求的改动除外。特效阶段标注这些事件；它们不重新定时。要求的开场或延伸是另一种时间改动：保留明确的源时间到输出时间映射，保留源表演窗口，并遵循下面的时长算术。向后延伸从源素材结尾的姿势、运动相位/方向/速度、构图、光、道具和音频状态开始；向前/加在前面的延伸以源素材的**第一帧状态**结束，接点属性相同。只为新素材做预算。实际 4–15 秒的生成限制和 15 秒的输入限制仍然有效；合并后的输出放不下时，用分开的兼容片段。

## 核心思路：保留，然后只改一样东西（The core idea: preserve, then change one thing）

变换提示词有两个互相拉扯的任务：**锁定**让源素材可辨认的一切（人的身份、脸、服装、表演、构图、镜头和摄影机运动），以及只**改变**点名的元素。锁定写得不够，Seedance 会重抽脸或镜头，编辑就和原片对不上了。所以每条提示词都明确写出两半，并在动作结尾重复最脆弱的护栏：通常是 **“face and identity unchanged”**。

这就是整个蓝图：真实素材进去，出来完全相同的镜头（同样的主体、同样的运动），只应用了那一个要求的改动。

---

## 分辨率：用 4K 跑（Resolution: run it in 4K）

一律用 **Seedance 2.0、`mode=std`、4K** 跑。4K 很重要：脸、口型和细节在 4K 下保得住，在 1080p 下会变形崩坏：而素材变换的成败，就在于保留的脸读起来是不是*同一张*脸。`4k` 分辨率枚举经过模型核实（`model-specs.json` → `seedance_2_0`）；“细节在 4K 下保得住”的观察是**实践者的说法**，很可信但不是规格保证。

要遵守的模型约束（来自 `higgsfield-seedance.md` § Pre-flight Linter）：原生 4K **只在 `mode=std` 下**可用：`mode=fast`（Seedance 2.0 Fast）最高 480p/720p。所以 4K 素材变换必须用 std 模式，在标准的 Seedance 2.0 入口上跑。用户在 fast 模式下要 4K 时，生成之前先指出这个上限。

---

## 提示词结构（变换版）（Prompt anatomy (transform variant)）

### 1. `@source` 声明（The `@source` declaration）

源片段是底，不是风格参考。一行：

```
@source: Original <clip name> — <who/what is in it: subject, wardrobe, setting, action>. Preserve
<identity, face, wardrobe, performance, framing, camera and motion> exactly; <what to change —
e.g. enhance only the environment / add the creature on the tower / transform only the right arm>.
```

如果变换需要一种模型总在做假的真实质感（动物的毛、一张特定的脸），加一个**第二输入**作为质感参考并声明它：

```
@creature: Reference photo of a real <animal> — <fur / face / anatomy notes>. Appearance and
fur/skin texture reference only; ignore the photo's background and lighting, do not use it for the
environment.
```

用户提供自己对文件里有什么的描述：正确使用标签，不要编造片段里有什么。但对能打开的片段，写 `@source` 之前**先检查它**：读它的时长 / 帧率 / 画幅，抽几帧。按素材实际显示的内容（主体、服装、构图、运镜、时间、主光方向）构建 `@source` 和规格行的时长，而不是按用户的一句话概述。默认把规格时长设为探测到的时长。没有描述源片段时，写之前先问他们从什么素材开始。

> Seedance 把上传的视频读作一组帧，而不是看一段片子：所以帧的内容（主体、走路、光）就是它拥有的语境。和 `higgsfield-seedance.md` § Load-Bearing Rule 里“截图 → Claude”流程是同一个原理。

### 2. 规格行（Specs line）

一行紧凑的规格。永远包括匹配源素材的约束：

```
Photoreal. <aspect, default 16:9>. <duration — match the source clip>s. 4K. <look / grade>.
NON-IP — generic <creature/design>, not based on any brand or character. <SFX only | SFX and
source dialogue only>.
```

- **默认与源时长一致。**片段 6 秒，提示词就是 6 秒。如果回报需要更多空间（一个生物慢慢转向镜头），明确指出需要的时间改动；只在要求的范围和实际模型限制内延长。不要为了做出等长的阶段而重新定时保留的台词或动作。
- 每当加了生物、盔甲、载具或角色设计，**NON-IP 护栏**就放进规格行：通用的，绝不是品牌角色。让输出干净，而且往往比商标设计生成得更可靠。（和 `higgsfield-seedance.md` § The Rewrite Playbook / Brand · IP 的过滤逻辑相同。）
- **音频：**加特效用 `SFX only`；源对白轨必须保留时用 `SFX and source dialogue only`（例如与一句台词同步的变焦：见 `higgsfield-seedance-vfx-dialogue-timing.md`）。

### 3. 场景动作：一个连续镜头（Scene action — one continuous shot）

对单镜头的源素材，描述**连续的镜头运动**，而不是新的切镜。如果源素材已经有切点，保留它们的时间码，除非要求的编辑改变了它们。先写镜头/镜头焦段和“same framing as the source”，然后是保留的表演，然后是变换的事件驱动阶段，然后是要求的计时运镜。新的特效阶段不意味着切镜。以最后的可见状态和锁定句收尾。

### 4. SFX 行（SFX line）

以一句具体、有顺序的 SFX 说明结尾，完全按上层语法的要求。加特效时写行为：不是“fire”，而是“a soft whoomph as it catches, then a low steady flame roar and crackle, occasional ember pop.”每个音效（脚步、撞击、风、生物叫声、伺服电机声）都和可见的动作同步。

---

## 三个级别（Three levels）

这个流程的难度可以递增。每个级别的步骤都一样（检查片段、点名那一个改动、锁定其余），但镜头动得越厉害，特效就越难跟住：

- **级别 1：换掉你周围的世界。**主体完全按拍摄的样子保留；替换环境。慢/稳的运动最容易；开车镜头会提高门槛，因为新世界必须以正确的速度掠过，并一路重新照亮主体（§ Two transformation modes / B）。
- **级别 2：改画面里的一个元素。**加入或变形一样具体的东西：让一头头发着火、把一只手变成意想不到的东西、加一只爬楼的生物。底片保留；特效叠进去并被照进画面里（§ Two transformation modes / A）。
- **级别 3：全程手持的电影镜头。**摄影机在手里，全程在动（角度、视差和晃动都在变），特效（生物、环境、天气）必须跟上所有这些而不散架。这是最难的情况；逐帧保留手持运动，并在这里最大程度地依靠 § Photoreal creature / element integration 和 § Lighting integration。

固定机位的镜头很容易：画面几乎不变，模型只要把特效画进去。难度完全取决于镜头动得有多厉害。

---

## 两种变换模式（Two transformation modes）

### A. 往素材里加一个元素（Add an element to the footage）

让头着火、变换一只手、让一条肢体隐形、让一只生物蹲在地标上。保留整个底片；把特效叠进去。

- 描述特效**随时间的物理和行为**，而不只是它的存在：从哪里开始、怎么扩散、怎么运动、投出什么光。变形用有方向的“蔓延”（“starts at the tattoo, fine seams split one at a time and peel back, a servo seats, a cable plugs in, the next plate locks…”），火用先点燃再变大。
- 让特效**和底片互动**：火光在脸上闪烁并溢到车漆上；玻璃般的隐形手臂折射背景；巨型生物在它抓住的结构上投下真实的柔边接触阴影。（模型会自己把加进去的火的橙色光溢到皮肤、衬衫和车上：但点名互动能让它可靠。）
- 巨型生物**必须明确写尺度**，否则模型会按真实大小渲染。写“enormous, its massive body dwarfing the structure, clearly colossal relative to the mast.”
- 主体通常保持**毫不知情 / 毫不在意**，继续说话：这种反差就是笑点。写明它。

### B. 替换保留主体周围的环境（Replace the environment around a preserved subject）

保留人、他们的车、安全带、摄影机装置及其运动；换掉整个世界。

- 新世界必须带着与原运动一致的**视差掠过**。如果车在开，替换的世界必须给它一个可以开的路面，以及高速掠过的东西。在快速运动上，环境不能只是待在主体后面：它必须以正确的速度和主体一起动，并一路改变光照。
- 运动越大，**锁定清单越长**：不再只是脸：还有车、安全带、装置构图、整个开车的运动，全都保持住，只有环境在变。
- **温暖、有方向的日光世界**对脸/身份一致性比夜景或霓虹更安全：后者迫使主体全面重新打光，提高漂移风险。用户还是想要夜景/霓虹时，指出这个取舍，并把重新打光的指示写进去。（Seedance 会从生成的世界里取光，反射到主体身上：霓虹滑过车身、岩浆在下巴下面发光：不用要求；点名它能让它可靠。）

---

## 光照融合（成败在此）（Lighting integration (the part that makes or breaks it)）

先和用户确定分岔：它改变一切：

- **保留主体的光照，只给新元素调色。**锁定主体原来的光；按主体身上已有的主光给加入的生物/环境打光和调色，让它们融合。身份风险最低。
- **用一种画面重新照亮整个画面。**包括主体。用于统一的电影 / 商业调色。对脸的风险更高，所以在只改光照和调色时，明确锁定身份/表情/服装。

只匹配颜色**不足以**让保留的主体坐进一个新世界：这是最常见的“看起来像贴上去的”失败。把一个主体（或生物）融进底片时，用这个配方超越颜色：

- **光：**同样的主光方向（写出来：画面左或画面右）、同样的柔度、主体上同样的阴影密度和方向。（“Keep the sun as the key from screen-left exactly as before so the face and the light on it barely change.”）
- **环境反射光：**让世界溢到主体身上：上方冷的天光、阳光照亮的地面/植被反上来的暖光、形体相接处细微的环境光遮蔽。
- **光学与氛围：**匹配镜头特性和微对比度；在主体上加一点场景的大气雾和空气透视，让他们在朦胧背景前不会不自然地锐利；把景深、焦外衰减和胶片颗粒匹配到画面其余部分。
- **边缘与落地：**去掉硬抠的边缘、光晕和不匹配的轮廓光；用可信的纵深让主体落地，让他们占据同一个空间。

具体写出时间和主光方向（“soft, diffused midday daylight with the key coming from screen-right”）。“更柔”指更大、更散的光源：柔和的柔边阴影、低对比度、平滑的高光过渡、淡淡的雾。完整的电影照明词汇在 `vocab.md` § Lighting。

---

## 照片写实的生物 / 元素融合（Photoreal creature / element integration）

加入一只生物或硬表面元素、并且它必须读起来是真的时：

- 明确要求野生动物纪录片 / 实拍的真实感：“fully photoreal, real fur with depth and individual strands (or true scale detail / brushed metal), true anatomy, **never CG, plastic or cartoonish**.”（工作室中文稿写成正向：“完全照片写实，真实的毛发层次、真实的解剖结构”。）
- **生物学准确**是区分活物和廉价渲染的关键。写出真实的解剖细节（“pebbled scaly skin, long claws, heavy tail, true reptile anatomy”），并要求**不完美**：深深的褶皱、裂纹、下垂、**不对称**、沾满泥、哑光。避免光滑、有光泽或像充气的表面；真实的动物是不均匀的。让行为符合物种（树懒挪动缓慢沉重的重心；黑猩猩警觉、抽动；蛇的身体收紧、分叉的舌头探着空气：蛇不眨眼，所以爬行动物的回报镜头用不眨眼的凝视，而不是眨眼）。
- **把尺度做实。**用画面里的参照物（树、楼、剧组、主体）建立真实大小，用浅景深的**长焦镜头错觉**把巨型生物部分遮在前景元素后面：再加一点动态模糊和手持的柔软感，让它融入而不是飘着。
- 把它绑进底片：和主体同样的太阳方向和色温，在它接触的东西上有真实的柔边接触阴影，和远处背景同样的朦胧大气和纵深。
- 如果一条素材之后它看起来还是 CG，可靠的修法是**第二输入**：一张真实动物/材料的参考照片，声明为只取质感的参考（见上面的 `@creature`）。当你已经确切知道想要什么时，*展示*给模型比描述好；在 `higgsfield-gpt-image-2.md`（GPT Image 2）或 Nano Banana Pro 里生成参考，然后让提示词指向它。

---

## 与台词同步的计时运镜（Timed camera moves synced to dialogue）

落在一个节拍上的急推或平滑推近是反复出现的回报。**同时用两种方式**锚定它，让它在 Seedance 内部计时漂移时也能落下：一个语义提示和一个数字提示。完整的测量步骤（怎么从源音频读出 `T`、怎么换算时间码）在 **`higgsfield-seedance-vfx-dialogue-timing.md`**。

- 语义：`On the line "<exact words>," the camera <snaps into a hard crash zoom | begins a smooth, steady push-in> …`。规格行需要 `SFX and source dialogue only`，让对白轨保留下来。
- 数字：`At about <T> seconds … the camera …`。从源音频得到 `T`（或者一个可见的动作节拍：“at about 2.2s, on his finger snap”）。
- **急推（crash zoom）** = 快速猛烈的推入；**平滑推近（smooth push-in）** = 缓慢稳定的滑行，不猛。按用户的用词来。
- 如果一个地标或主体必须在运动**全程**保持可见，明确写出来（“the tower stays in frame throughout, never cropped”）。
- 触发之后留足尾巴让回报展开（一个生物慢慢转向镜头需要约 2–3 秒）。片段短的话，在台词的第一个词上触发变焦，而不是在台词之后。

### 揭示后拉（向外的运动）（Reveal pull-back (the outward move)）

推近的镜像：开场紧贴单独的*新增*元素（生物/特效的长焦压缩构图，主体在画外），然后向外运动，落到真实底片上。两种风格，按用户的用词来：

- **硬 / 猛的拉远** = 快速向外猛拉，突然。
- **平滑后拉** = 缓慢稳定的展开，不猛。

用和计时变焦同样的两种方式锚定落点，并要求落点处**与源构图 100% 一致**：写出匹配的属性（同样的角度、头顶空间、地平线、镜头特性），否则模型会落到一个差一点的构图上，再也接不上原片。落点之后交接给保留的镜头，并保持源素材自己的运镜继续。

### 保留对已知台词的口型同步（Preserving lip-sync to a known line）

回报是主体的嘴对上一句特定的台词时，**一字不改**地引用它并锚定两次：一次在动作里（“…lips matching the source exactly, saying clearly: '<line>'…”），一次在 SFX/对白行里。规格行要求 `SFX and source dialogue only`，让对白轨保留下来，并把“lips matching the source exactly”加进锁定句。然后对照保留下来的对白窗口检查台词（见 § Duration discipline / Prepended-intro budget）：一句约 6 秒的台词放不进 5 秒的尾巴。放不下的话，交付之前先解决时长；不要交出一条没法对口型的提示词。对白 + `[AUDIO: Xs]` 的机制在 `higgsfield-audio.md`。

---

## 时长纪律（Duration discipline）

默认采用源片段的精确时长和事件时间码。用户改变时长时，从源时间到输出时间的映射**重算**数字化的变焦时间，并告诉他们新的标记；不要按比例拉伸源对白。转场和最后一帧的停留都算进预算。长时间停在一只静止的生物上时，加上适当的小“活着”的微动作（一次缓慢的眨眼、下颌移动、平稳的呼吸），让它不显得冻住。

### 加在前面的开场的预算：开场 + 剩余 = 总长（Prepended-intro budget: intro + remaining = total）

当你在必须保留的素材前面加一个节拍（一次揭示、一个长焦停留、一个建立性的生物镜头）时，保留的镜头不会变长：它会被*往后推*。每次都写出算术，并标出被截掉的部分：

`总时长 − 开场长度 = 源表演的保留窗口`

如果源镜头比保留窗口长，它的一部分就播不出来。明确说出来，并按保真度从高到低给出三种解决办法：

1. **延长总长**，让完整的源素材放得下（开场 + 完整源素材）。保真度最高，片子最长；超过模型单次生成的限制时，单独生成开场，在源素材的第一帧状态处把它和保留的源素材接起来。
2. **让源素材更早开始**：牺牲片段自己安静的开头，让对白仍然落在窗口里。总长不变，台词保留，损失预备段。
3. **接受截断**：源素材的前 N 秒不会出现。只有被丢掉的开头没有对白时才安全。

这些是明确的时间编辑选项，不是对保留型编辑的自动改动。完整源素材前加开场时，源时间 `t` 映射到输出时间 `开场 + t`；如果要求裁剪，写明保留的确切源区间和它的偏移。没先做这个减法，绝不同时承诺“100% 口型同步”和固定总长下的前置开场。两个数字中任何一个改变时，都重算并重新标出。

---

## 首帧 / 起始帧流程（First / start-frame workflow）

花视频额度之前，常常值得先把**变换后的开场静帧**作为图像生成出来，锁定画面，再从它开始做动画。在本工作室里，这张静帧是 `omni_reference` 里的场景/风格参考，绝不是必须的开场画面；历史流程（模型、设置、输入、上传机制，以及怎么把静帧作为 `start_image` 交回给 Seedance）只适用于明确选择 2.0 的任务。这与 `higgsfield-seedance.md` § Drafts Validate the Prompt 配套：钉住画面，而不是抽签。

---

## 迭代（Iterating）

用户迭代得快、步子小（“光柔一点”“从右边来”“山更大、雪更多”“把黑猩猩弄得巨大”“变焦前停一拍”“保持原时长”）。**只改点名的东西**，提示词其余部分保持稳定：重抽整条提示词会丢掉已经有效的部分。精修一张生成的静帧时，编辑选中的结果（把它作为底传回去），只修不对的地方，而不是从头开始。这是 `higgsfield-prompt.md` § The Iteration Rule 在素材变换上的情况。

---

## 输出格式（Output format）

**先输出英文**，纯文本：提示词里不加粗、不加标题、不加列表，不放在代码块里。方便原样复制。只有要求时才给中文翻译，放在英文之后，格式相同。（这是 2.0 原生英文格式；工作室当前交付用中文块结构。）

每条提示词上方一个简短标签（例如 `Hook_2 · Variant 1 — Through the clouds`）没问题，交付多个变体时有帮助；提示词正文本身保持纯文本。

把共享规划编译进这个原生骨架；阶段留在动作描述里，不需要新的标题、切镜或生成调用。保留源时间线，并在收尾锁定之前写明最终的特效状态。

骨架：

```
@source: ...
@creature: ...            (only if a texture reference is used)

Photoreal. 16:9. <N>s. 4K. <look/grade>. NON-IP — generic <X>. SFX [and source dialogue] only.

<Continuous shot, same framing as source. Preserved performance. The transformation, with physics
and plate interaction. Any timed camera move with semantic + numeric anchor. Lock-down clause: face
and identity unchanged; everything else identical to the source.>

SFX [and source dialogue] only: <specific, ordered sounds>.
```

## 语气（匹配用户）（Voice (match the user)）

简洁、有动感；物理上精确（确切的材料、行为、尺度）；导演思维（镜头、角度、运动）；不泛泛（不用“beautiful / stunning / amazing”，改用质感词）；情绪克制。不夸大、不软化、不解释东西“代表”什么。和 `higgsfield-seedance.md` § Voice Rewrite 同样的反套话纪律。

## Seedance 2.0 输入限制（参考）（Seedance 2.0 input limits (reference)）

图像 ≤ 9；视频 ≤ 3 个，合计 ≤ 15 秒；音频 ≤ 3 个 MP3，合计 ≤ 15 秒；混合输入合计 ≤ 12；生成时长 4–15 秒。一段源片段加一张质感参考照片轻松放得下。如果请求需要的输入超过允许的数量，指出来并说明优先放什么。（已对照 `model-specs.json` → `seedance_2_0` 核实：`media_roles` 包括 `video`、`image`、`audio`、`start_image`、`end_image`；`4k` 在 `mode=std` 下是合法分辨率。）

## 要内化的结构模式（只作风格参考，不要照搬）（Structure patterns to internalize (style reference only — do not reproduce)）

- **加元素：**`@source (preserve all, add effect)` → `specs + 4K + NON-IP + SFX only` → `continuous shot, preserved performance, effect igniting/creeping with plate interaction, subject unfazed` → `lock-down clause` → `SFX`。
- **换环境：**`@source (preserve subject + vehicle + rig + motion, replace world)` → `specs + 4K + grade for the new world` → `continuous shot from the same rig, new world streaming past with parallax, relight to match or relight-all` → `lock-down` → `SFX`。
- **地标上的生物加计时变焦：**`@source` + `@creature (texture ref)` → `specs + 4K + NON-IP + SFX and source dialogue only` → `continuous locked shot, giant photoreal creature integrated on the landmark, subject delivering to camera` → `at ~T / on the line "…", smooth push-in keeping the landmark in frame, creature turns to camera` → `lock-down` → `SFX and dialogue`。
- **加在前面的揭示开场（变换 + 向外运动 + 保留的表演）：**`@source (preserve subject + performance + lip-sync + framing, add element, prepend a telephoto intro)` + `@creature (texture ref)` → `specs + 4K + NON-IP + SFX and source dialogue only` → `open tight/telephoto on the added element in isolation for the intro beat, hard or smooth zoom-out at ~T landing on a 100% match of the source composition, then the preserved take plays with exact lip-sync to the quoted line while the added element continues behind` → `budget check (intro + remaining = total)` → `lock-down` → `SFX and dialogue`。

可直接填写的骨架和示例变体在 `template-footage-vfx-transform.md`。

---

## 相关模块（Related Skills）

- `higgsfield-seedance.md`：上层 Seedance 导演：六槽公式、提示词写作规律、引擎规则、内容过滤预检 lint，以及片内变形提示词模式
- `higgsfield-audio.md`：音频作为条件输入、`[AUDIO: Xs]` 对白/音效、口型同步（计时变焦对台词和保留源对白的情况）
- `higgsfield-camera.md`：视频参考、Load-Bearing Rule、运镜词汇（保留手持 + 你从没拍过的运动）
- `higgsfield-gpt-image-2.md`：生成生物/质感参考图和变换后的起始画面
- `higgsfield-facs.md`：保留对白的变换还需要精确表情时，肌肉级的面部控制
- `higgsfield-seedance-vfx-dialogue-timing.md`：本模块依赖的计时步骤
