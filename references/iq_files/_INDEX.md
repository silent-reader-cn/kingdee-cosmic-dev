# iq 模块表清单

> 本模块共收录 **20** 张表定义，来自 `iq_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope iq
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_history_inquiry` | 同行查询历史-主表 | 4 | [history_inquiry.md](./history_inquiry.md) |
| 2 | `t_iq_compose_detail` | 标准内容-子表 | 8 | [iq_quota_compose_detail.md](./iq_quota_compose_detail.md) |
| 3 | `t_iq_definition` | 名词释义-主表 | 11 | [definition.md](./definition.md) |
| 4 | `t_iq_definition_l` | 名词释义-多语言表 | 4 | [definition.md](./definition.md) |
| 5 | `t_iq_iask_entry` | 单据体-子表 | 5 | [iq_industry_ask.md](./iq_industry_ask.md) |
| 6 | `t_iq_industry_ask` | 行业要求单据-主表 | 3 | [iq_industry_ask.md](./iq_industry_ask.md) |
| 7 | `t_iq_industry_requirement` | 行业要求映射-主表 | 7 | [iq_industry_requirements.md](./iq_industry_requirements.md) |
| 8 | `t_iq_intelligence_d_std` | 标准内容-子表 | 8 | [iq_intelligence_detail.md](./iq_intelligence_detail.md) |
| 9 | `t_iq_intelligence_detail` | 智测测评明细-主表 | 6 | [iq_intelligence_detail.md](./iq_intelligence_detail.md) |
| 10 | `t_iq_intelligence_o_std` | 标准结果-子表 | 10 | [iq_intelligence_order.md](./iq_intelligence_order.md) |
| 11 | `t_iq_intelligence_order` | 智测测评单-主表 | 14 | [iq_intelligence_order.md](./iq_intelligence_order.md) |
| 12 | `t_iq_ir_placetraden` | 所属行业-多选基础资料表 | 3 | [iq_industry_requirements.md](./iq_industry_requirements.md) |
| 13 | `t_iq_legal_basis` | 法规依据-主表 | 14 | [legalbasis.md](./legalbasis.md) |
| 14 | `t_iq_legal_basis_l` | 法规依据-多语言表 | 7 | [legalbasis.md](./legalbasis.md) |
| 15 | `t_iq_major_issues` | 重大事项单据-主表 | 15 | [iq_major_issues_bill.md](./iq_major_issues_bill.md) |
| 16 | `t_iq_qcompose_detail` | 组合指标明细单据-主表 | 6 | [iq_quota_compose_detail.md](./iq_quota_compose_detail.md) |
| 17 | `t_report_attachment` | 模板内容文件-附件表 | 3 | [report_template.md](./report_template.md) |
| 18 | `t_report_attchment_entry` | 单据体-子表 | 9 | [report_template.md](./report_template.md) |
| 19 | `t_report_template` | 报告模板-主表 | 13 | [report_template.md](./report_template.md) |
| 20 | `t_report_template_l` | 报告模板-多语言表 | 4 | [report_template.md](./report_template.md) |
