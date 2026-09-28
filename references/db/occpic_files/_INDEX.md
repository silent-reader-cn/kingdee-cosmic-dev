# occpic 模块表清单

> 本模块共收录 **68** 张表定义，来自 `occpic_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category occpic
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_occpic_accrual` | 返利预提单-主表 | 28 | [occpic_rebateaccrual.md](./occpic_rebateaccrual.md) |
| 2 | `t_occpic_accrual_ee` | 预提明细-子表 | 38 | [occpic_rebateaccrual.md](./occpic_rebateaccrual.md) |
| 3 | `t_occpic_accrual_ee_lk` | 关联子实体-子表 | 10 | [occpic_rebateaccrual.md](./occpic_rebateaccrual.md) |
| 4 | `t_occpic_accrual_see` | 预算汇总-子表 | 14 | [occpic_rebateaccrual.md](./occpic_rebateaccrual.md) |
| 5 | `t_occpic_accrual_tc` | 返利预提单-关联追踪表 | 7 | [occpic_rebateaccrual.md](./occpic_rebateaccrual.md) |
| 6 | `t_occpic_accrual_wb` | 返利预提单-反写记录表 | 10 | [occpic_rebateaccrual.md](./occpic_rebateaccrual.md) |
| 7 | `t_occpic_rbtgt_form_dt` | 返利标准-子表 | 15 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 8 | `t_occpic_rbtgt_itemclass` | 返利商品-子表 | 7 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 9 | `t_occpic_rbtgt_itemfomul` | 分组返利标准-子表 | 19 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 10 | `t_occpic_rebatebasetab` | 返利数据底表-主表 | 38 | [occpibc_rebatebasetab.md](./occpibc_rebatebasetab.md) |
| 11 | `t_occpic_rebatepbdgentry` | 返利预结算明细-子表 | 62 | [occpic_rebateprebudget.md](./occpic_rebateprebudget.md) |
| 12 | `t_occpic_rebatepbdgentry_lk` | 关联子实体-子表 | 16 | [occpic_rebateprebudget.md](./occpic_rebateprebudget.md) |
| 13 | `t_occpic_rebatepolicy` | 返利政策-主表 | 31 | [occpic_rebatepolicy.md](./occpic_rebatepolicy.md) |
| 14 | `t_occpic_rebatepolicy` | 返利政策F7-主表 | 31 | [ocdbd_rebatepolicyf7.md](./ocdbd_rebatepolicyf7.md) |
| 15 | `t_occpic_rebateprbd_sa` | 商品销售属性-多选基础资料表 | 3 | [occpic_rebateprebudget.md](./occpic_rebateprebudget.md) |
| 16 | `t_occpic_rebateprebudget` | 返利预结算单-主表 | 63 | [occpic_rebateprebudget.md](./occpic_rebateprebudget.md) |
| 17 | `t_occpic_rebateprebudget_tc` | 返利预结算单-关联追踪表 | 7 | [occpic_rebateprebudget.md](./occpic_rebateprebudget.md) |
| 18 | `t_occpic_rebateprebudget_wb` | 返利预结算单-反写记录表 | 10 | [occpic_rebateprebudget.md](./occpic_rebateprebudget.md) |
| 19 | `t_occpic_rebatestatement` | 返利结算单-主表 | 53 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 20 | `t_occpic_rebatestatement` | 返利结算单F7-主表 | 53 | [occpic_rebatestatementf7.md](./occpic_rebatestatementf7.md) |
| 21 | `t_occpic_rebatestatement_lk` | 关联子实体-子表 | 6 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 22 | `t_occpic_rebatestatement_tc` | 返利结算单-关联追踪表 | 7 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 23 | `t_occpic_rebatestatement_wb` | 返利结算单-反写记录表 | 10 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 24 | `t_occpic_rebatestm_sa` | 商品销售属性-多选基础资料表 | 3 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 25 | `t_occpic_rebatestm_see` | 预算汇总-子表 | 14 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 26 | `t_occpic_rebatestmentry` | 返利结算明细-子表 | 65 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 27 | `t_occpic_rebatestmentry_lk` | 关联子实体-子表 | 6 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 28 | `t_occpic_rebatetarget` | 政策目标-主表 | 40 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 29 | `t_occpic_rebatetarget` | 政策目标F7-主表 | 40 | [ocdbd_rebatetargetf7.md](./ocdbd_rebatetargetf7.md) |
| 30 | `t_occpic_rebatetarget_lk` | 关联子实体-子表 | 6 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 31 | `t_occpic_rebatetarget_tc` | 政策目标-关联追踪表 | 7 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 32 | `t_occpic_rebatetarget_wb` | 政策目标-反写记录表 | 10 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 33 | `t_occpic_rp_bnfcust` | 返利对象-子表 | 9 | [occpic_rebatepolicy.md](./occpic_rebatepolicy.md) |
| 34 | `t_occpic_rp_formula` | 返利标准-子表 | 15 | [occpic_rebatepolicy.md](./occpic_rebatepolicy.md) |
| 35 | `t_occpic_rp_itemclass` | 返利商品-子表 | 7 | [occpic_rebatepolicy.md](./occpic_rebatepolicy.md) |
| 36 | `t_occpic_rp_itemfomul` | 分组返利标准-子表 | 19 | [occpic_rebatepolicy.md](./occpic_rebatepolicy.md) |
| 37 | `t_occpic_spolicy` | 采购返利政策-主表 | 26 | [occpic_supplierpolicy.md](./occpic_supplierpolicy.md) |
| 38 | `t_occpic_spolicy_ice` | 返利对象-子表 | 5 | [occpic_supplierpolicy.md](./occpic_supplierpolicy.md) |
| 39 | `t_occpic_spolicy_ife` | 返利标准-子表 | 19 | [occpic_supplierpolicy.md](./occpic_supplierpolicy.md) |
| 40 | `t_occpic_starget` | 采购政策目标-主表 | 33 | [occpic_suppliertarget.md](./occpic_suppliertarget.md) |
| 41 | `t_occpic_starget_ife` | 返利标准-子表 | 19 | [occpic_suppliertarget.md](./occpic_suppliertarget.md) |
| 42 | `t_occpic_starget_lk` | 关联子实体-子表 | 6 | [occpic_suppliertarget.md](./occpic_suppliertarget.md) |
| 43 | `t_occpic_starget_tc` | 采购政策目标-关联追踪表 | 7 | [occpic_suppliertarget.md](./occpic_suppliertarget.md) |
| 44 | `t_occpic_starget_wb` | 采购政策目标-反写记录表 | 10 | [occpic_suppliertarget.md](./occpic_suppliertarget.md) |
| 45 | `t_occpic_supbgt` | 采购返利结算单-主表 | 34 | [occpic_supbgt.md](./occpic_supbgt.md) |
| 46 | `t_occpic_supbgt_lk` | 关联子实体-子表 | 10 | [occpic_supbgt.md](./occpic_supbgt.md) |
| 47 | `t_occpic_supbgt_tc` | 采购返利结算单-关联追踪表 | 7 | [occpic_supbgt.md](./occpic_supbgt.md) |
| 48 | `t_occpic_supbgtentry` | 结算明细-子表 | 38 | [occpic_supbgt.md](./occpic_supbgt.md) |
| 49 | `t_occpic_supbgtentry_lk` | 关联子实体-子表 | 24 | [occpic_supbgt.md](./occpic_supbgt.md) |
| 50 | `t_occpic_supbgtentry_wb` | 采购返利结算单-反写记录表 | 10 | [occpic_supbgt.md](./occpic_supbgt.md) |
| 51 | `t_occpic_supprebgt` | 采购返利预结算单-主表 | 36 | [occpic_supprebgt.md](./occpic_supprebgt.md) |
| 52 | `t_occpic_supprebgt_tc` | 采购返利预结算单-关联追踪表 | 7 | [occpic_supprebgt.md](./occpic_supprebgt.md) |
| 53 | `t_occpic_supprebgt_wb` | 采购返利预结算单-反写记录表 | 10 | [occpic_supprebgt.md](./occpic_supprebgt.md) |
| 54 | `t_occpic_supprebgtentry` | 预结算明细-子表 | 46 | [occpic_supprebgt.md](./occpic_supprebgt.md) |
| 55 | `t_occpic_supprebgtentry_lk` | 关联子实体-子表 | 8 | [occpic_supprebgt.md](./occpic_supprebgt.md) |
| 56 | `t_ocdbd_billoperatelog` | 单据操作日志-主表 | 6 | [ocdbd_billoperatelog.md](./ocdbd_billoperatelog.md) |
| 57 | `t_ocdbd_bizdatatype` | 业务数据类型-主表 | 14 | [ocdbd_bizdatatype.md](./ocdbd_bizdatatype.md) |
| 58 | `t_ocdbd_bizdatatype_l` | 业务数据类型-多语言表 | 4 | [ocdbd_bizdatatype.md](./ocdbd_bizdatatype.md) |
| 59 | `t_ocdbd_conditongroup` | 条件组-主表 | 14 | [ocdbd_conditongroup.md](./ocdbd_conditongroup.md) |
| 60 | `t_ocdbd_conditongroup_l` | 条件组-多语言表 | 4 | [ocdbd_conditongroup.md](./ocdbd_conditongroup.md) |
| 61 | `t_ocdbd_conditongroupe` | 条件明细-子表 | 9 | [ocdbd_conditongroup.md](./ocdbd_conditongroup.md) |
| 62 | `t_ocdbd_datafetchrule` | 取数规则-主表 | 19 | [ocdbd_datafetchrule.md](./ocdbd_datafetchrule.md) |
| 63 | `t_ocdbd_datafetchrule_l` | 取数规则-多语言表 | 4 | [ocdbd_datafetchrule.md](./ocdbd_datafetchrule.md) |
| 64 | `t_ocdbd_excutefetchrule` | 取数规则执行情况表-主表 | 3 | [ocdbd_excutefetchrule.md](./ocdbd_excutefetchrule.md) |
| 65 | `t_ocdbd_kpi` | 政策类型-主表 | 19 | [ocdbd_kpi.md](./ocdbd_kpi.md) |
| 66 | `t_ocdbd_kpi_l` | 政策类型-多语言表 | 4 | [ocdbd_kpi.md](./ocdbd_kpi.md) |
| 67 | `t_ocdbd_rule_colmap` | 字段映射-子表 | 9 | [ocdbd_datafetchrule.md](./ocdbd_datafetchrule.md) |
| 68 | `t_ocdbd_rule_colmap_f` | 字段映射-分表 | 6 | [ocdbd_datafetchrule.md](./ocdbd_datafetchrule.md) |
