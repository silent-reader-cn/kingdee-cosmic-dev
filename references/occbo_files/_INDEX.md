# occbo 模块表清单

> 本模块共收录 **62** 张表定义，来自 `occbo_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope occbo
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_occbo_basedata` | 渠道出库数据-主表 | 25 | [occbo_basedata.md](./occbo_basedata.md) |
| 2 | `t_occbo_ch_announce` | 渠道公告-主表 | 32 | [occbo_channelannoun.md](./occbo_channelannoun.md) |
| 3 | `t_occbo_ch_announce` | 渠道公告-主表 | 32 | [occbo_channelannounce.md](./occbo_channelannounce.md) |
| 4 | `t_occbo_ch_announce_ch` | 渠道单据体-子表 | 5 | [occbo_channelannoun.md](./occbo_channelannoun.md) |
| 5 | `t_occbo_ch_announce_ch` | 渠道单据体-子表 | 5 | [occbo_channelannounce.md](./occbo_channelannounce.md) |
| 6 | `t_occbo_ch_announce_l` | 渠道公告-多语言表 | 4 | [occbo_channelannoun.md](./occbo_channelannoun.md) |
| 7 | `t_occbo_ch_announce_user` | 用户单据体-子表 | 5 | [occbo_channelannoun.md](./occbo_channelannoun.md) |
| 8 | `t_occbo_ch_announce_user` | 用户单据体-子表 | 5 | [occbo_channelannounce.md](./occbo_channelannounce.md) |
| 9 | `t_occbo_channelclass` | 公告分类-主表 | 19 | [occbo_reportclass.md](./occbo_reportclass.md) |
| 10 | `t_occbo_channelclass_l` | 公告分类-多语言表 | 5 | [occbo_reportclass.md](./occbo_reportclass.md) |
| 11 | `t_occbo_channelgoals` | 渠道目标-主表 | 22 | [occbo_channelgoals.md](./occbo_channelgoals.md) |
| 12 | `t_occbo_channelgoals` | 渠道目标单-主表 | 22 | [occbo_channelgoalsbill.md](./occbo_channelgoalsbill.md) |
| 13 | `t_occbo_channelgoals_l` | 渠道目标-多语言表 | 4 | [occbo_channelgoals.md](./occbo_channelgoals.md) |
| 14 | `t_occbo_channelgoals_l` | 渠道目标单-多语言表 | 4 | [occbo_channelgoalsbill.md](./occbo_channelgoalsbill.md) |
| 15 | `t_occbo_chlgoals_entry` | 目标详情-子表 | 39 | [occbo_channelgoalsbill.md](./occbo_channelgoalsbill.md) |
| 16 | `t_occbo_chlgoals_entry` | 月度目标-主表 | 39 | [occbo_monthgoals.md](./occbo_monthgoals.md) |
| 17 | `t_occbo_chlgoals_entry` | 渠道月度目标达成-主表 | 39 | [occbo_monthgoals_complete.md](./occbo_monthgoals_complete.md) |
| 18 | `t_occbo_chlgoals_entry` | 年度目标-主表 | 39 | [occbo_yeargoals.md](./occbo_yeargoals.md) |
| 19 | `t_occbo_chlgoals_entry` | 渠道年度目标达成-主表 | 39 | [occbo_yeargoals_complete.md](./occbo_yeargoals_complete.md) |
| 20 | `t_occbo_chlgoals_entry_a` | 目标详情-分表 | 18 | [occbo_channelgoalsbill.md](./occbo_channelgoalsbill.md) |
| 21 | `t_occbo_chlgoals_entry_a` | 月度目标-分表 | 18 | [occbo_monthgoals.md](./occbo_monthgoals.md) |
| 22 | `t_occbo_chlgoals_entry_a` | 渠道月度目标达成-分表 | 18 | [occbo_monthgoals_complete.md](./occbo_monthgoals_complete.md) |
| 23 | `t_occbo_chlgoals_entry_a` | 渠道年度目标达成-分表 | 18 | [occbo_yeargoals_complete.md](./occbo_yeargoals_complete.md) |
| 24 | `t_occbo_chlgoals_rp` | 目标月度-多选基础资料表 | 3 | [occbo_channelgoals.md](./occbo_channelgoals.md) |
| 25 | `t_occbo_chlgoals_rp` | 目标月度-多选基础资料表 | 3 | [occbo_channelgoalsbill.md](./occbo_channelgoalsbill.md) |
| 26 | `t_occbo_chnlannbrows` | 渠道公告浏览记录-主表 | 6 | [occbo_channelbrows.md](./occbo_channelbrows.md) |
| 27 | `t_occbo_chnlannfeedback` | 渠道公告反馈信息-主表 | 8 | [occbo_chnlannback.md](./occbo_chnlannback.md) |
| 28 | `t_occbo_deptsaleplan` | 渠道销售计划-主表 | 19 | [occbo_deptsaleplan.md](./occbo_deptsaleplan.md) |
| 29 | `t_occbo_deptsaleplan_ee` | 计划明细-子表 | 70 | [occbo_deptsaleplan.md](./occbo_deptsaleplan.md) |
| 30 | `t_occbo_deptsaleplan_ee_e` | 计划明细-分表 | 38 | [occbo_deptsaleplan.md](./occbo_deptsaleplan.md) |
| 31 | `t_occbo_kpi` | KPI-主表 | 15 | [occbo_kpi_base.md](./occbo_kpi_base.md) |
| 32 | `t_occbo_kpi_bi` | 单据配置信息-子表 | 21 | [occbo_kpi_base.md](./occbo_kpi_base.md) |
| 33 | `t_occbo_kpi_l` | KPI-多语言表 | 4 | [occbo_kpi_base.md](./occbo_kpi_base.md) |
| 34 | `t_occbo_orgsaleplan` | 机构销售计划-主表 | 19 | [occbo_orgsaleplan.md](./occbo_orgsaleplan.md) |
| 35 | `t_occbo_orgsaleplan_ee` | 计划明细-子表 | 69 | [occbo_orgsaleplan.md](./occbo_orgsaleplan.md) |
| 36 | `t_occbo_orgsaleplan_ee_e` | 计划明细-分表 | 38 | [occbo_orgsaleplan.md](./occbo_orgsaleplan.md) |
| 37 | `t_occbo_orgsaleplan_se` | 来源明细-子表 | 10 | [occbo_orgsaleplan.md](./occbo_orgsaleplan.md) |
| 38 | `t_occbo_prodmanuplan` | 产品运作计划-主表 | 13 | [occbo_productmanuplan.md](./occbo_productmanuplan.md) |
| 39 | `t_occbo_prodmanuplan_ee` | 计划明细-子表 | 14 | [occbo_productmanuplan.md](./occbo_productmanuplan.md) |
| 40 | `t_occbo_prodsaleplan` | 产品销售计划-主表 | 20 | [occbo_productsaleplan.md](./occbo_productsaleplan.md) |
| 41 | `t_occbo_prodsaleplan_ee` | 计划明细-子表 | 69 | [occbo_productsaleplan.md](./occbo_productsaleplan.md) |
| 42 | `t_occbo_prodsaleplan_ee_e` | 计划明细-分表 | 38 | [occbo_productsaleplan.md](./occbo_productsaleplan.md) |
| 43 | `t_occbo_prodsaleplan_se` | 来源明细-子表 | 10 | [occbo_productsaleplan.md](./occbo_productsaleplan.md) |
| 44 | `t_occbo_productset` | 产品经理产品设置-主表 | 5 | [occbo_productset.md](./occbo_productset.md) |
| 45 | `t_occbo_saleslevel` | 销售级别-主表 | 11 | [occbo_saleslevel.md](./occbo_saleslevel.md) |
| 46 | `t_occbo_saleslevel_kpi` | kpi单据体-子表 | 4 | [occbo_saleslevel.md](./occbo_saleslevel.md) |
| 47 | `t_occbo_saleslevel_l` | 销售级别-多语言表 | 4 | [occbo_saleslevel.md](./occbo_saleslevel.md) |
| 48 | `t_occbo_saleslevel_user` | 人员单据体-子表 | 7 | [occbo_saleslevel.md](./occbo_saleslevel.md) |
| 49 | `t_occbo_saleslevelgoals` | 销售级别年目标-主表 | 15 | [occbo_saleslevelgoals.md](./occbo_saleslevelgoals.md) |
| 50 | `t_occbo_salevolume` | 销量开单-主表 | 31 | [occbo_salevolume.md](./occbo_salevolume.md) |
| 51 | `t_occbo_salevolume_e` | 分录信息-子表 | 21 | [occbo_salevolume.md](./occbo_salevolume.md) |
| 52 | `t_occbo_slgoals_entry` | 单据体-子表 | 7 | [occbo_saleslevelgoals.md](./occbo_saleslevelgoals.md) |
| 53 | `t_occbo_usergoals` | 人员目标单-主表 | 20 | [occbo_usergoals.md](./occbo_usergoals.md) |
| 54 | `t_occbo_usgoals_entry` | 目标详情-子表 | 44 | [occbo_usergoals.md](./occbo_usergoals.md) |
| 55 | `t_occbo_usgoals_entry` | 人员目标分录基础资料-主表 | 44 | [occbo_usergoals_entry.md](./occbo_usergoals_entry.md) |
| 56 | `t_occbo_usgoals_entry_a` | 目标详情-分表 | 18 | [occbo_usergoals.md](./occbo_usergoals.md) |
| 57 | `t_occbo_usgoals_entry_a` | 人员目标分录基础资料-分表 | 18 | [occbo_usergoals_entry.md](./occbo_usergoals_entry.md) |
| 58 | `t_occbo_visit` | 拜访计划-主表 | 34 | [occbo_visit.md](./occbo_visit.md) |
| 59 | `t_occbo_visitentry` | 拜访记录-子表 | 7 | [occbo_visit.md](./occbo_visit.md) |
| 60 | `t_occbo_visitset` | 外勤设置-主表 | 7 | [occbo_visitset.md](./occbo_visitset.md) |
| 61 | `t_occbo_visitset_entry` | 拜访事务设置-子表 | 7 | [occbo_visitset.md](./occbo_visitset.md) |
| 62 | `t_occbo_visitset_role` | 使用角色-多选基础资料表 | 3 | [occbo_visitset.md](./occbo_visitset.md) |
