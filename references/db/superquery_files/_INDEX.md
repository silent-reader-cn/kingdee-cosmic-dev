# superquery 模块表清单

> 本模块共收录 **8** 张表定义，来自 `superquery_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category superquery
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_flydb_database` | 库-主表 | 7 | [bos_flydb_database.md](./bos_flydb_database.md) |
| 2 | `t_flydb_database_l` | 库-多语言表 | 4 | [bos_flydb_database.md](./bos_flydb_database.md) |
| 3 | `t_flydb_schema` | Schema管理-主表 | 10 | [bos_flydb_schema.md](./bos_flydb_schema.md) |
| 4 | `t_flydb_schema_l` | Schema管理-多语言表 | 4 | [bos_flydb_schema.md](./bos_flydb_schema.md) |
| 5 | `t_flydb_schema_perm` | Schema权限-主表 | 4 | [bos_flydb_schema_perm.md](./bos_flydb_schema_perm.md) |
| 6 | `t_flydb_schema_ref` | 自定义实体范围-多选基础资料表 | 3 | [bos_flydb_schema.md](./bos_flydb_schema.md) |
| 7 | `t_meta_entitydesign` | 业务对象列表_可多选-主表 | 18 | [bos_flydb_objlist.md](./bos_flydb_objlist.md) |
| 8 | `t_meta_entitydesign_l` | 业务对象列表_可多选-多语言表 | 6 | [bos_flydb_objlist.md](./bos_flydb_objlist.md) |
