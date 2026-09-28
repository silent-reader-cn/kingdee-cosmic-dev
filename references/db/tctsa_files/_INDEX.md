# tctsa 模块表清单

> 本模块共收录 **51** 张表定义，来自 `tctsa_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category tctsa
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_tctb_declare_main` | 申报进度明细-主表 | 66 | [tctsa_tax_progresslist.md](./tctsa_tax_progresslist.md) |
| 2 | `t_tctsa_fix_filling_query` | 固定填报查询-主表 | 23 | [tctsa_fixed_filling_query.md](./tctsa_fixed_filling_query.md) |
| 3 | `t_tctsa_fix_filling_query_l` | 固定填报查询-多语言表 | 4 | [tctsa_fixed_filling_query.md](./tctsa_fixed_filling_query.md) |
| 4 | `t_tctsa_fixed_duo_label` | 标签-多选基础资料表 | 3 | [tctsa_fixed_filling_query.md](./tctsa_fixed_filling_query.md) |
| 5 | `t_tctsa_label_type` | 标签类型-多选基础资料表 | 3 | [tctsa_target_info.md](./tctsa_target_info.md) |
| 6 | `t_tctsa_predata_entry` | 单据体-子表 | 9 | [tctsa_preferentdata.md](./tctsa_preferentdata.md) |
| 7 | `t_tctsa_predetail_entry` | 单据体-子表 | 9 | [tctsa_preferentdetail.md](./tctsa_preferentdetail.md) |
| 8 | `t_tctsa_preferentdata` | 优惠取数配置-主表 | 16 | [tctsa_preferentdata.md](./tctsa_preferentdata.md) |
| 9 | `t_tctsa_preferentdata_l` | 优惠取数配置-多语言表 | 4 | [tctsa_preferentdata.md](./tctsa_preferentdata.md) |
| 10 | `t_tctsa_preferentdetail` | 优惠明细-主表 | 22 | [tctsa_preferentdetail.md](./tctsa_preferentdetail.md) |
| 11 | `t_tctsa_provisi_tjsjb_djt` | 单据体-子表 | 7 | [tctsa_provision_tjsjb.md](./tctsa_provision_tjsjb.md) |
| 12 | `t_tctsa_provision_tjsjb` | 统计计提税金表-主表 | 14 | [tctsa_provision_tjsjb.md](./tctsa_provision_tjsjb.md) |
| 13 | `t_tctsa_rep_item_assign` | 固定填报项分配-主表 | 13 | [tctsa_report_item_assign.md](./tctsa_report_item_assign.md) |
| 14 | `t_tctsa_report_dtask_bill` | 待填报任务列表-主表 | 14 | [tctsa_report_dtask_bill.md](./tctsa_report_dtask_bill.md) |
| 15 | `t_tctsa_report_dtask_bill` | 临时填报查询-主表 | 14 | [tctsa_temp_report_query.md](./tctsa_temp_report_query.md) |
| 16 | `t_tctsa_report_item` | 新增填报项-主表 | 14 | [tctsa_report_items.md](./tctsa_report_items.md) |
| 17 | `t_tctsa_report_item_l` | 新增填报项-多语言表 | 4 | [tctsa_report_items.md](./tctsa_report_items.md) |
| 18 | `t_tctsa_report_item_label` | 标签单据体-子表 | 4 | [tctsa_report_items.md](./tctsa_report_items.md) |
| 19 | `t_tctsa_report_items_tree` | 填报类型-主表 | 14 | [tctsa_report_items_tree.md](./tctsa_report_items_tree.md) |
| 20 | `t_tctsa_report_items_tree_l` | 填报类型-多语言表 | 5 | [tctsa_report_items_tree.md](./tctsa_report_items_tree.md) |
| 21 | `t_tctsa_rpt_arg` | 参数单据体-子表 | 9 | [tctsa_rpt_data.md](./tctsa_rpt_data.md) |
| 22 | `t_tctsa_rpt_cell` | 单元格单据体-子表 | 15 | [tctsa_rpt_data.md](./tctsa_rpt_data.md) |
| 23 | `t_tctsa_rpt_data` | 报表数据集-主表 | 16 | [tctsa_rpt_data.md](./tctsa_rpt_data.md) |
| 24 | `t_tctsa_rpt_data_l` | 报表数据集-多语言表 | 4 | [tctsa_rpt_data.md](./tctsa_rpt_data.md) |
| 25 | `t_tctsa_rpt_value` | 值单据体-子表 | 10 | [tctsa_rpt_data.md](./tctsa_rpt_data.md) |
| 26 | `t_tctsa_sharingplan` | 共享方案-子表 | 6 | [tctsa_report_item_assign.md](./tctsa_report_item_assign.md) |
| 27 | `t_tctsa_sharingplan_items` | 风险-子表 | 5 | [tctsa_report_item_assign.md](./tctsa_report_item_assign.md) |
| 28 | `t_tctsa_sharingplan_orgs` | 被共享组织-子表 | 4 | [tctsa_report_item_assign.md](./tctsa_report_item_assign.md) |
| 29 | `t_tctsa_statistic_project` | 统计项目-主表 | 21 | [tctsa_statistic_project.md](./tctsa_statistic_project.md) |
| 30 | `t_tctsa_statistic_project_l` | 统计项目-多语言表 | 5 | [tctsa_statistic_project.md](./tctsa_statistic_project.md) |
| 31 | `t_tctsa_ta_collection_djt` | 单据体-子表 | 0 | [tctsa_tax_collection.md](./tctsa_tax_collection.md) |
| 32 | `t_tctsa_target_info` | 指标-主表 | 16 | [tctsa_target_info.md](./tctsa_target_info.md) |
| 33 | `t_tctsa_target_info_l` | 指标-多语言表 | 4 | [tctsa_target_info.md](./tctsa_target_info.md) |
| 34 | `t_tctsa_target_offset` | 单据体-子表 | 6 | [tctsa_target_info.md](./tctsa_target_info.md) |
| 35 | `t_tctsa_tax_collection` | 税金采集-主表 | 0 | [tctsa_tax_collection.md](./tctsa_tax_collection.md) |
| 36 | `t_tctsa_tax_collection_l` | 税金采集-多语言表 | 0 | [tctsa_tax_collection.md](./tctsa_tax_collection.md) |
| 37 | `t_tctsa_tax_collections` | 税金采集-主表 | 12 | [tctsa_tax_collections.md](./tctsa_tax_collections.md) |
| 38 | `t_tctsa_temp_dtask_djt` | 单据体-子表 | 7 | [tctsa_report_dtask_bill.md](./tctsa_report_dtask_bill.md) |
| 39 | `t_tctsa_temp_dtask_djt` | 单据体-子表 | 7 | [tctsa_temp_report_query.md](./tctsa_temp_report_query.md) |
| 40 | `t_tctsa_temp_dtask_label` | 卡片分录-子表 | 4 | [tctsa_report_dtask_bill.md](./tctsa_report_dtask_bill.md) |
| 41 | `t_tctsa_temp_dtask_label` | 卡片分录-子表 | 4 | [tctsa_temp_report_query.md](./tctsa_temp_report_query.md) |
| 42 | `t_tctsa_temp_items` | 填报事项-子表 | 6 | [tctsa_temp_report_item.md](./tctsa_temp_report_item.md) |
| 43 | `t_tctsa_temp_report_item` | 新增临时填报任务-主表 | 15 | [tctsa_temp_report_item.md](./tctsa_temp_report_item.md) |
| 44 | `t_tctsa_temp_report_label` | 标签单据体-子表 | 4 | [tctsa_temp_report_item.md](./tctsa_temp_report_item.md) |
| 45 | `t_tctsa_temp_share_orgs` | 组织被共享范围-子表 | 4 | [tctsa_temp_report_item.md](./tctsa_temp_report_item.md) |
| 46 | `t_tctsa_tjsjb_access_djt` | 单据体-子表 | 9 | [tctsa_tjsjb_rule_config.md](./tctsa_tjsjb_rule_config.md) |
| 47 | `t_tctsa_tjsjb_config` | 报表模板设置-主表 | 0 | [tctsa_tjsjb_config.md](./tctsa_tjsjb_config.md) |
| 48 | `t_tctsa_tjsjb_config_djt` | 单据体-子表 | 0 | [tctsa_tjsjb_config.md](./tctsa_tjsjb_config.md) |
| 49 | `t_tctsa_tjsjb_config_l` | 报表模板设置-多语言表 | 0 | [tctsa_tjsjb_config.md](./tctsa_tjsjb_config.md) |
| 50 | `t_tctsa_tjsjb_rule_config` | 取数规则配置-主表 | 20 | [tctsa_tjsjb_rule_config.md](./tctsa_tjsjb_rule_config.md) |
| 51 | `t_tctsa_tjsjb_rule_config_l` | 取数规则配置-多语言表 | 4 | [tctsa_tjsjb_rule_config.md](./tctsa_tjsjb_rule_config.md) |
