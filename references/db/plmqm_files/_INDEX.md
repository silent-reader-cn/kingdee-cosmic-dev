# plmqm 模块表清单

> 本模块共收录 **27** 张表定义，来自 `plmqm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category plmqm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ipd_lc_business_ctrl` | 单据体-子表 | 5 | [plm_qm_template.md](./plm_qm_template.md) |
| 2 | `t_ipd_lc_template` | 问题状态设置-主表 | 25 | [plm_qm_template.md](./plm_qm_template.md) |
| 3 | `t_ipd_lc_template_l` | 问题状态设置-多语言表 | 4 | [plm_qm_template.md](./plm_qm_template.md) |
| 4 | `t_ipd_lc_tmpl_fstatus` | 源状态单据体-子表 | 6 | [plm_qm_template.md](./plm_qm_template.md) |
| 5 | `t_ipd_lc_tmpl_tostatus` | 目标状态子单据体-子表 | 7 | [plm_qm_template.md](./plm_qm_template.md) |
| 6 | `t_plm_ipd_excludetype` | 排除分类-多选基础资料表 | 3 | [plm_qm_group.md](./plm_qm_group.md) |
| 7 | `t_plm_ipd_lc_status` | 问题状态-主表 | 26 | [plm_qm_lc_status.md](./plm_qm_lc_status.md) |
| 8 | `t_plm_ipd_lc_status_l` | 问题状态-多语言表 | 4 | [plm_qm_lc_status.md](./plm_qm_lc_status.md) |
| 9 | `t_plm_ipd_lc_status_u` | 问题状态-使用范围表 | 3 | [plm_qm_lc_status.md](./plm_qm_lc_status.md) |
| 10 | `t_plm_ipd_mul_lc` | 状态-多选基础资料表 | 3 | [plm_qm_template.md](./plm_qm_template.md) |
| 11 | `t_plm_ipd_prosettings` | 属性设置-主表 | 18 | [plm_qm_setting_attr_tab.md](./plm_qm_setting_attr_tab.md) |
| 12 | `t_plm_ipd_prosettings_l` | 属性设置-多语言表 | 4 | [plm_qm_setting_attr_tab.md](./plm_qm_setting_attr_tab.md) |
| 13 | `t_plm_ipditembaseinfo_lk` | 关联子实体-子表 | 6 | [plm_qm_baseinfo.md](./plm_qm_baseinfo.md) |
| 14 | `t_plm_ipditemgroup` | 问题分类-主表 | 32 | [plm_qm_group.md](./plm_qm_group.md) |
| 15 | `t_plm_ipditemgroup_l` | 问题分类-多语言表 | 6 | [plm_qm_group.md](./plm_qm_group.md) |
| 16 | `t_plm_ipditemgroup_u` | 问题分类-使用范围表 | 3 | [plm_qm_group.md](./plm_qm_group.md) |
| 17 | `t_plm_pm_projectattr` | 问题属性设置-主表 | 20 | [plm_qm_setting_attr.md](./plm_qm_setting_attr.md) |
| 18 | `t_plm_pm_projectattr_l` | 问题属性设置-多语言表 | 4 | [plm_qm_setting_attr.md](./plm_qm_setting_attr.md) |
| 19 | `t_plm_pm_projectattr_u` | 问题属性设置-使用范围表 | 3 | [plm_qm_setting_attr.md](./plm_qm_setting_attr.md) |
| 20 | `t_plm_pm_projectattrentry` | 单据体-子表 | 27 | [plm_qm_setting_attr.md](./plm_qm_setting_attr.md) |
| 21 | `t_plm_pm_projectattrentry_l` | 单据体-多语言表 | 4 | [plm_qm_setting_attr.md](./plm_qm_setting_attr.md) |
| 22 | `t_plm_qm_baseinfo` | 问题-主表 | 48 | [plm_qm_baseinfo.md](./plm_qm_baseinfo.md) |
| 23 | `t_plm_qm_baseinfo_l` | 问题-多语言表 | 4 | [plm_qm_baseinfo.md](./plm_qm_baseinfo.md) |
| 24 | `t_plm_qm_baseinfo_u` | 问题-使用范围表 | 3 | [plm_qm_baseinfo.md](./plm_qm_baseinfo.md) |
| 25 | `t_plm_qm_handlers` | 流程处理人-多选基础资料表 | 3 | [plm_qm_baseinfo.md](./plm_qm_baseinfo.md) |
| 26 | `t_plm_qm_warn_setting` | 问题升级预警配置-主表 | 12 | [plm_qm_warn_setting.md](./plm_qm_warn_setting.md) |
| 27 | `t_plm_rm_chargeperson` | 负责人-多选基础资料表 | 3 | [plm_qm_baseinfo.md](./plm_qm_baseinfo.md) |
