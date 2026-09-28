# didc 模块表清单

> 本模块共收录 **55** 张表定义，来自 `didc_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category didc
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_didc_board_role` | 角色权限-子表 | 4 | [didc_intelligenceboard.md](./didc_intelligenceboard.md) |
| 2 | `t_didc_board_user` | 用户权限-子表 | 4 | [didc_intelligenceboard.md](./didc_intelligenceboard.md) |
| 3 | `t_didc_cardentry` | 卡片单据体-子表 | 8 | [didc_intelligenceboard.md](./didc_intelligenceboard.md) |
| 4 | `t_didc_cardentry_l` | 卡片单据体-多语言表 | 4 | [didc_intelligenceboard.md](./didc_intelligenceboard.md) |
| 5 | `t_didc_decitree_role` | 角色权限-子表 | 4 | [didc_indexdecitree.md](./didc_indexdecitree.md) |
| 6 | `t_didc_decitree_user` | 用户权限-子表 | 4 | [didc_indexdecitree.md](./didc_indexdecitree.md) |
| 7 | `t_didc_dimensionentry` | 维度-子表 | 7 | [didc_manageobjective.md](./didc_manageobjective.md) |
| 8 | `t_didc_dimensionsetentry` | 维度设置-子表 | 10 | [didc_indexcatalogue.md](./didc_indexcatalogue.md) |
| 9 | `t_didc_dimensionsetentry_l` | 维度设置-多语言表 | 4 | [didc_indexcatalogue.md](./didc_indexcatalogue.md) |
| 10 | `t_didc_fieldmeta` | 字段元数据-子表 | 7 | [didc_ods.md](./didc_ods.md) |
| 11 | `t_didc_followtask` | 跟进任务-主表 | 37 | [didc_followtaskpage.md](./didc_followtaskpage.md) |
| 12 | `t_didc_followtask_l` | 跟进任务-多语言表 | 4 | [didc_followtaskpage.md](./didc_followtaskpage.md) |
| 13 | `t_didc_indexcatalogue` | 数智指标-主表 | 36 | [didc_indexcatalogue.md](./didc_indexcatalogue.md) |
| 14 | `t_didc_indexcatalogue_l` | 数智指标-多语言表 | 6 | [didc_indexcatalogue.md](./didc_indexcatalogue.md) |
| 15 | `t_didc_indexgroup` | 指标分类-主表 | 17 | [didc_indexgroup.md](./didc_indexgroup.md) |
| 16 | `t_didc_indexgroup_l` | 指标分类-多语言表 | 6 | [didc_indexgroup.md](./didc_indexgroup.md) |
| 17 | `t_didc_indexgroupstandard` | 指标分类标准-主表 | 11 | [didc_indexgroupstandard.md](./didc_indexgroupstandard.md) |
| 18 | `t_didc_indexgroupstandard_l` | 指标分类标准-多语言表 | 4 | [didc_indexgroupstandard.md](./didc_indexgroupstandard.md) |
| 19 | `t_didc_indexlabel` | 指标标签-主表 | 11 | [didc_indexlabel.md](./didc_indexlabel.md) |
| 20 | `t_didc_indexlabel_d` | 指标标签-多选基础资料表 | 3 | [didc_indexcatalogue.md](./didc_indexcatalogue.md) |
| 21 | `t_didc_indexlabel_l` | 指标标签-多语言表 | 4 | [didc_indexlabel.md](./didc_indexlabel.md) |
| 22 | `t_didc_indexrangeconfig` | 指标范围配置过滤条件-主表 | 14 | [didc_indexrangeconfig.md](./didc_indexrangeconfig.md) |
| 23 | `t_didc_indexrangeconfig_l` | 指标范围配置过滤条件-多语言表 | 4 | [didc_indexrangeconfig.md](./didc_indexrangeconfig.md) |
| 24 | `t_didc_indextree` | 指标决策树-主表 | 15 | [didc_indexdecitree.md](./didc_indexdecitree.md) |
| 25 | `t_didc_indextree_l` | 指标决策树-多语言表 | 5 | [didc_indexdecitree.md](./didc_indexdecitree.md) |
| 26 | `t_didc_indextreeentry` | 树形单据体-子表 | 10 | [didc_indexdecitree.md](./didc_indexdecitree.md) |
| 27 | `t_didc_indextreeentry_l` | 树形单据体-多语言表 | 4 | [didc_indexdecitree.md](./didc_indexdecitree.md) |
| 28 | `t_didc_indextreegroup` | 指标树分类-主表 | 15 | [didc_indextreegroup.md](./didc_indextreegroup.md) |
| 29 | `t_didc_indextreegroup_l` | 指标树分类-多语言表 | 5 | [didc_indextreegroup.md](./didc_indextreegroup.md) |
| 30 | `t_didc_indexwarn` | 指标风险项-主表 | 34 | [didc_indexwarn.md](./didc_indexwarn.md) |
| 31 | `t_didc_indexwarn_l` | 指标风险项-多语言表 | 4 | [didc_indexwarn.md](./didc_indexwarn.md) |
| 32 | `t_didc_indexwarnentry` | 单据体-子表 | 8 | [didc_indexwarn.md](./didc_indexwarn.md) |
| 33 | `t_didc_indexwarnlog` | 指标风险项日志-主表 | 13 | [didc_indexwarnlog.md](./didc_indexwarnlog.md) |
| 34 | `t_didc_inputdataentry` | 输入数据单据体-子表 | 4 | [didc_indexcatalogue.md](./didc_indexcatalogue.md) |
| 35 | `t_didc_inputdatasubentry` | 子单据体-子表 | 9 | [didc_indexcatalogue.md](./didc_indexcatalogue.md) |
| 36 | `t_didc_intelligenceboard` | AI看板-主表 | 19 | [didc_intelligenceboard.md](./didc_intelligenceboard.md) |
| 37 | `t_didc_intelligenceboard_l` | AI看板-多语言表 | 4 | [didc_intelligenceboard.md](./didc_intelligenceboard.md) |
| 38 | `t_didc_labelgroup` | 标签分类-主表 | 14 | [didc_labelgroup.md](./didc_labelgroup.md) |
| 39 | `t_didc_labelgroup_l` | 标签分类-多语言表 | 5 | [didc_labelgroup.md](./didc_labelgroup.md) |
| 40 | `t_didc_manageobjective` | 目标管理-主表 | 35 | [didc_manageobjective.md](./didc_manageobjective.md) |
| 41 | `t_didc_ods` | 离线数据源-主表 | 11 | [didc_ods.md](./didc_ods.md) |
| 42 | `t_didc_ods_l` | 离线数据源-多语言表 | 4 | [didc_ods.md](./didc_ods.md) |
| 43 | `t_didc_overviewconfig` | 指标概览配置基础资料-主表 | 13 | [didc_overview_configdata.md](./didc_overview_configdata.md) |
| 44 | `t_didc_overviewconfig_l` | 指标概览配置基础资料-多语言表 | 4 | [didc_overview_configdata.md](./didc_overview_configdata.md) |
| 45 | `t_didc_overviewsub` | 指标概览关注-主表 | 13 | [didc_overviewsub.md](./didc_overviewsub.md) |
| 46 | `t_didc_overviewsub_l` | 指标概览关注-多语言表 | 4 | [didc_overviewsub.md](./didc_overviewsub.md) |
| 47 | `t_didc_referentry` | 参考指标-子表 | 14 | [didc_indexcatalogue.md](./didc_indexcatalogue.md) |
| 48 | `t_didc_referentry_l` | 参考指标-多语言表 | 4 | [didc_indexcatalogue.md](./didc_indexcatalogue.md) |
| 49 | `t_didc_responsibility` | 责任对象数据集-子表 | 9 | [didc_indexcatalogue.md](./didc_indexcatalogue.md) |
| 50 | `t_didc_soucre_bill` | 取值来源单据-主表 | 2 | [didc_soucre_bill.md](./didc_soucre_bill.md) |
| 51 | `t_didc_targetentry` | 目标值-子表 | 21 | [didc_manageobjective.md](./didc_manageobjective.md) |
| 52 | `t_didc_taskprogress` | 跟进任务流程-主表 | 19 | [didc_taskprogresspage.md](./didc_taskprogresspage.md) |
| 53 | `t_didc_treeset` | 指标参数设置-主表 | 16 | [didc_treeset.md](./didc_treeset.md) |
| 54 | `t_didc_warn_dimension` | 风险项异常维度-主表 | 13 | [didc_warn_dimension.md](./didc_warn_dimension.md) |
| 55 | `t_didc_warnuser` | 给-多选基础资料表 | 3 | [didc_indexwarn.md](./didc_indexwarn.md) |
