# Higgsfield 词汇参考（Higgsfield Vocabulary Reference）

本文件是术语表：英文术语本身就是提示词词汇，保留原文；释义用中文。工作室块结构稿里，这些词按需要写进 `[具体情节]` 段头与 `运镜：`/`画面：` 行、`[视觉风格]`、`[镜头]`；英文预设名照原样写。

## 运镜术语（Camera Movement Terminology）

### 直线运动（Linear Movements）
- **Dolly In / Out**：平滑地靠近或远离主体
- **Dolly Left / Right**：平滑地横向移动
- **Dolly Zoom In / Out**：推轨同时反向变焦（眩晕/希区柯克效果）
- **Super Dolly In / Out**：推轨的夸张快速版
- **Truck**：横向推轨的另一种叫法

### 垂直运动（Vertical Movements）
- **Crane Up / Down**：垂直上升或下降
- **Crane Over The Head**：正上方，俯视
- **Levitation**：平滑如梦的向上漂浮
- **Tilt Up / Down**：摄影机绕水平轴旋转（不是物理移动）

### 环绕 / 弧线（Orbit / Arc）
- **360 Orbit**：绕主体一整圈
- **Arc**：半圈扫过
- **Lazy Susan**：慢速转盘式旋转
- **Robo Arm**：精密的机械弧线路径

### 变焦（Zoom）
- **Crash Zoom In / Out**：突然快速变焦
- **Rack Focus**：在近处和远处主体之间转焦

### 跟随 / 沉浸（Follow / Immersive）
- **Action Run**：低机位跟在奔跑的主体身后
- **FPV Drone**：快速灵活的空中穿梭
- **Handheld**：有机的、真实的手持晃动
- **Head Tracking**：锁定角色头部
- **Snorricam**：装在演员身上，背景晃动

### 电影技法（Cinematic Techniques）
- **Bullet Time**：绕定格主体的慢动作扫拍
- **Dutch Angle**：倾斜的对角构图
- **Fisheye**：广角畸变镜头
- **Whip Pan**：快速模糊摇镜
- **Overhead**：正上方俯视
- **Flying**：自由漂浮的空中滑行

### 机位角度（Camera Angles）
- **Low Angle**：仰拍主体（权力、主导）
- **High Angle**：俯拍主体（脆弱、渺小）
- **Eye Level**：中性，对话感
- **Bird's-Eye View**：正上方
- **Worm's-Eye View**：极低，垂直向上
- **Ground Level**：摄影机在地面上
- **Canted Angle / Dutch Tilt**：倾斜地平线，制造不安/紧张
- **Static Oblique**：斜角透视，偏轴
- **Over-the-Shoulder (OTS)**：对话构图，正反打
- **POV / First Person**：摄影机**就是**角色的眼睛

### 时间类（Time-Based）
- **Hyperlapse**：移动摄影机加延时
- **Timelapse Human / Landscape**：固定摄影机，时间快进
- **Low Shutter**：慢快门产生的运动拖影

