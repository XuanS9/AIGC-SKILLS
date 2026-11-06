# 模板：俯视平面图预可视化

写给**助手**（不是 Seedance）的元提示词模板。一次生成一张俯视平面图和一段可直接粘贴的 Seedance 站位说明，在任何 Seedance 生成开始前锁定空间几何。

> **地图是给你看的，文字是给模型看的。**本模板渲染的 HTML 只是写作辅助：你看它，对照意图检查几何关系，真正进入 Seedance 提示词的是**站位说明**。永远不要把平面图本身当参考图附上。
>
> 这不是风格偏好，而是各个来源对图示法唯一一致的结论：给视频模型看的站位参考图要**从摄影机一侧正面画，绝不俯视**。视频模型按画面思考，不按平面图思考；交给它一张平面图，它没办法把这套几何映射到镜头上。俯视是*推理*空间的正确形态，却是*展示*空间的错误形态。两件事同时成立，本模板完全站在推理这一侧。
>
> **展示这一侧是 `template-staging-reference.md`**：正面视角、按颜色区分的轮廓线稿，确实会附在生成里，并配有让它安全可附的三层防串染结构。在向任何人承诺它能钉住位置之前，先读它的实测说明。

## 何时使用

任何多人或几何复杂的镜头，只要 Seedance 历来容易把空间拼错：进门镜头、走廊方向镜头、需要跨切镜保持的双人站位。本模板防止的失败类型见 `higgsfield-seedance-failure-modes.md` § Spatial-awareness failures。

## 叙事交接

这张地图服务视频时，用 [共享叙事规划](narrative-planning.md)。八个语义层（资产、目标、全局视听与空间、行为、阶段、连续性、结尾画面、约束）为场景提供信息；本工具继续输出 HTML 加站位文字，提供规划里空间的那一部分。移动的站位要先找出事件、因果、揭晓或状态变化的边界，再分配时间；不预设阶段数，不平均分时。只画需要的空间状态，标出路径、触发、接触和最终位置。地图上的一个状态不自动等于一次切镜。保留静态平面图和比例尺功能，只把文字交给 Seedance。工作室交付时，站位说明编译进 `[具体情节]` 首段（定位秒）的 `画面：` 行和 `[保持一致]`。

## 助手提示词模板（可直接粘贴）

```
Build a top-down floor plan for [SCENE]. Mark every character with
their position, which direction they're facing, and who they're
looking at. Include distance between characters and a scale.

Below the diagram, write a paste-ready blocking note for Seedance —
one short paragraph per character covering: where they are, which way
they face, gaze line, pose, what they're touching.
For moving blocking, include the triggering event, path, and resulting position/contact
state only where they change; allocate timestamps afterward if needed. State the final
blocking and what the next shot inherits. Use as many states as the action requires.

Render as an HTML artifact.

Scene: [DESCRIPTION]
```

`[SCENE]` 填一行场景标题（如“餐馆对峙”）。`[DESCRIPTION]` 填完整场景描述：角色、地点、动作、氛围。描述越丰富，空间拼合越准确。

## 你会得到什么

- 一份把俯视平面图可视化渲染出来的 HTML
- 一段可直接粘贴的站位说明，格式适合直接复制进 Seedance 提示词正文的空间布局块（接收这段输出的块结构见 `higgsfield-seedance.md` § Spatial Layout Block）

## 差 / 好 / 很好

**差：**跳过预可视化。直接从场景描述写 Seedance 提示词，让 Seedance 自己拼空间。多人镜头的结果：角色站到画面错的一边、穿过家具、朝向不对。

**好：**用本模板拿到俯视图，目测几何关系，再手动把相关位置抄进 Seedance 提示词。空间准确度明显提高。几何复杂时，抄写这一步会引入错误。

**很好：**用本模板，**并且**把助手生成的站位说明直接贴进 Seedance 提示词的空间布局块。零抄写：助手推理的几何和 Seedance 收到的几何完全一致。锁定前在对话里反复调整平面图：改位置、视线、接触点，直到地图符合意图，再复制站位说明。

## 把道具尺度锁到地标上

这张地图还能把道具的**尺寸和位置锁定在一个固定地标上**，让大型布景道具每次生成都保持同样的尺度。用明确的尺寸倍数和共同视线，把道具钉在一个具名地标上：

```
标出消防栓。把充气人偶锁在它右侧，高度是一个人身高的两倍，和消防栓站在同一条线上。
```

地标（消防栓）是 Seedance 渲染稳定的东西；把道具绑在它上面（*两倍人高，同一条线*），给模型一个相对锚点，而不是一个它每次生成都会重新猜的绝对尺寸。任何超大或位置关键、必须跨切镜保持尺度的道具（充气人偶、车辆、招牌）都这样做。

## 另见

- `higgsfield-seedance.md` § Frame Coordinate System：站位说明用到的坐标词汇
- `higgsfield-seedance.md` § Spatial Layout Block：接收站位说明的提示词正文块
- `higgsfield-seedance-failure-modes.md` § Spatial-awareness failures：本模板防止的失败类型
- `template-multi-character-anchor.md`（同类模板）：接收站位说明的多人 Seedance 提示词
