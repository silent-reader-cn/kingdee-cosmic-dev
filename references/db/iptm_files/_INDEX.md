# iptm 模块表清单

> 本模块共收录 **50** 张表定义，来自 `iptm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category iptm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_iptm_bds_config` | 业务数据统计配置表-主表 | 17 | [iptm_bds_config.md](./iptm_bds_config.md) |
| 2 | `t_iptm_bds_config_l` | 业务数据统计配置表-多语言表 | 5 | [iptm_bds_config.md](./iptm_bds_config.md) |
| 3 | `t_iptm_bds_configentry` | 单据体-子表 | 6 | [iptm_bds_config.md](./iptm_bds_config.md) |
| 4 | `t_iptm_bds_configref` | 业务数据统计配置关系表-主表 | 3 | [iptm_bds_configref.md](./iptm_bds_configref.md) |
| 5 | `t_iptm_cloudscheme` | 云方案-主表 | 9 | [iptm_cloudscheme.md](./iptm_cloudscheme.md) |
| 6 | `t_iptm_cloudscheme_l` | 云方案-多语言表 | 4 | [iptm_cloudscheme.md](./iptm_cloudscheme.md) |
| 7 | `t_iptm_ct_configitems` | 传输对象-主表 | 36 | [iptm_ct_configitems.md](./iptm_ct_configitems.md) |
| 8 | `t_iptm_ct_configitems_l` | 传输对象-多语言表 | 4 | [iptm_ct_configitems.md](./iptm_ct_configitems.md) |
| 9 | `t_iptm_ct_configtree` | 传输对象左树-主表 | 15 | [iptm_ct_configtree.md](./iptm_ct_configtree.md) |
| 10 | `t_iptm_ct_configtree_l` | 传输对象左树-多语言表 | 5 | [iptm_ct_configtree.md](./iptm_ct_configtree.md) |
| 11 | `t_iptm_ct_datapacket` | 传输包管理-主表 | 22 | [iptm_ct_datapacket.md](./iptm_ct_datapacket.md) |
| 12 | `t_iptm_ct_datapacket_l` | 传输包管理-多语言表 | 4 | [iptm_ct_datapacket.md](./iptm_ct_datapacket.md) |
| 13 | `t_iptm_ct_destaccount` | 连接数据中心管理-主表 | 16 | [iptm_ct_destaccount.md](./iptm_ct_destaccount.md) |
| 14 | `t_iptm_ct_destaccount_l` | 连接数据中心管理-多语言表 | 4 | [iptm_ct_destaccount.md](./iptm_ct_destaccount.md) |
| 15 | `t_iptm_ct_initcheck` | 初始化校验记录-主表 | 0 | [iptm_ct_initcheck.md](./iptm_ct_initcheck.md) |
| 16 | `t_iptm_ct_initconfig` | 参数设置-主表 | 15 | [iptm_ct_initconfig.md](./iptm_ct_initconfig.md) |
| 17 | `t_iptm_ct_initconfigenv` | 配置管控分录-子表 | 14 | [iptm_ct_initconfig.md](./iptm_ct_initconfig.md) |
| 18 | `t_iptm_ct_initconfiguser` | 单据体-子表 | 5 | [iptm_ct_initconfig.md](./iptm_ct_initconfig.md) |
| 19 | `t_iptm_ct_itemrelyentry` | 配置依赖分录-子表 | 7 | [iptm_ct_configitems.md](./iptm_ct_configitems.md) |
| 20 | `t_iptm_ct_log` | 日志管理-主表 | 20 | [iptm_ct_log.md](./iptm_ct_log.md) |
| 21 | `t_iptm_ct_log_l` | 日志管理-多语言表 | 4 | [iptm_ct_log.md](./iptm_ct_log.md) |
| 22 | `t_iptm_ct_logentry` | 单据体-子表 | 8 | [iptm_ct_log.md](./iptm_ct_log.md) |
| 23 | `t_iptm_ct_packscheme` | 打包方案-主表 | 12 | [iptm_ct_packscheme.md](./iptm_ct_packscheme.md) |
| 24 | `t_iptm_ct_packscheme_l` | 打包方案-多语言表 | 4 | [iptm_ct_packscheme.md](./iptm_ct_packscheme.md) |
| 25 | `t_iptm_ct_packschemecfg` | 树形单据体-子表 | 13 | [iptm_ct_packscheme.md](./iptm_ct_packscheme.md) |
| 26 | `t_iptm_ct_subdatapacket` | 子传输包-子表 | 15 | [iptm_ct_datapacket.md](./iptm_ct_datapacket.md) |
| 27 | `t_iptm_ct_subpacket_fj` | 子包文件-附件表 | 3 | [iptm_ct_datapacket.md](./iptm_ct_datapacket.md) |
| 28 | `t_iptm_ct_version` | 上线版本-主表 | 17 | [iptm_ct_version.md](./iptm_ct_version.md) |
| 29 | `t_iptm_ct_version_l` | 上线版本-多语言表 | 4 | [iptm_ct_version.md](./iptm_ct_version.md) |
| 30 | `t_iptm_import_target` | 目标业务对象列表-主表 | 16 | [iptm_importtarget.md](./iptm_importtarget.md) |
| 31 | `t_iptm_import_target_l` | 目标业务对象列表-多语言表 | 4 | [iptm_importtarget.md](./iptm_importtarget.md) |
| 32 | `t_iptm_importobj` | 引入对象[废弃]-主表 | 5 | [iptm_importobj.md](./iptm_importobj.md) |
| 33 | `t_iptm_importobj_l` | 引入对象[废弃]-多语言表 | 4 | [iptm_importobj.md](./iptm_importobj.md) |
| 34 | `t_iptm_importreport` | 定制引入报告【废弃】-主表 | 20 | [iptm_importreport.md](./iptm_importreport.md) |
| 35 | `t_iptm_mappingrelation` | 树形单据体-子表 | 11 | [iptm_mappingscheme.md](./iptm_mappingscheme.md) |
| 36 | `t_iptm_mappingscheme` | 映射方案[废弃]-主表 | 12 | [iptm_mappingscheme.md](./iptm_mappingscheme.md) |
| 37 | `t_iptm_mappingscheme_l` | 映射方案[废弃]-多语言表 | 4 | [iptm_mappingscheme.md](./iptm_mappingscheme.md) |
| 38 | `t_iptm_mitask` | 导入任务-主表 | 15 | [iptm_imptask.md](./iptm_imptask.md) |
| 39 | `t_iptm_mitask_l` | 导入任务-多语言表 | 4 | [iptm_imptask.md](./iptm_imptask.md) |
| 40 | `t_iptm_mitask_targetmeta` | 目标业务对象-多选基础资料表 | 3 | [iptm_imptask.md](./iptm_imptask.md) |
| 41 | `t_iptm_mitaskdetail` | 字段映射-子表 | 9 | [iptm_imptask.md](./iptm_imptask.md) |
| 42 | `t_iptm_mitaskentry` | 导入任务分录-子表 | 14 | [iptm_imptask.md](./iptm_imptask.md) |
| 43 | `t_iptm_mitaskentry_oatt` | 重传附件-附件表 | 3 | [iptm_imptask.md](./iptm_imptask.md) |
| 44 | `t_iptm_multarmeta` | 目标业务对象-多选基础资料表 | 3 | [iptm_scheme.md](./iptm_scheme.md) |
| 45 | `t_iptm_scheme` | 导入方案详情-主表 | 19 | [iptm_scheme.md](./iptm_scheme.md) |
| 46 | `t_iptm_scheme_l` | 导入方案详情-多语言表 | 4 | [iptm_scheme.md](./iptm_scheme.md) |
| 47 | `t_iptm_schemedetail` | 引入任务分录-子表 | 11 | [iptm_scheme.md](./iptm_scheme.md) |
| 48 | `t_iptm_schemefieldmapping` | 字段映射-子表 | 9 | [iptm_scheme.md](./iptm_scheme.md) |
| 49 | `t_iptm_task_report` | 导入报告-主表 | 10 | [iptm_task_excute_report.md](./iptm_task_excute_report.md) |
| 50 | `t_iptm_task_reportentry` | 任务详情单据体-子表 | 12 | [iptm_task_excute_report.md](./iptm_task_excute_report.md) |
