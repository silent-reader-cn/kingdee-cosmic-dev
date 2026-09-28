# lgm 模块表清单

> 本模块共收录 **55** 张表定义，来自 `lgm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category lgm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_conm_contpartother` | 其他方-多选基础资料表 | 3 | [lgm_tradecontract.md](./lgm_tradecontract.md) |
| 2 | `t_lgm_shipment` | 运输单-主表 | 31 | [lgm_shipment.md](./lgm_shipment.md) |
| 3 | `t_lgm_shipment_l` | 运输单-多语言表 | 5 | [lgm_shipment.md](./lgm_shipment.md) |
| 4 | `t_lgm_shipment_tc` | 运输单-关联追踪表 | 7 | [lgm_shipment.md](./lgm_shipment.md) |
| 5 | `t_lgm_shipment_wb` | 运输单-反写记录表 | 10 | [lgm_shipment.md](./lgm_shipment.md) |
| 6 | `t_lgm_shipmententry` | 物料明细-子表 | 28 | [lgm_shipment.md](./lgm_shipment.md) |
| 7 | `t_lgm_shipmententry_l` | 物料明细-多语言表 | 5 | [lgm_shipment.md](./lgm_shipment.md) |
| 8 | `t_lgm_shipmententry_lk` | 关联子实体-子表 | 8 | [lgm_shipment.md](./lgm_shipment.md) |
| 9 | `t_lgm_shipmententry_r` | 物料明细-分表 | 17 | [lgm_shipment.md](./lgm_shipment.md) |
| 10 | `t_lgm_shipmentexpense` | 费用明细-子表 | 22 | [lgm_shipment.md](./lgm_shipment.md) |
| 11 | `t_lgm_shipmentexpense_l` | 费用明细-多语言表 | 4 | [lgm_shipment.md](./lgm_shipment.md) |
| 12 | `t_lgm_shipmentnodes` | 关键节点-子表 | 10 | [lgm_shipment.md](./lgm_shipment.md) |
| 13 | `t_lgm_shipmentsplitentry` | 分摊费用-子表 | 14 | [lgm_shipment.md](./lgm_shipment.md) |
| 14 | `t_lgm_shipmentsplitorder` | 订单明细-子表 | 9 | [lgm_shipment.md](./lgm_shipment.md) |
| 15 | `t_lgm_shipmentstages` | 运输阶段-子表 | 21 | [lgm_shipment.md](./lgm_shipment.md) |
| 16 | `t_lgm_shipmentstages_l` | 运输阶段-多语言表 | 4 | [lgm_shipment.md](./lgm_shipment.md) |
| 17 | `t_lgm_shipmentwrap` | 包装信息-子表 | 16 | [lgm_shipment.md](./lgm_shipment.md) |
| 18 | `t_lgm_shippingnode` | 运输单关键节点-主表 | 18 | [lgm_shippingnode.md](./lgm_shippingnode.md) |
| 19 | `t_lgm_shippingnode_l` | 运输单关键节点-多语言表 | 5 | [lgm_shippingnode.md](./lgm_shippingnode.md) |
| 20 | `t_lgm_shippingnode_rel` | 前置节点-多选基础资料表 | 3 | [lgm_shippingnode.md](./lgm_shippingnode.md) |
| 21 | `t_lgm_shippingnodeconfig` | 转换规则配置细则-子表 | 7 | [lgm_shippingnode.md](./lgm_shippingnode.md) |
| 22 | `t_lgm_shippingpoint` | 装运点-主表 | 32 | [lgm_shippingpoint.md](./lgm_shippingpoint.md) |
| 23 | `t_lgm_shippingpoint_l` | 装运点-多语言表 | 4 | [lgm_shippingpoint.md](./lgm_shippingpoint.md) |
| 24 | `t_lgm_shippingpoint_u` | 装运点-使用范围表 | 3 | [lgm_shippingpoint.md](./lgm_shippingpoint.md) |
| 25 | `t_lgm_shippingpointgroup` | 装运点分类-主表 | 17 | [lgm_shippingpointgroup.md](./lgm_shippingpointgroup.md) |
| 26 | `t_lgm_shippingpointgroup_l` | 装运点分类-多语言表 | 5 | [lgm_shippingpointgroup.md](./lgm_shippingpointgroup.md) |
| 27 | `t_lgm_shipservicelog` | 航迹跟踪查询记录-主表 | 14 | [lgm_shipservicelog.md](./lgm_shipservicelog.md) |
| 28 | `t_lgm_shiptool` | 运输工具档案-主表 | 20 | [lgm_shiptool.md](./lgm_shiptool.md) |
| 29 | `t_lgm_shiptool_l` | 运输工具档案-多语言表 | 4 | [lgm_shiptool.md](./lgm_shiptool.md) |
| 30 | `t_lgm_shiptrackinfo` | 航迹跟踪-主表 | 18 | [lgm_shiptrackinfo.md](./lgm_shiptrackinfo.md) |
| 31 | `t_lgm_shipunittype` | 运输单元类型-主表 | 33 | [lgm_shipunittype.md](./lgm_shipunittype.md) |
| 32 | `t_lgm_shipunittype_l` | 运输单元类型-多语言表 | 5 | [lgm_shipunittype.md](./lgm_shipunittype.md) |
| 33 | `t_lgm_shipunittype_u` | 运输单元类型-使用范围表 | 3 | [lgm_shipunittype.md](./lgm_shipunittype.md) |
| 34 | `t_lgm_shipunittypegr` | 运输单元类型分组-主表 | 17 | [lgm_shipunittypegrp.md](./lgm_shipunittypegrp.md) |
| 35 | `t_lgm_shipunittypegr_l` | 运输单元类型分组-多语言表 | 5 | [lgm_shipunittypegrp.md](./lgm_shipunittypegrp.md) |
| 36 | `t_lgm_termsentry` | 协议条款-子表 | 7 | [lgm_tradecontract.md](./lgm_tradecontract.md) |
| 37 | `t_lgm_tracontract` | 运输协议-主表 | 46 | [lgm_tradecontract.md](./lgm_tradecontract.md) |
| 38 | `t_lgm_tracontract_f` | 运输协议-分表 | 14 | [lgm_tradecontract.md](./lgm_tradecontract.md) |
| 39 | `t_lgm_tracontract_l` | 运输协议-多语言表 | 5 | [lgm_tradecontract.md](./lgm_tradecontract.md) |
| 40 | `t_lgm_tracontract_s` | 运输协议-分表 | 33 | [lgm_tradecontract.md](./lgm_tradecontract.md) |
| 41 | `t_lgm_tracontractentry` | 费用明细-子表 | 15 | [lgm_tradecontract.md](./lgm_tradecontract.md) |
| 42 | `t_lgm_transportroute` | 运输路线-主表 | 28 | [lgm_transportroute.md](./lgm_transportroute.md) |
| 43 | `t_lgm_transportroute_e` | 单据体-子表 | 8 | [lgm_transportroute.md](./lgm_transportroute.md) |
| 44 | `t_lgm_transportroute_l` | 运输路线-多语言表 | 4 | [lgm_transportroute.md](./lgm_transportroute.md) |
| 45 | `t_lgm_transportroute_u` | 运输路线-使用范围表 | 3 | [lgm_transportroute.md](./lgm_transportroute.md) |
| 46 | `t_plat_quoteconentry` | 前置条件-子表 | 7 | [lgm_quotestrategy.md](./lgm_quotestrategy.md) |
| 47 | `t_plat_quotescheme` | 运输取价方案-主表 | 26 | [lgm_quotescheme.md](./lgm_quotescheme.md) |
| 48 | `t_plat_quotescheme_l` | 运输取价方案-多语言表 | 5 | [lgm_quotescheme.md](./lgm_quotescheme.md) |
| 49 | `t_plat_quoteschemeentry` | 字段映射单据体-子表 | 11 | [lgm_quotescheme.md](./lgm_quotescheme.md) |
| 50 | `t_plat_quotesortentry` | 价格排序-子表 | 6 | [lgm_quotescheme.md](./lgm_quotescheme.md) |
| 51 | `t_plat_quotestentry` | 方案排序单据体-子表 | 11 | [lgm_quotestrategy.md](./lgm_quotestrategy.md) |
| 52 | `t_plat_quotestrategy` | 运输取价策略-主表 | 25 | [lgm_quotestrategy.md](./lgm_quotestrategy.md) |
| 53 | `t_plat_quotestrategy_l` | 运输取价策略-多语言表 | 5 | [lgm_quotestrategy.md](./lgm_quotestrategy.md) |
| 54 | `t_plat_quotestrategy_m` | 运输取价策略-使用范围位图表 | 2 | [lgm_quotestrategy.md](./lgm_quotestrategy.md) |
| 55 | `t_plat_quotestrategy_u` | 运输取价策略-使用范围表 | 3 | [lgm_quotestrategy.md](./lgm_quotestrategy.md) |
