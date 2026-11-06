# Higgsfield 模型选择指南

选视频模型时，先按 [共享导演规划](narrative-planning.md) 估出实际的事件与表演工作量，再比较各模型支持的模式、时长和参考控制。模型时长表是合法范围或可选档位，不是推荐的剧情阶段长度。阶段、镜头和生成片段分开决定；所选模型装不下必要内容时，在兼容的状态交接处拆分。保留各模型特有的控制项，快照过期时按下文核实。

提示词之外，选对模型是影响出图质量最大的因素。本文件回答选择问题；参数在 `model-specs.json` 和 `image-model-specs.json`。

---

## 快速决策表

快速查找；详细对比见下方完整表格。

| 需求 | 推荐模型 | 档位 |
|------|----------|------|
| 视频快速迭代 | Seedance 2.0 Mini / 2.0 `mode=fast` | 中 |
| 时尚 / 审美类图像 | Soul 2.0 | 免费 |
| 写实、锐利的图像 | Nano Banana Pro | 低 |
| AI 演员生成 | Soul Cast | 低 |
| 原生 4K 图像 | Kling Image 3.0 | 中 |

**价格档位：**免费（Soul 2.0）· 低（0.1–2 积分）· 中（2–10 积分）· 高（10 积分以上）。见 `model-guide.md` 的积分参考。

---

## 视频模型对比

| 模型 | 写实 | 角色 | 运动 | 风格 | 时长 | 音频 | 适合 |
|------|------|------|------|------|------|------|------|
| Seedance 2.5 | — | — | — | — | 4–30 秒 | ✅ | 默认：多参考（30 张图像参考）、视频编辑 / 延伸、最高 1080p；尚无实地评分 |
| Seedance 2.0 | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★☆ | 4–15 秒 | ✅ | 12 素材多模态、复杂运动 |
| Seedance 1.5 Pro | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★★☆ | 4/8/12 秒 | ✅ | 对口型最好、多语言音频 |
| Seedance Pro（旧界面标签，不在 API 目录中） | ★★★☆☆ | ★★★☆☆ | ★★★☆☆ | ★★★☆☆ | 10 秒 | ❌ | 已被 Seedance 2.0 Fast / Mini 取代 |

---

## 决策流程

```
图像还是视频？
├── 图像
│   ├── 人物 / 肖像？ → Soul 2.0
│   ├── 电影感关键帧？ → Soul Cinema Preview
│   ├── 原生 4K / 图像系列 / 分镜？ → Kling Image 3.0
│   ├── 最高锐度 / 4K？ → Nano Banana Pro
│   ├── 快速专业质量 / 文字渲染？ → Nano Banana 2
│   ├── 参考一致性或密集文字？ → Seedream 4.5
│   ├── 复杂版式 / 多格？ → Seedream 5.0 Lite
│   ├── 图里有文字 / 标志？ → GPT Image 1.5
│   └── 编辑现有图像？ → Flux Kontext
│
└── 视频（仅 Seedance 系列）
    ├── 默认 / 多参考 / 单条最长30秒 → Seedance 2.5 `omni_reference`
    ├── 改或续接现有视频 → Seedance 2.5 `video_edit` / `video_extension`
    ├── 需要 4K、`mode=fast` 或 genre 提示 → Seedance 2.0（2.5 已支持 1080p 与首尾帧）
    ├── 预算 / 速度优先 → Seedance 2.0 Mini 或 2.0 `mode=fast`
    └── 多语言对口型、4/8/12秒离散档 → Seedance 1.5 Pro
```

---

## 图像模型速选

