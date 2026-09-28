# fgptas 模块表清单

> 本模块共收录 **30** 张表定义，来自 `fgptas_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category fgptas
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fa_asset_req_e` | 真单据体-子表 | 8 | [fa_asset_requisition_copy.md](./fa_asset_requisition_copy.md) |
| 2 | `t_fa_asset_requisition` | 资产领用单_复制-主表 | 22 | [fa_asset_requisition_copy.md](./fa_asset_requisition_copy.md) |
| 3 | `t_fa_asset_requisition_lk` | 关联子实体-子表 | 6 | [fa_asset_requisition_copy.md](./fa_asset_requisition_copy.md) |
| 4 | `t_fa_asset_requisition_tc` | 资产领用单_复制-关联追踪表 | 7 | [fa_asset_requisition_copy.md](./fa_asset_requisition_copy.md) |
| 5 | `t_fa_asset_requisition_wb` | 资产领用单_复制-反写记录表 | 10 | [fa_asset_requisition_copy.md](./fa_asset_requisition_copy.md) |
| 6 | `t_fgpta_datasource` | 数据来源-子表 | 9 | [fgptas_fireport_template.md](./fgptas_fireport_template.md) |
| 7 | `t_fgptas_audit` | 附件审核-主表 | 15 | [fgptas_billaudit.md](./fgptas_billaudit.md) |
| 8 | `t_fgptas_auditconf` | 审核要素配置-主表 | 20 | [fgptas_auditconfig.md](./fgptas_auditconfig.md) |
| 9 | `t_fgptas_auditconf_l` | 审核要素配置-多语言表 | 4 | [fgptas_auditconfig.md](./fgptas_auditconfig.md) |
| 10 | `t_fgptas_confirmlog` | 财务AI助手试用确认日志-主表 | 4 | [fgptas_confirmlog.md](./fgptas_confirmlog.md) |
| 11 | `t_fgptas_datarequire` | 数据整体要求-多选基础资料表 | 3 | [fgptas_fireport_template.md](./fgptas_fireport_template.md) |
| 12 | `t_fgptas_datatable` | 数据表配置-主表 | 25 | [fgptas_datatable.md](./fgptas_datatable.md) |
| 13 | `t_fgptas_datatable_l` | 数据表配置-多语言表 | 5 | [fgptas_datatable.md](./fgptas_datatable.md) |
| 14 | `t_fgptas_datatable_u` | 数据表配置-使用范围表 | 3 | [fgptas_datatable.md](./fgptas_datatable.md) |
| 15 | `t_fgptas_datatablefield` | 数据表字段-子表 | 14 | [fgptas_datatable.md](./fgptas_datatable.md) |
| 16 | `t_fgptas_datatablefield_l` | 数据表字段-多语言表 | 5 | [fgptas_datatable.md](./fgptas_datatable.md) |
| 17 | `t_fgptas_element` | 审核要素明细-子表 | 6 | [fgptas_auditconfig.md](./fgptas_auditconfig.md) |
| 18 | `t_fgptas_outline` | 报告大纲-子表 | 11 | [fgptas_fireport_template.md](./fgptas_fireport_template.md) |
| 19 | `t_fgptas_report` | 财务报告-主表 | 19 | [fgptas_report.md](./fgptas_report.md) |
| 20 | `t_fgptas_report_gptlog` | GPT提示调用日志-主表 | 16 | [fgptas_report_gptlog.md](./fgptas_report_gptlog.md) |
| 21 | `t_fgptas_report_l` | 财务报告-多语言表 | 4 | [fgptas_report.md](./fgptas_report.md) |
| 22 | `t_fgptas_report_type` | 财务报告类型-主表 | 12 | [fgptas_report_type.md](./fgptas_report_type.md) |
| 23 | `t_fgptas_report_type_l` | 财务报告类型-多语言表 | 4 | [fgptas_report_type.md](./fgptas_report_type.md) |
| 24 | `t_fgptas_reporttempl` | 财务报告模版-主表 | 24 | [fgptas_fireport_template.md](./fgptas_fireport_template.md) |
| 25 | `t_fgptas_reporttempl_l` | 财务报告模版-多语言表 | 6 | [fgptas_fireport_template.md](./fgptas_fireport_template.md) |
| 26 | `t_fgptas_reporttempl_u` | 财务报告模版-使用范围表 | 3 | [fgptas_fireport_template.md](./fgptas_fireport_template.md) |
| 27 | `t_fgptas_skillaccesslog` | 技能访问日志-主表 | 6 | [fgptas_skillaccesslog.md](./fgptas_skillaccesslog.md) |
| 28 | `t_fgptas_tablecol` | 数据表字段映射-主表 | 11 | [fgptas_tablecol_mapping.md](./fgptas_tablecol_mapping.md) |
| 29 | `t_fgptas_tablecol_entry` | 映射关系-子表 | 6 | [fgptas_tablecol_mapping.md](./fgptas_tablecol_mapping.md) |
| 30 | `t_fgptas_tablecol_l` | 数据表字段映射-多语言表 | 4 | [fgptas_tablecol_mapping.md](./fgptas_tablecol_mapping.md) |
