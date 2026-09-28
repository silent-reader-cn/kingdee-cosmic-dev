# iba 模块表清单

> 本模块共收录 **38** 张表定义，来自 `iba_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category iba
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_customer_data_detail` | 结构明细-子表 | 7 | [iba_top5_customer_data.md](./iba_top5_customer_data.md) |
| 2 | `t_distribution_detail` | 分层方案-子表 | 6 | [distribution_plan.md](./distribution_plan.md) |
| 3 | `t_distribution_plan` | 营收分层方案-主表 | 11 | [distribution_plan.md](./distribution_plan.md) |
| 4 | `t_distribution_plan_l` | 营收分层方案-多语言表 | 4 | [distribution_plan.md](./distribution_plan.md) |
| 5 | `t_financiexpense_detail` | 单据体-子表 | 5 | [iba_financiexpense.md](./iba_financiexpense.md) |
| 6 | `t_iba_evaluate_core_rule` | 评分规则-子表 | 6 | [iba_evaluate_quota.md](./iba_evaluate_quota.md) |
| 7 | `t_iba_evaluate_quota` | 财务评价模型指标-主表 | 8 | [iba_evaluate_quota.md](./iba_evaluate_quota.md) |
| 8 | `t_iba_evaluate_type` | 财务评价模型类型-主表 | 12 | [iba_evaluate_type.md](./iba_evaluate_type.md) |
| 9 | `t_iba_evaluate_type_l` | 财务评价模型类型-多语言表 | 4 | [iba_evaluate_type.md](./iba_evaluate_type.md) |
| 10 | `t_iba_evaluate_type_orgs` | 适用组织-多选基础资料表 | 3 | [iba_evaluate_type.md](./iba_evaluate_type.md) |
| 11 | `t_iba_evaluate_weigh_cap` | 能力项权重信息-子表 | 5 | [iba_evaluate_type.md](./iba_evaluate_type.md) |
| 12 | `t_iba_financiexpense` | 财务费用明细表-主表 | 14 | [iba_financiexpense.md](./iba_financiexpense.md) |
| 13 | `t_iba_mbusiness_structure` | 主营结构表-主表 | 14 | [main_business_structure.md](./main_business_structure.md) |
| 14 | `t_iba_nrincome_stat` | 非经常性损益表-主表 | 14 | [iba_nrincome_stat.md](./iba_nrincome_stat.md) |
| 15 | `t_iba_nrincomes_detail` | 单据体-子表 | 5 | [iba_nrincome_stat.md](./iba_nrincome_stat.md) |
| 16 | `t_iba_overhead` | 管理费用明细表-主表 | 14 | [iba_overhead.md](./iba_overhead.md) |
| 17 | `t_iba_parameter` | 参数设置数据-主表 | 7 | [iba_parameter.md](./iba_parameter.md) |
| 18 | `t_iba_patent_count` | 专利数量表-主表 | 14 | [iba_patent_count.md](./iba_patent_count.md) |
| 19 | `t_iba_payrollpay` | 应付职工薪酬表-主表 | 14 | [iba_payrollpay.md](./iba_payrollpay.md) |
| 20 | `t_iba_pcount_detail` | 单据体-子表 | 5 | [iba_patent_count.md](./iba_patent_count.md) |
| 21 | `t_iba_rdexpense` | 研发费用明细表-主表 | 14 | [iba_rdexpense.md](./iba_rdexpense.md) |
| 22 | `t_iba_report_compare_c` | 对标公司-多选基础资料表 | 3 | [iba_report_record.md](./iba_report_record.md) |
| 23 | `t_iba_report_record` | 对标报告记录-主表 | 15 | [iba_report_record.md](./iba_report_record.md) |
| 24 | `t_iba_report_record_file` | 附件-附件表 | 3 | [iba_report_record.md](./iba_report_record.md) |
| 25 | `t_iba_report_scheme` | 行业方案设置-主表 | 31 | [iba_org_report_scheme.md](./iba_org_report_scheme.md) |
| 26 | `t_iba_report_scheme_l` | 行业方案设置-多语言表 | 4 | [iba_org_report_scheme.md](./iba_org_report_scheme.md) |
| 27 | `t_iba_searchplan` | 查询方案-主表 | 5 | [iba_search_plan.md](./iba_search_plan.md) |
| 28 | `t_iba_sellingexpense` | 销售费用明细表-主表 | 14 | [iba_sellingexpense.md](./iba_sellingexpense.md) |
| 29 | `t_iba_staff_build` | 人员结构表-主表 | 14 | [iba_staff_build.md](./iba_staff_build.md) |
| 30 | `t_iba_staff_build_detail` | 单据体-子表 | 5 | [iba_staff_build.md](./iba_staff_build.md) |
| 31 | `t_iba_structure_detail` | 结构明细-子表 | 13 | [main_business_structure.md](./main_business_structure.md) |
| 32 | `t_iba_top5_customer_data` | 收入前五客户表-主表 | 15 | [iba_top5_customer_data.md](./iba_top5_customer_data.md) |
| 33 | `t_iba_top5_supplier_data` | 采购前五供应商表-主表 | 15 | [iba_top5_supplier_data.md](./iba_top5_supplier_data.md) |
| 34 | `t_overhead_detail` | 单据体-子表 | 5 | [iba_overhead.md](./iba_overhead.md) |
| 35 | `t_payrollpay_detail` | 单据体-子表 | 9 | [iba_payrollpay.md](./iba_payrollpay.md) |
| 36 | `t_rdexpense_detail` | 单据体-子表 | 5 | [iba_rdexpense.md](./iba_rdexpense.md) |
| 37 | `t_sellingexpense_detail` | 单据体-子表 | 5 | [iba_sellingexpense.md](./iba_sellingexpense.md) |
| 38 | `t_supplier_data_detail` | 结构明细-子表 | 7 | [iba_top5_supplier_data.md](./iba_top5_supplier_data.md) |
