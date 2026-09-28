# arm 模块表清单

> 本模块共收录 **29** 张表定义，来自 `arm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category arm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_arm_backflush` | 倒冲-子表 | 12 | [arm_backflushdetail.md](./arm_backflushdetail.md) |
| 2 | `t_arm_backflushdetail` | 倒冲明细-子表 | 19 | [arm_backflushdetail.md](./arm_backflushdetail.md) |
| 3 | `t_arm_capacityentry` | 产能调整-子表 | 6 | [arm_linecapacity.md](./arm_linecapacity.md) |
| 4 | `t_arm_interbackflush` | 交互式倒冲-主表 | 11 | [arm_backflushdetail.md](./arm_backflushdetail.md) |
| 5 | `t_arm_linecapacity` | 生产线-主表 | 32 | [arm_linecapacity.md](./arm_linecapacity.md) |
| 6 | `t_arm_linecapacity_l` | 生产线-多语言表 | 4 | [arm_linecapacity.md](./arm_linecapacity.md) |
| 7 | `t_arm_linecapacity_u` | 生产线-使用范围表 | 3 | [arm_linecapacity.md](./arm_linecapacity.md) |
| 8 | `t_arm_linewareinventory` | 线边仓库存管理平台-主表 | 11 | [arm_linewarehouse_ivnt.md](./arm_linewarehouse_ivnt.md) |
| 9 | `t_arm_mateinvtstatus` | 物料库存状态-子表 | 31 | [arm_linewarehouse_ivnt.md](./arm_linewarehouse_ivnt.md) |
| 10 | `t_arm_materialentry` | 物料明细-子表 | 18 | [arm_linecapacity.md](./arm_linecapacity.md) |
| 11 | `t_arm_prdscheduleentry` | 单据体-子表 | 20 | [arm_productschedule.md](./arm_productschedule.md) |
| 12 | `t_arm_prdshedule` | 重复生产日程-主表 | 15 | [arm_productschedule.md](./arm_productschedule.md) |
| 13 | `t_arm_prodorderentry` | 用料清单-子表 | 46 | [arm_productionorder.md](./arm_productionorder.md) |
| 14 | `t_arm_productionorder` | 重复生产工单-主表 | 52 | [arm_productionorder.md](./arm_productionorder.md) |
| 15 | `t_arm_reorderpt` | 线边仓再订货点设置-主表 | 14 | [arm_cfg_reorderpoint.md](./arm_cfg_reorderpoint.md) |
| 16 | `t_arm_reorderptcmpentry` | 物料明细-子表 | 18 | [arm_cfg_reorderpoint.md](./arm_cfg_reorderpoint.md) |
| 17 | `t_arm_reorderptprdentry` | 生产线使用记录-子表 | 11 | [arm_cfg_reorderpoint.md](./arm_cfg_reorderpoint.md) |
| 18 | `t_arm_reorderptrelation` | BOM关联关系-子表 | 7 | [arm_cfg_reorderpoint.md](./arm_cfg_reorderpoint.md) |
| 19 | `t_arm_reorderptsubentry` | 子单据体-子表 | 9 | [arm_cfg_reorderpoint.md](./arm_cfg_reorderpoint.md) |
| 20 | `t_arm_report_workbanch` | 重复生产汇报平台-主表 | 43 | [arm_report_workbanch.md](./arm_report_workbanch.md) |
| 21 | `t_arm_schedulewriteoff` | 日程冲销-子表 | 13 | [arm_backflushdetail.md](./arm_backflushdetail.md) |
| 22 | `t_arm_scrapreportentry` | 单据体-子表 | 7 | [arm_report_workbanch.md](./arm_report_workbanch.md) |
| 23 | `t_arm_screason` | 报废原因-主表 | 4 | [arm_screason.md](./arm_screason.md) |
| 24 | `t_arm_screason_l` | 报废原因-多语言表 | 4 | [arm_screason.md](./arm_screason.md) |
| 25 | `t_arm_workhoursreport` | 重复生产工时汇报单-主表 | 21 | [arm_workhoursreport.md](./arm_workhoursreport.md) |
| 26 | `t_arm_workhoursreport_lk` | 关联子实体-子表 | 6 | [arm_workhoursreport.md](./arm_workhoursreport.md) |
| 27 | `t_arm_workhoursreport_tc` | 重复生产工时汇报单-关联追踪表 | 7 | [arm_workhoursreport.md](./arm_workhoursreport.md) |
| 28 | `t_arm_workhoursreport_wb` | 重复生产工时汇报单-反写记录表 | 10 | [arm_workhoursreport.md](./arm_workhoursreport.md) |
| 29 | `t_arm_workhoursrptentry` | 单据体-子表 | 14 | [arm_workhoursreport.md](./arm_workhoursreport.md) |
