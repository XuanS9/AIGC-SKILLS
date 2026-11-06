# 模板：日式动画（Seedance 2.0）（Template: Anime Animation (Seedance 2.0)）

Seedance 2.0 里日式动画和风格化 2D 动画的可粘贴流程与提示词骨架：打斗戏、平静的节拍、变身，以及角色保持一致的段落。围绕分层的导演语法公式搭建，配一个可复用的动画风格块，以及一条用于锁定身份的角色转面提示词。工作室完整视频仍按中文块结构交付：本页的风格块编译进 `[视觉风格]`，角色身份走资产参考，对白写进 `[声音]` 的计时行。

## 何时使用

用户要日式动画或风格化 2D 运动时使用：作画高光的动作、变身揭示、平静的角色时刻，或带风格化角色和环境的多镜头动画段落。同一个角色必须跨镜头保持一致时，身份锁定和风格块最重要。

---

## 分层提示词公式（The layered prompt formula）

用 [共享叙事规划](narrative-planning.md) 规划视频：资产/参考 → 目标与结局 → 全局视听与空间规则 → 行为与节奏 → 阶段 → 连续性 → 结尾画面/交接 → 约束。这八层组织含义；把它们编译进下面的紧凑公式，约束一行放最后。可复用的风格、约束和静态转面块保留原生格式。

从事件、因果转折、揭晓或状态变化选择阶段边界，然后为了可见性选镜头，并估算动作、反应、对白和转场时间。没有预设的阶段数，也没有等长规则。一个连续镜头可以跨几个阶段；一个阶段可能需要几个镜头或几次生成。跨边界带上身份、姿势、道具归属、变身状态和声音，直到计划的结局。

```text
SUBJECT + ACTION + ENVIRONMENT + CAMERA MOVEMENT + VISUAL STYLE + CONSTRAINTS
```

- **主体**：场景里是谁或什么。用视觉方式喂给 Seedance（参考图或下面的转面表），而不只是用文字描述。
- **动作**：什么在变化或移动。每个镜头一个主导动作。事件、揭晓或空间可读性需要时请求多个镜头；规划好变化后再分配时长。
- **环境**：在哪里发生。场景的参考图有助于一致性。
- **运镜**：观众怎么看到它：低角度、高角度、滑动变焦、摇、俯仰、POV 镜头、多个脸部近景。
- **视觉风格**：最终的画面身份（下面的动画风格块）。
- **约束**：IP 安全 / 格式护栏（最后一行）。

> 每个镜头重复稳定的特征（头发、服装、姿态、表情）来保持主体一致。日式动画对一致性的要求更高：转面表给模型的几何信息远比文字描述多。

---

## 可复用的动画风格块（Reusable anime style block）

把这个块放进任何动画提示词的**视觉风格**层。它作为一整段可复用的字符串保留：

```text
2026 animation style anime animation, post time skip. 2d anime glow subtle
effect anime animation studios. subtle non precise cartoony. subtle non
precise animation style with clean, uniform-weight linework and simple, flat
cel-shading. The color palette is soft, muted, and classic animated. The
lighting is soft and even, with minimal directional influence from power
effects. Gradient shifts are minimized. The overall composition is
simplified. Make sure to get characters consistent. Give multiple faces
close-ons and different POV shots.
```

工作室中文稿对应的写法（放进 `[视觉风格]`）：二维日式动画，线条干净、粗细均匀，平涂赛璐璐上色，两到三级明暗；色板柔和、低饱和；光照柔和均匀，特效光对受光方向影响很小；渐变少；构图简化。

**IP 安全约束行（原生格式时追加）：**

```text
NO NSFW, NO COPYRIGHTED Content. NO TEXT, 16:9 video (no black stripes on
the borders), NO LOGO(S). RESPECT THE MANGA IMAGE PANELS. DO NOT USE IMAGES
AS STARTING FRAMES, BUT AS STYLE LOOKS.
```

这一行既固定格式（16:9，没有黑边/文字/标识），又让生成留在内容政策之内：它告诉 Seedance 把上传的漫画画格当作*风格参考*，而不是字面的起始帧。**工作室格式：**块结构稿里不写这串否定清单；画幅放在平台设置，`[保持一致]` 末尾写“无字幕、无水印”，参考职责写在映射块（“只用画面风格，不作起始画面”）。

---

## 角色转面表提示词（身份锁定）（Character turnaround sheet prompt (identity lock)）

先生成一张角色设定表，再把它作为每个镜头的主体参考。把下面的提示词贴进图像模型（Soul 2.0、GPT Image 2.0 或 Nano Banana Pro）。**工作室项目**的角色组板以 [角色资产交付规范](template-character-asset-delivery.md) 为准（唯一清晰面部特写 + 三个无头全身格，背景按服装明度选）；下面这份原版多格转面表只在用户明确要求这种版式时使用。

