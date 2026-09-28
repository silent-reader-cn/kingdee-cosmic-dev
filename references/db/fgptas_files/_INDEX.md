# fgptas 模块表清单

> 本模块共收录 **43** 张表定义，来自 `fgptas_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category fgptas
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fgptas_audit` | 附件审核-主表 | 15 | [fgptas_billaudit.md](./fgptas_billaudit.md) |
| 2 | `t_fgptas_confirmlog` | 财务AI助手试用确认日志-主表 | 4 | [fgptas_confirmlog.md](./fgptas_confirmlog.md) |
| 3 | `t_fgptas_datatableconfig` | 数据来源-主表 | 22 | [fgptas_datatableconfig.md](./fgptas_datatableconfig.md) |
| 4 | `t_fgptas_datatableconfig_l` | 数据来源-多语言表 | 4 | [fgptas_datatableconfig.md](./fgptas_datatableconfig.md) |
| 5 | `t_fgptas_dtxkdatasr` | 数据表数据规范-子表 | 8 | [fgptas_datatableconfig.md](./fgptas_datatableconfig.md) |
| 6 | `t_fgptas_dtxkdatasr_l` | 数据表数据规范-多语言表 | 5 | [fgptas_datatableconfig.md](./fgptas_datatableconfig.md) |
| 7 | `t_fgptas_dtxkprojectsr` | 报表项目规范-子表 | 7 | [fgptas_datatableconfig.md](./fgptas_datatableconfig.md) |
| 8 | `t_fgptas_dtxkprojectsr_l` | 报表项目规范-多语言表 | 5 | [fgptas_datatableconfig.md](./fgptas_datatableconfig.md) |
| 9 | `t_fgptas_externaldata` | 外部数据-主表 | 18 | [fgptas_externaldata.md](./fgptas_externaldata.md) |
| 10 | `t_fgptas_fireport` | 财务报告-主表 | 18 | [fgptas_fireport.md](./fgptas_fireport.md) |
| 11 | `t_fgptas_fireport_l` | 财务报告-多语言表 | 4 | [fgptas_fireport.md](./fgptas_fireport.md) |
| 12 | `t_fgptas_fireportgenlog` | 财务报告生成记录-主表 | 20 | [fgptas_fireportgenlog.md](./fgptas_fireportgenlog.md) |
| 13 | `t_fgptas_fireportgenlog_l` | 财务报告生成记录-多语言表 | 5 | [fgptas_fireportgenlog.md](./fgptas_fireportgenlog.md) |
| 14 | `t_fgptas_fireporttemplate` | 财务报告模板-主表 | 16 | [fgptas_fireporttemplate.md](./fgptas_fireporttemplate.md) |
| 15 | `t_fgptas_fireporttemplate_l` | 财务报告模板-多语言表 | 4 | [fgptas_fireporttemplate.md](./fgptas_fireporttemplate.md) |
| 16 | `t_fgptas_llmprompts` | 大模型提示词-主表 | 3 | [fgptas_prompts.md](./fgptas_prompts.md) |
| 17 | `t_fgptas_llmprompts_l` | 大模型提示词-多语言表 | 4 | [fgptas_prompts.md](./fgptas_prompts.md) |
| 18 | `t_fgptas_otbasicinfo` | 外部数据表基本信息-子表 | 10 | [fgptas_outer_datatable.md](./fgptas_outer_datatable.md) |
| 19 | `t_fgptas_otbasicinfo_l` | 外部数据表基本信息-多语言表 | 5 | [fgptas_outer_datatable.md](./fgptas_outer_datatable.md) |
| 20 | `t_fgptas_otdtfield` | 外部数据表字段-子表 | 7 | [fgptas_outer_datatable.md](./fgptas_outer_datatable.md) |
| 21 | `t_fgptas_otdtfield_l` | 外部数据表字段-多语言表 | 5 | [fgptas_outer_datatable.md](./fgptas_outer_datatable.md) |
| 22 | `t_fgptas_otifsrentry` | 外部数据表数据规范-子表 | 8 | [fgptas_datatableconfig.md](./fgptas_datatableconfig.md) |
| 23 | `t_fgptas_otifsrentry_l` | 外部数据表数据规范-多语言表 | 4 | [fgptas_datatableconfig.md](./fgptas_datatableconfig.md) |
| 24 | `t_fgptas_ottb_test001` | 外部数据基础资料(测试专用)-主表 | 0 | [fgptas_ottb_test001.md](./fgptas_ottb_test001.md) |
| 25 | `t_fgptas_outer_datatable` | 外部数据表-主表 | 14 | [fgptas_outer_datatable.md](./fgptas_outer_datatable.md) |
| 26 | `t_fgptas_outer_datatable_l` | 外部数据表-多语言表 | 4 | [fgptas_outer_datatable.md](./fgptas_outer_datatable.md) |
| 27 | `t_fgptas_paragraphcr` | 内容要求-子表 | 10 | [fgptas_reportparagraph.md](./fgptas_reportparagraph.md) |
| 28 | `t_fgptas_paragraphcr` | 内容要求-子表 | 10 | [fgptas_templparagraph.md](./fgptas_templparagraph.md) |
| 29 | `t_fgptas_paragraphds` | 数据来源-子表 | 7 | [fgptas_reportparagraph.md](./fgptas_reportparagraph.md) |
| 30 | `t_fgptas_paragraphds` | 数据来源-子表 | 7 | [fgptas_templparagraph.md](./fgptas_templparagraph.md) |
| 31 | `t_fgptas_reportparagraph` | 财务报告章节-主表 | 15 | [fgptas_reportparagraph.md](./fgptas_reportparagraph.md) |
| 32 | `t_fgptas_reportparagraph_l` | 财务报告章节-多语言表 | 5 | [fgptas_reportparagraph.md](./fgptas_reportparagraph.md) |
| 33 | `t_fgptas_skillaccesslog` | 技能访问日志-主表 | 6 | [fgptas_skillaccesslog.md](./fgptas_skillaccesslog.md) |
| 34 | `t_fgptas_tablecolmapping` | 查询参数-主表 | 15 | [fgptas_tablecolmapping.md](./fgptas_tablecolmapping.md) |
| 35 | `t_fgptas_tablecolmapping_l` | 查询参数-多语言表 | 4 | [fgptas_tablecolmapping.md](./fgptas_tablecolmapping.md) |
| 36 | `t_fgptas_taskreporttmpl` | 报告模板-子表 | 11 | [fgptas_taskschedule.md](./fgptas_taskschedule.md) |
| 37 | `t_fgptas_taskschedule` | 财务报告生成定时方案-主表 | 14 | [fgptas_taskschedule.md](./fgptas_taskschedule.md) |
| 38 | `t_fgptas_taskschedule_l` | 财务报告生成定时方案-多语言表 | 4 | [fgptas_taskschedule.md](./fgptas_taskschedule.md) |
| 39 | `t_fgptas_templ_qparam` | 查询参数-多选基础资料表 | 3 | [fgptas_fireporttemplate.md](./fgptas_fireporttemplate.md) |
| 40 | `t_fgptas_templateoutline` | 报告大纲-子表 | 10 | [fgptas_fireporttemplate.md](./fgptas_fireporttemplate.md) |
| 41 | `t_fgptas_templateoutline_l` | 报告大纲-多语言表 | 4 | [fgptas_fireporttemplate.md](./fgptas_fireporttemplate.md) |
| 42 | `t_fgptas_templparagraph` | 财务报告章节-主表 | 13 | [fgptas_templparagraph.md](./fgptas_templparagraph.md) |
| 43 | `t_fgptas_templparagraph_l` | 财务报告章节-多语言表 | 5 | [fgptas_templparagraph.md](./fgptas_templparagraph.md) |
