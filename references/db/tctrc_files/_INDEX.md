# tctrc 模块表清单

> 本模块共收录 **95** 张表定义，来自 `tctrc_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category tctrc
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_tctrc_anal_scheme` | 分析方案-主表 | 13 | [tctrc_analysis_scheme.md](./tctrc_analysis_scheme.md) |
| 2 | `t_tctrc_anal_scheme_l` | 分析方案-多语言表 | 4 | [tctrc_analysis_scheme.md](./tctrc_analysis_scheme.md) |
| 3 | `t_tctrc_anal_schemeentry` | 单据体-子表 | 5 | [tctrc_analysis_scheme.md](./tctrc_analysis_scheme.md) |
| 4 | `t_tctrc_bala_sheet_record` | 资产负债表关键数据历史记录表-主表 | 5 | [tctrc_balanc_sheet_record.md](./tctrc_balanc_sheet_record.md) |
| 5 | `t_tctrc_check_list` | 健康检查风险指标清单-主表 | 13 | [tctrc_check_list.md](./tctrc_check_list.md) |
| 6 | `t_tctrc_check_list_l` | 健康检查风险指标清单-多语言表 | 4 | [tctrc_check_list.md](./tctrc_check_list.md) |
| 7 | `t_tctrc_check_list_org` | 单据体组织-子表 | 4 | [tctrc_check_list.md](./tctrc_check_list.md) |
| 8 | `t_tctrc_check_list_risk` | 单据体风险-子表 | 6 | [tctrc_check_list.md](./tctrc_check_list.md) |
| 9 | `t_tctrc_check_report_list` | 健康检查报告查询-主表 | 12 | [tctrc_checkup_report_list.md](./tctrc_checkup_report_list.md) |
| 10 | `t_tctrc_collect_entity` | 风险收藏实体-主表 | 6 | [tctrc_collect_entity.md](./tctrc_collect_entity.md) |
| 11 | `t_tctrc_collect_entity` | 收藏说明-主表 | 6 | [tctrc_collect_explain.md](./tctrc_collect_explain.md) |
| 12 | `t_tctrc_external_sys_conf` | 外部系统配置-主表 | 12 | [tctrc_external_sys_conf.md](./tctrc_external_sys_conf.md) |
| 13 | `t_tctrc_external_sys_conf_l` | 外部系统配置-多语言表 | 4 | [tctrc_external_sys_conf.md](./tctrc_external_sys_conf.md) |
| 14 | `t_tctrc_handle_entity` | 处理意见单据-主表 | 11 | [tctrc_handle_entity.md](./tctrc_handle_entity.md) |
| 15 | `t_tctrc_handle_suggestion` | 单据体-子表 | 4 | [tctrc_handle_entity.md](./tctrc_handle_entity.md) |
| 16 | `t_tctrc_indica_record_djt` | 单据体-子表 | 9 | [tctrc_indicators_record.md](./tctrc_indicators_record.md) |
| 17 | `t_tctrc_indicators_record` | 税负率指标分析历史记录表-主表 | 5 | [tctrc_indicators_record.md](./tctrc_indicators_record.md) |
| 18 | `t_tctrc_loss_s_record_djt` | 单据体-子表 | 9 | [tctrc_loss_stateme_record.md](./tctrc_loss_stateme_record.md) |
| 19 | `t_tctrc_loss_state_record` | 损益表关键数据历史记录表-主表 | 5 | [tctrc_loss_stateme_record.md](./tctrc_loss_stateme_record.md) |
| 20 | `t_tctrc_new_evaluation` | 风险评价-主表 | 23 | [tctrc_risk_evaluation_new.md](./tctrc_risk_evaluation_new.md) |
| 21 | `t_tctrc_new_evaluation_l` | 风险评价-多语言表 | 4 | [tctrc_risk_evaluation_new.md](./tctrc_risk_evaluation_new.md) |
| 22 | `t_tctrc_prefer_record_djt` | 单据体-子表 | 12 | [tctrc_preference_record.md](./tctrc_preference_record.md) |
| 23 | `t_tctrc_preference_record` | 税收优惠统计历史记录表-主表 | 2 | [tctrc_preference_record.md](./tctrc_preference_record.md) |
| 24 | `t_tctrc_records` | 风险运行记录表-主表 | 10 | [tctrc_result_records.md](./tctrc_result_records.md) |
| 25 | `t_tctrc_records_entry` | 单据体-子表 | 6 | [tctrc_result_records.md](./tctrc_result_records.md) |
| 26 | `t_tctrc_risk_assign` | 风险分配-主表 | 3 | [tctrc_risk_assign.md](./tctrc_risk_assign.md) |
| 27 | `t_tctrc_risk_d_record_djt` | 单据体-子表 | 11 | [tctrc_risk_detail_record.md](./tctrc_risk_detail_record.md) |
| 28 | `t_tctrc_risk_def_sbbtype` | 申报表类型-多选基础资料表 | 3 | [tctrc_element_verify.md](./tctrc_element_verify.md) |
| 29 | `t_tctrc_risk_def_sbbtype` | 申报表类型-多选基础资料表 | 3 | [tctrc_risk_definition.md](./tctrc_risk_definition.md) |
| 30 | `t_tctrc_risk_def_sbbtype` | 申报表类型-多选基础资料表 | 3 | [tctrc_risk_number.md](./tctrc_risk_number.md) |
| 31 | `t_tctrc_risk_def_sbbtype` | 申报表类型-多选基础资料表 | 3 | [tctrc_risk_sampling.md](./tctrc_risk_sampling.md) |
| 32 | `t_tctrc_risk_definition` | 数据比对-主表 | 36 | [tctrc_element_verify.md](./tctrc_element_verify.md) |
| 33 | `t_tctrc_risk_definition` | 风险设置-主表 | 36 | [tctrc_risk_definition.md](./tctrc_risk_definition.md) |
| 34 | `t_tctrc_risk_definition` | 数值指标-主表 | 36 | [tctrc_risk_number.md](./tctrc_risk_number.md) |
| 35 | `t_tctrc_risk_definition` | 筛查抽检-主表 | 36 | [tctrc_risk_sampling.md](./tctrc_risk_sampling.md) |
| 36 | `t_tctrc_risk_definition_l` | 数据比对-多语言表 | 4 | [tctrc_element_verify.md](./tctrc_element_verify.md) |
| 37 | `t_tctrc_risk_definition_l` | 风险设置-多语言表 | 4 | [tctrc_risk_definition.md](./tctrc_risk_definition.md) |
| 38 | `t_tctrc_risk_definition_l` | 数值指标-多语言表 | 4 | [tctrc_risk_number.md](./tctrc_risk_number.md) |
| 39 | `t_tctrc_risk_definition_l` | 筛查抽检-多语言表 | 4 | [tctrc_risk_sampling.md](./tctrc_risk_sampling.md) |
| 40 | `t_tctrc_risk_detai_record` | 风险指标详情历史记录表-主表 | 2 | [tctrc_risk_detail_record.md](./tctrc_risk_detail_record.md) |
| 41 | `t_tctrc_risk_entry` | 核对内容-子表 | 11 | [tctrc_element_verify.md](./tctrc_element_verify.md) |
| 42 | `t_tctrc_risk_entry` | 抽检内容-子表 | 11 | [tctrc_risk_sampling.md](./tctrc_risk_sampling.md) |
| 43 | `t_tctrc_risk_evaluation` | 风险评价表-主表 | 8 | [tctrc_risk_evaluation_db.md](./tctrc_risk_evaluation_db.md) |
| 44 | `t_tctrc_risk_guide_1` | 高于正常指引单据体-子表 | 4 | [tctrc_element_verify.md](./tctrc_element_verify.md) |
| 45 | `t_tctrc_risk_guide_1` | 单据体-子表 | 4 | [tctrc_risk_definition.md](./tctrc_risk_definition.md) |
| 46 | `t_tctrc_risk_guide_1` | 高于正常指引单据体-子表 | 4 | [tctrc_risk_number.md](./tctrc_risk_number.md) |
| 47 | `t_tctrc_risk_guide_1` | 高于正常指引单据体-子表 | 4 | [tctrc_risk_sampling.md](./tctrc_risk_sampling.md) |
| 48 | `t_tctrc_risk_guide_2` | 高于风险指引单据体-子表 | 4 | [tctrc_element_verify.md](./tctrc_element_verify.md) |
| 49 | `t_tctrc_risk_guide_2` | 单据体-子表 | 4 | [tctrc_risk_definition.md](./tctrc_risk_definition.md) |
| 50 | `t_tctrc_risk_guide_2` | 高于风险指引单据体-子表 | 4 | [tctrc_risk_number.md](./tctrc_risk_number.md) |
| 51 | `t_tctrc_risk_guide_2` | 高于风险指引单据体-子表 | 4 | [tctrc_risk_sampling.md](./tctrc_risk_sampling.md) |
| 52 | `t_tctrc_risk_guide_3` | 低于正常指引单据体-子表 | 4 | [tctrc_element_verify.md](./tctrc_element_verify.md) |
| 53 | `t_tctrc_risk_guide_3` | 低于正常指引单据体-子表 | 4 | [tctrc_risk_number.md](./tctrc_risk_number.md) |
| 54 | `t_tctrc_risk_guide_3` | 低于正常指引单据体-子表 | 4 | [tctrc_risk_sampling.md](./tctrc_risk_sampling.md) |
| 55 | `t_tctrc_risk_guide_4` | 低于风险指引单据体-子表 | 4 | [tctrc_element_verify.md](./tctrc_element_verify.md) |
| 56 | `t_tctrc_risk_guide_4` | 低于风险指引单据体-子表 | 4 | [tctrc_risk_number.md](./tctrc_risk_number.md) |
| 57 | `t_tctrc_risk_guide_4` | 低于风险指引单据体-子表 | 4 | [tctrc_risk_sampling.md](./tctrc_risk_sampling.md) |
| 58 | `t_tctrc_risk_label` | 标签单据体-子表 | 4 | [tctrc_element_verify.md](./tctrc_element_verify.md) |
| 59 | `t_tctrc_risk_label` | 单据体-子表 | 4 | [tctrc_risk_definition.md](./tctrc_risk_definition.md) |
| 60 | `t_tctrc_risk_label` | 标签单据体-子表 | 4 | [tctrc_risk_number.md](./tctrc_risk_number.md) |
| 61 | `t_tctrc_risk_label` | 标签单据体-子表 | 4 | [tctrc_risk_sampling.md](./tctrc_risk_sampling.md) |
| 62 | `t_tctrc_risk_level` | 风险等级-主表 | 11 | [tctrc_risk_level.md](./tctrc_risk_level.md) |
| 63 | `t_tctrc_risk_level_l` | 风险等级-多语言表 | 4 | [tctrc_risk_level.md](./tctrc_risk_level.md) |
| 64 | `t_tctrc_risk_offset` | 单据体-子表 | 19 | [tctrc_risk_definition.md](./tctrc_risk_definition.md) |
| 65 | `t_tctrc_risk_offset` | 偏差设置单据体-子表 | 19 | [tctrc_risk_number.md](./tctrc_risk_number.md) |
| 66 | `t_tctrc_risk_policies` | 政策法规指引单据体-子表 | 6 | [tctrc_element_verify.md](./tctrc_element_verify.md) |
| 67 | `t_tctrc_risk_policies` | 单据体-子表 | 6 | [tctrc_risk_definition.md](./tctrc_risk_definition.md) |
| 68 | `t_tctrc_risk_policies` | 政策法规指引单据体-子表 | 6 | [tctrc_risk_number.md](./tctrc_risk_number.md) |
| 69 | `t_tctrc_risk_policies` | 政策法规指引单据体-子表 | 6 | [tctrc_risk_sampling.md](./tctrc_risk_sampling.md) |
| 70 | `t_tctrc_risk_run_list` | 风险运行清单-主表 | 12 | [tctrc_risk_run_list.md](./tctrc_risk_run_list.md) |
| 71 | `t_tctrc_risk_run_log` | 风险计算日志-主表 | 8 | [tctrc_risk_run_log.md](./tctrc_risk_run_log.md) |
| 72 | `t_tctrc_risk_run_result` | 风险处理列表-主表 | 27 | [tctrc_handle_list.md](./tctrc_handle_list.md) |
| 73 | `t_tctrc_risk_run_result` | 风险结果查询-主表 | 27 | [tctrc_risk_run_result.md](./tctrc_risk_run_result.md) |
| 74 | `t_tctrc_risk_score_djt` | 单据体-子表 | 7 | [tctrc_risk_score_scheme.md](./tctrc_risk_score_scheme.md) |
| 75 | `t_tctrc_risk_score_scheme` | 风险得分方案-主表 | 15 | [tctrc_risk_score_scheme.md](./tctrc_risk_score_scheme.md) |
| 76 | `t_tctrc_risk_score_scheme_l` | 风险得分方案-多语言表 | 4 | [tctrc_risk_score_scheme.md](./tctrc_risk_score_scheme.md) |
| 77 | `t_tctrc_riskch_record_djt` | 单据体-子表 | 40 | [tctrc_riskcheck_record.md](./tctrc_riskcheck_record.md) |
| 78 | `t_tctrc_riskcheck_record` | 风险检查概况历史记录表-主表 | 8 | [tctrc_riskcheck_record.md](./tctrc_riskcheck_record.md) |
| 79 | `t_tctrc_risklevel_explain` | 风险定义-子表 | 7 | [tctrc_element_verify.md](./tctrc_element_verify.md) |
| 80 | `t_tctrc_risklevel_explain` | 风险定义-子表 | 7 | [tctrc_risk_sampling.md](./tctrc_risk_sampling.md) |
| 81 | `t_tctrc_sharingplan` | 共享方案-子表 | 5 | [tctrc_risk_assign.md](./tctrc_risk_assign.md) |
| 82 | `t_tctrc_sharingplan_orgs` | 被共享组织（废弃-21.4）-子表 | 4 | [tctrc_risk_assign.md](./tctrc_risk_assign.md) |
| 83 | `t_tctrc_sharingplan_risks` | 风险-子表 | 4 | [tctrc_risk_assign.md](./tctrc_risk_assign.md) |
| 84 | `t_tctrc_sharingplan_sub` | 子单据体（新）-子表 | 3 | [tctrc_risk_assign.md](./tctrc_risk_assign.md) |
| 85 | `t_tctrc_sharingplan_sub_a` | 选择共享组织属性-多选基础资料表 | 3 | [tctrc_risk_assign.md](./tctrc_risk_assign.md) |
| 86 | `t_tctrc_sharingplan_sub_o` | 选择共享税务组织-多选基础资料表 | 3 | [tctrc_risk_assign.md](./tctrc_risk_assign.md) |
| 87 | `t_tctrc_sheet_record_djt` | 单据体-子表 | 9 | [tctrc_balanc_sheet_record.md](./tctrc_balanc_sheet_record.md) |
| 88 | `t_tctrc_taxati_record_djt` | 单据体-子表 | 14 | [tctrc_taxation_record.md](./tctrc_taxation_record.md) |
| 89 | `t_tctrc_taxation_record` | 税金分布历史记录表-主表 | 2 | [tctrc_taxation_record.md](./tctrc_taxation_record.md) |
| 90 | `t_tctrc_taxtypemul` | 税种-多选基础资料表 | 3 | [tctrc_element_verify.md](./tctrc_element_verify.md) |
| 91 | `t_tctrc_taxtypemul` | 税种-多选基础资料表 | 3 | [tctrc_risk_definition.md](./tctrc_risk_definition.md) |
| 92 | `t_tctrc_taxtypemul` | 税种-多选基础资料表 | 3 | [tctrc_risk_number.md](./tctrc_risk_number.md) |
| 93 | `t_tctrc_taxtypemul` | 税种-多选基础资料表 | 3 | [tctrc_risk_sampling.md](./tctrc_risk_sampling.md) |
| 94 | `t_tctrc_variable` | 变量信息-主表 | 20 | [tctrc_variable_info.md](./tctrc_variable_info.md) |
| 95 | `t_tctrc_variable_l` | 变量信息-多语言表 | 4 | [tctrc_variable_info.md](./tctrc_variable_info.md) |
