# xkpac 模块表清单

> 本模块共收录 **9** 张表定义，来自 `xkpac_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category xkpac
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_pac_prodeductbill` | 项目保证金扣款单-主表 | 24 | [pac_projectdeductbill.md](./pac_projectdeductbill.md) |
| 2 | `t_pac_prodeductbill_lk` | 关联子实体-子表 | 6 | [pac_projectdeductbill.md](./pac_projectdeductbill.md) |
| 3 | `t_pac_prodeductbill_tc` | 项目保证金扣款单-关联追踪表 | 7 | [pac_projectdeductbill.md](./pac_projectdeductbill.md) |
| 4 | `t_pac_prodeductbill_wb` | 项目保证金扣款单-反写记录表 | 10 | [pac_projectdeductbill.md](./pac_projectdeductbill.md) |
| 5 | `t_pac_prosuretybill` | 项目保证金-主表 | 26 | [pac_projectsuretybill.md](./pac_projectsuretybill.md) |
| 6 | `t_pac_prosuretybill_lk` | 关联子实体-子表 | 6 | [pac_projectsuretybill.md](./pac_projectsuretybill.md) |
| 7 | `t_pac_prosuretybill_tc` | 项目保证金-关联追踪表 | 7 | [pac_projectsuretybill.md](./pac_projectsuretybill.md) |
| 8 | `t_pac_prosuretybill_wb` | 项目保证金-反写记录表 | 10 | [pac_projectsuretybill.md](./pac_projectsuretybill.md) |
| 9 | `t_pac_suretybill_entry` | 扣款信息-子表 | 7 | [pac_projectsuretybill.md](./pac_projectsuretybill.md) |
