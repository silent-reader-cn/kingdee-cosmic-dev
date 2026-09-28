# ipocommon 模块表清单

> 本模块共收录 **55** 张表定义，来自 `ipocommon_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope ipocommon
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fid_balancesheet` | 资产负债表-主表 | 0 | [fid_balancesheet.md](./fid_balancesheet.md) |
| 2 | `t_fid_bs_goodwill` | 商誉-主表 | 0 | [fid_bs_goodwill.md](./fid_bs_goodwill.md) |
| 3 | `t_fid_bs_inv` | 存货明细-主表 | 0 | [fid_bs_inv.md](./fid_bs_inv.md) |
| 4 | `t_fid_bs_payrollpay` | 应付职工薪酬-主表 | 0 | [fid_bs_payrollpay.md](./fid_bs_payrollpay.md) |
| 5 | `t_fid_bs_taxpayable` | 应交税费-主表 | 0 | [fid_bs_taxpayable.md](./fid_bs_taxpayable.md) |
| 6 | `t_fid_cashflowsext` | 现金流量表附注-主表 | 0 | [fid_cashflowsext.md](./fid_cashflowsext.md) |
| 7 | `t_fid_cashflowssheet` | 现金流量表-主表 | 0 | [fid_cashflowssheet.md](./fid_cashflowssheet.md) |
| 8 | `t_fid_com_capital_analy` | 资本结构分析-主表 | 0 | [com_capitalstruct_analys.md](./com_capitalstruct_analys.md) |
| 9 | `t_fid_com_cashflow_analy` | 现金流量分析-主表 | 0 | [com_cashflows_analysis.md](./com_cashflows_analysis.md) |
| 10 | `t_fid_com_growthab_analy` | 成长能力分析-主表 | 0 | [com_growthabi_analysis.md](./com_growthabi_analysis.md) |
| 11 | `t_fid_com_indexps_analy` | 每股指标分析-主表 | 0 | [com_indexpersh_analysis.md](./com_indexpersh_analysis.md) |
| 12 | `t_fid_com_ope_capa_analy` | 营运能力分析-主表 | 0 | [com_ope_capacity_analysis.md](./com_ope_capacity_analysis.md) |
| 13 | `t_fid_com_percapin_analy` | 人均指标分析-主表 | 0 | [com_percapindi_analysis.md](./com_percapindi_analysis.md) |
| 14 | `t_fid_com_profiqua_analy` | 盈利质量分析-主表 | 0 | [company_profitqu_analysis.md](./company_profitqu_analysis.md) |
| 15 | `t_fid_com_profitab_analy` | 盈利能力分析-主表 | 0 | [company_profitab_analysis.md](./company_profitab_analysis.md) |
| 16 | `t_fid_com_solvency_analy` | 债偿能力分析-主表 | 0 | [com_solvency_analysis.md](./com_solvency_analysis.md) |
| 17 | `t_fid_crar_aging` | 债权-应收账款账龄结构-主表 | 0 | [fid_crar_aging.md](./fid_crar_aging.md) |
| 18 | `t_fid_crar_othersaging` | 债权-其他应收款账龄结构-主表 | 0 | [fid_crar_othersaging.md](./fid_crar_othersaging.md) |
| 19 | `t_fid_crar_othersunit` | 债权-其他应收款主要单位-主表 | 0 | [fid_crar_othersunit.md](./fid_crar_othersunit.md) |
| 20 | `t_fid_crar_topcustomer` | 债权-前五大客户应收-主表 | 0 | [fid_crar_topcustomer.md](./fid_crar_topcustomer.md) |
| 21 | `t_fid_dbtap_aging` | 债务-应付账款账龄结构-主表 | 0 | [fid_dbtap_aging.md](./fid_dbtap_aging.md) |
| 22 | `t_fid_dbtap_othersaging` | 债务-其他应付款账龄结构-主表 | 0 | [fid_dbtap_othersaging.md](./fid_dbtap_othersaging.md) |
| 23 | `t_fid_dbtap_unit` | 债务-主要应付单位-主表 | 0 | [fid_dbtap_unit.md](./fid_dbtap_unit.md) |
| 24 | `t_fid_dbtprer_aging` | 债务-预收账款账龄结构-主表 | 0 | [fid_dbtprer_aging.md](./fid_dbtprer_aging.md) |
| 25 | `t_fid_executive_compensat` | 行业高管薪酬-主表 | 0 | [executive_compensation.md](./executive_compensation.md) |
| 26 | `t_fid_growth_ability_anal` | 成长能力分析-主表 | 0 | [growth_ability_analysis.md](./growth_ability_analysis.md) |
| 27 | `t_fid_incomestatement` | 利润表-主表 | 0 | [fid_incomestatement.md](./fid_incomestatement.md) |
| 28 | `t_fid_mainothers` | 其他业务收入成本-主表 | 0 | [fid_mainothers.md](./fid_mainothers.md) |
| 29 | `t_fid_mainstrarea` | 主营构成(地区)-主表 | 0 | [fid_mainstrarea.md](./fid_mainstrarea.md) |
| 30 | `t_fid_mainstrindustry` | 主营构成(行业)-主表 | 0 | [fid_mainstrindustry.md](./fid_mainstrindustry.md) |
| 31 | `t_fid_mainstrproduct` | 主营构成(产品)-主表 | 0 | [fid_mainstrproduct.md](./fid_mainstrproduct.md) |
| 32 | `t_fid_maintopcustomer` | 前五大客户营业收入比例-主表 | 0 | [fid_maintopcustomer.md](./fid_maintopcustomer.md) |
| 33 | `t_fid_maintopsupplier` | 前五大客户采购比例-主表 | 0 | [fid_maintopsupplier.md](./fid_maintopsupplier.md) |
| 34 | `t_fid_ope_capacity_analys` | 营运能力分析-主表 | 0 | [ope_capacity_analysis.md](./ope_capacity_analysis.md) |
| 35 | `t_fid_patent_stats` | 公司专利统计-主表 | 0 | [fid_patent_stats.md](./fid_patent_stats.md) |
| 36 | `t_fid_pepl_extraite` | 非经常性损益-主表 | 0 | [fid_pepl_extraite.md](./fid_pepl_extraite.md) |
| 37 | `t_fid_pepl_fi` | 财务费用-主表 | 0 | [fid_pepl_fi.md](./fid_pepl_fi.md) |
| 38 | `t_fid_pepl_manage` | 管理费用-主表 | 0 | [fid_pepl_manage.md](./fid_pepl_manage.md) |
| 39 | `t_fid_pepl_outincome` | 营业外收入明细-主表 | 0 | [fid_pepl_outincome.md](./fid_pepl_outincome.md) |
| 40 | `t_fid_pepl_outpay` | 营业外支出明细-主表 | 0 | [fid_pepl_outpay.md](./fid_pepl_outpay.md) |
| 41 | `t_fid_pepl_rd` | 研发费用-主表 | 0 | [fid_pepl_rd.md](./fid_pepl_rd.md) |
| 42 | `t_fid_pepl_rdpay` | 研发支出（研发投入）-主表 | 0 | [fid_pepl_rdpay.md](./fid_pepl_rdpay.md) |
| 43 | `t_fid_pepl_roi` | 投资收益明细-主表 | 0 | [fid_pepl_roi.md](./fid_pepl_roi.md) |
| 44 | `t_fid_pepl_sell` | 销售费用-主表 | 0 | [fid_pepl_sell.md](./fid_pepl_sell.md) |
| 45 | `t_fid_pepl_taxext` | 营业税金及附加-主表 | 0 | [fid_pepl_taxext.md](./fid_pepl_taxext.md) |
| 46 | `t_fid_profitability_analy` | 盈利能力分析-主表 | 0 | [profitability_analysis.md](./profitability_analysis.md) |
| 47 | `t_fid_ps_bydiploma` | 按学历-主表 | 0 | [fid_ps_bydiploma.md](./fid_ps_bydiploma.md) |
| 48 | `t_fid_ps_byjd` | 按岗位-主表 | 0 | [fid_ps_byjd.md](./fid_ps_byjd.md) |
| 49 | `t_fid_replace_table` | 财报DB替换表-主表 | 0 | [fid_replace_table.md](./fid_replace_table.md) |
| 50 | `t_fid_solvency_analysis` | 偿债能力分析_复制-主表 | 0 | [solvency_analysis_on_copy.md](./solvency_analysis_on_copy.md) |
| 51 | `t_fid_solvency_analysis` | 偿债能力分析-主表 | 0 | [solvency_analysis_one.md](./solvency_analysis_one.md) |
| 52 | `t_market_company_info` | 上市公司信息-主表 | 0 | [market_company_info.md](./market_company_info.md) |
| 53 | `t_market_company_info_l` | 上市公司信息-多语言表 | 0 | [market_company_info.md](./market_company_info.md) |
| 54 | `t_market_company_type` | 上市公司分类-主表 | 0 | [market_company_type.md](./market_company_type.md) |
| 55 | `t_market_company_type_l` | 上市公司分类-多语言表 | 0 | [market_company_type.md](./market_company_type.md) |
