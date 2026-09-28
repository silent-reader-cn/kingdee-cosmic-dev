# sysext 模块表清单

> 本模块共收录 **19** 张表定义，来自 `sysext_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category sysext
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_kf_cusparamtype` | 自定义参数-主表 | 13 | [kf_cusparamtype.md](./kf_cusparamtype.md) |
| 2 | `t_kf_cusparamtype_l` | 自定义参数-多语言表 | 5 | [kf_cusparamtype.md](./kf_cusparamtype.md) |
| 3 | `t_kf_cusparamtype_ref` | 自定义参数引用-主表 | 3 | [kf_cusparamtype_ref.md](./kf_cusparamtype_ref.md) |
| 4 | `t_kf_instance` | 实例-主表 | 14 | [kf_instance.md](./kf_instance.md) |
| 5 | `t_kf_instance_l` | 实例-多语言表 | 6 | [kf_instance.md](./kf_instance.md) |
| 6 | `t_kf_param` | 单据体-子表 | 7 | [kf_cusparamtype.md](./kf_cusparamtype.md) |
| 7 | `t_kf_param_l` | 单据体-多语言表 | 5 | [kf_cusparamtype.md](./kf_cusparamtype.md) |
| 8 | `t_kf_reference` | 引用关系-主表 | 14 | [kf_reference.md](./kf_reference.md) |
| 9 | `t_ks_control` | 轻脚本分级控制-主表 | 14 | [kingscript_level_control.md](./kingscript_level_control.md) |
| 10 | `t_ks_control_script` | 单据体-子表 | 6 | [kingscript_level_control.md](./kingscript_level_control.md) |
| 11 | `t_ks_monitor` | 轻脚本监控记录-主表 | 11 | [kingscript_monitor.md](./kingscript_monitor.md) |
| 12 | `t_ks_monitor_log` | 单据体-子表 | 12 | [kingscript_monitor.md](./kingscript_monitor.md) |
| 13 | `t_ks_scriptlet` | 脚本片段-主表 | 15 | [bos_scriptlet.md](./bos_scriptlet.md) |
| 14 | `t_ks_scriptlet_group` | 脚本片段分组-主表 | 14 | [bos_scriptlet_group.md](./bos_scriptlet_group.md) |
| 15 | `t_ks_scriptlet_group_l` | 脚本片段分组-多语言表 | 5 | [bos_scriptlet_group.md](./bos_scriptlet_group.md) |
| 16 | `t_ks_scriptlet_l` | 脚本片段-多语言表 | 5 | [bos_scriptlet.md](./bos_scriptlet.md) |
| 17 | `t_meta_bizobj_ext` | 轻扩展元数据-主表 | 0 | [bos_bizextmeta.md](./bos_bizextmeta.md) |
| 18 | `t_meta_formdesign` | 业务对象导入-表单元数据-主表 | 0 | [bos_bizobj_formmeta.md](./bos_bizobj_formmeta.md) |
| 19 | `t_meta_formdesign_l` | 业务对象导入-表单元数据-多语言表 | 0 | [bos_bizobj_formmeta.md](./bos_bizobj_formmeta.md) |
