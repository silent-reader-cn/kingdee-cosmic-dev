# iprm 模块表清单

> 本模块共收录 **32** 张表定义，来自 `iprm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category iprm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_gsc_enablepack` | 选择启用的本地化包-多选基础资料表 | 3 | [gsc_localconfig.md](./gsc_localconfig.md) |
| 2 | `t_gsc_localconfig` | 本地化配置-主表 | 10 | [gsc_localconfig.md](./gsc_localconfig.md) |
| 3 | `t_gsc_localconfig_l` | 本地化配置-多语言表 | 4 | [gsc_localconfig.md](./gsc_localconfig.md) |
| 4 | `t_gsc_locallog` | 本地化日志-主表 | 25 | [gsc_locallog.md](./gsc_locallog.md) |
| 5 | `t_gsc_locallog_l` | 本地化日志-多语言表 | 4 | [gsc_locallog.md](./gsc_locallog.md) |
| 6 | `t_gsc_localpackconfig` | 本地化包-主表 | 12 | [gsc_localpackconfig.md](./gsc_localpackconfig.md) |
| 7 | `t_gsc_localpackconfig_l` | 本地化包-多语言表 | 4 | [gsc_localpackconfig.md](./gsc_localpackconfig.md) |
| 8 | `t_gsc_localpackconfigapp` | 应用分录-子表 | 7 | [gsc_localpackconfig.md](./gsc_localpackconfig.md) |
| 9 | `t_gsc_localpackconfigapp_l` | 应用分录-多语言表 | 5 | [gsc_localpackconfig.md](./gsc_localpackconfig.md) |
| 10 | `t_gsc_localpackconfigbus` | 业务对象分录-子表 | 7 | [gsc_localpackconfig.md](./gsc_localpackconfig.md) |
| 11 | `t_gsc_localpackconfigbus_l` | 业务对象分录-多语言表 | 5 | [gsc_localpackconfig.md](./gsc_localpackconfig.md) |
| 12 | `t_iprm_installlog` | 内容包加载日志-主表 | 13 | [iprm_installlog.md](./iprm_installlog.md) |
| 13 | `t_iprm_installlogentry` | 单据体-子表 | 14 | [iprm_installlog.md](./iprm_installlog.md) |
| 14 | `t_iprm_localcontent` | 本地内容-主表 | 5 | [iprm_localcontent.md](./iprm_localcontent.md) |
| 15 | `t_iprm_localcontent_l` | 本地内容-多语言表 | 4 | [iprm_localcontent.md](./iprm_localcontent.md) |
| 16 | `t_iprm_myresource` | 我的应用-主表 | 17 | [iprm_myresource.md](./iprm_myresource.md) |
| 17 | `t_iprm_parameter` | 云内容参数管理-主表 | 3 | [iprm_parameter.md](./iprm_parameter.md) |
| 18 | `t_iprm_res_country` | 国家/地区-主表 | 5 | [iprm_res_country.md](./iprm_res_country.md) |
| 19 | `t_iprm_res_country_l` | 国家/地区-多语言表 | 4 | [iprm_res_country.md](./iprm_res_country.md) |
| 20 | `t_iprm_res_itype` | 领域-主表 | 12 | [iprm_res_itype.md](./iprm_res_itype.md) |
| 21 | `t_iprm_res_itype_l` | 领域-多语言表 | 4 | [iprm_res_itype.md](./iprm_res_itype.md) |
| 22 | `t_iprm_res_rtype` | 行业-主表 | 11 | [iprm_res_rtype.md](./iprm_res_rtype.md) |
| 23 | `t_iprm_res_rtype_l` | 行业-多语言表 | 4 | [iprm_res_rtype.md](./iprm_res_rtype.md) |
| 24 | `t_iprm_res_supportlang` | 支持语言-主表 | 5 | [iprm_res_supportlang.md](./iprm_res_supportlang.md) |
| 25 | `t_iprm_res_supportlang_l` | 支持语言-多语言表 | 4 | [iprm_res_supportlang.md](./iprm_res_supportlang.md) |
| 26 | `t_iprm_res_ttype` | 主题-主表 | 13 | [iprm_res_ttype.md](./iprm_res_ttype.md) |
| 27 | `t_iprm_res_ttype_l` | 主题-多语言表 | 4 | [iprm_res_ttype.md](./iprm_res_ttype.md) |
| 28 | `t_iprm_resource` | 云内容（废弃）-主表 | 29 | [iprm_resource.md](./iprm_resource.md) |
| 29 | `t_iprm_resource` | 云内容-主表 | 29 | [iprm_resourcenew.md](./iprm_resourcenew.md) |
| 30 | `t_iprm_resource_entry` | 单据体-子表 | 7 | [iprm_resource.md](./iprm_resource.md) |
| 31 | `t_iprm_resource_entry` | 单据体-子表 | 7 | [iprm_resourcenew.md](./iprm_resourcenew.md) |
| 32 | `t_iprm_resourceinstall` | 内容包安装申请记录-主表 | 14 | [iprm_resourceinstalllist.md](./iprm_resourceinstalllist.md) |
