# clmcd 模块表清单

> 本模块共收录 **34** 张表定义，来自 `clmcd_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category clmcd
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_clm_con_paymentnode` | 合同款项节点-主表 | 19 | [clm_contract_payment_node.md](./clm_contract_payment_node.md) |
| 2 | `t_clm_con_paymentnode_l` | 合同款项节点-多语言表 | 5 | [clm_contract_payment_node.md](./clm_contract_payment_node.md) |
| 3 | `t_clm_con_paymentplan` | 合同款项方案-主表 | 22 | [clm_contract_payment_plan.md](./clm_contract_payment_plan.md) |
| 4 | `t_clm_con_paymentplan_e` | 款项内容-子表 | 14 | [clm_contract_payment_plan.md](./clm_contract_payment_plan.md) |
| 5 | `t_clm_con_paymentplan_l` | 合同款项方案-多语言表 | 5 | [clm_contract_payment_plan.md](./clm_contract_payment_plan.md) |
| 6 | `t_clm_contract_fields_map` | 合同字段与值映射表-主表 | 11 | [clm_contract_fields_map.md](./clm_contract_fields_map.md) |
| 7 | `t_clm_contract_fields_map_l` | 合同字段与值映射表-多语言表 | 4 | [clm_contract_fields_map.md](./clm_contract_fields_map.md) |
| 8 | `t_clm_contract_review_log` | 单据体-子表 | 11 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 9 | `t_clm_contract_review_m` | 评审留言单据体-子表 | 10 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 10 | `t_clm_contract_review_re` | 评审说明单据体（隐藏）-子表 | 7 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 11 | `t_clm_contract_review_ro` | 轮次评审人-子表 | 11 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 12 | `t_clm_contract_template` | 合同模板-主表 | 25 | [clm_contract_template.md](./clm_contract_template.md) |
| 13 | `t_clm_contract_template_l` | 合同模板-多语言表 | 5 | [clm_contract_template.md](./clm_contract_template.md) |
| 14 | `t_clm_contractdraft` | 合同起草-主表 | 69 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 15 | `t_clm_contractdraft` | 合同-主表 | 69 | [clm_related_contract.md](./clm_related_contract.md) |
| 16 | `t_clm_contractdraft_c` | 合同起草-分表 | 4 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 17 | `t_clm_contractdraft_l` | 合同起草-多语言表 | 13 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 18 | `t_clm_contractdraft_l` | 合同-多语言表 | 13 | [clm_related_contract.md](./clm_related_contract.md) |
| 19 | `t_clm_contractdraft_m` | 合同起草-分表 | 4 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 20 | `t_clm_contractdraft_money` | 合同款项单据体-子表 | 14 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 21 | `t_clm_contractdraft_obj` | 合同标的单据体-子表 | 31 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 22 | `t_clm_contractdraft_r` | 合同起草-分表 | 8 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 23 | `t_clm_contractdraft_t` | 合同起草-分表 | 4 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 24 | `t_clm_contractdraft_t` | 合同-分表 | 4 | [clm_related_contract.md](./clm_related_contract.md) |
| 25 | `t_clm_contractitem` | 合同条款-主表 | 17 | [clm_contractterms.md](./clm_contractterms.md) |
| 26 | `t_clm_contractitem_entry` | 单据体-子表 | 5 | [clm_contractterms.md](./clm_contractterms.md) |
| 27 | `t_clm_contractitem_l` | 合同条款-多语言表 | 4 | [clm_contractterms.md](./clm_contractterms.md) |
| 28 | `t_clm_contractobject` | 合同标的-主表 | 20 | [clm_contractobject.md](./clm_contractobject.md) |
| 29 | `t_clm_contractobject_l` | 合同标的-多语言表 | 5 | [clm_contractobject.md](./clm_contractobject.md) |
| 30 | `t_clm_filestore` | 文件存储-主表 | 12 | [clm_filestore.md](./clm_filestore.md) |
| 31 | `t_clm_filestore_l` | 文件存储-多语言表 | 4 | [clm_filestore.md](./clm_filestore.md) |
| 32 | `t_clm_related_contract` | 关联合同-多选基础资料表 | 3 | [clm_contractdraft_tpl.md](./clm_contractdraft_tpl.md) |
| 33 | `t_clm_related_contract` | 关联合同-多选基础资料表 | 3 | [clm_related_contract.md](./clm_related_contract.md) |
| 34 | `t_clm_terms_contype` | 适用合同类型-多选基础资料表 | 3 | [clm_contractterms.md](./clm_contractterms.md) |
