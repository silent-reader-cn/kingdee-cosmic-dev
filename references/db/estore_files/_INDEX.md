# estore 模块表清单

> 本模块共收录 **23** 张表定义，来自 `estore_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category estore
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `tk_eafc_box_confi` | 单据体-子表 | 0 | [eafc_floor_part_config.md](./eafc_floor_part_config.md) |
| 2 | `tk_eafc_box_config` | 单据体-子表 | 10 | [eafc_floor_config_base.md](./eafc_floor_config_base.md) |
| 3 | `tk_eafc_box_config` | 单据体-子表 | 10 | [eafc_shelf_config.md](./eafc_shelf_config.md) |
| 4 | `tk_eafc_floor_config_base` | 层节设置(基础资料)-主表 | 14 | [eafc_floor_config_base.md](./eafc_floor_config_base.md) |
| 5 | `tk_eafc_floor_config_base_l` | 层节设置(基础资料)-多语言表 | 4 | [eafc_floor_config_base.md](./eafc_floor_config_base.md) |
| 6 | `tk_eafc_floor_part_confi` | 层节设置(已废弃)-主表 | 0 | [eafc_floor_part_config.md](./eafc_floor_part_config.md) |
| 7 | `tk_eafc_paper_doc_log` | 纸档整理日志-主表 | 16 | [eafc_paper_doc_log.md](./eafc_paper_doc_log.md) |
| 8 | `tk_eafc_shelf_config` | 密集架设置-主表 | 16 | [eafc_shelf_config.md](./eafc_shelf_config.md) |
| 9 | `tk_eafc_store_area_config` | 区域单据体-子表 | 21 | [eafc_store_config.md](./eafc_store_config.md) |
| 10 | `tk_eafc_store_area_config` | 单据体-子表 | 21 | [eafc_store_config_base.md](./eafc_store_config_base.md) |
| 11 | `tk_eafc_store_config` | 库房结构设置（已废弃）-主表 | 0 | [eafc_store_config.md](./eafc_store_config.md) |
| 12 | `tk_eafc_store_config_base` | 库房设置-主表 | 30 | [eafc_store_config_base.md](./eafc_store_config_base.md) |
| 13 | `tk_eafc_store_config_base_l` | 库房设置-多语言表 | 4 | [eafc_store_config_base.md](./eafc_store_config_base.md) |
| 14 | `tk_eafc_store_config_base_u` | 库房设置-使用范围表 | 3 | [eafc_store_config_base.md](./eafc_store_config_base.md) |
| 15 | `tk_fpy_message_notice` | 消息通知单-主表 | 17 | [fpy_message_notice.md](./fpy_message_notice.md) |
| 16 | `tk_fpy_msg_notice_item` | 单据体-子表 | 12 | [fpy_message_notice.md](./fpy_message_notice.md) |
| 17 | `tk_fpy_scan_bill` | 扫码单据-主表 | 37 | [fpy_scan_bill.md](./fpy_scan_bill.md) |
| 18 | `tk_fpy_storage_in` | 入库管理单-主表 | 26 | [fpy_storage_in.md](./fpy_storage_in.md) |
| 19 | `tk_fpy_storage_in_item` | 单据体-子表 | 16 | [fpy_storage_in.md](./fpy_storage_in.md) |
| 20 | `tk_fpy_storage_manag_item` | 单据体-子表 | 16 | [fpy_storage_manage.md](./fpy_storage_manage.md) |
| 21 | `tk_fpy_storage_manage` | 出库管理单-主表 | 27 | [fpy_storage_manage.md](./fpy_storage_manage.md) |
| 22 | `tk_fpy_storage_out` | 出库申请单-主表 | 20 | [fpy_storage_out.md](./fpy_storage_out.md) |
| 23 | `tk_fpy_storage_out_item` | 单据体-子表 | 15 | [fpy_storage_out.md](./fpy_storage_out.md) |
