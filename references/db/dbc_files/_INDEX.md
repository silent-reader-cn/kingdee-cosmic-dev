# dbc 模块表清单

> 本模块共收录 **13** 张表定义，来自 `dbc_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category dbc
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_dbc_database_comp` | 数据库比较-主表 | 24 | [dbc_database_comp.md](./dbc_database_comp.md) |
| 2 | `t_dbc_database_comp_items` | 数据表明细-子表 | 13 | [dbc_database_comp.md](./dbc_database_comp.md) |
| 3 | `t_dbc_database_copy` | 数据库复制-主表 | 24 | [dbc_database_copy.md](./dbc_database_copy.md) |
| 4 | `t_dbc_database_copy_items` | 数据表明细-子表 | 13 | [dbc_database_copy.md](./dbc_database_copy.md) |
| 5 | `t_dbc_table_copy` | 数据表复制-主表 | 24 | [dbc_table_copy.md](./dbc_table_copy.md) |
| 6 | `t_dbc_table_copy_items` | 过滤条件-子表 | 7 | [dbc_table_copy.md](./dbc_table_copy.md) |
| 7 | `t_dbc_table_copy_l` | 数据表复制-多语言表 | 4 | [dbc_table_copy.md](./dbc_table_copy.md) |
| 8 | `t_dbc_table_copy_log` | 数据表复制日志-主表 | 26 | [dbc_table_copy_log.md](./dbc_table_copy_log.md) |
| 9 | `t_dbc_tc_log_items` | 单据体-子表 | 17 | [dbc_table_copy_log.md](./dbc_table_copy_log.md) |
| 10 | `t_isc_database_link` | 数据库连接-主表 | 56 | [dbc_database_link.md](./dbc_database_link.md) |
| 11 | `t_isc_database_link_l` | 数据库连接-多语言表 | 4 | [dbc_database_link.md](./dbc_database_link.md) |
| 12 | `t_isc_datasource` | 数据库-主表 | 18 | [dbc_database.md](./dbc_database.md) |
| 13 | `t_isc_datasource_l` | 数据库-多语言表 | 4 | [dbc_database.md](./dbc_database.md) |
