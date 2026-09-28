# gtcp 模块表清单

> 本模块共收录 **29** 张表定义，来自 `gtcp_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category gtcp
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_gtcp_access_tax_entry` | 税额取数规则-子表 | 14 | [gtcp_accessconfig.md](./gtcp_accessconfig.md) |
| 2 | `t_gtcp_accessconf_entry` | 金额取数规则-子表 | 14 | [gtcp_accessconfig.md](./gtcp_accessconfig.md) |
| 3 | `t_gtcp_accessconfig` | 取数配置-主表 | 19 | [gtcp_accessconfig.md](./gtcp_accessconfig.md) |
| 4 | `t_gtcp_accessconfig_l` | 取数配置-多语言表 | 4 | [gtcp_accessconfig.md](./gtcp_accessconfig.md) |
| 5 | `t_gtcp_biz_type` | 业务类别-主表 | 14 | [gtcp_biz_type.md](./gtcp_biz_type.md) |
| 6 | `t_gtcp_biz_type_l` | 业务类别-多语言表 | 4 | [gtcp_biz_type.md](./gtcp_biz_type.md) |
| 7 | `t_gtcp_compare_entry_info` | 比对单据体明细-主表 | 6 | [gtcp_compare_entry_info.md](./gtcp_compare_entry_info.md) |
| 8 | `t_gtcp_compare_entry_info` | 单据体-子表 | 6 | [gtcp_jt_declare_than_list.md](./gtcp_jt_declare_than_list.md) |
| 9 | `t_gtcp_declare_payrefund` | 申报底稿补退税额附表-主表 | 8 | [gtcp_declare_payrefund.md](./gtcp_declare_payrefund.md) |
| 10 | `t_gtcp_declare_payrefund` | 单据体-子表 | 8 | [gtcp_normal_draft_list.md](./gtcp_normal_draft_list.md) |
| 11 | `t_gtcp_draft_tab` | 全球税底稿左树-主表 | 4 | [gtcp_draft_tab.md](./gtcp_draft_tab.md) |
| 12 | `t_gtcp_fetchitem` | 取数项目-主表 | 28 | [gtcp_fetchitem.md](./gtcp_fetchitem.md) |
| 13 | `t_gtcp_fetchitem_l` | 取数项目-多语言表 | 5 | [gtcp_fetchitem.md](./gtcp_fetchitem.md) |
| 14 | `t_gtcp_fetchitem_u` | 取数项目-使用范围表 | 3 | [gtcp_fetchitem.md](./gtcp_fetchitem.md) |
| 15 | `t_gtcp_gstledger_purchase` | GST明细-采购-主表 | 19 | [gtcp_gstledger_purchase.md](./gtcp_gstledger_purchase.md) |
| 16 | `t_gtcp_gstledger_sales` | GST明细-销售-主表 | 19 | [gtcp_gstledger_sales.md](./gtcp_gstledger_sales.md) |
| 17 | `t_gtcp_jtandbd_tab` | 计提与申报比对页签-主表 | 3 | [gtcp_jtandbd_tab.md](./gtcp_jtandbd_tab.md) |
| 18 | `t_gtcp_rus_vat_draft` | 海外通用申报底稿-主表 | 5 | [gtcp_rus_vat_draft.md](./gtcp_rus_vat_draft.md) |
| 19 | `t_gtcp_shardingplan` | 全球税共享方案-主表 | 13 | [gtcp_shardingplan.md](./gtcp_shardingplan.md) |
| 20 | `t_gtcp_shardingplan_l` | 全球税共享方案-多语言表 | 4 | [gtcp_shardingplan.md](./gtcp_shardingplan.md) |
| 21 | `t_gtcp_sharingplan_orgs` | 共享组织-子表 | 4 | [gtcp_shardingplan.md](./gtcp_shardingplan.md) |
| 22 | `t_gtcp_sharingplan_rules` | 共享规则-子表 | 4 | [gtcp_shardingplan.md](./gtcp_shardingplan.md) |
| 23 | `t_gtcp_taxpay_refund_bill` | 税金缴纳/退还-主表 | 25 | [gtcp_taxpay_refund_bill.md](./gtcp_taxpay_refund_bill.md) |
| 24 | `t_gtcp_usasharefactor` | 美国所得税州分摊系数-主表 | 17 | [gtcp_usasharefactor.md](./gtcp_usasharefactor.md) |
| 25 | `t_gtcp_usasharefactor_l` | 美国所得税州分摊系数-多语言表 | 4 | [gtcp_usasharefactor.md](./gtcp_usasharefactor.md) |
| 26 | `t_tpo_declare_main_tsc` | 申报表查询-主表 | 85 | [gtcp_declare_list.md](./gtcp_declare_list.md) |
| 27 | `t_tpo_declare_main_tsd` | 计提与申报比对列表-主表 | 59 | [gtcp_jt_declare_than_list.md](./gtcp_jt_declare_than_list.md) |
| 28 | `t_tpo_declare_main_tsd` | 申报底稿列表-主表 | 59 | [gtcp_normal_draft_list.md](./gtcp_normal_draft_list.md) |
| 29 | `t_tpo_declare_main_tsd` | 计提底稿列表-主表 | 59 | [gtcp_normal_jt_list.md](./gtcp_normal_jt_list.md) |
