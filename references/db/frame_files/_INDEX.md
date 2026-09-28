# frame 模块表清单

> 本模块共收录 **50** 张表定义，来自 `frame_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category frame
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bas_attachment` | 附件面板实体-主表 | 27 | [bos_attachment.md](./bos_attachment.md) |
| 2 | `t_bas_attachment` | 附件管理-主表 | 27 | [bos_attachment_management.md](./bos_attachment_management.md) |
| 3 | `t_bas_attachment_l` | 附件面板实体-多语言表 | 4 | [bos_attachment.md](./bos_attachment.md) |
| 4 | `t_bas_carouselbase` | 轮播图-主表 | 10 | [bos_carouselbase.md](./bos_carouselbase.md) |
| 5 | `t_bas_carouselbase_l` | 轮播图-多语言表 | 4 | [bos_carouselbase.md](./bos_carouselbase.md) |
| 6 | `t_bas_carsouelpicture` | 单据体-子表 | 4 | [bos_carouselbase.md](./bos_carouselbase.md) |
| 7 | `t_bas_cloudprinter` | 云打印机-主表 | 26 | [bos_cloudprinter.md](./bos_cloudprinter.md) |
| 8 | `t_bas_cloudprinter_l` | 云打印机-多语言表 | 5 | [bos_cloudprinter.md](./bos_cloudprinter.md) |
| 9 | `t_bas_cloudprintservice` | 云打印服务-主表 | 25 | [bos_cloudprintservice.md](./bos_cloudprintservice.md) |
| 10 | `t_bas_cloudprintservice_l` | 云打印服务-多语言表 | 6 | [bos_cloudprintservice.md](./bos_cloudprintservice.md) |
| 11 | `t_bas_filetype_magicnum` | 附件文件类型魔数-主表 | 3 | [bos_filetype_magicnumber.md](./bos_filetype_magicnumber.md) |
| 12 | `t_bas_flex` | 弹性域-主表 | 8 | [bos_flex.md](./bos_flex.md) |
| 13 | `t_bas_flex` | bos_flexitem-主表 | 8 | [bos_flexitem.md](./bos_flexitem.md) |
| 14 | `t_bas_flex_l` | 弹性域-多语言表 | 5 | [bos_flex.md](./bos_flex.md) |
| 15 | `t_bas_flex_l` | bos_flexitem-多语言表 | 5 | [bos_flexitem.md](./bos_flexitem.md) |
| 16 | `t_bas_flex_property` | 弹性域属性-主表 | 31 | [bos_flex_property.md](./bos_flex_property.md) |
| 17 | `t_bas_flex_property` | 单据体-子表 | 31 | [bos_flexitem.md](./bos_flexitem.md) |
| 18 | `t_bas_flex_property_l` | 弹性域属性-多语言表 | 5 | [bos_flex_property.md](./bos_flex_property.md) |
| 19 | `t_bas_flex_property_l` | 单据体-多语言表 | 5 | [bos_flexitem.md](./bos_flexitem.md) |
| 20 | `t_bas_import_user_config` | 导入导出个性化设置数据-主表 | 23 | [bos_impt_user_config_data.md](./bos_impt_user_config_data.md) |
| 21 | `t_bas_import_user_config_l` | 导入导出个性化设置数据-多语言表 | 4 | [bos_impt_user_config_data.md](./bos_impt_user_config_data.md) |
| 22 | `t_bas_importlog` | 导入结果-主表 | 17 | [bos_importlog.md](./bos_importlog.md) |
| 23 | `t_bas_mobileconfigentry` | 单据体-子表 | 14 | [bos_mobileformconfig2.md](./bos_mobileformconfig2.md) |
| 24 | `t_bas_mobileformconfig` | 移动平台单据启用设置2-主表 | 12 | [bos_mobileformconfig2.md](./bos_mobileformconfig2.md) |
| 25 | `t_bas_mul_scheme_map` | 子单据体-子表 | 11 | [bos_multi_import_scheme.md](./bos_multi_import_scheme.md) |
| 26 | `t_bas_mul_scheme_set` | 单据体-子表 | 17 | [bos_multi_import_scheme.md](./bos_multi_import_scheme.md) |
| 27 | `t_bas_mulimp_res_subtree` | 子单据体-子表 | 6 | [bos_multi_import_result.md](./bos_multi_import_result.md) |
| 28 | `t_bas_mulimp_result` | 导入结果-主表 | 14 | [bos_multi_import_result.md](./bos_multi_import_result.md) |
| 29 | `t_bas_mulimp_resulttree` | 实体详细错误信息-子表 | 14 | [bos_multi_import_result.md](./bos_multi_import_result.md) |
| 30 | `t_bas_mulimport_entity` | 将数据导入到-多选基础资料表 | 3 | [bos_multi_import_scheme.md](./bos_multi_import_scheme.md) |
| 31 | `t_bas_mulimport_scheme` | 自定义导入方案实体-主表 | 16 | [bos_multi_import_scheme.md](./bos_multi_import_scheme.md) |
| 32 | `t_bas_mulimport_scheme_l` | 自定义导入方案实体-多语言表 | 5 | [bos_multi_import_scheme.md](./bos_multi_import_scheme.md) |
| 33 | `t_bas_netprinter` | 打印机-主表 | 0 | [bos_netprinter.md](./bos_netprinter.md) |
| 34 | `t_bas_netprinter_l` | 打印机-多语言表 | 0 | [bos_netprinter.md](./bos_netprinter.md) |
| 35 | `t_bas_netprinter_m` | 打印机-使用范围位图表 | 2 | [bos_netprinter.md](./bos_netprinter.md) |
| 36 | `t_bas_netprinter_u` | 打印机-使用范围表 | 3 | [bos_netprinter.md](./bos_netprinter.md) |
| 37 | `t_bas_print_log` | 打印操作日志-主表 | 8 | [bos_print_logs.md](./bos_print_logs.md) |
| 38 | `t_bas_printtask` | 云打印任务-主表 | 26 | [bos_printtask.md](./bos_printtask.md) |
| 39 | `t_bas_printtask_l` | 云打印任务-多语言表 | 5 | [bos_printtask.md](./bos_printtask.md) |
| 40 | `t_bd_attach_version` | 附件版本维护-主表 | 4 | [bos_attachment_version.md](./bos_attachment_version.md) |
| 41 | `t_bd_attachment` | 附件字段实体-主表 | 20 | [bd_attachment.md](./bd_attachment.md) |
| 42 | `t_bd_attachment_l` | 附件字段实体-多语言表 | 5 | [bd_attachment.md](./bd_attachment.md) |
| 43 | `t_bos_multi_hided_entity` | 多实体导入入口实体隐藏-主表 | 2 | [bos_multi_hided_entity.md](./bos_multi_hided_entity.md) |
| 44 | `t_botp_billtracker` | 单据关联关系-主表 | 6 | [botp_billtracker.md](./botp_billtracker.md) |
| 45 | `t_botp_logdb` | BOTP日志分库-主表 | 4 | [botp_logdb.md](./botp_logdb.md) |
| 46 | `t_meta_mainentityinfo` | 业务对象_打印-主表 | 23 | [bos_entityobject_print.md](./bos_entityobject_print.md) |
| 47 | `t_meta_mainentityinfo_l` | 业务对象_打印-多语言表 | 4 | [bos_entityobject_print.md](./bos_entityobject_print.md) |
| 48 | `t_report_limit_config` | 报表限流-主表 | 10 | [bos_report_limit_config.md](./bos_report_limit_config.md) |
| 49 | `t_sch_task` | 导入结果明细-主表 | 22 | [bos_importtask.md](./bos_importtask.md) |
| 50 | `t_svc_attachment` | 附件管理中心-主表 | 19 | [bos_svc_attachment.md](./bos_svc_attachment.md) |
