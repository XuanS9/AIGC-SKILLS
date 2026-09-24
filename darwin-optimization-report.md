# Darwin 优化记录 · 2026-09-24

范围：`screenwriting-optimizer`、`script-writing-studio`、`video-script-studio` 三个整合包的根 `SKILL.md`。来源目录与 references 未修改；发行包及总合集 ZIP 已同步入口。版本分支：`auto-optimize/20260924-0403`。

## 测试 prompt 与基线（仅用于粗排）

各 skill 的两条典型 prompt 在其 `test-prompts.json`：影视优化包测试短片中段修订、缺原稿的剧集 pilot；文案包测试已确认条件下的梗概和局部对白；视频包测试资产有名无文件、跨批次资产确认与视频首帧模式。按 Darwin 9 维权重进行静态审查，并对每个 prompt 推演预期路由，得到基线粗排：

| Skill | 9 维基线（triage） | 主要发现 |
|---|---:|---|
| screenwriting-optimizer | 57.9 | 缺稿、冲突、资料不可得时未定义可交付的恢复路径；dim3 = 3/10 |
| script-writing-studio | 66.2 | 开头优先年轻漂亮成年人且不写未成年人，后文则不自动年轻化并要求核对未成年设定；dim7 = 7/10 |
| video-script-studio | 71.0 | 子模块有缺素材和样本说明，入口对三类常见失败未统一写明兜底；dim3 = 6/10 |

9 维评分向量（dim1→dim9）：影视优化 `8,8,3,3,7,9,7,5,2`；文案 `8,7,5,7,7,9,7,6,6`；视频 `8,8,6,8,8,9,7,6,6`。dim8 只是 prompt 干跑推演，未运行模型输出对照。6/6 prompt 为 `dry_run`，比例 100%（超过 Darwin 的 30% 失效警戒线），因此**这些总分不构成有效的效果评估，也不作为 keep/revert 依据**。Runtime 红灯扫描未发现指令性命中。

## 逐轮修改与判定

| Skill | 本轮唯一目标维度 | 修改 | 当前判定 |
|---|---|---|---|
| screenwriting-optimizer | dim3 失败恢复 | 给缺原稿、设定冲突、资料缺失和方法分歧分别指定当轮动作与兜底交付 | 本地静态检查通过，paired 评审未完成 |
| script-writing-studio | dim7 架构一致性 | 开头角色年龄/外形规则与后文边界统一，不自动年轻化；明确用户涉及未成年人时的核对路径 | 本地静态检查通过，paired 评审未完成 |
| video-script-studio | dim3 失败恢复 | 写明无资产文件、模型输入/限制冲突、样本修改时的处理和停止条件 | 本地静态检查通过，paired 评审未完成 |

修改前后可直接运行 `git diff d926b38 HEAD -- <skill>/SKILL.md` 查看。未取得三个独立 judge 的同轮 paired 多数投票：本机 `pi auth check` 显示没有可用认证，`claude -p --model haiku` 两次调用超时。所有修改在 `results.tsv` 记为 `provisional`，没有填造 after 分数或投票；保留可回退的提交，等待真实 paired 评审/人工复核。也没有把 2 条 prompt 的期望输出冒充实际生成输出。

## 验证

- `script-writing-studio`: `python3 tests/validate_skill.py` 通过，检查 24 个 Markdown 文件和入口路由。
- `screenwriting-optimizer`: 入口 Markdown 相对链接可解析，新增分支存在。
- `video-script-studio`: 本地 `scripts/seedance_lint.py --help` 运行成功，新增分支存在。
- 三组 prompt JSON 均有两条完整输入/预期；三个入口大小相对基线分别为 1.216、1.002、1.067 倍，均低于 1.5 倍约束。
- `python3 verify_merge.py` 返回 0 错误、三个入口及包内链接全部可解析；三个单包 ZIP 和根目录 `three-skills-bundle.zip` 已同步，后者补入已有 `asset-registry.md`。

图片成果卡片未制作：当前没有可用的 Playwright/Chromium 截图环境，也没有经过 paired 验证的 after 分数；避免用未经验证的分数展示提升。当前改动只涉及指令文本与发行包，不代表在线视频生成效果验证。
