# Darwin 三份 Skill 优化与实测 · 2026-09-24

## 后续更正：视频全部按参考职责输入

用户明确要求：当前视频制作不使用开头画面/首尾画面输入概念。已将 `video-script-studio` 的当前默认路由改为 Seedance 2.5 `omni_reference`；角色、道具、场景图片及参考视频、参考音频各指定采纳属性、排除项和真实绑定。只提供一张图片时仍作为参考。开场动作与结尾状态由剧情和导演文本说明；后者不是输入图片槽位。用户明确指定其他模型时，先核对该模型真实支持的参考类型。严格保留既有视频时间线的编辑/延伸请求另核验实际模式，不能将全能参考误称为像素级保真编辑。

同步改动覆盖根入口、导演编排、动作导演与诊断、样本确认、角色资产、Seedance 2.5 指南、全能参考模板、VFX 路由和发行 README。原 Seedance 2.0 等模型的历史参数示例保留为旧模型资料，现行项目入口明确禁止套用它们的开头画面方案。当前 `video-script-studio/test-prompts.json` 的第二案改为人物图、雨林场景图、狼追逐视频和环境音频的真实参考职责场景。

两条视频 prompt 均重新运行旧版入口、修订版入口和无 Skill 三组文本输出；共 6 条成功输出，保存在 `darwin-omni-evidence.json`。最终两条修订版输出的提示词代码块均无虚构 `@Image/@Video/@Audio` 标签，无参考图起点要求；第二案先交视频样本而没有把此前资产确认当作视频确认。3 位独立 paired judge 在同一次调用中比较本次改前/改后，结果 3 better / 0 worse / 0 tie，详见 `darwin-omni-paired.json`。这是本次更正的实测，下面原始两案的首帧字样仅记录此前曾测试过的旧假设，**不适用于当前用法**。

范围：`screenwriting-optimizer`、`script-writing-studio`、`video-script-studio` 三个整合包根目录的 `SKILL.md`。分支：`auto-optimize/20260924-0403`。来源目录和 references 未修改。最初的 9 维 triage 分数分别为 57.9、66.2、71.0；原始基线是干跑评分，只用于确定处理顺序，不用于 keep/revert。完整记录见 `results.tsv`。

## 实际修改

| Skill | 修改与验证结果 | Paired 三票 |
|---|---|---|
| screenwriting-optimizer | 输入不足、项目设定冲突、资料不可得、方法冲突时给出具体处理和兜底；允许材料分批提交 | 3 better / 0 worse / 0 tie |
| script-writing-studio | 开头角色年龄和外形默认与正文一致；梗概禁止无授权新增未成年相关情节；只润色对白但未给原句时先要原文，仅明确授权新写才拟写 | 2 better / 0 worse / 1 tie |
| video-script-studio | 缺素材、模式冲突、样本退回分别处理；名字已登记但未核实文件、状态及本片段绑定时，不把逻辑调用名写进可提交提示词；只有首帧的任务给条件性样本，不假装知道首帧内容或模型上限 | 3 better / 0 worse / 0 tie |

原版与最终版可运行 `git diff d926b38 HEAD -- <skill>/SKILL.md` 对照。中途试验发现两次输出回归并已修正：文案局部润色在缺原句时被过早扩大成拟写；视频样本曾把只有登记名的角色当作已绑定。视频另一次样本在首帧内容未见时只追问而没有给条件性样本；现已恢复样本。

## 效果验证

- 每包两条典型 prompt，三组分别在独立无工具调用中生成：无 Skill、原版 Skill、最终版 Skill；共 18 条成功输出（6 个 prompt × 3 组）。测试 prompt 在各包的 `test-prompts.json`，完整输出和退出状态在 `darwin-eval-evidence.json`。部分中间尝试曾因调用时限而超时，已重试；最终证据中的 18 条均成功返回。
- 每包由三个独立 judge 在**同一次调用内**读取改前和最终版，并以 9 维 rubric 比较，还看两条 prompt 的实际输出；三包共 9 个有效投票。理由和逐案观察在 `darwin-paired-results.json`。分数前后差值不作为 keep/revert 判据。
- 影视优化的缺稿任务给出可填写工作单；文案梗概满足已确认时长与停战结局，提供了原句的对白测试直接交可替换版本；视频缺狼文件时条件性样本不把狼当已绑定，首帧任务仍先提供视频样本。文学情节细节有抽样波动，某轮医院用药细节欠可信、某轮文案梗概漏掉制作初判；这些属于使用时仍需人工审稿的质量限制，不宣称每次创作都完美。

## 本地校验与发行包

`script-writing-studio/tests/validate_skill.py` 通过（24 份 Markdown）；影视优化入口链接可解析；视频 `seedance_lint.py --help` 启动成功；`verify_merge.py` 校验 299 项来源、三包结构与链接，0 错误、0 失效链接。三份入口文件大小都低于原版的 150%。三个单包 ZIP 和根 `three-skills-bundle.zip` 已同步，且总合集包含既有 `video-script-studio/references/asset-registry.md`。

结果卡片 PNG 未生成：本机缺 Playwright/Chromium 截图环境，且绝对前后分数不是可靠的提升量；报告与成对评审记录用于核对实际结果。未调用在线视频、图像服务，模型生成的真实视觉效果不在本轮验证范围内。
