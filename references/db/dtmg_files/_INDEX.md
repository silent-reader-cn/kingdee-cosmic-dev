# dtmg 模块表清单

> 本模块共收录 **25** 张表定义，来自 `dtmg_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category dtmg
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_dtmg_dc_billquantattach` | 附件-附件表 | 3 | [dtmg_datachecker_tasks.md](./dtmg_datachecker_tasks.md) |
| 2 | `t_dtmg_dc_billquanttasks` | 单据数量校对任务差异记录-子表 | 17 | [dtmg_datachecker_tasks.md](./dtmg_datachecker_tasks.md) |
| 3 | `t_dtmg_dc_billquanttasks` | 单据数量校对任务差异记录-子表 | 17 | [dtmg_dc_createtasks.md](./dtmg_dc_createtasks.md) |
| 4 | `t_dtmg_dc_datachekers` | 校对器-主表 | 18 | [dtmg_datachecker.md](./dtmg_datachecker.md) |
| 5 | `t_dtmg_dc_datachekers` | 校对器基础资料-主表 | 18 | [dtmg_datachecker_basedata.md](./dtmg_datachecker_basedata.md) |
| 6 | `t_dtmg_dc_exceltasks` | Excel校对任务差异记录-子表 | 32 | [dtmg_datachecker_tasks.md](./dtmg_datachecker_tasks.md) |
| 7 | `t_dtmg_dc_tasks` | 校对任务-主表 | 20 | [dtmg_datachecker_tasks.md](./dtmg_datachecker_tasks.md) |
| 8 | `t_dtmg_dc_tasks` | 创建校对任务-主表 | 20 | [dtmg_dc_createtasks.md](./dtmg_dc_createtasks.md) |
| 9 | `t_dtmg_initimport` | 快速初始化数据迁移-主表 | 18 | [dtmg_initdata_import.md](./dtmg_initdata_import.md) |
| 10 | `t_dtmg_initimport_l` | 快速初始化数据迁移-多语言表 | 4 | [dtmg_initdata_import.md](./dtmg_initdata_import.md) |
| 11 | `t_dtmg_initimportentry` | 初始化导入分录-子表 | 34 | [dtmg_initdata_import.md](./dtmg_initdata_import.md) |
| 12 | `t_dtmg_initimportentry_ot` | 重传附件-附件表 | 3 | [dtmg_initdata_import.md](./dtmg_initdata_import.md) |
| 13 | `t_dtmg_mighandlerlog` | 数据迁移后置器日志-主表 | 10 | [dtmg_mig_handler_log.md](./dtmg_mig_handler_log.md) |
| 14 | `t_dtmg_migparam` | 数据迁移参数过程-主表 | 3 | [dtmg_migrationparamdata.md](./dtmg_migrationparamdata.md) |
| 15 | `t_dtmg_migrationtask` | 数据迁移任务-主表 | 28 | [dtmg_datamigration_task.md](./dtmg_datamigration_task.md) |
| 16 | `t_dtmg_migrationtask` | 迁移任务基础资料-主表 | 28 | [dtmg_mig_task_base.md](./dtmg_mig_task_base.md) |
| 17 | `t_dtmg_migrationtask_atta` | 附件-附件表 | 3 | [dtmg_datamigration_task.md](./dtmg_datamigration_task.md) |
| 18 | `t_dtmg_migrationtask_l` | 迁移任务基础资料-多语言表 | 4 | [dtmg_mig_task_base.md](./dtmg_mig_task_base.md) |
| 19 | `t_dtmg_migrationtask_list` | 单据体-子表 | 22 | [dtmg_datamigration_task.md](./dtmg_datamigration_task.md) |
| 20 | `t_dtmg_objparallelentry` | 单据并行数量-子表 | 5 | [dtmg_validatorcfg.md](./dtmg_validatorcfg.md) |
| 21 | `t_dtmg_validatorcfg` | 数据迁移任务配置-主表 | 19 | [dtmg_validatorcfg.md](./dtmg_validatorcfg.md) |
| 22 | `t_dtmg_validatorcfg_l` | 数据迁移任务配置-多语言表 | 5 | [dtmg_validatorcfg.md](./dtmg_validatorcfg.md) |
| 23 | `t_dtmg_validatorcfgentry` | 单据体-子表 | 6 | [dtmg_validatorcfg.md](./dtmg_validatorcfg.md) |
| 24 | `t_dtmg_validatorcfgentry_l` | 单据体-多语言表 | 4 | [dtmg_validatorcfg.md](./dtmg_validatorcfg.md) |
| 25 | `t_dtmg_wisecustmdata` | 数据迁移WISE自定义数据-主表 | 9 | [dtmg_wisecustmdata.md](./dtmg_wisecustmdata.md) |
