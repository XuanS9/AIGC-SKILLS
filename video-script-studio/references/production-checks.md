# Production checks

## 本工作室适配优先

每次修改完成后执行 [修改后标准复查闭环](production-checks.md#修改后标准复查闭环)，再按本页分层验收；不是只在首稿交付时检查。

动作、对峙、对白及跨Clip改写同时执行 [动作同步、接缝去重与整场节奏](narrative-planning.md#动作同步接缝去重与整场节奏)：先后/并行共用事件时钟，前尾后首不重演，按整场累计问答等待与行动线缺席；剪辑顺序改变后复核新接缝。

以下通用检查服从根入口：完整视频四段式、阶段内先样本、按场景推进；已确认未变内容直接复用。流程纪律不额外增加确认点或实图门禁。项目视频用中文资产名及真实绑定，不以“只写外观标记”覆盖资产命名；时长在块外设置与段内时间轴一致即可，不在正文另塞规格栏。

导演增强使用 [导演编译](director-compiler.md) 与 [导演控制与返工](director-control-retake.md)：
- **叙事结构**：执行 [多线叙事与交叉剪辑](narrative-planning.md#多线叙事与交叉剪辑) 语义自检；核对有效行动线、首次露出/回切/汇合、观众与角色知情、切离期间状态推进及选择单线/交叉的理由。生成凑段不能延迟必要叙事线；结构lint不代替这项判断。
- **内容与事件覆盖**：按 [参考图内容划分](spatial-layout.md#21-按环境内容划分参考图) 判断复用或独立出图；按 [事件突出与细节特写](directorial-shot-design.md#事件突出与细节特写) 核角色反应、环境余波、景别可读性和动作接续。没有成片证据不能把规则存在写成效果通过。
- **编译对账**：确认镜序、对白、事件和落幅在四段式中均有落点；不得静默重写上游。
- **五维核对**：空间、摄影、表演、光、声音各有可定位证据或不适用理由。人物行为来自任务与刺激，不是机械表情清单。
- **逐缝核对**：位置、朝向/视线、左右手持物、动作相位/动量、可见情绪与气息；持久变化与未解线头记现有 project.md。
- **风险控制**：控制图有具体用途、帧源、作用时段和绑定状态；不足时只阻塞相应提交，不扩大到全项目。
- **证据返工**：定位矛盾/断链/走样/能力风险/硬约束违背，选改词、局部编辑、换镜头、改输入或回上游；每轮一个变量类别，保留版本与复验记录。

本地文本检查（skill 根目录）：

```bash
python3 scripts/director_contract_lint.py --file /path/to/video.txt
python3 scripts/director_contract_lint.py --file /path/to/video.txt --dialogue-source /path/to/same-scope-dialogue.txt
python3 scripts/proofread_manifest.py --prompt /path/to/final.txt --manifest /path/to/proofread-manifest.json
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
```

`seedance_lint.py` 默认使用 `--profile standard`，完整四段式母稿不套双语JSON的1800字符限制。只有交付目标明确为该JSON格式时才传 `--profile bilingual-json`，检查提取出的中文提示词或双语数组解码后的中文 `prompt` 字段；英文文本和JSON转义不计入中文限额。平台真实提交长度另核验，不能为消除格式误报删减母稿演出。

契约脚本只检查标准四段式文本：四标题、时间轴、单个 Clip≤30秒（声明时长与片内所有终点）、声音写法（不检查固定镜头数量或单镜3秒上限）及 `「台词」` 的字面覆盖次数。无块外时长或 `--duration` 时不核对目标总长是否相等，但仍执行30秒硬上限；不自动判断说话人、表演时长、布局语义或实际模型效果。真值稿只包含本次范围，重复台词按次数核对；原生 JSON/HTML、短式/资产/纯音频不运行该检查。模型参数与总表继续用 seedance_lint.py，真实绑定及视觉验收另行核对。

## 修改后标准复查闭环

**每次修改后、交付前必做，不能只在第一版执行。**适用于新写、修词、补镜、删并、重排、批量替换及Skill规则/模板维护；包括单条、样本和完整批次。内部复查不新增用户审批，不重审已确认且未变内容。

1. **修改前锁定基准。**读取本入口当前契约和本次适用模块，提取用户确认稿、格式、范围、时长、对白/说话人、资产名、布局/美术版本及不可改项。明确本轮到底改什么；样本/局部请求不扩大到全项目。
2. **修改后读回成品并证明覆盖。**重新读取最终落盘稿，而不是编辑前内容、替换片段或聊天摘要；未落盘时重新检查准备交付的完整复制块。检查整个改动条目；批量修改逐条检查全部改动Clip/图片，不能只看首条。对批量或全稿校对，按Clip建立覆盖清单：每个Clip记录复查状态、可定位结论、发现项（无发现填空列表）及该Clip最终文本SHA-256；资产/单提示词以完整文件为一个条目，需逐段或逐模块复查时用对应稳定ID拆分。写明预期条目集合，并记录完整成品哈希。清单须与最终稿同一版本；任何正文变动都使对应条目及总文件复查失效，修复后重新读回受影响条目及接缝并更新哈希。
3. **复查契约与提示词污染。**按T9核四段标题/顺序、秒轴、概述、内联对白/声音、平台设置块外、资产外观去重及干净复制块；图片核其版式、纯环境/独立背景、名称与已定风格。查新引用的模板是否引回旧标题、独立音频栏或内部登记说明。另做一次否定语义回读：检查`不/无/没/避免/禁止/不再`等否定句及其宾语，判断是否把不想生成的脸型、表情、动作或画面特征重新提给模型；能改为目标状态或可见行为时，改成正向描述。不能只靠关键词通过，也不能机械删除有明确默认失败风险且确有必要的约束。短式/原生格式只按实际分支，不用无参考作为完整视频省栏的理由。
4. **复查语义与依赖。**按适用T1—T8核事件/对白及说话人、时序、空间、表演和状态。修改Clip同时核前后接缝；重排核全部新相邻接缝；改资产名/图号/布局/美术核相关正文、标题、总表和下游。未变部分可引用原证据，但要确认本轮未影响它，不能将旧版通过记录挪作新版结论。不能为满足格式静默改剧情、台词或用户锁定镜序。
5. **运行适用检查。**每个 Clip≤30秒是不可跳过的硬参数；镜头数量与单镜时长不设固定门槛，按叙事、动作与表演可读性逐镜核验；逐条检查声明时长与所有片内时间段终点，超量先压缩或顺延到下一条，并同步标题、秒轴、引用时段与接缝，不能通过延长单条或承诺事后裁切放行。同镜跨段仍按连续观察理解，不以分行或编号虚报切镜；超过3秒不单独判失败。调整镜长或分组时同步标题、参考职责、分配表与接缝，不为填满30秒延长末镜。未运行、任一 Clip 超限或覆盖失败都阻塞完成。完整四段式运行 `director_contract_lint.py`；含引用时运行 `seedance_lint.py --asset-registry`；对白删并/拆分/改编传同范围 `--dialogue-source`，说话人与顺序另核。六行角色用模板校验，原生JSON用其schema/解析检查，场景图号/源图链/双向映射另核。没有适用工具时说明人工检查范围；不能称未运行的项目已通过。WARN逐项解释，不以零退出码替代语义验收。
6. **失败修复并重跑。**发现文字失败先修复，再读回修复稿并重跑受影响检查；修复带来新依赖时扩大复查范围，不增加制作范围。缺证据如实记待核验，不能通过修改标准、删测试或换成“不适用”让失败消失。
7. **覆盖门槛与分层交接。**完整稿校对须以`coverage_mode: complete`列齐最终稿的全部Clip；限定范围修订可用`coverage_mode: scoped`，但必须列出本轮实际复查条目、写明scope，并绑定最终完整文件哈希。两种模式都要求每个列入条目为`reviewed`、有逐条结论和发现列表，条目哈希匹配；校验器必须运行通过。限定范围通过只能称“所列条目复查通过”，不能称“全稿校对通过”。任一缺项或哈希漂移都不得称校对通过；先补审/复审，再重跑。脚本只证明覆盖记录完整且绑定当前版本，不证明结论正确，语义仍按T1—T9人工审。最后记录对象/版本或文件哈希、复查范围、实际命令及结果、语义证据、修复与待办，分别给文字/提交/结果结论。详细记录放既有 `project.md` / 总表，聊天简述；没有工作区放块外。未生成写“未生成，视觉未验收”；标准复查不是样本确认、真实绑定或成片验收。

### Skill维护的额外复查

改规则/模板不改用户项目。以当前入口为基准，检查入口→详规→模板/示例→检查器/测试的同一规则落点，全文检索已替换的旧用语；区分内部规划、历史记录和可复制生成正文，不把原生分支误改成四段式。改交付格式时，用填写后的模板与当前标准小样实际运行契约检查；历史范本明确标旧版与编译边界，不能继续标“可直接复制”。

每轮实际运行全量 `python3 -m unittest discover -s scripts/tests -p 'test_*.py'`，核修改文档本地链接、围栏与新增JSON示例；给本轮已发现的可计算缺陷补失败/通过回归，语义问题补人工证据。复查其他既定标准没有被覆盖，模型数据与未授权项目文件有保留性核对。**测试通过只证明已覆盖项，不证明全文无冲突。**优化记录写明当前变更与真实验证；旧策略标历史/已被覆盖，不作为当前标准来源。

## 统一调用与验收总表

本节汇总已有规范的调用与证据，不另创表演写法，也不新增用户审批。适用于新写、改写、补镜、合并生成及交付前复核；纯诊断只审指定范围。**读取模块不等于落实要求，结构检查通过不等于语义或成片通过。**

### 默认调用与落实记录

先识别本轮类型、版本、已确认项及变化范围；按下表组合选择模块，在现有 `project.md` 的检查记录中保留简短调用表。无工作区时仅在复制块外交接，不另建强制目录/台账。相同规则只引用其负责模块，不复制多套标准。

| 触发条件 | 默认读取的现有模块 | 必须落实的证据 |
|---|---|---|
| 任何视频提示词，包括单条、无对白及改写 | [叙事规划](narrative-planning.md)、[导演决策流程](directorial-shot-design.md#导演决策流程)、[导演编译](director-compiler.md)、[导演模板](template-general-director-2-5.md)；完整创作/改写另读演出范本 | 整场变化与主次、观众信息、调度、切/留/删并的已选主方案；逐Clip时间轴与正文证据 |
| 有人类角色表演，包括静音、跑动、听者、背景人物 | [表演](higgsfield-acting.md)与[FACS身体微反应](higgsfield-facs.md#physical-micro-beats--the-body-beyond-the-face)；细表情/对白特写再读对应FACS段 | 刺激—视线/判断—可见反应—行动，按景别写入演出；不是只声明“有情绪” |
| 有动物、奇幻生物或其他非人角色表演 | 表演模块的通用行为原则及[非人角色表演适配](higgsfield-acting.md#非人角色表演适配) | 已定解剖结构、拟人化边界及可见行为；不默认套人类AU |
| 剧情创作、改写或叙事审计 | [场景引擎](higgsfield-scene-engine.md)与叙事规划 | 目标、阻力、策略和信息变化；不为填表新增反转 |
| 追逐、交锋、受力或持续动作 | [动作导演](fight-director.md)与[事件时钟](narrative-planning.md#动作同步接缝去重与整场节奏) | 准备、接触、响应与结果在同一事件时间内成立 |
| 有对白/声效/音乐，或画外人声 | [音频](higgsfield-audio.md)，人声另取表演的当下语气/气息部分，不输出固定音色 | 说话人、原句、声源、气息与落点；画外说话者不因此入画，纯画外声不强制FACS |
| 场景参考、空间调度或跨镜持物 | [空间布局](spatial-layout.md)、[资产总表](asset-registry.md) | 环境内容划分依据，同版地标/连接、身体左右与构图自由；图号时段、弃用图删除与无悬空引用；场景整张无角色/生物/道具，视频另落实站位与物件落位 |
| 关键事件表现、角色/手部/接触特写 | [事件突出与细节特写](directorial-shot-design.md#事件突出与细节特写)及表演模块 | 事件准备/接触、必要反应与余波的具体落点；特写刺激、可见变化、手别/持物与切回状态 |
| 多镜、跨空间、短Clip或重组生成 | [生成分组验收](narrative-planning.md#生成分组与短段例外验收) | 合并候选、保留短段的理由、生成范围→成片区间映射 |
| 用户指定模型/平台、准备提交 | 对应模型资料；Higgsfield另读平台指南及相应模式模块 | 版本/来源、输入职责、真实绑定、模式限制；经验不冒充硬上限 |
| 基础角色/生物/道具或场景图片 | 对应资产模板、资产总表；场景另读空间布局与[视觉参考匹配](higgsfield-style.md#电影视觉参考匹配)及项目美术 | 版式、身份、比例、材质与干净背景；场景每个复制块有匹配媒介、建筑文化、材质、光色的证据；中性资产不强加剧情情绪 |
| 失败结果、实图差异或成片验收 | [控制与返工](director-control-retake.md)及对应故障模块 | 当前结果、时间段、期望与实际差异、最小修复及复验 |

调用记录：

| 适用任务/触发依据 | 实际读取模块及小节 | 本轮对象/版本/时段 | 正文落点或不适用理由 | 检查结果 |
|---|---|---|---|---|
| 按当前任务填写 | 未读不得写已读 | 样本只记样本范围 | 引用具体演出句，不写“已加强” | 按下列四态记录 |

已有且未变内容可引用原证据及版本，不重复审批；修改过的内容重新核对，不能把旧证据挪作新版通过。适用模块漏读、所需描写未进入正文，是执行缺项，交付前补齐。

### 四态与结论边界

- **通过**：在本层、本范围内有可定位的有效证据，适用项满足；不代表用户已确认设计。
- **失败**：已发现缺失、冲突、遗漏或不符合确认要求；记录修复位置。文字已知失败先修复再交付。
- **待核验**：适用但缺证据、未执行或有未定设计；说明影响与下一步。未生成的视觉效果记待核验，不记不适用。
- **不适用**：当前任务确无该需求，写明原因，如无对白不做口型核验；不能用于绕过未完成项。

**适用的关键项失败不能被其他项高分抵消。**只有本层适用项均通过或有合理不适用说明，才能称本层通过；存在待核验时给范围明确的结论。设计未定可交条件性方案，但不能称该设计已验收。缺实图/绑定不自动阻塞文字层，阻塞的是相应提交或结果验收。泛化“全通过”、平均分或测试数量均不能替代分项结论。

### 导演方案反向验收

文字结构检查之前，按 [导演决策流程](directorial-shot-design.md#导演决策流程) 连读整个戏剧段，复核下表。证据归入同一T1/T4/T6记录，不增加另一组审批或单独台账。每个机位无需长论证，但每个重点和可能抢走重点的处理须有实际依据。

| 判断 | 证据与修复方式 |
|---|---|
| 变化与人物依据 | 用具体行为与场末结果说明局势/关系如何变化；不能靠温柔近景或潜台词把未发生的转变拍成已发生 |
| 重点与支撑 | 标出最需要读清的选择/接触/后果，核前后注意力分配；准备与日常连接喧宾夺主时先删并，而非再加一个更大特写 |
| 信息与视点 | 分别核观众和人物知情，主观可见边界与揭晓时机；同一事件有悬念/惊奇等选择时有已选立场 |
| 切或留的必要性 | 比较持续观察、镜内交接与剪切；暂去候选插镜后，理解或情绪压力是否损失？无损失则删并，有价值的等待可保留 |
| 调度与表演 | 不看意图说明，仅凭正文的动作、距离、遮挡、声音能否读出人物策略与响应？失败回上游修可见行为 |
| 节奏与负荷 | 真实准备/飞行/承重/对白时间可执行，重点有窗口、结果有余波；不能用细分秒轴或完整句子数量证明能拍完 |
| 全批取舍 | 各Clip按本场功能检查，保留、删并、新增各有原因；不能要求每条都改、每条都增加或复制首条拍法 |

### 第一层：文字稿验收

| 检查项 | 通过条件与所需证据 | 失败时返回 |
|---|---|---|
| T1 剧情与信息 | 与确认稿逐项对账：事件、对白/说话人、结局及人物知情成立；授权重排有新旧依据 | 源稿/叙事规划 |
| T2 人物与生物表演 | 按[表演证据验收](higgsfield-acting.md#表演证据验收)逐项核对；非人角色另核结构和拟人边界；表情确实写入适用镜头 | 表演/相关演出句 |
| T3 动作与时间 | 不设每个 Clip 固定镜数或单镜3秒上限；镜长按真实动作、对白、表演与信息可读性判断，同镜续写/推近/移焦保留连续关系。准备、命中窗口、受力、先后/并行清楚；没有为了特写让对手暂停 | 动作时序/分镜 |
| T4 摄影与空间 | 按[导演决策流程](directorial-shot-design.md#导演决策流程)核场景重点、调度与切/留/删并取舍，再逐Clip查必要覆盖；理解和注意力有主次，主观归属/可见范围与机位成立，不能以字数/景别词/增镜数代替；地标/轴线与位移一致；大幅度空间转移有明确切镜/分镜或甩镜交接，B空间有重新建立的落幅 | 导演方案/分镜/文字布局 |
| T5 声音与对白 | 对白逐句落入正确人物和beat；现场声有源，不附音色段落、语气随情境，听者有回应 | 音频/表演 |
| T6 连续与整场节奏 | 核心选择与余波有读清窗口，支撑过程不挤占重点；有意义的等待/静止成立，新相邻镜不重演事件；持物、伤势、气息延续，行动线缺席有依据 | 接缝/整场编排 |
| T6.1 穿帮高发点 | 按 [穿帮高发点逐项排查](director-compiler.md#穿帮高发点逐项排查) 核视点可见性、物理可达与手别、资源守恒、通行姿态、距离行程、进出介质；适用项均成立 | 导演编译/布局 |
| T7 生成分组 | 每个 Clip 的声明时长及片内时间轴均≤30秒，模型更短上限仍满足；超量按[压缩或顺延规则](narrative-planning.md#单个clip的30秒硬上限与超量处理)落实，无关键内容遗漏；上限内已评估兼容合并，短段有具体例外，生成时段与成片映射无漏计/重复 | 生成分配表 |
| T8 资产、风格与引用 | 每张场景的媒介、时代/建筑、材料和光色按项目参考进入正文，多个参考各有职责；环境内容划分和复用有依据，弃用图删除且无悬空；身份/调用名及图号/源图/作用时段可追溯 | 总表/对应提示词/视觉风格 |
| T9 格式、范围与版本 | 对应任务格式符合入口：完整视频四段式及内联声音/对白；概述用一句具体事件概括本段主要内容，与时间轴对应，无空泛导演套话、风格/运镜堆叠或后续剧透；四栏不复述独立资产形态/外观，必要状态、空间与动作关系保留。资产和原生任务用其格式；总时长及引用正确，用户范围和旧版保留性有检查记录 | 编译/项目记录 |

T1—T9是检查维度，不是要求每个镜头都包含全部内容。无人景观可将人物表演注明不适用，但镜内自然运动仍需核对；静音人物视频仍核表情、姿态和可见呼吸。

### 第二层：提交条件核验

| 检查项 | 通过条件与所需证据 | 未满足时 |
|---|---|---|
| B1 素材与绑定 | 每个实际附件、版本、用途和本次真实槽位对得上；无未提供的素材或虚构标签 | 待绑定/待素材；不称可提交 |
| B2 模型与模式 | 当前来源可核验，时长、模态、附件数、分辨率等符合实际模式；离线快照与待核能力如实区分 | 待核验；不能拿其他模型经验作证明 |
| B3 上游与执行范围 | 本次所依赖的设计已确认、输入无已知冲突；执行授权与费用边界明确 | 只阻塞受影响提交，不要求补齐全片实图 |

纯文字生成在模式支持且用户采用时，附件绑定可注明不适用；仍须核B2/B3。已确认文字参考不等于已有图片。

### 第三层：生成结果与成片验收

| 检查项 | 通过条件与所需证据 | 失败时 |
|---|---|---|
| V1 单段画面与演出 | 引用实际视频/帧及时间码，身份/结构/数量、表情动机与幅度、受力、遮挡和空间符合目标 | 按最小修复出口返工 |
| V2 声画 | 实际对白、说话人、口型与声音来源正确；已有音频输入按真实映射使用，情绪气息相符，关键对白可听清 | 局部声音/口型或演出修复 |
| V3 组接与全片 | 以实际剪辑检查接缝、无重复动作、状态/光色/声场、完整情绪段、追踪/揭示及净时长 | 回剪辑或对应上下游 |

只看静帧不能宣称动作或口型通过，只听音频不能宣称表情通过；单段通过不能宣称整集通过。精确节拍、动作自然度及AU执行需实际结果，文案不能保证。没有生成结果时保留该层待核验，不索要全套素材作为写文字稿的前置。

### 验收记录与复验

统一记录：

| 检查项/层级 | 适用范围与版本 | 正文/画面证据 | 四态结果及理由 | 修复位置/待办 | 复验依据 |
|---|---|---|---|---|---|
| T/B/V对应项 | Clip/样本/全片与时段 | 原句、文件或实际结果时间码 | 不使用无依据“已优化” | 源文件和受影响范围 | 重新运行或重新查看的证据 |

此表放既有 `project.md` 的检查小节，可由已有格式承载同等信息；资产状态仍在同一总表中维护。生成分组及映射同样留项目记录，复制用提示词只保留生成内容。结论分别写“文字层…；提交层…；结果层…”，不新增一轮用户逐项审批。

导演决策的人工回归情境（验证取舍依据，不是生成实测，也不是关键词门槛）：

| 输入情境 | 应有处理 | 失败信号 |
|---|---|---|
| 未指定拍法的求助、拒绝或犹豫 | 主动识别关系转折，比较双人持续观察、关键接触与听者切入，选择能读清策略的一套 | 只按用户点名拍法；自动脸/手/道具三连切，未说明关系变化 |
| 同一威胁可提前露出或随人物揭晓 | 继承锁定信息顺序，未锁时按悬念/惊奇体验选一个方案，角色知情另核 | 采用最丰富角度导致提前泄密，或所有方案直接相加 |
| 操作细节齐全但高潮不突出 | 排出重点与支撑，合并常规准备，留选择/结果窗口 | 用更多上弦、脚步、手部特写让本场重点继续变弱 |
| 人物在亲人离开后静止停留 | 核等待/失去与经过时间是否让关系或代价被感受到；有依据则保持构图 | 用静帧对照判失败，强加眨眼、摸脸或转身来填时间 |
| 人物帮忙但仍索要收益 | 摄影保留利益与含混，转变只有新选择和代价成立时才能呈现 | 用暖光、笑脸与心理注释宣布已经无私或已获对方信任 |
| 无人物的风景/产品/教程 | 以感知揭示、功能状态或理解变化定重点，选合适停留和交接 | 套用人物冲突与每段反转，或机械补脸手特写 |
| 人物向前跑、狼从身后追，她回头 | 明确人物眼位朝后、摄影机随人物向前移动；狼头近景露齿/鼻息接回跑动与稳刀 | 只加狼头形容词，或把追兵拍成迎面来狼，回切人已停步 |
| 弩手准备后射中巨物 | 真实上弦/装填前置，或继承已待发状态；释放细节、短轨迹、命中/余震连在同一次事件 | 已上弦又重复拉；把弩当弓；几秒箭飞行中让演员演完反应才命中 |
| 多条Clip单镜描写都很长 | 全批逐条识别威胁、操作、接触与反应是否需要另一个视角，新增或保留均有依据 | 只扩写首条、后段一律中近景，或机械每条增加同样特写 |
| 长对白、触布告别或固定机位 | 保留必要持续表演，通过已有镜内调度/目光/移焦交接信息 | 为凑角度切碎对白与告别，或违背锁定一镜到底 |
| 岩坡遮住狼，人物只能听到鼻息 | 客观插入可展示狼推进，人物只按能听见/看见的信息行动 | 把岩后的狼写成人物第一视角，看穿遮挡或提前知道位置 |

自动工具边界：`director_contract_lint.py`核四段式/时间轴/字面对白次数；`seedance_lint.py`核其已实现的引用与模型快照规则。二者不证明表演动机、真实绑定或成片效果；自动报告中的WARN逐项解释，不以零退出码替代验收。可计算的区间、引用、版本保留性应自动检查；语义与实际效果按本表提供人工核对证据。

## Tier 1 — Workflow Discipline

### Pre-Prompt Confirmation Gate

Confirm intent in short form before composing a long prompt;
when stuck, prefer one narrow question over three open-ended.

**When to apply:** Output longer than a few sentences, or any sub-skill triggering expensive downstream work.


### Explicit-Stop Between Phases

Multi-phase workflows don't collapse into one response; each
phase produces an artifact the next phase consumes.

**When to apply:** Stateful loops where intermediate artifacts need user confirmation.


### Inventory-Extraction Checklist Before Composing

Silently catalog what the user provided — who / where / doing
what / with what camera / mood — before composing.

**When to apply:** Sub-skills authoring prompts from free-form briefs.


### Iteration-is-craft

Iteration is part of production. One historical feature-production case
reported roughly 1% image acceptance and 1.5% video acceptance; these are
case observations, not defaults for other projects. Estimate the current
work from its own scope and evidence, and label uncertain assumptions.

**When to apply:** Any sub-skill that produces generative output; any
budgeting or planning conversation; any post-clip diagnostic.


### Lock-before-generate

Lock subject, scene, camera, lighting, and coverage decisions BEFORE
prompting — not during. Decisions made during the iteration loop drift
from the original intent; decisions made before lock as anchors that
the iteration loop tests against.

**When to apply:** Any multi-shot or multi-character output; any work
that needs to hold consistency across cuts.


### Plausibility-over-verification

When the agent has training-data knowledge of *how a platform usually works* (typical CLI flag shapes, common aspect ratios, generic prompt structure), it can produce output that *looks* correct without actually checking against ground truth. The plausible answer is not the verified answer; the discipline is to run the verification command that is sitting right there.

**When to apply:** Any sub-skill where the agent could pattern-match from training instead of reading the skill files or calling a verification surface. CLI param schemas, MCP tool params, platform-specific vocabulary, model enum values.


### Falsifiable Success Criteria

Define what "good output" looks like in falsifiable terms BEFORE
prompting, so the iteration loop has a stopping criterion. The
discipline prevents the post-hoc rationalization failure mode —
claiming success regardless of outcome because no specific test was
committed to up front.

**When to apply:** Any project-level or scene-level work where
"finished" is not self-evident.


### 跨批次资产名称检查

资产样本、视频样本及完整交付均执行 [项目资产总表](asset-registry.md)：读取同一份项目总表，核对调用名逐字一致、中文名称与身份一致、没有为同一对象重复登记，并如实标记待生成与待绑定项。实际平台槽位按生成片段对照文件，不以槽位替代项目调用名。

含调用名时运行 `seedance_lint.py --preflight --file /path/to/prompt.txt --asset-registry /path/to/project/asset-registry.json`。脚本核对表结构、重复项、未知调用名、大小写和待补齐状态；正文换称、实际文件及平台附件仍需核对。提示词内部声明通过，不等于跨批次名称已通过。

### 电影视觉参考检查

剧情场景资产或视频交付前核对：

- 是否读取当前项目美术设定，且项目记录、总表与提示词的来源版本一致？具体风格是否记录在该项目？
- 是否将片名落实为当前场景可见的光色、尺度、空间、材质，而非只写“大片感”“电影级”？
- 昼夜、季节和天气是否服从剧情，曝光与直射/漫射比例是否来自用户指定参考的地区和场景，画幅是否继承设置？
- 夜景是否保留必要地形、表情与动作信息，携带光源的照明变化是否归入对应视频动作？
- 是否保持人物身份和服装，避免自动引入参考电影的军队、载具、生物与地标？
- 场景是否仅含地形、建筑和固定空间结构，整张图无角色/群演/生物及家具、货物、日用品、器械、船只等道具，包括远景/倒影/剪影？被移出的物件落位是否进入视频，角色与B/P是否遵守各自独立背景规范？
- 本轮反馈是否落到相应光色或陈设维度，正文是否用具体可见事实表达并继承其他已确认项？
- 文字风格参考、实际参考图及已生成结果是否如实区分，未虚构上传或验收？

方法见 [电影视觉参考匹配](higgsfield-style.md#电影视觉参考匹配)。维护文档只核查规则与链接；实际图片质感需待生成后验收。

## Tier 2 — Output Discipline

### Visual-Marker-Only Output Discipline

Use current project names/registered handles for identity and references; describe visible
action and state changes without repeating asset appearance. Preserve confirmed identity
and age; this is not a blanket name/age ban or a reason to conceal facts.

**When to apply:** Any prompt for image or video generation.


### Triple-Redundant Runtime

Runtime settings remain outside the copyable prompt; timed beats must agree with the
declared duration. Distinguish generation length from net edit length; do not add a second
settings header inside the four-section body.

**When to apply:** Multi-shot or time-anchored output.


### Single-Variable Iteration

Change exactly one variable per regeneration. Multi-variable
iteration makes diagnosis impossible.

**When to apply:** Iteration on close-but-not-right generations.


### Diagnose From the Current Output

Inspect the supplied image or video against the intended action, framing,
identity and continuity. Describe visible evidence, separate observed defects
from hypotheses, and mark anything you cannot inspect as unverified.

Repeated identical defects suggest a prompt or reference problem: change one
variable. If the prompt and references already satisfy the scene, another take
may help; do not invent acceptance rates or promise a successful reroll.


### BAD/GOOD/GREAT

Show output gradients explicitly — BAD, GOOD, GREAT examples
side-by-side — so the reader sees the difference, not just hears
about it. The contrast is what teaches; a single GOOD example without
a BAD comparison reads as one possibility rather than a chosen
direction.

**When to apply:** Any template, vocabulary, or pattern entry where
quality has a recognizable gradient.


### Anti-Bombast

Production-direction register. Avoid marketing voice, performative
urgency, fake confidence, and adjective stacks that describe what the
output should *be* rather than what the prompt should *do*. Replace
`epic`, `beautiful`, `cinematic masterpiece`, `ultra realistic`,
`dramatic` with named physical mechanisms (`low-angle 35mm anamorphic
medium shot`, `warm practical key light from screen-left`).

**When to apply:** Any prompt-construction surface; any documentation
the model or the user reads.


## Tier 3 — Architectural Discipline

### 3-Stage Chain / 4-Phase Loop Architectural Pattern

Multi-step production decomposes into named stages where each
stage produces an artifact the next stage consumes. Common shapes:
3-stage chain (character → image → video) or 4-phase loop
(script → assets → blocking → prompts).

**When to apply:** Orchestrating multiple generation stages.


### Select Shared Constraints by Shot

Check shared constraints for the shot's actual risks and model/mode scope.
Keep established identity and continuity locks consistent; do not append
an entire library or repeat locks already expressed in the prompt.

**When to apply:** Preparing a prompt or checking consistency across shots.


### Strict-Order Workflow with Refusal-to-Skip Phases

Follow the root sample/phase workflow and existing user authorization. Unchanged confirmed
work is reused; no extra per-check approvals or full-image return gate is created here.
A text review is not visual acceptance, and actual execution depends on its own inputs.

**When to apply:** Numbered sequence where each step depends on the prior step's artifact.


### Pre-Delivery Discipline

Before delivering output to the user, run a self-repair pass against
a checklist of common failure modes — catch preventable issues at
construction time rather than after credit burn. The pass takes
60-90 seconds; the savings compound across iteration loops.

**When to apply:** Any sub-skill that produces a long-form artifact
(prompt, plan, template fill) where issues are easier to fix
pre-delivery than post-generation.


