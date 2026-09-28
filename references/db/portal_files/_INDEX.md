# portal 模块表清单

> 本模块共收录 **57** 张表定义，来自 `portal_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category portal
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bas_advancesetting` | 高级设置基础资料-主表 | 6 | [bd_advancesetting.md](./bd_advancesetting.md) |
| 2 | `t_bas_cardconfig` | 首页卡片配置信息-主表 | 7 | [bos_mainpagecardconfig.md](./bos_mainpagecardconfig.md) |
| 3 | `t_bas_cardconfig_l` | 首页卡片配置信息-多语言表 | 5 | [bos_mainpagecardconfig.md](./bos_mainpagecardconfig.md) |
| 4 | `t_bas_mainpagelayout` | 首页布局（即将废弃）-主表 | 22 | [bos_mainpagelayout.md](./bos_mainpagelayout.md) |
| 5 | `t_bas_mainpagelayout` | 首页方案-主表 | 22 | [portal_scheme.md](./portal_scheme.md) |
| 6 | `t_bas_mainpagelayout_l` | 首页方案-多语言表 | 4 | [portal_scheme.md](./portal_scheme.md) |
| 7 | `t_bas_mainpagelayoutgroup` | 方案与用户组关系-主表 | 3 | [protal_scheme_group_rel.md](./protal_scheme_group_rel.md) |
| 8 | `t_bas_mobile_app` | 星瀚应用-主表 | 7 | [mobile_light_app.md](./mobile_light_app.md) |
| 9 | `t_bas_mobile_app_l` | 星瀚应用-多语言表 | 4 | [mobile_light_app.md](./mobile_light_app.md) |
| 10 | `t_bas_orgmainpage` | 行政组织和首页方案关系-主表 | 3 | [bos_orgmainpage_rel.md](./bos_orgmainpage_rel.md) |
| 11 | `t_bas_portal_current_app` | 最近使用的应用-主表 | 8 | [bos_portal_current_app.md](./bos_portal_current_app.md) |
| 12 | `t_bas_portal_current_menu` | 最近使用菜单-主表 | 6 | [bos_portal_current_menu.md](./bos_portal_current_menu.md) |
| 13 | `t_bas_privacy_policy` | 隐私协议-主表 | 8 | [bos_privacy_policy.md](./bos_privacy_policy.md) |
| 14 | `t_bas_privacy_user_record` | 用户隐私记录-主表 | 8 | [bos_user_privacy_record.md](./bos_user_privacy_record.md) |
| 15 | `t_bas_rolesmainpage` | 方案与角色关系-主表 | 3 | [portal_scheme_roles_rel.md](./portal_scheme_roles_rel.md) |
| 16 | `t_bas_schemegroup` | 用户组-主表 | 15 | [portal_scheme_group.md](./portal_scheme_group.md) |
| 17 | `t_bas_schemegroup_l` | 用户组-多语言表 | 6 | [portal_scheme_group.md](./portal_scheme_group.md) |
| 18 | `t_bas_schemegroupuser` | 首页方案用户组-主表 | 3 | [portal_group_user_rel.md](./portal_group_user_rel.md) |
| 19 | `t_bas_shortcuts` | 快捷键基础资料-主表 | 15 | [bd_shortcuts.md](./bd_shortcuts.md) |
| 20 | `t_bas_shortcuts_l` | 快捷键基础资料-多语言表 | 5 | [bd_shortcuts.md](./bd_shortcuts.md) |
| 21 | `t_bas_thirdapps_config` | 轻应用集成平台连接配置-主表 | 11 | [bos_thirdapps_config.md](./bos_thirdapps_config.md) |
| 22 | `t_bas_user_paras_config` | 个人参数设置-主表 | 15 | [bos_user_params_config.md](./bos_user_params_config.md) |
| 23 | `t_bas_userfixedapp` | 用户锁定应用-主表 | 4 | [bos_portal_userfixedapp.md](./bos_portal_userfixedapp.md) |
| 24 | `t_bas_usermainpage` | 用户默认系统首页列表-主表 | 3 | [portal_scheme_user_rel.md](./portal_scheme_user_rel.md) |
| 25 | `t_bas_usermarkedmenus` | 用户收藏菜单-主表 | 6 | [portal_usermarkedmenu.md](./portal_usermarkedmenu.md) |
| 26 | `t_bas_usersmainpage` | 方案与人员关系-主表 | 3 | [portal_scheme_users_rel.md](./portal_scheme_users_rel.md) |
| 27 | `t_bas_usertypesmainpage` | 方案与人员类型关系-主表 | 3 | [portal_scheme_utypes_rel.md](./portal_scheme_utypes_rel.md) |
| 28 | `t_meta_appmainpersonal` | 应用首页个性化方案实体-主表 | 0 | [tenant_personal_appmain.md](./tenant_personal_appmain.md) |
| 29 | `t_meta_personalcard` | 卡片个性化实体-主表 | 0 | [bos_card_personalcard.md](./bos_card_personalcard.md) |
| 30 | `t_meta_personalcard_l` | 卡片个性化实体-多语言表 | 0 | [bos_card_personalcard.md](./bos_card_personalcard.md) |
| 31 | `t_meta_personalscheme` | 个性化方案实体-主表 | 0 | [tenant_personal_scheme.md](./tenant_personal_scheme.md) |
| 32 | `t_sec_user` | 方案用户-主表 | 40 | [portal_scheme_user.md](./portal_scheme_user.md) |
| 33 | `t_sec_user_l` | 方案用户-多语言表 | 5 | [portal_scheme_user.md](./portal_scheme_user.md) |
| 34 | `t_sec_user_u` | 方案用户-使用范围表 | 20 | [portal_scheme_user.md](./portal_scheme_user.md) |
| 35 | `t_svc_handwrittensign` | 手写签名-主表 | 7 | [bos_handwritten_sign.md](./bos_handwritten_sign.md) |
| 36 | `t_xk_cloud_icon` | 云图标-主表 | 13 | [xk_cloud_icon.md](./xk_cloud_icon.md) |
| 37 | `t_xk_cloud_icon_l` | 云图标-多语言表 | 4 | [xk_cloud_icon.md](./xk_cloud_icon.md) |
| 38 | `t_xk_fea_data` | 特性数据-主表 | 5 | [xkfeature_data.md](./xkfeature_data.md) |
| 39 | `t_xk_fea_know_rec` | 我已知悉记录-主表 | 4 | [xkiknow_rec.md](./xkiknow_rec.md) |
| 40 | `t_xk_switch_record` | 用户切换首页方案记录-主表 | 4 | [xkswitch_scheme_record.md](./xkswitch_scheme_record.md) |
| 41 | `t_xkbas_card` | 首页卡片-主表 | 17 | [xkportal_card.md](./xkportal_card.md) |
| 42 | `t_xkbas_card_app` | 所属应用-多选基础资料表 | 3 | [xkportal_card.md](./xkportal_card.md) |
| 43 | `t_xkbas_card_l` | 首页卡片-多语言表 | 5 | [xkportal_card.md](./xkportal_card.md) |
| 44 | `t_xkbas_card_org` | 组织单据体-子表 | 5 | [xkportal_card.md](./xkportal_card.md) |
| 45 | `t_xkbas_card_role` | 角色单据体-子表 | 5 | [xkportal_card.md](./xkportal_card.md) |
| 46 | `t_xkbas_card_user` | 用户单据体-子表 | 5 | [xkportal_card.md](./xkportal_card.md) |
| 47 | `t_xkbas_cardtype` | 卡片类型-主表 | 11 | [xkportal_cardtype.md](./xkportal_cardtype.md) |
| 48 | `t_xkbas_cardtype_l` | 卡片类型-多语言表 | 4 | [xkportal_cardtype.md](./xkportal_cardtype.md) |
| 49 | `t_xkbas_flowcard` | 流程图卡片信息-主表 | 0 | [xkportal_flowcard.md](./xkportal_flowcard.md) |
| 50 | `t_xkbas_flowcard_lang` | 单据体-子表 | 0 | [xkportal_flowcard.md](./xkportal_flowcard.md) |
| 51 | `t_xkbas_flowcard_lang_l` | 单据体-多语言表 | 0 | [xkportal_flowcard.md](./xkportal_flowcard.md) |
| 52 | `t_xkbos_customize_menu` | 自定义全功能菜单-主表 | 11 | [xkbos_customize_menu.md](./xkbos_customize_menu.md) |
| 53 | `t_xkbos_recently_menu` | 最近使用菜单-主表 | 10 | [xkbos_recently_menu.md](./xkbos_recently_menu.md) |
| 54 | `t_xkbos_search_menu` | 搜索菜单-主表 | 10 | [xkbos_search_menu.md](./xkbos_search_menu.md) |
| 55 | `t_xkportal_open_app` | 用户默认打开的应用工作台-主表 | 4 | [xkuser_open_app.md](./xkuser_open_app.md) |
| 56 | `t_xksys_workbench` | 登录工作台设置-主表 | 5 | [xksys_workbench_config.md](./xksys_workbench_config.md) |
| 57 | `t_xksys_workbench_config` | 单据体-子表 | 8 | [xksys_workbench_config.md](./xksys_workbench_config.md) |
