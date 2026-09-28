# pca 模块表清单

> 本模块共收录 **61** 张表定义，来自 `pca_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category pca
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_pca_balance` | 项目核算余额-主表 | 19 | [pca_balance.md](./pca_balance.md) |
| 2 | `t_pca_balanceentry` | 子要素核算明细-子表 | 17 | [pca_balance.md](./pca_balance.md) |
| 3 | `t_pca_balancestart` | 项目核算期初余额-主表 | 10 | [pca_balance_start.md](./pca_balance_start.md) |
| 4 | `t_pca_balancestart_entry` | 子要素核算明细-子表 | 9 | [pca_balance_start.md](./pca_balance_start.md) |
| 5 | `t_pca_bizoperation_log` | 项目成本执行日志-主表 | 14 | [pca_bizoperation_log.md](./pca_bizoperation_log.md) |
| 6 | `t_pca_calmodel` | 项目计算模型-主表 | 13 | [pca_calmodel.md](./pca_calmodel.md) |
| 7 | `t_pca_calmodel_l` | 项目计算模型-多语言表 | 4 | [pca_calmodel.md](./pca_calmodel.md) |
| 8 | `t_pca_calmodelentry` | 单据体-子表 | 5 | [pca_calmodel.md](./pca_calmodel.md) |
| 9 | `t_pca_calpolicy` | 项目计算执行策略-主表 | 14 | [pca_calpolicy.md](./pca_calpolicy.md) |
| 10 | `t_pca_calpolicy_l` | 项目计算执行策略-多语言表 | 4 | [pca_calpolicy.md](./pca_calpolicy.md) |
| 11 | `t_pca_calunit` | 项目计算逻辑单元-主表 | 14 | [pca_calunit.md](./pca_calunit.md) |
| 12 | `t_pca_calunit_l` | 项目计算逻辑单元-多语言表 | 4 | [pca_calunit.md](./pca_calunit.md) |
| 13 | `t_pca_calunitentry` | 单据体-子表 | 5 | [pca_calunit.md](./pca_calunit.md) |
| 14 | `t_pca_checkitem` | 检查项-主表 | 17 | [pca_checkitem.md](./pca_checkitem.md) |
| 15 | `t_pca_checkitem_l` | 检查项-多语言表 | 4 | [pca_checkitem.md](./pca_checkitem.md) |
| 16 | `t_pca_checkresult` | 检查结果单-主表 | 18 | [pca_checkresult.md](./pca_checkresult.md) |
| 17 | `t_pca_checkresultentry` | 单据体-子表 | 12 | [pca_checkresult.md](./pca_checkresult.md) |
| 18 | `t_pca_checkresultentry_l` | 单据体-多语言表 | 4 | [pca_checkresult.md](./pca_checkresult.md) |
| 19 | `t_pca_checkresultsubentry` | 子单据体-子表 | 7 | [pca_checkresult.md](./pca_checkresult.md) |
| 20 | `t_pca_collfieldmapentity` | 字段映射-子表 | 13 | [pca_collconfig.md](./pca_collconfig.md) |
| 21 | `t_pca_costaccount` | 项目核算主体-主表 | 18 | [pca_costaccount.md](./pca_costaccount.md) |
| 22 | `t_pca_costaccount` | 结束初始化-主表 | 18 | [pca_endinit.md](./pca_endinit.md) |
| 23 | `t_pca_costaccount_l` | 项目核算主体-多语言表 | 4 | [pca_costaccount.md](./pca_costaccount.md) |
| 24 | `t_pca_costaccount_l` | 结束初始化-多语言表 | 4 | [pca_endinit.md](./pca_endinit.md) |
| 25 | `t_pca_costalloc_result` | 项目公共费用分摊记录-主表 | 17 | [pca_costalloc_result.md](./pca_costalloc_result.md) |
| 26 | `t_pca_costalloc_result_e` | 分摊明细-子表 | 20 | [pca_costalloc_result.md](./pca_costalloc_result.md) |
| 27 | `t_pca_costcalreport` | 项目成本计算报告-主表 | 17 | [pca_costcalreport.md](./pca_costcalreport.md) |
| 28 | `t_pca_costcalreportentry` | 单据体-子表 | 8 | [pca_costcalreport.md](./pca_costcalreport.md) |
| 29 | `t_pca_costcollcommplan` | 项目公共费用来源设置-主表 | 16 | [pca_costcollcommplan.md](./pca_costcollcommplan.md) |
| 30 | `t_pca_costcollcommplan_l` | 项目公共费用来源设置-多语言表 | 5 | [pca_costcollcommplan.md](./pca_costcollcommplan.md) |
| 31 | `t_pca_costcollectconfig` | 项目归集配置单-主表 | 18 | [pca_collconfig.md](./pca_collconfig.md) |
| 32 | `t_pca_costcollectconfig_l` | 项目归集配置单-多语言表 | 5 | [pca_collconfig.md](./pca_collconfig.md) |
| 33 | `t_pca_costcollplan` | 项目成本来源设置-主表 | 17 | [pca_costcollplan.md](./pca_costcollplan.md) |
| 34 | `t_pca_costcollplan_aca` | 来源实际成本核算-子表 | 7 | [pca_costcollplan.md](./pca_costcollplan.md) |
| 35 | `t_pca_costcollplan_ap` | 来源应付-子表 | 5 | [pca_costcollplan.md](./pca_costcollplan.md) |
| 36 | `t_pca_costcollplan_cal` | 来源存货核算-子表 | 9 | [pca_costcollplan.md](./pca_costcollplan.md) |
| 37 | `t_pca_costcollplan_gl` | 来源系统总账-子表 | 10 | [pca_costcollcommplan.md](./pca_costcollcommplan.md) |
| 38 | `t_pca_costcollplan_gl` | 来源系统总账-子表 | 10 | [pca_costcollplan.md](./pca_costcollplan.md) |
| 39 | `t_pca_costcollplan_l` | 项目成本来源设置-多语言表 | 5 | [pca_costcollplan.md](./pca_costcollplan.md) |
| 40 | `t_pca_costcollplan_rmb` | 来源费用报销-子表 | 6 | [pca_costcollplan.md](./pca_costcollplan.md) |
| 41 | `t_pca_costinit` | 初始化数据录入-主表 | 16 | [pca_costinit.md](./pca_costinit.md) |
| 42 | `t_pca_costinitentry` | 初始明细数据-子表 | 6 | [pca_costinit.md](./pca_costinit.md) |
| 43 | `t_pca_costinitsubentry` | 成本要素明细-子表 | 6 | [pca_costinit.md](./pca_costinit.md) |
| 44 | `t_pca_costobject` | 项目成本核算对象-主表 | 29 | [pca_costobject.md](./pca_costobject.md) |
| 45 | `t_pca_costobject_l` | 项目成本核算对象-多语言表 | 4 | [pca_costobject.md](./pca_costobject.md) |
| 46 | `t_pca_costphases` | 项目成本阶段类型-主表 | 11 | [pca_projectcostphases.md](./pca_projectcostphases.md) |
| 47 | `t_pca_costphases_l` | 项目成本阶段类型-多语言表 | 5 | [pca_projectcostphases.md](./pca_projectcostphases.md) |
| 48 | `t_pca_costrec` | 项目成本核算单-主表 | 19 | [pca_costrecord.md](./pca_costrecord.md) |
| 49 | `t_pca_costrec_bill` | 业务单据明细信息-子表 | 20 | [pca_costrecord.md](./pca_costrecord.md) |
| 50 | `t_pca_costrec_bill_ele` | 成本要素明细-子表 | 12 | [pca_costrecord.md](./pca_costrecord.md) |
| 51 | `t_pca_costrec_comm` | 项目公共费用归集单-主表 | 18 | [pca_costrecord_comm.md](./pca_costrecord_comm.md) |
| 52 | `t_pca_costrec_comm_bill` | 业务单据明细信息-子表 | 16 | [pca_costrecord_comm.md](./pca_costrecord_comm.md) |
| 53 | `t_pca_costtrf` | 项目成本结转单-主表 | 14 | [pca_costtransfer.md](./pca_costtransfer.md) |
| 54 | `t_pca_costtrf_pro` | 项目明细-子表 | 9 | [pca_costtransfer.md](./pca_costtransfer.md) |
| 55 | `t_pca_costtrf_pro_ele` | 成本要素明细-子表 | 6 | [pca_costtransfer.md](./pca_costtransfer.md) |
| 56 | `t_pca_custallocrule` | 自定义分摊标准-主表 | 15 | [pca_custallocrule.md](./pca_custallocrule.md) |
| 57 | `t_pca_custallocruleentry` | 单据体-子表 | 7 | [pca_custallocrule.md](./pca_custallocrule.md) |
| 58 | `t_pca_exec_log` | 项目成本执行日志-主表 | 0 | [pca_exec_log.md](./pca_exec_log.md) |
| 59 | `t_pca_exec_log_l` | 单据体-子表 | 0 | [pca_exec_log.md](./pca_exec_log.md) |
| 60 | `t_pca_projtimecoll` | 项目工时归集单-主表 | 12 | [pca_projtimecoll.md](./pca_projtimecoll.md) |
| 61 | `t_pca_projtimecollentry` | 单据体-子表 | 11 | [pca_projtimecoll.md](./pca_projtimecoll.md) |
