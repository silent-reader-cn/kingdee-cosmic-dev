# aifs 模块表清单

> 本模块共收录 **6** 张表定义，来自 `aifs_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope aifs
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_aifs_asstacttype` | 核算维度-多选基础资料表 | 3 | [aifs_targetset.md](./aifs_targetset.md) |
| 2 | `t_aifs_queryrecord` | 指标查询记录-主表 | 11 | [aifs_queryrecord.md](./aifs_queryrecord.md) |
| 3 | `t_aifs_queryrecord_l` | 指标查询记录-多语言表 | 4 | [aifs_queryrecord.md](./aifs_queryrecord.md) |
| 4 | `t_aifs_targetset` | 指标-主表 | 36 | [aifs_targetset.md](./aifs_targetset.md) |
| 5 | `t_aifs_targetset_l` | 指标-多语言表 | 4 | [aifs_targetset.md](./aifs_targetset.md) |
| 6 | `t_aifs_visitrecord` | 组织访问记录-主表 | 0 | [aifs_visitrecord.md](./aifs_visitrecord.md) |
