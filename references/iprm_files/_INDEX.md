# iprm 模块表清单

> 本模块共收录 **15** 张表定义，来自 `iprm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope iprm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_iprm_installlog` | 内容包加载日志-主表 | 13 | [iprm_installlog.md](./iprm_installlog.md) |
| 2 | `t_iprm_installlogentry` | 单据体-子表 | 14 | [iprm_installlog.md](./iprm_installlog.md) |
| 3 | `t_iprm_myresource` | 我的应用-主表 | 17 | [iprm_myresource.md](./iprm_myresource.md) |
| 4 | `t_iprm_parameter` | 云内容参数管理-主表 | 3 | [iprm_parameter.md](./iprm_parameter.md) |
| 5 | `t_iprm_res_itype` | 领域-主表 | 11 | [iprm_res_itype.md](./iprm_res_itype.md) |
| 6 | `t_iprm_res_itype_l` | 领域-多语言表 | 4 | [iprm_res_itype.md](./iprm_res_itype.md) |
| 7 | `t_iprm_res_rtype` | 行业-主表 | 10 | [iprm_res_rtype.md](./iprm_res_rtype.md) |
| 8 | `t_iprm_res_rtype_l` | 行业-多语言表 | 4 | [iprm_res_rtype.md](./iprm_res_rtype.md) |
| 9 | `t_iprm_res_ttype` | 主题-主表 | 12 | [iprm_res_ttype.md](./iprm_res_ttype.md) |
| 10 | `t_iprm_res_ttype_l` | 主题-多语言表 | 4 | [iprm_res_ttype.md](./iprm_res_ttype.md) |
| 11 | `t_iprm_resource` | 云内容（废弃）-主表 | 26 | [iprm_resource.md](./iprm_resource.md) |
| 12 | `t_iprm_resource` | 云内容-主表 | 26 | [iprm_resourcenew.md](./iprm_resourcenew.md) |
| 13 | `t_iprm_resource_entry` | 单据体-子表 | 7 | [iprm_resource.md](./iprm_resource.md) |
| 14 | `t_iprm_resource_entry` | 单据体-子表 | 7 | [iprm_resourcenew.md](./iprm_resourcenew.md) |
| 15 | `t_iprm_resourceinstall` | 内容包安装申请记录-主表 | 14 | [iprm_resourceinstalllist.md](./iprm_resourceinstalllist.md) |
