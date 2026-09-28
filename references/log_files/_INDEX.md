# log 模块表清单

> 本模块共收录 **89** 张表定义，来自 `log_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope log
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bd_secondauth_log` | 二次认证日志-主表 | 8 | [bos_authoperate_log.md](./bos_authoperate_log.md) |
| 2 | `t_bdlog_archivedataentry` | 操作数据分录-子表 | 13 | [bdctrl_archivelog.md](./bdctrl_archivelog.md) |
| 3 | `t_bdlog_archivefaildetail` | 失败原因明细-子表 | 8 | [bdctrl_archivelog.md](./bdctrl_archivelog.md) |
| 4 | `t_bdlog_archivelog` | 管控归档日志-主表 | 21 | [bdctrl_archivelog.md](./bdctrl_archivelog.md) |
| 5 | `t_bdlog_archiveorgentry` | 操作组织分录-子表 | 7 | [bdctrl_archivelog.md](./bdctrl_archivelog.md) |
| 6 | `t_bdlog_dataentry` | 操作数据分录-子表 | 14 | [bd_log.md](./bd_log.md) |
| 7 | `t_bdlog_failcausedetail` | 失败原因明细-子表 | 9 | [bd_log.md](./bd_log.md) |
| 8 | `t_bdlog_log` | 管控日志-主表 | 21 | [bd_log.md](./bd_log.md) |
| 9 | `t_bdlog_optype` | 操作类型-主表 | 8 | [bdlog_optype.md](./bdlog_optype.md) |
| 10 | `t_bdlog_optype_l` | 操作类型-多语言表 | 4 | [bdlog_optype.md](./bdlog_optype.md) |
| 11 | `t_bdlog_orgentry` | 操作组织分录-子表 | 8 | [bd_log.md](./bd_log.md) |
| 12 | `t_log_aduit_rule` | 审计日志_规则设置-主表 | 13 | [al_rule_setting.md](./al_rule_setting.md) |
| 13 | `t_log_aduit_rule_l` | 审计日志_规则设置-多语言表 | 5 | [al_rule_setting.md](./al_rule_setting.md) |
| 14 | `t_log_app` | 审计日志（旧）-主表 | 24 | [bos_aduit_log_view.md](./bos_aduit_log_view.md) |
| 15 | `t_log_app` | 历史记录-主表 | 24 | [bos_history_log_view.md](./bos_history_log_view.md) |
| 16 | `t_log_app` | 操作日志-主表 | 24 | [bos_log_operation.md](./bos_log_operation.md) |
| 17 | `t_log_app` | 操作日志v2-主表 | 24 | [bos_log_operation_inh.md](./bos_log_operation_inh.md) |
| 18 | `t_log_app_l` | 审计日志（旧）-多语言表 | 6 | [bos_aduit_log_view.md](./bos_aduit_log_view.md) |
| 19 | `t_log_app_l` | 历史记录-多语言表 | 6 | [bos_history_log_view.md](./bos_history_log_view.md) |
| 20 | `t_log_app_l` | 操作日志-多语言表 | 6 | [bos_log_operation.md](./bos_log_operation.md) |
| 21 | `t_log_app_l` | 操作日志v2-多语言表 | 6 | [bos_log_operation_inh.md](./bos_log_operation_inh.md) |
| 22 | `t_log_app_other` | 其他类型操作日志-主表 | 21 | [bos_log_operation_other.md](./bos_log_operation_other.md) |
| 23 | `t_log_app_other_l` | 其他类型操作日志-多语言表 | 0 | [bos_log_operation_other.md](./bos_log_operation_other.md) |
| 24 | `t_log_app_v2` | 上机操作日志-主表 | 21 | [bos_log_operation_web.md](./bos_log_operation_web.md) |
| 25 | `t_log_app_v2_l` | 上机操作日志-多语言表 | 6 | [bos_log_operation_web.md](./bos_log_operation_web.md) |
| 26 | `t_log_appsetting` | 日志设置-主表 | 14 | [bos_log_appsetting.md](./bos_log_appsetting.md) |
| 27 | `t_log_archive` | 归档操作日志-主表 | 24 | [bos_log_archive.md](./bos_log_archive.md) |
| 28 | `t_log_archive` | 归档操作日志-主表 | 24 | [bos_log_archive_new.md](./bos_log_archive_new.md) |
| 29 | `t_log_archive_l` | 归档操作日志-多语言表 | 6 | [bos_log_archive.md](./bos_log_archive.md) |
| 30 | `t_log_asyncop` | 异步服务日志-主表 | 15 | [bos_log_asyncop.md](./bos_log_asyncop.md) |
| 31 | `t_log_asyncop_l` | 异步服务日志-多语言表 | 5 | [bos_log_asyncop.md](./bos_log_asyncop.md) |
| 32 | `t_log_etconfig` | 监控配置-主表 | 6 | [bos_entitytraceconfig.md](./bos_entitytraceconfig.md) |
| 33 | `t_log_etconfigentry` | 监听方案-子表 | 6 | [bos_entitytraceconfig.md](./bos_entitytraceconfig.md) |
| 34 | `t_log_etl_setting` | 日志迁移设置-主表 | 5 | [bos_log_etl_setting.md](./bos_log_etl_setting.md) |
| 35 | `t_log_etl_task` | 日志迁移任务-主表 | 7 | [bos_log_etl_task.md](./bos_log_etl_task.md) |
| 36 | `t_log_exportlog` | 引出结果-主表 | 20 | [bos_exportlog.md](./bos_exportlog.md) |
| 37 | `t_log_failrecord` | 失败消息记录-主表 | 5 | [bos_log_fail_record.md](./bos_log_fail_record.md) |
| 38 | `t_log_index` | 日志索引-主表 | 7 | [bos_log_index.md](./bos_log_index.md) |
| 39 | `t_log_metaoperate` | 元数据操作日志-主表 | 8 | [meta_log.md](./meta_log.md) |
| 40 | `t_log_metaversion` | 单据体-子表 | 9 | [meta_log.md](./meta_log.md) |
| 41 | `t_log_settings` | 日志设置-主表 | 7 | [bos_log_settings.md](./bos_log_settings.md) |
| 42 | `t_logorm_monitor_index` | ES存储索引-主表 | 0 | [logorm_monitor_index.md](./logorm_monitor_index.md) |
| 43 | `t_perm_log` | 权限日志-主表 | 38 | [perm_log.md](./perm_log.md) |
| 44 | `t_perm_log_archive` | 权限日志归档-主表 | 36 | [perm_log_archive.md](./perm_log_archive.md) |
| 45 | `t_perm_log_copytaruser` | 复制权限差异-主表 | 8 | [perm_log_diff_copytaruser.md](./perm_log_diff_copytaruser.md) |
| 46 | `t_perm_log_diff_admorg` | 行政组织管辖范围差异-主表 | 9 | [perm_log_diff_admorg.md](./perm_log_diff_admorg.md) |
| 47 | `t_perm_log_diff_admorgusr` | 行政组织管辖范围额外用户差异-主表 | 12 | [perm_log_diff_admorguser.md](./perm_log_diff_admorguser.md) |
| 48 | `t_perm_log_diff_app` | 应用授权范围-主表 | 10 | [perm_log_diff_app.md](./perm_log_diff_app.md) |
| 49 | `t_perm_log_diff_bcperm` | 补充权限差异-主表 | 14 | [perm_log_diff_bcperm.md](./perm_log_diff_bcperm.md) |
| 50 | `t_perm_log_diff_bd_base` | 基础资料控制业务基本信息差异-主表 | 20 | [xkbd_auth_diff_base_info.md](./xkbd_auth_diff_base_info.md) |
| 51 | `t_perm_log_diff_bd_exrole` | 例外角色-多选基础资料表 | 3 | [xkbd_auth_diff_role_user.md](./xkbd_auth_diff_role_user.md) |
| 52 | `t_perm_log_diff_bd_exuser` | 例外用户-多选基础资料表 | 3 | [xkbd_auth_diff_role_user.md](./xkbd_auth_diff_role_user.md) |
| 53 | `t_perm_log_diff_bd_field` | 受控字段-多选基础资料表 | 3 | [xkbd_auth_diff_role_user.md](./xkbd_auth_diff_role_user.md) |
| 54 | `t_perm_log_diff_bd_perm` | 受控权限项-多选基础资料表 | 3 | [xkbd_auth_diff_role_user.md](./xkbd_auth_diff_role_user.md) |
| 55 | `t_perm_log_diff_bd_role` | 应用角色-多选基础资料表 | 3 | [xkbd_auth_diff_role_user.md](./xkbd_auth_diff_role_user.md) |
| 56 | `t_perm_log_diff_bd_ru` | 基础资料控制业务角色用户差异-主表 | 10 | [xkbd_auth_diff_role_user.md](./xkbd_auth_diff_role_user.md) |
| 57 | `t_perm_log_diff_bd_user` | 应用用户-多选基础资料表 | 3 | [xkbd_auth_diff_role_user.md](./xkbd_auth_diff_role_user.md) |
| 58 | `t_perm_log_diff_busirole` | 业务角色差异-主表 | 10 | [perm_log_diff_bizrole.md](./perm_log_diff_bizrole.md) |
| 59 | `t_perm_log_diff_busiunit` | 业务单元管辖范围差异-主表 | 9 | [perm_log_diff_busiunit.md](./perm_log_diff_busiunit.md) |
| 60 | `t_perm_log_diff_commrole` | 通用角色差异-主表 | 10 | [perm_log_diff_commrole.md](./perm_log_diff_commrole.md) |
| 61 | `t_perm_log_diff_dimdis` | 隔离维度禁用权限差异-主表 | 21 | [perm_log_diff_dimdis.md](./perm_log_diff_dimdis.md) |
| 62 | `t_perm_log_diff_dimfield` | 隔离维度字段权限差异-主表 | 23 | [perm_log_diff_dimfield.md](./perm_log_diff_dimfield.md) |
| 63 | `t_perm_log_diff_dimfps` | 隔离维度字段权限方案差异-主表 | 22 | [perm_log_diff_dimfps.md](./perm_log_diff_dimfps.md) |
| 64 | `t_perm_log_diff_dimfunc` | 隔离维度功能权限差异-主表 | 21 | [perm_log_diff_dimfun.md](./perm_log_diff_dimfun.md) |
| 65 | `t_perm_log_diff_dimnewdr` | 隔离维度数据规则差异表-主表 | 25 | [perm_log_diff_dimnewdr.md](./perm_log_diff_dimnewdr.md) |
| 66 | `t_perm_log_diff_dimnewdrp` | 隔离维度基础资料数据范围差异表-主表 | 27 | [perm_log_diff_dimnewdrp.md](./perm_log_diff_dimnewdrp.md) |
| 67 | `t_perm_log_diff_dimrange` | 隔离维度范围差异-主表 | 13 | [perm_log_diff_dimrange.md](./perm_log_diff_dimrange.md) |
| 68 | `t_perm_log_diff_dimrole` | 隔离维度通用角色差异-主表 | 17 | [perm_log_diff_dimcomrole.md](./perm_log_diff_dimcomrole.md) |
| 69 | `t_perm_log_diff_dimuser` | 隔离维度用户差异-主表 | 21 | [perm_log_roleorguser.md](./perm_log_roleorguser.md) |
| 70 | `t_perm_log_diff_disperm` | 权限禁用差异-主表 | 14 | [perm_log_diff_disperm.md](./perm_log_diff_disperm.md) |
| 71 | `t_perm_log_diff_fieldperm` | 字段权限差异-主表 | 16 | [perm_log_diff_fieldperm.md](./perm_log_diff_fieldperm.md) |
| 72 | `t_perm_log_diff_fps` | 字段权限方案差异-主表 | 15 | [perm_log_diff_fps.md](./perm_log_diff_fps.md) |
| 73 | `t_perm_log_diff_fpsd` | 字段权限方案明细差异-主表 | 16 | [perm_log_diff_fpsd.md](./perm_log_diff_fpsd.md) |
| 74 | `t_perm_log_diff_funcperm` | 功能权限差异-主表 | 14 | [perm_log_diff_funcperm.md](./perm_log_diff_funcperm.md) |
| 75 | `t_perm_log_diff_newdr` | 数据规则差异-主表 | 18 | [perm_log_diff_newdr.md](./perm_log_diff_newdr.md) |
| 76 | `t_perm_log_diff_newdrprop` | 基础资料数据范围差异-主表 | 20 | [perm_log_diff_newdrprop.md](./perm_log_diff_newdrprop.md) |
| 77 | `t_perm_log_diff_oprdirect` | 特殊数据权限指定主管差异-主表 | 15 | [perm_log_diff_oprdirector.md](./perm_log_diff_oprdirector.md) |
| 78 | `t_perm_log_diff_oprexrole` | 特殊数据权限例外通用角色差异-主表 | 10 | [perm_log_diff_oprexrole.md](./perm_log_diff_oprexrole.md) |
| 79 | `t_perm_log_diff_oprexusgr` | 特殊数据权限例外用户组差异表-主表 | 10 | [perm_log_diff_oprexusrgrp.md](./perm_log_diff_oprexusrgrp.md) |
| 80 | `t_perm_log_diff_oprexusr` | 特殊数据权限例外用户差异-主表 | 15 | [perm_log_diff_oprexusr.md](./perm_log_diff_oprexusr.md) |
| 81 | `t_perm_log_diff_roleadmgr` | 通用角色-管理员组关系差异-主表 | 14 | [perm_log_diff_roleadmgr.md](./perm_log_diff_roleadmgr.md) |
| 82 | `t_perm_log_diff_ugbizrole` | 用户组业务角色差异-主表 | 16 | [perm_log_ugbusirole.md](./perm_log_ugbusirole.md) |
| 83 | `t_perm_log_diff_ugroledim` | 用户组角色隔离维度差异-主表 | 21 | [perm_log_ugroledim.md](./perm_log_ugroledim.md) |
| 84 | `t_perm_log_diff_user` | 用户差异表-主表 | 14 | [perm_log_diff_user.md](./perm_log_diff_user.md) |
| 85 | `t_perm_log_diff_usrgrpu` | 用户组用户差异-主表 | 17 | [perm_log_usrgrpuser.md](./perm_log_usrgrpuser.md) |
| 86 | `t_perm_log_user` | 影响用户-主表 | 10 | [perm_log_user.md](./perm_log_user.md) |
| 87 | `t_permlog_busitype` | 权限日志业务类型-主表 | 13 | [permlog_busitype.md](./permlog_busitype.md) |
| 88 | `t_permlog_busitype_l` | 权限日志业务类型-多语言表 | 4 | [permlog_busitype.md](./permlog_busitype.md) |
| 89 | `t_sys_opreason` | 操作原因-主表 | 7 | [operatereason.md](./operatereason.md) |
