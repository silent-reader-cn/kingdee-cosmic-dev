# plat 模块表清单

> 本模块共收录 **15** 张表定义，来自 `plat_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category plat
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_plat_priceadjustlog` | 批量调整日志-主表 | 10 | [plat_priceadjustlog.md](./plat_priceadjustlog.md) |
| 2 | `t_plat_quoteconentry` | 前置条件-子表 | 7 | [plat_quotestrategy.md](./plat_quotestrategy.md) |
| 3 | `t_plat_quotefactor` | 自动取价因素-主表 | 17 | [plat_quotefactor.md](./plat_quotefactor.md) |
| 4 | `t_plat_quotefactor_l` | 自动取价因素-多语言表 | 5 | [plat_quotefactor.md](./plat_quotefactor.md) |
| 5 | `t_plat_quotefactorentry` | 字段明细-子表 | 6 | [plat_quotefactor.md](./plat_quotefactor.md) |
| 6 | `t_plat_quotelog` | 取价日志-主表 | 17 | [plat_quotelog.md](./plat_quotelog.md) |
| 7 | `t_plat_quotescheme` | 取价方案-主表 | 26 | [plat_quotescheme.md](./plat_quotescheme.md) |
| 8 | `t_plat_quotescheme_l` | 取价方案-多语言表 | 5 | [plat_quotescheme.md](./plat_quotescheme.md) |
| 9 | `t_plat_quoteschemeentry` | 字段映射单据体-子表 | 11 | [plat_quotescheme.md](./plat_quotescheme.md) |
| 10 | `t_plat_quotesortentry` | 价格排序-子表 | 6 | [plat_quotescheme.md](./plat_quotescheme.md) |
| 11 | `t_plat_quotestentry` | 方案排序单据体-子表 | 11 | [plat_quotestrategy.md](./plat_quotestrategy.md) |
| 12 | `t_plat_quotestrategy` | 取价策略-主表 | 25 | [plat_quotestrategy.md](./plat_quotestrategy.md) |
| 13 | `t_plat_quotestrategy_l` | 取价策略-多语言表 | 5 | [plat_quotestrategy.md](./plat_quotestrategy.md) |
| 14 | `t_plat_quotestrategy_m` | 取价策略-使用范围位图表 | 2 | [plat_quotestrategy.md](./plat_quotestrategy.md) |
| 15 | `t_plat_quotestrategy_u` | 取价策略-使用范围表 | 3 | [plat_quotestrategy.md](./plat_quotestrategy.md) |
