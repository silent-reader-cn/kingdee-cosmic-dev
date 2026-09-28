# sys 模块表清单

> 本模块共收录 **82** 张表定义，来自 `sys_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category sys
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bas_attachment_oplog` | 文件操作日志-主表 | 21 | [bos_attachment_oplog.md](./bos_attachment_oplog.md) |
| 2 | `t_bas_attachment_oplog_l` | 文件操作日志-多语言表 | 4 | [bos_attachment_oplog.md](./bos_attachment_oplog.md) |
| 3 | `t_bas_bill_file_mapping` | 单据文件映射关系-主表 | 15 | [bos_bill_file_mapping.md](./bos_bill_file_mapping.md) |
| 4 | `t_bas_cloudhubapp` | 协同云应用-主表 | 13 | [bos_cloudhubapp.md](./bos_cloudhubapp.md) |
| 5 | `t_bas_cloudhubapp_l` | 协同云应用-多语言表 | 5 | [bos_cloudhubapp.md](./bos_cloudhubapp.md) |
| 6 | `t_bas_daily_loginnumber` | 每日在线用户数-主表 | 12 | [bos_smc_onlineuser_numday.md](./bos_smc_onlineuser_numday.md) |
| 7 | `t_bas_daily_logintime` | 在线用户时长-主表 | 23 | [bos_smc_onlinetime.md](./bos_smc_onlinetime.md) |
| 8 | `t_bas_daily_onlinemax` | 在线用户峰值-主表 | 14 | [bos_smc_onlineuser_max.md](./bos_smc_onlineuser_max.md) |
| 9 | `t_bas_daily_onlinenumber` | 今日在线用户数-主表 | 16 | [bos_smc_onlineuser_number.md](./bos_smc_onlineuser_number.md) |
| 10 | `t_bas_extenderp` | 业务系统-主表 | 17 | [bas_extenderp.md](./bas_extenderp.md) |
| 11 | `t_bas_extenderp_l` | 业务系统-多语言表 | 6 | [bas_extenderp.md](./bas_extenderp.md) |
| 12 | `t_bas_imageconfig` | 影像系统配置-主表 | 23 | [bas_imageconfig.md](./bas_imageconfig.md) |
| 13 | `t_bas_imageconfig_l` | 影像系统配置-多语言表 | 5 | [bas_imageconfig.md](./bas_imageconfig.md) |
| 14 | `t_bas_imageerrorinfo` | 影像错误记录-主表 | 12 | [bas_imageerrorinfo.md](./bas_imageerrorinfo.md) |
| 15 | `t_bas_imageexpire_channel` | 消息渠道-多选基础资料表 | 3 | [bas_imageremind.md](./bas_imageremind.md) |
| 16 | `t_bas_imageremind` | 影像超时提醒规则-主表 | 18 | [bas_imageremind.md](./bas_imageremind.md) |
| 17 | `t_bas_imageremind_l` | 影像超时提醒规则-多语言表 | 6 | [bas_imageremind.md](./bas_imageremind.md) |
| 18 | `t_bas_imageremindbill` | 单据-多选基础资料表 | 3 | [bas_imageremind.md](./bas_imageremind.md) |
| 19 | `t_bas_imageremindorg` | 组织-多选基础资料表 | 3 | [bas_imageremind.md](./bas_imageremind.md) |
| 20 | `t_bas_imageremindrecord` | 影像超期提醒记录-主表 | 6 | [bas_imageremindrecord.md](./bas_imageremindrecord.md) |
| 21 | `t_bas_imagestrategy` | 影像编码生成策略-主表 | 14 | [bos_imagestrategy.md](./bos_imagestrategy.md) |
| 22 | `t_bas_imagestrategy_l` | 影像编码生成策略-多语言表 | 4 | [bos_imagestrategy.md](./bos_imagestrategy.md) |
| 23 | `t_bas_imastrategybill` | 单据-多选基础资料表 | 3 | [bos_imagestrategy.md](./bos_imagestrategy.md) |
| 24 | `t_bas_imastrategyorg` | 组织-多选基础资料表 | 3 | [bos_imagestrategy.md](./bos_imagestrategy.md) |
| 25 | `t_bas_invoice` | OCR发票识别-主表 | 17 | [bos_invoice.md](./bos_invoice.md) |
| 26 | `t_bas_invoiceentrykey` | 单据体-子表 | 6 | [bos_invoice.md](./bos_invoice.md) |
| 27 | `t_bas_invoicekey` | 单据体-子表 | 5 | [bos_invoice.md](./bos_invoice.md) |
| 28 | `t_bas_proverbs` | 箴言-主表 | 12 | [bos_proverbs.md](./bos_proverbs.md) |
| 29 | `t_bas_proverbs_l` | 箴言-多语言表 | 5 | [bos_proverbs.md](./bos_proverbs.md) |
| 30 | `t_bas_proverbsgroup` | 箴言分组-主表 | 15 | [bos_proverbsgroup.md](./bos_proverbsgroup.md) |
| 31 | `t_bas_proverbsgroup_l` | 箴言分组-多语言表 | 6 | [bos_proverbsgroup.md](./bos_proverbsgroup.md) |
| 32 | `t_bas_rescanremind` | 影像退扫提醒规则-主表 | 13 | [bas_rescanremind.md](./bas_rescanremind.md) |
| 33 | `t_bas_rescanremind_bill` | 单据-多选基础资料表 | 3 | [bas_rescanremind.md](./bas_rescanremind.md) |
| 34 | `t_bas_rescanremind_l` | 影像退扫提醒规则-多语言表 | 6 | [bas_rescanremind.md](./bas_rescanremind.md) |
| 35 | `t_bas_rescanremind_msg` | 消息渠道-多选基础资料表 | 3 | [bas_rescanremind.md](./bas_rescanremind.md) |
| 36 | `t_bas_rescanremind_org` | 组织-多选基础资料表 | 3 | [bas_rescanremind.md](./bas_rescanremind.md) |
| 37 | `t_bas_session_history` | 在线用户明细-主表 | 27 | [bos_smc_onlinesession_his.md](./bos_smc_onlinesession_his.md) |
| 38 | `t_bas_sessions` | 在线用户基础资料-主表 | 23 | [bos_smc_onlineuser_base.md](./bos_smc_onlineuser_base.md) |
| 39 | `t_bas_share_url` | 分享-主表 | 9 | [bos_svc_share.md](./bos_svc_share.md) |
| 40 | `t_bas_sscunit` | 扫描点-主表 | 14 | [bos_sscunitlist.md](./bos_sscunitlist.md) |
| 41 | `t_bas_sscunit_l` | 扫描点-多语言表 | 5 | [bos_sscunitlist.md](./bos_sscunitlist.md) |
| 42 | `t_bas_sscunitentry` | 单据体-子表 | 4 | [bos_sscunitlist.md](./bos_sscunitlist.md) |
| 43 | `t_bd_ignorerefcheck` | 基础数据删除引用检查白名单-主表 | 6 | [bd_ignorerefcheck.md](./bd_ignorerefcheck.md) |
| 44 | `t_bd_secondauthscheme` | 操作方案-主表 | 7 | [operate_scheme.md](./operate_scheme.md) |
| 45 | `t_bd_signconfirmorg` | 二次认证受控组织-主表 | 4 | [bos_confirm_orgentity.md](./bos_confirm_orgentity.md) |
| 46 | `t_bd_signmessagelog` | 签名日志-主表 | 7 | [bd_signmessagelog.md](./bd_signmessagelog.md) |
| 47 | `t_bd_userandcertrelation` | 证书用户关系-主表 | 3 | [bd_userandcertrelation.md](./bd_userandcertrelation.md) |
| 48 | `t_bd_usercredentials` | 证书管理-主表 | 15 | [bd_usercredentials.md](./bd_usercredentials.md) |
| 49 | `t_bd_usercredentials_l` | 证书管理-多语言表 | 4 | [bd_usercredentials.md](./bd_usercredentials.md) |
| 50 | `t_bos_imageparamsconfig` | 影像参数配置-主表 | 4 | [bos_imageparamsconfig.md](./bos_imageparamsconfig.md) |
| 51 | `t_caconfig_license` | 签名许可配置-主表 | 10 | [bd_caconfig_license.md](./bd_caconfig_license.md) |
| 52 | `t_meta_ext_jar` | 热部署-主表 | 10 | [bos_depolyjar.md](./bos_depolyjar.md) |
| 53 | `t_mutex_datalock` | 网络互斥-主表 | 12 | [bos_datalock.md](./bos_datalock.md) |
| 54 | `t_rw_split_check_event` | 从库检测事件-主表 | 6 | [rw_split_check_event.md](./rw_split_check_event.md) |
| 55 | `t_rw_split_config` | 读写分离配置-主表 | 17 | [rw_split_config.md](./rw_split_config.md) |
| 56 | `t_rw_split_config_l` | 读写分离配置-多语言表 | 4 | [rw_split_config.md](./rw_split_config.md) |
| 57 | `t_rw_split_scenes` | 读写分离场景配置-主表 | 12 | [rw_split_scenes.md](./rw_split_scenes.md) |
| 58 | `t_rw_split_scenes_l` | 读写分离场景配置-多语言表 | 4 | [rw_split_scenes.md](./rw_split_scenes.md) |
| 59 | `t_sch_deployinfo` | 调度部署记录-主表 | 7 | [sch_deployinfo.md](./sch_deployinfo.md) |
| 60 | `t_sch_errorjob` | 异常日志-主表 | 5 | [sch_errorjob.md](./sch_errorjob.md) |
| 61 | `t_sch_errorjob` | 异常日志详情-主表 | 5 | [sch_errorjob_details.md](./sch_errorjob_details.md) |
| 62 | `t_sch_graysetting` | 调度灰度配置-主表 | 12 | [sch_graysetting.md](./sch_graysetting.md) |
| 63 | `t_sch_job` | 调度作业-主表 | 21 | [sch_job.md](./sch_job.md) |
| 64 | `t_sch_job_l` | 调度作业-多语言表 | 5 | [sch_job.md](./sch_job.md) |
| 65 | `t_sch_job_m` | 消息通知单据体-子表 | 6 | [sch_job.md](./sch_job.md) |
| 66 | `t_sch_job_n` | 调度作业-分表 | 10 | [sch_job.md](./sch_job.md) |
| 67 | `t_sch_jobform` | 后台大任务-主表 | 7 | [sch_jobform.md](./sch_jobform.md) |
| 68 | `t_sch_jobmsgreceiver` | 消息接收人-多选基础资料表 | 3 | [sch_job.md](./sch_job.md) |
| 69 | `t_sch_retryjob` | 调度失败重试记录表-主表 | 10 | [sch_retryjob.md](./sch_retryjob.md) |
| 70 | `t_sch_schedule` | 调度计划-主表 | 70 | [sch_schedule.md](./sch_schedule.md) |
| 71 | `t_sch_schedule_entry` | 调度作业-子表 | 4 | [sch_schedule.md](./sch_schedule.md) |
| 72 | `t_sch_schedule_l` | 调度计划-多语言表 | 5 | [sch_schedule.md](./sch_schedule.md) |
| 73 | `t_sch_schedule_m` | 调度消息通知表-子表 | 6 | [sch_schedule.md](./sch_schedule.md) |
| 74 | `t_sch_schedule_n` | 调度计划-分表 | 9 | [sch_schedule.md](./sch_schedule.md) |
| 75 | `t_sch_schmsgreceiver` | 消息接收人-多选基础资料表 | 3 | [sch_schedule.md](./sch_schedule.md) |
| 76 | `t_sch_task` | 运行日志-主表 | 22 | [sch_task.md](./sch_task.md) |
| 77 | `t_sch_task` | 运行日志详情-主表 | 22 | [sch_tasklog_details.md](./sch_tasklog_details.md) |
| 78 | `t_sch_taskdefentry` | 参数分录-子表 | 9 | [sch_taskdefine.md](./sch_taskdefine.md) |
| 79 | `t_sch_taskdefentry_l` | 参数分录-多语言表 | 5 | [sch_taskdefine.md](./sch_taskdefine.md) |
| 80 | `t_sch_taskdefine` | 调度执行程序-主表 | 11 | [sch_taskdefine.md](./sch_taskdefine.md) |
| 81 | `t_sch_taskdefine_l` | 调度执行程序-多语言表 | 5 | [sch_taskdefine.md](./sch_taskdefine.md) |
| 82 | `t_sch_tasktrace` | 任务轨迹记录-主表 | 8 | [sch_tasktracerecord.md](./sch_tasktracerecord.md) |
