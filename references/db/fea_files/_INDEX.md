# fea 模块表清单

> 本模块共收录 **28** 张表定义，来自 `fea_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category fea
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fea_configentry` | 单据体-子表 | 9 | [fea_exportpluginconfig.md](./fea_exportpluginconfig.md) |
| 2 | `t_fea_datatype` | 数据类型-主表 | 20 | [fea_datatype.md](./fea_datatype.md) |
| 3 | `t_fea_datatype_l` | 数据类型-多语言表 | 5 | [fea_datatype.md](./fea_datatype.md) |
| 4 | `t_fea_element` | 数据元素-主表 | 18 | [fea_element.md](./fea_element.md) |
| 5 | `t_fea_element_l` | 数据元素-多语言表 | 4 | [fea_element.md](./fea_element.md) |
| 6 | `t_fea_exportlog` | 自定义档案项-主表 | 8 | [fea_custom_key.md](./fea_custom_key.md) |
| 7 | `t_fea_exportlog` | 自定义档案值-主表 | 8 | [fea_custom_value.md](./fea_custom_value.md) |
| 8 | `t_fea_exportlog` | 导出文件记录-主表 | 8 | [fea_exportlog.md](./fea_exportlog.md) |
| 9 | `t_fea_exportlog_l` | 自定义档案项-多语言表 | 4 | [fea_custom_key.md](./fea_custom_key.md) |
| 10 | `t_fea_exportlog_l` | 自定义档案值-多语言表 | 4 | [fea_custom_value.md](./fea_custom_value.md) |
| 11 | `t_fea_exportlog_l` | 导出文件记录-多语言表 | 4 | [fea_exportlog.md](./fea_exportlog.md) |
| 12 | `t_fea_exportpageconfig` | 分片导出配置-主表 | 7 | [fea_exportpageconfig.md](./fea_exportpageconfig.md) |
| 13 | `t_fea_exportpluginconfig` | 导出元素插件服务配置-主表 | 2 | [fea_exportpluginconfig.md](./fea_exportpluginconfig.md) |
| 14 | `t_fea_exporttask` | 导出任务-主表 | 13 | [fea_export_task.md](./fea_export_task.md) |
| 15 | `t_fea_exporttaskentry` | 任务明细-子表 | 17 | [fea_export_task.md](./fea_export_task.md) |
| 16 | `t_fea_plan` | 导出方案-主表 | 19 | [fea_plan.md](./fea_plan.md) |
| 17 | `t_fea_plan_l` | 导出方案-多语言表 | 4 | [fea_plan.md](./fea_plan.md) |
| 18 | `t_fea_plan_m` | 导出方案-使用范围位图表 | 2 | [fea_plan.md](./fea_plan.md) |
| 19 | `t_fea_plan_u` | 导出方案-使用范围表 | 3 | [fea_plan.md](./fea_plan.md) |
| 20 | `t_fea_planentry` | 单据体-子表 | 5 | [fea_plan.md](./fea_plan.md) |
| 21 | `t_fea_standard` | 文件标准-主表 | 12 | [fea_standard.md](./fea_standard.md) |
| 22 | `t_fea_standard_l` | 文件标准-多语言表 | 4 | [fea_standard.md](./fea_standard.md) |
| 23 | `t_fea_standardentry` | 详细信息-子表 | 5 | [fea_standard.md](./fea_standard.md) |
| 24 | `t_fea_standardsubentry` | XML声明子单据-子表 | 5 | [fea_standard.md](./fea_standard.md) |
| 25 | `t_fea_structure` | 数据结构-主表 | 19 | [fea_datastructure.md](./fea_datastructure.md) |
| 26 | `t_fea_structure_l` | 数据结构-多语言表 | 4 | [fea_datastructure.md](./fea_datastructure.md) |
| 27 | `t_fea_structureentry` | 树形单据体-子表 | 10 | [fea_datastructure.md](./fea_datastructure.md) |
| 28 | `t_fea_tasksubentry` | 子单据体-子表 | 11 | [fea_export_task.md](./fea_export_task.md) |
