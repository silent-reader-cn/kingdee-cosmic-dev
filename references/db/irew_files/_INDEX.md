# irew 模块表清单

> 本模块共收录 **27** 张表定义，来自 `irew_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category irew
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_irew_audit_result` | 发票预警结果-主表 | 25 | [irew_audit_result.md](./irew_audit_result.md) |
| 2 | `t_irew_audit_result_item` | 单据体-子表 | 6 | [irew_audit_result.md](./irew_audit_result.md) |
| 3 | `t_irew_engine` | 发票校验引擎-主表 | 28 | [irew_engine.md](./irew_engine.md) |
| 4 | `t_irew_engine_accord` | 引擎规则依据单据体-子表 | 5 | [irew_engine.md](./irew_engine.md) |
| 5 | `t_irew_engine_l` | 发票校验引擎-多语言表 | 4 | [irew_engine.md](./irew_engine.md) |
| 6 | `t_irew_engine_m` | 发票校验引擎-使用范围位图表 | 2 | [irew_engine.md](./irew_engine.md) |
| 7 | `t_irew_engine_queryconfig` | 单据体-子表 | 9 | [irew_engine.md](./irew_engine.md) |
| 8 | `t_irew_engine_queryfield` | 展示字段单据体-子表 | 7 | [irew_engine.md](./irew_engine.md) |
| 9 | `t_irew_engine_relation` | 关系单据体-子表 | 8 | [irew_engine.md](./irew_engine.md) |
| 10 | `t_irew_engine_rule` | 发票数据校验规则单据体-子表 | 8 | [irew_engine.md](./irew_engine.md) |
| 11 | `t_irew_engine_source` | 数据源单据体-子表 | 6 | [irew_engine.md](./irew_engine.md) |
| 12 | `t_irew_engine_sourcerule` | 其他数据源校验规则单据体-子表 | 11 | [irew_engine.md](./irew_engine.md) |
| 13 | `t_irew_engine_u` | 发票校验引擎-使用范围表 | 3 | [irew_engine.md](./irew_engine.md) |
| 14 | `t_irew_false_check_log` | 虚开发票数据推送日志-主表 | 11 | [irew_false_check_log.md](./irew_false_check_log.md) |
| 15 | `t_irew_false_invoice` | 发票-子表 | 7 | [irew_false_check_log.md](./irew_false_check_log.md) |
| 16 | `t_irew_query_condition` | 查询条件-主表 | 10 | [irew_query_condition.md](./irew_query_condition.md) |
| 17 | `t_irew_query_condition_l` | 查询条件-多语言表 | 4 | [irew_query_condition.md](./irew_query_condition.md) |
| 18 | `t_irew_scheme` | 发票预警方案-主表 | 23 | [irew_scheme.md](./irew_scheme.md) |
| 19 | `t_irew_scheme_condition` | 查询条件分录-子表 | 8 | [irew_scheme.md](./irew_scheme.md) |
| 20 | `t_irew_scheme_engine` | 引擎清单-子表 | 5 | [irew_scheme.md](./irew_scheme.md) |
| 21 | `t_irew_scheme_exptype` | 校验单据类型-多选基础资料表 | 3 | [irew_scheme.md](./irew_scheme.md) |
| 22 | `t_irew_scheme_l` | 发票预警方案-多语言表 | 4 | [irew_scheme.md](./irew_scheme.md) |
| 23 | `t_irew_scheme_log` | 预警方案执行日志-主表 | 10 | [irew_scheme_log.md](./irew_scheme_log.md) |
| 24 | `t_irew_scheme_log_items` | 引擎明细-子表 | 8 | [irew_scheme_log.md](./irew_scheme_log.md) |
| 25 | `t_irew_scheme_m` | 发票预警方案-使用范围位图表 | 2 | [irew_scheme.md](./irew_scheme.md) |
| 26 | `t_irew_scheme_u` | 发票预警方案-使用范围表 | 3 | [irew_scheme.md](./irew_scheme.md) |
| 27 | `t_irew_scheme_useorg` | 方案适用组织-多选基础资料表 | 3 | [irew_scheme.md](./irew_scheme.md) |
