# 参考：素材变换的对白与节拍计时（Reference — Dialogue & beat timing for footage transforms）

一次计时运镜（急推、推近、揭示后拉）只有落在正确的那一帧上才有回报。Seedance 内部的计时会漂，所以你要给运动**两次**锚定：一次按含义（说出的台词或一个可见的动作），一次按数字（一个秒数标记）。本文件讲怎么得到这个数字、怎么写出两个锚点。被 [`higgsfield-seedance-vfx.md`](higgsfield-seedance-vfx.md) § Timed camera moves synced to dialogue 引用。

## 从源片段测出 `T`（Measure `T` from the source clip）

你是从用户已有的素材上读出 `T`：不是猜。

1. **检查片段。**查它的时长 / 帧率（能打开的话抽几帧）。你需要提示词要匹配的总时长，以及回报应该落下的时刻。
2. **找到触发时刻。**它是下面之一：
   - **一个说出的词**：某个特定的词开始的那一帧。从音频里读，或者用户有的话从源字幕/文字稿里读。
   - **一个可见的动作节拍**：打响指、转头、迈步、抬手。往往比一个词更容易对准，因为在画面里看得见（“at about 2.2s, on his finger snap with his right hand up beside his head”）。
3. **把时间码换算成秒。**提示词要的是从片段开头算起的秒数，不是 `MM:SS:FF`。
   - `MM:SS` → `MM*60 + SS`。例：`00:02` → `2` 秒。
   - 带帧的 `MM:SS:FF`，帧率 `fps` → `MM*60 + SS + FF/fps`。例：24fps 下 `00:02:05` → `2 + 5/24 ≈ 2.2` 秒。
   - 四舍五入到一位小数（`~2.2s`）；Seedance 把它当作意图，不是帧级精确的目标。

## 写出两个锚点（Phrase both anchors）

两个都放进动作里，挨在一起：

```
At about 2.2 seconds, on the line "transform myself right in front of you," the camera snaps
into a hard crash zoom on his right hand …
```

- **语义锚点**：`On the line "<exact words>," …`（动作节拍则写 `exactly as the man turns and looks back, …`）。台词**一字不改**地引用。
- **数字锚点**：`At about <T> seconds, …`。

两者不一致时（词实际在 3 秒落下，你写的是 2.2 秒），改数字：语义锚点是真相，数字锚点是保险。

## 要求和边界情况（Requirements and edge cases）

- **保留对白轨。**任何锚定在台词上的运动，规格行都需要 `SFX and source dialogue only`，否则对白留不下来，也就没有东西可以锚定。`SFX only` 用于锚定在无声动作节拍上的运动。
- **留一个尾巴。**回报在触发之后需要空间展开：一个生物慢慢转向镜头需要约 2–3 秒。片段太短的话，改在台词的**第一个词**上触发运动，而不是在台词之后。
- **每次时长改变都重算。**用户改了总时长，每个数字 `T` 都会移动：重算并告诉他们新的标记。加在前面的开场会把整个源素材往后推；在承诺某句台词会落下之前，先做 `总长 − 开场 = 保留窗口` 的减法（`higgsfield-seedance-vfx.md` § Duration discipline）。
- **口型能不能放下。**一句约 6 秒的台词放不进 5 秒的保留窗口。交付之前，对照窗口检查台词长度。

对白生成、`[AUDIO: Xs]` 剧本块、口型同步，以及“只提取前 15 秒音频”的陷阱，记录在 [`higgsfield-audio.md`](higgsfield-audio.md) § Audio as a Conditioning Input。工作室块结构稿里，台词按 `起s-止s｜说话人＋状态＋说：{台词}` 写进 `[声音]`，这里测出的 `T` 就是那一行的起始秒。
