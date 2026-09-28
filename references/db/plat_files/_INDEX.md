# plat 模块表清单

> 本模块共收录 **38** 张表定义，来自 `plat_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category plat
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_plat_priceadjustlog` | 批量调整日志-主表 | 12 | [plat_priceadjustlog.md](./plat_priceadjustlog.md) |
| 2 | `t_plat_quoteconentry` | 前置条件-子表 | 7 | [plat_quotestrategy.md](./plat_quotestrategy.md) |
| 3 | `t_plat_quotefactor` | 自动取价因素-主表 | 17 | [plat_quotefactor.md](./plat_quotefactor.md) |
| 4 | `t_plat_quotefactor_l` | 自动取价因素-多语言表 | 5 | [plat_quotefactor.md](./plat_quotefactor.md) |
| 5 | `t_plat_quotefactorentry` | 字段明细-子表 | 6 | [plat_quotefactor.md](./plat_quotefactor.md) |
| 6 | `t_plat_quotelog` | 取价日志-主表 | 17 | [plat_quotelog.md](./plat_quotelog.md) |
| 7 | `t_plat_quotelog_tmp` | 取价日志临时表-主表 | 18 | [plat_quotelogtmp.md](./plat_quotelogtmp.md) |
| 8 | `t_plat_quotescheme` | 取价方案-主表 | 26 | [plat_quotescheme.md](./plat_quotescheme.md) |
| 9 | `t_plat_quotescheme_l` | 取价方案-多语言表 | 5 | [plat_quotescheme.md](./plat_quotescheme.md) |
| 10 | `t_plat_quoteschemeentry` | 字段映射单据体-子表 | 11 | [plat_quotescheme.md](./plat_quotescheme.md) |
| 11 | `t_plat_quotesortentry` | 价格排序-子表 | 6 | [plat_quotescheme.md](./plat_quotescheme.md) |
| 12 | `t_plat_quotestentry` | 方案排序单据体-子表 | 11 | [plat_quotestrategy.md](./plat_quotestrategy.md) |
| 13 | `t_plat_quotestrategy` | 取价策略-主表 | 25 | [plat_quotestrategy.md](./plat_quotestrategy.md) |
| 14 | `t_plat_quotestrategy_l` | 取价策略-多语言表 | 5 | [plat_quotestrategy.md](./plat_quotestrategy.md) |
| 15 | `t_plat_quotestrategy_m` | 取价策略-使用范围位图表 | 2 | [plat_quotestrategy.md](./plat_quotestrategy.md) |
| 16 | `t_plat_quotestrategy_u` | 取价策略-使用范围表 | 3 | [plat_quotestrategy.md](./plat_quotestrategy.md) |
| 17 | `t_plat_taxamountformula` | 计税金额公式配置-主表 | 15 | [plat_taxamountformula.md](./plat_taxamountformula.md) |
| 18 | `t_plat_taxamountformula_l` | 计税金额公式配置-多语言表 | 5 | [plat_taxamountformula.md](./plat_taxamountformula.md) |
| 19 | `t_plat_taxamtformulaorg` | 适用组织-子表 | 4 | [plat_taxamountformula.md](./plat_taxamountformula.md) |
| 20 | `t_plat_taxationentry` | 税额明细-子表 | 24 | [plat_taxexpense.md](./plat_taxexpense.md) |
| 21 | `t_plat_taxcatexpense` | 费用项目-子表 | 4 | [plat_taxcatexpenseset.md](./plat_taxcatexpenseset.md) |
| 22 | `t_plat_taxcatexpenseorg` | 适用组织-子表 | 4 | [plat_taxcatexpenseset.md](./plat_taxcatexpenseset.md) |
| 23 | `t_plat_taxcatexpenseset` | 税种涉及费用配置-主表 | 18 | [plat_taxcatexpenseset.md](./plat_taxcatexpenseset.md) |
| 24 | `t_plat_taxcatexpenseset_l` | 税种涉及费用配置-多语言表 | 5 | [plat_taxcatexpenseset.md](./plat_taxcatexpenseset.md) |
| 25 | `t_plat_taxcatformula` | 公式配置-子表 | 8 | [plat_taxamountformula.md](./plat_taxamountformula.md) |
| 26 | `t_plat_taxcatformula_l` | 公式配置-多语言表 | 4 | [plat_taxamountformula.md](./plat_taxamountformula.md) |
| 27 | `t_plat_taxexpense` | 供应链费用单-主表 | 32 | [plat_taxexpense.md](./plat_taxexpense.md) |
| 28 | `t_plat_taxexpense_l` | 供应链费用单-多语言表 | 4 | [plat_taxexpense.md](./plat_taxexpense.md) |
| 29 | `t_plat_taxexpense_lk` | 关联子实体-子表 | 6 | [plat_taxexpense.md](./plat_taxexpense.md) |
| 30 | `t_plat_taxexpense_tc` | 供应链费用单-关联追踪表 | 7 | [plat_taxexpense.md](./plat_taxexpense.md) |
| 31 | `t_plat_taxexpense_wb` | 供应链费用单-反写记录表 | 10 | [plat_taxexpense.md](./plat_taxexpense.md) |
| 32 | `t_plat_taxexpenseentry` | 物料明细-子表 | 30 | [plat_taxexpense.md](./plat_taxexpense.md) |
| 33 | `t_plat_taxexpenseentry_lk` | 关联子实体-子表 | 6 | [plat_taxexpense.md](./plat_taxexpense.md) |
| 34 | `t_plat_taxexpenseitem` | 费用明细-子表 | 39 | [plat_taxexpense.md](./plat_taxexpense.md) |
| 35 | `t_plat_taxexpenseitem_lk` | 关联子实体-子表 | 6 | [plat_taxexpense.md](./plat_taxexpense.md) |
| 36 | `t_plat_taxexpenseset` | 供应链费用单配置-主表 | 16 | [plat_taxexpenseset.md](./plat_taxexpenseset.md) |
| 37 | `t_plat_taxexpenseset_l` | 供应链费用单配置-多语言表 | 4 | [plat_taxexpenseset.md](./plat_taxexpenseset.md) |
| 38 | `t_scmc_report_params` | 供应链报表参数-主表 | 4 | [scmc_report_params.md](./scmc_report_params.md) |
