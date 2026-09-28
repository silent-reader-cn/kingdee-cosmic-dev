# msbd 模块表清单

> 本模块共收录 **62** 张表定义，来自 `msbd_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category msbd
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_msbd_changeresume` | 变更履历表-主表 | 17 | [msbd_changeresume.md](./msbd_changeresume.md) |
| 2 | `t_msbd_changeresumedetail` | 变更履历详情-主表 | 16 | [msbd_changeresumedetail.md](./msbd_changeresumedetail.md) |
| 3 | `t_msbd_dmfunit` | 操作校验单元-主表 | 19 | [msbd_dmfunit.md](./msbd_dmfunit.md) |
| 4 | `t_msbd_dmfunit_l` | 操作校验单元-多语言表 | 5 | [msbd_dmfunit.md](./msbd_dmfunit.md) |
| 5 | `t_msbd_dmfunitentry_p` | 处理插件实体-子表 | 10 | [msbd_dmfunit.md](./msbd_dmfunit.md) |
| 6 | `t_msbd_dmfunitentry_v` | 校验条件实体-子表 | 7 | [msbd_dmfunit.md](./msbd_dmfunit.md) |
| 7 | `t_msbd_dmfvscheme` | 操作校验方案-主表 | 17 | [msbd_dmfvalidscheme.md](./msbd_dmfvalidscheme.md) |
| 8 | `t_msbd_dmfvscheme_l` | 操作校验方案-多语言表 | 5 | [msbd_dmfvalidscheme.md](./msbd_dmfvalidscheme.md) |
| 9 | `t_msbd_dmfvschemeentry` | 操作校验单元清单-子表 | 5 | [msbd_dmfvalidscheme.md](./msbd_dmfvalidscheme.md) |
| 10 | `t_msbd_excludetgtbill` | 下游存在单据禁止同步-子表 | 7 | [msbd_synctgtbillcfg.md](./msbd_synctgtbillcfg.md) |
| 11 | `t_msbd_fixdatalog` | 巡检修复日志-主表 | 6 | [msbd_fixdatalog.md](./msbd_fixdatalog.md) |
| 12 | `t_msbd_fixdatalog_e` | 修复明细-子表 | 12 | [msbd_fixdatalog.md](./msbd_fixdatalog.md) |
| 13 | `t_msbd_inspectjob` | 数据巡检任务-主表 | 23 | [msbd_inspectjob.md](./msbd_inspectjob.md) |
| 14 | `t_msbd_inspectjob_l` | 数据巡检任务-多语言表 | 5 | [msbd_inspectjob.md](./msbd_inspectjob.md) |
| 15 | `t_msbd_inspectjobentry` | 数据巡检项目-子表 | 7 | [msbd_inspectjob.md](./msbd_inspectjob.md) |
| 16 | `t_msbd_inspectlog` | 数据巡检日志-主表 | 9 | [msbd_inspectlog.md](./msbd_inspectlog.md) |
| 17 | `t_msbd_inspectlogentry` | 检查详情-子表 | 14 | [msbd_inspectlog.md](./msbd_inspectlog.md) |
| 18 | `t_msbd_inspectlogentry_e` | 异常数据列表-子表 | 9 | [msbd_inspectlog.md](./msbd_inspectlog.md) |
| 19 | `t_msbd_inspectplan` | 数据巡检计划-主表 | 32 | [msbd_inspectplan.md](./msbd_inspectplan.md) |
| 20 | `t_msbd_inspectplan_d` | 数据巡检计划-分表 | 32 | [msbd_inspectplan.md](./msbd_inspectplan.md) |
| 21 | `t_msbd_inspectplan_l` | 数据巡检计划-多语言表 | 5 | [msbd_inspectplan.md](./msbd_inspectplan.md) |
| 22 | `t_msbd_inspectplan_m` | 数据巡检计划-使用范围位图表 | 27 | [msbd_inspectplan.md](./msbd_inspectplan.md) |
| 23 | `t_msbd_inspectunit` | 数据巡检模型-主表 | 22 | [msbd_inspectunit.md](./msbd_inspectunit.md) |
| 24 | `t_msbd_inspectunit_l` | 数据巡检模型-多语言表 | 5 | [msbd_inspectunit.md](./msbd_inspectunit.md) |
| 25 | `t_msbd_inspectunitentry_m` | 执行服务-子表 | 10 | [msbd_inspectunit.md](./msbd_inspectunit.md) |
| 26 | `t_msbd_inspectunitentry_p` | 处理插件实体-子表 | 10 | [msbd_inspectunit.md](./msbd_inspectunit.md) |
| 27 | `t_msbd_inspectunitentry_v` | 校验条件实体-子表 | 7 | [msbd_inspectunit.md](./msbd_inspectunit.md) |
| 28 | `t_msbd_puropermaterctrl` | 采购员-物料可采控制-主表 | 16 | [msbd_puropermaterctrl.md](./msbd_puropermaterctrl.md) |
| 29 | `t_msbd_puropermaterctrl_l` | 采购员-物料可采控制-多语言表 | 4 | [msbd_puropermaterctrl.md](./msbd_puropermaterctrl.md) |
| 30 | `t_msbd_puropmatctrlentry` | 单据体-子表 | 8 | [msbd_puropermaterctrl.md](./msbd_puropermaterctrl.md) |
| 31 | `t_msbd_salopermaterctrl` | 销售员-物料可销控制-主表 | 16 | [msbd_salopermaterctrl.md](./msbd_salopermaterctrl.md) |
| 32 | `t_msbd_salopermaterctrl_l` | 销售员-物料可销控制-多语言表 | 4 | [msbd_salopermaterctrl.md](./msbd_salopermaterctrl.md) |
| 33 | `t_msbd_salopmatctrlentry` | 单据体-子表 | 8 | [msbd_salopermaterctrl.md](./msbd_salopermaterctrl.md) |
| 34 | `t_msbd_sccomcfg` | 场景工作台表单通用配置-主表 | 16 | [msbd_scenecommoncfg.md](./msbd_scenecommoncfg.md) |
| 35 | `t_msbd_sccomcfg_filter` | 过滤控件配置-子表 | 5 | [msbd_scenecommoncfg.md](./msbd_scenecommoncfg.md) |
| 36 | `t_msbd_sccomcfg_l` | 场景工作台表单通用配置-多语言表 | 4 | [msbd_scenecommoncfg.md](./msbd_scenecommoncfg.md) |
| 37 | `t_msbd_sccomcfg_menu` | 场景菜单清单配置-子表 | 5 | [msbd_scenecommoncfg.md](./msbd_scenecommoncfg.md) |
| 38 | `t_msbd_sccomcfg_menu_l` | 场景菜单清单配置-多语言表 | 4 | [msbd_scenecommoncfg.md](./msbd_scenecommoncfg.md) |
| 39 | `t_msbd_sccomcfg_menuop` | 场景菜单清单执行操作配置-子表 | 5 | [msbd_scenecommoncfg.md](./msbd_scenecommoncfg.md) |
| 40 | `t_msbd_sccomcfg_toolbar` | 工具栏按钮配置-子表 | 5 | [msbd_scenecommoncfg.md](./msbd_scenecommoncfg.md) |
| 41 | `t_msbd_sccomcfg_toolbarop` | 工具栏按钮执行操作配置-子表 | 5 | [msbd_scenecommoncfg.md](./msbd_scenecommoncfg.md) |
| 42 | `t_msbd_sccustcfg` | 场景工作台配置-主表 | 13 | [msbd_scenecustomcfg.md](./msbd_scenecustomcfg.md) |
| 43 | `t_msbd_sccustcfg_card` | 数据卡片-子表 | 14 | [msbd_scenecustomcfg.md](./msbd_scenecustomcfg.md) |
| 44 | `t_msbd_sccustcfg_card_l` | 数据卡片-多语言表 | 5 | [msbd_scenecustomcfg.md](./msbd_scenecustomcfg.md) |
| 45 | `t_msbd_sccustcfg_l` | 场景工作台配置-多语言表 | 4 | [msbd_scenecustomcfg.md](./msbd_scenecustomcfg.md) |
| 46 | `t_msbd_sccustcfg_nav` | 导航栏信息-子表 | 7 | [msbd_scenecustomcfg.md](./msbd_scenecustomcfg.md) |
| 47 | `t_msbd_sccustcfg_nav_l` | 导航栏信息-多语言表 | 4 | [msbd_scenecustomcfg.md](./msbd_scenecustomcfg.md) |
| 48 | `t_msbd_sccustcfg_tab` | 页签信息-子表 | 6 | [msbd_scenecustomcfg.md](./msbd_scenecustomcfg.md) |
| 49 | `t_msbd_sccustcfg_tab_l` | 页签信息-多语言表 | 4 | [msbd_scenecustomcfg.md](./msbd_scenecustomcfg.md) |
| 50 | `t_msbd_syncfield` | 可同步字段-子表 | 4 | [msbd_synctgtbillcfg.md](./msbd_synctgtbillcfg.md) |
| 51 | `t_msbd_synctgtbillcfg` | 同步下游单据配置-主表 | 19 | [msbd_synctgtbillcfg.md](./msbd_synctgtbillcfg.md) |
| 52 | `t_msbd_synctgtbillcfg_l` | 同步下游单据配置-多语言表 | 4 | [msbd_synctgtbillcfg.md](./msbd_synctgtbillcfg.md) |
| 53 | `t_msbd_synctgtbillmap` | 下游单据-子表 | 8 | [msbd_synctgtbillcfg.md](./msbd_synctgtbillcfg.md) |
| 54 | `t_msbd_tracklog` | 跟踪日志-主表 | 17 | [msbd_tracklog.md](./msbd_tracklog.md) |
| 55 | `t_plat_changemodel` | 变更模型-主表 | 22 | [plat_changemodel.md](./plat_changemodel.md) |
| 56 | `t_plat_changemodel_l` | 变更模型-多语言表 | 5 | [plat_changemodel.md](./plat_changemodel.md) |
| 57 | `t_plat_changemodelbe` | 单据类型映射分录-子表 | 6 | [plat_changemodel.md](./plat_changemodel.md) |
| 58 | `t_plat_changemodelfe` | 字段映射-子表 | 12 | [plat_changemodel.md](./plat_changemodel.md) |
| 59 | `t_plat_changemodelpe` | 插件实体-子表 | 7 | [plat_changemodel.md](./plat_changemodel.md) |
| 60 | `t_plat_changemodelve` | 校验条件实体-子表 | 5 | [plat_changemodel.md](./plat_changemodel.md) |
| 61 | `t_plat_xbill` | 变更单模板-主表 | 0 | [plat_xbilltpl.md](./plat_xbilltpl.md) |
| 62 | `t_plat_xbilllog` | 变更日志-主表 | 17 | [plat_xbilllog.md](./plat_xbilllog.md) |
