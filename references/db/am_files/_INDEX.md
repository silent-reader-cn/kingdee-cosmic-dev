# am 模块表清单

> 本模块共收录 **71** 张表定义，来自 `am_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category am
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_am_accopenbill` | 开户申请-主表 | 59 | [am_accopenbill.md](./am_accopenbill.md) |
| 2 | `t_am_accopenbill_l` | 开户申请-多语言表 | 11 | [am_accopenbill.md](./am_accopenbill.md) |
| 3 | `t_am_accopenbill_lk` | 关联子实体-子表 | 6 | [am_accopenbill.md](./am_accopenbill.md) |
| 4 | `t_am_accopenbill_tc` | 开户申请-关联追踪表 | 7 | [am_accopenbill.md](./am_accopenbill.md) |
| 5 | `t_am_accopenbill_wb` | 开户申请-反写记录表 | 10 | [am_accopenbill.md](./am_accopenbill.md) |
| 6 | `t_am_acctclosebill` | 销户申请-主表 | 31 | [am_acctclosebill.md](./am_acctclosebill.md) |
| 7 | `t_am_acctclosebill_l` | 销户申请-多语言表 | 6 | [am_acctclosebill.md](./am_acctclosebill.md) |
| 8 | `t_am_acctopenbill_cur` | 币别-多选基础资料表 | 3 | [am_accopenbill.md](./am_accopenbill.md) |
| 9 | `t_am_associatebill` | 单据信息-主表 | 7 | [am_billinfolist.md](./am_billinfolist.md) |
| 10 | `t_am_associateentry` | 单据体-子表 | 8 | [am_businessapply.md](./am_businessapply.md) |
| 11 | `t_am_associateentry_lk` | 关联子实体-子表 | 7 | [am_businessapply.md](./am_businessapply.md) |
| 12 | `t_am_associateentry_lk` | 关联子实体-子表 | 7 | [am_holdgoodsinfos.md](./am_holdgoodsinfos.md) |
| 13 | `t_am_bankfunclist` | 单据体-子表 | 8 | [am_acctbank_schedule.md](./am_acctbank_schedule.md) |
| 14 | `t_am_businessapply` | 实物新增申请-主表 | 17 | [am_businessapply.md](./am_businessapply.md) |
| 15 | `t_am_businessapply_l` | 实物新增申请-多语言表 | 4 | [am_businessapply.md](./am_businessapply.md) |
| 16 | `t_am_businessapply_lk` | 关联子实体-子表 | 7 | [am_businessapply.md](./am_businessapply.md) |
| 17 | `t_am_businessapply_lk` | 关联子实体-子表 | 7 | [am_holdgoodsinfos.md](./am_holdgoodsinfos.md) |
| 18 | `t_am_businessapply_tc` | 实物新增申请-关联追踪表 | 7 | [am_businessapply.md](./am_businessapply.md) |
| 19 | `t_am_businessapply_wb` | 实物新增申请-反写记录表 | 10 | [am_businessapply.md](./am_businessapply.md) |
| 20 | `t_am_changeapply` | 变更申请-主表 | 13 | [am_changeapply.md](./am_changeapply.md) |
| 21 | `t_am_changeapply_config` | 变更申请配置-主表 | 12 | [am_changeapply_config.md](./am_changeapply_config.md) |
| 22 | `t_am_changeapply_cur` | 币别-多选基础资料表 | 3 | [am_changeapply.md](./am_changeapply.md) |
| 23 | `t_am_changeapply_entry` | 单据体-子表 | 12 | [am_changeapply.md](./am_changeapply.md) |
| 24 | `t_am_changeapply_entry2` | 单据体-子表 | 5 | [am_changeapply.md](./am_changeapply.md) |
| 25 | `t_am_changeapply_l` | 变更申请-多语言表 | 5 | [am_changeapply.md](./am_changeapply.md) |
| 26 | `t_am_changeapply_st` | 限定结算方式-多选基础资料表 | 3 | [am_changeapply.md](./am_changeapply.md) |
| 27 | `t_am_collectinfos` | 关联信息-子表 | 8 | [am_holdgoodsinfos.md](./am_holdgoodsinfos.md) |
| 28 | `t_am_goodsattach` | 附件-附件表 | 3 | [am_holdgoodsinfos.md](./am_holdgoodsinfos.md) |
| 29 | `t_am_goodsdetail` | 详细信息-子表 | 13 | [am_holdgoodsinfos.md](./am_holdgoodsinfos.md) |
| 30 | `t_am_goodsuse_change` | 变更信息-子表 | 14 | [am_holdgoods_use.md](./am_holdgoods_use.md) |
| 31 | `t_am_goodsuse_e` | 关联信息列表-子表 | 5 | [am_holdgoods_use.md](./am_holdgoods_use.md) |
| 32 | `t_am_goodsuse_sub` | 关联信息列表-子表 | 6 | [am_holdgoods_use.md](./am_holdgoods_use.md) |
| 33 | `t_am_holdgoods_use` | 实物业务处理-主表 | 18 | [am_holdgoods_use.md](./am_holdgoods_use.md) |
| 34 | `t_am_holdgoods_use_l` | 实物业务处理-多语言表 | 5 | [am_holdgoods_use.md](./am_holdgoods_use.md) |
| 35 | `t_am_holdgoodsinfo` | 实物新增-主表 | 12 | [am_holdgoodsinfos.md](./am_holdgoodsinfos.md) |
| 36 | `t_am_holdgoodsinfo_lk` | 关联子实体-子表 | 6 | [am_holdgoodsinfos.md](./am_holdgoodsinfos.md) |
| 37 | `t_am_holdgoodsinfo_tc` | 实物新增-关联追踪表 | 7 | [am_holdgoodsinfos.md](./am_holdgoodsinfos.md) |
| 38 | `t_am_holdgoodsinfo_wb` | 实物新增-反写记录表 | 10 | [am_holdgoodsinfos.md](./am_holdgoodsinfos.md) |
| 39 | `t_am_inventorygood` | 库存实物管理-主表 | 22 | [am_inventorygoodmanager.md](./am_inventorygoodmanager.md) |
| 40 | `t_am_inventorygood_att` | 附件-附件表 | 3 | [am_inventorygoodmanager.md](./am_inventorygoodmanager.md) |
| 41 | `t_am_inventorygood_l` | 库存实物管理-多语言表 | 4 | [am_inventorygoodmanager.md](./am_inventorygoodmanager.md) |
| 42 | `t_am_inventorygoode` | 关联信息-子表 | 6 | [am_inventorygoodmanager.md](./am_inventorygoodmanager.md) |
| 43 | `t_am_linkpayrelation` | 联动支付关系-主表 | 17 | [am_linkpayrelation.md](./am_linkpayrelation.md) |
| 44 | `t_am_linkpayrelation_l` | 联动支付关系-多语言表 | 5 | [am_linkpayrelation.md](./am_linkpayrelation.md) |
| 45 | `t_am_objecttype` | 实物类型设置-主表 | 15 | [am_objecttype.md](./am_objecttype.md) |
| 46 | `t_am_objecttype_l` | 实物类型设置-多语言表 | 5 | [am_objecttype.md](./am_objecttype.md) |
| 47 | `t_am_payrelationinfo` | 支付关系信息-子表 | 12 | [am_linkpayrelation.md](./am_linkpayrelation.md) |
| 48 | `t_am_postgoodsupdate_att` | 附件-附件表 | 3 | [am_holdgoods_update.md](./am_holdgoods_update.md) |
| 49 | `t_am_postgoodsupdate_sub` | 变更后关联信息-子表 | 5 | [am_holdgoods_update.md](./am_holdgoods_update.md) |
| 50 | `t_am_postgoodsupdates` | 实物变动清单-主表 | 39 | [am_holdgoods_update.md](./am_holdgoods_update.md) |
| 51 | `t_am_postgoodsupdates_l` | 实物变动清单-多语言表 | 4 | [am_holdgoods_update.md](./am_holdgoods_update.md) |
| 52 | `t_am_pregoodsupdate` | 实物信息列表-子表 | 4 | [am_holdgoods_update.md](./am_holdgoods_update.md) |
| 53 | `t_am_pregoodsupdate_att` | 附件-附件表 | 3 | [am_holdgoods_update.md](./am_holdgoods_update.md) |
| 54 | `t_am_pregoodsupdate_sub` | 关联信息列表-子表 | 5 | [am_holdgoods_update.md](./am_holdgoods_update.md) |
| 55 | `t_am_restrictedfundsmanag` | 受限资金管理-主表 | 27 | [am_restrictedfundsmanager.md](./am_restrictedfundsmanager.md) |
| 56 | `t_am_restrictedfundsmanag_lk` | 关联子实体-子表 | 6 | [am_restrictedfundsmanager.md](./am_restrictedfundsmanager.md) |
| 57 | `t_am_restrictedfundsmanag_tc` | 受限资金管理-关联追踪表 | 7 | [am_restrictedfundsmanager.md](./am_restrictedfundsmanager.md) |
| 58 | `t_am_restrictedfundsmanag_wb` | 受限资金管理-反写记录表 | 10 | [am_restrictedfundsmanager.md](./am_restrictedfundsmanager.md) |
| 59 | `t_am_restrictedfundstype` | 受限资金类型-主表 | 15 | [am_restrictedfundstype.md](./am_restrictedfundstype.md) |
| 60 | `t_am_restrictedfundstype_l` | 受限资金类型-多语言表 | 5 | [am_restrictedfundstype.md](./am_restrictedfundstype.md) |
| 61 | `t_am_strategy` | 账户管理策略-主表 | 36 | [am_strategy.md](./am_strategy.md) |
| 62 | `t_am_strategy_l` | 账户管理策略-多语言表 | 5 | [am_strategy.md](./am_strategy.md) |
| 63 | `t_bd_accountbanks` | 银行账户调度-主表 | 59 | [am_acctbank_schedule.md](./am_acctbank_schedule.md) |
| 64 | `t_bd_accountbanks_a` | 银行账户调度-分表 | 4 | [am_acctbank_schedule.md](./am_acctbank_schedule.md) |
| 65 | `t_bd_accountbanks_cur` | 币别范围-多选基础资料表 | 3 | [am_acctbank_schedule.md](./am_acctbank_schedule.md) |
| 66 | `t_bd_accountbanks_l` | 银行账户调度-多语言表 | 10 | [am_acctbank_schedule.md](./am_acctbank_schedule.md) |
| 67 | `t_bd_accountbanks_lk` | 关联子实体-子表 | 6 | [am_acctbank_schedule.md](./am_acctbank_schedule.md) |
| 68 | `t_bd_accountbanks_m` | 银行账户调度-使用范围位图表 | 2 | [am_acctbank_schedule.md](./am_acctbank_schedule.md) |
| 69 | `t_bd_accountbanks_nb` | 网银子账户-多选基础资料表 | 3 | [am_acctbank_schedule.md](./am_acctbank_schedule.md) |
| 70 | `t_bd_accountbanks_st` | 限定结算方式-多选基础资料表 | 3 | [am_acctbank_schedule.md](./am_acctbank_schedule.md) |
| 71 | `t_bd_accountbanks_u` | 银行账户调度-使用范围表 | 3 | [am_acctbank_schedule.md](./am_acctbank_schedule.md) |
