# Higgsfield FACS 导演（Higgsfield FACS Director）

完整格式和角色的事件/反应弧线以权威的 [共享导演规划](narrative-planning.md) 为准。AU 代码是可选的；AU 节拍、切镜和生成片段是不同的东西。把下面的表情/AU 数量当作复杂度经验，时长从实际表演推出。保留台词前/中/后的连续性，不设固定停顿。跨切镜和延伸接点带上表情、视线、呼吸和身体状态。

像动画师那样指导一张脸：靠**肌肉**，而不是靠情绪。FACS（面部动作编码系统）把每个面部动作命名为一个**动作单元**：`AU12` 是嘴角上提（笑），`AU6` 是脸颊上提，`AU4` 是皱眉。这些代码可以在 Seedance 2.0 提示词里请求对应的动作，遵循度是经验性的、有波动。它们为强挤的笑、诡异的脸、混合情绪和近景对白提供了可选词汇；直白的可见行为同样成立，既不要求精确执行，也不要求近景。

> **本模块是叠在 `higgsfield-seedance.md` 之上的面部控制层。**完整视频提示词仍用工作室块结构；原生格式或表情研究格式只在明确选择时使用。FACS 只细化相关的可见行为，不改变输出约定。应用 [表演证据验收](higgsfield-acting.md#表演证据验收)；非人主体用 [非人角色表演适配](higgsfield-acting.md#非人角色表演适配)，不假设人类肌肉/AU。读这个模块不要求使用 AU 代码，也不要求生成表情表（Reading this module does not require using AU codes or generating a sheet）。

## 速查（QUICK FACTS）
*路由辅助：实际规则见链接章节。*
- FACS = 把面部表情写成**动作单元代码**（肌肉运动），不是情绪标签；代码写进提示词 [→](#facs-是什么what-facs-is)
- **来源要分开：**AU 词汇是标准的人体科学；Seedance 对提示词里代码的*解读*是 **[EMPIRICAL]**：成功率高，**但不是保证** [→](#来源与不是保证规则provenance-and-the-not-a-guarantee-rule)
- **先规划。**确定表演需要的表情（在下文每次生成的复杂度指引内）→ *只为这些*生成一张 FACS 表 → 写代码。生成完整的 49 个 AU 再挑是反面做法 [→](#先规划流程the-plan-first-workflow)
- **3–4 个表情是可选的复杂度起点。**诊断 AU 过载，但不给完整表演设上限 [→](#第-2-步把-au-代码写进-seedance-提示词step-2--put-au-codes-in-the-seedance-prompt)
- 两种写法：**只写代码**（`AU12`）对比**代码 + 简短解剖描述**；两种都试，没有一种总是更好 [→](#第-2-步把-au-代码写进-seedance-提示词step-2--put-au-codes-in-the-seedance-prompt)
- 参考表是一张**带标签的网格图**（GPT Image 2 / Nano Banana Pro）；LLM 可能**标错 AU**，所以要迭代和核对 [→](#第-1-步生成-facs-参考表step-1--generate-the-facs-reference-sheet)
- 角色照片是**可选的**：没有它代码也有效；只为身份一致性才附上 [→](#第-2-步把-au-代码写进-seedance-提示词step-2--put-au-codes-in-the-seedance-prompt)
- 常见情绪可以拆成标准 AU 配方（杜兴微笑 = AU6+AU12；悲伤 = AU1+AU4+AU15）[→](#情绪--au-配方emotion--au-recipes)
- 价值在**对白 / 独白**：可选的 AU 节拍表配合计时对白；保留台词前 / 中 / 后的连续性，不强制手势或停顿 [→](#对白与独白的面部表演dialogue--monologue-facial-acting)
- [OFFICIAL] 身体微节拍菜单（喉、呼吸、皮肤、姿态）；按感知错开反应，0.3–0.5 秒只是示例；让听者在可读的景别下保持鲜活 [→](#物理微节拍脸以外的身体physical-micro-beats--the-body-beyond-the-face)

---

## FACS 是什么（What FACS Is）

面部动作编码系统（Ekman 与 Friesen）把脸拆成**动作单元**：视觉上可区分的最小肌肉运动。与其要求“高兴”（模型会在海量素材里分散地采样），不如要求*产生*这个表情的肌肉：

- `AU6`：脸颊上提（眼轮匝肌收紧，出现鱼尾纹）
- `AU12`：嘴角上提（颧大肌把嘴角向上向外拉）
- 合起来，`AU6 + AU12` 描述一个**杜兴式微笑**（脸颊与嘴角同时激活）；这个模式本身并不能证明内心情绪

只用 `AU12` 的笑读起来是*客套/勉强的*：眼睛没参与。这个区别对提示词里的“smile”是看不见的，用 FACS 指定却很简单。这就是为什么它适合**强挤的笑、压抑的表情、混合情绪和诡异感**：在这些情况里，*两个相似表情之间的差别*承载了意义。

FACS 被电影里的专业面部动画师使用；这里把它改用作 Seedance 2.0 的**提示词词汇**。

### 在仓库面部工具中的位置（Where it sits among the repo's facial tools）

分辨率递增的两层：

| 层 | 写法 | 粒度 |
|---|---|---|
| 行为通道 | `vocab.md` § Emotion as Visible Behavior — Channels（呼吸、下颌紧张、眼部行为……） | 情绪 → 可观察行为 |
| **动作单元（本模块）** | AU 代码 | 情绪 → **具名肌肉** |

通道是*行为*底层；AU 是*解剖*底层。一个具名表情如“安静的崩溃” = 一组通道组合（湿润发直的眼 + 紧绷的下颌）= 一组 AU 组合（AU1 + AU15 + AU17 + AU24）。具名表情太粗、你需要具体肌肉时，用 FACS。

---

## 来源与“不是保证”规则（Provenance and the "Not a Guarantee" Rule）

本模块里有两类不同的说法，要分开：

- **AU 词汇是标准科学。**哪个代码对应哪块肌肉，以及经典的情绪→AU 原型（EMFACS），是稳定、可引用的事实。把 AU 参考表和情绪配方当作可靠的。

- **Seedance 对 AU 代码的解读是 [EMPIRICAL]。**`seedance_2_0` 规格**没有 FACS 字段，没有表情枚举，没有任何面部相关的东西**（对照规格快照核实，2026-06-27）。所以“写 `AU12` 就得到笑”是*模型碰巧解读得好的提示词惯例*，不是文档记载的能力。实践者报告：成功率**高**，但**代码不保证**精确的表情，多个 AU 的提示可能渲染出大部分但不是全部单元。

**规则：**把 FACS 当作强有力的经验法则，让本仓库的迭代纪律（`higgsfield-prompt.md` § The Iteration Rule）在用户自己的素材上确认它。与 Seedance 提示词写作规律（`higgsfield-seedance.md` § Prompt-Craft Laws）属于同一类来源。绝不告诉用户 FACS 提示词是确定性的。

> 如果未来的 Seedance 规格加入了真正的面部/表情参数，规格漂移检查应该会发现它：届时需要更新的就是这里“模型没有字段”的说法。

---

## 先规划流程（The Plan-First Workflow）

最重要、也是实践者最常做错的纪律：

> **规划你需要的表情 → *只为这些*生成一张 FACS 表 → 把代码写进提示词。**

**不要生成完整的 49 个 AU 参考表再挑几个。**那明确是错误做法：要求渲染全部 49 个单元的表会把图像模型摊得很薄，标注读不清，而你为 45 个永远用不上的格子付了钱。只为这场戏需要的 3–6 个表情生成一张*小*表，身份一致性更好，标签也更干净。

三步：

1. **规划**：给这个镜头的情绪节拍命名。“她把恐惧伪装成安抚” → 恐惧（AU1+AU2+AU4+AU5）在一个强挤的笑（只有 AU12，没有 AU6）下面闪动。碰图像模型*之前*先定好 AU 组。
2. **生成表**（可选，但为了一致性推荐）：在真实角色上，只做这些表情的一张带标签的小网格。见 § Step 1。
3. **写提示词**：把代码写进 Seedance 提示词，镜头有时间结构时按节拍同步。见 § Step 2。

表是**可选的**。代码在没有任何图像的文生视频提示词里也有效（实践者只用代码生成过整段视频）。当你需要*这个角色*的脸跨镜头保持一致时才生成表。

---

## 第 1 步：生成 FACS 参考表（Step 1 — Generate the FACS Reference Sheet）

FACS 表是一张**带标签的网格图**：角色的脸在每个目标表情下，标注着它的 AU 代码，用作身份 + 表情参考。这是一项参考表图像任务；图像模型的机制在 `higgsfield-gpt-image-2.md`（Format A：结构化网格）和其附属文件 `higgsfield-gpt-image-2-reference-sheet-workflow.md`。本节负责 **FACS 专用**的提示词。

**模型：**GPT Image 2 和 **Nano Banana Pro** 都可以；Nano Banana Pro 通常读起来更干净。标注有时读不清：**迭代**。

### 表的提示词（把角色和 AU 清单参数化）（The sheet prompt (parameterize the character + the AU list)）

上传角色图，然后给图像模型提示。替换角色描述，**把 AU 清单删到只剩你规划的单元**：除非真的需要，不要把 49 个全贴进去：

```
Create a clean educational FACS Action Unit expression grid featuring
[CHARACTER — e.g. a realistic adult female character]. Use minimal studio
lighting, neutral white background, high readability, professional facial
anatomy reference-sheet aesthetic, realistic skin texture, consistent identity
across all panels.

COLOR SYSTEM: soft pastel color coding by category, sheet kept minimal and
elegant —
  Forehead & Brow AUs: soft pastel blue
  Eye & Eyelid AUs: soft pastel lavender
  Nose & Cheek AUs: soft pastel peach
  Lip & Mouth AUs: soft pastel pink
  Head Movement AUs: soft pastel mint
  Eye Direction AUs: soft pastel cyan
  Special / Misc AUs: soft pastel beige
Apply color subtly: panel background tint, thin borders, small label accents.
Keep colors soft, muted, professional.

Include these Action Units (one captioned panel each):
[PASTE ONLY THE AUs YOU PLANNED — e.g.
  AU6 Cheek Raiser, AU12 Lip Corner Puller, AU1 Inner Brow Raiser,
  AU4 Brow Lowerer, AU15 Lip Corner Depressor]
```

（可选取的完整类别→AU 清单在下文 § AU Code Reference。）这张表是带文字标注的研究用图，不是项目角色资产；角色资产组板仍按 [角色资产交付规范](template-character-asset-delivery.md) 制作。

### LLM 可能标错 AU：要核对（The LLM can mislabel AUs — verify）

图像模型是*一个 LLM*：它可能把错误的肌肉放在一个代码下面。流传的样表把鼻孔扩张标为 **`AU82`**，而标准 FACS（以及实践者自己的对白示例）对同一动作用 **`AU38`**；`AU8`（双唇相互靠拢）出现在真实提示词里，却完全不在那张表上。把任何自动生成的表当作*草稿*：对照 § AU Code Reference 表和可信的外部参考（如 **melindaozel.com/facs-cheat-sheet 的 FACS 速查表**）检查各个格子。这种标错风险，是规划一张*小而可核对*的表、而不是相信一张 49 格大杂烩的最有力理由。

---

## 第 2 步：把 AU 代码写进 Seedance 提示词（Step 2 — Put AU Codes in the Seedance Prompt）

选好之后，可选的 AU 跟在相应的计时可见行为后面。根入口的工作室块结构契约和实际的模型/模式优先；下面的 Seedance 2.0 示例不是通用的平台要求。FACS 只细化面部描述。工作室格式里，AU 写在 `[具体情节]` 各段的 `表情：` 行。

### 两种写法：两种都试（Two specification styles — test both）

| 写法 | 看起来像 | 何时用 |
|---|---|---|
| **只写代码** | `AU10, AU20, AU27, AU45` | 节拍清单、密集的节拍表；实践者这样跑过整段视频，模型对大多数单元解读得很好 |
| **代码 + 简短解剖描述** | `AU6 (cheek raiser, orbicularis oculi tightens, crow's feet) + AU12 (zygomaticus pulls corners up)` | 某个单元总被漏掉时；描述给模型第二个冗余信号 |

没有一种总是更好。**在你的素材上两种都试**：只写代码更简洁、常常就够了；模型总丢的单元再加描述。

### 硬限制（The hard limits）

旧标题并不让 AU 数量成为平台限制：下面是可选的复杂度指引、参考选择和场景语境检查。

- **3–4 个表情是补救经验，不是硬上限。**叠太多 AU 请求会降低遵循度。测试显示过载时，减少相互竞争的线索，或给必要的弧线更多时间/镜头覆盖；保留它的因果展开。下面 14 个节拍的例子是一次表情研究，它短而单一的节拍可能只渲染出一部分，不是容量保证。
- **角色照片是可选的。**没有图像（文生视频）代码也能起作用。只有需要*这个角色*的身份跨镜头保持一致时才附 `@Image1`：它改变的是一致性，而不是 AU 是否生效。
- **仍然要描述一个场景，而不只是一张脸。**Seedance 的过滤器读取整个场景的意图（`higgsfield-seedance.md` § The Filter Model）。保留构图/光照/情绪槽位：一份没有场景的裸 AU 清单太单薄。下面的例子都带了 Style/Mood 头就是这个原因。

### 按节拍同步的结构（Beat-synced structure）

有时间结构的表演，给每个节拍一个编号或一个时间区间，以及它的 AU 组：

```
1: AU10
2: AU20
3: AU22
4: AU45
```

或者带时间区间和描述：

```
2-4s: Happy — AU6 (cheek raiser, crow's feet) + AU12 (lip corners up), Duchenne smile
4-6s: Sad — AU1 (inner brow raise) + AU4 (brow knit) + AU15 (lip corners down)
```

每个节拍的时间标签遵循与任何多节拍 Seedance 提示词相同的时长算术（`higgsfield-seedance.md` § Runtime arithmetic）：节拍必须覆盖声明的时长，包括继承的停留。在这些近景研究里，把节拍表标为**一个连续镜头内的表情节拍**，而不是硬切。固定镜头或缓慢推近是一个选项；实际的构图和运镜路径跟随事件和用户指令。

---

## AU 代码参考（AU Code Reference）

来自标准表的动作单元，按面部区域分组。用来写表的提示词，以及核对自动生成表的标签。

### 前额与眉（Forehead & Brow）
| 代码 | 动作 |
|---|---|
| AU1 | 内眉上提（Inner Brow Raiser） |
| AU2 | 外眉上提（Outer Brow Raiser） |
| AU4 | 皱眉/眉下压（Brow Lowerer） |
| AU71 | 眉间沟（Brow Furrow） |
| AU72 | 眉部隆起（Brow Bulge） |

### 眼与眼睑（Eye & Eyelid）
| 代码 | 动作 |
|---|---|
| AU5 | 上眼睑上提（Upper Lid Raiser） |
| AU7 | 眼睑收紧（Lid Tightener） |
| AU41 | 眼睑下垂（Lid Droop） |
| AU42 | 眯成缝（Slit Eyes） |
| AU43 | 闭眼（Eyes Closed） |
| AU44 | 眯眼（Squint） |
| AU45 | 眨眼（Blink） |
| AU46 | 单眼眨（Wink） |

### 鼻与脸颊（Nose & Cheek）
| 代码 | 动作 |
|---|---|
| AU6 | 脸颊上提（Cheek Raiser） |
| AU9 | 皱鼻（Nose Wrinkler） |
| AU11 | 鼻唇沟加深（Nasolabial Deepener） |
| AU82 | 鼻孔扩张（Nostril Dilator） |
| AU83 | 鼻孔收缩（Nostril Compressor） |

### 唇与口（Lip & Mouth）
| 代码 | 动作 |
|---|---|
| AU10 | 上唇上提（Upper Lip Raiser） |
| AU12 | 嘴角上提（Lip Corner Puller） |
| AU13 | 嘴角尖拉（Sharp Lip Puller） |
| AU14 | 酒窝（Dimpler） |
| AU15 | 嘴角下压（Lip Corner Depressor） |
| AU16 | 下唇下压（Lower Lip Depressor） |
| AU17 | 下巴上提（Chin Raiser） |
| AU18 | 撅嘴（Lip Pucker） |
| AU20 | 嘴唇横拉（Lip Stretcher） |
| AU22 | 嘴唇呈漏斗状（Lip Funneler） |
| AU23 | 嘴唇收紧（Lip Tightener） |
| AU24 | 嘴唇压紧（Lip Pressor） |
| AU25 | 双唇分开（Lips Part） |
| AU26 | 下颌下落（Jaw Drop） |
| AU27 | 张大嘴（Mouth Stretch） |
| AU28 | 抿唇吸入（Lip Suck） |
| AU84 | 舌头上抬（Tongue Up） |
| AU85 | 伸舌（Tongue Out） |

### 头部运动（Head Movement）
| 代码 | 动作 |
|---|---|
| AU51 | 头向左转（Head Turn Left） |
| AU52 | 头向右转（Head Turn Right） |
| AU53 | 抬头（Head Up） |
| AU54 | 低头（Head Down） |
| AU55 | 头向左歪（Head Tilt Left） |
| AU56 | 头向右歪（Head Tilt Right） |
| AU57 | 头前伸（Head Forward） |
| AU58 | 头后仰（Head Back） |

### 视线方向（Eye Direction）
| 代码 | 动作 |
|---|---|
| AU61 | 眼向左转（Eyes Turn Left） |
| AU62 | 眼向右转（Eyes Turn Right） |
| AU63 | 眼向上（Eyes Up） |
| AU64 | 眼向下（Eyes Down） |

### 特殊 / 其他（Special / Misc）
| 代码 | 动作 |
|---|---|
| AU81 | 咀嚼（Chewing） |

> **编号说明。**流传的表上有些代码相对标准 FACS 是**非标准或被重新分配的**：尤其是 § Step 1 提到的鼻孔扩张 AU82（标准为 AU38）、AU71/AU72 的眉部代码，以及 AU82–AU85 这一段。标准 FACS 也有这张表漏掉的代码（例如真实提示词里用到的 `AU8` 双唇相互靠拢）。用这张表时按*这张表的*约定，但某个代码的表现让你意外时，对照 melindaozel.com/facs-cheat-sheet 交叉核对。

---

## 情绪 → AU 配方（Emotion → AU Recipes）

用户问“愤怒 / 恐惧 / 厌恶用哪个代码”时，这些是标准的 **EMFACS 情绪原型**：行为科学为每种基本情绪对应的标准 AU 组合。作为配方是可靠的；Seedance 对它们的*渲染*仍是 [EMPIRICAL]。

| 情绪 | 核心 AU | 读作 |
|---|---|---|
| **高兴（真诚 / 杜兴）** | AU6 + AU12 | 眼睛参与的笑，有鱼尾纹 |
| **高兴（客套 / 勉强）** | 只有 AU12（无 AU6） | 嘴在笑，眼睛没有：诡异/勉强的笑 |
| **悲伤** | AU1 + AU4 + AU15 | 斜眉，嘴角下垂 |
| **惊讶** | AU1 + AU2 + AU5 + AU26 | 眉上扬，眼睁大，下颌下落 |
| **恐惧** | AU1 + AU2 + AU4 + AU5 + AU7 + AU20 | 眉上扬又皱，眼睁大，嘴唇横拉 |
| **愤怒** | AU4 + AU5 + AU7 + AU23 | 眉下压，硬瞪，嘴唇收紧 |
| **厌恶** | AU9 + AU15 + AU16 | 皱鼻，嘴角下压 |
| **轻蔑** | AU12 + AU14（单侧） | 单侧冷笑 |

**混合出细腻。**有意思的表情是*混合*：一张强装温暖的面具，是真笑的肌肉（AU6+AU12）在同一帧里和恐惧的肌肉（AU1+AU7）对抗；“苦涩的好笑”是没有 AU6 的 AU12 加一点 AU4。混合时列出两种情绪的 AU，让冲突被读出来：这是用 FACS 做出“憋住的笑”“强作镇定”这类具名微表情的路径。

---

## 物理微节拍：脸以外的身体（Physical Micro-Beats — the Body Beyond the Face）

`[OFFICIAL — Higgsfield shotlist-builder skill, 2026-07; re-authored from the Chinese source]`：AU 代码止于脸。制作中的表演指导把同样肌肉级的纪律延伸到**喉、呼吸、皮肤和姿态**。这些配方和 AU 代码一起（或代替它）放进提示词的表演描述里（工作室格式：`[具体情节]` 各段的 `动作：`/`表情：`/`听者：` 行）。

**这些是菜单，不是清单。**只挑表达当前触发、且在所选景别下看得见或听得见的线索。**2–4 个破绽**是可选示例，不是下限也不是上限；面部 AU 经验不给身体动作设配额。保留完整的动作/反应链，挑有意义的呼吸或微表情细节，不加每秒一个的节拍表：

| 语域 | 身体配方 |
|---|---|
| **愤怒 / 决心** | 下颌咬肌明显搏动 · 颈部可见颈动脉跳动 · 太阳穴青筋鼓起 · 重读的词上鼻孔张开 · 瞳孔收紧 · 外眼角变硬（真正的强度，不是廉价的眯眼）· **高潮处不眨眼** · 眉间和鼻翼细密的汗珠 |
| **焦虑 / 紧张** | 一次看得见的吞咽（喉结）· 台词前一次短浅的鼻吸 · 舌头润一下干的下唇 · 下唇微微内收 · 脸颊泛起毛细血管的红 · 关键词上瞳孔放大 |
| **不流泪的悲伤** | 外眼角下垂 · 眼睛湿润有光，**但从不溢出** · 眉间皱眉肌收紧 · 嘴唇轻微颤抖 · 头下沉几度 |
| **掌控 / 平静 / 优越** | 均匀稳定的呼吸（与紧张的对手形成对比）· 放松的手指 · 缓慢刻意的眨眼 · 下巴微抬 · 杜兴微笑**逐渐**形成，绝不一上来就是完整的笑 |
| **沉重 / 被压着** | 肩下沉 · 头微低 · 深而慢的呼吸 · 回答时头微歪 5–15° |
| **震惊 / 僵住** | 在触发处可选的短暂静止（0.3–0.5 秒是一个例子，不是固定时长）· 看得见时瞳孔放大 · 嘴唇无声地分开 · 僵住解除时延迟的一次急吸 · 视线停在触发物上 |
| **压抑的情绪**（最难） | 写成*身体上的抵抗*：每块面部肌肉都在对抗涌上来的情绪 · 咬肌缓慢收紧 · 一次延迟而费力的吞咽 · 眼睛逐渐湿润到发亮，眼泪始终不落 · 一次缓慢、深长、受控的吸气，胸口明显起伏 · 下颌颤一下，立刻又咬紧 |

**防止 AI 视频破绽的默认做法：**

- **除非剧本明确要求，否则不流泪**：湿润有光是默认的悲伤读法。
- **匹配已批准的表演风格。**克制的作品里避免无动机的鬼脸；已确立的风格化/卡通表情成立（stylized/cartoon expression is valid when established）。点名注意的对象，而不是加泛泛的翻眼来表现思考。
- **给说话者和听者一个任务。**一个有意义的停住的姿势或视线可以承载它；不需要持续的微动作。
- **反应跟随感知和动机。**按距离、信息和角色改变起始时间和强度。0.3–0.5 秒的错开（`"Roko turns first; 0.4s later, Rein; another 0.4s, Jax"`）是可选示例，不是时间规则；刻意的同步表演仍然可用。
- **虚化里的听者保留行为。**用可读的头/肩朝向、姿态或由事件驱动的反应；不要给完全虚化或远处的人物规定看不见的瞳孔或面部细节。

**反 AI 测试。**交付前重读表演描述，问：*这可能来自一个提示词模板吗？还是读起来像一个看过演员排练的导演的笔记？*读起来像模板，就重写：微节拍应该感觉是观察出来的，而不是生成出来的。

---

## 对白与独白的面部表演（Dialogue & Monologue Facial Acting）

FACS 重要的原因：孤立的面部表情只是小把戏；价值在**说话时的表演**：近景独白和对白里，脸承载着台词没说出的潜台词。强挤的笑、漏出来的恐惧、说话时的混合情绪，都落在这里。

### 结构（The structure）

**每个说话节拍一组 AU**，与正在说的台词对齐：

```
Beat 1 (0-1s): AU5 + AU38 (upper lid raiser + nostril dilator — genuine fear, pre-dialogue)
Beat 3 (2-4s): AU12 (lip-corner pull — attempted reassuring smile; cheeks remain restrained) — delivers "everything's fine"
Beat 5 (5-6s): AU7 (lid tightener — eyes betraying the fear the smile hides)
Beat 7 (8-10s): AU4 + AU24 (brow lowerer + lip presser — seriousness cracking through)
```

技艺在于**一个节拍内的对比**：嘴在表演安全（AU12），眼睛却漏出恐惧（AU7），观众同时读到两者。**1–2 个 AU** 是为了清楚可读的可选起点，不是每个节拍的上限，也不是必须的代码数。

### 每句台词都有三个节拍（Every line gets three beats）

`[OFFICIAL — shotlist-builder]`：把准备、说出和余波当作连续的表演来考虑。写出这句台词和听者需要的变化；这不是三个必须的新手势，也不是分别计时的节拍：

- **台词前**：第一个字之前发生的事：一次吞咽、一次吸气、舔一下唇、一次姿态变化。
- **台词中**：哪些词承载重音，通过什么：鼻孔张开、语调、瞳孔移动。
- **台词后**：随之而来的视线、呼吸或身体状态带进下一个回应。约 0.5 秒的停留是一个例子；重叠、即时回答和更长的评估跟随实际的对白和事件。

> 台词前：一次短促的鼻吸，一次看得见的吞咽。
> 台词：“Don't ask me again.”：重音落在 *again* 上，说到这个词时鼻孔张开。
> 台词后：视线锁住对手 0.5 秒，然后飘开。

### 与音频和口型组合（Combine with audio + lip-sync）

对白 FACS 提示词自然地与音频条件层配合：

- 在工作室块结构视频稿里，台词写进 `[声音]` 的计时行（`6s-9s｜说话人＋状态＋说：{line}`）；`[具体情节]` 的对应段承载 AU 级面部线索。**`[AUDIO: Xs]` 脚本块**只用于明确选择、且支持它的原生/短格式流程。音频和口型由实际模型/模式决定；引用台词和写 AU 都不能保证嘴部同步（neither quoting dialogue nor writing AUs guarantees synchronized mouths）。
- 紧凑的近景加一个强的 `@Image1` 身份参考，有助于检查或修复口型（音频模块的 Lip-Sync Rules）。服务于场景时用这种覆盖；更宽的对白镜头仍然成立，用可读的线索。
- 说话节拍里，FACS 节拍表只写眉/眼/脸颊单元；让音频驱动说话时嘴唇/下颌的形状，明确的嘴唇/下颌 AU（AU12、AU15、AU24）留给*表现性*的叠加，而不是音素。

---

## 完整示例（Worked Examples）

三个例子都由实践者的提示词轻度整理而来。生成前先跑预检 lint（`python3 scripts/seedance_lint.py --preflight --model seedance_2_0 "<prompt>"`）。这些是 Seedance 2.0 原生格式的表情研究；工作室完整视频仍编译成块结构，对白写进 `[声音]` 的计时行。

### A：按节拍同步的表情扫描（只写代码）（A — Beat-synced expression sweep (codes-only)）

```
**Model:** Seedance 2.0
**Aspect ratio:** 1:1   **Duration:** 15s

Use the provided character @Image1 as the fixed identity reference.
Cinematic tight close-up, subtle neutral background, high facial clarity, slow
micro push-in, shallow depth of field. 14 beats, beat-synced:

1: AU10   2: AU20   3: AU22   4: AU23   5: AU27   6: AU28   7: AU45
8: AU53   9: AU61   10: AU62  11: AU64  12: AU85  13: AU84  14: AU46

Uneasy, hypnotic, controlled mood.

**Camera:** slow push-in
```

（只写代码，每个节拍一个 AU：预期大多数能落地，有些只部分实现；这是文档记载的表现，不是靠过度提示去修的失败。）

### B：情绪弧线（代码 + 解剖描述）（B — Emotion arc (codes + anatomical description)）

```
**Model:** Seedance 2.0
**Aspect ratio:** 16:9   **Duration:** 15s

**Style & Mood:** photoreal, face and shoulders only, bare skin no makeup, soft
diffused light, plain white background, shallow depth of field.

Timeline:
0-2s: Neutral resting face, eyes forward, relaxed brow and lips.
2-4s: Happy — AU6 (cheek raiser, crow's feet) + AU12 (lip corners up and out),
  Duchenne smile, slight eye squint from cheek push.
4-6s: Sad — AU1 (inner brow raise, oblique brow) + AU4 (brow knit) + AU15 (lip
  corners down), eyes slightly glassy.
6-8s: AU61 then AU62 — gaze shifts left, then right, head still.
8-11s: AU46 left wink, then AU46 right wink, subtle smirk between.

**Camera:** static medium close-up
```

### C：伪装成安抚的恐惧（对白 + FACS 节拍）（C — Fear masked as reassurance (dialogue + FACS beats)）

```
**Model:** Seedance 2.0
**Aspect ratio:** 16:9   **Duration:** 15s

Use the provided character @Image1 as the fixed identity reference.
Dim interior, single warm lamp, slight low angle, handheld micro-sway, shallow
depth of field.

[AUDIO: 0s] "Hey, hey — everything's fine, okay? We're just gonna play a game
where we stay really quiet. Can you do that for me?"

Beat 1 (0-1s): AU5 + AU38 (upper lid raiser + nostril dilator — genuine fear, pre-dialogue)
Beat 2 (1-2s): AU45 (blink — composing the mask)
Beat 3 (2-5s): AU12 (attempted reassuring smile; cheeks remain restrained) — "everything's fine, okay?"
Beat 4 (5-8s): AU2 + AU12 (smile + outer brow raise — performing fun) — "we're just gonna play a game"
Beat 5 (8-10s): AU4 + AU24 (brow lowerer + lip presser — seriousness cracking) — "where we stay really quiet"
Beat 6 (10-15s): AU6 + AU17 + AU1 (eyes smiling while chin trembles, desperation) — "can you do that for me?"

Devastating contrast between performed safety and visible terror — the face never
fully commits to either; the audience reads both at once.

**Camera:** handheld micro-sway, slow push-in
```

> 这个节拍结构的模板版本：`template-facs-expression-beats.md`。

---

## 相关模块（Related Skills）

- `higgsfield-seedance.md`：每条 FACS 提示词作为限定范围的旧词汇所使用的基础提示语法（完整视频的版式以工作室块结构契约为准；§ Voice Rewrite 的“写物理不写情绪”，FACS 是它在肌肉层面的情况）
- `higgsfield-audio.md` § Audio as a Conditioning Input：对白 FACS 用的 `[AUDIO: Xs]` 块和口型
- `higgsfield-gpt-image-2.md`：FACS 表用的 Format A 参考表图像机制
- `vocab.md` § Emotion as Visible Behavior — Channels：AU 词汇的行为层同类
- `template-facs-expression-beats.md`：按节拍同步的 AU 节拍表模板
