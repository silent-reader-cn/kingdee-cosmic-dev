# xkoaca 模块表清单

> 本模块共收录 **18** 张表定义，来自 `xkoaca_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category xkoaca
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_xkoaca_rpt` | 经营报表实体-主表 | 15 | [xkoaca_rpt.md](./xkoaca_rpt.md) |
| 2 | `t_xkoaca_rpt_l` | 经营报表实体-多语言表 | 5 | [xkoaca_rpt.md](./xkoaca_rpt.md) |
| 3 | `t_xkoaca_rptdim` | 经营报表维度-主表 | 34 | [xkoaca_reportdimension.md](./xkoaca_reportdimension.md) |
| 4 | `t_xkoaca_rptdim_acct` | 经营科目固定范围-多选基础资料表 | 3 | [xkoaca_reportdimension.md](./xkoaca_reportdimension.md) |
| 5 | `t_xkoaca_rptdim_amba` | 经营单元固定范围-多选基础资料表 | 3 | [xkoaca_reportdimension.md](./xkoaca_reportdimension.md) |
| 6 | `t_xkoaca_rptdim_l` | 经营报表维度-多语言表 | 5 | [xkoaca_reportdimension.md](./xkoaca_reportdimension.md) |
| 7 | `t_xkoaca_rptdim_opbk` | 经营账簿-多选基础资料表 | 3 | [xkoaca_reportdimension.md](./xkoaca_reportdimension.md) |
| 8 | `t_xkoaca_rptrole` | 可用角色-多选基础资料表 | 3 | [xkoaca_rpt.md](./xkoaca_rpt.md) |
| 9 | `t_xkoaca_rpttpl` | 经营报表模板-主表 | 25 | [xkoaca_rpttemplate.md](./xkoaca_rpttemplate.md) |
| 10 | `t_xkoaca_rpttpl_l` | 经营报表模板-多语言表 | 5 | [xkoaca_rpttemplate.md](./xkoaca_rpttemplate.md) |
| 11 | `t_xkoaca_rpttpl_opbk` | 经营账簿-多选基础资料表 | 3 | [xkoaca_rpttemplate.md](./xkoaca_rpttemplate.md) |
| 12 | `t_xkoaca_rpttplcolentry` | 列设置-子表 | 13 | [xkoaca_rpttemplate.md](./xkoaca_rpttemplate.md) |
| 13 | `t_xkoaca_rpttplcolentry_l` | 列设置-多语言表 | 4 | [xkoaca_rpttemplate.md](./xkoaca_rpttemplate.md) |
| 14 | `t_xkoaca_rpttplrowentry` | 行设置-子表 | 13 | [xkoaca_rpttemplate.md](./xkoaca_rpttemplate.md) |
| 15 | `t_xkoaca_rpttplrowentry_l` | 行设置-多语言表 | 4 | [xkoaca_rpttemplate.md](./xkoaca_rpttemplate.md) |
| 16 | `t_xkoaca_rptuser` | 可用人员-多选基础资料表 | 3 | [xkoaca_rpt.md](./xkoaca_rpt.md) |
| 17 | `t_xkoaca_srcdimension` | 自定义报表维度来源-主表 | 11 | [xkoaca_srcdimension.md](./xkoaca_srcdimension.md) |
| 18 | `t_xkoaca_srcdimension_l` | 自定义报表维度来源-多语言表 | 4 | [xkoaca_srcdimension.md](./xkoaca_srcdimension.md) |
