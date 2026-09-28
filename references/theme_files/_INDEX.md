# theme 模块表清单

> 本模块共收录 **68** 张表定义，来自 `theme_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope theme
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_balance_funds_entryent` | 单据体-子表 | 5 | [theme_balance_funds_bill.md](./theme_balance_funds_bill.md) |
| 2 | `t_compliance_guidance_nam` | IPO合规指引管理单据-主表 | 16 | [compliance_guidance_bill.md](./compliance_guidance_bill.md) |
| 3 | `t_inquiry_rate_distributi` | 问询率分布-主表 | 3 | [inquiry_rate_distribution.md](./inquiry_rate_distribution.md) |
| 4 | `t_risk_label_basicdata` | IPO风险标签下拉基础资料-主表 | 12 | [risk_label_basicdata.md](./risk_label_basicdata.md) |
| 5 | `t_risk_label_basicdata_l` | IPO风险标签下拉基础资料-多语言表 | 4 | [risk_label_basicdata.md](./risk_label_basicdata.md) |
| 6 | `t_risk_label_management` | IPO风险标签管理单据-主表 | 15 | [risk_label_bill.md](./risk_label_bill.md) |
| 7 | `t_theme_ap_ag_entryentity` | 单据体-子表 | 6 | [theme_ap_aging_bill.md](./theme_ap_aging_bill.md) |
| 8 | `t_theme_ap_aging` | 应付款账龄结构分析表-主表 | 8 | [theme_ap_aging_bill.md](./theme_ap_aging_bill.md) |
| 9 | `t_theme_ap_balance_change` | 应付款余额变动分析表-主表 | 13 | [theme_ap_balance_bill.md](./theme_ap_balance_bill.md) |
| 10 | `t_theme_ap_pa_entryentity` | 单据体-子表 | 6 | [theme_ap_pay_bill.md](./theme_ap_pay_bill.md) |
| 11 | `t_theme_ap_pay` | 应交税费分析表-主表 | 8 | [theme_ap_pay_bill.md](./theme_ap_pay_bill.md) |
| 12 | `t_theme_ap_topcustomer` | 前五大供应商应付分析表-主表 | 11 | [theme_ap_topcustomer_bill.md](./theme_ap_topcustomer_bill.md) |
| 13 | `t_theme_ar_aging` | 应收账款账龄结构分析表-主表 | 9 | [theme_ar_aging_bill.md](./theme_ar_aging_bill.md) |
| 14 | `t_theme_ar_aging_entity` | 报告数据-子表 | 9 | [theme_ar_aging_bill.md](./theme_ar_aging_bill.md) |
| 15 | `t_theme_ar_balance_change` | 应收款余额变动分析表-主表 | 15 | [theme_ar_balance_bill.md](./theme_ar_balance_bill.md) |
| 16 | `t_theme_ar_topcustomer` | 前五大客户应收分析表-主表 | 12 | [theme_ar_topcustomer_bill.md](./theme_ar_topcustomer_bill.md) |
| 17 | `t_theme_balance_funds` | 往来款项余额分析表-主表 | 9 | [theme_balance_funds_bill.md](./theme_balance_funds_bill.md) |
| 18 | `t_theme_bm_entryentity` | 借款单据体-子表 | 8 | [theme_borrow_money_bill.md](./theme_borrow_money_bill.md) |
| 19 | `t_theme_borrow_money` | 借款分析表-主表 | 13 | [theme_borrow_money_bill.md](./theme_borrow_money_bill.md) |
| 20 | `t_theme_cash_entryentity` | 单据体-子表 | 6 | [theme_cash_receipts_bill.md](./theme_cash_receipts_bill.md) |
| 21 | `t_theme_cash_flow` | 现金流量分析表-主表 | 44 | [theme_cash_flow_bill.md](./theme_cash_flow_bill.md) |
| 22 | `t_theme_cash_payment` | 现金付款分析表-主表 | 11 | [theme_cash_payment_bill.md](./theme_cash_payment_bill.md) |
| 23 | `t_theme_cash_receipts` | 现金收款分析表-主表 | 11 | [theme_cash_receipts_bill.md](./theme_cash_receipts_bill.md) |
| 24 | `t_theme_co_income` | 营业收入分析表-主表 | 13 | [theme_co_income_bill.md](./theme_co_income_bill.md) |
| 25 | `t_theme_fc_entryentity` | 单据体-子表 | 8 | [theme_finance_cost_bill.md](./theme_finance_cost_bill.md) |
| 26 | `t_theme_finance_cost` | 财务费用分析表-主表 | 8 | [theme_finance_cost_bill.md](./theme_finance_cost_bill.md) |
| 27 | `t_theme_gross_margin` | 毛利率波动分析表-主表 | 10 | [theme_gross_margin_bill.md](./theme_gross_margin_bill.md) |
| 28 | `t_theme_losses_bill` | 非经常性损益分析表-主表 | 52 | [theme_rg_losses_bill.md](./theme_rg_losses_bill.md) |
| 29 | `t_theme_manage_cost` | 管理费用分析表-主表 | 8 | [theme_manage_cost_bill.md](./theme_manage_cost_bill.md) |
| 30 | `t_theme_mb_area` | 主营业务收入构成分析表（按地区）-主表 | 8 | [theme_mb_area_bill.md](./theme_mb_area_bill.md) |
| 31 | `t_theme_mb_product` | 主营业收入分析表（按产品）-主表 | 8 | [theme_mb_product_bill.md](./theme_mb_product_bill.md) |
| 32 | `t_theme_mb_service` | 主营业务收入构成分析表（按业务板块）-主表 | 8 | [theme_mb_service_bill.md](./theme_mb_service_bill.md) |
| 33 | `t_theme_mba_entryentity` | 单据体-子表 | 9 | [theme_mb_area_bill.md](./theme_mb_area_bill.md) |
| 34 | `t_theme_mbp_entryentity` | 单据体-子表 | 11 | [theme_mb_product_bill.md](./theme_mb_product_bill.md) |
| 35 | `t_theme_mbs_entryentity` | 单据体-子表 | 9 | [theme_mb_service_bill.md](./theme_mb_service_bill.md) |
| 36 | `t_theme_mc_entryentity` | 单据体-子表 | 8 | [theme_manage_cost_bill.md](./theme_manage_cost_bill.md) |
| 37 | `t_theme_menu_risk_attribu` | IPO主题分析菜单-风险标签属性-主表 | 14 | [theme_menu_risk_attribute.md](./theme_menu_risk_attribute.md) |
| 38 | `t_theme_menu_risk_attribu_l` | IPO主题分析菜单-风险标签属性-多语言表 | 4 | [theme_menu_risk_attribute.md](./theme_menu_risk_attribute.md) |
| 39 | `t_theme_menu_type` | IPO主题分析菜单类型-主表 | 18 | [theme_menu_type.md](./theme_menu_type.md) |
| 40 | `t_theme_menu_type_guide` | IPO主题分析菜单-合规指引页签-主表 | 11 | [theme_menu_type_guide.md](./theme_menu_type_guide.md) |
| 41 | `t_theme_menu_type_guide_l` | IPO主题分析菜单-合规指引页签-多语言表 | 4 | [theme_menu_type_guide.md](./theme_menu_type_guide.md) |
| 42 | `t_theme_menu_type_l` | IPO主题分析菜单类型-多语言表 | 5 | [theme_menu_type.md](./theme_menu_type.md) |
| 43 | `t_theme_menu_type_risk` | IPO主题分析菜单-风险标签-主表 | 14 | [theme_menu_type_risklabel.md](./theme_menu_type_risklabel.md) |
| 44 | `t_theme_menu_type_risk_l` | IPO主题分析菜单-风险标签-多语言表 | 4 | [theme_menu_type_risklabel.md](./theme_menu_type_risklabel.md) |
| 45 | `t_theme_money_entryentity` | 单据体-子表 | 8 | [theme_money_lending_bill.md](./theme_money_lending_bill.md) |
| 46 | `t_theme_money_funds` | 货币资金结构分析表-主表 | 17 | [theme_money_funds_bill.md](./theme_money_funds_bill.md) |
| 47 | `t_theme_money_lending` | 资金拆借分析表-主表 | 9 | [theme_money_lending_bill.md](./theme_money_lending_bill.md) |
| 48 | `t_theme_oc_entryentity` | 单据体-子表 | 6 | [theme_operating_cost_bill.md](./theme_operating_cost_bill.md) |
| 49 | `t_theme_operating_cost` | 营业成本构成分析表-主表 | 9 | [theme_operating_cost_bill.md](./theme_operating_cost_bill.md) |
| 50 | `t_theme_pcash_entryentity` | 单据体-子表 | 6 | [theme_cash_payment_bill.md](./theme_cash_payment_bill.md) |
| 51 | `t_theme_rc_entryent` | 单据体-子表 | 8 | [theme_research_cost_bill.md](./theme_research_cost_bill.md) |
| 52 | `t_theme_rdetermination` | 关联关系认定表-主表 | 23 | [theme_rdetermination_bill.md](./theme_rdetermination_bill.md) |
| 53 | `t_theme_rdetermination_l` | 关联关系认定表-多语言表 | 4 | [theme_rdetermination_bill.md](./theme_rdetermination_bill.md) |
| 54 | `t_theme_rdetermination_u` | 关联关系认定表-使用范围表 | 3 | [theme_rdetermination_bill.md](./theme_rdetermination_bill.md) |
| 55 | `t_theme_research_cost` | 研发费用分析表-主表 | 8 | [theme_research_cost_bill.md](./theme_research_cost_bill.md) |
| 56 | `t_theme_risk` | 主题风险单据-主表 | 12 | [theme_risk.md](./theme_risk.md) |
| 57 | `t_theme_sale_trade` | 关联方销售交易分析表-主表 | 10 | [theme_sale_trade_bill.md](./theme_sale_trade_bill.md) |
| 58 | `t_theme_sc_entryentity` | 单据体-子表 | 8 | [theme_selling_cost_bill.md](./theme_selling_cost_bill.md) |
| 59 | `t_theme_selling_cost` | 销售费用分析表-主表 | 8 | [theme_selling_cost_bill.md](./theme_selling_cost_bill.md) |
| 60 | `t_theme_sf_entity` | 存货单据体-子表 | 10 | [theme_stock_falling_bill.md](./theme_stock_falling_bill.md) |
| 61 | `t_theme_stock_falling` | 存货构成与跌价分析表-主表 | 10 | [theme_stock_falling_bill.md](./theme_stock_falling_bill.md) |
| 62 | `t_theme_stock_turnover` | 存货周转分析表-主表 | 10 | [theme_stock_turnover_bill.md](./theme_stock_turnover_bill.md) |
| 63 | `t_theme_tfive_customer` | 收入前五大客户依赖分析表-主表 | 12 | [theme_tfive_customer_bill.md](./theme_tfive_customer_bill.md) |
| 64 | `t_theme_tparty_return` | 第三方回款分析表-主表 | 10 | [theme_tparty_return_bill.md](./theme_tparty_return_bill.md) |
| 65 | `t_theme_tpr_entryentity` | 单据体-子表 | 6 | [theme_tparty_return_bill.md](./theme_tparty_return_bill.md) |
| 66 | `t_theme_tsale_entryentity` | 单据体-子表 | 5 | [theme_sale_trade_bill.md](./theme_sale_trade_bill.md) |
| 67 | `t_theme_volume_trade` | 关联方采购交易额分析表-主表 | 10 | [theme_volume_trade_bill.md](./theme_volume_trade_bill.md) |
| 68 | `t_theme_vt_entryentity` | 单据体-子表 | 5 | [theme_volume_trade_bill.md](./theme_volume_trade_bill.md) |
