# receipt 模块表清单

> 本模块共收录 **28** 张表定义，来自 `receipt_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope receipt
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_aqap_bank_login` | 回单前置机配置-主表 | 15 | [receipt_bank_login.md](./receipt_bank_login.md) |
| 2 | `t_aqap_bank_login_l` | 回单前置机配置-多语言表 | 5 | [receipt_bank_login.md](./receipt_bank_login.md) |
| 3 | `t_receipt_bd_match_param` | 维护匹配字段-主表 | 12 | [receipt_bd_match_param.md](./receipt_bd_match_param.md) |
| 4 | `t_receipt_bd_match_param_l` | 维护匹配字段-多语言表 | 4 | [receipt_bd_match_param.md](./receipt_bd_match_param.md) |
| 5 | `t_receipt_bd_match_rule` | 银行回单匹配规则-主表 | 11 | [receipt_bd_match_rule.md](./receipt_bd_match_rule.md) |
| 6 | `t_receipt_bd_match_rule_l` | 银行回单匹配规则-多语言表 | 4 | [receipt_bd_match_rule.md](./receipt_bd_match_rule.md) |
| 7 | `t_receipt_connect_monitor` | 回单下载连接监控-主表 | 19 | [receipt_connect_monitor.md](./receipt_connect_monitor.md) |
| 8 | `t_receipt_connect_monitor_l` | 回单下载连接监控-多语言表 | 4 | [receipt_connect_monitor.md](./receipt_connect_monitor.md) |
| 9 | `t_receipt_defect_stats` | 回单缺失报表查询-主表 | 18 | [receipt_defect_sta_by_mon.md](./receipt_defect_sta_by_mon.md) |
| 10 | `t_receipt_detail` | 回单详情-主表 | 36 | [receipt_detail.md](./receipt_detail.md) |
| 11 | `t_receipt_detail` | 回单结果列表-主表 | 36 | [receipt_result.md](./receipt_result.md) |
| 12 | `t_receipt_download_task` | 回单任务-主表 | 32 | [receipt_download_task.md](./receipt_download_task.md) |
| 13 | `t_receipt_download_task` | 回单缺失详情-主表 | 32 | [receipt_task_defect.md](./receipt_task_defect.md) |
| 14 | `t_receipt_info` | 回单信息-主表 | 18 | [receipt_info.md](./receipt_info.md) |
| 15 | `t_receipt_json` | 回单报文-主表 | 14 | [receipt_json.md](./receipt_json.md) |
| 16 | `t_receipt_reconcilia_task` | 对账单任务-主表 | 22 | [reconcilia_download_task.md](./reconcilia_download_task.md) |
| 17 | `t_receipt_remote_file` | 前置机文件列表-主表 | 20 | [receipt_remote_bank_login.md](./receipt_remote_bank_login.md) |
| 18 | `t_receipt_remote_file` | 远程SFTP文件-主表 | 20 | [receipt_remote_sftp_file.md](./receipt_remote_sftp_file.md) |
| 19 | `t_receipt_remote_file_l` | 前置机文件列表-多语言表 | 5 | [receipt_remote_bank_login.md](./receipt_remote_bank_login.md) |
| 20 | `t_receipt_remote_file_l` | 远程SFTP文件-多语言表 | 5 | [receipt_remote_sftp_file.md](./receipt_remote_sftp_file.md) |
| 21 | `t_receipt_statistics` | 按天和账户统计-主表 | 28 | [receipt_stats_by_ac_day.md](./receipt_stats_by_ac_day.md) |
| 22 | `t_receipt_statistics` | 按月和账户统计-主表 | 28 | [receipt_stats_by_ac_mon.md](./receipt_stats_by_ac_mon.md) |
| 23 | `t_receipt_statistics` | 按天和银行统计-主表 | 28 | [receipt_stats_by_bk_day.md](./receipt_stats_by_bk_day.md) |
| 24 | `t_receipt_statistics` | 按月和银行统计-主表 | 28 | [receipt_stats_by_bk_mon.md](./receipt_stats_by_bk_mon.md) |
| 25 | `t_receipt_statistics` | 按天统计-主表 | 28 | [receipt_stats_by_day.md](./receipt_stats_by_day.md) |
| 26 | `t_receipt_statistics` | 统计父页面-主表 | 28 | [receipt_stats_parent.md](./receipt_stats_parent.md) |
| 27 | `t_reconciliation_detail` | 对账单详情-主表 | 32 | [reconciliation_detail.md](./reconciliation_detail.md) |
| 28 | `t_reconciliation_detail` | 对账单结果列表-主表 | 32 | [reconciliation_result.md](./reconciliation_result.md) |
