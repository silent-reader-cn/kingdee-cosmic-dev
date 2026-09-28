# fsa 模块表清单

> 本模块共收录 **65** 张表定义，来自 `fsa_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category fsa
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fsa_datacolcombfields` | 数据集合-组合字段-子表 | 7 | [fsa_data_collection.md](./fsa_data_collection.md) |
| 2 | `t_fsa_datacolcombmappings` | 组合字段的映射关系分录-子表 | 8 | [fsa_data_collection.md](./fsa_data_collection.md) |
| 3 | `t_fsa_datacolfieldparam` | 字段参数设置子分录-子表 | 5 | [fsa_data_collection.md](./fsa_data_collection.md) |
| 4 | `t_fsa_datacolfields` | 数据集合单据体-子表 | 11 | [fsa_data_collection.md](./fsa_data_collection.md) |
| 5 | `t_fsa_datacollection` | 数据集合-主表 | 17 | [fsa_data_collection.md](./fsa_data_collection.md) |
| 6 | `t_fsa_datacollection_l` | 数据集合-多语言表 | 4 | [fsa_data_collection.md](./fsa_data_collection.md) |
| 7 | `t_fsa_datacolsrcfilter` | 源字段集合-子表 | 9 | [fsa_data_collection.md](./fsa_data_collection.md) |
| 8 | `t_fsa_dataversion` | 数据版本-主表 | 9 | [fsa_dataversion.md](./fsa_dataversion.md) |
| 9 | `t_fsa_dstoryscheme` | 数据方案设置-主表 | 11 | [fsa_data_scheme.md](./fsa_data_scheme.md) |
| 10 | `t_fsa_dstoryscheme_l` | 数据方案设置-多语言表 | 4 | [fsa_data_scheme.md](./fsa_data_scheme.md) |
| 11 | `t_fsa_dstoryschemeent` | 可用数据单据体-子表 | 8 | [fsa_data_scheme.md](./fsa_data_scheme.md) |
| 12 | `t_fsa_dsyncparam` | 同步参数设置-主表 | 16 | [fsa_syncparam.md](./fsa_syncparam.md) |
| 13 | `t_fsa_dsyncparam_l` | 同步参数设置-多语言表 | 4 | [fsa_syncparam.md](./fsa_syncparam.md) |
| 14 | `t_fsa_dsyncparamdiment` | 维度分录-子表 | 8 | [fsa_syncparam.md](./fsa_syncparam.md) |
| 15 | `t_fsa_dsyncparamdimmement` | 维度过滤条件子分录-子表 | 7 | [fsa_syncparam.md](./fsa_syncparam.md) |
| 16 | `t_fsa_dv_filterfields` | 过滤字段-子表 | 7 | [fsa_dataversion.md](./fsa_dataversion.md) |
| 17 | `t_fsa_dv_filtermembers` | 过滤成员-子表 | 7 | [fsa_dataversion.md](./fsa_dataversion.md) |
| 18 | `t_fsa_history_set` | 历史设置版本-主表 | 9 | [fsa_history_set.md](./fsa_history_set.md) |
| 19 | `t_fsa_outputfields` | 数据集合子单据体-子表 | 10 | [fsa_data_scheme.md](./fsa_data_scheme.md) |
| 20 | `t_fsa_paramgroup` | 参数分组-主表 | 13 | [fsa_paramgroup.md](./fsa_paramgroup.md) |
| 21 | `t_fsa_paramgroup_l` | 参数分组-多语言表 | 5 | [fsa_paramgroup.md](./fsa_paramgroup.md) |
| 22 | `t_fsa_paramtemplate` | 数据参数模板-主表 | 11 | [fsa_paramtemplate.md](./fsa_paramtemplate.md) |
| 23 | `t_fsa_paramtemplate_l` | 数据参数模板-多语言表 | 4 | [fsa_paramtemplate.md](./fsa_paramtemplate.md) |
| 24 | `t_fsa_paramtemplateentry` | 参数项分录-子表 | 17 | [fsa_paramtemplate.md](./fsa_paramtemplate.md) |
| 25 | `t_fsa_rptacctdim` | 报表的科目维度信息-主表 | 0 | [fsa_rptacctdim.md](./fsa_rptacctdim.md) |
| 26 | `t_fsa_rptacctdim_l` | 报表的科目维度信息-多语言表 | 0 | [fsa_rptacctdim.md](./fsa_rptacctdim.md) |
| 27 | `t_fsa_rptbalance` | 资产负债表-主表 | 9 | [fsa_rptbalance.md](./fsa_rptbalance.md) |
| 28 | `t_fsa_rptbalance_config` | 资产负债表方案配置-主表 | 0 | [fsa_rptbalance_config.md](./fsa_rptbalance_config.md) |
| 29 | `t_fsa_rptbasedim` | 报表基础维度组信息-主表 | 0 | [fsa_rptbasedim.md](./fsa_rptbasedim.md) |
| 30 | `t_fsa_rptcashflow` | 现金流量表-主表 | 9 | [fsa_rptcashflow.md](./fsa_rptcashflow.md) |
| 31 | `t_fsa_rptdatasynclog` | 任务日志-主表 | 15 | [fsa_rptdata_synclog.md](./fsa_rptdata_synclog.md) |
| 32 | `t_fsa_rptdatasyncparam` | 同步参数-主表 | 12 | [fsa_rptdatasyncparam.md](./fsa_rptdatasyncparam.md) |
| 33 | `t_fsa_rptdatasyncparam_l` | 同步参数-多语言表 | 4 | [fsa_rptdatasyncparam.md](./fsa_rptdatasyncparam.md) |
| 34 | `t_fsa_rptdatasyncparament` | 同步参数分录-子表 | 5 | [fsa_rptdatasyncparam.md](./fsa_rptdatasyncparam.md) |
| 35 | `t_fsa_rptdatasynctask` | 任务列表-主表 | 11 | [fsa_rptdata_synctask.md](./fsa_rptdata_synctask.md) |
| 36 | `t_fsa_rptfacts` | 报表事实值信息-主表 | 0 | [fsa_rptfacts.md](./fsa_rptfacts.md) |
| 37 | `t_fsa_rptidxfacts` | 报表指标-主表 | 9 | [fsa_rptidxfacts.md](./fsa_rptidxfacts.md) |
| 38 | `t_fsa_rptidxrptent` | 单据体-子表 | 4 | [fsa_rptindicators.md](./fsa_rptindicators.md) |
| 39 | `t_fsa_rptincomestat` | 利润表-主表 | 9 | [fsa_rptincomestat.md](./fsa_rptincomestat.md) |
| 40 | `t_fsa_rptindicators` | 报表指标定义-主表 | 18 | [fsa_rptindicators.md](./fsa_rptindicators.md) |
| 41 | `t_fsa_rptindicators_l` | 报表指标定义-多语言表 | 4 | [fsa_rptindicators.md](./fsa_rptindicators.md) |
| 42 | `t_fsa_rptitems` | 标准报表项目-主表 | 14 | [fsa_rptitems.md](./fsa_rptitems.md) |
| 43 | `t_fsa_rptitems_l` | 标准报表项目-多语言表 | 4 | [fsa_rptitems.md](./fsa_rptitems.md) |
| 44 | `t_fsa_rptmappingent` | 报表映射分录信息-子表 | 11 | [fsa_rptmappings.md](./fsa_rptmappings.md) |
| 45 | `t_fsa_rptmappings` | 映射报表-主表 | 16 | [fsa_rptmappings.md](./fsa_rptmappings.md) |
| 46 | `t_fsa_rptmappings_l` | 映射报表-多语言表 | 4 | [fsa_rptmappings.md](./fsa_rptmappings.md) |
| 47 | `t_fsa_rptschema_config` | 报表方案配置-主表 | 0 | [fsa_rptschema_config.md](./fsa_rptschema_config.md) |
| 48 | `t_fsa_rptschema_config_l` | 报表方案配置-多语言表 | 0 | [fsa_rptschema_config.md](./fsa_rptschema_config.md) |
| 49 | `t_fsa_rptschema_indicator` | 指标名称-多选基础资料表 | 0 | [fsa_rptschema_config.md](./fsa_rptschema_config.md) |
| 50 | `t_fsa_rptscheme_config` | 报表方案配置-主表 | 14 | [fsa_rptscheme_config.md](./fsa_rptscheme_config.md) |
| 51 | `t_fsa_rptscheme_config_l` | 报表方案配置-多语言表 | 4 | [fsa_rptscheme_config.md](./fsa_rptscheme_config.md) |
| 52 | `t_fsa_scheme_pattern` | 用户数据权限-子表 | 10 | [fsa_rptscheme_config.md](./fsa_rptscheme_config.md) |
| 53 | `t_fsa_schtaskconfig` | 定时任务设置-主表 | 25 | [fsa_scheduletaskconfig.md](./fsa_scheduletaskconfig.md) |
| 54 | `t_fsa_schtaskconfig_l` | 定时任务设置-多语言表 | 4 | [fsa_scheduletaskconfig.md](./fsa_scheduletaskconfig.md) |
| 55 | `t_fsa_schtaskconfig_n` | 定时任务设置-分表 | 7 | [fsa_scheduletaskconfig.md](./fsa_scheduletaskconfig.md) |
| 56 | `t_fsa_schtaskentity` | 任务设置分录-子表 | 9 | [fsa_scheduletaskconfig.md](./fsa_scheduletaskconfig.md) |
| 57 | `t_fsa_schtasktime` | 预计执行时间分录-子表 | 6 | [fsa_scheduletaskconfig.md](./fsa_scheduletaskconfig.md) |
| 58 | `t_fsa_schtasktimesub` | 维度过滤条件分录-子表 | 9 | [fsa_scheduletaskconfig.md](./fsa_scheduletaskconfig.md) |
| 59 | `t_fsa_stdrptent` | 包含报表项单据体-子表 | 12 | [fsa_stdrpts.md](./fsa_stdrpts.md) |
| 60 | `t_fsa_stdrpts` | 标准报表-主表 | 10 | [fsa_stdrpts.md](./fsa_stdrpts.md) |
| 61 | `t_fsa_stdrpts_l` | 标准报表-多语言表 | 4 | [fsa_stdrpts.md](./fsa_stdrpts.md) |
| 62 | `t_fsa_task_config` | 系统参数配置-主表 | 11 | [fsa_task_control_config.md](./fsa_task_control_config.md) |
| 63 | `t_fsa_task_config_l` | 系统参数配置-多语言表 | 4 | [fsa_task_control_config.md](./fsa_task_control_config.md) |
| 64 | `t_gdt_fieldsparamdict` | 字段属性设置-主表 | 0 | [gdt_setting_param.md](./gdt_setting_param.md) |
| 65 | `t_gdt_fieldsparamdict_l` | 字段属性设置-多语言表 | 0 | [gdt_setting_param.md](./gdt_setting_param.md) |
