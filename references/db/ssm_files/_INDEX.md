# ssm 模块表清单

> 本模块共收录 **42** 张表定义，来自 `ssm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ssm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ssm_allocation` | 采购计划协议配额-主表 | 15 | [ssm_allocation.md](./ssm_allocation.md) |
| 2 | `t_ssm_allocationdetail` | 配额明细-子表 | 10 | [ssm_allocation.md](./ssm_allocation.md) |
| 3 | `t_ssm_allocationinfo` | 配额区间-子表 | 6 | [ssm_allocation.md](./ssm_allocation.md) |
| 4 | `t_ssm_displayscheme` | 显示方案-主表 | 15 | [ssm_displayscheme.md](./ssm_displayscheme.md) |
| 5 | `t_ssm_indepdemand` | 采购独立需求-主表 | 16 | [ssm_indepdemand.md](./ssm_indepdemand.md) |
| 6 | `t_ssm_itemdemand` | 采购物料需求-主表 | 11 | [ssm_itemdemand.md](./ssm_itemdemand.md) |
| 7 | `t_ssm_itemplandetail` | 需求明细-子表 | 10 | [ssm_itemdemand.md](./ssm_itemdemand.md) |
| 8 | `t_ssm_itemsupply` | 物料供应-主表 | 9 | [ssm_itemsupply.md](./ssm_itemsupply.md) |
| 9 | `t_ssm_log` | 应用日志-主表 | 10 | [ssm_log.md](./ssm_log.md) |
| 10 | `t_ssm_logentry` | 单据体-子表 | 7 | [ssm_log.md](./ssm_log.md) |
| 11 | `t_ssm_masterschddetail` | -子表 | 20 | [ssm_masterschedule.md](./ssm_masterschedule.md) |
| 12 | `t_ssm_masterschdinfo` | 采购协议列表-子表 | 6 | [ssm_masterschedule.md](./ssm_masterschedule.md) |
| 13 | `t_ssm_masterschdtree` | 树形子单据体-子表 | 40 | [ssm_masterschedule.md](./ssm_masterschedule.md) |
| 14 | `t_ssm_masterschedule` | 采购计划编制-主表 | 11 | [ssm_masterschedule.md](./ssm_masterschedule.md) |
| 15 | `t_ssm_netreqdetail` | 单据体-子表 | 11 | [ssm_netrequired.md](./ssm_netrequired.md) |
| 16 | `t_ssm_netrequired` | 采购净供需-主表 | 2 | [ssm_netrequired.md](./ssm_netrequired.md) |
| 17 | `t_ssm_plandemand` | 采购需求-子表 | 36 | [ssm_purdemand.md](./ssm_purdemand.md) |
| 18 | `t_ssm_plansch_detail` | 单据体-子表 | 20 | [ssm_plan_schedule.md](./ssm_plan_schedule.md) |
| 19 | `t_ssm_planschedule` | 供应商预测计划-主表 | 26 | [ssm_plan_schedule.md](./ssm_plan_schedule.md) |
| 20 | `t_ssm_pqohdetail` | -子表 | 75 | [ssm_supdembalancing.md](./ssm_supdembalancing.md) |
| 21 | `t_ssm_purdemand` | 采购需求-主表 | 10 | [ssm_purdemand.md](./ssm_purdemand.md) |
| 22 | `t_ssm_purorderentry` | 单据体-子表 | 42 | [ssm_purschdorder.md](./ssm_purschdorder.md) |
| 23 | `t_ssm_purorderentry_r` | 单据体-分表 | 18 | [ssm_purschdorder.md](./ssm_purschdorder.md) |
| 24 | `t_ssm_purschdorder` | 采购计划协议-主表 | 48 | [ssm_purschdorder.md](./ssm_purschdorder.md) |
| 25 | `t_ssm_purschdorder` | 采购计划协议F7-主表 | 48 | [ssm_purschdorder_f7.md](./ssm_purschdorder_f7.md) |
| 26 | `t_ssm_purschdorder_s` | 采购计划协议-分表 | 8 | [ssm_purschdorder.md](./ssm_purschdorder.md) |
| 27 | `t_ssm_purschdorder_s` | 采购计划协议F7-分表 | 8 | [ssm_purschdorder_f7.md](./ssm_purschdorder_f7.md) |
| 28 | `t_ssm_requiresc_detail` | 单据体-子表 | 20 | [ssm_require_schedule.md](./ssm_require_schedule.md) |
| 29 | `t_ssm_requireschedule` | 滚动收货计划-主表 | 27 | [ssm_require_schedule.md](./ssm_require_schedule.md) |
| 30 | `t_ssm_shipsch_detail` | 单据体-子表 | 21 | [ssm_ship_schedule.md](./ssm_ship_schedule.md) |
| 31 | `t_ssm_shipschedule` | 供应商交货计划-主表 | 26 | [ssm_ship_schedule.md](./ssm_ship_schedule.md) |
| 32 | `t_ssm_supdembalancing` | 预计可用库存-主表 | 2 | [ssm_supdembalancing.md](./ssm_supdembalancing.md) |
| 33 | `t_ssm_supplydemandcontras` | 供需即时对应-主表 | 31 | [ssm_supplydemandcontrast.md](./ssm_supplydemandcontrast.md) |
| 34 | `t_ssm_supplydetail` | 单据体-子表 | 31 | [ssm_itemsupply.md](./ssm_itemsupply.md) |
| 35 | `t_ssm_supplyentry` | 单据体-子表 | 24 | [ssm_supplydemandcontrast.md](./ssm_supplydemandcontrast.md) |
| 36 | `t_ssm_workbench` | 采购工作台首页筛选落库-主表 | 23 | [ssm_benchfilter_db.md](./ssm_benchfilter_db.md) |
| 37 | `t_ssm_workbench` | 采购计划平台-主表 | 23 | [ssm_purplan.md](./ssm_purplan.md) |
| 38 | `t_ssm_workbench` | 采购计划工作台模板-主表 | 23 | [ssm_workbenchbase.md](./ssm_workbenchbase.md) |
| 39 | `t_ssm_xpurorderentry` | 单据体-子表 | 44 | [ssm_xpurschdorder.md](./ssm_xpurschdorder.md) |
| 40 | `t_ssm_xpurorderentry_r` | 单据体-分表 | 16 | [ssm_xpurschdorder.md](./ssm_xpurschdorder.md) |
| 41 | `t_ssm_xpurschdorder` | 采购计划协议变更单-主表 | 58 | [ssm_xpurschdorder.md](./ssm_xpurschdorder.md) |
| 42 | `t_ssm_xpurschdorder_s` | 采购计划协议变更单-分表 | 8 | [ssm_xpurschdorder.md](./ssm_xpurschdorder.md) |
