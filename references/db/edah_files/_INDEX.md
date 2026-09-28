# edah 模块表清单

> 本模块共收录 **31** 张表定义，来自 `edah_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category edah
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `fah_e_ap_busbillmodel` | 应付单模型-主表 | 0 | [fah_e_ap_busbillmodel.md](./fah_e_ap_busbillmodel.md) |
| 2 | `fah_e_ap_busbillmodel_1` | 1-子表 | 0 | [fah_e_ap_busbillmodel.md](./fah_e_ap_busbillmodel.md) |
| 3 | `fah_e_edah_finarbill` | 财务应收单事件-主表 | 0 | [fah_e_edah_finarbill.md](./fah_e_edah_finarbill.md) |
| 4 | `fah_e_edah_finarbill_1` | entry1-子表 | 0 | [fah_e_edah_finarbill.md](./fah_e_edah_finarbill.md) |
| 5 | `t_ai_eventclass` | 异构数据对接模型-主表 | 25 | [fah_ext_datamodel.md](./fah_ext_datamodel.md) |
| 6 | `t_ai_eventclass_l` | 异构数据对接模型-多语言表 | 4 | [fah_ext_datamodel.md](./fah_ext_datamodel.md) |
| 7 | `t_ai_eventgroup` | 异构数据分类-主表 | 16 | [fah_ext_datamodel_group.md](./fah_ext_datamodel_group.md) |
| 8 | `t_ai_eventgroup_l` | 异构数据分类-多语言表 | 5 | [fah_ext_datamodel_group.md](./fah_ext_datamodel_group.md) |
| 9 | `t_ai_preevent` | 异构数据对接模型关系-主表 | 7 | [fah_ext_datamodel_rat.md](./fah_ext_datamodel_rat.md) |
| 10 | `t_fah_bgtask_log` | 迁入迁出日志-主表 | 12 | [fah_bgtask_log.md](./fah_bgtask_log.md) |
| 11 | `t_fah_bgtask_log_detail` | 日志明细记录-子表 | 7 | [fah_bgtask_log.md](./fah_bgtask_log.md) |
| 12 | `t_fah_ext_modfldgrp` | 数据字段分组定义-主表 | 11 | [fah_ext_model_fldgrp.md](./fah_ext_model_fldgrp.md) |
| 13 | `t_fah_ext_modflds` | 外部数据模型分录-主表 | 13 | [fah_ext_dataentry.md](./fah_ext_dataentry.md) |
| 14 | `t_fah_flex_import_log` | 导入日志-主表 | 9 | [fah_flex_importlog.md](./fah_flex_importlog.md) |
| 15 | `t_fah_flex_import_log_en` | 错误详情-子表 | 4 | [fah_flex_importlog.md](./fah_flex_importlog.md) |
| 16 | `t_fah_flex_mapval` | 映射键值对弹性域数据表-主表 | 42 | [fah_flex_mapval.md](./fah_flex_mapval.md) |
| 17 | `t_fah_flex_struc` | 映射结构弹性域元数据定义-主表 | 13 | [fah_flex_struc.md](./fah_flex_struc.md) |
| 18 | `t_fah_flex_struc` | 值集扩展字段定义-子表 | 13 | [fah_flex_struc_type.md](./fah_flex_struc_type.md) |
| 19 | `t_fah_flex_struc_type` | 值集扩展字段定义-主表 | 9 | [fah_flex_struc_type.md](./fah_flex_struc_type.md) |
| 20 | `t_fah_flex_valueset` | 值集弹性域数据表-主表 | 29 | [fah_flex_valueset.md](./fah_flex_valueset.md) |
| 21 | `t_fah_valmap_duplog` | 查重结果数据-主表 | 0 | [fah_valmap_duplog.md](./fah_valmap_duplog.md) |
| 22 | `t_fah_valmap_duplog_en` | 单据体-子表 | 0 | [fah_valmap_duplog.md](./fah_valmap_duplog.md) |
| 23 | `t_fah_valmap_struc` | 映射结构定义-主表 | 9 | [fah_valmap_struc.md](./fah_valmap_struc.md) |
| 24 | `t_fah_valmap_type` | 业财数据映射(废弃)-主表 | 14 | [fah_valmap_type.md](./fah_valmap_type.md) |
| 25 | `t_fah_valmap_type` | 业财数据映射-主表 | 14 | [fah_valmap_typenew.md](./fah_valmap_typenew.md) |
| 26 | `t_fah_valmap_type_group` | 业财数据映射分组-主表 | 14 | [fah_valmap_type_group.md](./fah_valmap_type_group.md) |
| 27 | `t_fah_valmap_type_group_l` | 业财数据映射分组-多语言表 | 5 | [fah_valmap_type_group.md](./fah_valmap_type_group.md) |
| 28 | `t_fah_valmap_type_l` | 业财数据映射(废弃)-多语言表 | 4 | [fah_valmap_type.md](./fah_valmap_type.md) |
| 29 | `t_fah_valmap_type_l` | 业财数据映射-多语言表 | 4 | [fah_valmap_typenew.md](./fah_valmap_typenew.md) |
| 30 | `t_fah_valmap_type_org` | 映射适用组织(单据)-主表 | 6 | [fah_valmap_type_org.md](./fah_valmap_type_org.md) |
| 31 | `t_fah_valueset_type` | 外部数据值集-主表 | 10 | [fah_valueset_type.md](./fah_valueset_type.md) |
