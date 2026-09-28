# ipm 模块表清单

> 本模块共收录 **8** 张表定义，来自 `ipm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope ipm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ipm_basetask_info` | 事项任务信息-主表 | 19 | [ipm_basetask_info.md](./ipm_basetask_info.md) |
| 2 | `t_ipm_basetask_info_l` | 事项任务信息-多语言表 | 4 | [ipm_basetask_info.md](./ipm_basetask_info.md) |
| 3 | `t_ipm_basetask_type` | 事项任务类型-主表 | 16 | [ipm_basetask_type.md](./ipm_basetask_type.md) |
| 4 | `t_ipm_basetask_type_l` | 事项任务类型-多语言表 | 5 | [ipm_basetask_type.md](./ipm_basetask_type.md) |
| 5 | `t_ipm_project_participant` | 任务参与人-多选基础资料表 | 3 | [ipm_project_progress_bill.md](./ipm_project_progress_bill.md) |
| 6 | `t_ipm_project_progress` | IPO项目进度-主表 | 26 | [ipm_project_progress_bill.md](./ipm_project_progress_bill.md) |
| 7 | `t_ipm_reform` | IPO财务问题自查整改清单-主表 | 21 | [ipm_reform_bill.md](./ipm_reform_bill.md) |
| 8 | `t_ipm_reform_participant` | 任务参与人-多选基础资料表 | 3 | [ipm_reform_bill.md](./ipm_reform_bill.md) |
