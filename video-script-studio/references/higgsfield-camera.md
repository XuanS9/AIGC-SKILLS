# Higgsfield 运镜控制（Higgsfield Camera Controls）

使用平台支持的运镜预设时，写出它的**准确预设名**。自由描述的运镜不需要预设。无论哪种，都要写明视点、跟随的主体、运动路径和结尾构图。

按 [共享叙事规划](narrative-planning.md) 规划镜头覆盖，它决定完整演出格式，并优先于本地的创作默认：**阶段**是一个戏剧事件或状态转变，**镜头**是两次切镜之间连续的摄影机覆盖，**生成片段**是一次模型输出。一个镜头可以跨几个阶段；一个阶段可能需要几个镜头；支持多镜头的片段可以包含几个镜头。从观众必须看到和感受到的东西出发选择切点和时长，再让镜头覆盖适配模型的生成限制。新阶段不自动要求切镜或新片段。

工作室格式里，运镜写在 `[具体情节]` 段头的简称和各段的 `运镜：` 行（方式＋角度＋起止景别＋距离或时长＋跟谁）；视场角只用锚点度数。下表的英文预设名是平台标识，照原样写；`Prompt phrase` 一列是英文原版示例。

## 速查（QUICK FACTS）
*路由辅助：实际规则见链接章节。*
- 按类别的具名预设表：推轨 / 升降 / 环绕 / 变焦 / 跟随 / 特殊 / 时间 / 穿越物体 / 载具，加上角度和景别；**使用平台预设时写准确的预设名** [→](#推轨运动dolly-movements)
- 相容的运动组合，以及固定摇和滑行的选择，都是镜头覆盖的选项；先后进行的组合要写明时间 [→](#组合运镜控制combining-camera-controls)
- **情绪同步是可选的运镜策略**：7 个语域提供示例；由观看需要和用户指令决定镜头覆盖 [→](#镜头与情绪同步按焦点角色的情绪运动camera-emotion-sync--movement-per-focal-character-emotion)
- [OFFICIAL] 按镜头*目的*选镜头和光圈（85/100mm F1.4 紧凑情绪近景 …… 45mm 微距 F2.8），并配上常用的锁焦和禁止畸变的句子 [→](#按镜头目的选镜头与光圈lens--aperture-by-shot-purpose)
- 按类型的镜头时长：[OFFICIAL] 来源的可选节奏示例，不是配额，也不是生成限制；动作、对白和情绪的可读性决定长度 [→](#按类型的镜头时长shot-duration-by-type)
- 微运动需要精确距离：写明总行程加时间（“7 秒内只移 10–15 厘米”）；物理移动绝不写 `zoom` [→](#微运动需要精确距离micro-moves-need-exact-distances)
- Seedance：单一运动规则、按题材的预设、可靠措辞库、通过 `@Video` 迁移运镜 [→](#seedance-运镜最佳实践seedance-camera-best-practices)
- `@Video` 参考能可靠读取什么（世界、材质、物理、镜头性格），做不到什么（逐帧精确续接、身份）[→](#视频参考能读什么不能读什么video-reference--what-it-reads-and-what-it-cant)

---

## 推轨运动（Dolly Movements）

| 控制 | 作用 | 适合 | 提示示例 |
|---------|-------------|----------|---------------|
| **Dolly In** | 平滑地直线靠近主体 | 亲密、揭示、累积紧张 | "Camera Dolly In toward her face" |
| **Dolly Out** | 平滑地直线远离主体 | 孤立、离开、展开语境 | "Camera Dolly Out revealing the empty square" |
| **Dolly Left** | 向左横移跟拍 | 跟随水平运动、揭示场景 | "Camera Dolly Left tracking alongside the runner" |
| **Dolly Right** | 向右横移跟拍 | 跟随水平运动、揭示场景 | "Camera Dolly Right as the car accelerates" |
| **Dolly Zoom In** | 向前推轨同时拉远焦距 | 眩晕、震惊、顿悟（希区柯克效果） | "Dolly Zoom In — subject stays size as background rushes away" |
| **Dolly Zoom Out** | 向后推轨同时推近焦距 | 被压垮、孤立、世界收拢 | "Dolly Zoom Out — city swallows the figure" |
| **Super Dolly In** | 夸张地快速冲向主体 | 突然的震惊、紧急的揭示 | "Super Dolly In on the handprint on the window" |
| **Super Dolly Out** | 夸张地快速后拉 | 戏剧性的尺度揭示、语境突变 | "Super Dolly Out to reveal the entire burning city" |

---

## 升降运动（Crane / Vertical Movements）

| 控制 | 作用 | 适合 | 提示示例 |
|---------|-------------|----------|---------------|
| **Crane Up** | 摄影机从地面/主体高度向上升 | 揭示范围，从亲密过渡到宏大 | "Crane Up from the soldier's hands to the war-torn landscape" |
| **Crane Down** | 摄影机从高处下降 | 从上方介绍地点，落到个人 | "Crane Down from the skyline to the lone figure on the street" |
| **Crane Over The Head** | 正上方的上帝视角 | 脆弱、监视、编舞 | "Crane Over The Head — top-down view of the crowd" |
| **Levitation** | 平滑向上漂浮，像梦 | 神秘、超越、灵魂出窍 | "Camera Levitates from her feet to her serene face" |

---

## 环绕运动（Orbit / Arc Movements）

| 控制 | 作用 | 适合 | 提示示例 |
|---------|-------------|----------|---------------|
| **360 Orbit** | 绕主体一整圈 | 情感孤立、戏剧强调 | "360 Orbit around the boxer in the ring" |
| **Arc** | 绕主体半圈扫过 | 揭示、情感转折点 | "Camera Arcs slowly around the two detectives" |
| **Lazy Susan** | 慢速转盘式旋转，主体居中 | 产品镜头、人物登场、服装展示 | "Lazy Susan around the antique watch on the table" |
| **Robo Arm** | 精密的机械弧线，复杂路径 | 编排好的场景、产品揭示 | "Robo Arm sweeps from headlights over the roof of the car" |

---

## 变焦效果（Zoom Effects）

| 控制 | 作用 | 适合 | 提示示例 |
|---------|-------------|----------|---------------|
| **Crash Zoom In** | 突然快速推近主体 | 震惊、顿悟、强调一个细节 | "Crash Zoom In on the bloody handprint" |
| **Crash Zoom Out** | 突然快速拉远 | 断开、突然更宽的语境 | "Crash Zoom Out revealing the battlefield" |

---

## 跟随 / 动作运动（Follow / Action Movements）

| 控制 | 作用 | 适合 | 提示示例 |
|---------|-------------|----------|---------------|
| **FPV Drone** | 像无人机一样快速灵活地穿梭 | 追逐段落、空中动作、动能 | "FPV Drone chasing the motorcycle through the warehouse" |
| **Action Run** | 低机位跟在奔跑的主体身后 | 追逐、逃跑、追捕 | "Action Run — camera low behind him, matching his sprint" |
| **Handheld** | 有机的手持晃动感 | 纪实真实、亲密、混乱 | "Handheld camera jostling with the crowd" |
| **Head Tracking** | 摄影机锁定角色头部运动 | 第一人称的强度、迷失方向 | "Head Tracking as the boxer staggers after the punch" |
| **Snorricam** | 摄影机装在演员身上，背景晃动 | 压力、醉酒、强烈情绪 | "Snorricam locked on her face as the room spins" |

---

## 特殊 / 电影感（Specialty / Cinematic）

| 控制 | 作用 | 适合 | 提示示例 |
|---------|-------------|----------|---------------|
| **Bullet Time** | 主体定格/慢动作，摄影机绕行 | 动作高潮、冲击瞬间 | "Bullet Time around the leaping assassin" |
| **Dutch Angle** | 摄影机斜着倾斜 | 心理紧张、不稳定、恐惧 | "Dutch Angle as the conspirators whisper" |
| **Fisheye** | 广角畸变，弯曲透视 | 超现实、滑板、实验 | "Fisheye lens capturing the skateboarder's trick" |
| **Whip Pan** | 快速横向模糊摇镜 | 动态转场、跟随快速动作 | "Whip Pan from the thief to the officer" |
| **Overhead** | 正上方鸟瞰 | 编舞、空间关系、脆弱 | "Overhead shot of the dancers forming patterns" |

---

## 时间类（Time-Based）

| 控制 | 作用 | 适合 | 提示示例 |
|---------|-------------|----------|---------------|
| **Hyperlapse** | 移动摄影机加延时 | 城市变化、旅行段落 | "Hyperlapse down the boulevard from dawn to dusk" |
| **Timelapse Human** | 固定摄影机，人的活动快进 | 日常、城市脉搏 | "Timelapse Human — subway platform, people rushing" |
| **Timelapse Landscape** | 固定摄影机，自然/风景随时间变化 | 天气变化、四季、日出日落 | "Timelapse Landscape — mountain valley sunrise to dusk" |
| **Low Shutter** | 慢快门，快速运动产生拖影 | 速度、紧迫、迷醉 | "Low Shutter on the spinning dancer — silhouette blurs" |

---

## 穿越物体（Through-Object）

| 控制 | 作用 | 适合 | 提示示例 |
|---------|-------------|----------|---------------|
| **Through Object In** | 摄影机穿过一个窄物体进入新空间 | 揭示秘密、创意转场 | "Camera glides Through Object In — through the keyhole into the dusty study" |
| **Through Object Out** | 摄影机从窄处穿出，揭示外部 | 从封闭到开阔的转场 | "Through Object Out — pulls back through the cabin window into the blizzard" |
| **Mouth In** | 摄影机推进角色张开的嘴里 | 超现实转场、进入回忆/梦境 | "Mouth In transition — camera enters the storyteller's mouth into the fantasy world" |

---

## 载具 / 动作特殊（Specialty Vehicle / Action）

| 控制 | 作用 | 适合 | 提示示例 |
|---------|-------------|----------|---------------|
| **Car Chasing** | 低机位贴地跟随高速车辆 | 高速追逐 | "Car Chasing — camera hugs the side of the black car through the streets" |
| **Car Grip** | 摄影机装在车上，随车移动 | 沉浸式载具段落 | "Car Grip — fixed to the hood, shaking on every bump" |
| **Buckle Up** | 剧烈颠簸的晃动 | 颠簸、湍流、失控 | "Buckle Up as the car skids around the corner" |

---

## 俯仰与视角：机位角度（Pitch & Perspective — Camera Angles）

| 控制 | 作用 | 适合 | 提示示例 |
|---------|-------------|----------|---------------|
| **Low Angle** | 仰拍主体 | 权力、主导、英雄感 | "Low angle looking up at the general on horseback" |
| **High Angle** | 俯拍主体 | 脆弱、渺小、暴露 | "High angle looking down at the lone figure in the empty hall" |
| **Eye Level** | 中性高度，对话感 | 对白、纪实、落地的场景 | "Eye level, two characters facing each other" |
| **Bird's-Eye View** | 正上方垂直向下 | 地图、编舞、上帝视角 | "Bird's-eye view of the marketplace from above" |
| **Worm's-Eye View** | 极低机位，垂直向上 | 高耸的尺度、超现实、异世界 | "Worm's-eye view looking up through the forest canopy" |
| **Ground Level** | 摄影机贴在地面上 | 与地形亲近、小主体、冲击 | "Ground level — ants marching across cracked earth" |
| **Canted Angle Left** | 地平线倾斜，向左偏（荷兰角） | 不安、紧张、心理扭曲 | "Canted angle left as the hallway stretches ahead" |
| **Canted Angle Right** | 地平线倾斜，向右偏（荷兰角） | 不安、紧张、心理扭曲 | "Canted angle right — the interrogation room feels wrong" |
| **Static Oblique** | 斜角透视，偏轴构图 | 风格化构图、不安、视觉趣味 | "Static oblique angle on the staircase" |
| **Over-the-Shoulder (OTS)** | 摄影机在一个人肩后，对着另一个人 | 对话构图、正反打 | "OTS from behind the detective, facing the suspect" |
| **POV / First Person** | 摄影机**就是**角色的眼睛 | 沉浸、恐怖、主观体验 | "POV — hands push open the heavy wooden door" |
| **Two-Shot** | 两个主体同框 | 关系、对峙、对白 | "Two-shot of the couple walking along the pier" |
| **Cowboy Shot** | 大腿中部以上 | 西部对峙、角色气场、随时动手 | "Cowboy shot — hands hovering near the holster" |

---

## 景别（Shot Sizes）

| 控制 | 作用 | 适合 | 提示示例 |
|---------|-------------|----------|---------------|
| **Extreme Long Shot (ELS)** | 辽阔风景，主体很小或不在 | 建立地点、孤立、史诗尺度 | "Extreme long shot — lone figure crossing the salt flat" |
| **Long Shot / Wide Shot (LS/WS)** | 全身可见加周围环境 | 在环境里建立角色、动作戏 | "Wide shot of the dancer on the empty stage" |
| **Medium Long Shot / Cowboy (MLS)** | 大腿中部以上 | 角色姿态、西部对峙、群体关系 | "Medium long shot — the three outlaws face the sheriff" |
| **Medium Shot (MS)** | 腰部以上 | 对白、采访、一般叙事 | "Medium shot — she leans against the bar, arms crossed" |
| **Medium Close-Up (MCU)** | 胸部以上 | 情感对话、反应镜头 | "Medium close-up as he reads the letter aloud" |
| **Close-Up (CU)** | 脸占满画面 | 原始情绪、强度、亲密 | "Close-up on her face — tears welling, jaw tight" |
| **Extreme Close-Up (ECU)** | 单一部位（眼、手、嘴） | 紧张、细节、心理强度 | "Extreme close-up on the twitching eye" |
| **Insert Shot** | 物件或动作的细节 | 剧情细节、时间压力、质感 | "Insert shot — the clock hand ticking past midnight" |

---

## 组合运镜控制（Combining Camera Controls）

叠加两个相容的运动能得到更丰富的镜头：

| 组合 | 效果 | 例子 |
|-------------|--------|---------|
| Dolly In + Dutch Angle | 收紧的紧张 + 不稳定 | 反派揭示 |
| Crane Up + 360 Orbit | 史诗的尺度揭示 + 孤立 | 最终战结尾 |
| FPV Drone + Crash Zoom In | 动能 + 突然聚焦 | 追逐高潮 |
| Handheld + Action Run | 粗粝真实 + 追捕紧迫 | 逃跑段落 |

**避免同时进行相互冲突的运动：**不要在同一瞬间同时要求 Dolly In 和 Dolly Out，或 Crane Up 和 Crane Down。一个连续镜头可以在一个有动机的事件处反向运动，前提是写明路径和终点。

**先后进行与同时进行的组合。**上表列的是*同时*组合（两个运动同时发生）。制作实践还用*先后*组合：第一阶段摇镜跟随角色，角色停下时推近到脸上。在提示词里写明顺序和时间（`Camera pans left from 0-3s tracking the character, holds, then pushes in on the face from 4-8s`），让模型把运动渲染成分开的阶段，而不是糊成一个含糊的运动。

**固定摇与滑行。***摇*的摄影机从固定位置旋转；*滑行*的摄影机在空间中平移。制作实践在大多数覆盖里更偏好固定摇而不是滑行：固定摇读起来是一个选定的视点、有引导的注意；滑行读起来是没有着落的。写清你指的是哪一个：`the camera stays in position and pans to follow him` 与 `the camera glides alongside him as he walks` 不同。

> **约束：**与运镜有关的时间/一致性瑕疵（矛盾的运动、运镜不起作用、静止的 I2V）及其预防措辞，见 `negative-constraints.md` 的 Temporal/Consistency Artifacts 部分。

---

## 镜头与情绪同步：按焦点角色的情绪运动（Camera-Emotion Sync — Movement per Focal Character Emotion）

在服务场景时，摄影机可以充当焦点角色的情绪替身。这是一个可选策略：按用户指令、视点、空间可读性和事件来选择运动、镜头和时长。刻意的情感距离、对比，或在情绪变化中保持镜头不动，都成立。

七个语域提供可选示例；时间和拍摄设置不是通用的：

| 焦点角色的情绪 | 运镜处方 |
|---|---|
| 愤怒 / 暴怒 / 紧张 / 绷着 | 呼吸感手持，抖动而不稳：断续的呼吸节奏，两个轴上都有可见的微抽动，幅度小，节奏不规则。避免稳定器。 |
| 平静 / 掌控 / 自信 | 呼吸感手持，平稳：稳定的呼吸频率，规则的微幅度。稳定器用得很轻，但仍是活的。 |
| 悲伤 / 脆弱 | 手持，慢，低：更低的呼吸频率，摄影机微微向下漂，操作者的分量感觉更重。 |
| 震惊 / 揭示 | 可选的固定停留 + 缓慢推近或后拉；0.5–2 秒的停顿是一个例子，时长由实际的揭示和反应决定。 |
| 动作 | 支持时可选 60fps / 180° 快门以得到干净的运动；按预定的画面和实际平台选择帧率和拖影。支持的设置与文字分开写。 |
| 最后一拍 / 定论 | 可选的顶拍定格：正上方，时间停止，所有位置锁定。0.3–0.5 秒的标点是一个例子；按结尾选择构图和长度。 |
| 情绪崩溃 / 角色需要空间 | 从中景/近景缓慢后拉到远景：“把角色留给他自己”。制作团队为情感时刻（角色抽泣、蜷缩，或者需要被看见但不被逼迫）命名的技法；拉开摄影机给观众视觉距离，读起来是情感空间而不是抛弃。 |

### 一个镜头内的情绪弧线（Emotional arcs within a single shot）

当焦点角色的情绪在一个连续镜头里*变化*时（例如一个镜头里从暴怒到克制），如果选择了情绪同步，摄影机可以随之变化。把这个选项写成具名的阶段：

- 开场阶段：按进入时的情绪给出运镜处方
- 过渡阶段：描述镜头性格怎么转变（手持幅度减小、漂移停下、推近放慢）
- 收尾阶段：按离开时的情绪给出运镜处方

把任何选择的运镜变化绑定到一个可见事件上；稳定的视点也可以撑住这段弧线。

> **用情绪同步时，先理清情绪，再选镜头。**上面七个情绪语域按*具名*情绪追踪（愤怒、平静、悲伤、震惊）。用户给出泛泛的情绪（“惊讶”“紧张”）时，第一步是把它拆成一个具体的具名语域：“是哪一种 X？”澄清模板见 `higgsfield-prompt.md` § Generic-Emotion Decomposition。

### 按镜头目的选镜头与光圈（Lens + aperture by shot purpose）

`[OFFICIAL — Higgsfield shotlist-builder skill, 2026-07; re-authored from the Chinese source]`：从镜头的*目的*出发选镜头，然后在提示词里同时写出焦段和光圈：

| 目的 | 镜头 | 光圈 |
|---|---|---|
| 极紧的情绪近景（额头到下巴占满画面） | 85mm 或 100mm（视场角 29° 或 18°） | F1.4 |
| 中景对白、双人镜头 | 50mm（视场角 47°） | F2.0–F2.8 |
| 远景 / 建立镜头 | 35mm（视场角 63°） | F4–F5.6 |
| 插入 / 物件细节（焦点锁在物件上） | 50mm 或 85mm（视场角 47°/29°） | F1.4 |
| 微距（毛孔、水珠、布料） | 45mm 微距：没有对应的视场角锚点；块式提示词里用主体尺度描述微距构图 | F2.8 |

打算保持焦点和直线几何的镜头可用的两句预防句；用户指令要求转焦或畸变时省略或修改：

- **插入镜头和紧近景锁焦：**`"focus plane locked on [object] from first frame to last — no focus drift, no rack focus, no autofocus hunting."`
- **广角/快镜头禁止畸变：**`"straight rectilinear lines, no barrel or pincushion distortion, no fisheye, no wide-angle warp."`（Seedance 块式提示词里视场角用度数而不是毫米：`higgsfield-seedance.md` § FOV anchors；本表的毫米/光圈词汇服务于非 Seedance 平台，而“目的→镜头”的逻辑两边都适用。）

### 按类型的镜头时长（Shot duration by type）

在确定事件、台词说出、可见反应或情绪弧线之后，再分配镜头时长。下面的范围是来自 shotlist-builder 来源的**可选节奏经验**，不是必须的长度，也不是切分 15 秒的配方。表演需要多久读出来就停留多久；注意、信息或因果需要时就切。没有固定的切镜数，也不要求主角停留。

| 镜头类型 | 示意剪辑时长 |
|---|---|
| 闪现的建立镜头 / 硬切开场（一瞬的远景） | 闪现 0.3–0.5 秒；地理需要被看清时更长 |
| 一句中等长度的台词 | 3–7 秒 |
| 带情绪弧线的无台词反应 | 5–10 秒 |
| 插入 / 远景 / 定格 | 0.3–2 秒 |
| 有完整弧线的情绪近景（例如 5–7 个表演节拍） | 8–15 秒 |

这些是剪辑上的镜头长度，不是 API 时长设置。短插入可以从一条合法生成里裁出来；更长的镜头可能需要支持的延伸，或者用离开/进入状态匹配的连贯片段。Seedance 2.0 的 **4–15 秒**范围按每次生成算，其他模型和模式有自己的限制。运镜时间与所选镜头时长保持一致，并在剪辑里核实结果。

### 微运动需要精确距离（Micro-moves need exact distances）

非常慢的推轨，要写明总行程**和**时间，否则模型会把运动做过头：`"over the full 7 seconds the camera pulls back only 10–15 centimeters — slow enough to barely register. No zoom, no sudden push."` 物理移动绝不写 `zoom`：写 dolly / track / push-in / pull-out。

**并且反过来检查：写出的运动必须能产生写出的结尾构图。**“缓慢推近”不可能从远景结束在大特写上，10 厘米的后拉也落不出一个全身揭示。运动和结尾构图对不上时，提示词内部就是不可能的：模型会选一个、即兴另一个。从更便宜的那一边修：加大运动（写出更大的行程），或缩小构图变化。`[EMPIRICAL — third-party director-skill evaluations 2026-08-09; re-derived]`

---

## Seedance 运镜最佳实践（Seedance Camera Best Practices）

> 这些最佳实践适用于 Seedance 2.0 / 2.5 视频生成。

### 单一运动规则（The One-Move Rule）

Seedance 文字驱动的运镜补救：叠加的运动导致抖动、意外旋转或失败时，每个镜头试**一个主运动**。这是针对模式的可靠性经验，不是对连续摄影机路径的通用禁令。工作室模板 `[镜头]` 里的“一段只做一个主运动”就是这条规则。

**错：**`Camera: dolly push forward while panning left and tilting up to reveal the skyline`
**对：**`Camera: slow dolly push from medium shot to tight close-up over 8 seconds`

如果这个补救需要分开覆盖，就拆成写明连续性的几个镜头；所选模式能渲染时，保留已批准的连续镜头。

### 按题材的运镜预设（Genre-Based Camera Presets）

这个模式下的可选起点；“避免”一列标出常见的不匹配，不是对用户指令或有动机的覆盖的禁令。

| 题材 | 主运镜 | 次运镜 | 避免 |
|-------|---------------|-----------|-------|
| 产品 / 电商 | 环绕、缓慢推近、固定 | 升降下降揭示 | 手持、甩镜 |
| 生活方式 / 社媒 | 手持、固定、缓慢摇 | 并行推轨 | 荷兰角、急推 |
| 剧情 / 叙事 | 缓慢推近、推轨后拉、跟拍 | 升起 | 快速运动、急推变焦 |
| MV | 甩镜、急推变焦、快速跟拍 | 360 环绕 | 固定（太闷） |
| 恐怖 | 慢慢潜近（推轨）、固定停留、荷兰角 | 降下 | 快速跟拍（打断紧张） |
| 动作 / 追逐 | FPV 无人机、跟拍、手持奔跑 | 急推 | 固定、慢速环绕 |
| 风景 / 旅行 | 升起、缓慢摇、无人机掠过 | 推轨后拉揭示 | 手持、紧景别 |
| 喜剧 / 社媒 | 固定（冷面）、急推变焦 | 甩镜 | 慢速的戏剧性运动 |

### 可靠措辞库（Reliable Phrasing Library）

这些措辞产出稳定、可预期的结果：

| 意图 | 可靠措辞 |
|--------|----------------|
| 不动 | `locked-off static camera, no movement` |
| 缓慢靠近 | `slow dolly push from medium shot to tight close-up over 8 seconds` |
| 跟随主体 | `handheld tracking following the subject, subtle shake, not chaotic` |
| 揭示尺度 | `crane shot rising from ground level to overhead` |
| 绕主体 | `smooth 180-degree orbit at eye level, constant distance` |
| 戏剧性变焦 | `crash zoom from wide to extreme close-up on impact` |
| 第一人称移动 | `FPV camera weaving through the environment at walking pace` |

中文提示词里对应写法：固定写“固定，平视，不推拉”；推近写“用 N 秒从中景推近到近景”；横移写“以 N km/h 横移跟随某人”。

### 通过 @Video 参考迁移运镜（Camera Transfer via @Video Reference）

实现复杂摄影机运动最安全的办法，是从参考里克隆：

```
Match the camera movement from @Video1. A dancer performs on a rooftop at sunset.
```

这绕过了单一运动规则，因为模型直接从参考里提取摄影机数据，而不是解读文字指令。

### 双视频参考（Dual Video Reference）

动作参考和运镜参考可以来自**不同的**视频。清楚地分开它们：

```
Reference @Video1 for the character's movement and choreography.
Reference @Video2 for camera movement only.
A martial artist performs a spinning kick in a dojo.
```

## 视频参考：能读什么，不能读什么（Video Reference — What It Reads, and What It Can't）

本仓库在好几个地方记录了 `@Video` 参考的用法（上面的运镜迁移、`higgsfield-style` 的调色延续、`higgsfield-audio` 的音色）。视频参考能可靠读取什么、哪里不足、完全做不到什么，这条能力边界在这里记录一次，适用于所有这些用法。

### 能可靠读取的（What It Reads Reliably）

`@Video` 参考能可靠地把源片段的这些属性带进生成：

- **世界设计**：整体环境、布景构造、光照逻辑、配色、氛围。
- **材质与质感**：表面的样子（湿木头、绳子、水的表现、布料的重量）。
- **物理与运动风格**：物体怎么动，水怎么表现，动作的重量和能量。
- **镜头性格**：摄影机操作的整体感觉、离主体的远近、它的运动词汇。
- **制作水准**：高预算还是低预算的感觉，整体的电影语域。
- **调色**：色调处理、反差、饱和度。
- **天气与环境条件**：风暴强度、雨的密度、雾、光的质量。

### 读取不太可靠的（What It Reads Less Reliably）

这些属性的迁移不稳定。设计提示词时不要依赖它们：

- **逐帧精确的动作续接**：要求模型精确接上上一帧结束的地方是不可靠的。参考理解的是当时发生的事的能量和世界，而不是每个元素精确的最终位置。
- **精确的角色身份**：角色身份锁定用图像参考，不用视频参考。视频参考读世界和能量比读脸或服装精度更好。
- **具体的对白或音频**：音色特征可能会带过来，但不保证精确的声音表演。

### 按用途的四种参考写法（Four Reference Patterns by Purpose）

在提示词里写明参考的任务。选与你想让参考做的事相符的写法：

| 用途 | 写法 |
|---|---|
| 世界连续 | `@Video1 — use for world continuity: same set construction, same lighting logic, same atmosphere, same production quality level` |
| 动作能量连续 | `@Video1 — use for action energy continuity: same event still in progress, same intensity of impact, same physical weight and momentum` |
| 镜头性格 + 制作感 | `@Video1 — use for camera character and production feel: same cinematic register, same operator presence, same overall quality` |
| 音色 + 表演风格 | `@Video1 — use for character voice and performance style: same vocal character, same delivery register, same performance energy` |

这种写法有效，是因为它告诉模型参考的哪个维度重要，让提示词的其余部分驱动新内容。工作室格式里，这一句按参考名称写在 `[动作与声音参考]` 的职责行，标签只在开头 `[参考资产]`。

### 硬限制（Hard Limits）

本节讲的是普通的 `@Video` 参考条件，不是 Seedance 2.5 原生的编辑/延伸或首尾帧流程；那些保留各自的母片和边界约定。不要只凭一个普通参考承诺这些结果：

- **不能从最后一帧接着某个具体动作。**如果参考片段结束在一个浪打上船，新片段不会自动以那个浪仍在打船开场。参考提供世界语境；明确写出新片段的开场动作，需要连续时继承源结尾的状态。
- **不能推翻你的提示词。**参考为生成提供信息，但不替代提示词指令。提示词和参考冲突时，通常动作以提示词为准，质感和世界感以参考为准。
- **不能单独提供角色身份。**角色一致性重要时，视频参考总要配一个图像参考。

### 承重规则（Load-Bearing Rule）

**动作以提示词为准，质感和世界感以参考为准。**提示词写发生了什么；让参考承载它看起来什么样。角色身份必须保持时，配一个图像参考。

---

## 相关模块（Related skills）
- `higgsfield-seedance-vfx`：视频到视频的素材变换：在替换世界或添加特效时逐帧保留真实的手持/驾驶镜头运动，并添加你从没拍过的计时运镜（急推、推近、揭示后拉）
- `higgsfield-image-shots`：静帧的机位角度和暗示的运动
- `higgsfield-prompt`：MCSLA 公式、提示词结构
- `higgsfield-style`：与运镜搭配的视觉风格
- `template-*.md`：演示运镜用法的带注释题材模板
