# fcs 模块表清单

> 本模块共收录 **55** 张表定义，来自 `fcs_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category fcs
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fcs_archiverecord` | 归档记录-主表 | 18 | [fcs_archiverecord.md](./fcs_archiverecord.md) |
| 2 | `t_fcs_archivesetting` | 归档配置-主表 | 20 | [fcs_archivesetting.md](./fcs_archivesetting.md) |
| 3 | `t_fcs_archivesetting_l` | 归档配置-多语言表 | 4 | [fcs_archivesetting.md](./fcs_archivesetting.md) |
| 4 | `t_fcs_bankquerydetail` | 同步状态时同步交易明细记录-主表 | 14 | [fcs_bankquerydetail.md](./fcs_bankquerydetail.md) |
| 5 | `t_fcs_changehistory` | 单据历史版本记录表-主表 | 21 | [fcs_changehistory.md](./fcs_changehistory.md) |
| 6 | `t_fcs_checkctrl` | 支付防重-主表 | 35 | [fcs_checkctrl.md](./fcs_checkctrl.md) |
| 7 | `t_fcs_checkctrl_amtctrl` | 规则单据体-子表 | 15 | [fcs_checkctrl.md](./fcs_checkctrl.md) |
| 8 | `t_fcs_checkctrl_amtctrl` | 规则单据体-子表 | 15 | [fcs_repeatecheck.md](./fcs_repeatecheck.md) |
| 9 | `t_fcs_checkctrl_l` | 支付防重-多语言表 | 7 | [fcs_checkctrl.md](./fcs_checkctrl.md) |
| 10 | `t_fcs_checkctrl_subamt` | 子单据体-子表 | 9 | [fcs_checkctrl.md](./fcs_checkctrl.md) |
| 11 | `t_fcs_checkctrl_subamt` | 子单据体-子表 | 9 | [fcs_repeatecheck.md](./fcs_repeatecheck.md) |
| 12 | `t_fcs_datasnap` | 数据快照-主表 | 24 | [fcs_datasnap.md](./fcs_datasnap.md) |
| 13 | `t_fcs_datasnap_l` | 数据快照-多语言表 | 5 | [fcs_datasnap.md](./fcs_datasnap.md) |
| 14 | `t_fcs_payaccess` | 支付准入-主表 | 27 | [fcs_payaccess.md](./fcs_payaccess.md) |
| 15 | `t_fcs_payaccess_bl` | 支付准入严控单据清单-主表 | 17 | [fcs_payaccess_blacklist.md](./fcs_payaccess_blacklist.md) |
| 16 | `t_fcs_payaccess_bl_l` | 支付准入严控单据清单-多语言表 | 5 | [fcs_payaccess_blacklist.md](./fcs_payaccess_blacklist.md) |
| 17 | `t_fcs_payaccess_l` | 支付准入-多语言表 | 5 | [fcs_payaccess.md](./fcs_payaccess.md) |
| 18 | `t_fcs_payaccess_newparam` | 支付准入新增参数设置-主表 | 16 | [fcs_payaccess_newparam.md](./fcs_payaccess_newparam.md) |
| 19 | `t_fcs_payaccess_newparam_l` | 支付准入新增参数设置-多语言表 | 5 | [fcs_payaccess_newparam.md](./fcs_payaccess_newparam.md) |
| 20 | `t_fcs_payaccess_record` | 支付链路数据-主表 | 32 | [fcs_payaccess_record.md](./fcs_payaccess_record.md) |
| 21 | `t_fcs_payaccess_record_h` | 支付链路数据_归档-主表 | 32 | [fcs_payaccess_record_h.md](./fcs_payaccess_record_h.md) |
| 22 | `t_fcs_payaccess_record_h_l` | 支付链路数据_归档-多语言表 | 5 | [fcs_payaccess_record_h.md](./fcs_payaccess_record_h.md) |
| 23 | `t_fcs_payaccess_record_l` | 支付链路数据-多语言表 | 5 | [fcs_payaccess_record.md](./fcs_payaccess_record.md) |
| 24 | `t_fcs_payaccess_set` | 支付准入链路控制-主表 | 18 | [fcs_payaccess_set.md](./fcs_payaccess_set.md) |
| 25 | `t_fcs_payaccess_set_l` | 支付准入链路控制-多语言表 | 5 | [fcs_payaccess_set.md](./fcs_payaccess_set.md) |
| 26 | `t_fcs_paytracelog` | 支付链路日志-主表 | 24 | [fcs_paytracelog.md](./fcs_paytracelog.md) |
| 27 | `t_fcs_paytracelog_h` | 支付链路日志_归档-主表 | 24 | [fcs_paytracelog_h.md](./fcs_paytracelog_h.md) |
| 28 | `t_fcs_repeatctrl_wl` | 防重服务白名单-主表 | 18 | [fcs_repeatctrl_whitelist.md](./fcs_repeatctrl_whitelist.md) |
| 29 | `t_fcs_repeatctrl_wl_l` | 防重服务白名单-多语言表 | 5 | [fcs_repeatctrl_whitelist.md](./fcs_repeatctrl_whitelist.md) |
| 30 | `t_fcs_repeatctrllog` | 防重服务日志-主表 | 20 | [fcs_repeatctrllog.md](./fcs_repeatctrllog.md) |
| 31 | `t_fcs_repeatctrllog_h` | 防重服务日志_归档-主表 | 19 | [fcs_repeatctrllog_h.md](./fcs_repeatctrllog_h.md) |
| 32 | `t_fcs_repeatecheck` | 重复控制设置-主表 | 0 | [fcs_repeatecheck.md](./fcs_repeatecheck.md) |
| 33 | `t_fcs_repeatecheck_l` | 重复控制设置-多语言表 | 0 | [fcs_repeatecheck.md](./fcs_repeatecheck.md) |
| 34 | `t_fcs_snapschedule` | 调度任务-主表 | 23 | [fcs_snapschedule.md](./fcs_snapschedule.md) |
| 35 | `t_fcs_snapschedule_l` | 调度任务-多语言表 | 5 | [fcs_snapschedule.md](./fcs_snapschedule.md) |
| 36 | `t_fcs_suspectbill` | 疑似重复单据-主表 | 18 | [fcs_suspectbill.md](./fcs_suspectbill.md) |
| 37 | `t_fcs_suspectbill_l` | 疑似重复单据-多语言表 | 4 | [fcs_suspectbill.md](./fcs_suspectbill.md) |
| 38 | `t_fcs_suspectbill_s` | 疑似重复单据体-子表 | 8 | [fcs_suspectbill.md](./fcs_suspectbill.md) |
| 39 | `t_fcs_suspectbill_s_l` | 疑似重复单据体-多语言表 | 4 | [fcs_suspectbill.md](./fcs_suspectbill.md) |
| 40 | `t_fcs_suspectlog` | 疑似防重日志-主表 | 15 | [fcs_suspectlog.md](./fcs_suspectlog.md) |
| 41 | `t_fcs_suspectlog_entry` | 日志信息-子表 | 6 | [fcs_suspectlog.md](./fcs_suspectlog.md) |
| 42 | `t_fcs_suspectlog_entry_h` | 日志信息-子表 | 6 | [fcs_suspectlog_h.md](./fcs_suspectlog_h.md) |
| 43 | `t_fcs_suspectlog_h` | 疑似防重日志_归档-主表 | 15 | [fcs_suspectlog_h.md](./fcs_suspectlog_h.md) |
| 44 | `t_fcs_suspectset` | 疑似防重配置-主表 | 25 | [fcs_suspectset.md](./fcs_suspectset.md) |
| 45 | `t_fcs_suspectset_l` | 疑似防重配置-多语言表 | 8 | [fcs_suspectset.md](./fcs_suspectset.md) |
| 46 | `t_fcs_suspectset_m` | 匹配方案-子表 | 12 | [fcs_suspectset.md](./fcs_suspectset.md) |
| 47 | `t_fcs_taskexecute_log` | 执行日志-主表 | 0 | [fcs_taskexecute_log.md](./fcs_taskexecute_log.md) |
| 48 | `t_fcs_taskexecute_log_l` | 执行日志-多语言表 | 0 | [fcs_taskexecute_log.md](./fcs_taskexecute_log.md) |
| 49 | `t_fcs_taskflow` | 任务编排-主表 | 28 | [fcs_taskflow.md](./fcs_taskflow.md) |
| 50 | `t_fcs_taskflow_l` | 任务编排-多语言表 | 5 | [fcs_taskflow.md](./fcs_taskflow.md) |
| 51 | `t_fcs_taskflow_org` | 组织单据体-子表 | 4 | [fcs_taskflow.md](./fcs_taskflow.md) |
| 52 | `t_fcs_taskflow_task` | 任务流单据体-子表 | 13 | [fcs_taskflow.md](./fcs_taskflow.md) |
| 53 | `t_fcs_tdalog` | 决策分析日志-主表 | 20 | [fcs_tdalog.md](./fcs_tdalog.md) |
| 54 | `t_fcs_tdalog_h` | 决策分析日志_归档-主表 | 20 | [fcs_tdalog_h.md](./fcs_tdalog_h.md) |
| 55 | `t_repeateccheckuser` | 消息接收人-多选基础资料表 | 0 | [fcs_repeatecheck.md](./fcs_repeatecheck.md) |
