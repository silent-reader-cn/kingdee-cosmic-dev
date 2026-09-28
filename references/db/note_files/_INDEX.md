# note 模块表清单

> 本模块共收录 **4** 张表定义，来自 `note_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category note
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_note_payable` | 应付票据-主表 | 110 | [note_payable.md](./note_payable.md) |
| 2 | `t_note_payable_l` | 应付票据-多语言表 | 4 | [note_payable.md](./note_payable.md) |
| 3 | `t_note_receivable` | 应收票据-主表 | 123 | [note_receivable.md](./note_receivable.md) |
| 4 | `t_note_receivable_l` | 应收票据-多语言表 | 4 | [note_receivable.md](./note_receivable.md) |
