# xkzlzc 模块表清单

> 本模块共收录 **23** 张表定义，来自 `xkzlzc_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category xkzlzc
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fa_discount_rate` | 折现率-主表 | 21 | [fa_discount_rate.md](./fa_discount_rate.md) |
| 2 | `t_fa_discount_rate_entry` | 单据体-子表 | 6 | [fa_discount_rate.md](./fa_discount_rate.md) |
| 3 | `t_fa_discount_rate_l` | 折现率-多语言表 | 4 | [fa_discount_rate.md](./fa_discount_rate.md) |
| 4 | `t_fa_discount_rate_m` | 折现率-使用范围位图表 | 2 | [fa_discount_rate.md](./fa_discount_rate.md) |
| 5 | `t_fa_discount_rate_u` | 折现率-使用范围表 | 3 | [fa_discount_rate.md](./fa_discount_rate.md) |
| 6 | `t_fa_interest_detail` | 计息明细表-主表 | 13 | [fa_interest_detail.md](./fa_interest_detail.md) |
| 7 | `t_fa_interest_detail_e` | 计息明细分录-子表 | 10 | [fa_interest_detail.md](./fa_interest_detail.md) |
| 8 | `t_fa_lease_change_bill` | 租赁变更单-主表 | 17 | [fa_lease_change_bill.md](./fa_lease_change_bill.md) |
| 9 | `t_fa_lease_chg_items` | 变更项目-多选基础资料表 | 3 | [fa_lease_change_bill.md](./fa_lease_change_bill.md) |
| 10 | `t_fa_lease_contract_new` | 租赁合同-主表 | 61 | [fa_lease_contract.md](./fa_lease_contract.md) |
| 11 | `t_fa_lease_contract_new` | 租赁合同初始化-主表 | 61 | [fa_lease_contract_init.md](./fa_lease_contract_init.md) |
| 12 | `t_fa_lease_contract_new_l` | 租赁合同-多语言表 | 5 | [fa_lease_contract.md](./fa_lease_contract.md) |
| 13 | `t_fa_lease_contract_new_l` | 租赁合同初始化-多语言表 | 5 | [fa_lease_contract_init.md](./fa_lease_contract_init.md) |
| 14 | `t_fa_lease_contract_new_lk` | 关联子实体-子表 | 6 | [fa_lease_contract.md](./fa_lease_contract.md) |
| 15 | `t_fa_lease_contract_new_lk` | 关联子实体-子表 | 6 | [fa_lease_contract_init.md](./fa_lease_contract_init.md) |
| 16 | `t_fa_lease_pay_plan` | 付款计划-子表 | 30 | [fa_lease_contract.md](./fa_lease_contract.md) |
| 17 | `t_fa_lease_pay_plan` | 付款计划-子表 | 30 | [fa_lease_contract_init.md](./fa_lease_contract_init.md) |
| 18 | `t_fa_lease_pay_plan` | 付款计划-主表 | 30 | [fa_lease_pay_plan.md](./fa_lease_pay_plan.md) |
| 19 | `t_fa_lease_pay_rule` | 付款规则-子表 | 15 | [fa_lease_contract.md](./fa_lease_contract.md) |
| 20 | `t_fa_lease_pay_rule` | 付款规则-子表 | 15 | [fa_lease_contract_init.md](./fa_lease_contract_init.md) |
| 21 | `t_fa_lease_rent_settle` | 摊销与计息-主表 | 24 | [fa_lease_rent_settle.md](./fa_lease_rent_settle.md) |
| 22 | `t_fa_payment_item` | 付款项目-主表 | 13 | [fa_payment_item.md](./fa_payment_item.md) |
| 23 | `t_fa_payment_item_l` | 付款项目-多语言表 | 4 | [fa_payment_item.md](./fa_payment_item.md) |
