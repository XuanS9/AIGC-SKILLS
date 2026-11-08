# 模板：全局风格前缀（改一次处处生效的块）

一个**原样粘在**连贯 Seedance 2.0 分镜表每条提示词前面的风格块。改一次，处处都变。它锁定全片的整体画面，让 25 个分别生成的场景读起来像同一部作品。

格式说明：原样前缀是**连贯分镜表**的形态 `[FIELD — 13-project harvest]`。*独立*的块式提示词与此前不同：它从 SCENE CONTEXT 开头，把风格分散进各自归属的块（`higgsfield-seedance.md` § Distributed style — the standalone-block rule）。

工作室交付时，前缀的内容编译进每条提示词的 `[视觉风格]` 与 `[保持一致]`，不在块结构前另加一段；声音策略落在 `[声音]` 末尾的 `NO BGM。`，`[保持一致]` 末尾写“无字幕、无水印”。

## 何时使用

任何每个片段都要共用同一画面的多场景 Seedance 制作：短片、MV、叙事段落。它是 [`higgsfield-shotlist-director`](higgsfield-shotlist-director.md) 产物的最上层：加在每个场景提示词复制块的前面，并在分镜表 HTML 顶部的可折叠块里展示一次。

前缀锁定的是**全局**画面。单个场景可以用**场景覆盖**（见下文）打破它：只改那一条提示词的前缀，不改全局块。

## 规划连贯段落

用 [共享叙事规划](narrative-planning.md) 规划这个段落：资产、目标、全局视听与空间、行为、阶段、连续性、结尾画面、约束。这些是语义层。本前缀提供共用的画面和锁定；每个场景的提示词承载事件、行为、空间变化和交接。保留原样前缀、场景覆盖、复制块和可折叠分镜表 HTML 的格式。

先找出事件、因果、揭晓或状态的边界，再选镜头、分配时长。不预设数量，也没有等时规则：开头的“25 个场景”和“场景 2”的例子只是示意。跨切镜保留有动机的状态变化；身份与道具的连续不等于冻结剧情。计划中的停留姿势，按前缀的表演规则仍可以有呼吸或环境运动。定义结尾画面，并把转场计入段落预算；模型的技术限制仍然有约束力。

## 默认前缀块（填空后冻结）

替换方括号字段，保留带标签的结构。设定之后不要逐条改；改一次，然后重新渲染整个分镜表。

```
Style: [IMAX cinematic look], [16:9] widescreen. Photorealistic — no 3D render, no game engine.
Lighting: [Source-motivated light, palette and contrast derived from the chosen film reference and location. Each scene specifies story time, weather and available sources; exposure follows those conditions.]
Color: [60:30:10] — dominant / secondary / accent.
Camera: Physical cine lens. 180° shutter motion blur.
Skin: Pore-level realism — vellus hair, asymmetric moles, capillary flush, pore-shadow matching on-set light.
Acting: Hollywood — micro-pauses before reactions, precise eye-line, living eyes with catch-lights, chest rise from breathing. Characters never standing, always reacting.
Physics: Gravity and inertia respected — mass has real weight, correct contact shadows. No floating props.
Composition: Rule of thirds + golden ratio. Every person moving from frame one.
Continuity: Characters, props, environment identical across every cut. No identity drift.
Technical: 24fps smooth motion. 8K detail. No jitter.
Audio: Diegetic dialogue and environmental SFX only. No music. No subtitles.
```

字段说明：

