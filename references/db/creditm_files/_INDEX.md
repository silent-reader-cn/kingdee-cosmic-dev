# creditm 模块表清单

> 本模块共收录 **35** 张表定义，来自 `creditm_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category creditm
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_cfm_creditagree` | 授信框架协议-主表 | 27 | [cfm_creditlimitagree.md](./cfm_creditlimitagree.md) |
| 2 | `t_cfm_creditagree_l` | 授信框架协议-多语言表 | 4 | [cfm_creditlimitagree.md](./cfm_creditlimitagree.md) |
| 3 | `t_cfm_creditagree_m` | 授信框架协议-使用范围位图表 | 2 | [cfm_creditlimitagree.md](./cfm_creditlimitagree.md) |
| 4 | `t_cfm_creditagree_org` | 成员组织分录-子表 | 4 | [cfm_creditlimitagree.md](./cfm_creditlimitagree.md) |
| 5 | `t_cfm_creditagree_type` | 类别限额分录-子表 | 5 | [cfm_creditlimitagree.md](./cfm_creditlimitagree.md) |
| 6 | `t_cfm_creditagree_type_c` | 授信类别-多选基础资料表 | 3 | [cfm_creditlimitagree.md](./cfm_creditlimitagree.md) |
| 7 | `t_cfm_creditagree_u` | 授信框架协议-使用范围表 | 3 | [cfm_creditlimitagree.md](./cfm_creditlimitagree.md) |
| 8 | `t_cfm_creditlimit` | 授信合同-主表 | 50 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 9 | `t_cfm_creditlimit_detai_c` | 资金组织-多选基础资料表 | 3 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 10 | `t_cfm_creditlimit_detai_d` | 授信类别-多选基础资料表 | 3 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 11 | `t_cfm_creditlimit_l` | 授信合同-多语言表 | 5 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 12 | `t_cfm_creditlimit_lk` | 关联子实体-子表 | 6 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 13 | `t_cfm_creditlimit_m` | 授信合同-使用范围位图表 | 2 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 14 | `t_cfm_creditlimit_merge` | 源单ID列表-多选基础资料表 | 3 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 15 | `t_cfm_creditlimit_mult` | 混合共享分录-子表 | 8 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 16 | `t_cfm_creditlimit_mult_o` | 资金组织-多选基础资料表 | 3 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 17 | `t_cfm_creditlimit_mult_t` | 授信类别-多选基础资料表 | 3 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 18 | `t_cfm_creditlimit_org` | 组织共享分录-子表 | 10 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 19 | `t_cfm_creditlimit_type` | 类别共享分录-子表 | 10 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 20 | `t_cfm_creditlimit_u` | 授信合同-使用范围表 | 3 | [cfm_creditlimit.md](./cfm_creditlimit.md) |
| 21 | `t_cfm_creditreturn` | 授信额度返还单-主表 | 28 | [cfm_creditreturn.md](./cfm_creditreturn.md) |
| 22 | `t_cfm_creditreturn_l` | 授信额度返还单-多语言表 | 4 | [cfm_creditreturn.md](./cfm_creditreturn.md) |
| 23 | `t_cfm_credittype` | 授信类别-主表 | 21 | [cfm_credittype.md](./cfm_credittype.md) |
| 24 | `t_cfm_credittype_entry` | 单据体-子表 | 5 | [cfm_credittype.md](./cfm_credittype.md) |
| 25 | `t_cfm_credittype_l` | 授信类别-多语言表 | 5 | [cfm_credittype.md](./cfm_credittype.md) |
| 26 | `t_cfm_credituse` | 授信额度占用单-主表 | 40 | [cfm_credituse.md](./cfm_credituse.md) |
| 27 | `t_cfm_credituse_l` | 授信额度占用单-多语言表 | 4 | [cfm_credituse.md](./cfm_credituse.md) |
| 28 | `t_cfm_credituse_return` | 单据体-子表 | 11 | [cfm_credituse.md](./cfm_credituse.md) |
| 29 | `t_cfm_use_credit` | 手工用信登记-主表 | 43 | [cfm_use_credit.md](./cfm_use_credit.md) |
| 30 | `t_creditm_apply` | 授信申请-主表 | 29 | [creditm_apply.md](./creditm_apply.md) |
| 31 | `t_creditm_apply_l` | 授信申请-多语言表 | 4 | [creditm_apply.md](./creditm_apply.md) |
| 32 | `t_creditm_apply_org` | 组织共享分录-子表 | 7 | [creditm_apply.md](./creditm_apply.md) |
| 33 | `t_creditm_apply_org_m` | 资金组织-多选基础资料表 | 3 | [creditm_apply.md](./creditm_apply.md) |
| 34 | `t_creditm_apply_type` | 类别共享分录-子表 | 6 | [creditm_apply.md](./creditm_apply.md) |
| 35 | `t_creditm_apply_type_m` | 授信类别-多选基础资料表 | 3 | [creditm_apply.md](./creditm_apply.md) |
