# frm 模块表清单

> 本模块共收录 **53** 张表定义，来自 `frm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category frm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ai_acctfieldmapentry` | 字段映射-子表 | 7 | [ai_rec_common_filter.md](./ai_rec_common_filter.md) |
| 2 | `t_ai_acctfieldmapentry` | 字段映射-子表 | 7 | [frm_rec_common_filter.md](./frm_rec_common_filter.md) |
| 3 | `t_ai_amounttype` | 取数类型_继承-主表 | 9 | [ai_amount_type.md](./ai_amount_type.md) |
| 4 | `t_ai_amounttype` | 对账类型-主表 | 9 | [frm_amount_type.md](./frm_amount_type.md) |
| 5 | `t_ai_amounttype_l` | 取数类型_继承-多语言表 | 4 | [ai_amount_type.md](./ai_amount_type.md) |
| 6 | `t_ai_amounttype_l` | 对账类型-多语言表 | 4 | [frm_amount_type.md](./frm_amount_type.md) |
| 7 | `t_ai_amounttypeentry` | 金额类别-子表 | 12 | [ai_amount_type.md](./ai_amount_type.md) |
| 8 | `t_ai_amounttypeentry` | 对账类型-主表 | 12 | [ai_amouttype_layout.md](./ai_amouttype_layout.md) |
| 9 | `t_ai_amounttypeentry` | 金额类别-子表 | 12 | [frm_amount_type.md](./frm_amount_type.md) |
| 10 | `t_ai_amounttypeentry` | 对账类型-主表 | 12 | [frm_amouttype_layout.md](./frm_amouttype_layout.md) |
| 11 | `t_ai_amounttypeentry_l` | 金额类别-多语言表 | 4 | [ai_amount_type.md](./ai_amount_type.md) |
| 12 | `t_ai_amounttypeentry_l` | 对账类型-多语言表 | 4 | [ai_amouttype_layout.md](./ai_amouttype_layout.md) |
| 13 | `t_ai_amounttypeentry_l` | 金额类别-多语言表 | 4 | [frm_amount_type.md](./frm_amount_type.md) |
| 14 | `t_ai_amounttypeentry_l` | 对账类型-多语言表 | 4 | [frm_amouttype_layout.md](./frm_amouttype_layout.md) |
| 15 | `t_ai_rec_common_assist` | 对账维度-多选基础资料表 | 3 | [ai_rec_common_filter.md](./ai_rec_common_filter.md) |
| 16 | `t_ai_rec_common_assist` | 对账维度-多选基础资料表 | 3 | [frm_rec_common_filter.md](./frm_rec_common_filter.md) |
| 17 | `t_ai_rec_common_entry` | 单据体-子表 | 11 | [ai_rec_common_filter.md](./ai_rec_common_filter.md) |
| 18 | `t_ai_rec_common_entry` | 单据体-子表 | 11 | [frm_rec_common_filter.md](./frm_rec_common_filter.md) |
| 19 | `t_ai_rec_common_filter` | 对账通用设置_继承-主表 | 14 | [ai_rec_common_filter.md](./ai_rec_common_filter.md) |
| 20 | `t_ai_rec_common_filter` | 对账通用设置-主表 | 14 | [frm_rec_common_filter.md](./frm_rec_common_filter.md) |
| 21 | `t_ai_rec_common_filter_l` | 对账通用设置_继承-多语言表 | 4 | [ai_rec_common_filter.md](./ai_rec_common_filter.md) |
| 22 | `t_ai_rec_common_filter_l` | 对账通用设置-多语言表 | 4 | [frm_rec_common_filter.md](./frm_rec_common_filter.md) |
| 23 | `t_ai_rec_impl` | 对账业务接口实现-主表 | 0 | [frm_reconciliation_impl.md](./frm_reconciliation_impl.md) |
| 24 | `t_ai_rec_impl_entry` | 单据体-子表 | 0 | [frm_reconciliation_impl.md](./frm_reconciliation_impl.md) |
| 25 | `t_ai_rec_impl_l` | 对账业务接口实现-多语言表 | 0 | [frm_reconciliation_impl.md](./frm_reconciliation_impl.md) |
| 26 | `t_ai_recdatarule` | 业务取数规则-主表 | 24 | [frm_recdatarule.md](./frm_recdatarule.md) |
| 27 | `t_ai_recdatarule_assist` | 业务维度-多选基础资料表 | 3 | [frm_recdatarule.md](./frm_recdatarule.md) |
| 28 | `t_ai_recdatarule_l` | 业务取数规则-多语言表 | 4 | [frm_recdatarule.md](./frm_recdatarule.md) |
| 29 | `t_ai_recdatarule_m` | 业务取数规则-使用范围位图表 | 2 | [frm_recdatarule.md](./frm_recdatarule.md) |
| 30 | `t_ai_recdatarule_u` | 业务取数规则-使用范围表 | 3 | [frm_recdatarule.md](./frm_recdatarule.md) |
| 31 | `t_ai_recdataruleentry` | 取数规则-子表 | 26 | [frm_recdatarule.md](./frm_recdatarule.md) |
| 32 | `t_ai_recdataruleentry_l` | 取数规则-多语言表 | 5 | [frm_recdatarule.md](./frm_recdatarule.md) |
| 33 | `t_ai_recdimconfig` | 对账维度配置-主表 | 14 | [frm_rec_dimconfig.md](./frm_rec_dimconfig.md) |
| 34 | `t_ai_recdimconfig_l` | 对账维度配置-多语言表 | 4 | [frm_rec_dimconfig.md](./frm_rec_dimconfig.md) |
| 35 | `t_ai_recon_scheme` | 业财对账方案-主表 | 29 | [frm_reconciliation_scheme.md](./frm_reconciliation_scheme.md) |
| 36 | `t_ai_recon_scheme_acct` | 科目-多选基础资料表 | 3 | [frm_reconciliation_scheme.md](./frm_reconciliation_scheme.md) |
| 37 | `t_ai_recon_scheme_amtype2` | 对账类型-多选基础资料表 | 4 | [frm_reconciliation_scheme.md](./frm_reconciliation_scheme.md) |
| 38 | `t_ai_recon_scheme_books` | 适用账簿-多选基础资料表 | 3 | [frm_reconciliation_scheme.md](./frm_reconciliation_scheme.md) |
| 39 | `t_ai_recon_scheme_l` | 业财对账方案-多语言表 | 4 | [frm_reconciliation_scheme.md](./frm_reconciliation_scheme.md) |
| 40 | `t_ai_recon_scheme_m` | 业财对账方案-使用范围位图表 | 2 | [frm_reconciliation_scheme.md](./frm_reconciliation_scheme.md) |
| 41 | `t_ai_recon_scheme_u` | 业财对账方案-使用范围表 | 3 | [frm_reconciliation_scheme.md](./frm_reconciliation_scheme.md) |
| 42 | `t_ai_recon_tab3entry` | 对账设置-子表 | 18 | [frm_reconciliation_scheme.md](./frm_reconciliation_scheme.md) |
| 43 | `t_frm_rec_sumentry_acct` | 科目-多选基础资料表 | 3 | [frm_rec_summary.md](./frm_rec_summary.md) |
| 44 | `t_frm_rec_summary` | 对账汇总结果快照-主表 | 11 | [frm_rec_summary.md](./frm_rec_summary.md) |
| 45 | `t_frm_rec_summaryentry` | 单据体-子表 | 29 | [frm_rec_summary.md](./frm_rec_summary.md) |
| 46 | `t_frm_sumentry_acct` | 科目-多选基础资料表 | 3 | [frm_sumresult.md](./frm_sumresult.md) |
| 47 | `t_frm_sumresult` | 对账汇总结果-主表 | 9 | [frm_sumresult.md](./frm_sumresult.md) |
| 48 | `t_frm_sumresultentry` | 单据体-子表 | 26 | [frm_sumresult.md](./frm_sumresult.md) |
| 49 | `t_frm_task` | 对账任务-主表 | 26 | [frm_task.md](./frm_task.md) |
| 50 | `t_frm_task_account` | 科目-多选基础资料表 | 3 | [frm_task.md](./frm_task.md) |
| 51 | `t_frm_task_amounttype` | 取数类型-多选基础资料表 | 3 | [frm_task.md](./frm_task.md) |
| 52 | `t_frm_task_detail` | 取数规则分录-子表 | 15 | [frm_task.md](./frm_task.md) |
| 53 | `t_frm_task_entry` | 对账方案分录-子表 | 11 | [frm_task.md](./frm_task.md) |
