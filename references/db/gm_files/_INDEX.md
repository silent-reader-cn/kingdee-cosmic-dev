# gm 模块表清单

> 本模块共收录 **70** 张表定义，来自 `gm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category gm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_gm_beneficiary_entry` | 单据体-子表 | 6 | [gm_letterofguaapply.md](./gm_letterofguaapply.md) |
| 2 | `t_gm_beneficiary_entry` | 单据体-子表 | 6 | [gm_letterofguarantee.md](./gm_letterofguarantee.md) |
| 3 | `t_gm_beneficiary_entry` | 单据体-子表 | 6 | [gm_letterofguarantee_f7.md](./gm_letterofguarantee_f7.md) |
| 4 | `t_gm_debtregister` | 担保债务登记-主表 | 34 | [gm_debt_register.md](./gm_debt_register.md) |
| 5 | `t_gm_debtregister_l` | 担保债务登记-多语言表 | 5 | [gm_debt_register.md](./gm_debt_register.md) |
| 6 | `t_gm_guaapply_aentry` | 保证金单据体-子表 | 9 | [gm_guaranteeapply.md](./gm_guaranteeapply.md) |
| 7 | `t_gm_guaapply_ceentry` | 反担保保证单据体-子表 | 9 | [gm_guaranteeapply.md](./gm_guaranteeapply.md) |
| 8 | `t_gm_guaapply_cmentry` | 反担保抵押单据体-子表 | 6 | [gm_guaranteeapply.md](./gm_guaranteeapply.md) |
| 9 | `t_gm_guaapply_cpentry` | 反担保质押单据体-子表 | 6 | [gm_guaranteeapply.md](./gm_guaranteeapply.md) |
| 10 | `t_gm_guaapply_eentry` | 保证单据体-子表 | 9 | [gm_guaranteeapply.md](./gm_guaranteeapply.md) |
| 11 | `t_gm_guaapply_mentry` | 抵押单据体-子表 | 6 | [gm_guaranteeapply.md](./gm_guaranteeapply.md) |
| 12 | `t_gm_guaapply_pentry` | 质押单据体-子表 | 6 | [gm_guaranteeapply.md](./gm_guaranteeapply.md) |
| 13 | `t_gm_guarantee_entry` | 担保人信息分录-子表 | 9 | [gm_guaranteeapply.md](./gm_guaranteeapply.md) |
| 14 | `t_gm_guarantee_entry` | 担保人信息分录-子表 | 9 | [gm_guaranteeapply_f7.md](./gm_guaranteeapply_f7.md) |
| 15 | `t_gm_guarantee_entry` | 担保人信息分录-子表 | 9 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 16 | `t_gm_guarantee_entry` | 担保人信息分录-子表 | 9 | [gm_guaranteecontract_f7.md](./gm_guaranteecontract_f7.md) |
| 17 | `t_gm_guaranteeapply` | 担保申请-主表 | 43 | [gm_guaranteeapply.md](./gm_guaranteeapply.md) |
| 18 | `t_gm_guaranteeapply` | 担保申请-主表 | 43 | [gm_guaranteeapply_f7.md](./gm_guaranteeapply_f7.md) |
| 19 | `t_gm_guaranteecontract_lk` | 关联子实体-子表 | 6 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 20 | `t_gm_guaranteecontract_tc` | 担保合同-关联追踪表 | 7 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 21 | `t_gm_guaranteecontract_wb` | 担保合同-反写记录表 | 10 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 22 | `t_gm_guaranteed_entry` | 被担保人信息分录-子表 | 9 | [gm_guaranteeapply.md](./gm_guaranteeapply.md) |
| 23 | `t_gm_guaranteed_entry` | 被担保人信息分录-子表 | 9 | [gm_guaranteeapply_f7.md](./gm_guaranteeapply_f7.md) |
| 24 | `t_gm_guaranteed_entry` | 被担保人信息分录-子表 | 9 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 25 | `t_gm_guaranteed_entry` | 被担保人信息分录-子表 | 9 | [gm_guaranteecontract_f7.md](./gm_guaranteecontract_f7.md) |
| 26 | `t_gm_guaranteequota` | 担保额度-主表 | 29 | [gm_guaranteequota.md](./gm_guaranteequota.md) |
| 27 | `t_gm_guaranteequota_l` | 担保额度-多语言表 | 5 | [gm_guaranteequota.md](./gm_guaranteequota.md) |
| 28 | `t_gm_guaranteequotause` | 担保额度占用-主表 | 21 | [gm_guaranteequotause.md](./gm_guaranteequotause.md) |
| 29 | `t_gm_guaranteetype` | 保函类型-主表 | 16 | [gm_guaranteetype.md](./gm_guaranteetype.md) |
| 30 | `t_gm_guaranteetype_l` | 保函类型-多语言表 | 5 | [gm_guaranteetype.md](./gm_guaranteetype.md) |
| 31 | `t_gm_guaranteeuse` | 担保占用-主表 | 31 | [gm_guaranteeuse.md](./gm_guaranteeuse.md) |
| 32 | `t_gm_guaranteeuse_entry` | 释放分录-子表 | 7 | [gm_guaranteeuse.md](./gm_guaranteeuse.md) |
| 33 | `t_gm_guaranteeuse_info` | 担保信息分录-子表 | 18 | [gm_letterofguaapply.md](./gm_letterofguaapply.md) |
| 34 | `t_gm_guaranteevarieties` | 担保品种-主表 | 17 | [gm_guaranteevarieties.md](./gm_guaranteevarieties.md) |
| 35 | `t_gm_guaranteevarieties_l` | 担保品种-多语言表 | 5 | [gm_guaranteevarieties.md](./gm_guaranteevarieties.md) |
| 36 | `t_gm_guarcontract` | 担保合同-主表 | 49 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 37 | `t_gm_guarcontract` | 担保合同-主表 | 49 | [gm_guaranteecontract_f7.md](./gm_guaranteecontract_f7.md) |
| 38 | `t_gm_guarcontract_aentry` | 保证金单据体-子表 | 9 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 39 | `t_gm_guarcontract_ceentry` | 反担保保证单据体-子表 | 9 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 40 | `t_gm_guarcontract_cmentry` | 反担保抵押单据体-子表 | 6 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 41 | `t_gm_guarcontract_cpentry` | 反担保质押单据体-子表 | 6 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 42 | `t_gm_guarcontract_eentry` | 保证单据体-子表 | 9 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 43 | `t_gm_guarcontract_mentry` | 抵押单据体-子表 | 6 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 44 | `t_gm_guarcontract_pentry` | 质押单据体-子表 | 6 | [gm_guaranteecontract.md](./gm_guaranteecontract.md) |
| 45 | `t_gm_letterofguaapply` | 业务申请-主表 | 45 | [gm_letterofguaapply.md](./gm_letterofguaapply.md) |
| 46 | `t_gm_letterofguaapply_l` | 业务申请-多语言表 | 4 | [gm_letterofguaapply.md](./gm_letterofguaapply.md) |
| 47 | `t_gm_letterofguarantee` | 开函登记-主表 | 51 | [gm_letterofguarantee.md](./gm_letterofguarantee.md) |
| 48 | `t_gm_letterofguarantee` | 开函登记-主表 | 51 | [gm_letterofguarantee_f7.md](./gm_letterofguarantee_f7.md) |
| 49 | `t_gm_letterofguarantee_e` | 开函登记-分表 | 3 | [gm_letterofguarantee.md](./gm_letterofguarantee.md) |
| 50 | `t_gm_letterofguarantee_l` | 开函登记-多语言表 | 4 | [gm_letterofguarantee.md](./gm_letterofguarantee.md) |
| 51 | `t_gm_letterofguarantee_l` | 开函登记-多语言表 | 4 | [gm_letterofguarantee_f7.md](./gm_letterofguarantee_f7.md) |
| 52 | `t_gm_letterofguarantee_lk` | 关联子实体-子表 | 6 | [gm_letterofguarantee.md](./gm_letterofguarantee.md) |
| 53 | `t_gm_letterofguarantee_tc` | 开函登记-关联追踪表 | 7 | [gm_letterofguarantee.md](./gm_letterofguarantee.md) |
| 54 | `t_gm_letterofguarantee_wb` | 开函登记-反写记录表 | 10 | [gm_letterofguarantee.md](./gm_letterofguarantee.md) |
| 55 | `t_gm_pledgebill` | 抵质押物-主表 | 35 | [gm_pledgebill.md](./gm_pledgebill.md) |
| 56 | `t_gm_pledgebill` | 抵质押物f7-主表 | 35 | [gm_pledgebill_f7.md](./gm_pledgebill_f7.md) |
| 57 | `t_gm_pledgebill_lk` | 关联子实体-子表 | 6 | [gm_pledgebill.md](./gm_pledgebill.md) |
| 58 | `t_gm_pledgebill_shareorg` | 共享组织单据体-子表 | 4 | [gm_pledgebill.md](./gm_pledgebill.md) |
| 59 | `t_gm_pledgebill_shareorg` | 单据体-子表 | 4 | [gm_pledgebill_f7.md](./gm_pledgebill_f7.md) |
| 60 | `t_gm_pledgebill_tc` | 抵质押物-关联追踪表 | 7 | [gm_pledgebill.md](./gm_pledgebill.md) |
| 61 | `t_gm_pledgebill_wb` | 抵质押物-反写记录表 | 10 | [gm_pledgebill.md](./gm_pledgebill.md) |
| 62 | `t_gm_pledgetype` | 抵质押物种类-主表 | 17 | [gm_pledgetype.md](./gm_pledgetype.md) |
| 63 | `t_gm_pledgetype_ac` | 对应资产类别-多选基础资料表 | 3 | [gm_pledgetype.md](./gm_pledgetype.md) |
| 64 | `t_gm_pledgetype_l` | 抵质押物种类-多语言表 | 5 | [gm_pledgetype.md](./gm_pledgetype.md) |
| 65 | `t_gm_receiveletter` | 收函登记-主表 | 36 | [gm_receiveletter.md](./gm_receiveletter.md) |
| 66 | `t_gm_receiveletter_l` | 收函登记-多语言表 | 4 | [gm_receiveletter.md](./gm_receiveletter.md) |
| 67 | `t_gm_receiveletter_lk` | 关联子实体-子表 | 6 | [gm_receiveletter.md](./gm_receiveletter.md) |
| 68 | `t_gm_receiveletter_tc` | 收函登记-关联追踪表 | 7 | [gm_receiveletter.md](./gm_receiveletter.md) |
| 69 | `t_gm_receiveletter_wb` | 收函登记-反写记录表 | 10 | [gm_receiveletter.md](./gm_receiveletter.md) |
| 70 | `t_gm_reguaquota_entry` | 被担保人分录-子表 | 7 | [gm_guaranteequota.md](./gm_guaranteequota.md) |
