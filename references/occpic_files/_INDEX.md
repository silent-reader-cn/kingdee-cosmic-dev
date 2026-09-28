# occpic 模块表清单

> 本模块共收录 **39** 张表定义，来自 `occpic_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope occpic
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_occpic_rbtgt_form_dt` | 返利标准-子表 | 12 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 2 | `t_occpic_rbtgt_itemclass` | 返利商品-子表 | 7 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 3 | `t_occpic_rbtgt_itemfomul` | 分组返利标准-子表 | 16 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 4 | `t_occpic_rebatebasetab` | 返利数据底表-主表 | 36 | [occpibc_rebatebasetab.md](./occpibc_rebatebasetab.md) |
| 5 | `t_occpic_rebatepbdgentry` | 返利预结算明细-子表 | 47 | [occpic_rebateprebudget.md](./occpic_rebateprebudget.md) |
| 6 | `t_occpic_rebatepolicy` | 返利政策-主表 | 29 | [occpic_rebatepolicy.md](./occpic_rebatepolicy.md) |
| 7 | `t_occpic_rebatepolicy` | 返利政策F7-主表 | 29 | [ocdbd_rebatepolicyf7.md](./ocdbd_rebatepolicyf7.md) |
| 8 | `t_occpic_rebateprbd_sa` | 商品销售属性-多选基础资料表 | 3 | [occpic_rebateprebudget.md](./occpic_rebateprebudget.md) |
| 9 | `t_occpic_rebateprebudget` | 返利预结算单-主表 | 54 | [occpic_rebateprebudget.md](./occpic_rebateprebudget.md) |
| 10 | `t_occpic_rebatestatement` | 返利结算单-主表 | 44 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 11 | `t_occpic_rebatestatement` | 返利结算单F7-主表 | 44 | [occpic_rebatestatementf7.md](./occpic_rebatestatementf7.md) |
| 12 | `t_occpic_rebatestatement_lk` | 关联子实体-子表 | 6 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 13 | `t_occpic_rebatestatement_tc` | 返利结算单-关联追踪表 | 7 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 14 | `t_occpic_rebatestatement_wb` | 返利结算单-反写记录表 | 10 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 15 | `t_occpic_rebatestm_sa` | 商品销售属性-多选基础资料表 | 3 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 16 | `t_occpic_rebatestmentry` | 返利结算明细-子表 | 46 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 17 | `t_occpic_rebatestmentry_lk` | 关联子实体-子表 | 6 | [occpic_rebatestatement.md](./occpic_rebatestatement.md) |
| 18 | `t_occpic_rebatetarget` | 政策目标-主表 | 36 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 19 | `t_occpic_rebatetarget` | 政策目标F7-主表 | 36 | [ocdbd_rebatetargetf7.md](./ocdbd_rebatetargetf7.md) |
| 20 | `t_occpic_rebatetarget_lk` | 关联子实体-子表 | 6 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 21 | `t_occpic_rebatetarget_tc` | 政策目标-关联追踪表 | 7 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 22 | `t_occpic_rebatetarget_wb` | 政策目标-反写记录表 | 10 | [occpic_rebatetarget.md](./occpic_rebatetarget.md) |
| 23 | `t_occpic_rp_bnfcust` | 返利对象-子表 | 9 | [occpic_rebatepolicy.md](./occpic_rebatepolicy.md) |
| 24 | `t_occpic_rp_formula` | 返利标准-子表 | 12 | [occpic_rebatepolicy.md](./occpic_rebatepolicy.md) |
| 25 | `t_occpic_rp_itemclass` | 返利商品-子表 | 7 | [occpic_rebatepolicy.md](./occpic_rebatepolicy.md) |
| 26 | `t_occpic_rp_itemfomul` | 分组返利标准-子表 | 16 | [occpic_rebatepolicy.md](./occpic_rebatepolicy.md) |
| 27 | `t_ocdbd_billoperatelog` | 单据操作日志-主表 | 6 | [ocdbd_billoperatelog.md](./ocdbd_billoperatelog.md) |
| 28 | `t_ocdbd_bizdatatype` | 业务数据类型-主表 | 14 | [ocdbd_bizdatatype.md](./ocdbd_bizdatatype.md) |
| 29 | `t_ocdbd_bizdatatype_l` | 业务数据类型-多语言表 | 4 | [ocdbd_bizdatatype.md](./ocdbd_bizdatatype.md) |
| 30 | `t_ocdbd_conditongroup` | 条件组-主表 | 14 | [ocdbd_conditongroup.md](./ocdbd_conditongroup.md) |
| 31 | `t_ocdbd_conditongroup_l` | 条件组-多语言表 | 4 | [ocdbd_conditongroup.md](./ocdbd_conditongroup.md) |
| 32 | `t_ocdbd_conditongroupe` | 条件明细-子表 | 9 | [ocdbd_conditongroup.md](./ocdbd_conditongroup.md) |
| 33 | `t_ocdbd_datafetchrule` | 取数规则-主表 | 19 | [ocdbd_datafetchrule.md](./ocdbd_datafetchrule.md) |
| 34 | `t_ocdbd_datafetchrule_l` | 取数规则-多语言表 | 4 | [ocdbd_datafetchrule.md](./ocdbd_datafetchrule.md) |
| 35 | `t_ocdbd_excutefetchrule` | 取数规则执行情况表-主表 | 3 | [ocdbd_excutefetchrule.md](./ocdbd_excutefetchrule.md) |
| 36 | `t_ocdbd_kpi` | 政策类型-主表 | 17 | [ocdbd_kpi.md](./ocdbd_kpi.md) |
| 37 | `t_ocdbd_kpi_l` | 政策类型-多语言表 | 4 | [ocdbd_kpi.md](./ocdbd_kpi.md) |
| 38 | `t_ocdbd_rule_colmap` | 字段映射-子表 | 9 | [ocdbd_datafetchrule.md](./ocdbd_datafetchrule.md) |
| 39 | `t_ocdbd_rule_colmap_f` | 字段映射-分表 | 6 | [ocdbd_datafetchrule.md](./ocdbd_datafetchrule.md) |
