# bal 模块表清单

> 本模块共收录 **24** 张表定义，来自 `bal_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category bal
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bal_auto_repair` | 自动巡检重算-主表 | 7 | [bal_auto_repair.md](./bal_auto_repair.md) |
| 2 | `t_bal_balanceinfo` | 余额表-主表 | 17 | [bal_balanceinfo.md](./bal_balanceinfo.md) |
| 3 | `t_bal_balanceinfo_l` | 余额表-多语言表 | 5 | [bal_balanceinfo.md](./bal_balanceinfo.md) |
| 4 | `t_bal_balancelog` | 余额更新日志-主表 | 12 | [bal_balance_log.md](./bal_balance_log.md) |
| 5 | `t_bal_balancelogentry` | 日志详情-子表 | 12 | [bal_balance_log.md](./bal_balance_log.md) |
| 6 | `t_bal_cfg` | 余额模型参数-主表 | 31 | [bal_config.md](./bal_config.md) |
| 7 | `t_bal_check_repair` | 余额巡检重算-主表 | 18 | [bal_check_repair.md](./bal_check_repair.md) |
| 8 | `t_bal_check_repair_mark` | 余额巡检重算增量标记-主表 | 6 | [bal_check_repair_mark.md](./bal_check_repair_mark.md) |
| 9 | `t_bal_check_repair_st` | 余额巡检重算条件-主表 | 5 | [bal_check_repair_setting.md](./bal_check_repair_setting.md) |
| 10 | `t_bal_check_repair_st_e` | 规则信息-子表 | 7 | [bal_check_repair_setting.md](./bal_check_repair_setting.md) |
| 11 | `t_bal_check_repair_task` | 余额巡检重算任务-主表 | 23 | [bal_check_repair_task.md](./bal_check_repair_task.md) |
| 12 | `t_bal_check_task` | 余额检查任务-主表 | 9 | [bal_check_task.md](./bal_check_task.md) |
| 13 | `t_bal_error_log` | 异步处理错误日志-主表 | 10 | [bal_error_log.md](./bal_error_log.md) |
| 14 | `t_bal_keycols` | 待重算的KEYCOL-主表 | 3 | [bal_keycols.md](./bal_keycols.md) |
| 15 | `t_bal_logic_col` | 余额规则逻辑字段-主表 | 6 | [bal_logic_col.md](./bal_logic_col.md) |
| 16 | `t_bal_logic_col_l` | 余额规则逻辑字段-多语言表 | 4 | [bal_logic_col.md](./bal_logic_col.md) |
| 17 | `t_bal_occurred_dbs` | 余额更新发生记录-主表 | 7 | [bal_occurred_dbs.md](./bal_occurred_dbs.md) |
| 18 | `t_bal_recal_log` | 余额重算日志-主表 | 0 | [bal_recal_log.md](./bal_recal_log.md) |
| 19 | `t_bal_snapshot` | 余额快照表-主表 | 0 | [bal_snapshot.md](./bal_snapshot.md) |
| 20 | `t_bal_sparse_seq` | 稀疏序列-主表 | 10 | [bal_sparse_seq.md](./bal_sparse_seq.md) |
| 21 | `t_bal_updateruledesign` | 余额更新规则列表-主表 | 21 | [bal_balanceupdaterule.md](./bal_balanceupdaterule.md) |
| 22 | `t_bal_updateruledesign_l` | 余额更新规则列表-多语言表 | 6 | [bal_balanceupdaterule.md](./bal_balanceupdaterule.md) |
| 23 | `t_bal_updateruledesign_s` | 余额更新规则列表-分表 | 2 | [bal_balanceupdaterule.md](./bal_balanceupdaterule.md) |
| 24 | `t_bal_updating` | 更新中单据-主表 | 11 | [bal_part_async_bills.md](./bal_part_async_bills.md) |
