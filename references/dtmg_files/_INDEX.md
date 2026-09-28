# dtmg 模块表清单

> 本模块共收录 **5** 张表定义，来自 `dtmg_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope dtmg
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_dtmg_initimport` | 快速初始化数据迁移-主表 | 14 | [dtmg_initdata_import.md](./dtmg_initdata_import.md) |
| 2 | `t_dtmg_initimport_l` | 快速初始化数据迁移-多语言表 | 4 | [dtmg_initdata_import.md](./dtmg_initdata_import.md) |
| 3 | `t_dtmg_initimportentry` | 初始化引入分录-子表 | 34 | [dtmg_initdata_import.md](./dtmg_initdata_import.md) |
| 4 | `t_dtmg_initimportentry_ot` | 重传附件-附件表 | 3 | [dtmg_initdata_import.md](./dtmg_initdata_import.md) |
| 5 | `t_dtmg_wisecustmdata` | 数据迁移WISE自定义数据-主表 | 9 | [dtmg_wisecustmdata.md](./dtmg_wisecustmdata.md) |
