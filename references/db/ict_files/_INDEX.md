# ict 模块表清单

> 本模块共收录 **28** 张表定义，来自 `ict_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ict
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ict_acctpuchamt` | 科目对账表-主表 | 44 | [ict_acctpuchamt.md](./ict_acctpuchamt.md) |
| 2 | `t_ict_acctpuchamt_log` | 科目对账日志表-主表 | 20 | [ict_acctpuchamt_log.md](./ict_acctpuchamt_log.md) |
| 3 | `t_ict_cashflowtolerance` | 现金流量容差-主表 | 22 | [ict_cashflowtolerance.md](./ict_cashflowtolerance.md) |
| 4 | `t_ict_cashflowtolerance_l` | 现金流量容差-多语言表 | 4 | [ict_cashflowtolerance.md](./ict_cashflowtolerance.md) |
| 5 | `t_ict_cashflowtolerance_u` | 现金流量容差-使用范围表 | 3 | [ict_cashflowtolerance.md](./ict_cashflowtolerance.md) |
| 6 | `t_ict_cf_cross_entry` | 单据体-子表 | 24 | [ict_check_cash_record.md](./ict_check_cash_record.md) |
| 7 | `t_ict_cf_cross_record` | 现金流量记录-主表 | 12 | [ict_check_cash_record.md](./ict_check_cash_record.md) |
| 8 | `t_ict_cfpuchamt` | 现金流量对账表-主表 | 18 | [ict_cfpuchamt.md](./ict_cfpuchamt.md) |
| 9 | `t_ict_cfpuchamt_log` | 现金流量对账日志-主表 | 16 | [ict_cfpuchamt_log.md](./ict_cfpuchamt_log.md) |
| 10 | `t_ict_commonassgrp` | 共同核算维度-多选基础资料表 | 3 | [ict_verifyscheme.md](./ict_verifyscheme.md) |
| 11 | `t_ict_cross_entry` | 单据体-子表 | 24 | [ict_check_record.md](./ict_check_record.md) |
| 12 | `t_ict_cross_record` | 科目记录-主表 | 12 | [ict_check_record.md](./ict_check_record.md) |
| 13 | `t_ict_mulaccount` | 科目-多选基础资料表 | 3 | [ict_recontolerance.md](./ict_recontolerance.md) |
| 14 | `t_ict_mulcashflowitem` | 现金流量项目-多选基础资料表 | 3 | [ict_cashflowtolerance.md](./ict_cashflowtolerance.md) |
| 15 | `t_ict_pullacctdetaillog` | 科目日志-主表 | 9 | [ict_pullacctdetaillog.md](./ict_pullacctdetaillog.md) |
| 16 | `t_ict_pullcfdetaillog` | 现金流量日志-主表 | 9 | [ict_pullcfdetaillog.md](./ict_pullcfdetaillog.md) |
| 17 | `t_ict_pulldatalog` | 数据抽取日志-主表 | 16 | [ict_pulldatalog.md](./ict_pulldatalog.md) |
| 18 | `t_ict_recontolerance` | 科目容差-主表 | 23 | [ict_recontolerance.md](./ict_recontolerance.md) |
| 19 | `t_ict_recontolerance_l` | 科目容差-多语言表 | 4 | [ict_recontolerance.md](./ict_recontolerance.md) |
| 20 | `t_ict_recontolerance_m` | 科目容差-使用范围位图表 | 2 | [ict_recontolerance.md](./ict_recontolerance.md) |
| 21 | `t_ict_recontolerance_u` | 科目容差-使用范围表 | 3 | [ict_recontolerance.md](./ict_recontolerance.md) |
| 22 | `t_ict_relacctrecord` | 科目数据-主表 | 39 | [ict_relacctrecord.md](./ict_relacctrecord.md) |
| 23 | `t_ict_relcfrecord` | 现金流量数据-主表 | 39 | [ict_relcfrecord.md](./ict_relcfrecord.md) |
| 24 | `t_ict_verifydimentry` | 对账维度单据体-子表 | 8 | [ict_verifyscheme.md](./ict_verifyscheme.md) |
| 25 | `t_ict_verifyscheme` | 内部交易对账方案-主表 | 22 | [ict_verifyscheme.md](./ict_verifyscheme.md) |
| 26 | `t_ict_verifyscheme_l` | 内部交易对账方案-多语言表 | 4 | [ict_verifyscheme.md](./ict_verifyscheme.md) |
| 27 | `t_ict_verifyscheme_m` | 内部交易对账方案-使用范围位图表 | 2 | [ict_verifyscheme.md](./ict_verifyscheme.md) |
| 28 | `t_ict_verifyscheme_u` | 内部交易对账方案-使用范围表 | 3 | [ict_verifyscheme.md](./ict_verifyscheme.md) |