```text
A high-definition, clean, minimalist character design board / character
turnaround reference sheet, set against a pure white background. The overall
presentation should resemble a professional game art character modeling
sheet, fashion design reference page, character design sheet, or character
turnaround board. The layout should be neat and well-organized, with clearly
divided information sections, a realistic and premium visual quality,
consistent lighting, and strict character consistency throughout. colored.

On the left side of the composition, show the character's full-body
three-view turnaround (front, left-side, back full-body standing poses) as
the main visual area. All three figures must be the exact same character,
with identical facial features, hairstyle, clothing, body shape, and height
proportions. Arms hang naturally at the sides. Eye-level camera, neutral
studio lighting, no obstruction, no exaggerated perspective, no complex
background.

The upper-right section holds six headshot / head-angle references of the
same character (front portrait, slight downward angle, back-of-head, left
profile, near-side angle, 3/4 profile) with clear facial features and
consistent facial structure.

The lower-right section holds six close-up detail images in a clean grid
(upper-garment fabric texture, front lower-body clothing, hip/tailoring
detail, leg or skin texture, eyes/facial detail, shoes as a standalone
item). All detail images must match the main character's outfit and
appearance exactly.

Overall style: minimalist, professional, realistic, unified, clean, and
premium — sharp character edges, clearly defined garment shapes, natural
hair strands, refined skin, accurate material rendering, generous white
space, as if made by a professional concept art team.

Output: landscape composition, white background, full character visible, no
cropping, no extra props, no explanatory text, no logo, no watermark, no UI
elements, no like/save buttons, no social-media-screenshot appearance.
```

[角色外观描述]：或者更好的做法，换成你生成的转面表作为主体参考。

---

## 动画提示词示例（Worked anime prompts）

来源示例里的镜头数和时长只是示意：“大约 7 个场景，平均约 2 秒”描述的是一种可能的处理，不是阶段数，也不是让镜头等长的规则。填提示词之前，先从选定的事件和支持的时长推出实际的节拍表。

**动画动作 / 变身：**

```text
In an epic sakuga anime animation, generate an unexpected transformation of
[character] into [describe]. Professional sound effects and motion, accurate
lighting, detailed close-ons. [Describe the necessary events and visible responses,
with each resulting transformation state carried into the next stage. Add shot
changes and timings only after estimating their performance needs. End on the
confirmed final form and composition.] Background should be [..] (check reference images).

[paste anime style block]
[paste IP-safe constraint line]
```

**写实手持镜头（与动画对比）：**

```text
Generate a handheld shot of [character from reference image] but giant
(at least one skyscraper tall) doing the moonwalk down a famous city street,
destroying every high building as he dances, then kicking the buildings.
Continuous low-angle view recorded by a citizen. Dynamic composition and
intense action, handheld shaky shot. Dynamic music. Detailed realism,
lifelike video recorded on iPhone (no phone visible).
```

---

## 运动、风格与迭代说明（Motion, style, and iteration notes）

- **明确控制运动。**写清身体怎么动、摄影机怎么动、环境怎么反应（头发里的风、飘动的灰尘、光的闪烁）。把主体动作和运镜结合起来制造能量：“角色猛地转向镜头，同时镜头微微向前推近”比“很有动感”活得多。
- **需要时明确请求镜头。**写清每个视角揭示什么，以及它的进入/离开状态。原资料里“前 10 秒里从 10 个视角拍 10 个不同镜头”是一个示意性的蒙太奇，不是节奏配额。动作读得清楚时保留连续镜头；按表演和音乐改变镜头长度，而不是为了填时间加切镜。
- **让风格语言匹配目标。**日式动画 → 干净的线条、平涂赛璐璐、细微的光晕、柔和的渐变、一致的设计。真人 → 自然的皮肤质感、真实的纵深、镜头行为。道具近景 → 受控的光照、反射、材质细节。
- **一次迭代一个变量。**第一轮：构图 + 运动。第二轮：运镜 + 节奏。第三轮：风格 + 一致性。最后：打磨最好的那条结果。比每次从头重写快。

## 常见错误（Common mistakes）

- 在提示词里堆相互冲突的风格（写实 + 卡通 + 水彩 + 玩具感同时出现 → 输出不稳定）。
- 不描述运动；忘了运镜；一个镜头里混太多角色；要求太多不相关的动作。
- 没有具体内容的含糊词（“超棒”“疯狂”“美”）。
- 提示词中途换风格。一条好的提示词胜过五条乱的。
