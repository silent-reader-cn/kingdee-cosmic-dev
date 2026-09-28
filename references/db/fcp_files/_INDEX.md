# fcp 模块表清单

> 本模块共收录 **11** 张表定义，来自 `fcp_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category fcp
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_gl_ac_reportdetail` | 执行详情-子表 | 11 | [gl_autoclose_report.md](./gl_autoclose_report.md) |
| 2 | `t_gl_ac_reportmsg` | X-执行失败信息-子表 | 6 | [gl_autoclose_report.md](./gl_autoclose_report.md) |
| 3 | `t_gl_autoclose_opdetail` | 执行操作详情-子表 | 7 | [gl_autoclose_scheme.md](./gl_autoclose_scheme.md) |
| 4 | `t_gl_autoclose_ref_book` | 账簿-多选基础资料表 | 3 | [gl_autoclose_scheme.md](./gl_autoclose_scheme.md) |
| 5 | `t_gl_autoclose_report` | 自动结账报告-主表 | 14 | [gl_autoclose_report.md](./gl_autoclose_report.md) |
| 6 | `t_gl_autoclose_rule` | 执行规则-子表 | 6 | [gl_autoclose_scheme.md](./gl_autoclose_scheme.md) |
| 7 | `t_gl_autoclose_scheme` | 自动结账方案-主表 | 10 | [gl_autoclose_scheme.md](./gl_autoclose_scheme.md) |
| 8 | `t_gl_autoclose_scheme_l` | 自动结账方案-多语言表 | 5 | [gl_autoclose_scheme.md](./gl_autoclose_scheme.md) |
| 9 | `t_gl_closeplan` | 结账计划-主表 | 10 | [gl_closeplan.md](./gl_closeplan.md) |
| 10 | `t_gl_closeschemerecord` | 期末方案执行记录-主表 | 10 | [gl_closeschemerecord.md](./gl_closeschemerecord.md) |
| 11 | `t_gl_schemevchlog` | 期末方案生成凭证记录-主表 | 5 | [gl_schemevchlog.md](./gl_schemevchlog.md) |
