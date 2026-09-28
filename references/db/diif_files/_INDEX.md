# diif 模块表清单

> 本模块共收录 **18** 张表定义，来自 `diif_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category diif
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_diif_idsresult` | 智能销售预测结果-主表 | 4 | [diif_idsresult.md](./diif_idsresult.md) |
| 2 | `t_diif_idsresultentry` | 单据体-子表 | 14 | [diif_idsresult.md](./diif_idsresult.md) |
| 3 | `t_diif_protocolentity` | 协议信息实体-主表 | 6 | [diif_protocolentity.md](./diif_protocolentity.md) |
| 4 | `t_diif_salforecast` | 销售预测单-主表 | 34 | [diif_salforecast.md](./diif_salforecast.md) |
| 5 | `t_diif_salforecast_l` | 销售预测单-多语言表 | 4 | [diif_salforecast.md](./diif_salforecast.md) |
| 6 | `t_diif_salforecastentry` | 明细信息-子表 | 9 | [diif_salforecast.md](./diif_salforecast.md) |
| 7 | `t_diif_salforecastentry_f` | 明细信息-分表 | 32 | [diif_salforecast.md](./diif_salforecast.md) |
| 8 | `t_diif_salforecastentry_h` | 明细信息-分表 | 32 | [diif_salforecast.md](./diif_salforecast.md) |
| 9 | `t_diif_salforecastentry_r` | 明细信息-分表 | 32 | [diif_salforecast.md](./diif_salforecast.md) |
| 10 | `t_diif_scheme` | 预测方案-主表 | 44 | [diif_scheme.md](./diif_scheme.md) |
| 11 | `t_diif_scheme` | 预测方案F7-主表 | 44 | [diif_scheme_f7.md](./diif_scheme_f7.md) |
| 12 | `t_diif_scheme_l` | 预测方案-多语言表 | 4 | [diif_scheme.md](./diif_scheme.md) |
| 13 | `t_diif_scheme_l` | 预测方案F7-多语言表 | 4 | [diif_scheme_f7.md](./diif_scheme_f7.md) |
| 14 | `t_diif_schemematerial` | 子单据体-子表 | 6 | [diif_scheme.md](./diif_scheme.md) |
| 15 | `t_diif_schemeresponsible` | 预测范围明细-子表 | 11 | [diif_scheme.md](./diif_scheme.md) |
| 16 | `t_diif_source` | 预测数据源-主表 | 23 | [diif_source.md](./diif_source.md) |
| 17 | `t_diif_source_l` | 预测数据源-多语言表 | 4 | [diif_source.md](./diif_source.md) |
| 18 | `t_diif_sourceresult` | 单据体-子表 | 5 | [diif_source.md](./diif_source.md) |
