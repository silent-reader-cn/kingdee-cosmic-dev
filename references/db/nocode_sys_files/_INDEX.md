# nocode_sys 模块表清单

> 本模块共收录 **40** 张表定义，来自 `nocode_sys_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category nocode_sys
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_nc_reftable` | 表格引用关系-主表 | 3 | [bos_nc_reftable.md](./bos_nc_reftable.md) |
| 2 | `t_nocode_association` | 表单双向关联关系-主表 | 5 | [bos_nocode_association.md](./bos_nocode_association.md) |
| 3 | `t_nocode_card` | 工作台卡片-主表 | 12 | [bos_nocode_card.md](./bos_nocode_card.md) |
| 4 | `t_nocode_card_orgauth` | 卡片库组织权限-主表 | 3 | [bos_nocode_card_orgauth.md](./bos_nocode_card_orgauth.md) |
| 5 | `t_nocode_card_userauth` | 卡片库用户权限-主表 | 3 | [bos_nocode_card_userauth.md](./bos_nocode_card_userauth.md) |
| 6 | `t_nocode_cardcollect` | 卡片收藏-主表 | 3 | [bos_nocode_cardcollect.md](./bos_nocode_cardcollect.md) |
| 7 | `t_nocode_cardcontainer` | 卡片容器-主表 | 9 | [bos_nocode_cardcontainer.md](./bos_nocode_cardcontainer.md) |
| 8 | `t_nocode_cardref` | 卡片引用-主表 | 7 | [bos_nocode_cardref.md](./bos_nocode_cardref.md) |
| 9 | `t_nocode_cardsch_active` | 卡片视图用户激活-主表 | 0 | [bos_nc_cardsch_active.md](./bos_nc_cardsch_active.md) |
| 10 | `t_nocode_cardsch_orgauth` | 卡片视图授权组织-主表 | 0 | [bos_nc_cardschema_orgauth.md](./bos_nc_cardschema_orgauth.md) |
| 11 | `t_nocode_cardsch_userauth` | 卡片视图用户权限-主表 | 0 | [bos_nc_cardsch_userauth.md](./bos_nc_cardsch_userauth.md) |
| 12 | `t_nocode_cardschema` | 工作台视图-主表 | 6 | [bos_nocode_cardschema.md](./bos_nocode_cardschema.md) |
| 13 | `t_nocode_export_record` | 单据列表导出记录-主表 | 8 | [bos_nocode_export_record.md](./bos_nocode_export_record.md) |
| 14 | `t_nocode_filterconfig` | 筛选项配置-主表 | 9 | [bos_nocode_filterconfig.md](./bos_nocode_filterconfig.md) |
| 15 | `t_nocode_form_auth` | 表单授权-主表 | 12 | [bos_nocode_form_auth.md](./bos_nocode_form_auth.md) |
| 16 | `t_nocode_forminfo_alias` | 表单信息别名-主表 | 8 | [bos_nc_forminfo_alias.md](./bos_nc_forminfo_alias.md) |
| 17 | `t_nocode_list_config` | 表单列表配置项-主表 | 6 | [bos_nocode_list_config.md](./bos_nocode_list_config.md) |
| 18 | `t_nocode_list_order` | 表头排序配置-主表 | 5 | [bos_nocode_list_order.md](./bos_nocode_list_order.md) |
| 19 | `t_nocode_list_schema` | 表单列表视图-主表 | 17 | [bos_nocode_list_schema.md](./bos_nocode_list_schema.md) |
| 20 | `t_nocode_pageinfo` | 表单列表分页信息-主表 | 5 | [bos_nocode_pageinfo.md](./bos_nocode_pageinfo.md) |
| 21 | `t_nocode_ruleconfig` | 规则配置-主表 | 13 | [bos_nocode_rule.md](./bos_nocode_rule.md) |
| 22 | `t_nocode_share` | 无代码分享-主表 | 9 | [bos_nocode_share.md](./bos_nocode_share.md) |
| 23 | `t_nocode_share_input` | 无代码分享表单记录-主表 | 4 | [bos_nocode_share_record.md](./bos_nocode_share_record.md) |
| 24 | `t_nocode_stat_card` | 统计卡片-主表 | 7 | [bos_nocode_stat_card.md](./bos_nocode_stat_card.md) |
| 25 | `t_nocode_statconfig` | 列表统计项-主表 | 9 | [bos_nocode_statconfig.md](./bos_nocode_statconfig.md) |
| 26 | `t_nocode_statschema` | 统计卡片和视图映射-主表 | 5 | [bos_nc_statschema.md](./bos_nc_statschema.md) |
| 27 | `t_nocode_tdomains` | 模板领域-主表 | 2 | [bos_nocode_tdomains.md](./bos_nocode_tdomains.md) |
| 28 | `t_nocode_template_config` | 模板配置-主表 | 15 | [bos_nocode_templateconfig.md](./bos_nocode_templateconfig.md) |
| 29 | `t_nocode_template_domain` | 领域-多选基础资料表 | 3 | [bos_nocode_templateconfig.md](./bos_nocode_templateconfig.md) |
| 30 | `t_nocode_template_trade` | 行业-多选基础资料表 | 3 | [bos_nocode_templateconfig.md](./bos_nocode_templateconfig.md) |
| 31 | `t_nocode_theme_config` | 个人主题配置-主表 | 3 | [bos_nocode_theme_config.md](./bos_nocode_theme_config.md) |
| 32 | `t_nocode_tmpform` | 流程实例运行时表单-主表 | 3 | [bos_nocode_tmpform.md](./bos_nocode_tmpform.md) |
| 33 | `t_nocode_tpl_comment` | 模板评价-主表 | 6 | [bos_nocode_tpl_comment.md](./bos_nocode_tpl_comment.md) |
| 34 | `t_nocode_tpl_orgauth` | 模板组织权限-主表 | 3 | [bos_nocode_tpl_org.md](./bos_nocode_tpl_org.md) |
| 35 | `t_nocode_tpl_userauth` | 模板用户权限-主表 | 3 | [bos_nocode_tpl_user.md](./bos_nocode_tpl_user.md) |
| 36 | `t_nocode_ttrades` | 模板行业-主表 | 2 | [bos_nocode_ttrades.md](./bos_nocode_ttrades.md) |
| 37 | `t_nocode_userlog` | 用户行为-主表 | 6 | [bos_nocode_userlog.md](./bos_nocode_userlog.md) |
| 38 | `t_nocode_userschema` | 用户视图中间表-主表 | 6 | [bos_nocode_userschema.md](./bos_nocode_userschema.md) |
| 39 | `t_nocode_wfinfo_alias` | 流程信息别名-主表 | 5 | [bos_nc_wfinfo_alias.md](./bos_nc_wfinfo_alias.md) |
| 40 | `t_nocode_wuserschema` | 工作台视图和用户关系表-主表 | 5 | [bos_nocode_wuserschema.md](./bos_nocode_wuserschema.md) |
