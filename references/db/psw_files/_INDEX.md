# psw 模块表清单

> 本模块共收录 **40** 张表定义，来自 `psw_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category psw
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_psw_adjcap` | 产能调整-主表 | 4 | [psw_adjcap.md](./psw_adjcap.md) |
| 2 | `t_psw_adjcapentry` | 调整明细-子表 | 7 | [psw_adjcap.md](./psw_adjcap.md) |
| 3 | `t_psw_approvalfilter` | 核准平台筛选字段-主表 | 20 | [psw_approval_filter.md](./psw_approval_filter.md) |
| 4 | `t_psw_cac` | 材料可用性分析-主表 | 15 | [psw_cac.md](./psw_cac.md) |
| 5 | `t_psw_cacdemand` | 需求明细-子表 | 16 | [psw_cacsupdem.md](./psw_cacsupdem.md) |
| 6 | `t_psw_cacdetail` | 树形单据体-子表 | 76 | [psw_cac.md](./psw_cac.md) |
| 7 | `t_psw_cacsupdem` | 物料可用性分析供需明细-主表 | 14 | [psw_cacsupdem.md](./psw_cacsupdem.md) |
| 8 | `t_psw_cacsupply` | 供应明细-子表 | 10 | [psw_cacsupdem.md](./psw_cacsupdem.md) |
| 9 | `t_psw_capacityallocbill` | 产能分配清单-子表 | 12 | [psw_masterschedule.md](./psw_masterschedule.md) |
| 10 | `t_psw_capacityplandetail` | 单据体-子表 | 9 | [psw_displayscheme.md](./psw_displayscheme.md) |
| 11 | `t_psw_deletedorder` | deletedorder-子表 | 5 | [psw_masterschedule.md](./psw_masterschedule.md) |
| 12 | `t_psw_displayscheme` | 显示方案-主表 | 23 | [psw_displayscheme.md](./psw_displayscheme.md) |
| 13 | `t_psw_doh` | 预计可用天数-主表 | 9 | [psw_doh.md](./psw_doh.md) |
| 14 | `t_psw_dohdetail` | 预计可用天数明细-子表 | 70 | [psw_doh.md](./psw_doh.md) |
| 15 | `t_psw_filtermateriel` | 物料明细-子表 | 6 | [psw_approval_filter.md](./psw_approval_filter.md) |
| 16 | `t_psw_filterprodline` | 生产线明细-子表 | 6 | [psw_approval_filter.md](./psw_approval_filter.md) |
| 17 | `t_psw_filterreqorg` | 需求组织明细-子表 | 6 | [psw_approval_filter.md](./psw_approval_filter.md) |
| 18 | `t_psw_firmorder` | 计划订单投放-主表 | 10 | [psw_firmplanorder.md](./psw_firmplanorder.md) |
| 19 | `t_psw_firmorderdet` | 计划订单-子表 | 36 | [psw_firmplanorder.md](./psw_firmplanorder.md) |
| 20 | `t_psw_indepdemand` | 独立需求-主表 | 17 | [psw_indepdemand.md](./psw_indepdemand.md) |
| 21 | `t_psw_itemdemand` | 生产线物料需求-主表 | 11 | [psw_itemdemand.md](./psw_itemdemand.md) |
| 22 | `t_psw_itemplandetail` | 需求明细-子表 | 10 | [psw_itemdemand.md](./psw_itemdemand.md) |
| 23 | `t_psw_itemsupply` | 物料供应-主表 | 9 | [psw_itemsupply.md](./psw_itemsupply.md) |
| 24 | `t_psw_linedemand` | 生产线需求-主表 | 10 | [psw_linedemand.md](./psw_linedemand.md) |
| 25 | `t_psw_masterschedule` | 计划编制-主表 | 11 | [psw_masterschedule.md](./psw_masterschedule.md) |
| 26 | `t_psw_mstrschdvercap` | 单据体-子表 | 6 | [psw_mstrschdversion.md](./psw_mstrschdversion.md) |
| 27 | `t_psw_mstrschdvermtl` | 单据体-子表 | 7 | [psw_mstrschdversion.md](./psw_mstrschdversion.md) |
| 28 | `t_psw_mstrschdversion` | 计划编制版本-主表 | 19 | [psw_mstrschdversion.md](./psw_mstrschdversion.md) |
| 29 | `t_psw_mtlmstrschdver` | 计划编制版本物料详情-主表 | 11 | [psw_mtlmstrschdver.md](./psw_mtlmstrschdver.md) |
| 30 | `t_psw_mtlmstrschdverdet` | 数量明细-子表 | 6 | [psw_mtlmstrschdver.md](./psw_mtlmstrschdver.md) |
| 31 | `t_psw_orderinfo` | 订单信息-子表 | 36 | [psw_masterschedule.md](./psw_masterschedule.md) |
| 32 | `t_psw_plandemand` | 生产线需求-子表 | 36 | [psw_linedemand.md](./psw_linedemand.md) |
| 33 | `t_psw_pqoh` | 预计可用库存-主表 | 2 | [psw_pqoh.md](./psw_pqoh.md) |
| 34 | `t_psw_pqohdetail` | -子表 | 74 | [psw_pqoh.md](./psw_pqoh.md) |
| 35 | `t_psw_supplydemandcontras` | 供需即时对应-主表 | 34 | [psw_supplydemandcontrast.md](./psw_supplydemandcontrast.md) |
| 36 | `t_psw_supplydetail` | 单据体-子表 | 37 | [psw_itemsupply.md](./psw_itemsupply.md) |
| 37 | `t_psw_supplyentry` | 单据体-子表 | 24 | [psw_supplydemandcontrast.md](./psw_supplydemandcontrast.md) |
| 38 | `t_psw_workbench` | 工作台首页筛选落库-主表 | 23 | [psw_benchfilter_db.md](./psw_benchfilter_db.md) |
| 39 | `t_psw_workbench` | 生产线计划平台-主表 | 23 | [psw_lineplan.md](./psw_lineplan.md) |
| 40 | `t_psw_workbench` | 生产线计划平台（计划订单）-主表 | 23 | [psw_mrpapproval.md](./psw_mrpapproval.md) |
