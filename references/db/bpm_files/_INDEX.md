# bpm 模块表清单

> 本模块共收录 **13** 张表定义，来自 `bpm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category bpm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bpm_billrelationtype` | 单据关系类型-主表 | 9 | [bpm_billrelationtype.md](./bpm_billrelationtype.md) |
| 2 | `t_bpm_billrelationtype_l` | 单据关系类型-多语言表 | 5 | [bpm_billrelationtype.md](./bpm_billrelationtype.md) |
| 3 | `t_bpm_execonversion` | 实例转换-主表 | 13 | [bpm_execonversion.md](./bpm_execonversion.md) |
| 4 | `t_bpm_relationmodel` | 单据关系配置-主表 | 11 | [bpm_billrelationmodel.md](./bpm_billrelationmodel.md) |
| 5 | `t_bpm_relationmodel_l` | 单据关系配置-多语言表 | 5 | [bpm_billrelationmodel.md](./bpm_billrelationmodel.md) |
| 6 | `t_wf_execution` | 流程实例-主表 | 51 | [wf_execution_tree.md](./wf_execution_tree.md) |
| 7 | `t_wf_execution_l` | 流程实例-多语言表 | 10 | [wf_execution_tree.md](./wf_execution_tree.md) |
| 8 | `t_wf_hiprocinst` | 历史流程-主表 | 36 | [bpm_historicalprocess.md](./bpm_historicalprocess.md) |
| 9 | `t_wf_hiprocinst_l` | 历史流程-多语言表 | 10 | [bpm_historicalprocess.md](./bpm_historicalprocess.md) |
| 10 | `t_wf_processevent` | 流程内事件-主表 | 6 | [wf_processevent.md](./wf_processevent.md) |
| 11 | `t_wf_processevent_l` | 流程内事件-多语言表 | 5 | [wf_processevent.md](./wf_processevent.md) |
| 12 | `t_wf_processevententry` | 单据体-子表 | 6 | [wf_processevent.md](./wf_processevent.md) |
| 13 | `t_wf_processevententry_l` | 单据体-多语言表 | 5 | [wf_processevent.md](./wf_processevent.md) |
