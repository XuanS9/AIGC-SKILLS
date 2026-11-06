# 模板：对话气泡文字叠加

可直接粘贴的 Seedance 文字叠加模板：在说话角色旁边的画面里渲染出归属于该角色的对白文字。用于漫画风场景、社媒片段的对白、动画讲解。仅在用户明确要求文字叠加时使用；默认视频无字幕。

## 在视频中的时间安排

用 [共享叙事规划](narrative-planning.md) 规划所属视频的语义层：资产、目标、全局视听与空间、行为、阶段、连续性、结尾画面、约束。保留本页的简短气泡格式。由说话人的这句话和回应决定气泡出现的时机，再留出进入、阅读和退出的时间；不强加节拍数或等长时段。对齐实际的对白或源时间线，在运动中跟住说话人和气泡，并写明气泡在结尾画面是消失还是保留。守住下面的短对白和位置约束；已确认的长对白要拆成多个可读的气泡，不能悄悄删掉。

## 提示词模板

```
Character A says, "[SHORT DIALOGUE]". A clean speech bubble appears
near Character A's head, positioned in the upper-left area, with
simple readable text and no complex symbols.
```

## 字段填写

- **`Character A`**：换成实际角色名（已绑定的参考用资产中文名，无参考时写“穿红夹克的女人”这类可见标记）。
- **`[SHORT DIALOGUE]`**：控制在约 8 个词以内。更长的对白会溢出气泡，或把字缩到看不清。
- **气泡位置**：默认 `upper-left area`（左上方）；角色在画面左侧、气泡会压到脸时，换成 `upper-right`（右上方）。避免气泡压住说话角色的脸。

## 为什么写“no complex symbols”

Seedance 的文字渲染对字母和基础标点很可靠。符号（破折号、弯引号、星号、emoji）常被渲染成乱码或直接丢掉。对白文字保持朴素。

## 另见

- `template-subtitle.md`（同类模板）：与对白音频同步的台词字幕
