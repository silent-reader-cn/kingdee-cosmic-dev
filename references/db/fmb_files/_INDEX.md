# fmb 模块表清单

> 本模块共收录 **5** 张表定义，来自 `fmb_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category fmb
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_gl_bookscheme` | 账簿合并方案-主表 | 12 | [gl_bookscheme.md](./gl_bookscheme.md) |
| 2 | `t_gl_bookscheme_l` | 账簿合并方案-多语言表 | 4 | [gl_bookscheme.md](./gl_bookscheme.md) |
| 3 | `t_gl_bookschemeentry` | 单据体-子表 | 7 | [gl_bookscheme.md](./gl_bookscheme.md) |
| 4 | `t_gl_virualacctbook` | 合并方案虚拟账簿-主表 | 10 | [gl_virualacctbook.md](./gl_virualacctbook.md) |
| 5 | `t_gl_virualacctbook_l` | 合并方案虚拟账簿-多语言表 | 4 | [gl_virualacctbook.md](./gl_virualacctbook.md) |
