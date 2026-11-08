# 模板：FACS 表情节拍表

可直接粘贴的 Seedance 2.0 提示词模板，用于由 **FACS 动作单元（AU）代码**驱动的近景面部表演：每个节拍一组 AU。完整方法、AU 参考表和“情绪 → AU”配方在 `higgsfield-facs.md`。工作室交付仍用中文块结构：节拍映射到 `[具体情节]` 各段的 `演出：` 行，对白写进 `[声音]` 的计时对白行。

## 何时使用

**脸**就是内容的近景镜头：独白、对白、强挤的笑、混合或诡异的表情、一个连续镜头里的情绪弧线。不用于调度或全身动作为主的镜头（那种用 `template-single-character-position.md`）。

> **先规划。**按 [共享叙事规划](narrative-planning.md)：先找出刺激、领悟或表情状态的变化及其可见反应，再分配时间。不预设节拍数，不平均分时。AU 组保持稀疏：叠得越多准确度越低。原来的 3–4 个节拍是每次生成的复杂度上限，不是目标或下限；够用就少写，表演过载时在有意义的边界拆开，保持对白和表情的连续。见 `higgsfield-facs` § The Plan-First Workflow。

八个规划层（资产、目标、全局视听与空间、行为、阶段、连续性、结尾画面、约束）是语义检查。把它们映射进这份 AU 节拍表以及身份、情绪、对白和运镜字段；保持连续近景格式。记录起始表情和预定的最终表情与视线。

## 提示词模板

```
**Model:** Seedance 2.0
**Aspect ratio:** [1:1 / 16:9 / 9:16]   **Duration:** [Ns]

[Use the provided character @Image1 as the fixed identity reference. — optional,
 only for identity consistency; codes work without an image]

**Style & Mood:** [framing — tight close-up, face + shoulders], [lighting],
[background], shallow depth of field, [mood].

[Optional dialogue — generates speech + automatic lip-sync, see higgsfield-audio
 § Audio as a Conditioning Input:
 [AUDIO: 0s] "[the spoken line]"]

Beat [n] ([start-end seconds, allocated after planning]): [trigger and inherited expression]
→ [AU codes] ([optional short anatomical description]) → [visible response / end state]
[After the physical facial/body action, add only when useful: （潜台词：[one short, direct performance intention]）]
[— delivers "<line>"]
[Repeat only for necessary expression changes; respect the per-generation complexity ceiling.]
Final expression and gaze: [state held into the final frame or next clip].

[One-line mood / subtext — optional. Keep it as a direct acting intention, not a
 literary inner monologue; do not add one to every beat.]

**Camera:** [one dominant move — slow push-in / static medium close-up]
```

## 各字段写什么

- **AU 代码**：来自 `higgsfield-facs.md` § AU Code Reference。简短节拍表写**只有代码**（`AU12`）；模型总是漏掉的单元写**代码加简短解剖描述**。两种都试。
- **情绪 → AU**：“愤怒/恐惧/悲伤用哪个代码”见 `higgsfield-facs` § Emotion → AU Recipes（杜兴微笑 = AU6+AU12，悲伤 = AU1+AU4+AU15 等）。混合表情在同一节拍里混用两种情绪的 AU。
- **节拍是连续近景里的表情变化，不是切镜。**运镜保持单一，免得 Seedance 把节拍表读成镜头表。节拍时间段必须连续覆盖**时长**，包括过渡和可读的停留（`higgsfield-seedance` § Runtime arithmetic）。表情与语义弧线清楚后再分配时间；保护完整的台词短语，有实际音频时按音频时间。上面的 `[AUDIO: 0s]` 只是示意，放在台词实际开始的位置。
- **对白节拍**：`[AUDIO: Xs]` 块驱动嘴唇和下颌的音素口型；你明确写的 AU 节拍表留给台词周围有表现力的眉、眼、脸颊肌肉。

## 另见

- `higgsfield-facs.md`：完整 FACS 方法、AU 表、情绪配方、示例，以及“不保证效果”的来源规则
- `higgsfield-audio.md` § Audio as a Conditioning Input：`[AUDIO: Xs]` 对白与口型
- `template-single-character-position.md`（同类模板）：内容是调度而不是脸的时候用
