# tlmgt 模块表清单

> 本模块共收录 **27** 张表定义，来自 `tlmgt_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category tlmgt
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_tlmgt_activity_record` | 活动状态-子表 | 9 | [tlmgt_execute_record.md](./tlmgt_execute_record.md) |
| 2 | `t_tlmgt_activity_scope` | 子单据体-子表 | 13 | [tlmgt_execute_record.md](./tlmgt_execute_record.md) |
| 3 | `t_tlmgt_basedata_config` | 提示语工程配置-主表 | 12 | [tlmgt_basedata_config.md](./tlmgt_basedata_config.md) |
| 4 | `t_tlmgt_basedata_config_l` | 提示语工程配置-多语言表 | 3 | [tlmgt_basedata_config.md](./tlmgt_basedata_config.md) |
| 5 | `t_tlmgt_custom_lang` | 自定义抽取语言-多选基础资料表 | 3 | [tlmgt_extract_scheme.md](./tlmgt_extract_scheme.md) |
| 6 | `t_tlmgt_execute_record` | 抽取方案执行记录-主表 | 12 | [tlmgt_execute_record.md](./tlmgt_execute_record.md) |
| 7 | `t_tlmgt_extr_scheme` | 抽取方案-主表 | 13 | [tlmgt_extract_scheme.md](./tlmgt_extract_scheme.md) |
| 8 | `t_tlmgt_extr_scheme_l` | 抽取方案-多语言表 | 5 | [tlmgt_extract_scheme.md](./tlmgt_extract_scheme.md) |
| 9 | `t_tlmgt_frm_config` | 处理器配置-主表 | 17 | [tlmgt_frm_config.md](./tlmgt_frm_config.md) |
| 10 | `t_tlmgt_frm_config_l` | 处理器配置-多语言表 | 3 | [tlmgt_frm_config.md](./tlmgt_frm_config.md) |
| 11 | `t_tlmgt_frm_match` | 匹配值设置-主表 | 11 | [tlmgt_frm_match.md](./tlmgt_frm_match.md) |
| 12 | `t_tlmgt_frm_match_l` | 匹配值设置-多语言表 | 4 | [tlmgt_frm_match.md](./tlmgt_frm_match.md) |
| 13 | `t_tlmgt_frm_processor` | 处理器基础资料-主表 | 11 | [tlmgt_frm_processor.md](./tlmgt_frm_processor.md) |
| 14 | `t_tlmgt_frm_processor_l` | 处理器基础资料-多语言表 | 4 | [tlmgt_frm_processor.md](./tlmgt_frm_processor.md) |
| 15 | `t_tlmgt_original_file` | 抽取原始文件-主表 | 21 | [tlmgt_original_file.md](./tlmgt_original_file.md) |
| 16 | `t_tlmgt_original_file_l` | 抽取原始文件-多语言表 | 4 | [tlmgt_original_file.md](./tlmgt_original_file.md) |
| 17 | `t_tlmgt_original_word` | 抽取原始词条-主表 | 12 | [tlmgt_original_word.md](./tlmgt_original_word.md) |
| 18 | `t_tlmgt_resource_scope` | 资源范围-子表 | 9 | [tlmgt_extract_scheme.md](./tlmgt_extract_scheme.md) |
| 19 | `t_tlmgt_resource_type` | 资源类型-主表 | 11 | [tlmgt_resource_type.md](./tlmgt_resource_type.md) |
| 20 | `t_tlmgt_resource_type_l` | 资源类型-多语言表 | 4 | [tlmgt_resource_type.md](./tlmgt_resource_type.md) |
| 21 | `t_tlmgt_scheme_resource` | 抽取方案资源-子表 | 5 | [tlmgt_extract_scheme.md](./tlmgt_extract_scheme.md) |
| 22 | `t_tlmgt_standardisv` | 标品开发商标识-主表 | 3 | [tlmgt_standardisv.md](./tlmgt_standardisv.md) |
| 23 | `t_tlmgt_transfile` | 翻译文件-主表 | 19 | [tlmgt_transfile.md](./tlmgt_transfile.md) |
| 24 | `t_tlmgt_transfile_l` | 翻译文件-多语言表 | 4 | [tlmgt_transfile.md](./tlmgt_transfile.md) |
| 25 | `t_tlmgt_wordtype` | 词条类型-主表 | 14 | [tlmgt_wordtype.md](./tlmgt_wordtype.md) |
| 26 | `t_tlmgt_wordtype_l` | 词条类型-多语言表 | 5 | [tlmgt_wordtype.md](./tlmgt_wordtype.md) |
| 27 | `t_tlmgt_wordunit` | 翻译工作台-主表 | 21 | [tlmgt_wordunit.md](./tlmgt_wordunit.md) |
