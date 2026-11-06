---
name: video-script-studio
description: 将剧本与参考素材编排为角色/生物/道具/场景资产提示词、分镜、视频提示词及制作交接。支持剧情表演、打斗追逐、多线剪辑、Seedance、Higgsfield、VFX、模型选择和生成诊断；完整制作按场景分阶段、先样本后展开，单类型请求保持范围。
---

# 视频脚本工作室

本页只写核心契约。每条规则的详细写法只在一个负责模块里维护，按 [最小加载与规则归属](references/load-map.md) 读取需要的章节，不整包加载，也不从历史记录恢复旧流程。用户明确的格式或范围例外按对应分支处理；平台硬限制必须满足。

## 视频提示词契约

完整视频（含样本和改写稿）按 Higgsfield 块结构交付，块顺序固定：

`[角色]` `[道具]` `[场景]` `[动作与声音参考]`（前四个按需）→ `[生成目标]` → `[具体情节]` → `[视觉风格]` → `[镜头]` → `[声音]` → `[保持一致]`

- **语言：**块标签、字段与描述用中文，只有对白原句用英文。`【】` 是 Dreamina 的字幕括号，不用作块标签。
- **[具体情节]：**每段段头 `起s-止s｜景别｜视场角N°｜运镜`，下面写 `画面：` `运镜：` `动作：` `表情：`，两人以上同框加 `听者：`，有接触音效加 `声音：<…>`，以 `→ 结束：` 收尾。只写画面上看得见的事，不写镜头编号、落幅、机位或给审稿人的说明，不引用其他 Clip。有切镜时 `[镜头]` 写切镜锁定。
- **不设字数上限。**写足方位、量和先后，每件事只说一次。逐项写法见 [模板 §1](references/template-general-director-2-5.md#1-块结构higgsfield--dreamina-seedance-25-标准)。
- **对白照 Higgsfield 写在 `[声音]`：**先写 `对白语言：英语。`，再每句一行 `起s-止s｜说话人＋状态＋说：{English line}`，时间段落在说话那一段之内。段内动作和表情只写看得见的说话动作；台词写进动作描述会被模型演成行为。保留对白原句、说话人和顺序。无对白写 `本段无对白（设计）。`；音乐只在用户要求时用 `(…)`；末尾 `NO BGM。`
- **每条第一秒加 hm 锁站位：**有人物的 Clip 以约 1 秒定位秒开场（全景，按戏份可用中景；人物、朝向、持物、光已到位，不说台词、不做动作），`[声音]` 写 `0s-1s｜<画面中一人>轻声：{Hm.}`。这一声让模型把开场当成独立镜头并记住站位，不算剧本台词。`恰好 0 人` 的 Clip 不写。
- **资产映射：**`@中文名` 只出现在前四个映射块，每行 `名字 对应 @名字。本段状态：…`（坐姿、持物、伤势等，不写基础外观）。`[角色]` 首行写 `恰好 N 人，不出现其他人：…`，两人以上每人写身高；`[场景]` 写场景锁。其余块用中文名。
- **[保持一致]** 写数量、持物链、左右位置（以镜头为准），末尾 `无字幕、无水印。` 平台设置写在代码块外。
- 精简请求或硬限制用单段短式；原生 JSON、HTML、图像、纯音频保留各自格式。

## 时长与 Clip 边界

- 每个 Clip ≤30 秒，模型上限更短时取更短值。超量按 [压缩或顺延](references/narrative-planning.md#单个clip的30秒硬上限与超量处理) 处理，不截台词、不靠加速压缩、不延长单条。同场兼容的完整事件合进同一条，让每条接近所选模型的上限；不注水，也不把下一事件切一半塞进来；短于约 20 秒写明理由。
- 每个 Clip 独立生成，模型看不到上一条。边界按 [Clip 边界隔离](references/narrative-planning.md#clip-边界隔离强制) 处理：连续事件不跨边界；尾镜最后约 1 秒动作完成、镜头静止；首镜明显换镜头并以定位秒开场；跨边界只用文字交接静态状态。每个边界记入衔接表。
- 快切不等于交叉剪辑，生成顺序不等于成片顺序。并行追逐、分头行动、救援或倒计时须按 [多线叙事与交叉剪辑](references/narrative-planning.md#多线叙事与交叉剪辑) 评估交叉呈现并留理由。

## 镜长与切镜计数

**先事件、后切点、再估时，最后编入 Clip。3 秒是复核阈值，不是硬上限或固定镜长。**详规见 [事件驱动的镜长与节奏](references/shot-rhythm.md)。

- 对白按自然语速和气口估时；没朗读或预演的标“文字估算”。扑击、命中、跌落不为插入反应镜头而拖长。
- 每次真实切镜有观看任务。同镜推近、移焦、跨段续写不新增切镜，镜长累计；只改编号或分行不能重置镜长。超过 3 秒记录观看和切出依据；连续 4 镜以上等长触发复核，不强迫随机改秒数。
- 节奏 lint 只核证据范围和哈希；切点与表演由人工核验。

## 导演决策

按 [导演决策流程](references/directorial-shot-design.md#导演决策流程) 主动选择：场景变化与主次 → 观众信息 → 调度 → 切、留、镜内交接 → 时长与节奏 → 删并与反向核对。不以镜数或字数证明优化，不静默改已确认的剧情、对白、揭晓或镜序。

- 角色进出门先按 [门槛方向锁定](references/spatial-layout.md#32-进出门门槛方向锁定) 核对门两侧、起态与末态，再编译动作；进出画、朝向镜头和推拉门不能代替进出门方向。
- 大幅度空间转移按 [拆镜或甩镜过桥](references/directorial-shot-design.md#大幅度空间转移必须拆镜或用甩镜头过桥) 写，不写成单画面“从 A 到 B”。用户锁定一镜到底时才核路线、中间地标和摄影机路径。
- 有人物即调用 [表演](references/higgsfield-acting.md) 与 FACS 的适用部分，无对白和动作镜头也一样；非人角色走 [非人适配](references/higgsfield-acting.md#非人角色表演适配)。人物近景必须有当前可读的表情和触发依据。
- 一次交付导演方案、提示词和生成风险，见 [模板 §1.5](references/template-general-director-2-5.md#15-一次交付导演方案提示词生成风险)。

## 资产与场景

- 外观从故事推导：写任何 C/B/P/S 前先按 [资产设计依据](references/asset-design-basis.md) 填依据卡，每项标来源，推导内容随样本确认。
- 角色组板（六行四格、背景明度、声纹波形与音色标签）按 [角色资产模板](references/template-character-asset-delivery.md)。有台词的角色可登记完整音色描述，视频在 `[角色]` 原样附 `音色：…`；固定音色不替代当下的语气和气息。
- 命名、图号、源图链与 Clip 映射按 [资产总表](references/asset-registry.md)。handle 是 `@` + 纯中文名，逻辑调用名、图号、文件、平台槽位分开维护，不编造未建资产的标签。
- 场景图只交付纯环境，按 [场景资产内容边界](references/spatial-layout.md#场景资产内容边界)；场景与视频从同版 [空间布局](references/spatial-layout.md) 取关系。
- 风格：用户指定 → 项目已确认 → 按题材推荐，不默认真人。影视参考先拆进项目视觉总纲，复制正文不写片名。清理跨媒介污染靠改正向描述，不靠负面提示词。

## 默认值

视频只用 Seedance 系列，其他视频模型和后期视频工具已移除，用户点名时说明。未指定时 Seedance 2.5、16:9、中文。有任一参考用 `omni_reference`，完全没有参考用 `t2v`。2.5 支持到 1080p；需要 4K、`mode=fast` 或 `genre` 时选 2.0 / 2.0 Mini / 1.5 Pro。动作的强度与速度方案、人兽战与追逐见 [动作导演](references/fight-director.md)。

## 工作流程

1. **继承与范围：**读工作区的 `project.md`、`asset-registry.json` 和当前美术设定，继承已确认的参数、故事、对白、名称和阶段；读不到时说明，不虚报。咨询和诊断不强行变成制作。
2. **阶段与样本：**完整制作先统一规划、共享资产先定稿，再按场景走「补充基础资产 → 场景 → 视频」。每阶段新设计先给样本，确认后展开；用户明确要快速预览才联合预稿。已授权、不改确认设计的局部修订直接实施并复查。已确认未变的内容复用，不重复审批。见 [样本确认流程](references/sample-approval.md)。
3. **导演与编译：**先补事实、定导演方案，再按 [导演编译](references/director-compiler.md) 转块结构，不静默重排确认稿。
4. **修改后必复查：**按 [修改后标准复查闭环](references/production-checks.md#修改后标准复查闭环) 回读最终落盘稿和受影响的接缝，运行适用工具，修复后重跑。完整稿或批量修改运行 `proofread_manifest.py`，覆盖清单或哈希不匹配不得称校对通过。
5. **交付：**复制块只含必要标题和干净正文；确认、版本、路径和检查记录放 `project.md` / 总表。用户素材不移动，生成文件不写进 Skill 目录。无法写盘时附可保存内容，不声称落盘。

## 验收

按 [统一调用与验收总表](references/production-checks.md#统一调用与验收总表) 记录。文字、提交、生成结果分别写“通过／失败／待核验／不适用”，缺证据不能写通过；未生成写“未生成，视觉未验收”。零退出码不等于可提交，工具不证明语义、表演或模型效果。

## 检查工具

Python 标准库，从 Skill 根目录运行，只跑适用的工具。

```bash
python3 scripts/director_contract_lint.py --file video.txt --dialogue-source same-scope-dialogue.txt
python3 scripts/seedance_lint.py --preflight --model seedance_2_5 --file video.txt --asset-registry asset-registry.json
python3 scripts/shot_rhythm_lint.py --file video.txt --review rhythm-review.json --strict-review
python3 scripts/project_data_lint.py --asset-registry asset-registry.json --video video.txt --scenes scenes.txt
python3 scripts/asset_basis_lint.py --asset-registry asset-registry.json
python3 scripts/proofread_manifest.py --prompt final.txt --manifest proofread-manifest.json
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
```

FAIL 是可验证的本地缺陷；WARN 逐项解释。模型规格是离线快照，更新与信任边界见 [模型规格维护](references/model-spec-maintenance.md)。
