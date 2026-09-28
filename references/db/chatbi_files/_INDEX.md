# chatbi 模块表清单

> 本模块共收录 **94** 张表定义，来自 `chatbi_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category chatbi
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_cbi_advanced_settings` | 高级配置-主表 | 19 | [cbi_advanced_settings.md](./cbi_advanced_settings.md) |
| 2 | `t_cbi_agent_analysis` | 分析框架-主表 | 10 | [cbi_agent_analysis.md](./cbi_agent_analysis.md) |
| 3 | `t_cbi_agent_analysisentry` | 单据体-子表 | 14 | [cbi_agent_analysis.md](./cbi_agent_analysis.md) |
| 4 | `t_cbi_agent_base` | 智能体-主表 | 12 | [cbi_agent_base.md](./cbi_agent_base.md) |
| 5 | `t_cbi_agent_baseinfo` | 智能体基本信息-主表 | 9 | [cbi_agent_baseinfo.md](./cbi_agent_baseinfo.md) |
| 6 | `t_cbi_agent_biz_fallback` | 兜底配置-子表 | 11 | [cbi_agent_bizdata.md](./cbi_agent_bizdata.md) |
| 7 | `t_cbi_agent_biz_filtercf` | 口语化过滤条件配置-子表 | 10 | [cbi_agent_bizdata.md](./cbi_agent_bizdata.md) |
| 8 | `t_cbi_agent_biz_namecf` | 指标维度查数配置-子表 | 11 | [cbi_agent_bizdata.md](./cbi_agent_bizdata.md) |
| 9 | `t_cbi_agent_biz_packagecf` | 业务查数配置-子表 | 10 | [cbi_agent_bizdata.md](./cbi_agent_bizdata.md) |
| 10 | `t_cbi_agent_bizdata` | 智能体_业务查数配置-主表 | 10 | [cbi_agent_bizdata.md](./cbi_agent_bizdata.md) |
| 11 | `t_cbi_agent_dataconfig` | 智能体数据配置-主表 | 13 | [cbi_agent_dataconfig.md](./cbi_agent_dataconfig.md) |
| 12 | `t_cbi_agent_role_config` | 用户身份配置-主表 | 6 | [cbi_agent_role_config.md](./cbi_agent_role_config.md) |
| 13 | `t_cbi_agent_rule` | 规则配置-主表 | 13 | [chatbi_agent_rules.md](./chatbi_agent_rules.md) |
| 14 | `t_cbi_aggr_date_config` | 聚合日期数据源配置-主表 | 4 | [cbi_aggregation_date_conf.md](./cbi_aggregation_date_conf.md) |
| 15 | `t_cbi_assistant` | 连接配置-主表 | 10 | [chatbi_assistant.md](./chatbi_assistant.md) |
| 16 | `t_cbi_assistant_a` | 连接配置-分表 | 11 | [chatbi_assistant.md](./chatbi_assistant.md) |
| 17 | `t_cbi_assistant_d` | 连接配置-分表 | 6 | [chatbi_assistant.md](./chatbi_assistant.md) |
| 18 | `t_cbi_basedata_alias` | 枚举值同义词-子表 | 6 | [cbi_basedata_know.md](./cbi_basedata_know.md) |
| 19 | `t_cbi_basedata_field` | 字段元数据-子表 | 7 | [cbi_basedata_know.md](./cbi_basedata_know.md) |
| 20 | `t_cbi_basedata_know` | 主数据知识库-主表 | 15 | [cbi_basedata_know.md](./cbi_basedata_know.md) |
| 21 | `t_cbi_basedata_know_l` | 主数据知识库-多语言表 | 4 | [cbi_basedata_know.md](./cbi_basedata_know.md) |
| 22 | `t_cbi_bottom_opt_config` | 兜底优化配置-主表 | 6 | [cbi_bottom_opt_config.md](./cbi_bottom_opt_config.md) |
| 23 | `t_cbi_chat_feedback` | 对话反馈列表-主表 | 5 | [cbi_chat_feedback.md](./cbi_chat_feedback.md) |
| 24 | `t_cbi_chat_record` | 历史对话-主表 | 31 | [cbi_chat_record.md](./cbi_chat_record.md) |
| 25 | `t_cbi_config` | 参数配置-主表 | 15 | [chatbi_config.md](./chatbi_config.md) |
| 26 | `t_cbi_datamodel` | 指标模型-主表 | 10 | [cbi_agent_datamodel.md](./cbi_agent_datamodel.md) |
| 27 | `t_cbi_datamodel_cnfd` | 指标语义-子表 | 30 | [cbi_datamodel_semcnf.md](./cbi_datamodel_semcnf.md) |
| 28 | `t_cbi_datamodel_dimcnf` | 单据体1-子表 | 0 | [cbi_datamodel_semamtic.md](./cbi_datamodel_semamtic.md) |
| 29 | `t_cbi_datamodel_indcnf` | 单据体3-子表 | 0 | [cbi_datamodel_semamtic.md](./cbi_datamodel_semamtic.md) |
| 30 | `t_cbi_datamodel_levcnf` | 单据体2-子表 | 0 | [cbi_datamodel_semamtic.md](./cbi_datamodel_semamtic.md) |
| 31 | `t_cbi_datamodel_metricmap` | 指标映射配置-主表 | 0 | [cbi_datamodel_metricmap.md](./cbi_datamodel_metricmap.md) |
| 32 | `t_cbi_datamodel_prompt` | 单据体-子表 | 9 | [cbi_advanced_settings.md](./cbi_advanced_settings.md) |
| 33 | `t_cbi_datamodel_semamtic` | 指标语义配置-主表 | 0 | [cbi_datamodel_semamtic.md](./cbi_datamodel_semamtic.md) |
| 34 | `t_cbi_datamodel_semcnf` | 指标语义配置-主表 | 3 | [cbi_datamodel_semcnf.md](./cbi_datamodel_semcnf.md) |
| 35 | `t_cbi_dataset_dmcf` | 维度层级配置-主表 | 2 | [chatbi_dataset_demconfig.md](./chatbi_dataset_demconfig.md) |
| 36 | `t_cbi_dataset_dmdetails` | 单据体-子表 | 7 | [chatbi_dataset_demconfig.md](./chatbi_dataset_demconfig.md) |
| 37 | `t_cbi_dataset_indexcfdata` | 指标展示配置-子表 | 7 | [cbi_dataset_indexconfig.md](./cbi_dataset_indexconfig.md) |
| 38 | `t_cbi_dataset_indexconfig` | 指标展示配置-主表 | 2 | [cbi_dataset_indexconfig.md](./cbi_dataset_indexconfig.md) |
| 39 | `t_cbi_dataset_interpretio` | 数据解读配置-主表 | 4 | [cbi_dataset_interpretion.md](./cbi_dataset_interpretion.md) |
| 40 | `t_cbi_datasource` | 数据源-主表 | 20 | [cbi_datasource.md](./cbi_datasource.md) |
| 41 | `t_cbi_datasource_config` | 数据源日期聚合方式-子表 | 7 | [cbi_aggregation_date_conf.md](./cbi_aggregation_date_conf.md) |
| 42 | `t_cbi_datasource_date_cnf` | 数据源日期聚合方式-子表 | 0 | [cbi_datamodel_metricmap.md](./cbi_datamodel_metricmap.md) |
| 43 | `t_cbi_datasource_file` | -附件表 | 3 | [cbi_datasource.md](./cbi_datasource.md) |
| 44 | `t_cbi_datasource_meta` | 字段元数据-子表 | 15 | [cbi_datasource.md](./cbi_datasource.md) |
| 45 | `t_cbi_dbconfig` | 数据连接-主表 | 18 | [chatbi_dbconfig_base.md](./chatbi_dbconfig_base.md) |
| 46 | `t_cbi_dimen_att_config` | 维度归因配置-主表 | 10 | [cbi_dimension_att_config.md](./cbi_dimension_att_config.md) |
| 47 | `t_cbi_dimension_associate` | 关联维度单据体-子表 | 4 | [cbi_dimension_config.md](./cbi_dimension_config.md) |
| 48 | `t_cbi_dimension_bill` | 维度清单-子表 | 7 | [cbi_datamodel_metricmap.md](./cbi_datamodel_metricmap.md) |
| 49 | `t_cbi_dimension_bill` | 维度清单-子表 | 7 | [cbi_dimension_config.md](./cbi_dimension_config.md) |
| 50 | `t_cbi_dimension_conf_tree` | 维度层级配置-子表 | 5 | [cbi_dimension_config.md](./cbi_dimension_config.md) |
| 51 | `t_cbi_dimension_config` | 维度配置-主表 | 4 | [cbi_dimension_config.md](./cbi_dimension_config.md) |
| 52 | `t_cbi_dimension_val_conf` | 维度值配置-子表 | 8 | [cbi_agent_dataconfig.md](./cbi_agent_dataconfig.md) |
| 53 | `t_cbi_display_config` | 展示配置-主表 | 3 | [cbi_display_config.md](./cbi_display_config.md) |
| 54 | `t_cbi_dm_dim_attr_config` | 维度归因-主表 | 9 | [cbi_dm_dim_attr_config.md](./cbi_dm_dim_attr_config.md) |
| 55 | `t_cbi_dm_subcaliber` | 子口径-子表 | 0 | [cbi_datamodel_metricmap.md](./cbi_datamodel_metricmap.md) |
| 56 | `t_cbi_dsvalue_mapping` | 维度值映射配置-主表 | 2 | [cbi_dsvalue_mapping.md](./cbi_dsvalue_mapping.md) |
| 57 | `t_cbi_dsvalue_mapping_cf` | 指标展示配置-子表 | 9 | [cbi_dsvalue_mapping.md](./cbi_dsvalue_mapping.md) |
| 58 | `t_cbi_fallback_response` | 兜底配置-子表 | 11 | [cbi_agent_baseinfo.md](./cbi_agent_baseinfo.md) |
| 59 | `t_cbi_flat_dimensions` | 单据体-子表 | 6 | [cbi_datamodel_metricmap.md](./cbi_datamodel_metricmap.md) |
| 60 | `t_cbi_flat_dimensions` | 展平维度-子表 | 6 | [cbi_dimension_config.md](./cbi_dimension_config.md) |
| 61 | `t_cbi_indicator_bill` | 指标清单单据体-子表 | 0 | [cbi_datamodel_metricmap.md](./cbi_datamodel_metricmap.md) |
| 62 | `t_cbi_join_message_cnf` | 子单据体-子表 | 6 | [cbi_datamodel_semcnf.md](./cbi_datamodel_semcnf.md) |
| 63 | `t_cbi_legal_document` | 法律文件-主表 | 11 | [chatbi_legal_document.md](./chatbi_legal_document.md) |
| 64 | `t_cbi_legal_document_l` | 法律文件-多语言表 | 4 | [chatbi_legal_document.md](./chatbi_legal_document.md) |
| 65 | `t_cbi_metric_tree` | 单据体-子表 | 11 | [cbi_datamodel_metric_tree.md](./cbi_datamodel_metric_tree.md) |
| 66 | `t_cbi_metric_tree_config` | 指标树-主表 | 2 | [cbi_datamodel_metric_tree.md](./cbi_datamodel_metric_tree.md) |
| 67 | `t_cbi_predictive_cnf` | 预测分析配置-主表 | 4 | [cbi_predictive_config.md](./cbi_predictive_config.md) |
| 68 | `t_cbi_privacy_management` | 隐私签署管理-主表 | 12 | [chatbi_privacy_agreement.md](./chatbi_privacy_agreement.md) |
| 69 | `t_cbi_question_rewriting` | 树形单据体-子表 | 7 | [cbi_advanced_settings.md](./cbi_advanced_settings.md) |
| 70 | `t_cbi_recommend_queries` | 单据体-子表 | 4 | [cbi_display_config.md](./cbi_display_config.md) |
| 71 | `t_cbi_role_config` | 用户身份配置-子表 | 7 | [cbi_agent_role_config.md](./cbi_agent_role_config.md) |
| 72 | `t_cbi_roleconfig` | 用户身份配置-主表 | 7 | [chatbi_role_config.md](./chatbi_role_config.md) |
| 73 | `t_cbi_trd_metric` | 第三方指标-主表 | 14 | [cbi_trd_metric.md](./cbi_trd_metric.md) |
| 74 | `t_cbi_workflow` | 工作流管理-主表 | 10 | [chatbi_workflow.md](./chatbi_workflow.md) |
| 75 | `t_cbi_workflow` | 工作流基础资料-主表 | 10 | [chatbi_workflow_base.md](./chatbi_workflow_base.md) |
| 76 | `t_cbi_workflow_file` | 工作流文件-附件表 | 3 | [chatbi_workflow.md](./chatbi_workflow.md) |
| 77 | `t_cbi_workflow_http` | 单据体-子表 | 7 | [chatbi_workflow.md](./chatbi_workflow.md) |
| 78 | `t_cbi_workflow_model` | 单据体-子表 | 9 | [chatbi_workflow.md](./chatbi_workflow.md) |
| 79 | `t_cbi_workflow_tool` | 单据体-子表 | 8 | [chatbi_workflow.md](./chatbi_workflow.md) |
| 80 | `t_gai_cbi_assistant_agent` | 适用智能体-多选基础资料表 | 3 | [chatbi_assistant.md](./chatbi_assistant.md) |
| 81 | `t_gai_cbi_assistant_conn` | 单据体-子表 | 25 | [chatbi_assistant.md](./chatbi_assistant.md) |
| 82 | `t_gai_cbi_assistant_theme` | 适用主题-多选基础资料表 | 3 | [chatbi_assistant.md](./chatbi_assistant.md) |
| 83 | `t_gai_cbi_business_word` | 单据体_业务名词知识库-子表 | 11 | [gai_cbi_theme_singledata.md](./gai_cbi_theme_singledata.md) |
| 84 | `t_gai_cbi_caseset` | 单据体_案例集-子表 | 11 | [gai_cbi_theme_singledata.md](./gai_cbi_theme_singledata.md) |
| 85 | `t_gai_cbi_config` | 向量配置-主表 | 8 | [gai_cbi_config.md](./gai_cbi_config.md) |
| 86 | `t_gai_cbi_dataset` | 数据集-主表 | 22 | [gai_cbi_dataset.md](./gai_cbi_dataset.md) |
| 87 | `t_gai_cbi_dataset_l` | 数据集-多语言表 | 4 | [gai_cbi_dataset.md](./gai_cbi_dataset.md) |
| 88 | `t_gai_cbi_dataset_meta` | 字段元数据-子表 | 14 | [gai_cbi_dataset.md](./gai_cbi_dataset.md) |
| 89 | `t_gai_cbi_fieldconfig` | 单据体_字段语义配置-子表 | 17 | [gai_cbi_theme_singledata.md](./gai_cbi_theme_singledata.md) |
| 90 | `t_gai_cbi_prompt_config` | 单据体_业务提示词配置-子表 | 14 | [gai_cbi_theme_singledata.md](./gai_cbi_theme_singledata.md) |
| 91 | `t_gai_cbi_show_config` | 展示配置单据体-子表 | 9 | [gai_cbi_theme_singledata.md](./gai_cbi_theme_singledata.md) |
| 92 | `t_gai_cbi_single_scheme` | 主题基础资料-主表 | 17 | [gai_cbi_theme_basedata.md](./gai_cbi_theme_basedata.md) |
| 93 | `t_gai_cbi_single_scheme` | 主题-主表 | 17 | [gai_cbi_theme_singledata.md](./gai_cbi_theme_singledata.md) |
| 94 | `t_gai_cbi_theme_dataset` | 单据体_数据集配置-子表 | 11 | [gai_cbi_theme_singledata.md](./gai_cbi_theme_singledata.md) |
