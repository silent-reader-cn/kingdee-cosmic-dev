# privacy 模块表清单

> 本模块共收录 **26** 张表定义，来自 `privacy_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category privacy
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_privacy_blackfield` | 黑名单管理-主表 | 11 | [privacy_blackfield_manage.md](./privacy_blackfield_manage.md) |
| 2 | `t_privacy_blackfieldinfo` | 单据体-子表 | 7 | [privacy_blackfield_manage.md](./privacy_blackfield_manage.md) |
| 3 | `t_privacy_config_tpl` | 隐私方案配置_模板-主表 | 13 | [t_privacy_config_temp.md](./t_privacy_config_temp.md) |
| 4 | `t_privacy_config_tpl_l` | 隐私方案配置_模板-多语言表 | 4 | [t_privacy_config_temp.md](./t_privacy_config_temp.md) |
| 5 | `t_privacy_data_field_tpl` | 单据体-子表 | 16 | [privacy_data_tags_temp.md](./privacy_data_tags_temp.md) |
| 6 | `t_privacy_data_tag` | 数据安全标签-主表 | 9 | [privacy_data_tags.md](./privacy_data_tags.md) |
| 7 | `t_privacy_data_tag_fields` | 单据体-子表 | 16 | [privacy_data_tags.md](./privacy_data_tags.md) |
| 8 | `t_privacy_data_tag_l` | 数据安全标签-多语言表 | 4 | [privacy_data_tags.md](./privacy_data_tags.md) |
| 9 | `t_privacy_data_tag_tpl` | 数据安全标签模板-主表 | 9 | [privacy_data_tags_temp.md](./privacy_data_tags_temp.md) |
| 10 | `t_privacy_data_tag_tpl_l` | 数据安全标签模板-多语言表 | 4 | [privacy_data_tags_temp.md](./privacy_data_tags_temp.md) |
| 11 | `t_privacy_decrypt_control` | 字段解密控制-子表 | 10 | [t_privacy_scheme_config.md](./t_privacy_scheme_config.md) |
| 12 | `t_privacy_decrypt_receive` | 消息接收人-多选基础资料表 | 3 | [t_privacy_scheme_config.md](./t_privacy_scheme_config.md) |
| 13 | `t_privacy_desen_authority` | 脱敏权限设置-子表 | 11 | [t_privacy_scheme_config.md](./t_privacy_scheme_config.md) |
| 14 | `t_privacy_desen_rules` | 脱敏规则-主表 | 17 | [privacy_desen_rules.md](./privacy_desen_rules.md) |
| 15 | `t_privacy_desen_rules_l` | 脱敏规则-多语言表 | 5 | [privacy_desen_rules.md](./privacy_desen_rules.md) |
| 16 | `t_privacy_desen_tpl` | 脱敏规则模板-子表 | 21 | [t_privacy_config_temp.md](./t_privacy_config_temp.md) |
| 17 | `t_privacy_encrypt_tpl` | 加密规则模板-子表 | 20 | [t_privacy_config_temp.md](./t_privacy_config_temp.md) |
| 18 | `t_privacy_global_control` | 全局控制-主表 | 11 | [privacy_global_control.md](./privacy_global_control.md) |
| 19 | `t_privacy_global_receive` | 消息接收人-多选基础资料表 | 3 | [privacy_global_control.md](./privacy_global_control.md) |
| 20 | `t_privacy_scheme_config` | 隐私方案配置-主表 | 14 | [t_privacy_scheme_config.md](./t_privacy_scheme_config.md) |
| 21 | `t_privacy_scheme_config_l` | 隐私方案配置-多语言表 | 4 | [t_privacy_scheme_config.md](./t_privacy_scheme_config.md) |
| 22 | `t_privacy_scheme_desen` | 脱敏规则-子表 | 21 | [t_privacy_scheme_config.md](./t_privacy_scheme_config.md) |
| 23 | `t_privacy_scheme_encrypt` | 加密规则-子表 | 20 | [t_privacy_scheme_config.md](./t_privacy_scheme_config.md) |
| 24 | `t_privacy_scheme_permrole` | 角色-多选基础资料表 | 3 | [t_privacy_scheme_config.md](./t_privacy_scheme_config.md) |
| 25 | `t_privacy_scheme_permuser` | 用户-多选基础资料表 | 3 | [t_privacy_scheme_config.md](./t_privacy_scheme_config.md) |
| 26 | `t_privacy_task` | 数据处理-主表 | 32 | [t_privacy_task.md](./t_privacy_task.md) |
