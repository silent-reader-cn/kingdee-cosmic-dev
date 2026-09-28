# idi 模块表清单

> 本模块共收录 **29** 张表定义，来自 `idi_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category idi
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_idi_accept_log` | 接受记录-主表 | 6 | [idi_accept_log.md](./idi_accept_log.md) |
| 2 | `t_idi_api_config` | API配置-主表 | 14 | [idi_api_config.md](./idi_api_config.md) |
| 3 | `t_idi_api_config_l` | API配置-多语言表 | 4 | [idi_api_config.md](./idi_api_config.md) |
| 4 | `t_idi_api_param_config` | 参数信息-子表 | 6 | [idi_api_config.md](./idi_api_config.md) |
| 5 | `t_idi_attachmentfield` | 附件字段-主表 | 16 | [idi_attachmentfield.md](./idi_attachmentfield.md) |
| 6 | `t_idi_attachmentfield_l` | 附件字段-多语言表 | 4 | [idi_attachmentfield.md](./idi_attachmentfield.md) |
| 7 | `t_idi_decisionextentry` | 源单-多选基础资料表 | 3 | [idi_decision_extinfo.md](./idi_decision_extinfo.md) |
| 8 | `t_idi_decisionextinfo` | 检查项扩展-主表 | 23 | [idi_decision_extinfo.md](./idi_decision_extinfo.md) |
| 9 | `t_idi_decisionextinfo_l` | 检查项扩展-多语言表 | 4 | [idi_decision_extinfo.md](./idi_decision_extinfo.md) |
| 10 | `t_idi_decisionschema` | 决策方案-主表 | 19 | [idi_schema.md](./idi_schema.md) |
| 11 | `t_idi_decisionschema_l` | 决策方案-多语言表 | 5 | [idi_schema.md](./idi_schema.md) |
| 12 | `t_idi_fgptastemplatref` | ai附件模板引用关系-主表 | 6 | [idi_fgptastemplatrefrence.md](./idi_fgptastemplatrefrence.md) |
| 13 | `t_idi_fieldgroup` | 附件模板分类-主表 | 15 | [idi_fieldgroup.md](./idi_fieldgroup.md) |
| 14 | `t_idi_fieldgroup_l` | 附件模板分类-多语言表 | 5 | [idi_fieldgroup.md](./idi_fieldgroup.md) |
| 15 | `t_idi_invoice` | 发票云发票识别结果-主表 | 21 | [idi_invoice.md](./idi_invoice.md) |
| 16 | `t_idi_invoiceentrykey` | 单据体-子表 | 6 | [idi_invoice.md](./idi_invoice.md) |
| 17 | `t_idi_invoicekey` | 单据体-子表 | 5 | [idi_invoice.md](./idi_invoice.md) |
| 18 | `t_idi_itemexeresult` | 检查项执行结果-主表 | 16 | [idi_itemexeresult.md](./idi_itemexeresult.md) |
| 19 | `t_idi_keyword_library` | 敏感词库-主表 | 15 | [idi_keyword_library.md](./idi_keyword_library.md) |
| 20 | `t_idi_keyword_library_l` | 敏感词库-多语言表 | 5 | [idi_keyword_library.md](./idi_keyword_library.md) |
| 21 | `t_idi_logistics_data` | 详细物流信息-子表 | 8 | [idi_logistics_info.md](./idi_logistics_info.md) |
| 22 | `t_idi_logistics_info` | 物流信息-主表 | 7 | [idi_logistics_info.md](./idi_logistics_info.md) |
| 23 | `t_idi_logisticserrorinfo` | 物流查询失败信息-主表 | 11 | [idi_logistics_errorinfo.md](./idi_logistics_errorinfo.md) |
| 24 | `t_idi_originattachrecord` | 附件识别原始接口结果-主表 | 9 | [idi_originattachrecord.md](./idi_originattachrecord.md) |
| 25 | `t_idi_param` | 参数配置-主表 | 6 | [idi_param_config.md](./idi_param_config.md) |
| 26 | `t_idi_param_l` | 参数配置-多语言表 | 4 | [idi_param_config.md](./idi_param_config.md) |
| 27 | `t_idi_processattachrecord` | 附件识别解析后的结果记录-主表 | 8 | [idi_processattachrecord.md](./idi_processattachrecord.md) |
| 28 | `t_idi_schema_decision` | 决策方案检查项-主表 | 3 | [idi_schema_decision.md](./idi_schema_decision.md) |
| 29 | `t_idi_schemaexeresult` | 方案执行结果-主表 | 10 | [idi_schemaexeresult.md](./idi_schemaexeresult.md) |
