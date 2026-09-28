# botp 模块表清单

> 本模块共收录 **29** 张表定义，来自 `botp_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category botp
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bos_report_record` | 监控报告中心-主表 | 8 | [bos_report_record.md](./bos_report_record.md) |
| 2 | `t_bos_report_record` | 报告记录-主表 | 8 | [bos_report_record_new.md](./bos_report_record_new.md) |
| 3 | `t_bos_report_registcenter` | 监控注册中心-主表 | 8 | [bos_report_regist.md](./bos_report_regist.md) |
| 4 | `t_botp_bill_rule_record` | 单据_转换规则记录-主表 | 9 | [botp_bill_rule_record.md](./botp_bill_rule_record.md) |
| 5 | `t_botp_convert_watch` | 单据转换报告-主表 | 17 | [botp_convertwatch.md](./botp_convertwatch.md) |
| 6 | `t_botp_convertpath_param` | 转换路线参数-主表 | 16 | [botp_convertpath_param.md](./botp_convertpath_param.md) |
| 7 | `t_botp_convertpath_param_l` | 转换路线参数-多语言表 | 4 | [botp_convertpath_param.md](./botp_convertpath_param.md) |
| 8 | `t_botp_convertrule` | 转换规则-主表 | 21 | [botp_crlist.md](./botp_crlist.md) |
| 9 | `t_botp_convertrule` | 签入转换规则-主表 | 21 | [botp_crlistcheckin.md](./botp_crlistcheckin.md) |
| 10 | `t_botp_convertrule_l` | 转换规则-多语言表 | 5 | [botp_crlist.md](./botp_crlist.md) |
| 11 | `t_botp_convertrule_l` | 签入转换规则-多语言表 | 5 | [botp_crlistcheckin.md](./botp_crlistcheckin.md) |
| 12 | `t_botp_convertrule_s` | 转换规则-分表 | 3 | [botp_crlist.md](./botp_crlist.md) |
| 13 | `t_botp_convertrule_s` | 签入转换规则-分表 | 3 | [botp_crlistcheckin.md](./botp_crlistcheckin.md) |
| 14 | `t_botp_convertrulever` | 转换规则版本-主表 | 13 | [botp_convertrulever.md](./botp_convertrulever.md) |
| 15 | `t_botp_convertrulever_l` | 转换规则版本-多语言表 | 4 | [botp_convertrulever.md](./botp_convertrulever.md) |
| 16 | `t_botp_entrytracker` | 反写快照-主表 | 0 | [botp_snapshot.md](./botp_snapshot.md) |
| 17 | `t_botp_entrytracker` | 反写快照_业务跟踪-主表 | 0 | [botp_snapshot_tc.md](./botp_snapshot_tc.md) |
| 18 | `t_botp_link_log` | 关联关系日志（废弃）-主表 | 16 | [botp_link_log.md](./botp_link_log.md) |
| 19 | `t_botp_linkdeleted_record` | 关联关系删除记录-主表 | 12 | [link_deleted_record.md](./link_deleted_record.md) |
| 20 | `t_botp_log` | 反写日志-主表 | 0 | [botp_log.md](./botp_log.md) |
| 21 | `t_botp_writeback_watch` | 单据反写报告-主表 | 16 | [botp_writebackwatch.md](./botp_writebackwatch.md) |
| 22 | `t_botp_writebackrule` | 反写规则-主表 | 20 | [botp_writebackrule.md](./botp_writebackrule.md) |
| 23 | `t_botp_writebackrule` | 签入反写规则-主表 | 20 | [botp_wrlistcheckin.md](./botp_wrlistcheckin.md) |
| 24 | `t_botp_writebackrule_l` | 反写规则-多语言表 | 5 | [botp_writebackrule.md](./botp_writebackrule.md) |
| 25 | `t_botp_writebackrule_l` | 签入反写规则-多语言表 | 5 | [botp_wrlistcheckin.md](./botp_wrlistcheckin.md) |
| 26 | `t_botp_writebackrule_s` | 反写规则-分表 | 2 | [botp_writebackrule.md](./botp_writebackrule.md) |
| 27 | `t_botp_writebackrule_s` | 签入反写规则-分表 | 2 | [botp_wrlistcheckin.md](./botp_wrlistcheckin.md) |
| 28 | `t_botp_writebacksnap` | 反写记录单据体-子表 | 0 | [botp_snapshot.md](./botp_snapshot.md) |
| 29 | `t_botp_writebacksnap` | 反写快照_反写条目-主表 | 0 | [botp_snapshot_wb.md](./botp_snapshot_wb.md) |
