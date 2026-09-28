# ds 模块表清单

> 本模块共收录 **82** 张表定义，来自 `ds_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category ds
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_ds_account` | 会计科目-主表 | 8 | [ds_account.md](./ds_account.md) |
| 2 | `t_ds_accountbalance_1f` | 科目余额(包含未过账原币)-主表 | 42 | [ds_accountbalance_1f.md](./ds_accountbalance_1f.md) |
| 3 | `t_ds_accountbalance_1l` | 科目余额(包含未过账本位币)-主表 | 42 | [ds_accountbalance_1l.md](./ds_accountbalance_1l.md) |
| 4 | `t_ds_accountbalance_1r` | 科目余额(包含未过账报告币)-主表 | 42 | [ds_accountbalance_1r.md](./ds_accountbalance_1r.md) |
| 5 | `t_ds_accountbalance_5f` | 科目余额(过账原币)-主表 | 42 | [ds_accountbalance_5f.md](./ds_accountbalance_5f.md) |
| 6 | `t_ds_accountbalance_5l` | 科目余额(过账本位币)-主表 | 42 | [ds_accountbalance_5l.md](./ds_accountbalance_5l.md) |
| 7 | `t_ds_accountbalance_5r` | 科目余额(过账报告币)-主表 | 42 | [ds_accountbalance_5r.md](./ds_accountbalance_5r.md) |
| 8 | `t_ds_accountbanks` | 银行账户-主表 | 5 | [ds_accountbanks.md](./ds_accountbanks.md) |
| 9 | `t_ds_accounttable` | 科目表-主表 | 5 | [ds_accounttable.md](./ds_accounttable.md) |
| 10 | `t_ds_api2ierp_org` | 行政组织-主表 | 27 | [isc_api2ierp_org.md](./isc_api2ierp_org.md) |
| 11 | `t_ds_api2ierp_user` | 人员-主表 | 30 | [isc_api2ierp_user.md](./isc_api2ierp_user.md) |
| 12 | `t_ds_assistantdetail` | 辅助账竖表-主表 | 0 | [ds_assistantdetail.md](./ds_assistantdetail.md) |
| 13 | `t_ds_assistanthg` | 辅助帐横表-主表 | 0 | [ds_assistanthg.md](./ds_assistanthg.md) |
| 14 | `t_ds_assistbalance_1f` | 辅助账余额(包含未过账原币)-主表 | 44 | [ds_assistbalance_1f.md](./ds_assistbalance_1f.md) |
| 15 | `t_ds_assistbalance_1l` | 辅助账余额(包含未过账本位币)-主表 | 44 | [ds_assistbalance_1l.md](./ds_assistbalance_1l.md) |
| 16 | `t_ds_assistbalance_1r` | 辅助账余额(包含未过账报告币)-主表 | 44 | [ds_assistbalance_1r.md](./ds_assistbalance_1r.md) |
| 17 | `t_ds_assistbalance_5f` | 辅助账余额(过账原币)-主表 | 44 | [ds_assistbalance_5f.md](./ds_assistbalance_5f.md) |
| 18 | `t_ds_assistbalance_5l` | 辅助账余额(过账本位币)-主表 | 44 | [ds_assistbalance_5l.md](./ds_assistbalance_5l.md) |
| 19 | `t_ds_assistbalance_5r` | 辅助账余额(过账报告币)-主表 | 44 | [ds_assistbalance_5r.md](./ds_assistbalance_5r.md) |
| 20 | `t_ds_asstaccount` | 辅助账类型-主表 | 0 | [ds_asstaccount.md](./ds_asstaccount.md) |
| 21 | `t_ds_asstact` | 自定义核算项目-主表 | 7 | [ds_asstact.md](./ds_asstact.md) |
| 22 | `t_ds_asstactgroup` | 自定义核算项目类型-主表 | 5 | [ds_asstactgroup.md](./ds_asstactgroup.md) |
| 23 | `t_ds_asstacttype` | 核算项目类型-主表 | 6 | [ds_asstacttype.md](./ds_asstacttype.md) |
| 24 | `t_ds_bank` | 金融机构-主表 | 5 | [ds_bank.md](./ds_bank.md) |
| 25 | `t_ds_bgitem` | 预算项目-主表 | 0 | [ds_bgitem.md](./ds_bgitem.md) |
| 26 | `t_ds_cashflowitem` | 现金流量项目-主表 | 5 | [ds_cashflowitem.md](./ds_cashflowitem.md) |
| 27 | `t_ds_changetype` | 变动类型-主表 | 7 | [ds_changetype.md](./ds_changetype.md) |
| 28 | `t_ds_city` | 城市-主表 | 5 | [ds_city.md](./ds_city.md) |
| 29 | `t_ds_company` | 财务组织-主表 | 5 | [ds_company.md](./ds_company.md) |
| 30 | `t_ds_costcenter` | 成本中心-主表 | 5 | [ds_costcenter.md](./ds_costcenter.md) |
| 31 | `t_ds_costitem` | 聚合收款账户-主表 | 5 | [ds_costitem.md](./ds_costitem.md) |
| 32 | `t_ds_costobject` | 成本对象-主表 | 5 | [ds_costobject.md](./ds_costobject.md) |
| 33 | `t_ds_country` | 国家或地区-主表 | 5 | [ds_country.md](./ds_country.md) |
| 34 | `t_ds_currency` | 币种-主表 | 5 | [ds_currency.md](./ds_currency.md) |
| 35 | `t_ds_customer` | 客户-主表 | 5 | [ds_customer.md](./ds_customer.md) |
| 36 | `t_ds_dataelement` | 报表取数类型-主表 | 5 | [ds_dataelement.md](./ds_dataelement.md) |
| 37 | `t_ds_dep_org` | 星空组织部门结构-主表 | 20 | [ds_dep_org.md](./ds_dep_org.md) |
| 38 | `t_ds_ebs_kd_org` | ebs_kd_组织-主表 | 0 | [ds_ebs_kd_org.md](./ds_ebs_kd_org.md) |
| 39 | `t_ds_ebs_legal_entity` | 法人实体中间表-主表 | 0 | [ds_ebs_legal_entity.md](./ds_ebs_legal_entity.md) |
| 40 | `t_ds_ebs_org` | 业务实体中间表-主表 | 0 | [ds_ebs_org.md](./ds_ebs_org.md) |
| 41 | `t_ds_ebs_org_storage` | 库存组织中间表-主表 | 0 | [ds_ebs_org_storage.md](./ds_ebs_org_storage.md) |
| 42 | `t_ds_entry_dpt` | 单据体-子表 | 0 | [ds_user.md](./ds_user.md) |
| 43 | `t_ds_fiscalperiod` | 期间-主表 | 5 | [ds_fiscalperiod.md](./ds_fiscalperiod.md) |
| 44 | `t_ds_fiscalyear` | 财年-主表 | 5 | [ds_fiscalyear.md](./ds_fiscalyear.md) |
| 45 | `t_ds_fiscialperiod` | 期间-主表 | 0 | [ds_fiscialperiod.md](./ds_fiscialperiod.md) |
| 46 | `t_ds_fiscialyear` | 财年-主表 | 0 | [ds_fiscialyear.md](./ds_fiscialyear.md) |
| 47 | `t_ds_glsyn_voucher` | 凭证中间表-主表 | 0 | [gl_syn_voucher.md](./gl_syn_voucher.md) |
| 48 | `t_ds_glsyn_voucher` | 凭证头中间表-主表 | 0 | [gl_syn_voucherheader.md](./gl_syn_voucherheader.md) |
| 49 | `t_ds_glsyn_voucherentry` | 单据体-子表 | 0 | [gl_syn_voucher.md](./gl_syn_voucher.md) |
| 50 | `t_ds_glsyn_voucherentry` | 凭证行中间表-主表 | 0 | [gl_syn_voucherentry.md](./gl_syn_voucherentry.md) |
| 51 | `t_ds_idaas_id_map` | 苍穹与玉符人员ID映射-主表 | 3 | [ds_idaas_id_map.md](./ds_idaas_id_map.md) |
| 52 | `t_ds_ierp_out_orgid_map` | 苍穹与外部组织ID映射-主表 | 6 | [ds_ierp_out_orgid_map.md](./ds_ierp_out_orgid_map.md) |
| 53 | `t_ds_industry` | 行业-主表 | 5 | [ds_industry.md](./ds_industry.md) |
| 54 | `t_ds_inneraccount` | 内部账户-主表 | 5 | [ds_inneraccount.md](./ds_inneraccount.md) |
| 55 | `t_ds_material` | 物料-主表 | 5 | [ds_material.md](./ds_material.md) |
| 56 | `t_ds_mergereport` | 合并报表-主表 | 3 | [ds_mergereport.md](./ds_mergereport.md) |
| 57 | `t_ds_org` | 组织中间表-主表 | 0 | [ds_org.md](./ds_org.md) |
| 58 | `t_ds_org_l` | 组织中间表-多语言表 | 0 | [ds_org.md](./ds_org.md) |
| 59 | `t_ds_orgunit` | 组织单元-主表 | 6 | [ds_orgunit.md](./ds_orgunit.md) |
| 60 | `t_ds_period` | 会计期间-主表 | 8 | [ds_period.md](./ds_period.md) |
| 61 | `t_ds_person` | 职员-主表 | 5 | [ds_person.md](./ds_person.md) |
| 62 | `t_ds_position` | 岗位信息-主表 | 5 | [ds_position.md](./ds_position.md) |
| 63 | `t_ds_project` | 项目-主表 | 5 | [ds_project.md](./ds_project.md) |
| 64 | `t_ds_province` | 省份-主表 | 5 | [ds_province.md](./ds_province.md) |
| 65 | `t_ds_reportdata` | 合并报表中间表-主表 | 0 | [ds_reportdata.md](./ds_reportdata.md) |
| 66 | `t_ds_reportdata_eas` | 集成EAS合并报表中间表-主表 | 0 | [ds_reportdata_eas.md](./ds_reportdata_eas.md) |
| 67 | `t_ds_reportperiod` | 报表周期-主表 | 5 | [ds_reportperiod.md](./ds_reportperiod.md) |
| 68 | `t_ds_reporttype` | 报表类型-主表 | 5 | [ds_reporttype.md](./ds_reporttype.md) |
| 69 | `t_ds_rptitem` | 报表项目-主表 | 5 | [ds_rptitem.md](./ds_rptitem.md) |
| 70 | `t_ds_srcsys` | 来源系统-主表 | 15 | [ds_srcsys.md](./ds_srcsys.md) |
| 71 | `t_ds_srcsys_l` | 来源系统-多语言表 | 4 | [ds_srcsys.md](./ds_srcsys.md) |
| 72 | `t_ds_srcsystype` | 来源系统类型-主表 | 10 | [ds_srcsystype.md](./ds_srcsystype.md) |
| 73 | `t_ds_srcsystype_l` | 来源系统类型-多语言表 | 4 | [ds_srcsystype.md](./ds_srcsystype.md) |
| 74 | `t_ds_supplier` | 供应商-主表 | 5 | [ds_supplier.md](./ds_supplier.md) |
| 75 | `t_ds_unit_test_bill` | 单元测试类处理单据-主表 | 0 | [ds_unit_test_bill.md](./ds_unit_test_bill.md) |
| 76 | `t_ds_user` | 人员中间表-主表 | 0 | [ds_user.md](./ds_user.md) |
| 77 | `t_ds_user_l` | 人员中间表-多语言表 | 0 | [ds_user.md](./ds_user.md) |
| 78 | `t_ds_xk_dep` | 星空部门中间表-主表 | 17 | [ds_xk_dep.md](./ds_xk_dep.md) |
| 79 | `t_ds_xk_org` | 星空组织中间表-主表 | 13 | [ds_xk_org.md](./ds_xk_org.md) |
| 80 | `t_ds_xk_person` | 用户信息-主表 | 5 | [ds_xk_person.md](./ds_xk_person.md) |
| 81 | `t_ds_xk_taxrate` | 税率信息-主表 | 6 | [ds_taxrate.md](./ds_taxrate.md) |
| 82 | `t_ds_yzj_id_mapping` | 云之家组织ID映射表-主表 | 6 | [ds_yzj_id_mapping.md](./ds_yzj_id_mapping.md) |
