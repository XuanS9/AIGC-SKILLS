# 模型规格维护：离线快照不是在线能力证明

本包的 `model-specs.json`、`image-model-specs.json`、`audio-model-specs.json` 是带日期的离线参数快照；对应Markdown是便于查阅的摘要。默认模型和项目30秒上限是本工作室策略，不等于当前平台能力承诺。

## 当前来源边界

JSON记录 `snapshot_date`、`snapshot_file`、`snapshot_sha256`。这些SHA指向历史原始导出，不是规范化JSON自己的哈希。本包未包含那些原始导出及原转换器，因此不能从现有JSON证明原始来源哈希正确，不能反向编造原始快照，也不能只修改日期让旧数据看似新鲜。

本轮代码/文档修复保持原模型JSON字节不变。没有实时schema或用户提供的新导出时，B2提交条件仍为待核验；本地枚举检查仅说明“符合/不符合所加载快照”。

## 执行前核验

1. 只读所选输出类型和模型条目，确认来源日期、ID、模式、时长范围/离散档位、分辨率、画幅、附件职责和组合限制。
2. 超过30天、来源缺失、日期非法或未来日期时不称当前能力已核验。可用实际已安装的Higgsfield CLI/MCP核schema，或请用户提供当前导出，不能把文档里的命令当已执行。
3. 当前schema与旧快照不同，以实际模型/模式schema为执行依据；先报告受影响参数，再同步正文、时长和引用，不擅自改变确认剧情。
4. 未能取得新来源时仍可完成文字稿和本地检查，明确缺证据；不宣称“可提交”或生成已完成。

## 新导出的可复现更新

- 保留用户提供的原始导出、取得日期与工具/接口版本，并计算原文件SHA-256；来源敏感信息清理与转换要另留记录。原始导出可在维护归档，不强制放进Skill运行目录。
- 本地模型lint接受规范化JSON：顶层 `models` 数组；模型包含 `id`、`name`，适用的 `aliases`、`duration`、`resolutions`、`modes`、`aspect_ratios`、`params`、`constraints`。原始CLI/MCP导出若结构不同，应显式转换并记录转换代码；不要假设任意响应都能直接用作 `--specs`。
- 更新记录至少含原文件哈希、转换器版本/哈希、转换后JSON哈希、来源日期和变更模型列表；未知参数留未知，不凭其他模型推导。
- 先用 `--specs /path/to/new-model-specs.json` 进行隔离检查，跑合法/非法参数回归，再经授权替换对应JSON并同步Markdown摘要。三模态分开更新，不因视频换版覆盖图像/音频资料。

```bash
python3 scripts/seedance_lint.py --preflight --model seedance_2_5 --mode omni_reference --duration 8 --ar 16:9 --resolution 720p --specs /path/to/new-model-specs.json --file /path/to/video.txt
python3 -m unittest discover -s scripts/tests -p 'test_*.py'
```

真实素材绑定、平台费用/权限、最新内容政策和生成效果仍须分别核验。本地PASS或WARN不是平台接受预测。
