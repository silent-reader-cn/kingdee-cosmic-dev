# gtm 模块表清单

> 本模块共收录 **90** 张表定义，来自 `gtm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category gtm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_gtm_cominvoice` | 商业发票-主表 | 27 | [gtm_cominvoice.md](./gtm_cominvoice.md) |
| 2 | `t_gtm_cominvoice_f` | 商业发票-分表 | 11 | [gtm_cominvoice.md](./gtm_cominvoice.md) |
| 3 | `t_gtm_cominvoice_l` | 商业发票-多语言表 | 7 | [gtm_cominvoice.md](./gtm_cominvoice.md) |
| 4 | `t_gtm_cominvoice_t` | 商业发票-分表 | 19 | [gtm_cominvoice.md](./gtm_cominvoice.md) |
| 5 | `t_gtm_cominvoice_tc` | 商业发票-关联追踪表 | 7 | [gtm_cominvoice.md](./gtm_cominvoice.md) |
| 6 | `t_gtm_cominvoice_wb` | 商业发票-反写记录表 | 10 | [gtm_cominvoice.md](./gtm_cominvoice.md) |
| 7 | `t_gtm_cominvoiceentry` | 明细信息-子表 | 21 | [gtm_cominvoice.md](./gtm_cominvoice.md) |
| 8 | `t_gtm_cominvoiceentry_l` | 明细信息-多语言表 | 4 | [gtm_cominvoice.md](./gtm_cominvoice.md) |
| 9 | `t_gtm_cominvoiceentry_lk` | 关联子实体-子表 | 8 | [gtm_cominvoice.md](./gtm_cominvoice.md) |
| 10 | `t_gtm_contpartother` | 其他方-多选基础资料表 | 3 | [gtm_tradecontract.md](./gtm_tradecontract.md) |
| 11 | `t_gtm_customsdistrict` | 海关关区-主表 | 25 | [gtm_customsdistrict.md](./gtm_customsdistrict.md) |
| 12 | `t_gtm_customsdistrict_l` | 海关关区-多语言表 | 5 | [gtm_customsdistrict.md](./gtm_customsdistrict.md) |
| 13 | `t_gtm_customsdistrict_u` | 海关关区-使用范围表 | 3 | [gtm_customsdistrict.md](./gtm_customsdistrict.md) |
| 14 | `t_gtm_customslinkcfg` | 集成参数配置-主表 | 18 | [gtm_customslinkconfig.md](./gtm_customslinkconfig.md) |
| 15 | `t_gtm_customslinkcfg_l` | 集成参数配置-多语言表 | 4 | [gtm_customslinkconfig.md](./gtm_customslinkconfig.md) |
| 16 | `t_gtm_customslinkcfgety` | 海关配置-子表 | 10 | [gtm_customslinkconfig.md](./gtm_customslinkconfig.md) |
| 17 | `t_gtm_customslinkcfgety_l` | 海关配置-多语言表 | 4 | [gtm_customslinkconfig.md](./gtm_customslinkconfig.md) |
| 18 | `t_gtm_customslinkcfgpath` | 接口配置-子表 | 6 | [gtm_customslinkconfig.md](./gtm_customslinkconfig.md) |
| 19 | `t_gtm_customslinkmap` | 集成映射配置-主表 | 22 | [gtm_customslinkmap.md](./gtm_customslinkmap.md) |
| 20 | `t_gtm_customslinkmap_l` | 集成映射配置-多语言表 | 4 | [gtm_customslinkmap.md](./gtm_customslinkmap.md) |
| 21 | `t_gtm_customslinkmap_u` | 集成映射配置-使用范围表 | 3 | [gtm_customslinkmap.md](./gtm_customslinkmap.md) |
| 22 | `t_gtm_customslinkmapety` | 单据体-子表 | 7 | [gtm_customslinkmap.md](./gtm_customslinkmap.md) |
| 23 | `t_gtm_customslinkmapety_l` | 单据体-多语言表 | 4 | [gtm_customslinkmap.md](./gtm_customslinkmap.md) |
| 24 | `t_gtm_customsport` | 海关口岸-主表 | 24 | [gtm_customsport.md](./gtm_customsport.md) |
| 25 | `t_gtm_customsport_l` | 海关口岸-多语言表 | 5 | [gtm_customsport.md](./gtm_customsport.md) |
| 26 | `t_gtm_customsport_u` | 海关口岸-使用范围表 | 3 | [gtm_customsport.md](./gtm_customsport.md) |
| 27 | `t_gtm_declareform` | 报关单-主表 | 33 | [gtm_declareform.md](./gtm_declareform.md) |
| 28 | `t_gtm_declareform_d` | 报关单-分表 | 27 | [gtm_declareform.md](./gtm_declareform.md) |
| 29 | `t_gtm_declareform_f` | 报关单-分表 | 16 | [gtm_declareform.md](./gtm_declareform.md) |
| 30 | `t_gtm_declareform_l` | 报关单-多语言表 | 7 | [gtm_declareform.md](./gtm_declareform.md) |
| 31 | `t_gtm_declareform_t` | 报关单-分表 | 19 | [gtm_declareform.md](./gtm_declareform.md) |
| 32 | `t_gtm_declareform_tc` | 报关单-关联追踪表 | 7 | [gtm_declareform.md](./gtm_declareform.md) |
| 33 | `t_gtm_declareform_wb` | 报关单-反写记录表 | 10 | [gtm_declareform.md](./gtm_declareform.md) |
| 34 | `t_gtm_declareformgood` | 报关商品信息-子表 | 18 | [gtm_declareform.md](./gtm_declareform.md) |
| 35 | `t_gtm_declareformmat` | 报关明细-子表 | 22 | [gtm_declareform.md](./gtm_declareform.md) |
| 36 | `t_gtm_declareformmat_l` | 报关明细-多语言表 | 4 | [gtm_declareform.md](./gtm_declareform.md) |
| 37 | `t_gtm_declareformmat_lk` | 关联子实体-子表 | 8 | [gtm_declareform.md](./gtm_declareform.md) |
| 38 | `t_gtm_declareformtax` | 税务信息-子表 | 8 | [gtm_declareform.md](./gtm_declareform.md) |
| 39 | `t_gtm_expenseitem` | 费用项目-子表 | 6 | [gtm_tradeterm.md](./gtm_tradeterm.md) |
| 40 | `t_gtm_expenseitem_l` | 费用项目-多语言表 | 4 | [gtm_tradeterm.md](./gtm_tradeterm.md) |
| 41 | `t_gtm_inspectplan` | 检查方案配置-主表 | 16 | [gtm_inspectionplan.md](./gtm_inspectionplan.md) |
| 42 | `t_gtm_inspectplan_l` | 检查方案配置-多语言表 | 5 | [gtm_inspectionplan.md](./gtm_inspectionplan.md) |
| 43 | `t_gtm_inspectplanmap` | 单据字段映射-子表 | 8 | [gtm_inspectionplan.md](./gtm_inspectionplan.md) |
| 44 | `t_gtm_inspectplanrange` | 检查单据范围-子表 | 4 | [gtm_inspectionplan.md](./gtm_inspectionplan.md) |
| 45 | `t_gtm_ladingbill` | 提单-主表 | 34 | [gtm_ladingbill.md](./gtm_ladingbill.md) |
| 46 | `t_gtm_ladingbill_l` | 提单-多语言表 | 7 | [gtm_ladingbill.md](./gtm_ladingbill.md) |
| 47 | `t_gtm_ladingbill_t` | 提单-分表 | 27 | [gtm_ladingbill.md](./gtm_ladingbill.md) |
| 48 | `t_gtm_ladingbill_tc` | 提单-关联追踪表 | 7 | [gtm_ladingbill.md](./gtm_ladingbill.md) |
| 49 | `t_gtm_ladingbill_wb` | 提单-反写记录表 | 10 | [gtm_ladingbill.md](./gtm_ladingbill.md) |
| 50 | `t_gtm_ladingbillentry` | 明细信息-子表 | 30 | [gtm_ladingbill.md](./gtm_ladingbill.md) |
| 51 | `t_gtm_ladingbillentry_l` | 明细信息-多语言表 | 4 | [gtm_ladingbill.md](./gtm_ladingbill.md) |
| 52 | `t_gtm_ladingbillentry_lk` | 关联子实体-子表 | 8 | [gtm_ladingbill.md](./gtm_ladingbill.md) |
| 53 | `t_gtm_licence_bill_record` | 许可证业务单据关联记录-主表 | 13 | [gtm_licence_bill_record.md](./gtm_licence_bill_record.md) |
| 54 | `t_gtm_naturelevy` | 征免性质-主表 | 21 | [gtm_naturelevy.md](./gtm_naturelevy.md) |
| 55 | `t_gtm_naturelevy_l` | 征免性质-多语言表 | 6 | [gtm_naturelevy.md](./gtm_naturelevy.md) |
| 56 | `t_gtm_naturelevy_u` | 征免性质-使用范围表 | 3 | [gtm_naturelevy.md](./gtm_naturelevy.md) |
| 57 | `t_gtm_packinglist` | 装箱单-主表 | 32 | [gtm_packinglist.md](./gtm_packinglist.md) |
| 58 | `t_gtm_packinglist_l` | 装箱单-多语言表 | 7 | [gtm_packinglist.md](./gtm_packinglist.md) |
| 59 | `t_gtm_packinglist_t` | 装箱单-分表 | 19 | [gtm_packinglist.md](./gtm_packinglist.md) |
| 60 | `t_gtm_packinglist_tc` | 装箱单-关联追踪表 | 7 | [gtm_packinglist.md](./gtm_packinglist.md) |
| 61 | `t_gtm_packinglist_wb` | 装箱单-反写记录表 | 10 | [gtm_packinglist.md](./gtm_packinglist.md) |
| 62 | `t_gtm_palistentry` | 明细信息-子表 | 27 | [gtm_packinglist.md](./gtm_packinglist.md) |
| 63 | `t_gtm_palistentry_l` | 明细信息-多语言表 | 4 | [gtm_packinglist.md](./gtm_packinglist.md) |
| 64 | `t_gtm_palistentry_lk` | 关联子实体-子表 | 8 | [gtm_packinglist.md](./gtm_packinglist.md) |
| 65 | `t_gtm_queryscheme` | 单证合规性方案查询-主表 | 15 | [gtm_queryscheme.md](./gtm_queryscheme.md) |
| 66 | `t_gtm_queryscheme_l` | 单证合规性方案查询-多语言表 | 4 | [gtm_queryscheme.md](./gtm_queryscheme.md) |
| 67 | `t_gtm_regulatorymode` | 监管方式-主表 | 21 | [gtm_regulatorymode.md](./gtm_regulatorymode.md) |
| 68 | `t_gtm_regulatorymode_l` | 监管方式-多语言表 | 6 | [gtm_regulatorymode.md](./gtm_regulatorymode.md) |
| 69 | `t_gtm_regulatorymode_u` | 监管方式-使用范围表 | 3 | [gtm_regulatorymode.md](./gtm_regulatorymode.md) |
| 70 | `t_gtm_slintegratelog` | 国际贸易关务集成日志-主表 | 20 | [gtm_slintegratelog.md](./gtm_slintegratelog.md) |
| 71 | `t_gtm_slintegratelog_l` | 国际贸易关务集成日志-多语言表 | 4 | [gtm_slintegratelog.md](./gtm_slintegratelog.md) |
| 72 | `t_gtm_tracontract` | 贸易协议-主表 | 84 | [gtm_tradecontract.md](./gtm_tradecontract.md) |
| 73 | `t_gtm_tracontract_f` | 贸易协议-分表 | 25 | [gtm_tradecontract.md](./gtm_tradecontract.md) |
| 74 | `t_gtm_tracontract_l` | 贸易协议-多语言表 | 7 | [gtm_tradecontract.md](./gtm_tradecontract.md) |
| 75 | `t_gtm_tracontract_s` | 贸易协议-分表 | 17 | [gtm_tradecontract.md](./gtm_tradecontract.md) |
| 76 | `t_gtm_tracontractentry` | 物料明细-子表 | 26 | [gtm_tradecontract.md](./gtm_tradecontract.md) |
| 77 | `t_gtm_tracontractentry_f` | 物料明细-分表 | 29 | [gtm_tradecontract.md](./gtm_tradecontract.md) |
| 78 | `t_gtm_tracontractentry_r` | 物料明细-分表 | 13 | [gtm_tradecontract.md](./gtm_tradecontract.md) |
| 79 | `t_gtm_tracontractpentry` | 付款计划-子表 | 13 | [gtm_tradecontract.md](./gtm_tradecontract.md) |
| 80 | `t_gtm_tracontracttentry` | 协议条款-子表 | 7 | [gtm_tradecontract.md](./gtm_tradecontract.md) |
| 81 | `t_gtm_tradeterm` | 贸易术语-主表 | 30 | [gtm_tradeterm.md](./gtm_tradeterm.md) |
| 82 | `t_gtm_tradeterm_l` | 贸易术语-多语言表 | 6 | [gtm_tradeterm.md](./gtm_tradeterm.md) |
| 83 | `t_gtm_tradeterm_u` | 贸易术语-使用范围表 | 3 | [gtm_tradeterm.md](./gtm_tradeterm.md) |
| 84 | `t_gtm_tradetermgroup` | 贸易术语分组-主表 | 17 | [gtm_tradetermgroup.md](./gtm_tradetermgroup.md) |
| 85 | `t_gtm_tradetermgroup_l` | 贸易术语分组-多语言表 | 5 | [gtm_tradetermgroup.md](./gtm_tradetermgroup.md) |
| 86 | `t_gtm_transportmode` | 运输方式-主表 | 26 | [gtm_transportmode.md](./gtm_transportmode.md) |
| 87 | `t_gtm_transportmode_l` | 运输方式-多语言表 | 5 | [gtm_transportmode.md](./gtm_transportmode.md) |
| 88 | `t_gtm_transportmode_u` | 运输方式-使用范围表 | 3 | [gtm_transportmode.md](./gtm_transportmode.md) |
| 89 | `t_gtm_transportmodegroup` | 运输方式分组-主表 | 17 | [gtm_transportmodegroup.md](./gtm_transportmodegroup.md) |
| 90 | `t_gtm_transportmodegroup_l` | 运输方式分组-多语言表 | 5 | [gtm_transportmodegroup.md](./gtm_transportmodegroup.md) |
