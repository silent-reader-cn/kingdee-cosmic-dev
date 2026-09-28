# sbs 模块表清单

> 本模块共收录 **28** 张表定义，来自 `sbs_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope sbs
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_sbs_billsqnrelation` | 单据序列号关联表-主表 | 10 | [sbs_billsnrelation.md](./sbs_billsnrelation.md) |
| 2 | `t_sbs_billsqnrelation_e` | 序列号明细-子表 | 11 | [sbs_billsnrelation.md](./sbs_billsnrelation.md) |
| 3 | `t_sbs_entryreserve` | 预留记录传递记录-主表 | 6 | [sbs_entry_reserve.md](./sbs_entry_reserve.md) |
| 4 | `t_sbs_matchrule` | 匹配规则（旧）-主表 | 12 | [cal_matchrule.md](./cal_matchrule.md) |
| 5 | `t_sbs_matchrule_l` | 匹配规则（旧）-多语言表 | 5 | [cal_matchrule.md](./cal_matchrule.md) |
| 6 | `t_sbs_matchruleentry` | 单据体-子表 | 7 | [cal_matchrule.md](./cal_matchrule.md) |
| 7 | `t_sbs_reservation` | 预留记录（旧）-主表 | 42 | [sbs_reservation.md](./sbs_reservation.md) |
| 8 | `t_sbs_reserve_colmap` | 字段映射（旧）（废弃）-主表 | 10 | [sbs_reserve_colmap.md](./sbs_reserve_colmap.md) |
| 9 | `t_sbs_reserve_release` | 预留释放记录（废弃）-主表 | 9 | [sbs_reserve_release.md](./sbs_reserve_release.md) |
| 10 | `t_sbs_reserve_st` | 预留方案（旧）（废弃）-主表 | 29 | [sbs_reserve_st.md](./sbs_reserve_st.md) |
| 11 | `t_sbs_reserve_st_l` | 预留方案（旧）（废弃）-多语言表 | 4 | [sbs_reserve_st.md](./sbs_reserve_st.md) |
| 12 | `t_sbs_reserve_st_m` | 预留方案（旧）（废弃）-使用范围位图表 | 2 | [sbs_reserve_st.md](./sbs_reserve_st.md) |
| 13 | `t_sbs_reserve_st_u` | 预留方案（旧）（废弃）-使用范围表 | 3 | [sbs_reserve_st.md](./sbs_reserve_st.md) |
| 14 | `t_sbs_scmcapplevelparam` | 供应链应用级参数-主表 | 11 | [sbs_scmcapplevelparam.md](./sbs_scmcapplevelparam.md) |
| 15 | `t_sbs_scmcapplevelparam_l` | 供应链应用级参数-多语言表 | 5 | [sbs_scmcapplevelparam.md](./sbs_scmcapplevelparam.md) |
| 16 | `t_sbs_snbillcfgopeentry` | 操作映射-子表 | 5 | [sbs_snbillconfig.md](./sbs_snbillconfig.md) |
| 17 | `t_sbs_snbillcfgsmfentry` | 序列号主档字段映射-子表 | 8 | [sbs_snbillconfig.md](./sbs_snbillconfig.md) |
| 18 | `t_sbs_snbillcfgtrkentry` | 序列号轨迹字段映射-子表 | 8 | [sbs_snbillconfig.md](./sbs_snbillconfig.md) |
| 19 | `t_sbs_snbillcfgtrkventry` | 序列号轨迹校验字段映射-子表 | 8 | [sbs_snbillconfig.md](./sbs_snbillconfig.md) |
| 20 | `t_sbs_snbillconfig` | 序列号单据配置-主表 | 27 | [sbs_snbillconfig.md](./sbs_snbillconfig.md) |
| 21 | `t_sbs_snbillconfig_l` | 序列号单据配置-多语言表 | 5 | [sbs_snbillconfig.md](./sbs_snbillconfig.md) |
| 22 | `t_sbs_snsupplement` | 补录序列号-主表 | 9 | [sbs_snsupplement.md](./sbs_snsupplement.md) |
| 23 | `t_sbs_snsupplement_e` | 序列号明细-子表 | 7 | [sbs_snsupplement.md](./sbs_snsupplement.md) |
| 24 | `t_sbs_systemcallconf` | 系统间联用配置-主表 | 13 | [sbs_intersystemcallconf.md](./sbs_intersystemcallconf.md) |
| 25 | `t_sbs_systemcallconf_l` | 系统间联用配置-多语言表 | 5 | [sbs_intersystemcallconf.md](./sbs_intersystemcallconf.md) |
| 26 | `t_sbs_test` | 测试预留-主表 | 0 | [test_reserve.md](./test_reserve.md) |
| 27 | `t_sbs_writeofftype` | 核销类别（旧）-主表 | 12 | [cal_writeofftype.md](./cal_writeofftype.md) |
| 28 | `t_sbs_writeofftype_l` | 核销类别（旧）-多语言表 | 5 | [cal_writeofftype.md](./cal_writeofftype.md) |
