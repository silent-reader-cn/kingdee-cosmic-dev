# xkfsa 模块表清单

> 本模块共收录 **6** 张表定义，来自 `xkfsa_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope xkfsa
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_xkfsa_industrydata` | 行业数据-主表 | 18 | [xkfsa_industrydata.md](./xkfsa_industrydata.md) |
| 2 | `t_xkfsa_industrydata_l` | 行业数据-多语言表 | 3 | [xkfsa_industrydata.md](./xkfsa_industrydata.md) |
| 3 | `t_xkfsa_rptwarningagent` | 报表项目预警动因-主表 | 24 | [xkfsa_rptitemwarningagent.md](./xkfsa_rptitemwarningagent.md) |
| 4 | `t_xkfsa_rptwarningagent_l` | 报表项目预警动因-多语言表 | 4 | [xkfsa_rptitemwarningagent.md](./xkfsa_rptitemwarningagent.md) |
| 5 | `t_xkfsa_warningagententry` | 单据体-子表 | 4 | [xkfsa_rptitemwarningagent.md](./xkfsa_rptitemwarningagent.md) |
| 6 | `t_xkfsa_warningagententry_l` | 单据体-多语言表 | 4 | [xkfsa_rptitemwarningagent.md](./xkfsa_rptitemwarningagent.md) |
