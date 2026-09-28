# iv 模块表清单

> 本模块共收录 **20** 张表定义，来自 `iv_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category iv
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_iv_purchasebill` | 采购发票单-主表 | 58 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 2 | `t_iv_purchasebill_e` | 采购发票单-分表 | 17 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 3 | `t_iv_purchasebill_l` | 采购发票单-多语言表 | 5 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 4 | `t_iv_purchasebill_lk` | 关联子实体-子表 | 6 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 5 | `t_iv_purchasebill_tc` | 采购发票单-关联追踪表 | 7 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 6 | `t_iv_purchasebill_wb` | 采购发票单-反写记录表 | 10 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 7 | `t_iv_purchasebillentry` | 明细-子表 | 68 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 8 | `t_iv_purchasebillentry_e` | 明细-分表 | 24 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 9 | `t_iv_purchasebillentry_lk` | 关联子实体-子表 | 14 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 10 | `t_iv_purchaseinvoicedinfo` | 已开票信息-子表 | 20 | [iv_purchasebill.md](./iv_purchasebill.md) |
| 11 | `t_iv_salebill` | 销售发票单-主表 | 57 | [iv_salebill.md](./iv_salebill.md) |
| 12 | `t_iv_salebill_e` | 销售发票单-分表 | 17 | [iv_salebill.md](./iv_salebill.md) |
| 13 | `t_iv_salebill_l` | 销售发票单-多语言表 | 5 | [iv_salebill.md](./iv_salebill.md) |
| 14 | `t_iv_salebill_lk` | 关联子实体-子表 | 6 | [iv_salebill.md](./iv_salebill.md) |
| 15 | `t_iv_salebill_tc` | 销售发票单-关联追踪表 | 7 | [iv_salebill.md](./iv_salebill.md) |
| 16 | `t_iv_salebill_wb` | 销售发票单-反写记录表 | 10 | [iv_salebill.md](./iv_salebill.md) |
| 17 | `t_iv_salebillentry` | 明细-子表 | 67 | [iv_salebill.md](./iv_salebill.md) |
| 18 | `t_iv_salebillentry_e` | 明细-分表 | 9 | [iv_salebill.md](./iv_salebill.md) |
| 19 | `t_iv_salebillentry_lk` | 关联子实体-子表 | 14 | [iv_salebill.md](./iv_salebill.md) |
| 20 | `t_iv_saleinvoicedinfo` | 已开票信息-子表 | 20 | [iv_salebill.md](./iv_salebill.md) |
