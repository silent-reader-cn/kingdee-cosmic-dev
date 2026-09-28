# plmipdsm 模块表清单

> 本模块共收录 **99** 张表定义，来自 `plmipdsm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope plmipdsm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `-` | IPD基础模型-使用范围表 plm_ipd_baseorg_u | 3 | [plm_ipd_base.md](./plm_ipd_base.md) |
| 2 | `-` | IPD基础模型-多语言表 plm_ipd_baseorg_l | 0 | [plm_ipd_base.md](./plm_ipd_base.md) |
| 3 | `-` | IPD基础模型-主表 plm_ipd_baseorg | 0 | [plm_ipd_base.md](./plm_ipd_base.md) |
| 4 | `t_deliverable_model_map` | 转换映射-子表 | 7 | [plm_ipdsm_fc_model.md](./plm_ipdsm_fc_model.md) |
| 5 | `t_deliverable_model_param` | 配置参数-子表 | 5 | [plm_ipdsm_fc_model.md](./plm_ipdsm_fc_model.md) |
| 6 | `t_ipd_contextual_cfgs` | 工作项上下文关系配置-主表 | 13 | [plm_ipd_contextual_cfgs.md](./plm_ipd_contextual_cfgs.md) |
| 7 | `t_ipd_lc_business_ctrl` | 单据体-子表 | 5 | [plm_ipdsm_lc_template.md](./plm_ipdsm_lc_template.md) |
| 8 | `t_ipd_lc_business_ctrl` | 单据体-子表 | 5 | [plm_ipdsm_lc_template_org.md](./plm_ipdsm_lc_template_org.md) |
| 9 | `t_ipd_lc_template` | 状态设置-主表 | 22 | [plm_ipdsm_lc_template.md](./plm_ipdsm_lc_template.md) |
| 10 | `t_ipd_lc_template` | 状态设置(组织受控)-主表 | 22 | [plm_ipdsm_lc_template_org.md](./plm_ipdsm_lc_template_org.md) |
| 11 | `t_ipd_lc_template_l` | 状态设置-多语言表 | 4 | [plm_ipdsm_lc_template.md](./plm_ipdsm_lc_template.md) |
| 12 | `t_ipd_lc_template_l` | 状态设置(组织受控)-多语言表 | 4 | [plm_ipdsm_lc_template_org.md](./plm_ipdsm_lc_template_org.md) |
| 13 | `t_ipd_lc_template_u` | 状态设置(组织受控)-使用范围表 | 3 | [plm_ipdsm_lc_template_org.md](./plm_ipdsm_lc_template_org.md) |
| 14 | `t_ipd_lc_tmpl_fstatus` | 源状态单据体-子表 | 6 | [plm_ipdsm_lc_template.md](./plm_ipdsm_lc_template.md) |
| 15 | `t_ipd_lc_tmpl_fstatus` | 源状态单据体-子表 | 6 | [plm_ipdsm_lc_template_org.md](./plm_ipdsm_lc_template_org.md) |
| 16 | `t_ipd_lc_tmpl_tostatus` | 目标状态子单据体-子表 | 7 | [plm_ipdsm_lc_template.md](./plm_ipdsm_lc_template.md) |
| 17 | `t_ipd_lc_tmpl_tostatus` | 目标状态子单据体-子表 | 7 | [plm_ipdsm_lc_template_org.md](./plm_ipdsm_lc_template_org.md) |
| 18 | `t_meta_mainentityinfo` | IPD主实体对象-主表 | 0 | [bos_entityobject_ipdext.md](./bos_entityobject_ipdext.md) |
| 19 | `t_meta_mainentityinfo_l` | IPD主实体对象-多语言表 | 0 | [bos_entityobject_ipdext.md](./bos_entityobject_ipdext.md) |
| 20 | `t_plm_ipd_contextual_ins` | 上下文实例数据表-主表 | 24 | [plm_ipd_contextual_ins.md](./plm_ipd_contextual_ins.md) |
| 21 | `t_plm_ipd_contextual_ins_s` | 上下文实例数据表-分表 | 3 | [plm_ipd_contextual_ins.md](./plm_ipd_contextual_ins.md) |
| 22 | `t_plm_ipd_description` | 描述大文本-主表 | 10 | [plm_ipd_description.md](./plm_ipd_description.md) |
| 23 | `t_plm_ipd_lc_status` | 状态-主表 | 25 | [plm_ipd_lc_status.md](./plm_ipd_lc_status.md) |
| 24 | `t_plm_ipd_lc_status` | 工作项状态-主表 | 25 | [plm_ipdsm_lc_status.md](./plm_ipdsm_lc_status.md) |
| 25 | `t_plm_ipd_lc_status_l` | 状态-多语言表 | 4 | [plm_ipd_lc_status.md](./plm_ipd_lc_status.md) |
| 26 | `t_plm_ipd_lc_status_l` | 工作项状态-多语言表 | 4 | [plm_ipdsm_lc_status.md](./plm_ipdsm_lc_status.md) |
| 27 | `t_plm_ipd_lc_status_u` | 状态-使用范围表 | 3 | [plm_ipd_lc_status.md](./plm_ipd_lc_status.md) |
| 28 | `t_plm_ipd_lc_status_u` | 工作项状态-使用范围表 | 3 | [plm_ipdsm_lc_status.md](./plm_ipdsm_lc_status.md) |
| 29 | `t_plm_ipd_mul_lc` | 状态-多选基础资料表 | 3 | [plm_ipdsm_lc_template.md](./plm_ipdsm_lc_template.md) |
| 30 | `t_plm_ipd_mul_lc` | 状态-多选基础资料表 | 3 | [plm_ipdsm_lc_template_org.md](./plm_ipdsm_lc_template_org.md) |
| 31 | `t_plm_ipd_prosettings` | 属性设置-主表 | 18 | [plm_ipditem_setting.md](./plm_ipditem_setting.md) |
| 32 | `t_plm_ipd_prosettings_l` | 属性设置-多语言表 | 4 | [plm_ipditem_setting.md](./plm_ipditem_setting.md) |
| 33 | `t_plm_ipddynamicattr` | 动态属性-主表 | 0 | [plm_ipddynamicattr.md](./plm_ipddynamicattr.md) |
| 34 | `t_plm_ipddynamicattr_l` | 动态属性-多语言表 | 0 | [plm_ipddynamicattr.md](./plm_ipddynamicattr.md) |
| 35 | `t_plm_ipditem` | 不带版本工作项-主表 | 0 | [plm_ipdnoversionitem.md](./plm_ipdnoversionitem.md) |
| 36 | `t_plm_ipditem` | 带版本工作项-主表 | 0 | [plm_ipdversionitem.md](./plm_ipdversionitem.md) |
| 37 | `t_plm_ipditem_l` | 不带版本工作项-多语言表 | 0 | [plm_ipdnoversionitem.md](./plm_ipdnoversionitem.md) |
| 38 | `t_plm_ipditem_l` | 带版本工作项-多语言表 | 0 | [plm_ipdversionitem.md](./plm_ipdversionitem.md) |
| 39 | `t_plm_ipditemgroup` | 工作项类型配置-主表 | 29 | [plm_ipditemgroup.md](./plm_ipditemgroup.md) |
| 40 | `t_plm_ipditemgroup_l` | 工作项类型配置-多语言表 | 6 | [plm_ipditemgroup.md](./plm_ipditemgroup.md) |
| 41 | `t_plm_ipditemgroup_u` | 工作项类型配置-使用范围表 | 3 | [plm_ipditemgroup.md](./plm_ipditemgroup.md) |
| 42 | `t_plm_ipditempic` | 工作项图标-主表 | 20 | [plm_ipditempic.md](./plm_ipditempic.md) |
| 43 | `t_plm_ipditempic_l` | 工作项图标-多语言表 | 4 | [plm_ipditempic.md](./plm_ipditempic.md) |
| 44 | `t_plm_ipditempic_u` | 工作项图标-使用范围表 | 3 | [plm_ipditempic.md](./plm_ipditempic.md) |
| 45 | `t_plm_ipdpagecfg` | IPD页面配置-主表 | 22 | [plm_ipdpagecfg.md](./plm_ipdpagecfg.md) |
| 46 | `t_plm_ipdpagecfg` | IPD页面配置_继承-主表 | 22 | [plm_ipdpagecfg_inh.md](./plm_ipdpagecfg_inh.md) |
| 47 | `t_plm_ipdpagecfg_l` | IPD页面配置-多语言表 | 4 | [plm_ipdpagecfg.md](./plm_ipdpagecfg.md) |
| 48 | `t_plm_ipdpagecfg_l` | IPD页面配置_继承-多语言表 | 4 | [plm_ipdpagecfg_inh.md](./plm_ipdpagecfg_inh.md) |
| 49 | `t_plm_ipdpagecfg_u` | IPD页面配置-使用范围表 | 3 | [plm_ipdpagecfg.md](./plm_ipdpagecfg.md) |
| 50 | `t_plm_ipdpagecfg_u` | IPD页面配置_继承-使用范围表 | 3 | [plm_ipdpagecfg_inh.md](./plm_ipdpagecfg_inh.md) |
| 51 | `t_plm_ipdpagecfgentry` | 单据体-子表 | 11 | [plm_ipdpagecfg.md](./plm_ipdpagecfg.md) |
| 52 | `t_plm_ipdpagecfgentry` | 单据体-子表 | 11 | [plm_ipdpagecfg_inh.md](./plm_ipdpagecfg_inh.md) |
| 53 | `t_plm_ipdpagecfgentry_l` | 单据体-多语言表 | 4 | [plm_ipdpagecfg.md](./plm_ipdpagecfg.md) |
| 54 | `t_plm_ipdpagecfgentry_l` | 单据体-多语言表 | 4 | [plm_ipdpagecfg_inh.md](./plm_ipdpagecfg_inh.md) |
| 55 | `t_plm_ipdpagecfgfield` | 子单据体-子表 | 8 | [plm_ipdpagecfg.md](./plm_ipdpagecfg.md) |
| 56 | `t_plm_ipdpagecfgfield` | 子单据体-子表 | 8 | [plm_ipdpagecfg_inh.md](./plm_ipdpagecfg_inh.md) |
| 57 | `t_plm_ipdsm_businessctrl` | 状态设置业务控制-主表 | 18 | [plm_ipdsm_businessctrl.md](./plm_ipdsm_businessctrl.md) |
| 58 | `t_plm_ipdsm_businessctrl_l` | 状态设置业务控制-多语言表 | 4 | [plm_ipdsm_businessctrl.md](./plm_ipdsm_businessctrl.md) |
| 59 | `t_plm_ipdsm_businessctrl_u` | 状态设置业务控制-使用范围表 | 3 | [plm_ipdsm_businessctrl.md](./plm_ipdsm_businessctrl.md) |
| 60 | `t_plm_ipdsm_ctx_shard` | 上下文分表配置-主表 | 2 | [plm_ipdsm_ctx_sharding.md](./plm_ipdsm_ctx_sharding.md) |
| 61 | `t_plm_ipdsm_ctx_shard_e` | 分表配置-子表 | 5 | [plm_ipdsm_ctx_sharding.md](./plm_ipdsm_ctx_sharding.md) |
| 62 | `t_plm_ipdsm_fc_cfg` | 关联项列表显示配置-主表 | 2 | [plm_ipdsm_fc_field_cfg.md](./plm_ipdsm_fc_field_cfg.md) |
| 63 | `t_plm_ipdsm_fc_cfg_e` | 字段配置-子表 | 8 | [plm_ipdsm_fc_field_cfg.md](./plm_ipdsm_fc_field_cfg.md) |
| 64 | `t_plm_ipdsm_fc_cfg_e_l` | 字段配置-多语言表 | 4 | [plm_ipdsm_fc_field_cfg.md](./plm_ipdsm_fc_field_cfg.md) |
| 65 | `t_plm_ipdsm_itemr_entry` | 关联项-子表 | 64 | [plm_ipdsm_itemrealtion.md](./plm_ipdsm_itemrealtion.md) |
| 66 | `t_plm_ipdsm_itemr_entry_l` | 关联项-多语言表 | 54 | [plm_ipdsm_itemrealtion.md](./plm_ipdsm_itemrealtion.md) |
| 67 | `t_plm_ipdsm_itemrealtion` | 关联项-主表 | 14 | [plm_ipdsm_itemrealtion.md](./plm_ipdsm_itemrealtion.md) |
| 68 | `t_plm_ipdsm_itemrealtion_l` | 关联项-多语言表 | 4 | [plm_ipdsm_itemrealtion.md](./plm_ipdsm_itemrealtion.md) |
| 69 | `t_plm_ipdsm_statustrans` | 状态转换规则配置-主表 | 15 | [plm_ipdsm_statustrans.md](./plm_ipdsm_statustrans.md) |
| 70 | `t_plm_pm_dataconverter` | 柔性容器数据转换器-主表 | 0 | [plm_ipdsm_fc_converter.md](./plm_ipdsm_fc_converter.md) |
| 71 | `t_plm_pm_dataconverter_l` | 柔性容器数据转换器-多语言表 | 0 | [plm_ipdsm_fc_converter.md](./plm_ipdsm_fc_converter.md) |
| 72 | `t_plm_pm_mappingstatus` | 关联状态-多选基础资料表 | 3 | [plm_ipdsm_fc_model.md](./plm_ipdsm_fc_model.md) |
| 73 | `t_plm_pm_projectattr` | 工作项类型设置-属性属性-主表 | 20 | [plm_ipditem_attr_setting.md](./plm_ipditem_attr_setting.md) |
| 74 | `t_plm_pm_projectattr_l` | 工作项类型设置-属性属性-多语言表 | 4 | [plm_ipditem_attr_setting.md](./plm_ipditem_attr_setting.md) |
| 75 | `t_plm_pm_projectattr_u` | 工作项类型设置-属性属性-使用范围表 | 3 | [plm_ipditem_attr_setting.md](./plm_ipditem_attr_setting.md) |
| 76 | `t_plm_pm_projectattrentry` | 单据体-子表 | 25 | [plm_ipditem_attr_setting.md](./plm_ipditem_attr_setting.md) |
| 77 | `t_plm_pm_projectattrentry_l` | 单据体-多语言表 | 4 | [plm_ipditem_attr_setting.md](./plm_ipditem_attr_setting.md) |
| 78 | `t_plm_pm_trd` | 集成应用配置-主表 | 23 | [plm_pm_trd.md](./plm_pm_trd.md) |
| 79 | `t_plm_pm_trd_auth` | 认证参数-子表 | 5 | [plm_pm_trd.md](./plm_pm_trd.md) |
| 80 | `t_plm_pm_trd_authtype` | 集成认证服务-主表 | 12 | [plm_pm_trd_authtype.md](./plm_pm_trd_authtype.md) |
| 81 | `t_plm_pm_trd_authtype_l` | 集成认证服务-多语言表 | 4 | [plm_pm_trd_authtype.md](./plm_pm_trd_authtype.md) |
| 82 | `t_plm_pm_trd_l` | 集成应用配置-多语言表 | 4 | [plm_pm_trd.md](./plm_pm_trd.md) |
| 83 | `t_plm_pm_trd_u` | 集成应用配置-使用范围表 | 3 | [plm_pm_trd.md](./plm_pm_trd.md) |
| 84 | `t_plmipdsm_fc_ent` | 数据实例-子表 | 69 | [plm_ipdsm_fc.md](./plm_ipdsm_fc.md) |
| 85 | `t_plmipdsm_fc_ent` | 数据实例-子表 | 69 | [plm_ipdsm_fc_base.md](./plm_ipdsm_fc_base.md) |
| 86 | `t_plmipdsm_fc_ent` | 数据实例-子表 | 69 | [plm_ipdsm_fc_base_inh.md](./plm_ipdsm_fc_base_inh.md) |
| 87 | `t_plmipdsm_fc_ent` | 数据实例-子表 | 69 | [plm_ipdsm_fc_inh_test.md](./plm_ipdsm_fc_inh_test.md) |
| 88 | `t_plmipdsm_fc_ent_l` | 数据实例-多语言表 | 55 | [plm_ipdsm_fc.md](./plm_ipdsm_fc.md) |
| 89 | `t_plmipdsm_fc_ent_l` | 数据实例-多语言表 | 55 | [plm_ipdsm_fc_inh_test.md](./plm_ipdsm_fc_inh_test.md) |
| 90 | `t_plmpm_deliverable` | 柔性容器-主表 | 17 | [plm_ipdsm_fc.md](./plm_ipdsm_fc.md) |
| 91 | `t_plmpm_deliverable` | 柔性容器-抽象-主表 | 17 | [plm_ipdsm_fc_base.md](./plm_ipdsm_fc_base.md) |
| 92 | `t_plmpm_deliverable` | 柔性容器-继承-主表 | 17 | [plm_ipdsm_fc_base_inh.md](./plm_ipdsm_fc_base_inh.md) |
| 93 | `t_plmpm_deliverable` | 柔性容器_继承升级测试-主表 | 17 | [plm_ipdsm_fc_inh_test.md](./plm_ipdsm_fc_inh_test.md) |
| 94 | `t_plmpm_deliverable_l` | 柔性容器-多语言表 | 4 | [plm_ipdsm_fc.md](./plm_ipdsm_fc.md) |
| 95 | `t_plmpm_deliverable_l` | 柔性容器-抽象-多语言表 | 4 | [plm_ipdsm_fc_base.md](./plm_ipdsm_fc_base.md) |
| 96 | `t_plmpm_deliverable_l` | 柔性容器-继承-多语言表 | 4 | [plm_ipdsm_fc_base_inh.md](./plm_ipdsm_fc_base_inh.md) |
| 97 | `t_plmpm_deliverable_l` | 柔性容器_继承升级测试-多语言表 | 4 | [plm_ipdsm_fc_inh_test.md](./plm_ipdsm_fc_inh_test.md) |
| 98 | `t_plmpm_deliverablemodel` | 关联项类型配置-主表 | 21 | [plm_ipdsm_fc_model.md](./plm_ipdsm_fc_model.md) |
| 99 | `t_plmpm_deliverablemodel_l` | 关联项类型配置-多语言表 | 5 | [plm_ipdsm_fc_model.md](./plm_ipdsm_fc_model.md) |
