# arm 模块表清单

> 本模块共收录 **59** 张表定义，来自 `arm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category arm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_arm_backflush` | 倒冲-子表 | 15 | [arm_backflushdetail.md](./arm_backflushdetail.md) |
| 2 | `t_arm_backflush_history` | 倒冲历史-主表 | 13 | [arm_backflush_history.md](./arm_backflush_history.md) |
| 3 | `t_arm_backflushdetail` | 倒冲明细-子表 | 25 | [arm_backflushdetail.md](./arm_backflushdetail.md) |
| 4 | `t_arm_barcodeentry` | 汇报条码单据体-子表 | 13 | [arm_report_workbanch.md](./arm_report_workbanch.md) |
| 5 | `t_arm_batch_qtyreport` | 汇报明细-子表 | 32 | [arm_batch_report.md](./arm_batch_report.md) |
| 6 | `t_arm_batch_report` | 重复生产批量汇报-主表 | 19 | [arm_batch_report.md](./arm_batch_report.md) |
| 7 | `t_arm_batch_whreport` | 工时汇报明细-子表 | 14 | [arm_batch_report.md](./arm_batch_report.md) |
| 8 | `t_arm_batchworkoursreport` | 工时明细-子表 | 15 | [arm_report_workbanch.md](./arm_report_workbanch.md) |
| 9 | `t_arm_capacityentry` | 产能调整-子表 | 7 | [arm_linecapacity.md](./arm_linecapacity.md) |
| 10 | `t_arm_capacityplandetail` | 单据体-子表 | 9 | [arm_displayscheme.md](./arm_displayscheme.md) |
| 11 | `t_arm_chartdisplay` | 记录多选下拉项-主表 | 12 | [arm_chartdisplay_record.md](./arm_chartdisplay_record.md) |
| 12 | `t_arm_displayscheme` | 显示方案-主表 | 3 | [arm_displayscheme.md](./arm_displayscheme.md) |
| 13 | `t_arm_downtimerep` | 停机时长汇报-主表 | 16 | [arm_downtimerep.md](./arm_downtimerep.md) |
| 14 | `t_arm_downtimerepentity` | 单据体-子表 | 10 | [arm_downtimerep.md](./arm_downtimerep.md) |
| 15 | `t_arm_interbackflush` | 汇报倒冲明细-主表 | 17 | [arm_backflushdetail.md](./arm_backflushdetail.md) |
| 16 | `t_arm_linecapacity` | 生产线-主表 | 39 | [arm_linecapacity.md](./arm_linecapacity.md) |
| 17 | `t_arm_linecapacity_l` | 生产线-多语言表 | 4 | [arm_linecapacity.md](./arm_linecapacity.md) |
| 18 | `t_arm_linecapacity_u` | 生产线-使用范围表 | 3 | [arm_linecapacity.md](./arm_linecapacity.md) |
| 19 | `t_arm_linewareinventory` | 线边仓库存管理平台-主表 | 11 | [arm_linewarehouse_ivnt.md](./arm_linewarehouse_ivnt.md) |
| 20 | `t_arm_log` | 生产线排程日志-主表 | 10 | [arm_log.md](./arm_log.md) |
| 21 | `t_arm_logentry` | 单据体-子表 | 7 | [arm_log.md](./arm_log.md) |
| 22 | `t_arm_mateinvtstatus` | 物料库存状态-子表 | 35 | [arm_linewarehouse_ivnt.md](./arm_linewarehouse_ivnt.md) |
| 23 | `t_arm_materialentry` | 物料明细-子表 | 31 | [arm_linecapacity.md](./arm_linecapacity.md) |
| 24 | `t_arm_pickoutentry` | 领料记录-子表 | 4 | [arm_report_workbanch.md](./arm_report_workbanch.md) |
| 25 | `t_arm_prdinvordernoentry` | 入库记录-子表 | 4 | [arm_report_workbanch.md](./arm_report_workbanch.md) |
| 26 | `t_arm_prdplanorder` | 导入重复生产工单-主表 | 32 | [arm_imptplanorder.md](./arm_imptplanorder.md) |
| 27 | `t_arm_prdplanorder_lk` | 关联子实体-子表 | 6 | [arm_imptplanorder.md](./arm_imptplanorder.md) |
| 28 | `t_arm_prdplanorder_tc` | 导入重复生产工单-关联追踪表 | 7 | [arm_imptplanorder.md](./arm_imptplanorder.md) |
| 29 | `t_arm_prdplanorder_wb` | 导入重复生产工单-反写记录表 | 10 | [arm_imptplanorder.md](./arm_imptplanorder.md) |
| 30 | `t_arm_prdplanorderentry` | 单据体-子表 | 3 | [arm_imptplanorder.md](./arm_imptplanorder.md) |
| 31 | `t_arm_prdscheduleentry` | 单据体-子表 | 21 | [arm_productschedule.md](./arm_productschedule.md) |
| 32 | `t_arm_prdshedule` | 重复生产日程-主表 | 15 | [arm_productschedule.md](./arm_productschedule.md) |
| 33 | `t_arm_prodorderentry` | 用料清单-子表 | 48 | [arm_productionorder.md](./arm_productionorder.md) |
| 34 | `t_arm_productionorder` | 重复生产工单-主表 | 59 | [arm_productionorder.md](./arm_productionorder.md) |
| 35 | `t_arm_productionorder_lk` | 关联子实体-子表 | 6 | [arm_productionorder.md](./arm_productionorder.md) |
| 36 | `t_arm_productionorder_tc` | 重复生产工单-关联追踪表 | 7 | [arm_productionorder.md](./arm_productionorder.md) |
| 37 | `t_arm_productionorder_wb` | 重复生产工单-反写记录表 | 10 | [arm_productionorder.md](./arm_productionorder.md) |
| 38 | `t_arm_reorderpt` | 线边仓补料设置-主表 | 15 | [arm_cfg_reorderpoint.md](./arm_cfg_reorderpoint.md) |
| 39 | `t_arm_reorderptcmpentry` | 物料明细-子表 | 22 | [arm_cfg_reorderpoint.md](./arm_cfg_reorderpoint.md) |
| 40 | `t_arm_reorderptprdentry` | 生产线使用记录-子表 | 11 | [arm_cfg_reorderpoint.md](./arm_cfg_reorderpoint.md) |
| 41 | `t_arm_reorderptrelation` | BOM关联关系-子表 | 7 | [arm_cfg_reorderpoint.md](./arm_cfg_reorderpoint.md) |
| 42 | `t_arm_reorderptsubentry` | 子单据体-子表 | 9 | [arm_cfg_reorderpoint.md](./arm_cfg_reorderpoint.md) |
| 43 | `t_arm_report_workbanch` | 重复生产汇报平台-主表 | 66 | [arm_report_workbanch.md](./arm_report_workbanch.md) |
| 44 | `t_arm_report_workbanch_lk` | 关联子实体-子表 | 6 | [arm_report_workbanch.md](./arm_report_workbanch.md) |
| 45 | `t_arm_report_workbanch_tc` | 重复生产汇报平台-关联追踪表 | 7 | [arm_report_workbanch.md](./arm_report_workbanch.md) |
| 46 | `t_arm_report_workbanch_wb` | 重复生产汇报平台-反写记录表 | 10 | [arm_report_workbanch.md](./arm_report_workbanch.md) |
| 47 | `t_arm_schedulewriteoff` | 日程冲销-子表 | 17 | [arm_backflushdetail.md](./arm_backflushdetail.md) |
| 48 | `t_arm_scrapreportentry` | 报废明细-子表 | 7 | [arm_report_workbanch.md](./arm_report_workbanch.md) |
| 49 | `t_arm_screason` | 原因代码-主表 | 7 | [arm_screason.md](./arm_screason.md) |
| 50 | `t_arm_screason_l` | 原因代码-多语言表 | 4 | [arm_screason.md](./arm_screason.md) |
| 51 | `t_arm_shift` | 生产线班次-主表 | 12 | [arm_shift.md](./arm_shift.md) |
| 52 | `t_arm_shift_l` | 生产线班次-多语言表 | 4 | [arm_shift.md](./arm_shift.md) |
| 53 | `t_arm_shiftentry` | 班次-子表 | 9 | [arm_linecapacity.md](./arm_linecapacity.md) |
| 54 | `t_arm_shiftentry_l` | 班次-多语言表 | 4 | [arm_linecapacity.md](./arm_linecapacity.md) |
| 55 | `t_arm_workhoursreport` | 重复生产工时汇报单-主表 | 23 | [arm_workhoursreport.md](./arm_workhoursreport.md) |
| 56 | `t_arm_workhoursreport_lk` | 关联子实体-子表 | 6 | [arm_workhoursreport.md](./arm_workhoursreport.md) |
| 57 | `t_arm_workhoursreport_tc` | 重复生产工时汇报单-关联追踪表 | 7 | [arm_workhoursreport.md](./arm_workhoursreport.md) |
| 58 | `t_arm_workhoursreport_wb` | 重复生产工时汇报单-反写记录表 | 10 | [arm_workhoursreport.md](./arm_workhoursreport.md) |
| 59 | `t_arm_workhoursrptentry` | 单据体-子表 | 24 | [arm_workhoursreport.md](./arm_workhoursreport.md) |