| 需求 | 模型 | 积分 |
|------|------|------|
| 时尚 / 文化肖像 | Soul 2.0 | 免费 |
| 电影感关键帧 | Soul Cinema Preview | 低 |
| 一致的角色身份（16:9） | Soul Cast | `budget` 10–500 |
| 环境 / 场景底图 | Soul Location | — |
| 最便宜 | Z-Image | 0.15 |
| 低价肖像 | Higgsfield Soul | 0.5 |
| 原生 4K / 图像系列 | Kling Image 3.0 | — |
| 4K + 高级编辑 | Kling Image 3.0 Omni | — |
| 快速通用 2K | Seedream 5.0 Lite | 1 |
| 4K 通用 | Seedream 4.5 | 1 |
| 草图生图（Draw） | Nano Banana | 1 |
| 艺术 / 风格化 | Wan 2.2 | 1 |
| 混合多张参考 | Multi Reference | 1.5 |
| 快速专业质量 + 文字渲染 | Nano Banana 2 | 1.5 |
| 低价 NB2（仅 1k，`thinking` MINIMAL/HIGH） | Nano Banana 2 Lite | — |
| 复杂提示词 / 图中文字 | GPT Image 1.5 | 2 |
| 基于参考的编辑 + 最好的文字渲染 | OpenAI Hazel | — |
| 最高保真 / Thinking 模式 / 14 张参考 | Nano Banana Pro | 2 |
| 图像编辑 / 局部重绘 | Flux Kontext | 不定 |

图像模型完整规格与界面控制见 `image-models.md`。

---

## 预算档位

**图像模型，按积分：**
- **免费 / 近乎免费：**Soul 2.0（5000 次）· Z-Image（0.15）· Face Swap（2 次免费）
- **低（0.5–1）：**Higgsfield Soul · Kling O1 · Seedream 系列 · Nano Banana · Wan 2.2 · Reve
- **中（1.5–2）：**Nano Banana 2 · Multi Reference · FLUX.2 Pro · Flux Kontext Max · GPT Image · NB Pro · Character Swap
- **高（5–6）：**FLUX.2 Flex · FLUX.2 Max

**通用价格档位（视频与图像，约数）：**
- **免费：**Soul 2.0
- **低：**每次 0.1–2 积分
- **中：**每次 2–10 积分
- **高：**每次 10 积分以上

各视频模型的确切积分见 `model-guide.md` 的积分参考。

---

## 独有功能对照

| 功能 | 支持的模型 |
|------|-----------|
| 原生音频（对白、音效、环境声） | Seedance 2.5 · Seedance 2.0 / 2.0 Mini · Seedance 1.5 Pro |
| Soul ID 角色槽 | Soul 2.0 · GPT Image · Higgsfield Soul |
| @ Elements 语法 | Seedream 4.5/5.0 Lite · Nano Banana Pro |
| Draw（草图生图） | Nano Banana · Nano Banana Pro |
| 视频编辑 / 延伸 | Seedance 2.5 `video_edit` / `video_extension` |
| 多图参考混合 | Multi Reference · Nano Banana Pro（14 张）· Seedance 2.5（30 张图像参考） |
| 首尾帧控制 | Seedance 2.0 / 2.0 Mini · Seedance 1.5 Pro |
| Soul Cast AI 演员 | 独立的 `soul_cast` 图像模型（16:9，`budget` 10–500） |
| Soul HEX 配色匹配 | Soul 2.0 · Soul Cinema Preview |
| 原生 4K 图像系列 | Kling Image 3.0 |
| 风格预设 + 色彩迁移 | Soul 2.0 |
| Google 搜索增强 | Nano Banana Pro |

---

## 模型要点

**Seedance 2.0：**12 素材规则（每次生成最多 12 个素材）。禁止上传真人面孔，用合成角色参考。Seedance 2.0 的提示词最佳实践已并入各子模块（见 higgsfield-prompt、higgsfield-camera）。

**Grok Imagine：**Aurora 架构（自回归，非扩散），擅长文字 / 标志渲染和多图合成。图像编辑支持多轮迭代。

---

## 相关模块
- `higgsfield-prompt`：MCSLA 公式与提示词结构
- `higgsfield-audio`：带音频模型的细节
- `template-*.md`：带各题材模型推荐的注释模板
