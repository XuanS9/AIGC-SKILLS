# Seedance 2.0 失败模式参考（Seedance 2.0 — Failure Modes Reference）

Seedance 输出失败的具名目录：每种失败的原因，以及提示词侧的修法。生成结果落进一个可辨认的模式、而不是随机失手时查阅。本文件属于 Seedance 2.0 历史资料，但大多数模式对 2.5 同样适用；工作室验收按 [统一调用与验收总表](production-checks.md#统一调用与验收总表) 的四态记录。

---

## 怎么使用这份参考（How to use this reference）

下面每个条目都用同样的四个字段：

- **症状**：用户在输出里看到什么。
- **机制**：Seedance 为什么产出这种结果。
- **对策**：提示词侧的修法。
- **示例**：修法展示比描述更清楚时，给出具体的前后对比。

生成失败时，先扫章节标题找匹配的症状。没有匹配的，这个失败可能属于 `higgsfield-seedance.md` § When the User Is Already in a Failure Loop：那一节覆盖过滤器拒绝，而不是渲染失败。

---

## 帧率漂移与逐帧去重（FPS drift and frame-by-frame de-duplication）

**症状。**输出播放起来卡顿。在剪辑软件里逐帧检查，本该连续运动的地方出现重复的连续帧。要求 24 fps；把重复帧算进去，实际节奏接近 12–18 fps。

**机制。**Seedance 不总是遵守要求的帧率。在负载下或者动作密集的提示词上，它会降低有效帧率，用重复帧填充时间线来凑够要求的时长。重复帧就是破绽。

**对策。**两层，按顺序：

1. 在提示词正文里明确写出帧率，而不只是在元信息头里：`The video runs at 24 fps. No frame is repeated.` 把帧率锚定在动态描述里，能提高输出正确的比例，但不能让它确定。
2. 输出仍然漂移、而这段片子只是作为空镜（不是主镜头）时，在剪辑软件里逐帧去重：删掉重复帧，重新插帧，把结果当作连接素材。主镜头留着重新生成。

逐帧去重是退路，不是修法。落在 12 fps 的主镜头仍然是坏的；重新生成。

---

## 逐帧审查是必须的（Frame-level review is mandatory）

**症状。**一段 Seedance 片子全速看没问题，但其中一个坏帧在播放时毁掉了剪辑：一只闪烁的手、一张扭曲的脸、一个放错位置的物体，只有暂停时的眼睛才能抓到。

**机制。**Seedance 的输出是生成的，不是拍摄的。和胶片素材里镜头光学约束了每一帧能包含什么不同，AI 片子每一帧的状态是独立的，可能在某一帧毫无预兆地漂移。一段 24 帧的片子是模型串起来的 24 次独立生成。

**对策。**在剪辑软件里逐帧审查之前，把每段 Seedance 片子都当作不可信的。用 J/K/L 拖动或方向键逐帧走；一个坏帧就足以淘汰这条素材。把逐帧审查的时间算进迭代预算：一段 10 秒的片子，每遍大约需要 30–60 秒仔细拖看。

---

## 抢救失败的生成（Failed-generation salvage）

**症状。**一次生成在素材层面被淘汰：运镜不对、动作垮了、构图在镜头中途坏了。第一反应是丢掉重新生成。

**机制。**一次“失败”的 Seedance 生成，很少在 10 秒时长里全部失败。模型经常在一段本要丢弃的片子里产出 1–3 秒可用的素材：运镜漂移之前干净的开头、动作垮掉之前干净的中段、接近结尾的一个可用插入镜头。

**对策。**丢弃之前，拖看被淘汰的素材，用入点/出点标出可用的段落。剪出来存好。从“失败”生成里留下的 2 秒插入镜头，常常能作为连接素材放进另一场戏，或者在原镜头里撑住一个反应节拍。

从失败素材里挖出可用的几秒，在整个项目里会累积：那部 90 分钟的戛纳长片，光靠抢救的剪辑就交付了可观的时长。

---

## NSFW 误判（提供方侧）（NSFW false-positive (provider-side)）

**症状。**一条没有 NSFW 内容的提示词被当作 NSFW 拒绝。IP 检查那部分通过了；只有 NSFW 分类器触发。

**机制。**Seedance 的 NSFW 分类器在提示词文字和中间生成标记上运行。身体部位的具体描述、某些服装词汇，以及一些带感官色彩但干净的措辞，即使内容无害也可能触发分类器。分类器是概率性的，调得偏保守；误判是它运行特性的一部分。

**对策。**改写提示词：

1. 去掉或泛化身体部位的具体描述（`her bare shoulders` → `her shoulders`；`tight-fitting dress` → `fitted dress`）。
2. 把感官语域的形容词换成中性的对应词（`sultry` → `composed`；`seductive` → `direct`）。
3. 把改写后的提示词跑一遍 `higgsfield-seedance.md` § Pre-flight Linter 里的预检 lint，抓出其他风险词。

不要不加改动地重新生成同一条提示词：同样的文字会触发同样的分类器。反循环纪律见 `higgsfield-seedance.md` § When the User Is Already in a Failure Loop。

---

## 关键帧一致性逼出编造（Keyframe-consistency forces invention）

**症状。**提示词要求一个元素出现或移动（`the character pulls a Polaroid off the fridge`），但源关键帧里没有这个元素。Seedance 照样产出这个动作，编造元素的位置：常常放在和场景其他几何矛盾的地方。

**机制。**Seedance 把源关键帧当作世界里有什么的强锚点。提示词要求一个关键帧里没有的元素时，模型得同时制造元素**和**它的位置，而位置常常漂到模型能塞进去、又不覆盖其他参考内容的地方。

**对策。**明确写出缺失，让模型知道它被要求的是添加，而不是匹配：`The Polaroid is not visible on the fridge in image 5; it appears in this shot when the character lifts their hand from below the frame.` 这句明确的“参考里没有”告诉模型，源关键帧和目标输出在这个元素上是刻意不一致的，于是模型会有意地编造位置，而不是作为退路。工作室中文稿写成正向：“这张照片在本段开始时位于画面下方，人物抬手时进入画面。”

---

## 物理状态锚点（Physics-state-anchor）

**症状。**相邻物体移动时，一个实物的表现不对：角色从冰箱上取下拍立得时，磁铁跟着拍立得飞走；角色端起碟子时杯子倒了；角色转头时帽子飘起来。相邻物体的物理违例。

**机制。**Seedance 没有强制的物理模拟。两个物体在源画面里视觉上相邻时，模型可能把其中一个的运动理解成两个都在动，尤其是在快速运镜或动作密集的提示词下。

**对策。**明确写出不变量。在提示词里加一句点明什么保持不动：`The magnet stays attached to the fridge surface throughout. Only the Polaroid moves.` 物理锚点读作软约束，不是硬性保证：但点明不变量后，相邻物体的漂移会明显下降。

---

## 动作倒放填充（Action-reversal fill）

**症状。**提示的动作在前几秒就完成了，片子剩下的部分把它倒放回来：角色向前走，然后退回起点；俯身，然后后撤；伸手，然后缩回。读起来是没有动机的一来一回。运镜版本：一个没写目的地的运动，到达之后又沿原路漂回去。

**机制。**一个短动作在片子结束之前就完成了，而模型还有几秒时间线要填。提示词里没有进一步的指示时，与场景一致的最便宜的延续，就是把它已经渲染过的运动倒着跑一遍。`[EMPIRICAL — dramaclaw production corpus, Seedance]`；这是与模型无关的图生视频行为，不是 Seedance 的规格。

**对策。**给运动足够的材料，让它把整段片子花在一个方向上：沿同一方向串起 2–3 个相连的动作（走到窗边、拉开窗帘、靠向玻璃）。如果故事需要一来一回，那是两个镜头，不是一条提示词。运镜要写明终点：说明运动结束时画面里是什么。完整说明：`higgsfield-seedance.md` § Prompt-Craft Laws → Motion-prompt laws。

---

## 短台词上的填充嘀咕（Filler-babble on a short dialogue line）

**症状。**单人镜头里的一句短台词，回来时被编造的嘀咕包着：台词前后有含糊的伪语音，或者台词被说了两遍。这是从文字稿评分的，所以这是**音频**症状；嘴是否也一直在动，下面的测试没有评分，这里也不作声称。

**机制。**音频分支会填满空白时间，就像 § Action-reversal fill 把剩下的运动时间花掉一样。一句远早于片子结束就说完的台词留下一个安静的窗口，而与镜头一致的最便宜的延续，就是用同一个声音发出更多像说话的声音。`[MEASURED — sync-budget ladder, 2026-08-09, EN × 4s × 480p × Seedance 2.0]`：≤6 个词的每一条都带了它；8 个和 12 个词的台词 4/4 都干净。风险方向是**短**台词，不是长台词：到 12 个词（约每秒 3 个词）都没观察到截断。

**对策。**给空白时间一个任务，而不是把选择留给模型，并写明每张可见的脸的嘴部状态：

1. **填满窗口。**在 4 秒镜头里把台词延长到大约 8 个词以上，或者把镜头剪到台词的长度。
2. **把安静写出来。**如果台词必须短，写出窗口剩下的部分被什么占据：一个具名的停顿节拍、一个环境声或音效事件、覆盖台词前后空档的动作描述。
3. **一个说话人，一句台词，说一次。**说话的角色说这句台词，别的什么都不说；完整的音频块写法在 `higgsfield-seedance-hell-grind.md` § Dialogue construction。承载想法而不是台词的节拍在那里标为 `INNER (unspoken)`，让它完全不进嘴里。
4. **其他每张可见的脸都给一个正向的静止嘴部事实。**画面里没标注的嘴，模型可能会认为它在说话。把静止状态写成*为真*的东西：“嘴唇放松”、“下颌闭合，呼吸抬起胸口”、“看着说话的人，嘴不动”：绝不写成否定（`higgsfield-seedance.md` § Prompt-Craft Laws → No negative prompts in the prompt body）。注意“listens without speaking”读起来是正向的，但带着 *without*，所以触犯同一条规律；优先用上面的形式。

**示例。**一个 4 秒的双人镜头，带一句剧本台词：

❌ `AUDIO — MIRA (dry, clipped): "It's gone."` 窗口大部分没写，画面里的第二张脸完全没有嘴部状态。

✅ `AUDIO — Diegetic only: rain on the skylight, one door latch at 3.4s. MIRA (dry, clipped) says her line once and nothing else: "It's gone, and it took the ledger with it." DEV keeps his eyes on her — lips at rest, jaw closed, his breath lifting his chest.`

工作室格式的对应写法：台词写成 `[声音]` 里覆盖整个窗口的计时行，空档写音效计时行；听者的静止嘴部状态写进 `[具体情节]` 对应段的 `画面：` 行。

改写台词是测量过的那一半：它填满了窗口。第二个角色的静止嘴部事实是**没测量过**的那一半：它是第二张脸没法排除在镜头外时提示词侧的处理，还没在这里实测过。一次 480p 的单次 A/B（两个角色、一句短台词、有/没有嘴部事实）就能确定。

---

## 被截断的动作：切点落在结果之前（Truncated action — the cut lands before the result）

**症状。**分镜表读起来覆盖完整，片子里却什么都没落地。切镜来时盖子还在合上，手还在伸，门还半关着。段落里的每个动作都是一次尝试；没有一个是结果。快切段落最常带这个问题，而且它能通过审查，因为每个单独的镜头看起来都对。

**机制。**镜头按它*包含*什么来定价，而不是按什么必须在里面*完成*，所以模型把时长花在接近上，完成落到了边界之外。提示词里没有说镜头结束之前必须看到哪个状态，所以任何一帧都和其他帧一样适合作为停止点。`[HOUSE — technique re-derived from the nutllwhy/seedance-tvc-director evaluation, MIT, 2026-08-09. UNPROVEN HERE: not A/B'd on our material.]`

**对策。**把完成状态写成一个可见的事实，并让它在任何别的事发生之前稳定下来：*盖子严丝合缝地合上并停在那里*、*杯子落定在木头上*、*她的手完全握住把手*。节奏确实需要更早切时，让**下一个**镜头以已经成立的结果开场（笔记本已经合上、房间已经暗了），让段落继承切镜跳过的东西。来源在切镜前把完成状态保持大约 0.15–0.35 秒；把它当作倾向的方向，而不是测量值。

这条规律的音频孪生已经在本仓库里了：一句台词钉得早，让切镜继承一个尾巴（§ Filler-babble，以及 OSIDE 的 `dialogue-no-handle`）。这是同一条规律用在画面上。

---

## 空手比划：手在动，物体不动（Mimed manipulation — hands move, the object does not）

**症状。**角色打开、撕开、倒、按或者摊开某样东西，而物体从不变化：手指在一个始终密封的包装上逼真地动着，一个瓶盖从不破封，一个表面从不起皱。读起来像演员在没有道具的情况下排练。

**机制。**操作被写成了它的动词（*tears it open cleanly*、*twists the cap off*），这给了模型一个手势而没有机制。没有写明结构、锚点和材料的反应，手势就是它唯一能渲染的部分。`[HOUSE — re-derived from the same evaluation. UNPROVEN HERE.]`

**对策。**按顺序写出因果链：

1. **初始结构**：接触之前物体是什么样（顶边密封、盖着盖子、满的）。
2. **锚点**：什么把它固定住、怎么固定（另一只手握着包装的主体，底座平放在台面上）。
3. **力**：力作用在哪里、朝哪个方向（拇指和食指在撕口处，横向拉）。
4. **材料反馈**：材料可见地做了什么（薄膜从撕口处分开，包装被握住的地方起皱）。
5. **完成状态**：完成时什么为真（一个连续的开口，里面的东西可见，撕下的条脱离包装）。

随它一起的两条路由规则。如果这个操作只是*把我们带到*下一个状态，而不是镜头的重点，就改用两个状态加一个声音：密封的包装、画外听到一声撕开、手已经在里面了；更便宜，而且不会这样失败。并且绝不编造参考里显示不了的结构：如果撕口、封口或卡扣在你手上的素材里看不见，就在画外打开它、剪开它，或者实拍。

不要在一个镜头里叠加清晰的品牌正面、双手操作和强烈特效：操作镜头证明机制，另一个镜头证明标签。

---

## 群像镜头里的无主肢体（Orphan limbs in a group shot）

**症状。**三个或更多角色，一只手进入动作，后面没有身体：一只袖子横过另一个角色的胸口，一条从画外伸进来、没有肩膀的前臂，一只没人认领的多余的手。与之相邻的：人数在切镜之间变化，或者两个邻座在远景和近景之间互换位置。

**机制。**没有顺序锁定时，模型在每次切镜时重新推导群体，而不是把一个群体带下去。伸手是它暴露的时刻，因为手是画面里必须属于某个人的最小的东西。`[HOUSE — re-derived from the same evaluation. UNPROVEN HERE.]`

**对策。**在动作之前锁定群体：精确的人数、从左到右的画面顺序、谁挨着谁：在每个取景里都保持。然后给每只进入动作的手一个主人：谁的手、哪只手、什么袖子、从画面哪一侧进入、回到哪里。每个镜头的手部动作最多两个角色；其他人在看。

镜头同时想要一个细节、两张脸和一次群体回顾时，那是三个镜头：一个对物体的固定插入镜头，最多两只能归属的手；一个对做出反应的邻座的双人镜头；然后一个静态的群体画面，手已经离开物体。一次连续的后拉给不了这三样。

**这不只是群像的失败：单人近景也会长出第三只手。**`[FIELD — Higgsfield Studio, RED FLAG breakdown, 2026-08-19]` 一个人撬锁的近景回来时多了第三只手，场景里没有任何别人可以认领它。机制是一样的（手是画面里必须属于某个人的最小的东西），但上面的顺序锁定不适用，因为没有顺序。**即使只有一个角色，解剖结构也需要明确的数量。**在每个手部近景里带上它：

```
There are only two hands in the frame, both belonging to the same person,
entering from the same sleeve.
```

注意它的形状：它写明了数量、归属，**以及进入点**。光有数量，仍然会让数量正确的一双手从两个方向进来。

---

## 多重运镜过载（Multi-motion camera overload）

**症状。**一个叠加了多种运动的运镜（手持 + 上升 + 推近 + 移焦）产出读不懂的结果。观众跟不住任何一种运动，因为三种同时在发生；镜头读作不稳定，而不是调度。

**机制。**Seedance 能把任何单一运镜渲染好；组合运动会考验模型在所有轴同时变化时把主体留在画面里的能力。观众侧的问题是独立的：即使渲染得干净，人的注意力也解析不了三种同时进行的运镜。

**对策。**每个镜头一个主导运动。需要两种运动时，把镜头拆成两次切镜，每次切镜用一种运动。剧本要求复合运动（`rise into a push-in`）时，用带时间的清楚顺序写出各个运动：`Camera rises from 0-3s, holds, then pushes in from 4-8s`：让模型把它们渲染成离散的阶段，而不是同时变化的轴。

多镜头拆分的机制见 `higgsfield-seedance.md` § Single-vs-multi-shot decision。

---

## 空间感知失败（Spatial-awareness failures）

**症状。**进门镜头的失败率比静态镜头高。走廊方向的镜头最后朝错了方向。角色穿过家具而不是绕过去。在空间信息写得不够时，模型会选空间上错的摆放。

**机制。**Seedance 从参考加提示词文字重建场景几何。参考没有显示提示词需要的精确几何（门前摄影机的位置、走廊的方向、绕过沙发的路径）时，模型会选一个看似合理的默认，而它常常和用户的预期不一致。

**对策。**在动作描述之前，用一个空间布局块锁定几何。明确写出：

- 镜头开始时摄影机在哪里（`Camera inside the room, facing the closed door`）。
- 相关的几何特征（`The couch sits between the character and the camera`）。
- 任何运动的行进方向（`The character walks around the couch from screen-left to screen-right`）。

完整的块结构见 `higgsfield-seedance.md` § Spatial Layout Block，逐主体的坐标词汇见 § Frame Coordinate System。工作室格式见 [空间布局](spatial-layout.md)。

---

## 走路是最难的特技（Walking is the hardest stunt）

**症状。**普通的走路以细小但明白无误的方式出错：人形**滑行**而没有重心转移，两只脚同时离地，或者同一只脚迈了两次。两个人一起走时会分开，或者一个人走到前面去。一个应该从楼梯井里升上来的人形一下子瞬移上来：或者楼梯口被删掉，砌成了实墙。

**机制。**`[FIELD — Higgsfield Studio, RED FLAG breakdown, 2026-08-19]` 行走是一个周期性的物理约束，而模型渲染的是走路的*样子*，而不是执行这个约束。画面没有强制的任何东西（交替、触地、两个行走者之间的关系、身体必须从里面出来的那个开口）都可以自由漂移。楼梯井的情况是极端：机制在**画外**，画面里没有东西把模型拴在它上面，最简单的解决办法就是把它删掉。

**对策。**把周期写成物理，而不是一项活动：

```
heel lands first, strict left-right alternation, one foot always on the ground
```

- **两人并排需要自己的锁定**：*“肩并肩，在一条纵深线上，两个头一样大”*：否则一个会漂到前面，这一对读起来像两次分开的走路。头的大小那一句，是防止它变成纵深变化的关键。
- **把入场写成带时长的物理**：*“一次一个看不见的台阶地被抬进画面，用两到三秒。”*并且**把画外的机制写成一个具名的、必须存在的物体**：一个被告知必须存在的开口，比一个模型仅仅推断出来的开口难砌掉得多。

**匹配的切镜会暴露一个更隐蔽的问题：运镜速度。**同一段走路的两个跟拍镜头回来时速度不同（“脚快，背慢”），逐镜头的描述抓不到这个，因为每个镜头单独看都没问题。像“镜头 9 的运镜速度等于镜头 10”这样的关系，要求的是两次生成都看不到的东西：每条提示词都是隔离的（`higgsfield-seedance.md` 里的 § Context isolation）。把**同一个绝对值**一字不差地写进两条提示词，让每一条自己就带着完整的指示：`the camera tracks alongside at a steady 5 km/h, matching their walking pace, 2 m from them`。两个镜头之间必须一致的任何东西，都是一个重复的共享绝对值：绝不是交叉引用。`[fix adopted from OSideMedia/higgsfield-ai-prompt-skill v3.38.0]`

---

## 分成独立片段生成的打斗，回来时卡顿（A fight generated as separate clips comes back choppy）

`[FIELD — Higgsfield Studio, RED FLAG breakdown, 2026-08-19]` 一段多招式的交锋，分成独立片段生成时剪不到一起。**每段片子都重新猜姿势和节奏**，所以身体在每个接点都复位，每次切镜都悄悄多了一个停顿：招式都在，打斗读起来仍像幻灯片。

三条对策，按收益从大到小：

1. **把片段帧链起来。**片段 N 的最后一帧成为片段 N+1 的第一帧，**动作在招式中途跨过切点**：而不是在两个招式之间的静止位置。在一个已完成的节拍上接链，读起来仍然是一次停顿。（当前项目走 `omni_reference`：把上一段结尾的状态写进下一段第一段的 `画面：` 行，并配上一段的结尾截图作为场景/动作参考。）
2. **给最贵的那个招式一个连续镜头。**把整套组合写成一条以秒为单位的时间线，而不是分开的生成。
3. **点名禁止慢动作，并写明真实速度。**视频模型在打斗里会自己去用慢动作；如果镜头应该以真实速度落地，提示词就必须说出来。（这是一个点名值得付出引导代价的情况，因为模型的默认已经就是失败。）工作室中文稿写成正向：“全程真实速度”。

**每个招式都要点名并且带方向。**没写方向的招式每条素材都会被重新发明：*“她用脚把他从自己身上翻过去”*没说他最后在哪里，身体每次都落在不同的地方。把方向写进招式里：*“……他落地时脸朝着她，头朝着窗户。”*

**全身连续性太贵时，切进身体。**手、腰和脚的快速插入镜头能遮住过渡、增加冲击：而且**脚的近景比两个身体的远景难坏得多**。打斗关键帧也可以带上它们自己的火柴人站位图作为首帧几何（`template-staging-reference.md`）。

相关：§ Truncated action（切点落在结果之前）和 § Orphan limbs in a group shot，是最可能和这一条同时出现的两种失败。

---

## 交付前的自我修复（Self-repair before delivery）

提示词送进 Seedance 之前，跑这份交付前检查清单。它把上面的对策合并成一遍预防，让常见失败在构建提示词时就被抓到，而不是在烧掉一次生成之后。

- **帧率写在提示词正文里**（不只是元信息头）？交叉参考：§ FPS drift。
- **身体部位 / 感官语域的词清理掉了**？交叉参考：§ NSFW false-positive。
- **首次出现的元素标明了源关键帧里没有**？交叉参考：§ Keyframe-consistency forces invention。
- 适用时**点明了相邻物体的不变量**（`X stays attached`、`Y does not move`）？交叉参考：§ Physics-state-anchor。
- **运动把整段片子花在一个方向上**？短动作串成 2–3 个同方向的节拍；运镜有具名的终点？交叉参考：§ Action-reversal fill。
- **对白窗口写满了**？短台词延长了（4 秒镜头里约 8 个词以上）或者它的安静被写出来了，并且每张可见的脸都带了嘴部状态？交叉参考：§ Filler-babble on a short dialogue line。
- **每个镜头一个主导运镜**？复合运动拆成有顺序的阶段或分开的切镜？交叉参考：§ Multi-motion camera overload。
- 有多于一个主体，或者任何历来容易出空间失败的镜头（进门、走廊方向、绕家具）时，**用空间布局块锁定了几何**？交叉参考：§ Spatial-awareness failures。
- 为产出的素材**预留了逐帧审查时间**？交叉参考：§ Frame-level review is mandatory。

这份清单每条提示词花 60–90 秒，在烧额度之前抓住大多数可预防的失败。

---

## 交叉参考（Cross-references）

- `higgsfield-seedance.md` § Filter Model：先读这个，区分过滤器拒绝和渲染失败
- `higgsfield-seedance.md` § Voice Rewrite：为通过过滤器做的语言层面改写（与本文件的 § NSFW false-positive 相邻）
- `higgsfield-seedance.md` § When the User Is Already in a Failure Loop：过滤循环的恢复（渲染失败这一侧的兄弟目录）
- `higgsfield-seedance.md` § Spatial Layout Block：防止空间感知失败的块结构
- `higgsfield-seedance.md` § Frame Coordinate System：空间布局块用的坐标词汇
- `higgsfield-seedance.md` § Single-vs-multi-shot decision：§ Multi-motion camera overload 引用的多镜头拆分机制
- `higgsfield-seedance-hell-grind.md` § Dialogue construction：§ Filler-babble on a short dialogue line 依赖的音频块写法和 `INNER (unspoken)` 标记
- `higgsfield-troubleshoot.md` § Sequence & Continuation Failure Atlas：链式/续接缺陷的“症状 → 单一修复变量”表（本目录覆盖单段片子的渲染失败；那张表覆盖接点）
