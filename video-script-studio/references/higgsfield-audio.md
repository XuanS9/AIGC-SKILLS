# Higgsfield 音频提示指南（Higgsfield Audio Prompting Guide）

## 速查（QUICK FACTS）
*路由辅助：完整规则见链接的章节。*
- 这里的视频音频只覆盖 Seedance 系列（2.5、2.0 / 2.0 Mini、1.5 Pro），全部是原生联合生成 [→](#哪些模型支持音频which-models-support-audio)
- 每条提示词要考虑的四层：对白 / 音效 / 环境声 / BGM [→](#四个音频层the-four-audio-layers)
- 对口型可靠性：3–8 秒是试验窗口，不是时长规则；嘴部清楚、动作克制有帮助。说话人数取决于模型/模式；各语言的同步词数预算来自实地报告 [→](#对口型规则lip-sync-rules)
- **Seedance 2.0 的 `@Audio1` 是条件输入**：节拍同步、`[AUDIO: Xs]` 脚本块，以及前 15 秒截取陷阱 [→](#音频作为条件输入seedance-20audio1audio-as-a-conditioning-input--seedance-20-audio1)
- 像图像参考一样给音频参考限定范围：写明要迁移的属性、**不能**迁移的属性，以及被排除的属性改从哪里来 [→](#给音频参考限定范围说清迁移哪个属性scope-an-audio-reference--say-which-property-rides)
- 多片段组装：一条主音轨 · 切点落在音乐的标点上，绝不切在唱出的元音中间（大特写口型匹配是唯一例外）· 统一颗粒加 LUT 掩盖批次色差 [→](#按音乐剪辑把分别生成的片段组装到一条音轨上cutting-to-music--assembling-separately-generated-clips-on-one-track)
- **Seed Audio 1.0**（`seed_audio`，独立）= 一次生成整场音频：多人对白 + 音乐 + 音效 + 环境声混好 [→](#场景音频生成seed-audio-10scene-audio-generation--seed-audio-10)
- 独立音频目录（2026-08-01 快照）：`seed_audio`、`qwen_audio_tts`（新：Qwen 3.0 TTS Flash，表现力指令 + 克隆音色）、`text2speech_v2`（5 个引擎，含 cozy_voice），另有 3 个仅限游戏管线的工具；与视频内联合音频不同 [→](#独立音频标签页工具目录2026-08-01-快照standalone-audio-tab--tool-catalog-2026-08-01-snapshot)

## 声画的叙事规划（Narrative planning for sound and picture）

写提示、节拍同步、对口型、多片段组装或独立场景音频之前，先应用 [共享叙事规划](narrative-planning.md)。剧情事件、因果、揭晓和状态转变决定阶段；说话的含义、气口、反应、沉默和乐句帮助确定它们的边界。做完这些决定后再估算时长。不预设阶段数、等长阶段，也不在每个节拍上切镜。**阶段不是一次切镜，也不是一个生成片段**：一个镜头或一段连续的音频底可以跨多个阶段，一个阶段在实际模型限制内可以用几个镜头或几次调用。

**完整视频提示词使用工作室块结构契约（block-structure）**，单镜头也一样：工作室的 Higgsfield 块结构（`[参考资产]` → `[角色]` … `[生成目标]` → `[具体情节]` → `[视觉风格]` → `[镜头]` → `[声音]` → `[保持一致]`）。先读 [完整演出范本](template-full-performance-example.md) 和 [导演模板](template-general-director-2-5.md)；按 [统一调用与验收总表](production-checks.md#统一调用与验收总表) 验收。

真实音色/音轨参考的标签集中在开头 `[参考资产]`，职责按名称写在 `[动作与声音参考]`，音色描述写在 `[角色]`。所有对白写在 `[声音]`（Higgsfield 写法）：先写 `对白语言：英语。`，然后每句台词一行计时行 `起s-止s｜说话人＋状态＋说：{line}`，落在说出它的那一段之内。有人物的 Clip 在定位秒开头写 `0s-1s｜<名字>轻声：{Hm.}`。接触音效 `<…>` 写在各段的 `声音：` 行；音乐只在用户要求时用 `(…)`；无对白写 `本段无对白（设计）。`；最后写 `NO BGM。`。`[具体情节]` 各段只描述看得见的说话动作（嘴、气息、姿态）；写进动作描述的台词会被读成行为并演出来（Higgsfield / Dreamina 规则）。演绎跟随场景；提供的音频参考保持其实际职责和绑定。文字本身不能证明口型同步。尾声计入最后一个计时节拍。

跨片段的波形和混音属于后期：在可复制的提示词之外记录预定的接点，然后检查实际剪辑。单个片段的文字控制不了整部片的声音底。四个音频层仍是规划辅助，不是四个额外的输出栏目。

明确的精简请求、局部编辑、纯音频任务（audio-only tasks）和有硬限制/原生格式的提交，保留它们相关的内联提示、Audio 字段、`[AUDIO: Xs]`、广播剧、TTS、变声或翻译格式。完整视频工作从完整演出稿编译，不把重复的长稿硬塞进要求的原生格式。不给独立音频加视觉指令或视频标题。

编辑、翻译和变声时保留源时间码和时长，除非明确要求改时间；新的演绎对齐已有的时间窗口。唯一来源的音轨保留其内部时间。延伸时，在接点继承音色、声学环境、响度、乐句/音素相位，以及画面上的姿势、动作相位/方向/速度、构图和光。向前延伸从源的结尾开始；反向延伸结束在**源的首帧与音频状态**。只有新素材获得新预算。转场、停顿和最后的停留/衰减都计入总长。多个片段时，区分源时间码、成片时间线和片段内时间码；重叠/交叉淡化在最终剪辑里只计一次；独立生成的镜头的提示词无法强制这种连续性。Seedance 2.0 的 15 秒参考/截取限制和各 Seedance 模型的实际限制（见下文）保持不变；它们都不决定叙事阶段的长度。

## 哪些模型支持音频？（Which Models Support Audio?）

| 模型 | 音频类型 | 对白 | 音效 | 环境声 | BGM | 对口型 |
|-------|-----------|----------|-----|---------|-----|----------|
| Seedance 2.5 | 原生联合 | ✅ | ✅ | ✅ | ✅ | ✅ 多语言 |
| Seedance 2.0 | 原生联合 | ✅ | ✅ | ✅ | ✅ | ✅ 多语言 |
| Seedance 1.5 Pro | 原生联合 | ✅ | ✅ | ✅ | ✅ | ✅ 对口型最好 |
| 在所选模式下确认没有原生音频的模型 | ❌ | — | — | — | — | — |

**“原生联合”**指音频和视频在一次生成中同时产生，而不是之后叠上去。这能在不做后期的情况下得到自然的同步。

所选模式下原生音频失败时，用外部工具在后期加音频。这张表不完整；没列出的模型不自动等于没有音频能力。下面的能力和上传限制适用于指明的模型、模式、平台和日期来源。输入格式与输出格式分开；不要把某个平台的 MP3 限制推广到 Seed Audio、TTS 或其他 Seedance 版本。

---

## 四个音频层（The Four Audio Layers）

每条带音频的提示词都要考虑四层。不是每条都需要四层全写，但知道该写哪几层，能给模型清楚的方向。

### 1. 对白：角色说什么（Dialogue — What characters say）

台词用引号括起来。明确写出谁说、什么语气、什么语言。工作室格式里，台词写在 `[声音]` 的计时行里，用 `{}`。

```
She says: "We need to leave. Now."
He whispers: "Not yet."
```

**最佳实践：**
- 对白保持聚焦：每个镜头每个角色 1–2 句是短镜头示例；保留完整的含义和已批准的台词，再为演绎和反应留时间
- 写明情绪语气：“says urgently”“whispers”“shouts across the room”
- 非英语：写明语言和方言 → `She speaks in Cantonese: "走啦"`
- Seedance 1.5 Pro 支持：英语、中文（含四川话、粤语、台湾国语、上海话）、日语、韩语、西班牙语、印尼语

### 2. 音效：与动作绑定的具体声音事件（SFX — Specific sound events tied to action）

在声音发生的那一刻描述它。把音效绑到可见的动作上。

```
The glass shatters on the floor — sharp crack, then settling tinkle.
Footsteps on wet concrete — splashing, rhythmic.
A door slams shut — heavy metal, echoing.
```

**最佳实践：**
- 把音效绑到引起它的动作上；每个节拍一句简洁描述是为了清楚的经验法则，不是配额，也不要求每个阶段都加声音
- 少用拟声词：描述性短语比“BANG”或“CRASH”效果好
- 时机绑定到动作：“as she sets the cup down”；已指定时间时，保留源时间码或原生 `[AUDIO: Xs]` 标记，同时写上因果线索

### 3. 环境声：背景声景（Ambient — Background soundscape）

设定声学环境。这是连续的声音底。

```
Ambient: quiet café murmur, espresso machine, rain against windows.
Ambient: forest at night — crickets, distant owl, gentle wind through leaves.
Ambient: busy intersection — traffic, horns, construction in the distance.
```

**最佳实践：**
- 从几个不同的环境元素开始（例如 2–3 个）；优先清晰可辨，不要把数量当上限，也不要为凑数加声音
- 描述*空间*的声学：“reverberant church hall”“tight car interior”
- 用沉默对比声音制造冲击：“Dead silence. Then — a single footstep.”

### 4. BGM：背景音乐情绪（BGM — Background music mood）

不写歌名或艺人名（内容过滤）。描述音乐的质感。本工作室默认 `NO BGM`，只有用户要求音乐时才写。

```
BGM: slow piano, minor key, melancholic.
BGM: tense orchestral build — low strings, rising.
BGM: lo-fi hip-hop beat, warm vinyl crackle, relaxed.
```

**最佳实践：**
- 描述配器、速度、情绪，而不只是题材标签
- “Tense strings, building”比“suspenseful music”效果好
- 写明音乐何时进入/退出：“Piano enters at the midpoint, builds to the end”
- 卡节拍的内容：“Cuts match the downbeat”或“Movement peaks on the drop”

### 压制音乐：`NO BGM` 是规格，`no music` 是偏好（Suppressing music — `NO BGM` is a spec, `no music` is a preference）

`[DEMO — Joey cinema-director-v3, 2026-08-16]` `[UNPROVEN HERE]` 一段内容必须没有配乐时，措辞很重要。**`no music` 读起来是一个弱的风格偏好**，会输给模型“生成视频底下要有一层音乐”的强先验。**`NO BGM` 读起来是制作术语**，是硬规格，应该这样写。第一次使用时展开一次，让缩写不产生歧义，之后就让它沿用。

**先写正向，再写否定。**先说音频*是*什么，再说它不是什么：与表面和材质绑定的画内声源，加上房间底噪。一句里只有压制、没有任何正向内容，就是让模型自己决定“安静”听起来是什么样，而它会选择一层铺底。

```
Audio: diegetic sound only — footsteps on wet stone, fabric shift, breath, room tone.
NO BGM — no background music.
```

**每个独立生成的镜头，默认在该镜头的音频字段写 NO BGM。**一次包含多个阶段的生成里，只写一次（工作室格式：`[声音]` 末尾）。各段只描述允许的声音事件。`NO BGM` 排除的是配乐，不是所有声音。要求原生短提示词时，把这条策略放进它的音频字段。这是演示用的措辞，不是通用保证；所选模式需要时，用正向的声源/混音措辞。

> **列举要小心：这和关于否定的内部规则相抵触。**`negative-constraints.md` 和本仓库的站位参考规则都认为，**在否定下点名一样东西，等于还是把这个 token 送了进去**，可能反而引出你要拒绝的输出。原资料里那串长清单（score、soundtrack、instrumental、underscore、ambient pad、drone、tone bed、swell、sting、humming、whistling、lyrics）是它对一个真实失败的回答：裸否定会让模型补上一层“环境质感”、并认为指令已被满足；但这只是一个实践者的修法，**这里没有测量过**。默认用上面的短写法；只有短写法已经在眼前这个镜头上失败时，才用完整的列举，并预期列举本身会带来一些引导风险。

**应用附加音轨锁定之前，先区分参考的用途。**光是附上一个素材，并不会让它的声音成为输出。把每个音频/视频参考归类为：保留的原始音轨、视觉节奏驱动、表演属性参考，或音色身份参考。写明它是否可听，以及允许哪些生成层。只用作镜头/画面参考的视频不提供它的音轨。一个参考可以有明确相容的多个职责；可听的音乐层加新对白是混音，不是唯一来源锁定。

**附加音轨锁定只在任务指定该音轨为唯一且完整的音轨时适用。**保留其内部时间；不要给对口型的镜头强加新的逐拍说话窗口。仅限这种模式：

```
AUDIO: the attached clip @Video1 is the sole and complete soundtrack for this
sequence, preserved with all existing speech, music, and sounds at their original
times. Generate no additional audio.
```

**“听不见的音轨”技巧**让身体跟着混音里没有的音乐表演，适合配乐后期再加的情况：写明音轨听不见，然后描述对着它的表演（*“singing roughly in time to the unheard 87 BPM beat”*），加上确实能听到的画内声音层。

---

## 音频提示词结构（Audio Prompt Structure）

完整视频提示词用上面的块结构映射：参考职责写在映射块，计时对白行写在 `[声音]`，接触音效写在各段的 `声音：` 行，稳定的身份写在 `[保持一致]`。下面的紧凑示例只用于要求的短格式/纯音频工作或明确的原生字段。

### 内联写法（Inline method (preferred for short prompts)）：

```
A woman walks into a quiet library. Her heels click on the marble floor — each step
echoing. She whispers to the librarian: "Do you have the Collected Letters?"
Distant page turns. A clock ticks somewhere above.
```

### 独立音频块写法（Dedicated block method (better for complex audio)）：

```
[Scene description — visual content, action, camera]

Audio:
  Dialogue: She says "We leave at dawn." He replies: "I'll be ready."
  SFX: coffee cup set down, chair scraping back
  Ambient: early morning kitchen — birds outside, kettle just boiled
  BGM: none — silence emphasizes the tension
```

---

## 对口型规则（Lip-Sync Rules）

对口型是最容易失败的音频功能。下面的构图和短窗口做法是可靠性经验，不是阶段长度规则，也不是模型时长限制。保留源台词和完整的短语；只有能干净衔接、不截断也不重新定时台词时，才用更短的生成覆盖：

> **台词*周围*的面部表演**（勉强的笑、漏出来的恐惧、说话时的混合情绪）由每个节拍的 FACS 动作单元代码单独驱动。让对口型负责音素；为表演安排眉、眼、脸颊的 AU。见 `higgsfield-facs.md` § Dialogue & Monologue Facial Acting。

### 要做（Do）：
- 3–8 秒是对白镜头准确度的经验最佳区间，不是必须的段长；让实际的说话和反应决定窗口
- 用中近景或更近的构图：模型需要清楚看到嘴
- 单脸模式或说话人路由不可靠时，隔离出一张说话的脸；支持多说话人的模式改用明确的说话人归属
- `locked-off static camera` 或 `slow Dolly In` 是有用的可靠性基线；所选模式和表演支持时，保留其他运镜
- 如果说话时的头部动作（`nodding`、`turning head`）导致不同步，减少这些竞争线索；保留有动机的眼、眉、脸颊反应和听者行为

### 不要做（Don't）：
- 不要在同一条提示词里把对白和剧烈的头部动作放在一起
- Seedance 2.0 的 15 秒对白镜头同步可能比短镜头弱；测试需要的表演，而不是自动在 8 秒处拆开。其他模型保留各自的时长限制
- 唯一来源的语音录音，去掉额外生成音频的请求。原生对白配音效/环境声/音乐时，优先保证可懂度，只在需要时简化竞争层；它们的存在不是通用的对口型禁令
- 原指南报告其 Seedance 2.0 上传路径上非 MP3 文件失败；见 § Seedance 2.0 下限定范围的格式说明，这不是对所有模型/平台的格式禁令

### 多角色对白的变通（Multi-character dialogue workaround）：
说话人路由取决于 Seedance 模型和模式。Seed Audio 支持多个可听的说话人，但不生成嘴。不要把某条路径的限制变成所有模型的禁令。所选视频模式缺少多说话人口型，或镜头的说话人归属失败时：
1. 每个角色用自己的音频片段单独生成
2. 在 CapCut/Premiere 里用画中画加线性蒙版（15% 羽化）合成
3. 需要时用生成的听者反应；只有表演需要静止时，静态听者画面才是一个可选的合成捷径

### 各语言的对白同步预算（Per-language dialogue-sync budgets）[FIELD — community, seedance-2.0 repo v6.6.0]

约 15 秒的视频内 Seedance 对白片段里，实地观察到的**可靠对口型**词数预算：不是官方限制，也不等于模型能*念*出多少词。**声学预算 ≠ 可靠同步预算**：模型很乐意说出比它能和嘴对上的更多的词。

| 语言 | 可靠同步预算（约 15 秒片段） | 备注 |
|----------|----------------------------------|-------|
| 英语 | 约 16–20 词（每句 5–10 词） | 西方语言里最强 |
| 普通话 | — | 整体同步最强 |
| 俄语 | 约 10–15 词 | 弱，保守预算 |
| 日语 / 韩语 | 测试不足 | 还没有可靠的实地数字 |

跨语言的计量单位：**“一句短句 ≈ 一口气。”**按一口气长的句子写对白，数气口而不是数秒。

### 音色参考对口型路径（Voice-reference lip-sync path）[FIELD — community, seedance-2.0 repo v6.6.0]

在接受语音参考的平台上，附上的**已获授权的录音会直接驱动对口型**：模型把嘴对齐你的录音，而不是先合成一个声音。这是实地报告中**非英语对白**最可靠的路径（它绕开了上面较弱语言的同步预算）。**涉及权利：**只用你有明确权利的录音；未经授权克隆或抓取的录音不在此列。下面的独立 TTS 路径仍可使用受支持的、经授权的克隆音色。

---

## 音频作为条件输入：Seedance 2.0（`@Audio1`）（Audio as a Conditioning Input — Seedance 2.0 (`@Audio1`)）

Seedance 2.0 最被低估的能力：上传的音频文件是**条件输入**，不只是输出音轨。模型规格把 `audio` 和 `image` / `video` 并列为参考媒体职责，而 `generate_audio`（原生声音输出）被记录为*独立于音频参考媒体*：也就是说，上传的文件约束的是**生成**，片段是否另外生成声音是另一个开关。

这意味着 `@Audio1` 有下面**三种不同用法**。先声明它的用途和可听输出策略；只有明确时才组合相容的用法。音色身份也可以单独限定范围（§ Voice-reference lip-sync 和 § Scope an audio reference）。

| 用法 | `@Audio1` 做什么 | 提示纪律 |
|-----|---------------------|-------------------|
| **音频即输出** | 要求把上传的音轨原样作为片段音轨 | 用时间码锚定（`plays exactly as uploaded from 0s to end`）。**唯一来源**的音轨，去掉额外生成层的请求。预定混音时，点名保留的层和允许的新增；精确保留可能需要后期组装。 |
| **音频即驱动（节拍同步）** | 驱动**画面**：切镜时机、摄影机加速、动作节奏、能量峰值 | 明确写出音频→画面的映射（下文）。片段仍可以生成声音，或把 `generate_audio` 设为 false 只要画面。 |
| **音频即表演** | 画面里的角色**表演**这条音轨：哼唱、唱、跟着演奏、随之运动，踩准实际的音符 | 把它限定到你要的那一个属性（§ Scope an audio reference，下文）。不限定的话，它还会借出它的声音。 |

> **为什么有效（作者的模型：经验性的，不在官方规格里）：**推理运动和节奏的时间分支会读取声音的结构（节拍位置、动态轮廓、音色质感、歌曲段落），并把它映射成视觉节奏。把机制当作工作模型；把能力（音频参考职责）当作已确认。

### 给音频参考限定范围：说清迁移哪个属性（Scope an audio reference — say which property rides）

这套方法里每个*图像*参考都是双向限定的：它锁定什么，以及什么必须忽略（“ignore the sheet's grey background”“not its camera vantage”）。**音频参考一直没有对应的词汇，而它们出于同样的原因需要它**：一个声音文件同时带着好几个属性，不限定的参考会把它们全部借出去。

说明这一点的案例 [DEMO — Higgsfield "AI Love Stories" tutorial, 2026-08]：一个角色要在镜头前哼一段特定的曲调。没有参考时，模型**每次都编一段不同的旋律**：无参考对照组的报告结果是跑调、没节奏的表演。附上一段这首曲子的语音备忘后，第一次就踩准了音符。

但那段备忘是别人的声音，而角色有他自己的声音。所以参考**用文字限定了范围**：

```
@Audio1 is the reference for the HUMMED LINE only. Take from it ONLY the
melody: the exact notes, pitches and intervals, the tempo, the phrasing and
the rhythmic pause — note for note, beat for beat, nothing improvised. Do NOT
copy the voice, timbre or vocal identity heard in the recording — he hums in
his OWN natural speaking voice, the same voice he speaks his lines with. All
spoken dialogue is performed as scripted below, not taken from any audio.
```

**归纳出的模式有三部分，第三部分最常被跳过：**

1. **点名要迁移的属性**，越窄越好：音符、音高和音程；速度和乐句；节奏上的停顿。而不是“这首歌”。
2. **明确点名不能迁移的东西**：嗓音、音色、声音身份。声音文件既带着一段表演，也带着一个表演者。
3. **说明被排除的属性改从哪里来**：“他自己自然说话的声音，和他说台词用的是同一个”。只被告知不要做什么的参考，会让模型自己挑，而它会挑参考。

同样的三部分形式也适用于其他音频属性：

| 迁移 | 排除 | 改从哪里来 |
|---|---|---|
| 旋律、速度、乐句 | 嗓音、音色、身份 | 角色自己的说话声 |
| 节奏和重音型 | 配器、调性 | 场景自己的画内声音 |
| 情绪轮廓、动态 | 歌词/话语 | 剧本里的对白 |

**范围说明。**参考音轨是否变成说出的输出，因模型线而异：见 § Audio by Model。上面的限定词汇讲的是哪个*属性*迁移，要和该模型线对附加音轨的处理一起读，而不是替代它。

**权利：**上面那段备忘是本人为此专门录的。与音色参考对口型路径同样的约束：只用你有明确权利的录音。

[UNPROVEN HERE]：一个制作，一个属性（旋律）。*机制*已经确认（音频是参考媒体职责）；这里没有证实的是文字限定能把它引导到什么程度。用任何你拥有的曲子都能便宜地测试。

### 节拍同步：音频为画面编舞（Beat sync — the audio choreographs the visuals）

把一个 MP3 作为 `@Audio1` 上传，然后把音频特征映射到视觉元素。覆盖**节奏来源 / 哪个视觉元素响应 / 能量怎样映射到弧线**。下面的三句写法是示例，不是最少句数或阶段数：

```
Use @Audio1 as the rhythmic foundation. Sync camera transitions to the beat
positions. Visual energy builds with the audio crescendo and peaks at the drop.
```

你可以**把不同的视觉元素分配给不同的音频特征**，像混音一样混合音频到画面的映射：

```
@Audio1 drives the visual rhythm. Camera cuts land on the downbeats. Subject
movement accelerates into the build, holds at the peak, releases on the drop.
Colour temperature shifts warmer with the crescendo.
```

镜头 ← 节拍位置。运动 ← 动态轮廓。色彩 ← 整体能量弧线。这些映射适用于要求卡节拍的工作。挑选支持故事的、有音乐意义的提示点；一个节拍不必触发切镜，一个乐句也不必等于一个阶段。保留附加表演的时间，而不是把它硬塞进等长的时间区间。

它**可以和其他参考叠加**：角色来自 `@Image1`，镜头风格来自 `@Video1`，节奏来自 `@Audio1`，一起处理：

```
@Image1 as character reference. Follow @Video1 camera-movement style. @Audio1 as
rhythmic foundation — sync all camera transitions to the beat positions.
Character movement should pulse with the music.
```

**唯一的约束：**`@Video1` 的镜头风格和 `@Audio1` 的节奏必须**在时间上相容**。从视频参考里拿来的缓慢连续推轨对上一首 EDM，会给时间分支发出相互冲突的指令：和混用风格冲突的参考*图像*是同一类失败。挑能共存的参考。（与 `higgsfield-seedance.md` § Reference Roles → Load-Bearing Rule 是同一原则：参考各守其道。）

### 按音乐剪辑：把分别生成的片段组装到一条音轨上（Cutting to music — assembling separately-generated clips on one track）

非音乐类场景，剪辑师可以让环境声和音效尾巴跨过切点。把这一点记为后期交接，而不是一条让某个生成镜头能读到上一个镜头声音的指令。每个独立镜头的提示词只写它自己的可听声源；匹配和交叉淡化在生成之后完成。

`[EMPIRICAL — third-party skill corpus, re-derived; cross-model editing craft]` 节拍同步管的是片段*内部*发生什么；下面这几条管的是片段落上去的时间线：

- **连续性是剪辑决定。**如果组装好的影片需要不间断的天气声或房间底噪，就在后期混一层统一的声音底，并让音效尾巴过渡。单条生成的提示词无法保证跨镜头的同一声音。
- **音乐是可选的，镜头里默认关闭。**用户明确想要配乐时，在后期规划一条主音乐轨；不要在每个镜头里生成新的配乐。要求的音乐轨里的切点，比画面切点更先被听到。
- **切点落在音乐的标点上**：一次换气、一个歌词停顿、一下军鼓、drop。绝不在唱出的元音中间硬切，除非接进来的是一个口型延续这个元音的大特写：嘴唇的连续是*剪辑*约束，不只是提示词约束。
- **有意识地掩盖批次色差。**分开生成的片段调色永远不会完全一致。在整条时间线上统一做一次细颗粒加一个 LUT，作为刻意的收尾步骤，能藏住否则会被读成连续性错误的片段间色差。

### `[AUDIO: Xs]` 脚本块：只靠文字生成对白 + 音效 + 口型（The `[AUDIO: Xs]` script block — dialogue + SFX + lip-sync from text alone）

不需要麦克风，不需要录音。写在**提示词文字里**的带时间码的脚本能生成人声、音效和口型。引号里的文字 → 带自动口型的说话；物理描述 → 音效。每个标记是片段里的一个时间码：

```
[AUDIO: 0s] heavy footsteps on concrete, echoing in a corridor
[AUDIO: 2s] door bursting open, impact bang
[AUDIO: 3s] character says "Nobody move"
[AUDIO: 5s] tense silence, distant traffic
[AUDIO: 7s] character says "Put it down. Slowly."
[AUDIO: 9s] object placed on table, soft thud
```

模型**先生成声音**，再把面部运动映射到波形上，所以口型质量主要取决于你把对白写得多准确。**准确的引用文字胜过意译。**它跨语言有效（用西班牙语/日语/法语写台词 → 生成该语言的说话和音素级口型）。

它遵循和上面 § Lip-Sync Rules 一样的物理规则：一个强的 `@Image1` 角色参考提供一致的嘴部结构来做动画，**近景胜过远景**（小脸的像素太少，无法同步）。3–8 秒的准确度窗口是单条对白镜头有用的测试示例；它不能截断句子，也不能覆盖源时间。

所选模式支持预定的混音时，它**可以和节拍同步在一次生成里组合**：上传的音乐作为节奏基础和可听的背景层，脚本块作为新的前景对白/音效。这不是唯一来源锁定。如果生成改变了原始音轨，就在后期做精确保留。例子：

```
@Audio1 as background music. Sync camera transitions to the beats.
[AUDIO: 0s] music from @Audio1 begins
[AUDIO: 3s] character says "This changes everything"
[AUDIO: 5s] sharp breath — beat drop hits simultaneously
[AUDIO: 8s] character says "Let's go"
```

工作室块结构里，对白不用 `[AUDIO: Xs]`，而写成 `[声音]` 的计时行；`[AUDIO: Xs]` 只用于明确选择的原生/短格式流程。

### 15 秒截取问题：挑窗口，别上传整首（The 15-second extraction problem — pick the window, don't upload the track）

对 **Seedance 2.0**，音频参考限制是 **15 秒，而模型取你上传内容的前 15 秒**。丢进一首 3 分钟的曲子，你几乎总是喂给它**前奏**：能量低，常常是氛围性的，没有节奏推动。时间分支没有东西可映射。

要求一段能量上升的卡节拍段落时，**铺垫 → drop** 的窗口是一个有用的例子：它的动态梯度可以驱动视觉能量。它不是必须的弧线，也不是必须的 15 秒阶段。稳定的律动、持续的氛围、沉默或一句完整的台词，可能更服务实际的叙事。在输入限制内挑选相关的窗口，不切碎含义，也不编造渐强。

铺垫/drop 窗口位置的例子：

- 预副歌进入副歌
- 器乐铺垫进入 drop（EDM、电子、嘻哈）
- 主歌高潮进入桥段
- 前奏最后 15 秒冲进第一个 hook

**上传之前精确截出那一段。**原流程建议节拍检测用 **≥256kbps** 的 MP3；这是对那条路径的质量建议，不是通用的接受格式或最低码率要求。不要上传整首然后碰运气：挑窗口、剪下来、上传。（把流程反过来，先音频、再围绕它构建画面，会在结构层面而不是细微处改变输出。）

---

## 按模型看音频：哪里效果最好（Audio by Model — What Works Best Where）

### Seedance 1.5 Pro
- Seedance 系列里对口型最准
- 一流的多语言支持，包括中文方言
- 情绪语气控制最稳定
- 用于：专业对白场景、多语言内容

### Seedance 2.0
- 把 MP3 音频作为 @Audio 参考上传（计入 12 素材规则）
- **原流程的格式报告：**原音频指南把它的 Seedance 2.0 上传路径描述为只接受 MP3，并报告 WAV/AAC/OGG/FLAC 静默失败。它的具体平台没有指明；这不是对每个 Seedance 2.0 API/界面都已核实的限制。用所选平台支持的输入格式；MP3 是原流程的备选。
- 原流程的限制：每段最长 15 秒，3 个音频文件，每个 10MB；**≥256kbps** 是它的节拍同步质量建议
- **测得的执行边界** `[EMPIRICAL — third-party, China Ark lane, 2026-08]`：单段时长在 **1.8–15.2 秒**之间执行，并且**所有附加片段的总长也上限为 ≤15.2 秒**：三段各自合法的 6 秒片段会被拒绝（捕获到 400 错误）。这是第三方在 China Ark 通道上测的；Higgsfield 自己代理的执行**未经核实**：多段附件失败时，先怀疑这个总长上限。
- 时间码锚定（音频即输出）：`"Audio @Audio1 plays exactly as uploaded from 0s to end. Do not modify."` 唯一来源的音轨，去掉额外生成对白、环境声/音效/音乐的请求。视觉驱动、表演参考和有意混音的用法保留它们明确允许的声音层。
- **`@Audio1` 也是视觉驱动**：节拍同步、`[AUDIO: Xs]` 脚本块和前 15 秒截取陷阱都在上面的 § Audio as a Conditioning Input。

> **只用画内声音是可选的混音策略**，适用于配乐要在后期加、或生成的音乐底干扰了对白的情况。在那种流程里，描述物理声源：脚步、布料、呼吸、房间底噪、天气和人群反应。它不覆盖要求的原生 BGM、演唱、音乐表演、节拍同步的条件输入，或有意的参考加对白混音。唯一来源锁定只允许附加的音轨；只用画内声音的生成允许新的场景声音。按用途选策略，并在完整稿里只写一次（工作室格式：`[声音]`）。

## 常见音频失败与修正（Common Audio Failures and Fixes）

| 问题 | 原因 | 修正 |
|---------|-------|-----|
| 口型完全对不上 | 演绎太长/太复杂，或头部动作和同步争抢 | 去掉点头/转头词；合适时测试一段完整的较短短语，保留源时间和已批准的对白 |
| 模型替换了本该保留的音轨 | 生成层可能与预定的源锁定冲突 | 确认参考用途；用时间码锚定原音轨。只有唯一来源输出才去掉新增层的请求；需要时在后期精确保留音轨 |
| 对白完全消失 | 可能是原指南 Seedance 2.0 路径上不支持的上传格式，或输出/路由设置 | 检查所选平台接受的输入和音频设置；在那条报告过的路径上试 128–320kbps 的 MP3 |
| 音效盖过对白 | 声音线索或混音电平相互竞争 | 降低或简化竞争的音效，优先对白；没有固定的音效配额 |
| 声音听起来像机器人 | 情绪线索平淡 | 加情绪指引：“says warmly”“whispers with urgency” |
| 背景音乐太响 | 混音优先级不清楚 | 设定对白优先于音乐，在 `[声音]`（或原生 Audio 字段）里降低 BGM；局部电平变化写在对应事件处 |

---

## 何时不写音频（When to Skip Audio）

不是每条提示词都需要音频指引。以下情况不写音频提示：
- 所选 Seedance 模式关闭了原生音频
- 内容纯视觉（产品美图、抽象运动、风景）
- 音频完全在后期加；画面仍依赖那段音频时，保留视觉节奏/表演的条件输入和时间提示
- 明确的短格式提交里，可选的声音提示可以让位给必要的视觉指引；200 词软上限不会去掉必需的音频，也不会缩短完整稿

---

> **约束：**音频相关的瑕疵（口型不同步、背景音乐盖过对白、音效盖过对白）及其预防措辞，见 `negative-constraints.md` 的 Temporal/Consistency Artifacts 部分。在这里确立的范围内应用它的音频行：3–8 秒是可靠性试验，MP3 失败是原路径的报告，去掉额外层服务于唯一来源保留。这些行不覆盖参考用途、已批准的时间、原生多说话人支持或工作室块结构交付。

---

## 场景音频生成：Seed Audio 1.0（Scene-Audio Generation — Seed Audio 1.0）

独立于上面的视频内联合音频：**Seed Audio 1.0**（字节跳动，2026-06-23 在 FORCE 大会发布）是一个独立的**一次生成整场音频的生成器**。一次生成就产出多人对白 + 音乐 + 音效 + 环境声，已经混好：是一场广播剧，而不是一条单人声轨。用它为要在后期组装的素材做音轨，或者做完全没有视频的场景音频。

### 何时选它：决策表（When to choose it — decision table）

| 你需要 | 用 | 为什么 |
|----------|-----|-----|
| 整场戏的音轨：几个说话人 + 音乐 + 音效 + 环境声，一次混好 | **Seed Audio 1.0**（`seed_audio`） | 一次生成场景音频；剧本式提示词驱动整个混音 |
| 一条干净的人声轨（旁白、单人画外音） | **`text2speech_v2`**（选一个引擎） | 单人声 TTS：更简单，可选引擎 |
| 声音烤进生成的视频里，与画面动作和嘴同步 | **Seedance `generate_audio`**（视频内） | 原生联合生成：音频和画面在同一次生成里（见 § Audio as a Conditioning Input） |

### 已核实的参数面（Verified surface）[OFFICIAL — model spec 2026-08-01]

模型 id `seed_audio`（output_type `audio`）。参数：

| 参数 | 范围 / 选项 | 默认 |
|-------|-----------------|---------|
| `format` | wav / mp3 / pcm / ogg_opus | wav |
| `sample_rate` | 8000–48000 Hz | 24000 |
| `speech_rate` | −50..100 | 0 |
| `loudness_rate` | −50..100 | 0 |
| `pitch_rate` | −12..+12 | 0 |
| `voice_type` + `voice_id` | preset \| element，**必须一起出现** | 无 |

媒体职责：`image_references` + `audio_references`。按 fal 的 schema：最多 **3 段参考音频**（每段 ≤30 秒，≤10MB）**或一张图像参考，二选一**：图像和音频参考不能组合。在提示词里按加载顺序引用参考音频：`@Audio1`、`@Audio2`、`@Audio3`。

### 剧本格式提示（Script-format prompting）[EMPIRICAL — community guides, NOT official docs]

本小节的一切都是社区收敛出的实践，不是规格：当作起点，不是保证。把提示词写成一份**广播剧剧本**：

- 用场景标题开头：`[Scene: busy coffee shop, morning]`
- 说话人标签加情绪括注：`Host (warm, upbeat): "…"`
- 在声音发生处写内联声音提示：`[sound: espresso machine, soft jazz fades in]`
- 音乐按**情绪而不是题材**写：“soft piano builds to triumphant orchestra”，而不是“cinematic score”
- **约 4 个不同说话人**是社区报告的 Seed Audio 可靠性准则，不是 schema 限制，也不是其他多说话人模型的上限
- 往约 2 分钟上限扩展之前，**先测一段有代表性的场景片段**；20 秒是试验示例，不是阶段大小，也不是组装规则
- 音频要进后期时输出 **WAV**（`format: wav`）

用共享的事件/状态规划来安排说话、回应、停顿和声音变化；保留这种广播剧格式。纯音频工作里，最终的可听状态代替结尾画面描述。完整的短语和混音连续性决定接点，而不是等长分块或说话人标签的数量。

紧凑示例：

```
[Scene: rain-soaked night market, closing time]
Vendor (tired, warm): "Last skewers — half price, take them."
Customer (excited): "Two! No — three!"
[sound: rain drumming on tarp canopy, a scooter passing in the distance]
Vendor (chuckling): "Three it is. Careful, they're hot."
[sound: coins dropped on a metal tray, charcoal hiss]
Music: a lonely muted trumpet fades in under the rain, wistful but hopeful.
```

---

## 独立音频标签页：工具目录（2026-08-01 快照）（Standalone Audio tab — tool catalog (2026-08-01 snapshot)）

在线的独立音频目录，与 **2026-08-01** 的 models_explore 快照对齐（参数数据：`audio-model-specs.json`；表格：`AUDIO-MODEL-SPECS.md`；正式制作前对照当前 schema 核实）。音频标签页的界面工具（**Voiceover**：文字 → 语音；**Change Voice**：替换任意视频里的声音；**Translation**：翻译任意视频里的说话）建立在这些模型之上：

| 模型 id | 名称 | 做什么 | 可用性 |
|----------|------|--------------|--------------|
| `seed_audio` | Seed Audio 1.0（字节跳动） | 一次生成整场音频：对白 + 音乐 + 音效 + 环境声（§ 上文） | 通用 |
| `qwen_audio_tts` | Qwen Audio 3.0 TTS Flash（阿里巴巴） | 表现力 TTS：用自然语言 `instruction` 控制情绪/方言/语速，预设或克隆的参考元素音色，13 种语言提示 | 通用 *（2026-08-01 新增）* |
| `text2speech_v2` | Text to Speech V2 | 单人声 TTS；引擎通过 `variant` 选择：`elevenlabs`、`minimax`、`seed_speech`、`vibe_voice`、**`cozy_voice`** *（新）*；预设或参考元素音色（`voice_type` + `voice_id`） | 通用 |
| `sonilo_music` | Sonilo Music（FAL） | 可控时长的文生音乐 | **仅游戏管线** |
| `mirelo_text_to_audio` | Mirelo Text to Audio（FAL） | 可控时长的文生音效 | **仅游戏管线** |
| `inworld_text_to_speech` | Inworld TTS（FAL） | 预设音色 TTS，约 110 个音色，覆盖 en/zh/ja/ko/es/fr/de/ru/… | **仅游戏管线** |

`text2speech_v2` 里的引擎选择：交付是多语言画外音/旁白时选 **seed_speech**；需要细腻的情绪/语气控制时选 **elevenlabs**（Eleven v3）；长篇旁白选 **vibe_voice**。这些是独立的音频生成器，不同于视频生成时烤进 Seedance 2.5 / 2.0 的原生联合音频。（目录反映 2026-08-01 快照；报价或说明可用性之前先在线核实。）

### 生成后的画外音：Supercomputer 流程（Post-generation voice-over — Supercomputer workflow）[DEMO]

一种完全不在提示词里写音频的生成后替代方案：把**成片**上传到 Supercomputer，要求一段分析式的画外音（例如“Analyze the video and create a voiceover for it in the style of wildlife documentaries”）：智能体分析素材、写稿，并提供可选的声音。Higgsfield 的 Seedance-4K 教程里演示过；适合画面已锁定、只缺旁白的情况。

---

## 相关模块（Related skills）
- `higgsfield-seedance-vfx`：素材变换中，兑现点是与一句台词同步的运镜（急推 / 推近），或在变换中保留源说话音轨（`SFX and source dialogue only`）；见 `higgsfield-seedance-vfx-dialogue-timing.md`
- `higgsfield-models`：哪些模型支持原生音频
- `higgsfield-troubleshoot`：音频失败诊断