- **画幅 / 分辨率**：与交付物的画幅一致。Seedance 2.0 支持 `auto/21:9/16:9/4:3/1:1/3:4/9:16` 和 `480p/720p/1080p/4k`（4K 仅 `mode=std`）。保持在模型枚举内，预检 lint 会抓出枚举外的值。
- **光照**：读取当前项目的美术设定。把它的光源逻辑、配色和反差带进每个场景，故事时间、天气、曝光和光源变化在场景里单独写。所选风格改变时先更新项目美术设定，再重新编译受影响的提示词。
- **色彩 `60:30:10`**：主色 / 辅色 / 点缀色的比例；三种颜色的名字写在每个场景的 Scene 块里，不写在这里。
- **音频：只用画内声音**：提示词正文只写真实世界的音效；配乐在后期叠加。见 `higgsfield-audio.md` § Seedance 2.0 与画内声音惯例。
- **质感行是画面声明，不是质量恳求**：Camera 行里的“180° 快门运动模糊”和 Color 里提到的颗粒，是*这部片声明的质感*，这是合法写法。退化的情况是同样的词孤零零地拖在某条场景提示词末尾、不依附任何东西；两者的区别见 `negative-constraints.md` § Whole-Frame Degradation。
- **写声明，不写否定清单**：每一行都是*必须成立的状态的声明*。声明里短短的锁定尾巴（“Photorealistic — no 3D render”“Diegetic SFX only. No music.”）在采集的语料里经过实地验证，也与 Seedance 规则自己的标准例子（“Consistent lighting, no flicker”）一致。禁止的是 `negative:` 清单语法或独立的裸否定清单：Seedance 没有负面嵌入结构，会把它们当成场景描述来解析。见 `higgsfield-seedance.md` § Prompt-Craft Laws → No negative prompts in the prompt body。

## 实地样本：生产中的前缀实际锁定了什么

`[FIELD — 13-project community harvest, 2026-07-18]`：采集到的每个项目都用**完全这种形态**的前缀：**每个分句一条轴，每条都是硬性的正向规则，总是以连续性/不漂移加音频策略收尾。**语料里观察到的轴（按项目需要选）：

- **格式**：“4K 变形宽银幕” / “8K 电影级照片写实”
- **媒介否定**：“照片写实的真人实拍：不要 3D 渲染、不要游戏引擎、不要动画电影质感”
- **镜头语言，按世界/场景变化时分别写**：“冒险片语言：急推、跟随飞行物、一镜到底” · 或一份**按场景的镜头语法表**（“客厅里是带操作员呼吸感的手持，追逐时是龙身后的跟拍，野生动物用锁定的超长焦”）
- **光照**：“单一有动机的光源：灯笼实景光、沙漠硬日光、暖色公寓钨丝灯对显示器的绿光”
- **色彩加保留的点缀色**：“每个世界用低饱和的年代调色，唯一的饱和点缀：装置的酸绿色光”（剧情道具独占唯一的饱和色；画面也可以留给剧情专用：“黄金时刻只留给反转”）
- **皮肤 / 表演 / 物理**：毛孔级写实 · 肌肉级表演、微停顿 · “遵守重力与惯性：沙会下陷，布会贴身，灰尘按真实颗粒落下”
- **连续性**：“角色、道具和环境在每次切镜中都锁定参考。不漂移身份。”
- **音频**：“只有环境音效和对白。没有音乐。”（这是*项目选择*，不是定律：13 个项目里 12 个禁用音乐、配乐留到后期；一个项目把挽歌做进了概念里）

**按语域区分的前缀**也经过实地验证：有一部片在同一个前缀里同时用温暖手持的“叙事”语域和干净锁定机位的“演示插入”语域，约束块本身也按语域划分范围（“不用三脚架、不用硬棚光：只留给演示插入镜头”）。

## 场景覆盖示例（场景 2 / 阳光下的体育场）

有一个场景打破了柔和的全局画面。只替换这一条提示词前缀里的 **Lighting 行**；其他字段和其他场景都留在全局块上：

```
Lighting: Natural light only — bright, genuinely sunny midday, strong direct sunlight from high and frontal (sun in front of and above the subject, behind the camera), deep blue sky, crisp hard-edged shadows, vivid saturated colour, low haze.
```

覆盖只是对一条提示词的局部修改，不是改全局风格前缀。如果你发现很多场景都在覆盖同一个字段，那个字段就应该归进全局块：收上去，重新渲染。

## 相关文件

- `higgsfield-shotlist-director.md`：本前缀位于其顶部的连贯分镜表
- `higgsfield-seedance.md` § Prompt-Craft Laws：前缀所包裹的单条提示词语法
