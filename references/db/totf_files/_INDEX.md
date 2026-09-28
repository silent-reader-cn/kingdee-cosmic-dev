# totf 模块表清单

> 本模块共收录 **54** 张表定义，来自 `totf_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category totf
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_tctb_declare_entry` | 单据体-子表 | 14 | [totf_whsyjs_declare_query.md](./totf_whsyjs_declare_query.md) |
| 2 | `t_tctb_declare_main` | 其他税费查询-主表 | 66 | [totf_nssb_query.md](./totf_nssb_query.md) |
| 3 | `t_tctb_declare_main` | 通用申报查询-主表 | 66 | [totf_tysb_declare_main.md](./totf_tysb_declare_main.md) |
| 4 | `t_tctb_declare_main` | 文化事业建设费查询-主表 | 66 | [totf_whsyjs_declare_query.md](./totf_whsyjs_declare_query.md) |
| 5 | `t_totf_accdetail_adjust` | 取数明细调整表-主表 | 13 | [totf_accountdetail_adjust.md](./totf_accountdetail_adjust.md) |
| 6 | `t_totf_embankment_account` | 堤围防护费台账-主表 | 31 | [totf_embankment_account.md](./totf_embankment_account.md) |
| 7 | `t_totf_employment_fund` | 残疾人就业保障金台账-主表 | 28 | [totf_employment_fund.md](./totf_employment_fund.md) |
| 8 | `t_totf_jsxzsyxsf_account` | 建设行政事业性收费收入台账-主表 | 33 | [totf_jsxzsyxsf_account.md](./totf_jsxzsyxsf_account.md) |
| 9 | `t_totf_jybz_declare` | 残疾人就业保障金申报子表-主表 | 8 | [totf_jybz_declare_entry.md](./totf_jybz_declare_entry.md) |
| 10 | `t_totf_jybz_declare` | 单据体-子表 | 8 | [totf_jybz_declare_query.md](./totf_jybz_declare_query.md) |
| 11 | `t_totf_otherincome` | 其他收入台账-主表 | 31 | [totf_otherincome_account.md](./totf_otherincome_account.md) |
| 12 | `t_totf_rule_wafund_entity` | 取数规则-子表 | 14 | [totf_rule_waterfund.md](./totf_rule_waterfund.md) |
| 13 | `t_totf_rule_waterfund` | 水利基金不含税收入规则-主表 | 13 | [totf_rule_waterfund.md](./totf_rule_waterfund.md) |
| 14 | `t_totf_rule_waterfund_l` | 水利基金不含税收入规则-多语言表 | 4 | [totf_rule_waterfund.md](./totf_rule_waterfund.md) |
| 15 | `t_totf_rule_whsy_entity` | 取数规则-子表 | 14 | [totf_rule_whsyjsf.md](./totf_rule_whsyjsf.md) |
| 16 | `t_totf_rule_whsyjsf` | 文化事业建设费应征收入规则-主表 | 13 | [totf_rule_whsyjsf.md](./totf_rule_whsyjsf.md) |
| 17 | `t_totf_rule_whsyjsf_l` | 文化事业建设费应征收入规则-多语言表 | 4 | [totf_rule_whsyjsf.md](./totf_rule_whsyjsf.md) |
| 18 | `t_totf_sharingplan` | 共享方案-子表 | 14 | [totf_edit_sharingplan.md](./totf_edit_sharingplan.md) |
| 19 | `t_totf_sharingplan` | 共享方案-主表 | 14 | [totf_sharingplan.md](./totf_sharingplan.md) |
| 20 | `t_totf_sharingplan_edit` | 其他税费共享方案-主表 | 5 | [totf_edit_sharingplan.md](./totf_edit_sharingplan.md) |
| 21 | `t_totf_sharingplan_l` | 共享方案-多语言表 | 4 | [totf_edit_sharingplan.md](./totf_edit_sharingplan.md) |
| 22 | `t_totf_sharingplan_l` | 共享方案-多语言表 | 4 | [totf_sharingplan.md](./totf_sharingplan.md) |
| 23 | `t_totf_sharingplan_orgs` | 被共享组织-子表 | 4 | [totf_edit_sharingplan.md](./totf_edit_sharingplan.md) |
| 24 | `t_totf_sharingplan_orgs` | 单据体-子表 | 4 | [totf_sharingplan.md](./totf_sharingplan.md) |
| 25 | `t_totf_sharingplan_rules` | 规则-子表 | 5 | [totf_edit_sharingplan.md](./totf_edit_sharingplan.md) |
| 26 | `t_totf_sharingplan_rules` | 单据体-子表 | 5 | [totf_sharingplan.md](./totf_sharingplan.md) |
| 27 | `t_totf_sjfzsf_dtb` | 通用申报表动态行表-主表 | 32 | [totf_sjfzsf_dtb.md](./totf_sjfzsf_dtb.md) |
| 28 | `t_totf_sjfzsf_dtb` | 单据体-子表 | 32 | [totf_tysb_declare_main.md](./totf_tysb_declare_main.md) |
| 29 | `t_totf_sjfzsf_info` | 通用申报表信息表-主表 | 14 | [totf_sjfzsf_info.md](./totf_sjfzsf_info.md) |
| 30 | `t_totf_taxable_deductitem` | 应税服务减除项目清单台账-主表 | 21 | [totf_taxable_deduct_item.md](./totf_taxable_deduct_item.md) |
| 31 | `t_totf_tcept_airrpt` | 按月计算报表（大气污染物适用）-主表 | 18 | [totf_tcept_airrpt.md](./totf_tcept_airrpt.md) |
| 32 | `t_totf_tcept_declare_alzb` | 环保税纳税申报表A类主表-主表 | 14 | [totf_tcept_declare_alzb.md](./totf_tcept_declare_alzb.md) |
| 33 | `t_totf_tcept_noiserpt` | 按月计算报表（噪声适用）-主表 | 17 | [totf_tcept_noiserpt.md](./totf_tcept_noiserpt.md) |
| 34 | `t_totf_tcept_solidrpt` | 按月计算报表（固体废物适用）-主表 | 11 | [totf_tcept_solidrpt.md](./totf_tcept_solidrpt.md) |
| 35 | `t_totf_tcept_taxreducedtl` | 环保税减免税明细表-主表 | 19 | [totf_tcept_taxreducedtl.md](./totf_tcept_taxreducedtl.md) |
| 36 | `t_totf_tcept_waterrpt` | 按月计算报表（水污染物适用）-主表 | 19 | [totf_tcept_waterrpt.md](./totf_tcept_waterrpt.md) |
| 37 | `t_totf_tcvvt_declare` | 车船税纳税申报表-主表 | 22 | [totf_tcvvt_declare.md](./totf_tcvvt_declare.md) |
| 38 | `t_totf_tcvvt_dsdjrpt` | 车船税代收代缴报告表-主表 | 47 | [totf_tcvvt_dsdjrpt.md](./totf_tcvvt_dsdjrpt.md) |
| 39 | `t_totf_tcvvt_shipsdetail` | 车船税税源明细表（船舶）-主表 | 18 | [totf_tcvvt_shipsdetail.md](./totf_tcvvt_shipsdetail.md) |
| 40 | `t_totf_tcvvt_vehiclesdtl` | 车船税税源明细表（车辆）-主表 | 16 | [totf_tcvvt_vehiclesdtl.md](./totf_tcvvt_vehiclesdtl.md) |
| 41 | `t_totf_wafund_accunt_deta` | 水利基金预缴底稿取数明细-主表 | 11 | [totf_wafund_accunt_detail.md](./totf_wafund_accunt_detail.md) |
| 42 | `t_totf_water_fund` | 水利建设基金台账-主表 | 25 | [totf_water_fund.md](./totf_water_fund.md) |
| 43 | `t_totf_waterfund_detail` | 水利建设基金台账自动取数明细-主表 | 19 | [totf_waterfund_detail.md](./totf_waterfund_detail.md) |
| 44 | `t_totf_whsydetail_adjust` | 文化事业建设费取数明细调整-主表 | 12 | [totf_whsydetail_adjust.md](./totf_whsydetail_adjust.md) |
| 45 | `t_totf_whsyjsf_account` | 文化事业建设费台账-主表 | 22 | [totf_whsyjsf_account.md](./totf_whsyjsf_account.md) |
| 46 | `t_totf_whsyjsf_detail` | 文化事业建设费自动取数明细-主表 | 18 | [totf_whsyjsf_detail.md](./totf_whsyjsf_detail.md) |
| 47 | `t_totf_whsyjsf_ysfwjcxmqd` | 应税服务减除项目清单-主表 | 10 | [totf_whsyjsf_ysfwjcxmqd.md](./totf_whsyjsf_ysfwjcxmqd.md) |
| 48 | `t_totf_whsyjsf_zb` | 文化事业建设费主表-主表 | 23 | [totf_whsyjsf_zb.md](./totf_whsyjsf_zb.md) |
| 49 | `t_totf_yys_declare` | 烟叶税纳税申报表-主表 | 9 | [totf_yys_declare.md](./totf_yys_declare.md) |
| 50 | `t_totf_zys_declare` | 资源税纳税申报表-主表 | 15 | [totf_zys_declare.md](./totf_zys_declare.md) |
| 51 | `t_totf_zys_declaredetail` | 资源税申报计算明细表-主表 | 14 | [totf_zys_declaredetail.md](./totf_zys_declaredetail.md) |
| 52 | `t_totf_zys_jzzc` | 资源税减征政策-主表 | 6 | [totf_zys_jzzc.md](./totf_zys_jzzc.md) |
| 53 | `t_totf_zys_taxreducedtl` | 资源税减免税计算明细表-主表 | 14 | [totf_zys_taxreducedtl.md](./totf_zys_taxreducedtl.md) |
| 54 | `t_tpo_declare_main_tsc` | 残疾人就业保障金缴费申报查询-主表 | 62 | [totf_jybz_declare_query.md](./totf_jybz_declare_query.md) |
