# ipobase 模块表清单

> 本模块共收录 **53** 张表定义，来自 `ipobase_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ipobase
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_base_rptitemdatatype` | IPO项目数据类型-主表 | 0 | [ipo_rptitemdatatype.md](./ipo_rptitemdatatype.md) |
| 2 | `t_base_rptitemdatatype_l` | IPO项目数据类型-多语言表 | 0 | [ipo_rptitemdatatype.md](./ipo_rptitemdatatype.md) |
| 3 | `t_business_asstacttype` | 企业版核算维度-主表 | 10 | [business_asstacttype.md](./business_asstacttype.md) |
| 4 | `t_business_asstacttype_l` | 企业版核算维度-多语言表 | 4 | [business_asstacttype.md](./business_asstacttype.md) |
| 5 | `t_cfa_three_fin_report` | 财务报表项目数据-主表 | 13 | [fin_report_item_data.md](./fin_report_item_data.md) |
| 6 | `t_csrc_industry_info` | 证监会行业-主表 | 17 | [csrc_industry_info.md](./csrc_industry_info.md) |
| 7 | `t_csrc_industry_info_l` | 证监会行业-多语言表 | 4 | [csrc_industry_info.md](./csrc_industry_info.md) |
| 8 | `t_csrc_industry_type` | 证监会行业分类-主表 | 15 | [csrc_industry_type.md](./csrc_industry_type.md) |
| 9 | `t_csrc_industry_type_l` | 证监会行业分类-多语言表 | 6 | [csrc_industry_type.md](./csrc_industry_type.md) |
| 10 | `t_fin_report` | 财务报表-主表 | 16 | [ipo_fin_report.md](./ipo_fin_report.md) |
| 11 | `t_fin_report_item` | 财务报表项目-主表 | 20 | [ipo_fin_report_item.md](./ipo_fin_report_item.md) |
| 12 | `t_fin_report_item_l` | 财务报表项目-多语言表 | 5 | [ipo_fin_report_item.md](./ipo_fin_report_item.md) |
| 13 | `t_fin_report_type` | IPO财务报表类型-主表 | 10 | [ipo_fin_report_type.md](./ipo_fin_report_type.md) |
| 14 | `t_fin_report_type_l` | IPO财务报表类型-多语言表 | 4 | [ipo_fin_report_type.md](./ipo_fin_report_type.md) |
| 15 | `t_ipo_anal_datasourse` | IPO主题分析表取数来源单据-主表 | 5 | [ipo_anal_datasourse.md](./ipo_anal_datasourse.md) |
| 16 | `t_ipo_base_quota` | 多指标组合判断-多选基础资料表 | 3 | [ipo_quota_info.md](./ipo_quota_info.md) |
| 17 | `t_ipo_business_account` | 企业版科目-主表 | 10 | [business_account.md](./business_account.md) |
| 18 | `t_ipo_business_account_l` | 企业版科目-多语言表 | 4 | [business_account.md](./business_account.md) |
| 19 | `t_ipo_business_item` | 企业版项目-主表 | 12 | [ipo_business_item.md](./ipo_business_item.md) |
| 20 | `t_ipo_business_item_l` | 企业版项目-多语言表 | 4 | [ipo_business_item.md](./ipo_business_item.md) |
| 21 | `t_ipo_dupont_quota` | 上级指标(归因)-多选基础资料表 | 3 | [ipo_quota_info.md](./ipo_quota_info.md) |
| 22 | `t_ipo_lconditions_data` | IPO上市条件标准值与默认值-主表 | 17 | [ipo_list_conditions_data.md](./ipo_list_conditions_data.md) |
| 23 | `t_ipo_lconditions_data_l` | IPO上市条件标准值与默认值-多语言表 | 4 | [ipo_list_conditions_data.md](./ipo_list_conditions_data.md) |
| 24 | `t_ipo_lconditions_type` | 上市条件类型-主表 | 25 | [ipo_list_conditions_type.md](./ipo_list_conditions_type.md) |
| 25 | `t_ipo_lconditions_type_l` | 上市条件类型-多语言表 | 5 | [ipo_list_conditions_type.md](./ipo_list_conditions_type.md) |
| 26 | `t_ipo_listed_company` | 上市公司-主表 | 11 | [ipo_listed_company.md](./ipo_listed_company.md) |
| 27 | `t_ipo_listed_company_l` | 上市公司-多语言表 | 4 | [ipo_listed_company.md](./ipo_listed_company.md) |
| 28 | `t_ipo_quota_info` | 指标库-主表 | 53 | [ipo_quota_info.md](./ipo_quota_info.md) |
| 29 | `t_ipo_quota_info_l` | 指标库-多语言表 | 4 | [ipo_quota_info.md](./ipo_quota_info.md) |
| 30 | `t_ipo_quota_type` | 指标分类目录-主表 | 20 | [ipo_quota_type.md](./ipo_quota_type.md) |
| 31 | `t_ipo_quota_type_l` | 指标分类目录-多语言表 | 5 | [ipo_quota_type.md](./ipo_quota_type.md) |
| 32 | `t_national_gics_info` | 国民经济分类标准（国资）-主表 | 16 | [national_gics_data.md](./national_gics_data.md) |
| 33 | `t_national_gics_info_l` | 国民经济分类标准（国资）-多语言表 | 5 | [national_gics_data.md](./national_gics_data.md) |
| 34 | `t_star_third_identify` | 星空第三方授权身份-主表 | 10 | [star_third_auth_identify.md](./star_third_auth_identify.md) |
| 35 | `t_theme_account_mapping` | 取数科目映射单据-主表 | 10 | [ipo_account_mapping_bill.md](./ipo_account_mapping_bill.md) |
| 36 | `t_theme_account_mapping_a` | 会计科目-多选基础资料表 | 3 | [ipo_account_mapping_bill.md](./ipo_account_mapping_bill.md) |
| 37 | `t_theme_account_mapping_t` | 核算维度-多选基础资料表 | 3 | [ipo_account_mapping_bill.md](./ipo_account_mapping_bill.md) |
| 38 | `t_theme_anal_item` | IPO主题分析表科目-主表 | 23 | [ipo_theme_anal_item.md](./ipo_theme_anal_item.md) |
| 39 | `t_theme_anal_item_l` | IPO主题分析表科目-多语言表 | 5 | [ipo_theme_anal_item.md](./ipo_theme_anal_item.md) |
| 40 | `t_theme_anal_period` | 期间-多选基础资料表 | 3 | [ipo_anal_datasourse.md](./ipo_anal_datasourse.md) |
| 41 | `t_theme_item_mapping` | 取数项目映射-主表 | 10 | [ipo_item_mapping_bill.md](./ipo_item_mapping_bill.md) |
| 42 | `t_theme_org` | IPO编制组织-主表 | 15 | [ipo_org.md](./ipo_org.md) |
| 43 | `t_theme_org_l` | IPO编制组织-多语言表 | 4 | [ipo_org.md](./ipo_org.md) |
| 44 | `t_theme_report_item` | IPO主体报表方案项目-主表 | 0 | [ipo_org_report_item.md](./ipo_org_report_item.md) |
| 45 | `t_theme_report_item_l` | IPO主体报表方案项目-多语言表 | 0 | [ipo_org_report_item.md](./ipo_org_report_item.md) |
| 46 | `t_theme_report_scheme` | IPO主体报表方案-主表 | 26 | [ipo_org_report_scheme.md](./ipo_org_report_scheme.md) |
| 47 | `t_theme_report_scheme_l` | IPO主体报表方案-多语言表 | 4 | [ipo_org_report_scheme.md](./ipo_org_report_scheme.md) |
| 48 | `t_theme_rtransact_type` | 关联关系类型-主表 | 12 | [theme_rtransact_type.md](./theme_rtransact_type.md) |
| 49 | `t_theme_rtransact_type_l` | 关联关系类型-多语言表 | 4 | [theme_rtransact_type.md](./theme_rtransact_type.md) |
| 50 | `t_theme_scheme_dimansion` | IPO主体方案核算维度-主表 | 0 | [ipo_org_scheme_dimansion.md](./ipo_org_scheme_dimansion.md) |
| 51 | `t_theme_scheme_dimansion_l` | IPO主体方案核算维度-多语言表 | 0 | [ipo_org_scheme_dimansion.md](./ipo_org_scheme_dimansion.md) |
| 52 | `t_theme_transaction_conte` | 关联交易内容-主表 | 13 | [theme_transaction_content.md](./theme_transaction_content.md) |
| 53 | `t_theme_transaction_conte_l` | 关联交易内容-多语言表 | 4 | [theme_transaction_content.md](./theme_transaction_content.md) |
