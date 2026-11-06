# Higgsfield 电影感图像提示词（Higgsfield Cinematic Image Prompting）

用作视频关键帧或分镜参考的静帧，把景别、主体位置、视线、画面方向和光传进 [共享导演规划](narrative-planning.md)。按需要的事件或揭示选视角；一个景别选项不强加切镜或时长。独立静帧的构图仍由下面的完整参考决定。

## 速查（QUICK FACTS）
- 范围：只管静帧构图；`[img 1]` 是上传参考图的占位符：没有参考时换成角色描述或 @ Element [→](#怎么使用这份参考how-to-use-this-reference)
- 基础写法：[景别关键词] of [img 1 或角色描述] + [姿势/动作] + [环境细节] + [光照/氛围] [→](#怎么使用这份参考how-to-use-this-reference)
- 10 种景别，从 EWS 到 Macro：EWS 主体在风景里很小、Wide 全身、Full 从头到脚、MLS 膝盖以上、Cowboy 大腿中部以上、Medium 腰以上、MCU 胸部以上、CU 脸、ECU 单个细节、Macro 质感 [→](#距离与景别速查distance--size--quick-reference)
- 景别关键词：“EWS, Vast, Landscape” / “Wide Shot, Full Body” / “Cowboy Shot” / “MCU” / “Close-Up” / “ECU” / “Macro” [→](#距离与景别速查distance--size--quick-reference)
- 10 种角度：Eye-Level、Low Angle、High Angle、Overhead、Worm's Eye、Dutch/Canted、OTS、POV、Selfie、Ground Level [→](#角度速查angles--quick-reference)
- 角度 = 情绪读法：低角度 = 力量，高角度 = 脆弱，荷兰角 = 不安/混乱，虫视 = 极端力量/超现实 [→](#角度速查angles--quick-reference)
- 多词的角度关键词：“POV, First Person Perspective” / “Selfie Angle, Arm's Length” / “Ground Level, Surface View” [→](#角度速查angles--quick-reference)
- OTS = 越过一个人的肩膀看另一个人：对白必备 [→](#过肩镜头otsover-the-shoulder-ots)
- 运动关键词在单帧里制造运动的感觉：动态模糊、暗示的运动、定格在动作中途 [→](#镜头运动在静帧中暗示camera-movements-implied-in-still-images)
- 静止/基础运动：Static、Pan、Tilt、Zoom In / Zoom Out、Pedestal Up/Down [→](#静止--基础static--basic)
- 进阶物理运动：Dolly In、Dolly Out、Truck Left/Right、Orbit、Crane [→](#进阶物理运动advanced-physical)
- 电影感与 AI 运动：Dolly Zoom（Vertigo）、Crash Zoom、FPV、Bullet Time、Handheld Follow、Camera Roll、Rack Focus、Pull Back Reveal、Fly-Through [→](#电影感与-ai-运动cinematic--ai)
- 最强的提示词三者叠加：[距离/景别] + [角度] + [运动暗示] + 主体 + 环境 + 光照 [→](#组合景别--角度--运动combining-shot--angle--movement)
- 完整公式以 [光照：时间、光源、质感] 收尾，再接 [风格：电影感、胶片、调色] [→](#图像提示词公式电影感静帧image-prompt-formula-for-cinematic-stills)


这个模块覆盖**静帧**的镜头构图：AI 图像生成的景别、角度和暗示的镜头运动。为任何 Higgsfield 图像模型写提示词时使用这些关键词和写法。

**与视频运镜控制的关键区别：**这些是单帧的构图指令。`[img 1]` 占位符指上传的参考图。没有参考图时，换成你的角色描述或 @ Element。工作室项目里，图像提示词按资产类型选模型（见 `image-models.md` § Routing by Asset Class）。

---

## 怎么使用这份参考（How to Use This Reference）

每个条目都有：
- **镜头/运动**：摄影术语
- **AI 提示词关键词**：放进图像提示词的确切词
- **用途**：它产生的情绪/构图效果
- **提示词示例**：可以直接改写的提示词短语

**图像生成的提示词写法：**
```
[Shot keyword] of [img 1 or character description] + [pose/action] + [environment detail] + [lighting/atmosphere]
```

---

## 距离与景别：镜头取景（Distance & Size — Shot Framing）

这些控制主体占画面多少、能看到多少环境。按这张图讲的是世界、角色还是一个细节来选。

### 大远景（EWS）（Extreme Wide Shot (EWS)）
**AI 提示词关键词：**EWS, Vast, Landscape
**定义：**主体几乎看不见；强调广阔的风景或地点。
**用途：**建立广阔感、表现孤立或强调尺度。
**提示词示例：**
```
Extreme wide shot of [img 1] standing alone in a vast, empty frozen tundra.
The subject is small in the distance, surrounded by massive snowy mountains.
Cinematic lighting
```

---

### 远景（WS）/ 全景（Wide Shot (WS) / Long Shot）
**AI 提示词关键词：**Wide Shot, Full Body
**定义：**在环境里显示完整的主体。
**用途：**提供语境和空间感。
**提示词示例：**
```
Wide shot of [img 1] standing full body in a snowstorm. She is wearing fur armor,
boots visible, centered in a snowy forest clearing. Environmental context.
```

---

### 全身镜头（Full Shot）
**AI 提示词关键词：**Full Shot, Framed
**定义：**从头到脚框住主体，同时更多地填满画面。
**用途：**平衡角色细节和环境。
**提示词示例：**
```
Full body shot of [img 1] from head to toe. She stands confidently in the snow,
holding a weapon at her side. Detailed costume design
```

---

### 中远景（MLS）（Medium Long Shot (MLS)）
**AI 提示词关键词：**Medium Long Shot
**定义：**从膝盖以上框住主体。
**用途：**运动或对白的自然取景。
**提示词示例：**
```
Medium long shot of [img 1] framed from the knees up. She is walking through
deep snow, looking towards the horizon. 3/4 angle view.
```

---

### 牛仔镜头（Cowboy Shot）
**AI 提示词关键词：**Cowboy Shot
**定义：**从大腿中部以上框住主体。
**用途：**强调姿态、准备状态或动作。
**提示词示例：**
```
Cowboy shot of [img 1] framed from mid-thigh up. Focus on her hands resting
on her belt, confident stance, snowy background with soft bokeh.
```

---

### 中景（MS）（Medium Shot (MS)）
**AI 提示词关键词：**Medium Shot
**定义：**从腰部以上框住主体。
**用途：**情绪和身体之间平衡的取景。
**提示词示例：**
```
Medium shot of [img 1] from the waist up. She is looking directly at the camera
with a serious expression. Snowflakes falling in the foreground.
```

---

### 中近景（MCU）（Medium Close-Up (MCU)）
**AI 提示词关键词：**MCU
**定义：**从胸部或肩部以上框住主体。
**用途：**有情感连接但不过分强烈。
**提示词示例：**
```
Medium close-up of [img 1] framed from chest up. Focus on her face and fur collar.
The wind is blowing her braided hair. Intimate and dramatic
```

---

### 近景/特写（CU）（Close-Up (CU)）
**AI 提示词关键词：**Close-Up
**定义：**紧框住脸或一个关键细节。
**用途：**突出情绪或细节。
**提示词示例：**
```
Close-up of [img 1], framing only her head and neck. Her piercing eyes looking
into the lens. Frosty breath visible in the cold air.
```

---

### 大特写（ECU）（Extreme Close-Up (ECU)）
**AI 提示词关键词：**ECU
**定义：**聚焦在很小的细节上。
**用途：**提升紧张感或亲密感。
**提示词示例：**
```
Extreme close-up on the eyes of [img 1]. Macro detail of the iris, snowflakes
caught in her eyelashes, war paint texture. Intense gaze
```

---

### 微距镜头（Macro Shot）
**AI 提示词关键词：**Macro
**定义：**显示细微质感的超近镜头。
**用途：**强调细节和质感。
**提示词示例：**
```
Macro shot of the texture of [img 1]'s fur armor and the frost on her skin.
Microscopic details of snow crystals and leather grain
```

---

## 距离与景别速查（Distance & Size — Quick Reference）

| 镜头 | 画面内容 | AI 关键词 | 最适合 |
|------|--------------|------------|----------|
| EWS | 主体在广阔风景里很小 | EWS, Vast, Landscape | 尺度、孤立、世界观建立 |
| Wide / Long | 全身 + 完整环境 | Wide Shot, Full Body | 语境、建立镜头 |
| Full Shot | 从头到脚，主体填满画面 | Full Shot, Framed | 服装、角色登场 |
| Medium Long | 膝盖以上 | Medium Long Shot | 运动、对白 |
| Cowboy | 大腿中部以上 | Cowboy Shot | 姿态、准备状态、动作 |
| Medium | 腰以上 | Medium Shot | 情绪与身体平衡 |
| MCU | 胸部/肩部以上 | MCU | 连接、亲密 |
| Close-Up | 脸 | Close-Up | 情绪、表情 |
| ECU | 单个细节（眼睛、手） | ECU | 紧张、亲密、质感 |
| Macro | 超近的质感 | Macro | 细节、材质、表面 |

---

## 角度（Angles）

这些控制摄影机和主体之间的垂直和空间关系。角度的选择会大幅改变一张图的情绪读法。

### 平视（Eye-Level）
**AI 提示词关键词：**Eye-Level
**定义：**摄影机与主体的眼睛齐平。
**用途：**中性、真实的视角。
**提示词示例：**
```
Eye-level shot of [img 1] facing the camera. Neutral perspective, realistic
documentary style portrait in the snow.
```

---

### 低角度（Low Angle）
**AI 提示词关键词：**Low Angle
**定义：**摄影机仰视主体。
**用途：**传达力量或支配。
**提示词示例：**
```
Low angle shot looking up at [img 1]. She towers over the camera, looking powerful
and dominant against a stormy sky.
```

---

### 高角度（High Angle）
**AI 提示词关键词：**High Angle
**定义：**摄影机俯视主体。
**用途：**传达脆弱或渺小。
**提示词示例：**
```
High angle shot looking down at [img 1]. She is looking up towards the camera,
snow falling onto her face. Vulnerable perspective.
```

---

### 顶视 / 鸟瞰（Overhead / Bird's Eye View）
**AI 提示词关键词：**Overhead
**定义：**从正上方拍。
**用途：**抽象或战略性的视角。
**提示词示例：**
```
Direct overhead bird's eye view of [img 1] standing in the snow. Top-down angle
showing her shadow stretching on the white ground.
```

---

### 虫视（Worm's Eye View）
**AI 提示词关键词：**Worm's Eye
**定义：**从地面正对上方拍。
**用途：**极端的力量感或超现实的尺度。
**提示词示例：**
```
Worm's eye view from the ground looking up at [img 1]'s boots and legs, with
her face distant in the sky. Ant-man perspective
```

---

### 荷兰角 / 倾斜角（Dutch Angle / Canted Angle）
**AI 提示词关键词：**Dutch Angle, Canted Angle
**定义：**摄影机向一侧倾斜（地平线倾斜）。
**用途：**制造不安、迷失方向或混乱。
**提示词示例：**
```
Dutch angle shot of [img 1], tilted horizon line. Disorienting and chaotic
atmosphere, battle ready pose, dynamic composition
```

---

### 过肩镜头（OTS）（Over-the-Shoulder (OTS)）
**AI 提示词关键词：**Over-the-Shoulder, OTS
**定义：**越过一个人的肩膀看另一个人。
**用途：**对白必备，让对话落地。
**提示词示例：**
```
Over-the-shoulder shot looking past a blurry Viking warrior in the foreground,
focusing on [img 1] who is staring back at them.
```

---

### 主观视角（POV）（Point of View (POV)）
**AI 提示词关键词：**POV, First Person Perspective
**定义：**摄影机*就是*角色的眼睛。
**用途：**观众体验角色看到的东西，沉浸感很强。
**提示词示例：**
```
First person POV shot of someone approaching [img 1]. She is looking directly
at the viewer, hand extended as if greeting the camera.
```

---

### 自拍角度（Selfie Angle）
**AI 提示词关键词：**Selfie Angle, Arm's Length
**定义：**高角度，一臂距离，面对主体。
**用途：**社媒美感里常见，随意、贴近。
**提示词示例：**
```
Handheld selfie angle of [img 1] looking into the lens, arm extended.
Casual vlog style, snowy mountains in the immediate background.
```

---

### 贴地（Ground Level）
**AI 提示词关键词：**Ground Level, Surface View
**定义：**摄影机直接放在地面/表面上，常带浅景深。
**用途：**沉浸式的地面或环境近景。
**提示词示例：**
```
Ground level shot, camera resting on the snow. Shallow depth of field with snow
crystals in foreground, [img 1] walking in the background.
```

---

## 角度速查（Angles — Quick Reference）

| 角度 | 摄影机位置 | AI 关键词 | 情绪效果 |
|-------|----------------|------------|-----------------|
| Eye-Level | 与眼睛齐平 | Eye-Level | 中性、真实 |
| Low Angle | 在下方，仰视 | Low Angle | 力量、支配 |
| High Angle | 在上方，俯视 | High Angle | 脆弱、渺小 |
| Overhead | 正上方 | Overhead | 抽象、战略 |
| Worm's Eye | 地面，正对上方 | Worm's Eye | 极端力量、超现实 |
| Dutch Angle | 地平线倾斜 | Dutch Angle, Canted Angle | 不安、混乱、紧张 |
| OTS | 越过肩膀 | Over-the-Shoulder, OTS | 对白、对峙 |
| POV | 角色的眼睛 | POV, First Person Perspective | 沉浸 |
| Selfie | 一臂距离，偏高 | Selfie Angle, Arm's Length | 社媒、随意 |
| Ground Level | 在表面上 | Ground Level, Surface View | 环境沉浸 |

---

## 镜头运动（在静帧中暗示）（Camera Movements (Implied in Still Images)）

图像生成里，运镜关键词在单帧里制造运动的*感觉*：动态模糊、暗示运动的构图，或者定格在运动中途的瞬间。

### 静止 / 基础（Static / Basic）

| 运动 | AI 关键词 | 定义 | 用途 | 提示词示例 |
|----------|-----------|------------|---------|----------------|
| 固定镜头 | Static | 摄影机不动 | 稳定和聚焦 | "Static camera shot of [img 1]. She stands perfectly still while snow falls heavily around her and the wind moves her hair. Tripod shot." |
| 左右摇 | Pan | 摄影机水平转动 | 揭示或跟随动作 | "Camera pans slowly from left to right, starting on a snowy tree and revealing [img 1] standing in the distance." |
| 上下俯仰 | Tilt | 摄影机垂直转动 | 揭示高度或纵深 | "Camera tilts up, starting at [img 1]'s boots in the snow and moving up to reveal her face and the mountain peak behind her." |
| 推近 | Zoom In, Lens Zoom | 摄影机缓慢靠近主体 | 增强情绪强度 | "Slow zoom in on [img 1]'s face. The background compresses as the camera gets tighter on her expression." |
| 拉远 | Zoom Out, Wide Reveal | 摄影机远离主体 | 揭示环境或孤立 | "Zoom out from [img 1]'s eye to reveal she is standing on the edge of a massive cliff. Establishing the environment." |
| 升降 | Pedestal Up, Pedestal Down | 整台摄影机物理地上下移动（像电梯） | 改变主体与地面的关系 | "Camera pedestals up, rising from the snow level to eye-level with [img 1], revealing her stature against the mountains." |

---

### 进阶物理运动（Advanced Physical）

| 运动 | AI 关键词 | 定义 | 用途 | 提示词示例 |
|----------|-----------|------------|---------|----------------|
| 推轨前进 | Dolly In | 摄影机沿轨道向前 | 受控的电影感亲密 | "Smooth cinematic dolly in towards [img 1]. The camera physically pushes forward through the snow, getting closer to her." |
| 推轨后退 | Dolly Out | 摄影机沿轨道向后 | 揭示尺度或情感距离 | "Cinematic dolly out from [img 1]. The camera physically moves backward, starting close to her face and retreating to show her alone." |
| 横移 | Truck Left | 摄影机水平向左或向右移动 | 增加视差和运动感 | "Truck right camera movement. The camera slides sideways parallel to [img 1] as she stands in profile, revealing the army behind her." |
| 环绕 | Orbit | 摄影机绕主体转圈 | 戏剧化的强调和能量 | "Camera orbits 360 degrees around [img 1]. She stands still in the center while the snowy background spins slowly behind her." |
| 摇臂 | Crane | 摄影机在摇臂上垂直移动 | 宏大揭示或史诗尺度 | "Crane shot starting low on [img 1] and sweeping high up into the air, looking down at the snowy valley below." |

---

### 电影感与 AI 运动（Cinematic & AI）

| 运动 | AI 关键词 | 定义 | 用途 | 提示词示例 |
|----------|-----------|------------|---------|----------------|
| 滑动变焦 | Dolly Zoom, Vertigo Effect | 摄影机后退同时推焦（或反过来） | 背景变形而主体大小不变：迷失方向 | "Dolly zoom effect on [img 1]. The background mountains appear to warp and grow larger while she stays the same size. Vertigo effect." |
| 急推 | Crash Zoom | 快速猛烈的变焦 | 震惊或突然的强调 | "Sudden crash zoom into [img 1]'s face. The camera snaps from a wide shot to an extreme close-up instantly. Dramatic impact." |
| FPV 无人机 | FPV | 快速、沉浸的飞行运镜 | 高能量和沉浸 | "Fast FPV drone shot flying through a snowy canyon and swooping past [img 1]. High speed, dynamic motion blur." |
| 子弹时间 | Bullet Time | 时间像冻结，摄影机在动 | 风格化的戏剧强调 | "Bullet time effect. Time is frozen with snowflakes suspended in mid-air, while the camera smoothly rotates 180 degrees around [img 1]." |
| 手持跟拍 | Handheld Follow | 手持摄影机跟随主体 | 紧迫感和真实感 | "Handheld camera movement following [img 1]. The image has slight shake and organic motion, documentary war reporter style." |
| 镜头旋转 | Camera Roll | 摄影机绕自身轴旋转 | 迷失方向或强烈感 | "Camera roll. The horizon line spins 360 degrees while focused on [img 1], turning the snowy world upside down and back again." |
| 移焦 | Rack Focus | 焦点在主体之间转移 | 引导观众注意 | "Rack focus shot. Starts focused on a sword in the foreground, then shifts focus to [img 1]'s face in the background." |
| 后拉揭示 | Reveal | 摄影机后拉揭示新语境 | 意外或尺度揭示 | "Pull back reveal. Camera starts on the detail of [img 1]'s eye, then pulls back rapidly to show she is standing on top of a burning village." |
| 穿越 | Fly-Through | 摄影机穿过环境元素 | 沉浸和动势 | "Camera flies through a gap in the trees and past falling snow to land on a medium shot of [img 1]." |

---

## 组合景别 + 角度 + 运动（Combining Shot + Angle + Movement）

最强的图像提示词三者叠加：

**写法：**`[距离/景别] + [角度] + [运动暗示] + [主体] + [环境] + [光照]`

**示例：**

```
Low angle medium close-up of [img 1], camera dolly zooming in slowly.
She towers over the frame against a blood-red sunset, wind whipping her cloak.
Cinematic lighting, high contrast.
```

```
Overhead extreme wide shot, static camera. [img 1] is a tiny figure at the center
of a vast frozen lake, her shadow stretching long. Blue hour lighting, desolate.
```

```
Ground level close-up, rack focus. Snow crystals sharp in the foreground,
[img 1]'s boots blurred behind them, then focus shifts to her face looking down.
Shallow depth of field, cold blue tones.
```

```
Dutch angle cowboy shot, handheld feel. [img 1] stands mid-thigh up in a
burning village, tilted horizon, smoke swirling. War paint on her face,
weapon drawn. Chaotic, urgent composition.
```

---

## 图像提示词公式（电影感静帧）（Image Prompt Formula (for Cinematic Stills)）

```
[Shot size] + [Angle] + [Movement keyword] of [img 1 / character description].
[Pose, expression, or action].
[Environment — location, weather, atmosphere].
[Lighting — time of day, source, quality].
[Style — cinematic, film stock, color grade].
```

**完整示例：**
```
Medium close-up, low angle, slow dolly in toward [img 1].
She stares past the camera with narrowed eyes, jaw set, braids falling over
one shoulder. A frozen battlefield stretches behind her, smoke rising from
distant fires. Golden hour backlight rims her silhouette.
Style: Cinematic, Kodak Vision3 500T, desaturated teal shadows, warm highlights.
```

---

> **共享约束：**图像生成里的脸/身份和质感/光照瑕疵，见 `negative-constraints.md`。

---

## 相关模块（Related skills）
- `higgsfield-camera`：视频运镜控制（本模块覆盖静帧构图）
- `higgsfield-style`：视觉风格和光照技法
- `higgsfield-models`：图像模型选择（Soul 2.0、Nano Banana、Seedream 等）
- `template-*.md`：按题材的注释提示词模板
