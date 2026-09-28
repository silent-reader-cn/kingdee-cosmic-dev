# devnew 模块表清单

> 本模块共收录 **22** 张表定义，来自 `devnew_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category devnew
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bas_plugin` | 插件信息-主表 | 5 | [bos_devpn_pluginlistinfo.md](./bos_devpn_pluginlistinfo.md) |
| 2 | `t_bas_plugin_ref` | 引用信息-子表 | 11 | [bos_devpn_pluginlistinfo.md](./bos_devpn_pluginlistinfo.md) |
| 3 | `t_meta_bizapp` | 业务应用列表-主表 | 0 | [bos_devp_bizapplist.md](./bos_devp_bizapplist.md) |
| 4 | `t_meta_bizapp_l` | 业务应用列表-多语言表 | 0 | [bos_devp_bizapplist.md](./bos_devp_bizapplist.md) |
| 5 | `t_meta_entitydesign` | 业务对象列表-主表 | 0 | [bos_devpn_bizobjectlist.md](./bos_devpn_bizobjectlist.md) |
| 6 | `t_meta_entitydesign` | 实体列表-主表 | 0 | [bos_devpn_entitylist.md](./bos_devpn_entitylist.md) |
| 7 | `t_meta_entitydesign` | 实体元数据-主表 | 0 | [bos_devpn_entitymeta.md](./bos_devpn_entitymeta.md) |
| 8 | `t_meta_entitydesign_l` | 业务对象列表-多语言表 | 0 | [bos_devpn_bizobjectlist.md](./bos_devpn_bizobjectlist.md) |
| 9 | `t_meta_entitydesign_l` | 实体列表-多语言表 | 0 | [bos_devpn_entitylist.md](./bos_devpn_entitylist.md) |
| 10 | `t_meta_entitydesign_l` | 实体元数据-多语言表 | 0 | [bos_devpn_entitymeta.md](./bos_devpn_entitymeta.md) |
| 11 | `t_meta_entitytabledict` | 数据表-主表 | 0 | [devp_entitytableinfo.md](./devp_entitytableinfo.md) |
| 12 | `t_meta_fields` | 标准字段-主表 | 0 | [bos_devpn_field.md](./bos_devpn_field.md) |
| 13 | `t_meta_fields_l` | 标准字段-多语言表 | 0 | [bos_devpn_field.md](./bos_devpn_field.md) |
| 14 | `t_meta_fieldsentry` | 单据体-子表 | 0 | [bos_devpn_field.md](./bos_devpn_field.md) |
| 15 | `t_meta_formdesign` | 表单实体-主表 | 0 | [bos_devpn_formmeta.md](./bos_devpn_formmeta.md) |
| 16 | `t_meta_formdesign1` | 参数管理列表-主表 | 0 | [bos_devp_paramlist_bak.md](./bos_devp_paramlist_bak.md) |
| 17 | `t_meta_formdesign_l` | 表单实体-多语言表 | 0 | [bos_devpn_formmeta.md](./bos_devpn_formmeta.md) |
| 18 | `t_meta_managedbill` | 单据管理-主表 | 0 | [bos_devpn_manage_bill.md](./bos_devpn_manage_bill.md) |
| 19 | `t_meta_managedrpt` | 报表管理-主表 | 0 | [bos_devpn_manage_rpt.md](./bos_devpn_manage_rpt.md) |
| 20 | `t_meta_tabledict` | 数据表字典(废弃)-主表 | 0 | [bos_devp_tabledict.md](./bos_devp_tabledict.md) |
| 21 | `t_meta_tablediction` | 数据表字典-主表 | 0 | [bos_devp_tablediction.md](./bos_devp_tablediction.md) |
| 22 | `t_meta_tableref` | 单据体-子表 | 0 | [bos_devp_tabledict.md](./bos_devp_tabledict.md) |
