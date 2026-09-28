# ccm 模块表清单

> 本模块共收录 **86** 张表定义，来自 `ccm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ccm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ccm_adjustmententry` | 额度调整分录-子表 | 14 | [ccm_balanceadjustment.md](./ccm_balanceadjustment.md) |
| 2 | `t_ccm_archive` | 信用档案-主表 | 48 | [ccm_archive.md](./ccm_archive.md) |
| 3 | `t_ccm_archive_apply` | （废弃）信用档案申请单-主表 | 22 | [ccm_archive_apply.md](./ccm_archive_apply.md) |
| 4 | `t_ccm_archive_apply_entry` | 信用档案设置-子表 | 23 | [ccm_archive_apply_new.md](./ccm_archive_apply_new.md) |
| 5 | `t_ccm_archive_apply_entry_l` | 信用档案设置-多语言表 | 4 | [ccm_archive_apply_new.md](./ccm_archive_apply_new.md) |
| 6 | `t_ccm_archive_apply_new` | 信用档案申请-主表 | 19 | [ccm_archive_apply_new.md](./ccm_archive_apply_new.md) |
| 7 | `t_ccm_archive_apply_sch_e` | 信用额度分录-子表 | 23 | [ccm_archive_apply.md](./ccm_archive_apply.md) |
| 8 | `t_ccm_archive_apply_share` | 额度共享范围分录-子表 | 4 | [ccm_archive_apply_new.md](./ccm_archive_apply_new.md) |
| 9 | `t_ccm_archive_change` | （废弃）信用档案变更申请单-主表 | 21 | [ccm_archive_change.md](./ccm_archive_change.md) |
| 10 | `t_ccm_archive_change_e` | 信用额度分录-子表 | 30 | [ccm_archive_change.md](./ccm_archive_change.md) |
| 11 | `t_ccm_archive_l` | 信用档案-多语言表 | 4 | [ccm_archive.md](./ccm_archive.md) |
| 12 | `t_ccm_balanceadjustment` | （废弃）信用额度调整单-主表 | 19 | [ccm_balanceadjustment.md](./ccm_balanceadjustment.md) |
| 13 | `t_ccm_billcheckrecord` | 单据信用检查结果记录-主表 | 20 | [ccm_billcheckrecord.md](./ccm_billcheckrecord.md) |
| 14 | `t_ccm_billops` | 单据支持信用的操作设置-主表 | 4 | [ccm_billopset.md](./ccm_billopset.md) |
| 15 | `t_ccm_billstrategy` | （废弃）单据策略-主表 | 31 | [ccm_billstrategy.md](./ccm_billstrategy.md) |
| 16 | `t_ccm_billstrategy_l` | （废弃）单据策略-多语言表 | 4 | [ccm_billstrategy.md](./ccm_billstrategy.md) |
| 17 | `t_ccm_billstrategy_new` | 信用单据策略-主表 | 40 | [ccm_billstrategy_new.md](./ccm_billstrategy_new.md) |
| 18 | `t_ccm_billstrategy_new_l` | 信用单据策略-多语言表 | 4 | [ccm_billstrategy_new.md](./ccm_billstrategy_new.md) |
| 19 | `t_ccm_bs_checkentry` | 检查策略取值分录-子表 | 12 | [ccm_billstrategy.md](./ccm_billstrategy.md) |
| 20 | `t_ccm_bs_checkentry_new` | 信控取值配置-子表 | 12 | [ccm_billstrategy_new.md](./ccm_billstrategy_new.md) |
| 21 | `t_ccm_bs_recalentry` | 重算策略取值分录-子表 | 12 | [ccm_billstrategy.md](./ccm_billstrategy.md) |
| 22 | `t_ccm_bs_recalentry_new` | 重算策略取值分录-子表 | 12 | [ccm_billstrategy_new.md](./ccm_billstrategy_new.md) |
| 23 | `t_ccm_checktype` | （废弃）信用控制形式-主表 | 12 | [ccm_checktype.md](./ccm_checktype.md) |
| 24 | `t_ccm_checktype_l` | （废弃）信用控制形式-多语言表 | 5 | [ccm_checktype.md](./ccm_checktype.md) |
| 25 | `t_ccm_controlstatus` | 维度成员值受控状态-主表 | 4 | [ccm_controlstatus.md](./ccm_controlstatus.md) |
| 26 | `t_ccm_creditnetrecord` | 信用网控记录-主表 | 8 | [ccm_creditnetrecord.md](./ccm_creditnetrecord.md) |
| 27 | `t_ccm_cusunicode` | 客户统一码-主表 | 12 | [ccm_cusunicode.md](./ccm_cusunicode.md) |
| 28 | `t_ccm_cusunicode_l` | 客户统一码-多语言表 | 5 | [ccm_cusunicode.md](./ccm_cusunicode.md) |
| 29 | `t_ccm_cusunicodeentry` | 统一码成员分录-子表 | 4 | [ccm_cusunicode.md](./ccm_cusunicode.md) |
| 30 | `t_ccm_dimension` | 信控维度-主表 | 12 | [ccm_dimension.md](./ccm_dimension.md) |
| 31 | `t_ccm_dimension_l` | 信控维度-多语言表 | 5 | [ccm_dimension.md](./ccm_dimension.md) |
| 32 | `t_ccm_dimensionentry` | 维度成员-子表 | 7 | [ccm_dimension.md](./ccm_dimension.md) |
| 33 | `t_ccm_ec_dimensions` | 维度映射分录-子表 | 5 | [ccm_entityconfig.md](./ccm_entityconfig.md) |
| 34 | `t_ccm_ec_quotatypes` | 额度映射分录-子表 | 5 | [ccm_entityconfig.md](./ccm_entityconfig.md) |
| 35 | `t_ccm_ec_selectors` | 字段分录-子表 | 4 | [ccm_entityconfig.md](./ccm_entityconfig.md) |
| 36 | `t_ccm_entityconfig` | 单据配置-主表 | 21 | [ccm_entityconfig.md](./ccm_entityconfig.md) |
| 37 | `t_ccm_entityconfig_l` | 单据配置-多语言表 | 5 | [ccm_entityconfig.md](./ccm_entityconfig.md) |
| 38 | `t_ccm_grade` | 信用等级-主表 | 14 | [ccm_grade.md](./ccm_grade.md) |
| 39 | `t_ccm_grade_l` | 信用等级-多语言表 | 5 | [ccm_grade.md](./ccm_grade.md) |
| 40 | `t_ccm_gradeentry` | 等级详情-子表 | 6 | [ccm_grade.md](./ccm_grade.md) |
| 41 | `t_ccm_journal` | 信用流水-主表 | 34 | [ccm_journal.md](./ccm_journal.md) |
| 42 | `t_ccm_journaldetail` | 信用流水明细-主表 | 44 | [ccm_journaldetail.md](./ccm_journaldetail.md) |
| 43 | `t_ccm_mode` | （废弃）信用控制方式-主表 | 10 | [ccm_mode.md](./ccm_mode.md) |
| 44 | `t_ccm_mode_l` | （废弃）信用控制方式-多语言表 | 5 | [ccm_mode.md](./ccm_mode.md) |
| 45 | `t_ccm_overdueset` | 信用逾期设置-主表 | 17 | [ccm_overdueset.md](./ccm_overdueset.md) |
| 46 | `t_ccm_overdueset_l` | 信用逾期设置-多语言表 | 4 | [ccm_overdueset.md](./ccm_overdueset.md) |
| 47 | `t_ccm_params` | 信用管理应用参数-主表 | 4 | [ccm_params.md](./ccm_params.md) |
| 48 | `t_ccm_privilege` | （废弃）特权审批申请单-主表 | 33 | [ccm_achive_privilege.md](./ccm_achive_privilege.md) |
| 49 | `t_ccm_recalarchive` | 信用重算的档案-主表 | 5 | [ccm_recalarchives.md](./ccm_recalarchives.md) |
| 50 | `t_ccm_recalculatedetail` | 重算流水明细-主表 | 34 | [ccm_recalculatedetail.md](./ccm_recalculatedetail.md) |
| 51 | `t_ccm_recalproclog` | 信用重算过程日志-主表 | 6 | [ccm_recalcreditlog.md](./ccm_recalcreditlog.md) |
| 52 | `t_ccm_recalresult` | 信用重算日志-主表 | 16 | [ccm_recalculaterecord.md](./ccm_recalculaterecord.md) |
| 53 | `t_ccm_recalresult_org` | 组织共享范围-多选基础资料表 | 3 | [ccm_recalculaterecord.md](./ccm_recalculaterecord.md) |
| 54 | `t_ccm_recalresultentry` | 重算结果-子表 | 21 | [ccm_recalculaterecord.md](./ccm_recalculaterecord.md) |
| 55 | `t_ccm_role` | 维度成员-主表 | 13 | [ccm_role.md](./ccm_role.md) |
| 56 | `t_ccm_role_l` | 维度成员-多语言表 | 4 | [ccm_role.md](./ccm_role.md) |
| 57 | `t_ccm_scheme` | （废弃）信控方案-主表 | 28 | [ccm_scheme.md](./ccm_scheme.md) |
| 58 | `t_ccm_scheme_entry` | 单据策略分录-子表 | 5 | [ccm_scheme.md](./ccm_scheme.md) |
| 59 | `t_ccm_scheme_l` | （废弃）信控方案-多语言表 | 5 | [ccm_scheme.md](./ccm_scheme.md) |
| 60 | `t_ccm_scheme_orgentry` | 额度共享范围-子表 | 4 | [ccm_scheme.md](./ccm_scheme.md) |
| 61 | `t_ccm_schemes` | 信用控制方案-主表 | 30 | [ccm_schemes.md](./ccm_schemes.md) |
| 62 | `t_ccm_schemes_entry` | 单据策略分录-子表 | 11 | [ccm_schemes.md](./ccm_schemes.md) |
| 63 | `t_ccm_schemes_l` | 信用控制方案-多语言表 | 5 | [ccm_schemes.md](./ccm_schemes.md) |
| 64 | `t_ccm_schemes_orgentry` | 额度共享范围-子表 | 4 | [ccm_schemes.md](./ccm_schemes.md) |
| 65 | `t_ccm_shareorgs` | 额度共享范围-多选基础资料表 | 3 | [ccm_archive.md](./ccm_archive.md) |
| 66 | `t_ccm_temp_archive` | （废弃）临时信用档案申请单-主表 | 18 | [ccm_temp_archive.md](./ccm_temp_archive.md) |
| 67 | `t_ccm_temp_archive_entry` | 临时档案设置分录-子表 | 21 | [ccm_temp_archive.md](./ccm_temp_archive.md) |
| 68 | `t_ccm_temp_archive_new` | 临时信用档案申请-主表 | 16 | [ccm_temp_archive_new.md](./ccm_temp_archive_new.md) |
| 69 | `t_ccm_temp_archive_new_l` | 临时信用档案申请-多语言表 | 4 | [ccm_temp_archive_new.md](./ccm_temp_archive_new.md) |
| 70 | `t_ccm_temp_archive_new_lk` | 关联子实体-子表 | 6 | [ccm_temp_archive_new.md](./ccm_temp_archive_new.md) |
| 71 | `t_ccm_temp_archive_new_tc` | 临时信用档案申请-关联追踪表 | 7 | [ccm_temp_archive_new.md](./ccm_temp_archive_new.md) |
| 72 | `t_ccm_temp_archive_new_wb` | 临时信用档案申请-反写记录表 | 10 | [ccm_temp_archive_new.md](./ccm_temp_archive_new.md) |
| 73 | `t_ccm_temparchive_entity` | 临时档案设置-子表 | 21 | [ccm_temp_archive_new.md](./ccm_temp_archive_new.md) |
| 74 | `t_ccm_temparchive_entity_l` | 临时档案设置-多语言表 | 4 | [ccm_temp_archive_new.md](./ccm_temp_archive_new.md) |
| 75 | `t_ccm_temparchive_entity_lk` | 关联子实体-子表 | 6 | [ccm_temp_archive_new.md](./ccm_temp_archive_new.md) |
| 76 | `t_ccm_temparchive_orgs` | 授信组织-多选基础资料表 | 3 | [ccm_temp_archive_new.md](./ccm_temp_archive_new.md) |
| 77 | `t_ccm_upcreditlog` | 信用更新日志-主表 | 20 | [ccm_updatecreditlog.md](./ccm_updatecreditlog.md) |
| 78 | `t_ccm_usedetail` | 信用更新明细-主表 | 16 | [ccm_usedetail.md](./ccm_usedetail.md) |
| 79 | `t_ccm_xarchive` | 信用档案变更单-主表 | 16 | [ccm_xarchive.md](./ccm_xarchive.md) |
| 80 | `t_ccm_xarchive_entity` | 变更详情单据体-子表 | 29 | [ccm_xarchive.md](./ccm_xarchive.md) |
| 81 | `t_ccm_xarchive_entity_lk` | 关联子实体-子表 | 6 | [ccm_xarchive.md](./ccm_xarchive.md) |
| 82 | `t_ccm_xarchive_l` | 信用档案变更单-多语言表 | 5 | [ccm_xarchive.md](./ccm_xarchive.md) |
| 83 | `t_ccm_xarchive_lk` | 关联子实体-子表 | 6 | [ccm_xarchive.md](./ccm_xarchive.md) |
| 84 | `t_ccm_xarchive_orgs` | 授信组织-多选基础资料表 | 3 | [ccm_xarchive.md](./ccm_xarchive.md) |
| 85 | `t_ccm_xarchive_tc` | 信用档案变更单-关联追踪表 | 7 | [ccm_xarchive.md](./ccm_xarchive.md) |
| 86 | `t_ccm_xarchive_wb` | 信用档案变更单-反写记录表 | 10 | [ccm_xarchive.md](./ccm_xarchive.md) |
