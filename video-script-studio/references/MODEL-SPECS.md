# 视频模型规格

**快照：2026-09-26。**正式制作前，以用户提供的当前 schema 核对参数。

图像模型见 IMAGE-MODEL-SPECS.md（快照 2026-08-01）；本文件只含视频模型。

本工作室只保留 Seedance 系列。其他视频生成模型（Kling、Veo、Sora、Wan、MiniMax、Grok、Gemini Omni、FLUX Video、Happy Horse、Cinema Studio Video）和后期视频工具（超分、对口型、去背景、去闪烁、剪辑、预设）已从本快照中删除（removed）。

| Model（模型） | id（别名） | 时长 | 分辨率 | 模式 | 画幅 | 媒体职责 | 约束 |
|-------|--------------|----------|-------------|-------|---------------|-------------|-------------|
| Seedance 1.5 Pro | seedance1_5 (seedance_1_5) | 4/8/12s | 480p, 720p, 1080p | — | auto, 16:9, 9:16, 4:3, 3:4, 1:1, 21:9 | medias: start_image, end_image | — |
| Seedance 2.0 | seedance_2_0 (video_standard) | 4–15s | 480p, 720p, 1080p, 4k | std, fast | auto, 16:9, 9:16, 4:3, 3:4, 1:1, 21:9 | medias: start_image, end_image, image_references, video_references, audio_references | mode=fast 不可用 1080p/4k |
| Seedance 2.0 Mini | seedance_2_0_mini | 4–15s | 480p, 720p | — | auto, 16:9, 9:16, 4:3, 3:4, 1:1, 21:9 | medias: start_image, end_image, image_references, video_references, audio_references | — |
| Seedance 2.5 | seedance_2_5 | 4–30s | 480p, 720p, 1080p | t2v, omni_reference, video_edit, video_extension | auto, 21:9, 16:9, 4:3, 1:1, 3:4, 9:16 | medias: start_image, end_image, image_references, video_references, audio_references | start_image/end_image 仅限 omni_reference；t2v 不带参考；omni_reference 至少 1 个参考；图像参考 + 首帧 + 尾帧 ≤ 30；全部参考 + 首帧 + 尾帧 ≤ 50 |

各模型完整参数 schema 在 `model-specs.json`（含 2.5 / 2.0 / 2.0 Mini 的 `bitrate_mode` standard/high）。来源：OSideMedia/higgsfield-ai-prompt-skill v3.42.0（MIT），快照 2026-09-26。
