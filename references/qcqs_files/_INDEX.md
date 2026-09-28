# qcqs 模块表清单

> 本模块共收录 **18** 张表定义，来自 `qcqs_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope qcqs
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_qcbd_chartset` | 图表设置(废弃)-主表 | 17 | [qcqs_chartsettings.md](./qcqs_chartsettings.md) |
| 2 | `t_qcbd_chartset_l` | 图表设置(废弃)-多语言表 | 5 | [qcqs_chartsettings.md](./qcqs_chartsettings.md) |
| 3 | `t_qcqs_analyrptkey` | 统计分析报表关键字-主表 | 11 | [qcqs_analyrptkey.md](./qcqs_analyrptkey.md) |
| 4 | `t_qcqs_analyrptkey_l` | 统计分析报表关键字-多语言表 | 4 | [qcqs_analyrptkey.md](./qcqs_analyrptkey.md) |
| 5 | `t_qcqs_biztype` | 业务类型-多选基础资料表 | 3 | [qcqs_charsettingschem.md](./qcqs_charsettingschem.md) |
| 6 | `t_qcqs_chartentry` | 单据体-子表 | 10 | [qcqs_charsettingschem.md](./qcqs_charsettingschem.md) |
| 7 | `t_qcqs_chartschem` | 图表设置方案-主表 | 27 | [qcqs_charsettingschem.md](./qcqs_charsettingschem.md) |
| 8 | `t_qcqs_chartschem_l` | 图表设置方案-多语言表 | 4 | [qcqs_charsettingschem.md](./qcqs_charsettingschem.md) |
| 9 | `t_qcqs_chartschem_m` | 图表设置方案-使用范围位图表 | 2 | [qcqs_charsettingschem.md](./qcqs_charsettingschem.md) |
| 10 | `t_qcqs_chartschem_u` | 图表设置方案-使用范围表 | 3 | [qcqs_charsettingschem.md](./qcqs_charsettingschem.md) |
| 11 | `t_qcqs_entryentity` | 单据体-子表 | 6 | [qcqs_evaluationscheme.md](./qcqs_evaluationscheme.md) |
| 12 | `t_qcqs_evgrade` | 过程能力评价等级-主表 | 19 | [qcqs_evaluategrade.md](./qcqs_evaluategrade.md) |
| 13 | `t_qcqs_evgrade_l` | 过程能力评价等级-多语言表 | 4 | [qcqs_evaluategrade.md](./qcqs_evaluategrade.md) |
| 14 | `t_qcqs_evgrade_u` | 过程能力评价等级-使用范围表 | 3 | [qcqs_evaluategrade.md](./qcqs_evaluategrade.md) |
| 15 | `t_qcqs_evscheme` | 过程能力评价方案-主表 | 21 | [qcqs_evaluationscheme.md](./qcqs_evaluationscheme.md) |
| 16 | `t_qcqs_evscheme_l` | 过程能力评价方案-多语言表 | 4 | [qcqs_evaluationscheme.md](./qcqs_evaluationscheme.md) |
| 17 | `t_qcqs_evscheme_u` | 过程能力评价方案-使用范围表 | 3 | [qcqs_evaluationscheme.md](./qcqs_evaluationscheme.md) |
| 18 | `t_qcqs_rptkeyentry` | 单据体-子表 | 4 | [qcqs_analyrptkey.md](./qcqs_analyrptkey.md) |
