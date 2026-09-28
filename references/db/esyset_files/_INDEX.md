# esyset 模块表清单

> 本模块共收录 **51** 张表定义，来自 `esyset_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category esyset
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_eafc_reviewrecord` | 人工复核记录-主表 | 18 | [eafc_reviewrecord.md](./eafc_reviewrecord.md) |
| 2 | `t_eafc_reviewrecord_ent` | 单据体-子表 | 8 | [eafc_reviewrecord.md](./eafc_reviewrecord.md) |
| 3 | `tk_eafc_archive_center` | 档案中心-主表 | 9 | [eafc_archive_center.md](./eafc_archive_center.md) |
| 4 | `tk_eafc_archive_metadata` | 元数据管理-主表 | 13 | [eafc_archive_metadata.md](./eafc_archive_metadata.md) |
| 5 | `tk_eafc_arcorgs` | 适用归档组织-多选基础资料表 | 3 | [eafc_inspect_plan.md](./eafc_inspect_plan.md) |
| 6 | `tk_eafc_book` | 账薄管理-主表 | 10 | [eafc_book.md](./eafc_book.md) |
| 7 | `tk_eafc_booktype` | 账薄类型-主表 | 11 | [eafc_booktype.md](./eafc_booktype.md) |
| 8 | `tk_eafc_booktype_l` | 账薄类型-多语言表 | 5 | [eafc_booktype.md](./eafc_booktype.md) |
| 9 | `tk_eafc_comm_serial_bak` | 流水号表_备份表-主表 | 17 | [eafc_common_serial_back.md](./eafc_common_serial_back.md) |
| 10 | `tk_eafc_common_serial` | 流水号表-主表 | 15 | [eafc_common_serial.md](./eafc_common_serial.md) |
| 11 | `tk_eafc_cus_watermark_bas` | 自定义水印-主表 | 24 | [eafc_cus_watermark_bas.md](./eafc_cus_watermark_bas.md) |
| 12 | `tk_eafc_custom_arcnum_ent` | 单据体-子表 | 12 | [eafc_custom_arcnumber.md](./eafc_custom_arcnumber.md) |
| 13 | `tk_eafc_custom_arcnumber` | 编号规则配置-主表 | 17 | [eafc_custom_arcnumber.md](./eafc_custom_arcnumber.md) |
| 14 | `tk_eafc_custom_arcnumber_l` | 编号规则配置-多语言表 | 4 | [eafc_custom_arcnumber.md](./eafc_custom_arcnumber.md) |
| 15 | `tk_eafc_custom_numtree` | 自定义编号树形类型维护-主表 | 11 | [eafc_custom_numtree.md](./eafc_custom_numtree.md) |
| 16 | `tk_eafc_custom_numtree_l` | 自定义编号树形类型维护-多语言表 | 4 | [eafc_custom_numtree.md](./eafc_custom_numtree.md) |
| 17 | `tk_eafc_data_range` | 单据体-子表 | 7 | [eafc_inspect_plan.md](./eafc_inspect_plan.md) |
| 18 | `tk_eafc_data_range_f` | 业务单据-数据范围-子表 | 7 | [eafc_inspect_plan.md](./eafc_inspect_plan.md) |
| 19 | `tk_eafc_general_archive` | 全宗管理(弃用)-主表 | 18 | [eafc_general_archive.md](./eafc_general_archive.md) |
| 20 | `tk_eafc_general_archive_b` | 全宗管理-主表 | 16 | [eafc_general_archive_base.md](./eafc_general_archive_base.md) |
| 21 | `tk_eafc_general_archive_b_l` | 全宗管理-多语言表 | 4 | [eafc_general_archive_base.md](./eafc_general_archive_base.md) |
| 22 | `tk_eafc_inspect_config` | 单据体-子表 | 25 | [eafc_inspect_config.md](./eafc_inspect_config.md) |
| 23 | `tk_eafc_inspect_config` | 检测环境配置表-主表 | 25 | [eafc_inspect_link_config.md](./eafc_inspect_link_config.md) |
| 24 | `tk_eafc_inspect_config_l` | 检测环境配置表-多语言表 | 4 | [eafc_inspect_link_config.md](./eafc_inspect_link_config.md) |
| 25 | `tk_eafc_inspect_config_u` | 检测环境配置表-使用范围表 | 3 | [eafc_inspect_link_config.md](./eafc_inspect_link_config.md) |
| 26 | `tk_eafc_inspect_detail` | 单据体-子表 | 25 | [eafc_four_inspect_result.md](./eafc_four_inspect_result.md) |
| 27 | `tk_eafc_inspect_list_log` | 检测日志-主表 | 20 | [eafc_inspect_list_log.md](./eafc_inspect_list_log.md) |
| 28 | `tk_eafc_inspect_plan` | 业务检测配置-主表 | 32 | [eafc_inspect_plan.md](./eafc_inspect_plan.md) |
| 29 | `tk_eafc_inspect_plan_orgs` | 适用组织-多选基础资料表 | 3 | [eafc_inspect_plan.md](./eafc_inspect_plan.md) |
| 30 | `tk_eafc_inspect_result` | 四性检测方案结果-主表 | 31 | [eafc_four_inspect_result.md](./eafc_four_inspect_result.md) |
| 31 | `tk_eafc_inspect_result` | 四性检测结果(废弃)-主表 | 31 | [eafc_inspect_result.md](./eafc_inspect_result.md) |
| 32 | `tk_eafc_inspect_schema` | 四性检测配置-主表 | 34 | [eafc_inspect_schema.md](./eafc_inspect_schema.md) |
| 33 | `tk_eafc_inspect_schema_l` | 四性检测配置-多语言表 | 4 | [eafc_inspect_schema.md](./eafc_inspect_schema.md) |
| 34 | `tk_eafc_inspect_schema_u` | 四性检测配置-使用范围表 | 3 | [eafc_inspect_schema.md](./eafc_inspect_schema.md) |
| 35 | `tk_eafc_inspect_strategy` | 四性检测基础资料-主表 | 29 | [eafc_inspect_base.md](./eafc_inspect_base.md) |
| 36 | `tk_eafc_inspect_strategy` | 四性检测配置-主表 | 29 | [eafc_inspect_config.md](./eafc_inspect_config.md) |
| 37 | `tk_eafc_inspect_strategy_l` | 四性检测配置-多语言表 | 4 | [eafc_inspect_config.md](./eafc_inspect_config.md) |
| 38 | `tk_eafc_inspect_strategy_u` | 四性检测配置-使用范围表 | 3 | [eafc_inspect_config.md](./eafc_inspect_config.md) |
| 39 | `tk_eafc_mul_businesss` | 自定义单据类型-多选基础资料表 | 3 | [eafc_inspect_plan.md](./eafc_inspect_plan.md) |
| 40 | `tk_eafc_org` | 归档体系_旧-主表 | 14 | [eafc_org.md](./eafc_org.md) |
| 41 | `tk_eafc_org_l` | 归档体系_旧-多语言表 | 4 | [eafc_org.md](./eafc_org.md) |
| 42 | `tk_eafc_s_inspect_log` | 质检检测日志-主表 | 24 | [eafc_standard_inspect_log.md](./eafc_standard_inspect_log.md) |
| 43 | `tk_eafc_syset_busf7_mult` | 适用分类-多选基础资料表 | 3 | [eafc_custom_arcnumber.md](./eafc_custom_arcnumber.md) |
| 44 | `tk_fpy_inspect_itemdetail` | 单据体-子表 | 7 | [eafc_four_inspect_result.md](./eafc_four_inspect_result.md) |
| 45 | `tk_fpy_scan_label` | 影像标签配置-主表 | 12 | [fpy_scan_label_conf.md](./fpy_scan_label_conf.md) |
| 46 | `tk_fpy_scan_label_item` | 影像文档标签映射-子表 | 6 | [fpy_scan_label_conf.md](./fpy_scan_label_conf.md) |
| 47 | `tk_fpy_scan_label_l` | 影像标签配置-多语言表 | 4 | [fpy_scan_label_conf.md](./fpy_scan_label_conf.md) |
| 48 | `tk_fpy_syset_orgmapp` | 归档组织映射-主表 | 9 | [fpy_syset_orgmapp_bill.md](./fpy_syset_orgmapp_bill.md) |
| 49 | `tk_fpy_syset_orgmapp_ent` | 归档组织映射基础资料-主表 | 19 | [fpy_syset_orgmapp.md](./fpy_syset_orgmapp.md) |
| 50 | `tk_fpy_syset_orgmapp_ent` | 单据体-子表 | 19 | [fpy_syset_orgmapp_bill.md](./fpy_syset_orgmapp_bill.md) |
| 51 | `tk_fpy_syset_orgmapp_ent_l` | 归档组织映射基础资料-多语言表 | 4 | [fpy_syset_orgmapp.md](./fpy_syset_orgmapp.md) |
