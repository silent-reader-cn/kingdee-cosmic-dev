# sbs 模块表清单

> 本模块共收录 **56** 张表定义，来自 `sbs_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category sbs
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_sbs_billsqnrelation` | 制造单据序列号关联表-主表 | 10 | [mpdm_billsnrelation.md](./mpdm_billsnrelation.md) |
| 2 | `t_sbs_billsqnrelation` | 单据序列号关联表-主表 | 10 | [sbs_billsnrelation.md](./sbs_billsnrelation.md) |
| 3 | `t_sbs_billsqnrelation_e` | 序列号明细-子表 | 13 | [mpdm_billsnrelation.md](./mpdm_billsnrelation.md) |
| 4 | `t_sbs_billsqnrelation_e` | 序列号明细-子表 | 13 | [sbs_billsnrelation.md](./sbs_billsnrelation.md) |
| 5 | `t_sbs_data_targetinfo` | 指标目标值信息-主表 | 16 | [sbs_datasrc_targetinfo.md](./sbs_datasrc_targetinfo.md) |
| 6 | `t_sbs_datametrics` | 数据指标-主表 | 44 | [sbs_datametrics.md](./sbs_datametrics.md) |
| 7 | `t_sbs_datametrics_l` | 数据指标-多语言表 | 5 | [sbs_datametrics.md](./sbs_datametrics.md) |
| 8 | `t_sbs_dimensionsetentry` | 维度设置-子表 | 12 | [sbs_datametrics.md](./sbs_datametrics.md) |
| 9 | `t_sbs_dimensionsetentry_l` | 维度设置-多语言表 | 4 | [sbs_datametrics.md](./sbs_datametrics.md) |
| 10 | `t_sbs_entryreserve` | 预留记录传递记录-主表 | 6 | [sbs_entry_reserve.md](./sbs_entry_reserve.md) |
| 11 | `t_sbs_idxdatasource` | 自定义数据来源-主表 | 23 | [sbs_custdatasource.md](./sbs_custdatasource.md) |
| 12 | `t_sbs_idxdatasource_l` | 自定义数据来源-多语言表 | 4 | [sbs_custdatasource.md](./sbs_custdatasource.md) |
| 13 | `t_sbs_indexgroup` | 指标分类分组-主表 | 17 | [sbs_metricsgroup.md](./sbs_metricsgroup.md) |
| 14 | `t_sbs_indexgroup_l` | 指标分类分组-多语言表 | 6 | [sbs_metricsgroup.md](./sbs_metricsgroup.md) |
| 15 | `t_sbs_manageobjective` | 目标管理-主表 | 35 | [sbs_manageobjective.md](./sbs_manageobjective.md) |
| 16 | `t_sbs_matchrule` | 匹配规则（旧）-主表 | 12 | [cal_matchrule.md](./cal_matchrule.md) |
| 17 | `t_sbs_matchrule_l` | 匹配规则（旧）-多语言表 | 5 | [cal_matchrule.md](./cal_matchrule.md) |
| 18 | `t_sbs_matchruleentry` | 单据体-子表 | 7 | [cal_matchrule.md](./cal_matchrule.md) |
| 19 | `t_sbs_multiorgpslogentry` | 单据体-子表 | 8 | [sbs_multiorgpursalelog.md](./sbs_multiorgpursalelog.md) |
| 20 | `t_sbs_multiorgpursalelog` | 多角贸易日志-主表 | 9 | [sbs_multiorgpursalelog.md](./sbs_multiorgpursalelog.md) |
| 21 | `t_sbs_objectdimentry` | 维度-子表 | 7 | [sbs_manageobjective.md](./sbs_manageobjective.md) |
| 22 | `t_sbs_referentry` | 参考指标-子表 | 19 | [sbs_datametrics.md](./sbs_datametrics.md) |
| 23 | `t_sbs_referentry_l` | 参考指标-多语言表 | 4 | [sbs_datametrics.md](./sbs_datametrics.md) |
| 24 | `t_sbs_reservation` | 预留记录（旧）-主表 | 42 | [sbs_reservation.md](./sbs_reservation.md) |
| 25 | `t_sbs_reserve_colmap` | 字段映射（旧）（废弃）-主表 | 10 | [sbs_reserve_colmap.md](./sbs_reserve_colmap.md) |
| 26 | `t_sbs_reserve_release` | 预留释放记录（废弃）-主表 | 9 | [sbs_reserve_release.md](./sbs_reserve_release.md) |
| 27 | `t_sbs_reserve_st` | 预留方案（旧）（废弃）-主表 | 29 | [sbs_reserve_st.md](./sbs_reserve_st.md) |
| 28 | `t_sbs_reserve_st_l` | 预留方案（旧）（废弃）-多语言表 | 4 | [sbs_reserve_st.md](./sbs_reserve_st.md) |
| 29 | `t_sbs_reserve_st_m` | 预留方案（旧）（废弃）-使用范围位图表 | 2 | [sbs_reserve_st.md](./sbs_reserve_st.md) |
| 30 | `t_sbs_reserve_st_u` | 预留方案（旧）（废弃）-使用范围表 | 3 | [sbs_reserve_st.md](./sbs_reserve_st.md) |
| 31 | `t_sbs_scmcapplevelparam` | 供应链应用级参数-主表 | 11 | [sbs_scmcapplevelparam.md](./sbs_scmcapplevelparam.md) |
| 32 | `t_sbs_scmcapplevelparam_l` | 供应链应用级参数-多语言表 | 5 | [sbs_scmcapplevelparam.md](./sbs_scmcapplevelparam.md) |
| 33 | `t_sbs_snbillcfgopeentry` | 操作映射-子表 | 6 | [sbs_snbillconfig.md](./sbs_snbillconfig.md) |
| 34 | `t_sbs_snbillcfgsmfentry` | 序列号主档字段映射-子表 | 8 | [sbs_snbillconfig.md](./sbs_snbillconfig.md) |
| 35 | `t_sbs_snbillcfgtrkentry` | 序列号轨迹字段映射-子表 | 8 | [sbs_snbillconfig.md](./sbs_snbillconfig.md) |
| 36 | `t_sbs_snbillcfgtrkventry` | 序列号轨迹校验字段映射-子表 | 8 | [sbs_snbillconfig.md](./sbs_snbillconfig.md) |
| 37 | `t_sbs_snbillconfig` | 序列号单据配置-主表 | 29 | [sbs_snbillconfig.md](./sbs_snbillconfig.md) |
| 38 | `t_sbs_snbillconfig_l` | 序列号单据配置-多语言表 | 5 | [sbs_snbillconfig.md](./sbs_snbillconfig.md) |
| 39 | `t_sbs_snrelextconfig` | 序列号关联扩展配置-主表 | 11 | [sbs_snrelextconfig.md](./sbs_snrelextconfig.md) |
| 40 | `t_sbs_snsupplement` | 补录序列号-主表 | 9 | [sbs_snsupplement.md](./sbs_snsupplement.md) |
| 41 | `t_sbs_snsupplement_e` | 序列号明细-子表 | 7 | [sbs_snsupplement.md](./sbs_snsupplement.md) |
| 42 | `t_sbs_systemcallconf` | 系统间联用配置-主表 | 13 | [sbs_intersystemcallconf.md](./sbs_intersystemcallconf.md) |
| 43 | `t_sbs_systemcallconf_l` | 系统间联用配置-多语言表 | 5 | [sbs_intersystemcallconf.md](./sbs_intersystemcallconf.md) |
| 44 | `t_sbs_targetentry` | 目标值-子表 | 22 | [sbs_manageobjective.md](./sbs_manageobjective.md) |
| 45 | `t_sbs_test` | 测试预留-主表 | 0 | [test_reserve.md](./test_reserve.md) |
| 46 | `t_sbs_topiccard` | 指标卡片-主表 | 21 | [sbs_topiccard.md](./sbs_topiccard.md) |
| 47 | `t_sbs_topiccard_l` | 指标卡片-多语言表 | 4 | [sbs_topiccard.md](./sbs_topiccard.md) |
| 48 | `t_sbs_topiccardgroup` | 指标卡片分组-主表 | 14 | [sbs_topiccardgroup.md](./sbs_topiccardgroup.md) |
| 49 | `t_sbs_topiccardgroup_l` | 指标卡片分组-多语言表 | 5 | [sbs_topiccardgroup.md](./sbs_topiccardgroup.md) |
| 50 | `t_sbs_topiccarduserentry` | 用户范围单据体-子表 | 6 | [sbs_topiccard.md](./sbs_topiccard.md) |
| 51 | `t_sbs_tradeorg` | 中间贸易组织-子表 | 4 | [sbs_traderoute.md](./sbs_traderoute.md) |
| 52 | `t_sbs_traderoute` | 贸易路线-主表 | 24 | [sbs_traderoute.md](./sbs_traderoute.md) |
| 53 | `t_sbs_traderoute_l` | 贸易路线-多语言表 | 4 | [sbs_traderoute.md](./sbs_traderoute.md) |
| 54 | `t_sbs_traderouteentry` | 贸易路径概览-子表 | 19 | [sbs_traderoute.md](./sbs_traderoute.md) |
| 55 | `t_sbs_writeofftype` | 核销类别（旧）-主表 | 12 | [cal_writeofftype.md](./cal_writeofftype.md) |
| 56 | `t_sbs_writeofftype_l` | 核销类别（旧）-多语言表 | 5 | [cal_writeofftype.md](./cal_writeofftype.md) |
