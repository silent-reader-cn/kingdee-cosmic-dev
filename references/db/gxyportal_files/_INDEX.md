# gxyportal 模块表清单

> 本模块共收录 **18** 张表定义，来自 `gxyportal_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category gxyportal
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bas_mainpagelayout` | 首页方案-主表 | 22 | [gxyportal_scheme.md](./gxyportal_scheme.md) |
| 2 | `t_bas_mainpagelayout_l` | 首页方案-多语言表 | 4 | [gxyportal_scheme.md](./gxyportal_scheme.md) |
| 3 | `t_bas_mainpagelayoutgroup` | 方案与用户组关系-主表 | 3 | [gxyprotal_scheme_group_re.md](./gxyprotal_scheme_group_re.md) |
| 4 | `t_bas_orgmainpage` | 行政组织和首页方案关系-主表 | 3 | [gxybos_orgmainpage_rel.md](./gxybos_orgmainpage_rel.md) |
| 5 | `t_bas_rolesmainpage` | 方案与角色关系-主表 | 3 | [gxyportal_scheme_roles_re.md](./gxyportal_scheme_roles_re.md) |
| 6 | `t_bas_schemegroup` | 用户组-主表 | 15 | [gxyportal_scheme_group.md](./gxyportal_scheme_group.md) |
| 7 | `t_bas_schemegroup_l` | 用户组-多语言表 | 6 | [gxyportal_scheme_group.md](./gxyportal_scheme_group.md) |
| 8 | `t_bas_schemegroupuser` | 首页方案用户组-主表 | 3 | [gxyportal_group_user_rel.md](./gxyportal_group_user_rel.md) |
| 9 | `t_bas_usermainpage` | 用户默认系统首页列表-主表 | 3 | [gxyportal_scheme_user_rel.md](./gxyportal_scheme_user_rel.md) |
| 10 | `t_bas_usersmainpage` | 方案与人员关系-主表 | 3 | [gxyportal_scheme_users_re.md](./gxyportal_scheme_users_re.md) |
| 11 | `t_bas_usertypesmainpage` | 方案与人员类型关系-主表 | 3 | [gxyportal_scheme_uty_rel.md](./gxyportal_scheme_uty_rel.md) |
| 12 | `t_gxy_ai_assigent` | 首页AI助手配置-主表 | 21 | [gxy_ai_assigent.md](./gxy_ai_assigent.md) |
| 13 | `t_gxy_ai_assigent_l` | 首页AI助手配置-多语言表 | 5 | [gxy_ai_assigent.md](./gxy_ai_assigent.md) |
| 14 | `t_gxy_ai_assigentlink` | 单据体-子表 | 8 | [gxy_ai_assigent.md](./gxy_ai_assigent.md) |
| 15 | `t_sec_user` | 方案用户-主表 | 57 | [gxyportal_scheme_user.md](./gxyportal_scheme_user.md) |
| 16 | `t_sec_user_l` | 方案用户-多语言表 | 5 | [gxyportal_scheme_user.md](./gxyportal_scheme_user.md) |
| 17 | `t_sec_user_u` | 方案用户-使用范围表 | 20 | [gxyportal_scheme_user.md](./gxyportal_scheme_user.md) |
| 18 | `t_xkportal_upnotification` | 升级通知消息-主表 | 15 | [gxyportal_upnotification.md](./gxyportal_upnotification.md) |
