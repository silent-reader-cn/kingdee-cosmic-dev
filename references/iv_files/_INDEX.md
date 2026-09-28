# iv 模块表清单

> 本模块共收录 **12** 张表定义，来自 `iv_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope iv
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_iv_purchasebill` | 采购发票单-主表 | 43 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 2 | `t_iv_purchasebill_lk` | 关联子实体-子表 | 6 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 3 | `t_iv_purchasebill_tc` | 采购发票单-关联追踪表 | 7 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 4 | `t_iv_purchasebill_wb` | 采购发票单-反写记录表 | 10 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 5 | `t_iv_purchasebillentry` | 明细-子表 | 64 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 6 | `t_iv_purchasebillentry_lk` | 关联子实体-子表 | 6 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 7 | `t_iv_salebill` | 销售发票单-主表 | 40 | [iv_salebill.md](./iv_salebill.md) |
| 8 | `t_iv_salebill_lk` | 关联子实体-子表 | 6 | [iv_salebill.md](./iv_salebill.md) |
| 9 | `t_iv_salebill_tc` | 销售发票单-关联追踪表 | 7 | [iv_salebill.md](./iv_salebill.md) |
| 10 | `t_iv_salebill_wb` | 销售发票单-反写记录表 | 10 | [iv_salebill.md](./iv_salebill.md) |
| 11 | `t_iv_salebillentry` | 明细-子表 | 62 | [iv_salebill.md](./iv_salebill.md) |
| 12 | `t_iv_salebillentry_lk` | 关联子实体-子表 | 6 | [iv_salebill.md](./iv_salebill.md) |
