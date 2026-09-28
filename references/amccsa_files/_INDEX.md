# amccsa 模块表清单

> 本模块共收录 **53** 张表定义，来自 `amccsa_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope amccsa
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_amccsa_asn` | 提前发运通知单-主表 | 15 | [amccsa_asn.md](./amccsa_asn.md) |
| 2 | `t_amccsa_asn_tc` | 提前发运通知单-关联追踪表 | 7 | [amccsa_asn.md](./amccsa_asn.md) |
| 3 | `t_amccsa_asn_wb` | 提前发运通知单-反写记录表 | 10 | [amccsa_asn.md](./amccsa_asn.md) |
| 4 | `t_amccsa_asndata` | ASN数据记录-主表 | 18 | [amccsa_asndata.md](./amccsa_asndata.md) |
| 5 | `t_amccsa_asndatadetail` | 物料明细-子表 | 25 | [amccsa_asndata.md](./amccsa_asndata.md) |
| 6 | `t_amccsa_asndatadetail_l` | 物料明细-多语言表 | 4 | [amccsa_asndata.md](./amccsa_asndata.md) |
| 7 | `t_amccsa_asndetail` | 协议物料信息-子表 | 22 | [amccsa_asn.md](./amccsa_asn.md) |
| 8 | `t_amccsa_asndetail_lk` | 关联子实体-子表 | 6 | [amccsa_asn.md](./amccsa_asn.md) |
| 9 | `t_amccsa_asndetailsub` | 需求明细-子表 | 24 | [amccsa_asn.md](./amccsa_asn.md) |
| 10 | `t_amccsa_asnstocksub` | 出库明细-子表 | 14 | [amccsa_asn.md](./amccsa_asn.md) |
| 11 | `t_amccsa_asnstocksub_l` | 出库明细-多语言表 | 4 | [amccsa_asn.md](./amccsa_asn.md) |
| 12 | `t_amccsa_calendar` | 客户日历-主表 | 26 | [amccsa_calendar.md](./amccsa_calendar.md) |
| 13 | `t_amccsa_calendar_l` | 客户日历-多语言表 | 4 | [amccsa_calendar.md](./amccsa_calendar.md) |
| 14 | `t_amccsa_calendar_u` | 客户日历-使用范围表 | 3 | [amccsa_calendar.md](./amccsa_calendar.md) |
| 15 | `t_amccsa_calendarentry` | 单据体-子表 | 5 | [amccsa_calendar.md](./amccsa_calendar.md) |
| 16 | `t_amccsa_csorderentry` | 订单明细-子表 | 41 | [amccsa_custschdorder.md](./amccsa_custschdorder.md) |
| 17 | `t_amccsa_csorderentry_lk` | 关联子实体-子表 | 6 | [amccsa_custschdorder.md](./amccsa_custschdorder.md) |
| 18 | `t_amccsa_csorderentry_lk` | 关联子实体-子表 | 6 | [amccsa_xcustschdorder.md](./amccsa_xcustschdorder.md) |
| 19 | `t_amccsa_csorderentry_r` | 订单明细-分表 | 24 | [amccsa_custschdorder.md](./amccsa_custschdorder.md) |
| 20 | `t_amccsa_custschdorder` | 销售计划协议-主表 | 32 | [amccsa_custschdorder.md](./amccsa_custschdorder.md) |
| 21 | `t_amccsa_custschdorder` | 销售计划协议F7-主表 | 32 | [amccsa_custschdorder_f7.md](./amccsa_custschdorder_f7.md) |
| 22 | `t_amccsa_custschdorder_c` | 销售计划协议-分表 | 21 | [amccsa_custschdorder.md](./amccsa_custschdorder.md) |
| 23 | `t_amccsa_custschdorder_c` | 销售计划协议F7-分表 | 21 | [amccsa_custschdorder_f7.md](./amccsa_custschdorder_f7.md) |
| 24 | `t_amccsa_custschdorder_tc` | 销售计划协议-关联追踪表 | 7 | [amccsa_custschdorder.md](./amccsa_custschdorder.md) |
| 25 | `t_amccsa_custschdorder_tc` | 销售计划协议变更单-关联追踪表 | 7 | [amccsa_xcustschdorder.md](./amccsa_xcustschdorder.md) |
| 26 | `t_amccsa_custschdorder_wb` | 销售计划协议-反写记录表 | 10 | [amccsa_custschdorder.md](./amccsa_custschdorder.md) |
| 27 | `t_amccsa_custschdorder_wb` | 销售计划协议变更单-反写记录表 | 10 | [amccsa_xcustschdorder.md](./amccsa_xcustschdorder.md) |
| 28 | `t_amccsa_delivernotice_tc` | 滚动发货通知单-关联追踪表 | 7 | [amccsa_deliverynotice.md](./amccsa_deliverynotice.md) |
| 29 | `t_amccsa_delivernotice_wb` | 滚动发货通知单-反写记录表 | 10 | [amccsa_deliverynotice.md](./amccsa_deliverynotice.md) |
| 30 | `t_amccsa_deliverynotentry` | 物料明细-子表 | 38 | [amccsa_deliverynotice.md](./amccsa_deliverynotice.md) |
| 31 | `t_amccsa_deliverynotentry_lk` | 关联子实体-子表 | 6 | [amccsa_deliverynotice.md](./amccsa_deliverynotice.md) |
| 32 | `t_amccsa_deliverynotentry_r` | 物料明细-分表 | 16 | [amccsa_deliverynotice.md](./amccsa_deliverynotice.md) |
| 33 | `t_amccsa_deliverynotice` | 滚动发货通知单-主表 | 44 | [amccsa_deliverynotice.md](./amccsa_deliverynotice.md) |
| 34 | `t_amccsa_forecastqlf` | 需求预测类型-主表 | 13 | [amccsa_forecastqualifier.md](./amccsa_forecastqualifier.md) |
| 35 | `t_amccsa_forecastqlf_l` | 需求预测类型-多语言表 | 5 | [amccsa_forecastqualifier.md](./amccsa_forecastqualifier.md) |
| 36 | `t_amccsa_group_coderule` | 发放号-主表 | 13 | [amccsa_release.md](./amccsa_release.md) |
| 37 | `t_amccsa_group_coderule_l` | 发放号-多语言表 | 4 | [amccsa_release.md](./amccsa_release.md) |
| 38 | `t_amccsa_log` | 应用日志-主表 | 10 | [amccsa_log.md](./amccsa_log.md) |
| 39 | `t_amccsa_logentry` | 单据体-子表 | 7 | [amccsa_log.md](./amccsa_log.md) |
| 40 | `t_amccsa_plansch_detail` | 单据体-子表 | 16 | [amccsa_plan_schedule.md](./amccsa_plan_schedule.md) |
| 41 | `t_amccsa_planschedule` | 滚动预测计划-主表 | 39 | [amccsa_plan_schedule.md](./amccsa_plan_schedule.md) |
| 42 | `t_amccsa_requiresc_detail` | 单据体-子表 | 19 | [amccsa_require_schedule.md](./amccsa_require_schedule.md) |
| 43 | `t_amccsa_requireschedule` | 滚动交货计划-主表 | 42 | [amccsa_require_schedule.md](./amccsa_require_schedule.md) |
| 44 | `t_amccsa_sdpcode` | SDP代码-主表 | 13 | [amccsa_sdpcode.md](./amccsa_sdpcode.md) |
| 45 | `t_amccsa_sdpcode_l` | SDP代码-多语言表 | 5 | [amccsa_sdpcode.md](./amccsa_sdpcode.md) |
| 46 | `t_amccsa_sdpcodegroup` | EDI协议分组-主表 | 10 | [amccsa_sdpcodegroup.md](./amccsa_sdpcodegroup.md) |
| 47 | `t_amccsa_sdpcodegroup_l` | EDI协议分组-多语言表 | 4 | [amccsa_sdpcodegroup.md](./amccsa_sdpcodegroup.md) |
| 48 | `t_amccsa_shipsch_detail` | 单据体-子表 | 16 | [amccsa_ship_schedule.md](./amccsa_ship_schedule.md) |
| 49 | `t_amccsa_shipschedule` | 滚动要货计划-主表 | 39 | [amccsa_ship_schedule.md](./amccsa_ship_schedule.md) |
| 50 | `t_amccsa_xcsorderentry` | 订单明细-子表 | 43 | [amccsa_xcustschdorder.md](./amccsa_xcustschdorder.md) |
| 51 | `t_amccsa_xcsorderentry_r` | 订单明细-分表 | 24 | [amccsa_xcustschdorder.md](./amccsa_xcustschdorder.md) |
| 52 | `t_amccsa_xcustschdorder` | 销售计划协议变更单-主表 | 43 | [amccsa_xcustschdorder.md](./amccsa_xcustschdorder.md) |
| 53 | `t_amccsa_xcustschdorder_c` | 销售计划协议变更单-分表 | 21 | [amccsa_xcustschdorder.md](./amccsa_xcustschdorder.md) |
