# osr 模块表清单

> 本模块共收录 **59** 张表定义，来自 `osr_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category osr
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_osr_appfilterscheme` | 应用过滤方案-主表 | 15 | [osr_appfilterscheme.md](./osr_appfilterscheme.md) |
| 2 | `t_osr_appfilterscheme_l` | 应用过滤方案-多语言表 | 4 | [osr_appfilterscheme.md](./osr_appfilterscheme.md) |
| 3 | `t_osr_displayschemekit` | 显示方案套件-主表 | 15 | [osr_displayschemekit.md](./osr_displayschemekit.md) |
| 4 | `t_osr_displayschemekit_l` | 显示方案套件-多语言表 | 4 | [osr_displayschemekit.md](./osr_displayschemekit.md) |
| 5 | `t_osr_dispschbiztype` | 界面显示方案业务类型-主表 | 21 | [osr_dispschemebiztype.md](./osr_dispschemebiztype.md) |
| 6 | `t_osr_dispschbiztype_c` | 配置项单据体-子表 | 9 | [osr_dispschemebiztype.md](./osr_dispschemebiztype.md) |
| 7 | `t_osr_dispschbiztype_c_l` | 配置项单据体-多语言表 | 7 | [osr_dispschemebiztype.md](./osr_dispschemebiztype.md) |
| 8 | `t_osr_dispschbiztype_l` | 界面显示方案业务类型-多语言表 | 4 | [osr_dispschemebiztype.md](./osr_dispschemebiztype.md) |
| 9 | `t_osr_dispschbiztype_p` | 依赖许可单据体-子表 | 13 | [osr_dispschemebiztype.md](./osr_dispschemebiztype.md) |
| 10 | `t_osr_dispschbiztype_p_l` | 依赖许可单据体-多语言表 | 7 | [osr_dispschemebiztype.md](./osr_dispschemebiztype.md) |
| 11 | `t_osr_dispscheme` | 界面显示方案-主表 | 21 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 12 | `t_osr_dispscheme` | （废弃）平板工序报工显示方案-主表 | 21 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 13 | `t_osr_dispscheme_entry` | 列表字段配置单据体-子表 | 18 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 14 | `t_osr_dispscheme_entry` | 列表字段配置单据体-子表 | 18 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 15 | `t_osr_dispscheme_entry_l` | 列表字段配置单据体-多语言表 | 9 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 16 | `t_osr_dispscheme_entry_l` | 列表字段配置单据体-多语言表 | 9 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 17 | `t_osr_dispscheme_entrya` | 区域显示配置分录-子表 | 9 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 18 | `t_osr_dispscheme_entrya` | 区域显示配置分录-子表 | 9 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 19 | `t_osr_dispscheme_entrya_l` | 区域显示配置分录-多语言表 | 5 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 20 | `t_osr_dispscheme_entrya_l` | 区域显示配置分录-多语言表 | 5 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 21 | `t_osr_dispscheme_entryc` | 配置项单据体-子表 | 10 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 22 | `t_osr_dispscheme_entryc` | 配置项单据体-子表 | 10 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 23 | `t_osr_dispscheme_entryd` | 详情字段配置单据体-子表 | 18 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 24 | `t_osr_dispscheme_entryd` | 详情字段配置单据体-子表 | 18 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 25 | `t_osr_dispscheme_entryd_l` | 详情字段配置单据体-多语言表 | 9 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 26 | `t_osr_dispscheme_entryd_l` | 详情字段配置单据体-多语言表 | 9 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 27 | `t_osr_dispscheme_entrye` | 编辑页面配置分录-子表 | 12 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 28 | `t_osr_dispscheme_entrye` | 编辑页面配置分录-子表 | 12 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 29 | `t_osr_dispscheme_entrye_l` | 编辑页面配置分录-多语言表 | 6 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 30 | `t_osr_dispscheme_entrye_l` | 编辑页面配置分录-多语言表 | 6 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 31 | `t_osr_dispscheme_entryop` | 功能按钮配置分录-子表 | 15 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 32 | `t_osr_dispscheme_entryop` | 功能按钮配置分录-子表 | 15 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 33 | `t_osr_dispscheme_entryop_l` | 功能按钮配置分录-多语言表 | 6 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 34 | `t_osr_dispscheme_entryop_l` | 功能按钮配置分录-多语言表 | 6 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 35 | `t_osr_dispscheme_l` | 界面显示方案-多语言表 | 4 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 36 | `t_osr_dispscheme_l` | （废弃）平板工序报工显示方案-多语言表 | 4 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 37 | `t_osr_dispscheme_org` | 适用车间-多选基础资料表 | 3 | [osr_displayscheme.md](./osr_displayscheme.md) |
| 38 | `t_osr_dispscheme_org` | 适用车间-多选基础资料表 | 3 | [osr_pad_psreport_scheme.md](./osr_pad_psreport_scheme.md) |
| 39 | `t_osr_dispschemekit_org` | 适用车间-多选基础资料表 | 3 | [osr_displayschemekit.md](./osr_displayschemekit.md) |
| 40 | `t_osr_dispschmapping` | 显示配置布局映射-主表 | 10 | [osr_dispschememapping.md](./osr_dispschememapping.md) |
| 41 | `t_osr_dispschmapping_e` | 编辑表单-多选基础资料表 | 3 | [osr_dispschememapping.md](./osr_dispschememapping.md) |
| 42 | `t_osr_dispschmappinge` | 业务类型映射单据体-子表 | 6 | [osr_dispschememapping.md](./osr_dispschememapping.md) |
| 43 | `t_osr_fctionconfig` | 平板首页功能-主表 | 18 | [osr_pad_functionconfig.md](./osr_pad_functionconfig.md) |
| 44 | `t_osr_fctionconfig_l` | 平板首页功能-多语言表 | 4 | [osr_pad_functionconfig.md](./osr_pad_functionconfig.md) |
| 45 | `t_osr_hfuncgroup` | 平板功能分组-主表 | 15 | [osr_pad_homefuncgroups.md](./osr_pad_homefuncgroups.md) |
| 46 | `t_osr_hfuncgroup_l` | 平板功能分组-多语言表 | 5 | [osr_pad_homefuncgroups.md](./osr_pad_homefuncgroups.md) |
| 47 | `t_osr_homeconfig` | 首页界面显示方案-主表 | 12 | [osr_pad_displayscheme.md](./osr_pad_displayscheme.md) |
| 48 | `t_osr_homeconfig_entry` | 主页配置-子表 | 8 | [osr_pad_displayscheme.md](./osr_pad_displayscheme.md) |
| 49 | `t_osr_homeconfig_entry_l` | 主页配置-多语言表 | 4 | [osr_pad_displayscheme.md](./osr_pad_displayscheme.md) |
| 50 | `t_osr_homeconfig_l` | 首页界面显示方案-多语言表 | 4 | [osr_pad_displayscheme.md](./osr_pad_displayscheme.md) |
| 51 | `t_osr_homeconfig_org` | 适用车间-多选基础资料表 | 3 | [osr_pad_displayscheme.md](./osr_pad_displayscheme.md) |
| 52 | `t_osr_hpscheme` | 首页配置方案-主表 | 14 | [osr_hpschemeconfig.md](./osr_hpschemeconfig.md) |
| 53 | `t_osr_hpscheme_l` | 首页配置方案-多语言表 | 5 | [osr_hpschemeconfig.md](./osr_hpschemeconfig.md) |
| 54 | `t_osr_schemecardset` | 主页配置-子表 | 6 | [osr_hpschemeconfig.md](./osr_hpschemeconfig.md) |
| 55 | `t_osr_userfuncrel` | 用户首页功能关联表-主表 | 13 | [osr_pad_userfuncrelation.md](./osr_pad_userfuncrelation.md) |
| 56 | `t_osr_userfuncrel_l` | 用户首页功能关联表-多语言表 | 4 | [osr_pad_userfuncrelation.md](./osr_pad_userfuncrelation.md) |
| 57 | `t_osr_userorgdept` | 用户组织车间设置（后台辅助表单，不用于数据显示）-主表 | 8 | [osr_padreport_userorgdept.md](./osr_padreport_userorgdept.md) |
| 58 | `t_osr_userorgdept_l` | 用户组织车间设置（后台辅助表单，不用于数据显示）-多语言表 | 0 | [osr_padreport_userorgdept.md](./osr_padreport_userorgdept.md) |
| 59 | `t_schemeconfig_entry` | 显示方案配置单据体-子表 | 5 | [osr_displayschemekit.md](./osr_displayschemekit.md) |
