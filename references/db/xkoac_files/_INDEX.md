# xkoac 模块表清单

> 本模块共收录 **70** 张表定义，来自 `xkoac_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category xkoac
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_xkoac_account` | 经营科目-主表 | 21 | [xkoac_account.md](./xkoac_account.md) |
| 2 | `t_xkoac_account_l` | 经营科目-多语言表 | 5 | [xkoac_account.md](./xkoac_account.md) |
| 3 | `t_xkoac_accountentry` | 单据体-子表 | 5 | [xkoac_account.md](./xkoac_account.md) |
| 4 | `t_xkoac_accounttable` | 经营科目表-主表 | 13 | [xkoac_accounttable.md](./xkoac_accounttable.md) |
| 5 | `t_xkoac_accounttable_l` | 经营科目表-多语言表 | 5 | [xkoac_accounttable.md](./xkoac_accounttable.md) |
| 6 | `t_xkoac_allctplan` | 经营费用分摊执行方案-主表 | 9 | [xkoac_expensealloctplan.md](./xkoac_expensealloctplan.md) |
| 7 | `t_xkoac_allctplan_l` | 经营费用分摊执行方案-多语言表 | 4 | [xkoac_expensealloctplan.md](./xkoac_expensealloctplan.md) |
| 8 | `t_xkoac_allctplanentity` | 选择经营账簿-子表 | 7 | [xkoac_expensealloctplan.md](./xkoac_expensealloctplan.md) |
| 9 | `t_xkoac_allctplansub` | 选择经营费用分摊方案-子表 | 4 | [xkoac_expensealloctplan.md](./xkoac_expensealloctplan.md) |
| 10 | `t_xkoac_allctreportentry` | 报告明细-子表 | 6 | [xkoac_allocatereport.md](./xkoac_allocatereport.md) |
| 11 | `t_xkoac_allocateentity` | 单据体-子表 | 11 | [xkoac_allocationplan.md](./xkoac_allocationplan.md) |
| 12 | `t_xkoac_allocateentity_l` | 单据体-多语言表 | 5 | [xkoac_allocationplan.md](./xkoac_allocationplan.md) |
| 13 | `t_xkoac_allocatereport` | 经营费用分摊报告-主表 | 15 | [xkoac_allocatereport.md](./xkoac_allocatereport.md) |
| 14 | `t_xkoac_allocatesub` | 分摊目标-子表 | 4 | [xkoac_allocationplan.md](./xkoac_allocationplan.md) |
| 15 | `t_xkoac_allocationplan` | 经营费用分摊方案-主表 | 18 | [xkoac_allocationplan.md](./xkoac_allocationplan.md) |
| 16 | `t_xkoac_allocationplan_l` | 经营费用分摊方案-多语言表 | 5 | [xkoac_allocationplan.md](./xkoac_allocationplan.md) |
| 17 | `t_xkoac_assist` | 经营核算维度横表-主表 | 3 | [xkoac_assist.md](./xkoac_assist.md) |
| 18 | `t_xkoac_assist_bd` | 经营核算维度基础资料-主表 | 4 | [xkoac_assist_bd.md](./xkoac_assist_bd.md) |
| 19 | `t_xkoac_assist_txt` | 经营核算维度文本-主表 | 4 | [xkoac_assist_txt.md](./xkoac_assist_txt.md) |
| 20 | `t_xkoac_balance` | 经营余额表-主表 | 24 | [xkoac_balance.md](./xkoac_balance.md) |
| 21 | `t_xkoac_buildreport` | 经营流水账生成报告-主表 | 21 | [xkoac_buildreport.md](./xkoac_buildreport.md) |
| 22 | `t_xkoac_buildreportentry` | 报告明细-子表 | 6 | [xkoac_buildreport.md](./xkoac_buildreport.md) |
| 23 | `t_xkoac_businessplan` | 经营计划单-主表 | 16 | [xkoac_businessplan.md](./xkoac_businessplan.md) |
| 24 | `t_xkoac_busiplanentry` | 单据体-子表 | 7 | [xkoac_businessplan.md](./xkoac_businessplan.md) |
| 25 | `t_xkoac_busiplanentry_l` | 单据体-多语言表 | 4 | [xkoac_businessplan.md](./xkoac_businessplan.md) |
| 26 | `t_xkoac_costcollecte` | 经营费用归集单-主表 | 23 | [xkoac_costcollecte.md](./xkoac_costcollecte.md) |
| 27 | `t_xkoac_costcollecte_l` | 经营费用归集单-多语言表 | 4 | [xkoac_costcollecte.md](./xkoac_costcollecte.md) |
| 28 | `t_xkoac_costcollectentry` | 单据体-子表 | 13 | [xkoac_costcollecte.md](./xkoac_costcollecte.md) |
| 29 | `t_xkoac_costshare` | 经营费用分摊结果单-主表 | 25 | [xkoac_allocationresults.md](./xkoac_allocationresults.md) |
| 30 | `t_xkoac_costshareentry` | 单据体-子表 | 10 | [xkoac_allocationresults.md](./xkoac_allocationresults.md) |
| 31 | `t_xkoac_initaccount` | 经营科目初始化-主表 | 10 | [xkoac_initaccount.md](./xkoac_initaccount.md) |
| 32 | `t_xkoac_initaccountentry` | 树形单据体-子表 | 13 | [xkoac_initaccount.md](./xkoac_initaccount.md) |
| 33 | `t_xkoac_initsubentry` | 子单据体-子表 | 6 | [xkoac_initaccount.md](./xkoac_initaccount.md) |
| 34 | `t_xkoac_instatement` | 经营单元内部结算单-主表 | 17 | [xkoac_instatement.md](./xkoac_instatement.md) |
| 35 | `t_xkoac_instatemententry` | 分录-子表 | 12 | [xkoac_instatement.md](./xkoac_instatement.md) |
| 36 | `t_xkoac_instatemententry_l` | 分录-多语言表 | 4 | [xkoac_instatement.md](./xkoac_instatement.md) |
| 37 | `t_xkoac_operatingbook` | 经营账簿-主表 | 29 | [xkoac_operatingbook.md](./xkoac_operatingbook.md) |
| 38 | `t_xkoac_operatingbook_l` | 经营账簿-多语言表 | 5 | [xkoac_operatingbook.md](./xkoac_operatingbook.md) |
| 39 | `t_xkoac_orgstructure` | 经营组织架构版本-多选基础资料表 | 3 | [xkoac_allocationplan.md](./xkoac_allocationplan.md) |
| 40 | `t_xkoac_orgsystem` | 经营组织架构版本-主表 | 17 | [xkoac_orgsystem.md](./xkoac_orgsystem.md) |
| 41 | `t_xkoac_orgsystem_l` | 经营组织架构版本-多语言表 | 4 | [xkoac_orgsystem.md](./xkoac_orgsystem.md) |
| 42 | `t_xkoac_orgsystementry` | 经营组织架构单据体-子表 | 8 | [xkoac_orgsystem.md](./xkoac_orgsystem.md) |
| 43 | `t_xkoac_orgsystemgroup` | 经营组织架构-主表 | 13 | [xkoac_orgsystemgroup.md](./xkoac_orgsystemgroup.md) |
| 44 | `t_xkoac_orgsystemgroup_l` | 经营组织架构-多语言表 | 5 | [xkoac_orgsystemgroup.md](./xkoac_orgsystemgroup.md) |
| 45 | `t_xkoac_setpricebook` | 适用经营账簿-多选基础资料表 | 3 | [xkoac_settleprice.md](./xkoac_settleprice.md) |
| 46 | `t_xkoac_setpricebuyer` | 买方经营单元-多选基础资料表 | 3 | [xkoac_settleprice.md](./xkoac_settleprice.md) |
| 47 | `t_xkoac_setpriceentry` | 单据体-子表 | 14 | [xkoac_settleprice.md](./xkoac_settleprice.md) |
| 48 | `t_xkoac_setpriceseller` | 卖方经营单元-多选基础资料表 | 3 | [xkoac_settleprice.md](./xkoac_settleprice.md) |
| 49 | `t_xkoac_settleprice` | 经营单元结算价目表-主表 | 17 | [xkoac_settleprice.md](./xkoac_settleprice.md) |
| 50 | `t_xkoac_settleprice_l` | 经营单元结算价目表-多语言表 | 4 | [xkoac_settleprice.md](./xkoac_settleprice.md) |
| 51 | `t_xkoac_shareweightentry` | 单据体-子表 | 5 | [xkoac_shareweights.md](./xkoac_shareweights.md) |
| 52 | `t_xkoac_shareweights` | 固定分摊权重-主表 | 16 | [xkoac_shareweights.md](./xkoac_shareweights.md) |
| 53 | `t_xkoac_shareweights_l` | 固定分摊权重-多语言表 | 4 | [xkoac_shareweights.md](./xkoac_shareweights.md) |
| 54 | `t_xkoac_vchimptplan` | 经营流水账来源方案-主表 | 25 | [xkoac_voucherimptplan.md](./xkoac_voucherimptplan.md) |
| 55 | `t_xkoac_vchimptplan_l` | 经营流水账来源方案-多语言表 | 4 | [xkoac_voucherimptplan.md](./xkoac_voucherimptplan.md) |
| 56 | `t_xkoac_vchplanbook` | 适用经营账簿-多选基础资料表 | 3 | [xkoac_voucherimptplan.md](./xkoac_voucherimptplan.md) |
| 57 | `t_xkoac_vchplanentry` | 数据来源-子表 | 23 | [xkoac_voucherimptplan.md](./xkoac_voucherimptplan.md) |
| 58 | `t_xkoac_vchplanentry_l` | 数据来源-多语言表 | 7 | [xkoac_voucherimptplan.md](./xkoac_voucherimptplan.md) |
| 59 | `t_xkoac_vchplanglbook` | 来源总账账簿-多选基础资料表 | 3 | [xkoac_voucherimptplan.md](./xkoac_voucherimptplan.md) |
| 60 | `t_xkoac_vchplanunit` | 适用经营单元-多选基础资料表 | 3 | [xkoac_voucherimptplan.md](./xkoac_voucherimptplan.md) |
| 61 | `t_xkoac_vchsubentry` | 分录设置-子表 | 39 | [xkoac_voucherimptplan.md](./xkoac_voucherimptplan.md) |
| 62 | `t_xkoac_vchsubentry_l` | 分录设置-多语言表 | 14 | [xkoac_voucherimptplan.md](./xkoac_voucherimptplan.md) |
| 63 | `t_xkoac_voucher` | 经营流水账-主表 | 30 | [xkoac_voucher.md](./xkoac_voucher.md) |
| 64 | `t_xkoac_voucherentry` | 单据体-子表 | 17 | [xkoac_voucher.md](./xkoac_voucher.md) |
| 65 | `t_xkoac_voucherentry_l` | 单据体-多语言表 | 4 | [xkoac_voucher.md](./xkoac_voucher.md) |
| 66 | `t_xkoac_voucherplan` | 生成经营流水账方案-主表 | 7 | [xkoac_voucherplan.md](./xkoac_voucherplan.md) |
| 67 | `t_xkoac_voucherplan_l` | 生成经营流水账方案-多语言表 | 4 | [xkoac_voucherplan.md](./xkoac_voucherplan.md) |
| 68 | `t_xkoac_voucherplanentity` | 单据体-子表 | 5 | [xkoac_voucherplan.md](./xkoac_voucherplan.md) |
| 69 | `t_xkoac_voucherplansub` | 子单据体-子表 | 5 | [xkoac_voucherplan.md](./xkoac_voucherplan.md) |
| 70 | `t_xkoac_vouchplanunit` | 多选经营单元-多选基础资料表 | 3 | [xkoac_voucherplan.md](./xkoac_voucherplan.md) |
