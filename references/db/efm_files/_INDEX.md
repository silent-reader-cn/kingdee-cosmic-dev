# efm 模块表清单

> 本模块共收录 **26** 张表定义，来自 `efm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category efm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `tk_eafc_appraise_info` | 鉴定申请单-主表 | 19 | [eafc_appraise_info.md](./eafc_appraise_info.md) |
| 2 | `tk_eafc_appraise_item` | 单据体-子表 | 27 | [eafc_appraise_info.md](./eafc_appraise_info.md) |
| 3 | `tk_eafc_appraise_plan` | 保管期限鉴定-主表 | 5 | [eafc_appraise_plan.md](./eafc_appraise_plan.md) |
| 4 | `tk_eafc_authcontroltest01` | 二次授权验证01-主表 | 0 | [eafc_authcontrol_test01.md](./eafc_authcontrol_test01.md) |
| 5 | `tk_eafc_deliver_apply` | 移交申请单-主表 | 34 | [eafc_deliver_apply.md](./eafc_deliver_apply.md) |
| 6 | `tk_eafc_deliver_category` | 移交种类-主表 | 7 | [eafc_deliver_category.md](./eafc_deliver_category.md) |
| 7 | `tk_eafc_deliver_config` | 移交配置-主表 | 9 | [eafc_deliver_config.md](./eafc_deliver_config.md) |
| 8 | `tk_eafc_deliver_item` | 移交目录-子表 | 8 | [eafc_deliver_apply.md](./eafc_deliver_apply.md) |
| 9 | `tk_eafc_deliver_mul_book` | 机构问题-多选基础资料表 | 3 | [eafc_deliver_apply.md](./eafc_deliver_apply.md) |
| 10 | `tk_eafc_deliver_schedule` | 移交调度计划-主表 | 0 | [eafc_deliver_schedule.md](./eafc_deliver_schedule.md) |
| 11 | `tk_eafc_deliver_schedule_l` | 移交调度计划-多语言表 | 0 | [eafc_deliver_schedule.md](./eafc_deliver_schedule.md) |
| 12 | `tk_eafc_deliver_task` | 移交任务监控-主表 | 21 | [eafc_deliver_task.md](./eafc_deliver_task.md) |
| 13 | `tk_eafc_deliver_task_file` | 单据体-子表 | 11 | [eafc_deliver_task.md](./eafc_deliver_task.md) |
| 14 | `tk_eafc_deliver_task_item` | 单据体-子表 | 13 | [eafc_deliver_task.md](./eafc_deliver_task.md) |
| 15 | `tk_eafc_destruction_info` | 档案销毁-主表 | 24 | [eafc_destruction_info.md](./eafc_destruction_info.md) |
| 16 | `tk_eafc_destruction_item` | 单据体-子表 | 23 | [eafc_destruction_info.md](./eafc_destruction_info.md) |
| 17 | `tk_eafc_download_mag` | 下载管理-主表 | 21 | [eafc_download_mag.md](./eafc_download_mag.md) |
| 18 | `tk_eafc_receiver` | 接收方配置-主表 | 36 | [eafc_receiver.md](./eafc_receiver.md) |
| 19 | `tk_fpy_backup` | 备份申请单-主表 | 16 | [fpy_offline_backup.md](./fpy_offline_backup.md) |
| 20 | `tk_fpy_backup_category` | 备份种类-主表 | 6 | [fpy_backup_category.md](./fpy_backup_category.md) |
| 21 | `tk_fpy_backup_item` | 备份目录-子表 | 6 | [fpy_offline_backup.md](./fpy_offline_backup.md) |
| 22 | `tk_fpy_backup_mul_book` | 机构问题-多选基础资料表 | 3 | [fpy_offline_backup.md](./fpy_offline_backup.md) |
| 23 | `tk_fpy_backup_task` | 备份任务单-主表 | 20 | [fpy_backup_task.md](./fpy_backup_task.md) |
| 24 | `tk_fpy_backup_task_item` | 单据体-子表 | 15 | [fpy_backup_task.md](./fpy_backup_task.md) |
| 25 | `tk_fpy_behavior_log` | 行为日志-主表 | 30 | [fpy_behavior_log.md](./fpy_behavior_log.md) |
| 26 | `tk_fpy_org_user` | 机构人员-主表 | 15 | [fpy_org_user.md](./fpy_org_user.md) |
