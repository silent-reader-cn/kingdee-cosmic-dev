# xkpb 模块表清单

> 本模块共收录 **43** 张表定义，来自 `xkpb_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope xkpb
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_xkbm_budgetcalendar` | 预算日历-主表 | 24 | [xkpb_budgetcalendar.md](./xkpb_budgetcalendar.md) |
| 2 | `t_xkbm_budgetcalendar_l` | 预算日历-多语言表 | 5 | [xkpb_budgetcalendar.md](./xkpb_budgetcalendar.md) |
| 3 | `t_xkbm_budgetperiod` | 树形单据体-子表 | 12 | [xkpb_budgetcalendar.md](./xkpb_budgetcalendar.md) |
| 4 | `t_xkbm_budgetperiod_l` | 树形单据体-多语言表 | 5 | [xkpb_budgetcalendar.md](./xkpb_budgetcalendar.md) |
| 5 | `t_xkbm_ctrlbill` | 控制单据单据体-子表 | 35 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 6 | `t_xkbm_ctrlbill_l` | 控制单据单据体-多语言表 | 9 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 7 | `t_xkbm_ctrlbilldata` | 控制数据子单据体-子表 | 16 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 8 | `t_xkbm_ctrlbilldata_l` | 控制数据子单据体-多语言表 | 5 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 9 | `t_xkbm_ctrlbilldim` | 控制维度子单据体-子表 | 10 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 10 | `t_xkbm_ctrlbilldim_l` | 控制维度子单据体-多语言表 | 4 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 11 | `t_xkbm_ctrldata` | 控制项目数据类型单据体-子表 | 5 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 12 | `t_xkbm_ctrldim` | 控制维度单据体-子表 | 19 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 13 | `t_xkbm_ctrldim_l` | 控制维度单据体-多语言表 | 5 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 14 | `t_xkbm_ctrlrule` | 项目预算控制规则-主表 | 50 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 15 | `t_xkbm_ctrlrule_l` | 项目预算控制规则-多语言表 | 5 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 16 | `t_xkbm_effectorgunit` | 生效组织-多选基础资料表 | 3 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 17 | `t_xkbm_opratectrl` | 控制操作与强度单据体-子表 | 5 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 18 | `t_xkbm_systemparam` | 项目预算系统参数-主表 | 14 | [xkpb_systemparam.md](./xkpb_systemparam.md) |
| 19 | `t_xkpb_budgetadjust` | 项目预算变更单-主表 | 17 | [xkpb_budgetadjust.md](./xkpb_budgetadjust.md) |
| 20 | `t_xkpb_budgetadjust_l` | 项目预算变更单-多语言表 | 4 | [xkpb_budgetadjust.md](./xkpb_budgetadjust.md) |
| 21 | `t_xkpb_budgetadjustentry` | 预算变更-子表 | 21 | [xkpb_budgetadjust.md](./xkpb_budgetadjust.md) |
| 22 | `t_xkpb_budgetadjustentry_l` | 预算变更-多语言表 | 4 | [xkpb_budgetadjust.md](./xkpb_budgetadjust.md) |
| 23 | `t_xkpb_budgetvalue` | 项目预算预算数后台数据-主表 | 28 | [xkpb_budgetvalue.md](./xkpb_budgetvalue.md) |
| 24 | `t_xkpb_budgetvalue_assis` | 项目预算预算数辅助编制区-主表 | 28 | [xkpb_budgetvalue_assis.md](./xkpb_budgetvalue_assis.md) |
| 25 | `t_xkpb_costbudget` | 项目成本费用预算单-主表 | 28 | [xkpb_costbudget_f7.md](./xkpb_costbudget_f7.md) |
| 26 | `t_xkpb_costbudget` | 项目成本费用预算单-主表 | 28 | [xkpb_costbudgets.md](./xkpb_costbudgets.md) |
| 27 | `t_xkpb_costbudget_l` | 项目成本费用预算单-多语言表 | 4 | [xkpb_costbudget_f7.md](./xkpb_costbudget_f7.md) |
| 28 | `t_xkpb_costbudget_l` | 项目成本费用预算单-多语言表 | 4 | [xkpb_costbudgets.md](./xkpb_costbudgets.md) |
| 29 | `t_xkpb_ctrlrulegroup` | 项目预算控制规则分组-主表 | 11 | [xkpb_ctrlrulegroup.md](./xkpb_ctrlrulegroup.md) |
| 30 | `t_xkpb_ctrlrulegroup_l` | 项目预算控制规则分组-多语言表 | 5 | [xkpb_ctrlrulegroup.md](./xkpb_ctrlrulegroup.md) |
| 31 | `t_xkpb_ctrlruleorg` | 受控组织-多选基础资料表 | 3 | [xkpb_ctrlrule.md](./xkpb_ctrlrule.md) |
| 32 | `t_xkpb_dimensionvalue` | 项目成本费用预算额-子表 | 18 | [xkpb_costbudget_f7.md](./xkpb_costbudget_f7.md) |
| 33 | `t_xkpb_dimensionvalue` | 项目成本费用预算额-子表 | 18 | [xkpb_costbudgets.md](./xkpb_costbudgets.md) |
| 34 | `t_xkpb_dimensionvalue_l` | 项目成本费用预算额-多语言表 | 4 | [xkpb_costbudgets.md](./xkpb_costbudgets.md) |
| 35 | `t_xkpb_granularitydim` | 细粒度编制维度-多选基础资料表 | 3 | [xkpb_subelegranularity.md](./xkpb_subelegranularity.md) |
| 36 | `t_xkpb_granularityensub` | 成本子要素单据体-子表 | 4 | [xkpb_subelegranularity.md](./xkpb_subelegranularity.md) |
| 37 | `t_xkpb_granularityentry` | 成本要素单据体-子表 | 4 | [xkpb_subelegranularity.md](./xkpb_subelegranularity.md) |
| 38 | `t_xkpb_granularitygroup` | 成本子要素细粒度编制方案分组-主表 | 4 | [xkpb_granularitygroup.md](./xkpb_granularitygroup.md) |
| 39 | `t_xkpb_granularitygroup_l` | 成本子要素细粒度编制方案分组-多语言表 | 5 | [xkpb_granularitygroup.md](./xkpb_granularitygroup.md) |
| 40 | `t_xkpb_granularityproject` | 项目-多选基础资料表 | 3 | [xkpb_subelegranularity.md](./xkpb_subelegranularity.md) |
| 41 | `t_xkpb_granularitysubdim` | 细粒度编制维度-多选基础资料表 | 3 | [xkpb_subelegranularity.md](./xkpb_subelegranularity.md) |
| 42 | `t_xkpb_subelegranularity` | 成本子要素细粒度编制方案-主表 | 13 | [xkpb_subelegranularity.md](./xkpb_subelegranularity.md) |
| 43 | `t_xkpb_subelegranularity_l` | 成本子要素细粒度编制方案-多语言表 | 5 | [xkpb_subelegranularity.md](./xkpb_subelegranularity.md) |
