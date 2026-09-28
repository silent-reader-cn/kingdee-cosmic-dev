# cfa 模块表清单

> 本模块共收录 **18** 张表定义，来自 `cfa_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope cfa
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_cfa_parameter_setting` | 参数设置单据-主表 | 7 | [cfa_parameter_setting_doc.md](./cfa_parameter_setting_doc.md) |
| 2 | `t_cfa_quota_card_memory` | 指标卡片页面记忆-主表 | 8 | [cfa_quota_card_memory.md](./cfa_quota_card_memory.md) |
| 3 | `t_cfa_quota_cardlibrary` | 指标卡片库-主表 | 29 | [cfa_quota_cardlibrary.md](./cfa_quota_cardlibrary.md) |
| 4 | `t_cfa_quota_cardlibrary_l` | 指标卡片库-多语言表 | 4 | [cfa_quota_cardlibrary.md](./cfa_quota_cardlibrary.md) |
| 5 | `t_cfa_risk_financial` | 财务风险模型单据-主表 | 8 | [cfa_risk_financial_doc.md](./cfa_risk_financial_doc.md) |
| 6 | `t_cfa_risk_financial_impo` | 重要程度单据体-子表 | 5 | [cfa_risk_financial_doc.md](./cfa_risk_financial_doc.md) |
| 7 | `t_cfa_risk_financial_over` | 总体风险水平单据体-子表 | 6 | [cfa_risk_financial_doc.md](./cfa_risk_financial_doc.md) |
| 8 | `t_cfa_risk_financial_type` | 风险类别单据体-子表 | 5 | [cfa_risk_financial_doc.md](./cfa_risk_financial_doc.md) |
| 9 | `t_cfa_target_value` | 目标值表-主表 | 12 | [cfa_target_value_bill.md](./cfa_target_value_bill.md) |
| 10 | `t_cfa_targetv_detail` | 数据存储实体-子表 | 24 | [cfa_target_value_bill.md](./cfa_target_value_bill.md) |
| 11 | `t_cfa_three_fin_report` | 公司三大财务报表-主表 | 13 | [cfa_three_fin_report_bill.md](./cfa_three_fin_report_bill.md) |
| 12 | `t_cfa_warning_anal` | 异常原因分析单据-主表 | 25 | [cfa_item_warning_anal_bil.md](./cfa_item_warning_anal_bil.md) |
| 13 | `t_cfa_warning_anal_entry` | 单据体-子表 | 6 | [cfa_item_warning_anal_bil.md](./cfa_item_warning_anal_bil.md) |
| 14 | `t_cfa_warning_anal_entry_l` | 单据体-多语言表 | 4 | [cfa_item_warning_anal_bil.md](./cfa_item_warning_anal_bil.md) |
| 15 | `t_cfa_warning_anal_l` | 异常原因分析单据-多语言表 | 4 | [cfa_item_warning_anal_bil.md](./cfa_item_warning_anal_bil.md) |
| 16 | `t_cfa_warning_rules` | 预警规则-主表 | 23 | [cfa_warning_rules.md](./cfa_warning_rules.md) |
| 17 | `t_cfa_warning_rules_l` | 预警规则-多语言表 | 4 | [cfa_warning_rules.md](./cfa_warning_rules.md) |
| 18 | `t_warning_rule_detail` | 预警规则明细-子表 | 11 | [cfa_warning_rules.md](./cfa_warning_rules.md) |
