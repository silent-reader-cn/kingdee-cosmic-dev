# fr 模块表清单

> 本模块共收录 **26** 张表定义，来自 `fr_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope fr
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_fr_amortassgrpentry` | 科目核算维度-子表 | 9 | [fr_manualtallybill.md](./fr_manualtallybill.md) |
| 2 | `t_fr_amortmainassgrpentry` | 主表项目核算维度-子表 | 9 | [fr_manualtallybill.md](./fr_manualtallybill.md) |
| 3 | `t_fr_glrassoapply` | 关联申请分录-子表 | 15 | [fr_glreim_paybill.md](./fr_glreim_paybill.md) |
| 4 | `t_fr_glrpaybill` | 总账付款申请单-主表 | 39 | [fr_glreim_paybill.md](./fr_glreim_paybill.md) |
| 5 | `t_fr_glrpaybill_l` | 总账付款申请单-多语言表 | 4 | [fr_glreim_paybill.md](./fr_glreim_paybill.md) |
| 6 | `t_fr_glrpayplan` | 付款计划分录-子表 | 11 | [fr_glreim_paybill.md](./fr_glreim_paybill.md) |
| 7 | `t_fr_glrpayplanwriteback` | 付款计划子分录(反写)-子表 | 8 | [fr_glreim_paybill.md](./fr_glreim_paybill.md) |
| 8 | `t_fr_glrpaytallydetail` | 记账明细分录-子表 | 10 | [fr_glreim_paybill.md](./fr_glreim_paybill.md) |
| 9 | `t_fr_glrrecbill` | 总账收款申请单-主表 | 37 | [fr_glreim_recbill.md](./fr_glreim_recbill.md) |
| 10 | `t_fr_glrrecbill_l` | 总账收款申请单-多语言表 | 4 | [fr_glreim_recbill.md](./fr_glreim_recbill.md) |
| 11 | `t_fr_glrreccaswriteback` | 资金反写分录-子表 | 7 | [fr_glreim_recbill.md](./fr_glreim_recbill.md) |
| 12 | `t_fr_glrreccaventry` | 核销付款-子表 | 19 | [fr_glreim_recbill.md](./fr_glreim_recbill.md) |
| 13 | `t_fr_glrrecsettleentry` | 结算信息-子表 | 15 | [fr_glreim_recbill.md](./fr_glreim_recbill.md) |
| 14 | `t_fr_glrrectallyentry` | 记账明细-子表 | 11 | [fr_glreim_recbill.md](./fr_glreim_recbill.md) |
| 15 | `t_fr_manutalbill` | 通用转账申请单-主表 | 39 | [fr_manualtallybill.md](./fr_manualtallybill.md) |
| 16 | `t_fr_manutalbill_l` | 通用转账申请单-多语言表 | 4 | [fr_manualtallybill.md](./fr_manualtallybill.md) |
| 17 | `t_fr_manutalbill_tc` | 通用转账申请单-关联追踪表 | 7 | [fr_manualtallybill.md](./fr_manualtallybill.md) |
| 18 | `t_fr_manutalbill_wb` | 通用转账申请单-反写记录表 | 10 | [fr_manualtallybill.md](./fr_manualtallybill.md) |
| 19 | `t_fr_manutalentry` | 记账明细-子表 | 31 | [fr_manualtallybill.md](./fr_manualtallybill.md) |
| 20 | `t_fr_manutalentry_lk` | 关联子实体-子表 | 7 | [fr_manualtallybill.md](./fr_manualtallybill.md) |
| 21 | `t_tk_tallyapplybill` | 记账申请单-主表 | 29 | [ssc_tallyapplybill.md](./ssc_tallyapplybill.md) |
| 22 | `t_tk_tallyapplybill_l` | 记账申请单-多语言表 | 4 | [ssc_tallyapplybill.md](./ssc_tallyapplybill.md) |
| 23 | `t_tk_tallyapplybill_tc` | 记账申请单-关联追踪表 | 7 | [ssc_tallyapplybill.md](./ssc_tallyapplybill.md) |
| 24 | `t_tk_tallyapplybill_wb` | 记账申请单-反写记录表 | 10 | [ssc_tallyapplybill.md](./ssc_tallyapplybill.md) |
| 25 | `t_tk_tallydetail` | 记账明细-子表 | 18 | [ssc_tallyapplybill.md](./ssc_tallyapplybill.md) |
| 26 | `t_tk_tallyentity_lk` | 关联子实体-子表 | 6 | [ssc_tallyapplybill.md](./ssc_tallyapplybill.md) |
