# scax 模块表清单

> 本模块共收录 **53** 张表定义，来自 `scax_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope scax
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_cad_calctaskrecord` | 卷算报告-主表 | 14 | [scax_calctaskrecord.md](./scax_calctaskrecord.md) |
| 2 | `t_cad_calctaskrecord_l` | 卷算报告-多语言表 | 3 | [scax_calctaskrecord.md](./scax_calctaskrecord.md) |
| 3 | `t_scax_bomsetting` | 成本BOM设置-主表 | 21 | [scax_bomsetting.md](./scax_bomsetting.md) |
| 4 | `t_scax_bomsetting_l` | 成本BOM设置-多语言表 | 4 | [scax_bomsetting.md](./scax_bomsetting.md) |
| 5 | `t_scax_calcbomcost` | 模拟卷算结果-主表 | 17 | [scax_calcbomcost.md](./scax_calcbomcost.md) |
| 6 | `t_scax_calcbomdetail` | 半成品耗用详情-子表 | 12 | [scax_calcbomcost.md](./scax_calcbomcost.md) |
| 7 | `t_scax_calcruleroutesort` | 工艺路线优先级排序-子表 | 5 | [scax_costcalcrule.md](./scax_costcalcrule.md) |
| 8 | `t_scax_childcostdetail` | 单据体-子表 | 18 | [scax_calcbomcost.md](./scax_calcbomcost.md) |
| 9 | `t_scax_costbom` | 成本BOM-主表 | 31 | [scax_costbom.md](./scax_costbom.md) |
| 10 | `t_scax_costbom_l` | 成本BOM-多语言表 | 4 | [scax_costbom.md](./scax_costbom.md) |
| 11 | `t_scax_costbom_u` | 成本BOM-使用范围表 | 3 | [scax_costbom.md](./scax_costbom.md) |
| 12 | `t_scax_costbomcopentry` | 联副产品-子表 | 10 | [scax_costbom.md](./scax_costbom.md) |
| 13 | `t_scax_costbomcopentry_l` | 联副产品-多语言表 | 4 | [scax_costbom.md](./scax_costbom.md) |
| 14 | `t_scax_costbomentry` | 组件信息-子表 | 19 | [scax_costbom.md](./scax_costbom.md) |
| 15 | `t_scax_costcalcrule` | 卷算数据归集方案-主表 | 24 | [scax_costcalcrule.md](./scax_costcalcrule.md) |
| 16 | `t_scax_costcalcrule_l` | 卷算数据归集方案-多语言表 | 4 | [scax_costcalcrule.md](./scax_costcalcrule.md) |
| 17 | `t_scax_costcalcrulesort` | 优先级排序-子表 | 5 | [scax_costcalcrule.md](./scax_costcalcrule.md) |
| 18 | `t_scax_costpriceplan` | 取价方案-主表 | 15 | [scax_costpriceplan.md](./scax_costpriceplan.md) |
| 19 | `t_scax_costpriceplan_l` | 取价方案-多语言表 | 5 | [scax_costpriceplan.md](./scax_costpriceplan.md) |
| 20 | `t_scax_costpricerule` | 取价规则-主表 | 17 | [scax_costpricerule.md](./scax_costpricerule.md) |
| 21 | `t_scax_costpricerule_l` | 取价规则-多语言表 | 5 | [scax_costpricerule.md](./scax_costpricerule.md) |
| 22 | `t_scax_costroute` | 成本工艺路线-主表 | 30 | [scax_costroute.md](./scax_costroute.md) |
| 23 | `t_scax_costroute_l` | 成本工艺路线-多语言表 | 4 | [scax_costroute.md](./scax_costroute.md) |
| 24 | `t_scax_costroute_u` | 成本工艺路线-使用范围表 | 3 | [scax_costroute.md](./scax_costroute.md) |
| 25 | `t_scax_costrouteactive` | 子单据体-子表 | 13 | [scax_costroute.md](./scax_costroute.md) |
| 26 | `t_scax_costrouteentry` | 工序-子表 | 19 | [scax_costroute.md](./scax_costroute.md) |
| 27 | `t_scax_costrouteentry_l` | 工序-多语言表 | 4 | [scax_costroute.md](./scax_costroute.md) |
| 28 | `t_scax_matstdpricedetail` | 成本子要素信息-子表 | 7 | [scax_matstdprices.md](./scax_matstdprices.md) |
| 29 | `t_scax_matstdpriceentry` | 物料信息-子表 | 11 | [scax_matstdprices.md](./scax_matstdprices.md) |
| 30 | `t_scax_matstdprices` | 物料标准价目表-主表 | 12 | [scax_matstdprices.md](./scax_matstdprices.md) |
| 31 | `t_scax_matstdprices_l` | 物料标准价目表-多语言表 | 4 | [scax_matstdprices.md](./scax_matstdprices.md) |
| 32 | `t_scax_mftworkprice` | 作业价格维护-主表 | 17 | [scax_mftworkprice.md](./scax_mftworkprice.md) |
| 33 | `t_scax_mftworkprice_l` | 作业价格维护-多语言表 | 4 | [scax_mftworkprice.md](./scax_mftworkprice.md) |
| 34 | `t_scax_mftworkpricedetail` | 成本要素明细-子表 | 8 | [scax_mftworkprice.md](./scax_mftworkprice.md) |
| 35 | `t_scax_mftworkpriceentry` | 价格维护-子表 | 11 | [scax_mftworkprice.md](./scax_mftworkprice.md) |
| 36 | `t_scax_outpricedetail` | 成本子要素信息-子表 | 7 | [scax_outsourceprices.md](./scax_outsourceprices.md) |
| 37 | `t_scax_outpriceentry` | 物料信息-子表 | 11 | [scax_outsourceprices.md](./scax_outsourceprices.md) |
| 38 | `t_scax_outsourceprices` | 产品委外标准价目表-主表 | 12 | [scax_outsourceprices.md](./scax_outsourceprices.md) |
| 39 | `t_scax_outsourceprices_l` | 产品委外标准价目表-多语言表 | 4 | [scax_outsourceprices.md](./scax_outsourceprices.md) |
| 40 | `t_scax_planoutpriceentry` | 产品委外标准价目表单据体-子表 | 5 | [scax_costpriceplan.md](./scax_costpriceplan.md) |
| 41 | `t_scax_planpurpricesentry` | 物料价目表单据体-子表 | 5 | [scax_costpriceplan.md](./scax_costpriceplan.md) |
| 42 | `t_scax_routersetting` | 成本工艺路线设置-主表 | 13 | [scax_routersetting.md](./scax_routersetting.md) |
| 43 | `t_scax_routersetting_l` | 成本工艺路线设置-多语言表 | 4 | [scax_routersetting.md](./scax_routersetting.md) |
| 44 | `t_scax_standardhour` | 标准工时维护-主表 | 14 | [scax_standardhour.md](./scax_standardhour.md) |
| 45 | `t_scax_standardhour_l` | 标准工时维护-多语言表 | 4 | [scax_standardhour.md](./scax_standardhour.md) |
| 46 | `t_scax_standardhourentry` | 物料信息-子表 | 15 | [scax_standardhour.md](./scax_standardhour.md) |
| 47 | `t_scax_workcostcenter` | 适配成本中心-多选基础资料表 | 3 | [scax_worksplit.md](./scax_worksplit.md) |
| 48 | `t_scax_worksplit` | 作业分割方案-主表 | 13 | [scax_worksplit.md](./scax_worksplit.md) |
| 49 | `t_scax_worksplit_l` | 作业分割方案-多语言表 | 5 | [scax_worksplit.md](./scax_worksplit.md) |
| 50 | `t_scax_worksplitdetail` | 成本子要素-子表 | 6 | [scax_worksplit.md](./scax_worksplit.md) |
| 51 | `t_scax_worksplitentry` | 作业类型-子表 | 6 | [scax_worksplit.md](./scax_worksplit.md) |
| 52 | `t_scax_worktype` | 作业类型-主表 | 14 | [scax_worktype.md](./scax_worktype.md) |
| 53 | `t_scax_worktype_l` | 作业类型-多语言表 | 5 | [scax_worktype.md](./scax_worktype.md) |
