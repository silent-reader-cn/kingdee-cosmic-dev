# ict 模块表清单

> 本模块共收录 **20** 张表定义，来自 `ict_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ict
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ict_cf_cross_entry` | 单据体-子表 | 18 | [ict_check_cash_record.md](./ict_check_cash_record.md) |
| 2 | `t_ict_cf_cross_record` | 现金流量记录-主表 | 10 | [ict_check_cash_record.md](./ict_check_cash_record.md) |
| 3 | `t_ict_commonassgrp` | 共同核算维度-多选基础资料表 | 3 | [ict_verifyscheme.md](./ict_verifyscheme.md) |
| 4 | `t_ict_cross_entry` | 单据体-子表 | 22 | [ict_check_record.md](./ict_check_record.md) |
| 5 | `t_ict_cross_record` | 科目记录-主表 | 10 | [ict_check_record.md](./ict_check_record.md) |
| 6 | `t_ict_mulaccount` | 科目-多选基础资料表 | 3 | [ict_recontolerance.md](./ict_recontolerance.md) |
| 7 | `t_ict_pullacctdetaillog` | 科目日志-主表 | 8 | [ict_pullacctdetaillog.md](./ict_pullacctdetaillog.md) |
| 8 | `t_ict_pullcfdetaillog` | 现金流量日志-主表 | 8 | [ict_pullcfdetaillog.md](./ict_pullcfdetaillog.md) |
| 9 | `t_ict_pulldatalog` | 数据抽取日志-主表 | 16 | [ict_pulldatalog.md](./ict_pulldatalog.md) |
| 10 | `t_ict_recontolerance` | 对账容差-主表 | 23 | [ict_recontolerance.md](./ict_recontolerance.md) |
| 11 | `t_ict_recontolerance_l` | 对账容差-多语言表 | 4 | [ict_recontolerance.md](./ict_recontolerance.md) |
| 12 | `t_ict_recontolerance_m` | 对账容差-使用范围位图表 | 2 | [ict_recontolerance.md](./ict_recontolerance.md) |
| 13 | `t_ict_recontolerance_u` | 对账容差-使用范围表 | 3 | [ict_recontolerance.md](./ict_recontolerance.md) |
| 14 | `t_ict_relacctrecord` | 科目数据-主表 | 38 | [ict_relacctrecord.md](./ict_relacctrecord.md) |
| 15 | `t_ict_relcfrecord` | 现金流量数据-主表 | 34 | [ict_relcfrecord.md](./ict_relcfrecord.md) |
| 16 | `t_ict_verifydimentry` | 对账维度单据体-子表 | 6 | [ict_verifyscheme.md](./ict_verifyscheme.md) |
| 17 | `t_ict_verifyscheme` | 内部交易对账方案-主表 | 22 | [ict_verifyscheme.md](./ict_verifyscheme.md) |
| 18 | `t_ict_verifyscheme_l` | 内部交易对账方案-多语言表 | 4 | [ict_verifyscheme.md](./ict_verifyscheme.md) |
| 19 | `t_ict_verifyscheme_m` | 内部交易对账方案-使用范围位图表 | 2 | [ict_verifyscheme.md](./ict_verifyscheme.md) |
| 20 | `t_ict_verifyscheme_u` | 内部交易对账方案-使用范围表 | 3 | [ict_verifyscheme.md](./ict_verifyscheme.md) |
