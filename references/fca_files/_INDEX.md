# fca 模块表清单

> 本模块共收录 **53** 张表定义，来自 `fca_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope fca
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fca_acctgroup` | 母子账户组-主表 | 23 | [fca_acctgroup.md](./fca_acctgroup.md) |
| 2 | `t_fca_acctgroup` | 母子账户组（F7以母子账户组及母账户信息维度）-主表 | 23 | [fca_acctgroup_inh.md](./fca_acctgroup_inh.md) |
| 3 | `t_fca_acctgroup_entrys` | 子账户信息-子表 | 10 | [fca_acctgroup.md](./fca_acctgroup.md) |
| 4 | `t_fca_acctgroup_entrys` | 子账户信息-子表 | 10 | [fca_acctgroup_inh.md](./fca_acctgroup_inh.md) |
| 5 | `t_fca_acctgroup_l` | 母子账户组-多语言表 | 6 | [fca_acctgroup.md](./fca_acctgroup.md) |
| 6 | `t_fca_acctgroup_l` | 母子账户组（F7以母子账户组及母账户信息维度）-多语言表 | 6 | [fca_acctgroup_inh.md](./fca_acctgroup_inh.md) |
| 7 | `t_fca_applytransdownbill_lk` | 关联子实体-子表 | 6 | [fca_applytransdownbill.md](./fca_applytransdownbill.md) |
| 8 | `t_fca_applytransdownbill_tc` | 资金请款申请-关联追踪表 | 7 | [fca_applytransdownbill.md](./fca_applytransdownbill.md) |
| 9 | `t_fca_applytransdownbill_wb` | 资金请款申请-反写记录表 | 10 | [fca_applytransdownbill.md](./fca_applytransdownbill.md) |
| 10 | `t_fca_applytransupbill_lk` | 关联子实体-子表 | 6 | [fca_applytransupbill.md](./fca_applytransupbill.md) |
| 11 | `t_fca_applytransupbill_tc` | 资金上划申请-关联追踪表 | 7 | [fca_applytransupbill.md](./fca_applytransupbill.md) |
| 12 | `t_fca_applytransupbill_wb` | 资金上划申请-反写记录表 | 10 | [fca_applytransupbill.md](./fca_applytransupbill.md) |
| 13 | `t_fca_apptransdown` | 资金请款申请-主表 | 20 | [fca_applytransdownbill.md](./fca_applytransdownbill.md) |
| 14 | `t_fca_apptransdown_entry` | 划拨明细-子表 | 17 | [fca_applytransdownbill.md](./fca_applytransdownbill.md) |
| 15 | `t_fca_apptransdown_entry_l` | 划拨明细-多语言表 | 4 | [fca_applytransdownbill.md](./fca_applytransdownbill.md) |
| 16 | `t_fca_apptransdown_l` | 资金请款申请-多语言表 | 4 | [fca_applytransdownbill.md](./fca_applytransdownbill.md) |
| 17 | `t_fca_apptransup` | 资金上划申请-主表 | 20 | [fca_applytransupbill.md](./fca_applytransupbill.md) |
| 18 | `t_fca_apptransup_entry` | 划拨明细-子表 | 17 | [fca_applytransupbill.md](./fca_applytransupbill.md) |
| 19 | `t_fca_apptransup_entry_l` | 划拨明细-多语言表 | 4 | [fca_applytransupbill.md](./fca_applytransupbill.md) |
| 20 | `t_fca_apptransup_l` | 资金上划申请-多语言表 | 4 | [fca_applytransupbill.md](./fca_applytransupbill.md) |
| 21 | `t_fca_autotrans` | 自动划拨设置-主表 | 22 | [fca_autotrans.md](./fca_autotrans.md) |
| 22 | `t_fca_autotrans_acctgroup` | 母子账户信息-子表 | 6 | [fca_autotrans.md](./fca_autotrans.md) |
| 23 | `t_fca_autotrans_entry` | 调拨明细-子表 | 16 | [fca_autotrans.md](./fca_autotrans.md) |
| 24 | `t_fca_autotrans_l` | 自动划拨设置-多语言表 | 5 | [fca_autotrans.md](./fca_autotrans.md) |
| 25 | `t_fca_autotranslog` | 自动划拨执行日志-主表 | 7 | [fca_autotranslog.md](./fca_autotranslog.md) |
| 26 | `t_fca_autotranslog_cash` | 调拨明细-子表 | 17 | [fca_autotranslog.md](./fca_autotranslog.md) |
| 27 | `t_fca_autotranslog_entry` | 单据体-子表 | 11 | [fca_autotranslog.md](./fca_autotranslog.md) |
| 28 | `t_fca_cash_poolsetting` | 我关注的现金池设置-主表 | 3 | [fca_cash_poolsetting.md](./fca_cash_poolsetting.md) |
| 29 | `t_fca_transchgbill` | 变更支付渠道-主表 | 25 | [fca_transchgbill.md](./fca_transchgbill.md) |
| 30 | `t_fca_transchgbill_entry` | 划拨明细-子表 | 10 | [fca_transchgbill.md](./fca_transchgbill.md) |
| 31 | `t_fca_transchgbill_entry_lk` | 关联子实体-子表 | 6 | [fca_transchgbill.md](./fca_transchgbill.md) |
| 32 | `t_fca_transchgbill_l` | 变更支付渠道-多语言表 | 4 | [fca_transchgbill.md](./fca_transchgbill.md) |
| 33 | `t_fca_transchgbill_lk` | 关联子实体-子表 | 6 | [fca_transchgbill.md](./fca_transchgbill.md) |
| 34 | `t_fca_transchgbill_tc` | 变更支付渠道-关联追踪表 | 7 | [fca_transchgbill.md](./fca_transchgbill.md) |
| 35 | `t_fca_transchgbill_wb` | 变更支付渠道-反写记录表 | 10 | [fca_transchgbill.md](./fca_transchgbill.md) |
| 36 | `t_fca_transdownbill` | 资金下拨单-主表 | 40 | [fca_transdownbill.md](./fca_transdownbill.md) |
| 37 | `t_fca_transdownbill_entry` | 下拨明细-子表 | 30 | [fca_transdownbill.md](./fca_transdownbill.md) |
| 38 | `t_fca_transdownbill_entry_lk` | 关联子实体-子表 | 6 | [fca_transdownbill.md](./fca_transdownbill.md) |
| 39 | `t_fca_transdownbill_l` | 资金下拨单-多语言表 | 4 | [fca_transdownbill.md](./fca_transdownbill.md) |
| 40 | `t_fca_transdownbill_lk` | 关联子实体-子表 | 6 | [fca_transdownbill.md](./fca_transdownbill.md) |
| 41 | `t_fca_transdownbill_tc` | 资金下拨单-关联追踪表 | 7 | [fca_transdownbill.md](./fca_transdownbill.md) |
| 42 | `t_fca_transdownbill_wb` | 资金下拨单-反写记录表 | 10 | [fca_transdownbill.md](./fca_transdownbill.md) |
| 43 | `t_fca_transdowndetail_lk` | 关联子实体-子表 | 6 | [fca_applytransdownbill.md](./fca_applytransdownbill.md) |
| 44 | `t_fca_transtrategy` | 账户划拨策略-主表 | 28 | [fca_transtrategy.md](./fca_transtrategy.md) |
| 45 | `t_fca_transtrategy_l` | 账户划拨策略-多语言表 | 5 | [fca_transtrategy.md](./fca_transtrategy.md) |
| 46 | `t_fca_transupbill` | 资金上划单-主表 | 40 | [fca_transupbill.md](./fca_transupbill.md) |
| 47 | `t_fca_transupbill_entry` | 划拨明细-子表 | 30 | [fca_transupbill.md](./fca_transupbill.md) |
| 48 | `t_fca_transupbill_entry_lk` | 关联子实体-子表 | 6 | [fca_transupbill.md](./fca_transupbill.md) |
| 49 | `t_fca_transupbill_l` | 资金上划单-多语言表 | 4 | [fca_transupbill.md](./fca_transupbill.md) |
| 50 | `t_fca_transupbill_lk` | 关联子实体-子表 | 6 | [fca_transupbill.md](./fca_transupbill.md) |
| 51 | `t_fca_transupbill_tc` | 资金上划单-关联追踪表 | 7 | [fca_transupbill.md](./fca_transupbill.md) |
| 52 | `t_fca_transupbill_wb` | 资金上划单-反写记录表 | 10 | [fca_transupbill.md](./fca_transupbill.md) |
| 53 | `t_fca_transupdetail_lk` | 关联子实体-子表 | 6 | [fca_applytransupbill.md](./fca_applytransupbill.md) |