### 剪辑与连续性词汇（Cut & Continuity Vocabulary）
- **Double contrast（双重对比）**：当事件得益于强烈对比时，同时改变景别**和**镜头性格（手持 / 固定 / 稳定跟拍 / 摇臂 / 航拍）的切镜技法。有意的重复覆盖和匹配剪辑仍然成立；这个技法不要求额外切镜。
- **Camera character（镜头性格）**：运动本身的方式：手持 | 固定/锁定 | 稳定跟拍 | 摇臂/垂直 | 航拍/无人机
- **Re-anchoring（重新锚定）**：任何切镜回到已建立的空间之后，重新写清谁在哪里、朝哪个方向。切镜前角色从左向右移动，切镜后方向相同。
- **180° rule（180 度规则）**：摄影机保持在主体之间假想线的同一侧，保住画面方向；越过它会让左右翻转，让观众迷失。
- **Exit-frame = implicit cut（出画即隐性切镜）**：角色离开画面后，在这个镜头剩下的时间里就不在了。这是旧版 Seedance 2.0 的补救经验：回来的角色漂移时，锚定他的路线、时机和重新入画状态，或用匹配的镜头覆盖；不禁止有意的连续出画/重新入画（见 `higgsfield-prompt.md` § Character & spatial rules）。
- **Causally-motivated insert（有因果动机的插入镜头）**：观众明白**为什么**看到的、不到一秒（0.3–0.5 秒）的静态细节。永远点名主体（“**他的**手抓住金属”），不写泛泛的（“一只手”）。线索揭示或道具状态变化需要足够阅读的时间。
- **Match cut（匹配剪辑）**：两个镜头之间以形状、运动或构图相连的切镜。
- **Anchor-gesture cut（锚定手势剪辑，“cut on action”）**：为了让两个*分别生成*的片段干净地剪在一起，让离开片段的结尾和进入片段的开头落在**同一个重复的手势**上（如轻敲耳机、推门、转头）。**工作室规则：**独立生成的 Clip 按 [Clip 边界隔离](narrative-planning.md#clip-边界隔离强制) 处理，边界按剪辑点隔离：尾镜动作完成、镜头静止，首镜换镜头并以定位秒开场，不依赖逐帧对齐的动作匹配。这个技法只用于一次生成内的切镜，或有真实输入的受控续接。
- **Multi-take micro-slice assembly（多条素材微切片组装）**：一场完成的戏常常是从很多条素材里剪出来的，而不是一条留下的片段：勺子来自一次生成，火焰来自另一次，倒水来自第三次，啜饮来自第四次。为此做计划：在每条素材里找出最好的 1–3 秒，存起这些切片，再组装。这是采用率纪律（`production-checks.md`）在挑选素材上的体现；另见 `higgsfield-seedance-failure-modes.md` § Failed-generation salvage。
- **Smash cut（冲击剪辑）**：没有任何过渡缓冲的突兀切镜
- **Hard cut / direct cut（硬切 / 直切）**：标准直切，没有效果
- **L-cut / J-cut**：下一个镜头的声音先于画面（J）或上一个镜头的声音延续到画面之后（L）。L-cut 的**声音桥**是制作团队的工作叫法：让离开镜头的声音跨过切点延续，使进入的画面落在已经建立的声景里。跨独立 Clip 的声音连续交给后期剪辑。
- **Whip-pan transition（甩镜转场）**：把两个镜头连成一个运动的模糊摇镜。大幅度空间转移按 [拆镜或甩镜过桥](directorial-shot-design.md#大幅度空间转移必须拆镜或用甩镜头过桥) 写。
- **Camera-relative-to-previous-shot continuity（相对上一镜头的机位连续）**：规划下一个镜头时，用**相对于上一镜头摄影机**的位置来写（`camera now behind him, facing the same direction he was facing`），而不是绝对位置。避免切镜让观众迷失。工作室复制正文里不写“上一镜”这类跨镜引用；把相对关系写成本段可见的方位。

### 剪辑语法（Editing Syntax）

提示词里表示时间和剪辑结构的写法惯例。

- **`[0-Ns]` 括号写法**：单个连续镜头内各阶段的时间区间前缀。例：`[0-3s] subject enters frame, [3-7s] camera pushes in`。用于单镜头连续运动里的逐秒节拍（见 `higgsfield-seedance.md` § Single-vs-multi-shot decision）。工作室格式改用段头 `起s-止s｜景别｜视场角N°｜运镜`。
- **`Establishing → phrase → reaction` 箭头写法**：多镜头对白或节拍段落的剪辑流写法。读作“建立镜头，然后台词，然后反应镜头”。三拍切镜结构的紧凑速记。

### 运动层级（Motion Hierarchy）

**四层运动层级**把一个镜头可以同时承载的运动分开，让提示词逐层点名：

1. **主体运动**：角色/物体做什么（走、转身、抬手）
2. **内部运动**：主体内部的微运动（呼吸、头发飘动、布料、眼动、微表情）
3. **摄影机运动**：摄影机做什么（摇、推轨、推近、停住）
4. **环境运动**：世界做什么（雨、落叶、背景车流、光线变化）

分开写每一层，可以防止多重运动过载的失败模式（见 `higgsfield-seedance-failure-modes.md` § Multi-motion camera overload）。

### 镜头约定（Camera Contract）

**镜头约定**是一种提示纪律：在描述主体或动作之前，先把摄影机行为写成明确的规则。摄影机行为不写明时，模型按训练先验去理解，未必符合想要的镜头；写明约定能锚定模型的输出。

三个示例约定，来自常见的镜头形态：

- `Static locked-off camera. Zero movement. No pan, no zoom, no dolly, no shake.`：氛围 / 观察性镜头、道具近景、神圣语域的画面
- `Slow push-in only — 10% scale change over the full duration.`：安静的情绪加强、顿悟节拍、单主体场景
- `Single handheld drift, slight organic sway, no cuts.`：自然 / 纪实语域、亲密场景、低保真视觉风格

原资料建议把每条镜头约定配上**负面提示强化**（见下文 § Composition Vocabulary → Negative-prompt reinforcement）。Seedance 正文没有负面提示语法；工作室写法是在 `[镜头]` 里用正向的约定句，例如“各段视场角段内不漂移，一段只做一个主运动”。

> 属于“五支柱电影运动语言”框架，另见 § Motion Physics Anchor（下文）、§ Lens Behavior Sequence（下文）、§ Composition Vocabulary → Spatial Zoning 与 Negative space。译自 Adil Aliyev 的 cinematic-motion-language 原始语料。

### 运动物理锚点（Motion Physics Anchor）

**运动物理锚点**通过把速度锚定到一个物理类比或时间测量上，来说明运动元素穿过画面有*多快*。

它不同于下文的 § Subject & Character → Movement Quality：后者描述运动的*性格*（流畅、生硬、犹豫、自信），是表演指导，而不是速度规格。两套词汇可以组合：一个角色可以用 `stumbling` 的性格（Movement Quality）、以 `the pace of a clock's hour hand` 的速度（Motion Physics Anchor）移动。这是描述运动的不同维度。

**物理类比的速度参照**把抽象的节奏锚定到可观察的真实运动上：

- `like dust suspended in honey`：极慢、黏滞、刻意
- `like embers floating in still air`：慢、失重、飘移
- `like smoke through a cathedral at dawn`：慢、分层、氛围感
- `like the surface of a lake disturbed by a single drop`：慢慢向外扩散的涟漪
- `like a flag in a steady cross-breeze`：中速、周期性、有方向
- `like a slammed door rebounding`：快、衰减的振荡

**时间锚定的测量**把节奏写成一个量：

- `one full revolution across the entire 10-second clip`
- `roughly 6 degrees per second`
- `the pace of a clock's hour hand — imperceptibly slow`
- `travels the full arc in 8 seconds with no pause`

运动速度的精度重要时，锚定到物理类比或时间测量，而不是形容词。`slow` 或 `fast` 这类形容词在随手写的提示词里可以快速指定，但比物理类比或时间锚点更难被可靠解读。方向性的规律：锚点越具体 → 输出越可控。工作室格式写成“用 N 秒”“以 N km/h”“约 N cm”。

> 属于“五支柱电影运动语言”框架，另见 § Camera Contract（上文）、§ Lens Behavior Sequence（下文）、§ Composition Vocabulary → Spatial Zoning 与 Negative space。与 `vocab.md` § Scene-physics lighting 相同的翻译纪律（用具名的物理机制替换形容词）。译自 Adil Aliyev 的 cinematic-motion-language 原始语料。

### 镜头行为序列（Lens Behavior Sequence）

**镜头行为序列**把一次对焦或景深事件描述成有结构的叙事：触发 → 转移 → 状态 → 回归 → 重复。把序列写成因果而不是单一静态的景深状态时，模型往往产出更干净、更可靠的对焦事件。

示例序列：

> `Focus opens on the subject. As the foreground element crosses the lens plane, focus shifts onto it — the subject softens into warm bokeh. The element drifts past. Focus breathes back to the subject. This cycle repeats organically 2-3 times.`

关键词汇：

- **shallow depth of field（浅景深）**：清晰平面很窄，前景/背景虚掉
- **focus-breathing（焦点呼吸）**：两个主体之间有机的进出焦变化，没有硬转焦
- **rack focus（转焦）**：在两个点名主体之间刻意的、有方向的焦点转移（简要条目见上文 § Camera Movement Terminology → Zoom → Rack Focus）
- **bokeh silhouette（焦外剪影）**：失焦的主体在背景光前变成一个柔和的暖色形状
- **lens plane crossing（穿过镜头平面）**：前景元素从摄影机和主体之间经过的那一刻，触发一次对焦事件
- **anamorphic lens rendering（变形镜头成像）**：椭圆焦外、横向光晕、宽银幕感（风格语域另见 § Visual Style Vocabulary → Named Platform Styles → Anamorphic，输出与风格的边界见 § Aspect Ratio: output spec vs. style register）

> 属于“五支柱电影运动语言”框架，另见 § Camera Contract（上文）、§ Motion Physics Anchor（上文）、§ Composition Vocabulary → Spatial Zoning 与 Negative space。译自 Adil Aliyev 的 cinematic-motion-language 原始语料。

---

## 景别词汇（Shot Size Vocabulary）

| 术语 | 画面内容 |
|------|--------------|
| Extreme Long Shot (ELS) | 辽阔风景，主体很小或不在 |
| Extreme Wide (EWS) | 主体在环境里很小 |
| Wide Shot / Long Shot (WS/LS) | 全身加周围环境 |
| Medium Long Shot / Cowboy (MLS) | 主体大腿中部以上 |
| Medium Wide (MWS) | 主体膝盖以上 |
| Medium (MS) | 腰部以上 |
| Medium Close-Up (MCU) | 胸部以上 |
| Close-Up (CU) | 脸 |
| Extreme Close-Up (ECU) | 细节：眼睛、手、物件 |
| Insert Shot | 物件或动作的细节 |
| Over-the-Shoulder (OTS) | 从角色肩后看过去 |
| POV | 第一人称角色视角 |
| Two-Shot | 两个角色同框 |
| Cowboy Shot | 大腿中部以上，姿态与随时动手的状态 |

工作室段头的标准景别词：远景、全景、中全景、中景、中近景、近景、特写、大特写（lint 按这些词识别）。

---

## 视觉风格词汇（Visual Style Vocabulary）

### 具名平台风格（Named Platform Styles）
- **Cinematic**：精致、高反差、专业
- **VHS**：复古颗粒、渗色、模拟的温暖
- **Super 8MM**：温暖的胶片颗粒、柔和暗角、怀旧
- **Anamorphic**：超宽、镜头光晕、史诗尺度
- **Abstract**：超现实、非具象、艺术化

### 画幅：输出规格与风格语域（Aspect Ratio: output spec vs. style register）

| 关注点 | 是什么 | 放在提示词哪里 | 受什么约束 |
|---|---|---|---|
| 输出画幅 | 硬性平台规格：模型实际输出的东西 | 头部或平台设置（例如“画幅：16:9”），工作室格式写在代码块外 | 按模型的枚举（Seedance 2.5：auto / 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16；用 `higgsfield model get <model>` 核对） |
| Anamorphic / 2.35:1 / 2.39:1 / Scope / Cinemascope | 摄影语域：变形镜头光晕、遮幅式构图的美感 | 画面那一行，作为风格要求（“anamorphic-style flares, letterboxed composition”），工作室格式写在 `[视觉风格]` | 风格性的：模型在所选输出画幅之内渲染出这种画面 |

把两者混为一谈会产生自相矛盾的提示词。“16:9 anamorphic”同时要求两件矛盾的事。模型要么忽略其一，要么产出不稳定的结果。把它们分开。

### 调色语言（Color Grade Language）

| 情绪 | 描述 |
|------|-------------|
| 大片 | 青色阴影，橙色高光，高反差 |
| 冷峻惊悚 | 去饱和的蓝灰，压暗的黑位 |
| 温暖怀旧 | 金琥珀色，提亮的阴影，柔和颗粒 |
| 赛博朋克 | 霓虹品红 + 青色，深阴影，HDR |
| 恐怖 | 病态的黄绿色，低反差，浑浊 |
| 爱情 | 柔和的粉金色，提亮的阴影，梦幻 |
| 纪录片 | 自然中性，不调色 |
| 史诗奇幻 | 深沉的宝石色调，体积光 |
| 黑色电影 | 高反差黑白 |
| 末日废土 | 去饱和的橙棕色，尘霾 |

### 色彩规则（Color rules）

- **60/30/10 色彩规则**：制作指导里的配色纪律。一帧画面里 60% 是一个主色，30% 是辅色，10% 是点缀色时读起来最干净。写出一个主色调加配套色板的提示词，比列出五种相互竞争颜色的提示词更统一。

### 胶片模拟（Film Stock Emulation）
- Kodak Portra 400：温暖、肤色饱满，轻微颗粒
- Fuji Velvia：鲜艳饱和的色彩，细颗粒
- Kodak Vision3 500T：电影感、自然、略暖
- Ilford HP5：经典黑白，可见颗粒
- Kodak Ektachrome：明亮、高反差、干净的反转片

（工作室复制正文不写外部片名或“某作品质感”；胶片型号是画面声明，不是作品引用。风格以项目视觉总纲为准。）

---

## 光照词汇（Lighting Vocabulary）

| 类型 | 描述 |
|------|-------------|
| Golden hour / Magic hour | 温暖有方向，太阳接近地平线 |
| Blue hour | 冷、柔，日落刚过 |
| Overcast / Softbox | 漫射、柔和，没有阴影 |
| Neon | 来自招牌/屏幕的彩色人工光 |
| Volumetric | 光束可见（雾/尘/烟） |
| Practical only | 只有画面里可见光源的光 |
| Side-lit | 一侧单一强光源 |
| Backlit / Rimlit | 光源在主体身后 |
| Motivated | 与场景里合理光源一致的光 |
| Hard light | 强的单一光源，阴影清晰 |
| Soft light | 漫射、包裹、阴影很少 |
| Rembrandt | 暗侧脸颊上的三角形光 |
| Butterfly / Paramount | 顶光，鼻下有阴影（魅力光） |
| Split lighting | 半张脸亮，半张脸在阴影里 |
| Chiaroscuro | 极端的明暗对比 |
| High-key | 明亮，阴影很少（喜剧、轻松场景） |
| Low-key | 深阴影，情绪化（黑色电影、恐怖） |
| Harsh midday sun | 硬的顶光，阴影强烈清晰 |

### 场景物理式光照（Scene-physics lighting）

把光照描述成场景里的一个物理事件，而不是一个风格形容词。写明光源位置、它反射的表面，以及由此产生的阴影几何：模型用每个点名的部分在镜头间一致地重建照明。

- **光源位置**：`key light from screen-left, ~30° above eye line`
- **反射 / 反弹**：`warm bounce off the wooden floor lifting under-jaw shadow`
- **阴影几何**：`hard shadow on screen-right wall reading the silhouette of the desk lamp`
- **环境密度**：`dense ambient haze in the foreground softening contrast 6m+ out from camera`

场景物理的写法用可以组合的具名物理机制，替换风格形容词（`moody`、`dramatic`、`cinematic`）。模型能渲染具名的机制；对形容词只能近似。工作室格式：`[视觉风格]` 写光源方向（画面左/右）、色温 K、反差和材质。

> 把保留的真实主体或新增的生物*融合*进新底片时（视频到视频），只匹配颜色读起来像“贴上去的”。要同时匹配主光方向、环境反弹、光学/大气雾霾和边缘落地：完整配方在 `higgsfield-seedance-vfx.md` § Lighting integration。

### 夜景语域（The night register）

`[DEMO — Joey banana-pro-director 3.0, 2026-08-16]` `[UNPROVEN HERE]` 直白地写“夜晚”，回来的是**明亮的夜**：一个均匀照亮的场景罩上一层蓝青色，那是白天底片调冷的样子，不是夜晚的样子。院线式的夜景**大部分是暗的，硬而有力的实景光源从中穿过**。这个语域分成两种，区别在于**允许什么当光源**：

**A. 室外 / 开阔夜景**（峡谷公路、偏远外景，任何没有建筑照明的地方）。光**只来自场景里的实景光源**：车头灯、刹车灯、从开着的车门漏出的仪表盘光、远处城市的光晕。**没有环境月光，没有天空提亮。**天空和周围压成深沉的近黑。空气中的雾霾接住光束，形成可见的体积光柱；后向散射只照亮车辆正前方和它前面的地面。光照范围之外的一切落到近黑，所以主体主要读作剪影，光源勾出它们向前的边缘。极远处可以有一点地平线光晕：小、收敛、勉强读出是远处的人烟，**绝不亮到能照亮**前景或中景的任何东西。

**B. 室内 / 城市夜景**（车库、仓库、街道、小屋）。实景光源仍然主导画面：钠灯、荧光灯、霓虹、仪表盘光、刹车灯。**这里允许青–琥珀的分色**，正是因为实景光源为它提供了动机：冷的钠灯和荧光对暖的仪表盘和琥珀色。没有动机的版本（画面里没有光源，青色却泼满一切）读起来是调色，而不是场景。

决定性的检验，就是本仓库对光照的一贯要求：**写出光源，而不是情绪。**上表里的 `Motivated` 和 `Practical only` 是撑起夜景的两行；单写 `low-key` 不够，因为它只说了有多暗，没说光从哪里来。

### 频闪（Strobe）

频闪照明的场景，需要把脉冲描述成一个事件而不是形容词，并且要同时写明三件事，否则读起来像坏掉的素材：

1. **脉冲本身**：硬开、硬关，按写明的 BPM，偶尔有两连、三连的卡顿。每次闪光瞬间而耀眼，把场景清楚地定格在动作中途；每个间隔落到近乎全黑。没有渐变：每次转换都是硬切。
2. **一个辅助光**，在两次闪光之间保持微弱的恒定光，让形体在黑暗里仍可读，而不是画面变成什么都没有。
3. **一句持续运动的说明**：*“闪光之间没有任何东西被冻结、停住或静止；每个身体始终在持续运动，只是光让它们停住了。”*没有这一句，模型会把身体渲染成真的停下，这就是频闪和卡顿的区别。

> **逐拍的光脉冲会让人感觉画面卡顿。**收到输出卡顿的反馈时，先把脉冲柔化成缓慢连续的起伏；还卡就去掉脉冲，改成恒定光。原因通常是脉冲，不是帧率。

---

## 主体与角色词汇（Subject & Character Vocabulary）

### 肢体语言 / 姿态（Body Language / Posture）
- Upright, tense, coiled, relaxed, hunched, squared-off（挺直、紧绷、蓄势、放松、佝偻、端正对峙）
- Arms open / crossed / raised / at sides（手臂张开 / 交叉 / 举起 / 垂在身侧）
- Weight forward / back / centered（重心前倾 / 后靠 / 居中）
- Eyes wide / narrowed / cast down / direct to camera（眼睛睁大 / 眯起 / 低垂 / 直视镜头）

### 运动性格（Movement Quality）
- Fluid, jerky, precise, hesitant, confident, stumbling（流畅、生硬、精准、犹豫、自信、踉跄）
- Slow-motion, overcranked（高帧率 = 慢放）
- Undercranked（低帧率 = 快放）
- Natural, stilted, mechanical, animal-like（自然、僵硬、机械、像动物）

### 情绪线索（用于运镜和表演）（Emotion Cues (for camera and performance)）
- 顿悟：缓慢 Dolly In，眼睛睁大
- 恐惧：Dutch Angle，Handheld
- 力量：Crane Up，360 Orbit，宽站姿
- 脆弱：Overhead，Dolly Out，在画面里很小
- 亲密：Dolly In，浅景深
- 混乱：FPV Drone，Handheld，快切

（这些是可选的起点，不是映射规则；见 `higgsfield-camera.md` § Camera-Emotion Sync。）

### 情绪作为可见行为：通道（Emotion as Visible Behavior — Channels）

情绪变得对镜头可见的八个具名通道。用它们把抽象的情绪语言（“她害怕”“他生气”）拆解成模型能演出的可观察身体行为。

- **呼吸**：频率、深浅、屏住、呼气的性质
- **眼部行为**：注视、眨眼频率、视线方向
- **下颌紧张**：咬紧、松弛、在动、定住
- **失焦**：视线飘走、注意力溜走、反应延迟
- **扫视模式**：眼/头扫过的方向、追踪的目标
- **延迟恢复**：刺激与调整回基线之间的滞后
- **控制尝试**：可见的压抑或调节努力
- **峰值之后的情绪残留**：主导节拍之后身体上还读得出的东西

下面的微表情词汇一节列出具名的终点表情（憋住的笑、冷静盘算等）：它们是这些通道的组合。上面的通道是底层；具名表情是底层产生的东西。

这八个通道是情绪的**行为**拆解。**解剖**拆解（把具名的面部肌肉写成 FACS 动作单元代码，如 AU6 脸颊上提、AU12 嘴角上提，用于肌肉级的 Seedance 控制）是它的同类，在 `higgsfield-facs.md`。通道说身体*做*什么；AU 说哪些*肌肉*在动。工作室格式里，这些线索写在 `[具体情节]` 各段的 `表情：` 行，近景/特写写 2–4 个。

---

## 环境与氛围词汇（Environment & Atmosphere Vocabulary）

### 时段（Time of Day）
- 黎明：第一缕光，薄雾，冷蓝转暖橙
- 黄金时刻：日出后 / 日落前一小时
- 正午：硬的顶光，深阴影
- 阴天：平、漫射、中性
- 蓝调时刻：日落后，冷而柔的光
- 夜晚：暗，一片片的光，阴影重

### 天气 / 氛围（Weather / Atmosphere）
- 雨：湿表面、反光、升起的蒸汽
- 雾：柔和的纵深、降低反差、神秘
- 雪：低饱和的色彩、漫射光、暗示安静
- 热霾：闪动的空气、温暖的扭曲
- 风：运动的元素，头发/布料/树
- 尘/烟：体积光的机会

### 环境类型（Environment Types）
- 城市：混凝土、玻璃、霓虹、人群、车流
- 工业：金属、锈、机器、蒸汽管
- 自然：有机质感、多变的光、尺度
- 室内：受控的光、道具、亲密
- 荒野：原始、不可预测、辽阔
- 奇幻：设计过的、非现实、加强的

### 通过重复建立世界（World Through Recurrence）

让一个世界跨多个镜头对观众变得可读的八个具名底层维度。用它们找出哪些东西应该跨场景一致地重复：世界来自重复出现的东西，而不是被解释的东西。

- **反复出现的空间**：回来的地点，跨幕呼应的空间类型
- **光的行为**：光以重复的模式进入、落下、衰减
- **沉默**：安静的质感和时机，节拍之间留住的东西
- **材质**：表面词汇、物质选择、触感特征
- **建筑**：走廊逻辑、门槛的用法、建造形态约束运动的方式
- **道具**：以一致含义反复出现的实物
- **情绪状态**：反复出现的情感状态、恐惧的浓度、一个节拍解决之后还留着什么
- **镜头距离 / 节奏**：远近选择、何时后退、节奏模式

---

## 音频 / 声音词汇（用于 Seedance 和支持音频的模型）（Audio / Sound Vocabulary (for Seedance and audio-capable models)）

| 声音类型 | 提示词里的描述 |
|------------|----------------------|
| 环境声 | "soft city hum", "distant traffic", "forest insects"  |
| 天气 | "rain on cobblestones", "wind through trees", "thunder rumble" |
| 运动 | "footsteps on gravel", "fabric movement", "glass crunch" |
| 机械 | "engine revving", "metal scrape", "hydraulic hiss" |
| 人声 | "breathing", "heartbeat rising", "crowd murmur" |
| 音乐提示 | "tense strings build", "low bass drone", "electronic pulse" |

工作室格式：接触音效 `<…>` 写在各段的 `声音：` 行，环境声写在 `[声音]`，音乐只在用户要求时用 `(…)`，末尾 `NO BGM。`

---

## 平台功能词汇（Platform Feature Vocabulary）

这些是 Higgsfield 图像侧的平台术语；本工作室不覆盖相应的平台功能流程，角色一致性按 [角色资产交付规范](template-character-asset-delivery.md) 和资产总表处理。

| 术语 | 定义 |
|------|-----------|
| Soul ID | 上传一个真人的 20 张以上照片，训练跨生成的身份一致性 |
| Soul Cast | 从参数生成 AI 演员（不需要照片） |
| Soul HEX | 从参考照片提取配色，让镜头之间的画面颜色一致 |
| Soul Cinema Preview | Higgsfield 自有的电影级图像模型，只用提示词驱动，擅长近景 |
| Reference Anchor | 跨所有镜头锁定角色几何的系统 |
| Hero Frame | 在视频之前生成的关键图像，定义视觉基调、光照和构图 |

### 图像参考写法：`@Image1` 与 `<<<image_1>>>`（Image Reference Notations — `@Image1` vs `<<<image_1>>>`）

两种写法指向同一个底层的 @ 参考机制；用哪种括号取决于你在面向哪个界面。

- **`@Image1`**：在给 Higgsfield 生成引擎的实际提示词里使用的平台侧参考语法。大写 `I`，没有下划线，单个 `@`。用于 `template-*.md` 和大多数子模块的提示词示例（如 `template-06-portrait-character-intro.md`）。提示词里的写法：`@Image1 as the character`、`@Image2 as the background`。工作室项目里，项目调用名是 `@` + 纯中文名（写在开头 `[参考资产]` 的 `@名字 对应 名字。` 行），平台槽位编号另行维护。
- **`<<<image_1>>>`**：Seedance 2 Skill 内部的显式参考写法，用在给 `seedance-bilingual-json.md` 中英双语提示词导演的用户请求里。小写 `image`，下划线，三重尖括号。用户请求里打出来时 Seedance Skill 能识别，然后映射到合适的场景元素（见 `seedance-bilingual-json.md` § Image reference system）。

**按槽位的职责约定**：制作实践给每个 `@Image` 槽位锁定一个稳定的职责，在一张分镜表的每条提示词里保持一致：`@Image1 = 角色身份`、`@Image2 = 服装`、`@Image3 = 环境 + 光照`、`@Image4 = 构图`、`@Video1 = 动作`、`@Video2 = 运镜`、`@Audio1 = 节奏 + 氛围`。这个约定是团队侧的纪律，不由模型强制；好处是长分镜表里参考稳定（见 `higgsfield-seedance.md` § Per-Image Role Convention）。

---

## 构图词汇（Composition Vocabulary）

描述画面**里**有什么、放在哪里的词汇：区别于摄影机侧的语言（描述摄影机怎么动）和光照（描述照明）。

### 负面提示强化（Negative-prompt reinforcement）

原资料里的一条贯穿性构图纪律：提示词对画面声明一个正向约束（锁定的摄影机、一个黑色区域、刻意空着的区域）时，在负面提示里镜像这个排除，让模型从两边都受约束。

**工作室范围：**Seedance 提示词正文没有负面提示语法（`higgsfield-prompt.md` § No Negative Prompts），也不靠负面提示词修复画面。下面的负面一侧只适用于确有独立负面字段的平台；在工作室块结构里只写正向一侧的声明。

示例对：

- 正向：`Static locked-off camera. Zero movement.`
  负面：`camera movement, pan, zoom, dolly, shake`
- 正向：`Left third: pure black, no motion, no light.`
  负面：`particles on the left side, light on the left side, movement on the left side`
- 正向：`Foreground plane: particle layer only — no subject.`
  负面：`subject in foreground, character in foreground`

正向的声明说出意图；负面的强化防止模型违背这个意图去填充。使用这个技法的支柱：§ Camera Movement Terminology → Camera Contract（镜头规则强化）；下文 § Spatial Zoning（区域规则强化）；下文 § Negative space（排除区域强化）。

### 空间分区（Spatial Zoning）

**空间分区**提示把画面分成具名区域，并给每个区域分配明确的规则。这能防止模型用编造的内容填充空白：这是一个可证伪的制作说法，与基于 transformer 的视频模型对明确约束的反应方式很一致。

**区域命名惯例**（按需组合）：

- 三分：`left third`、`center third`、`right third`
- 纵深平面：`foreground plane`、`midground`、`background`
- 二分：`upper half`、`lower half`
- 非对称分割：`right two-thirds / left void`、`left two-thirds / right void`

**区域规则示例**（每个区域声明它的内容和行为）：

- `Left third: pure black, no light, no particles, no movement.`
- `Right two-thirds: all action contained here.`
- `Foreground plane: particle layer only — no subject.`
- `Background: unlit void, no detail.`

原资料建议总是在负面提示里强化区域规则（见上文 § Negative-prompt reinforcement 及其工作室范围）。下文 § Negative space 是空间分区体系里一种常见的区域类型。工作室格式里，区域写在 `[具体情节]` 各段的 `画面：` 行（前景/中景/背景、画面左/右/上/下）。

> 属于“五支柱电影运动语言”框架，另见 § Camera Movement Terminology → Camera Contract、§ Motion Physics Anchor、§ Lens Behavior Sequence、§ Negative space（下文）。译自 Adil Aliyev 的 cinematic-motion-language 原始语料。

### 负空间（Negative space）

画面里刻意空着、用来孤立主体或给它分量的区域。制作指导的写法：`negative space sits center-left of frame, narrowing as the character advances`。把负空间点名为一个构图元素，能防止模型用无关细节填满它。

提示词点名一个负空间区域时，原资料建议在负面提示里镜像这个排除（见上文 § Negative-prompt reinforcement 及其工作室范围）。负空间是 § Spatial Zoning 体系里的一种具名区域类型：空间分区声明区域规则；负空间点名哪些区域刻意空着。两者可以组合。

原始语域有时用富有感染力的说法命名负空间：`sacred emptiness`、`active darkness, not background`、`deliberate compositional weight`。当这种说法建立在构图规则之上时，制作指导语域是容许的：例如在一个区域已经声明为无光、无运动、无粒子*之后*，再把它叫作 `sacred emptiness`。没有底下的规则，感染性的命名读起来就是堆形容词；正是规则让这种说法起作用。（感染性命名的例子来自 Adil Aliyev 的 cinematic-motion-language 语料。）

> 属于“五支柱电影运动语言”框架，另见 § Camera Movement Terminology → Camera Contract、§ Motion Physics Anchor、§ Lens Behavior Sequence、§ Spatial Zoning（上文）。

### 越位规则（Crossing rule）

一条电影语法句，说明角色在一个镜头内或跨切镜时是否可以在画面上交换位置。它不同于摄影机侧的 180° 规则（关于主体之间的假想线）：越位规则说主体可以做什么，180° 规则说摄影机可以做什么。例：`Character A stays on the left, Character B stays on the right, neither crosses the central vertical axis`。工作室格式写在 `[保持一致]`，左右以镜头为准。

### 坐标写法（Coordinate notation）

画面内位置的定性 + 百分比配对锚点。`Character A stands in the right third, x-position 70%, y-position 50%, frame occupancy 25%`。定性词给出电影语言的抓手；百分比给出精度目标。完整的坐标系统和注意事项见 `higgsfield-seedance.md` § Frame Coordinate System。

---

## 制作词汇（Production Vocabulary）

从传统电影制作引入 AI 电影实践的术语：制作流程里反复出现的纪律的名字。

- **Script supervising（场记）**：传统电影制作的纪律，跨镜头追踪每个角色的状态（伤势、服装、道具、头发），让连续性跨切镜保持。在 AI 电影里通过按状态的角色参考来实现：一个有五个阶段的角色（例如初始 / 打斗受伤 / 部分变形 / 几乎完全变形 / 完全变形）得到五个不同的状态衍生图，每阶段一个。工作室按资产总表登记状态图（`状态_基础对象_状态名_v01.png`），基础阶段不批量做。
- **State lock（状态锁定）**：每个镜头里点名角色当前情绪或身体状态（平静、筋疲力尽、受伤、湿透、在运动中）的指令。不同于 `pose`（身体姿势）和 `facial expression`（情绪语域）：状态锁定点名的是应该在整个镜头时长里保持的持续状态。工作室格式写在映射块的 `本段状态：…`。

---

## 微表情词汇（Micro-Expression Vocabulary）

上面的“情绪作为可见行为：通道”一节列出了这些终点表情拆解成的八个底层通道。

角色提示词的表演指导：

| 表情 | 描述 |
|-----------|-------------|
| Deadpan Neutral（冷面中性） | 平淡的情感，没有可见情绪 |
| Fierce Focus（凶狠专注） | 强烈锁定的凝视，全部注意力 |
| Suppressed Smile（憋住的笑） | 在忍住笑，嘴角抽动 |
| Quiet Devastation（安静的崩溃） | 眼睛湿润发直，下颌紧绷，强撑着 |
| Cold Calculation（冷静盘算） | 眼睛扫视，没有情绪泄漏，冷静客观 |
| Bitter Amusement（苦涩的好笑） | 单侧冷笑，眼睛没在笑 |
| Frozen Shock（定格的震惊） | 嘴微张，眼睛定住，身体不动 |
| Simmering Rage（压着的怒火） | 咬紧下颌，鼻孔张开，稳定的瞪视 |
| Vulnerable Openness（脆弱的敞开） | 眼神柔和，双唇微分，毫无防备 |
