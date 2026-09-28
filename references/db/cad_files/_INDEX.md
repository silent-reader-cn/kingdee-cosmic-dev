# cad 模块表清单

> 本模块共收录 **84** 张表定义，来自 `cad_files/`。

> 索引由 `scripts/build_index.py` 从 Markdown 自动生成，请勿手工编辑。
> 检索本模块表结构请用统一检索脚本（比翻本文件更快）：
> ```bash
> python scripts/search.py <关键词> --scope db --category cad
> ```

| 序号 | 数据库表名 | 中文名称 | 字段数 | 详细定义文件 |
| :---: | :--- | :--- | :---: | :--- |
| 1 | `t_bd_matcostinfo` | 物料成本信息-主表 | 36 | [cad_matcostinfo.md](./cad_matcostinfo.md) |
| 2 | `t_bd_matcostinfo_l` | 物料成本信息-多语言表 | 4 | [cad_matcostinfo.md](./cad_matcostinfo.md) |
| 3 | `t_bd_matcostinfoentry` | 单据体-子表 | 7 | [cad_matcostinfo.md](./cad_matcostinfo.md) |
| 4 | `t_cad_autoexecruleentry` | 单据体-子表 | 8 | [cad_autoexecrulesetting.md](./cad_autoexecrulesetting.md) |
| 5 | `t_cad_autoexecrulesetting` | 自动执行规则设置-主表 | 9 | [cad_autoexecrulesetting.md](./cad_autoexecrulesetting.md) |
| 6 | `t_cad_autoexecrulesetting_l` | 自动执行规则设置-多语言表 | 4 | [cad_autoexecrulesetting.md](./cad_autoexecrulesetting.md) |
| 7 | `t_cad_bomsetting` | 成本BOM设置（废弃）-主表 | 37 | [cad_bomsetting.md](./cad_bomsetting.md) |
| 8 | `t_cad_bomsetting_l` | 成本BOM设置（废弃）-多语言表 | 4 | [cad_bomsetting.md](./cad_bomsetting.md) |
| 9 | `t_cad_calccheckdtresult` | 合法性检查结果明细-子表 | 7 | [cad_calccheckresult.md](./cad_calccheckresult.md) |
| 10 | `t_cad_calccheckiteminfos` | 标准成本卷算合法性检查项信息表-主表 | 6 | [cad_calccheckiteminfos.md](./cad_calccheckiteminfos.md) |
| 11 | `t_cad_calccheckiteminfos_l` | 标准成本卷算合法性检查项信息表-多语言表 | 6 | [cad_calccheckiteminfos.md](./cad_calccheckiteminfos.md) |
| 12 | `t_cad_calccheckresult` | 卷算合法性检查结果明细-主表 | 9 | [cad_calccheckresult.md](./cad_calccheckresult.md) |
| 13 | `t_cad_calccheckresult_l` | 卷算合法性检查结果明细-多语言表 | 4 | [cad_calccheckresult.md](./cad_calccheckresult.md) |
| 14 | `t_cad_calcdimension` | 成本卷算维度-主表 | 12 | [cad_calcdimension.md](./cad_calcdimension.md) |
| 15 | `t_cad_calcdimension_l` | 成本卷算维度-多语言表 | 4 | [cad_calcdimension.md](./cad_calcdimension.md) |
| 16 | `t_cad_calcdimensionentry` | 单据体-子表 | 5 | [cad_calcdimension.md](./cad_calcdimension.md) |
| 17 | `t_cad_calceffectiveresult` | 生效卷算结果表-主表 | 32 | [cad_calceffectiveresult.md](./cad_calceffectiveresult.md) |
| 18 | `t_cad_calceffectrsentry` | 单据体-子表 | 22 | [cad_calceffectiveresult.md](./cad_calceffectiveresult.md) |
| 19 | `t_cad_calchangerecord` | 卷算变更记录-主表 | 17 | [cad_calchangerecord.md](./cad_calchangerecord.md) |
| 20 | `t_cad_calcparameter` | 标准成本卷算参数-主表 | 13 | [cad_calcparameter.md](./cad_calcparameter.md) |
| 21 | `t_cad_calcparammat` | 单据体-子表 | 6 | [cad_calcparameter.md](./cad_calcparameter.md) |
| 22 | `t_cad_calcparammatgroup` | 单据体-子表 | 4 | [cad_calcparameter.md](./cad_calcparameter.md) |
| 23 | `t_cad_calcsimtreeentry` | 单据体-子表 | 7 | [cad_calcsimulationresult.md](./cad_calcsimulationresult.md) |
| 24 | `t_cad_calcsimulars` | 模拟卷算结果表-主表 | 25 | [cad_calcsimulationresult.md](./cad_calcsimulationresult.md) |
| 25 | `t_cad_calcsimularsentry` | 单据体-子表 | 22 | [cad_calcsimulationresult.md](./cad_calcsimulationresult.md) |
| 26 | `t_cad_calcsuccessrecord` | 标准成本卷算物料展开记录-主表 | 3 | [cad_calcmatexpandrecord.md](./cad_calcmatexpandrecord.md) |
| 27 | `t_cad_calctaskrecord` | 卷算报告-主表 | 14 | [cad_calctaskrecord.md](./cad_calctaskrecord.md) |
| 28 | `t_cad_calctaskrecord_l` | 卷算报告-多语言表 | 3 | [cad_calctaskrecord.md](./cad_calctaskrecord.md) |
| 29 | `t_cad_calprocessroutecost` | 工艺路线成本计算临时存储表-主表 | 12 | [cad_calprocessroutecost.md](./cad_calprocessroutecost.md) |
| 30 | `t_cad_costobjectaccount` | 成本核算对象与成本主体-主表 | 6 | [cad_costobjectaccount.md](./cad_costobjectaccount.md) |
| 31 | `t_cad_costrenewaldif` | 生产成本更新差异单-主表 | 17 | [cad_costrenewaldif.md](./cad_costrenewaldif.md) |
| 32 | `t_cad_costupdatebill` | 成本更新记录单-主表 | 26 | [cad_costupdatebill.md](./cad_costupdatebill.md) |
| 33 | `t_cad_costupdatematerials` | 单据体-子表 | 7 | [cad_costupdatenew.md](./cad_costupdatenew.md) |
| 34 | `t_cad_costupdatenew` | 更新申请单-主表 | 26 | [cad_costupdatenew.md](./cad_costupdatenew.md) |
| 35 | `t_cad_costupdatenew` | 更新申请单F7-主表 | 26 | [cad_costupdatenewf7.md](./cad_costupdatenewf7.md) |
| 36 | `t_cad_costupestbish` | 更新确认单-主表 | 9 | [cad_costupdateestablished.md](./cad_costupdateestablished.md) |
| 37 | `t_cad_costupestbish` | 更新确认单F7-主表 | 9 | [cad_costupdateestshf7.md](./cad_costupdateestshf7.md) |
| 38 | `t_cad_costupestbish_acct` | 库存成本单账簿单据体-子表 | 17 | [cad_costupdateestablished.md](./cad_costupdateestablished.md) |
| 39 | `t_cad_costupestbish_cost` | 成本更新-子表 | 16 | [cad_costupdateestablished.md](./cad_costupdateestablished.md) |
| 40 | `t_cad_costupestbish_l` | 更新确认单F7-多语言表 | 0 | [cad_costupdateestshf7.md](./cad_costupdateestshf7.md) |
| 41 | `t_cad_costupestbish_prod` | 生产成本单据体-子表 | 19 | [cad_costupdateestablished.md](./cad_costupdateestablished.md) |
| 42 | `t_cad_costupestbish_stor` | 库存成本单据体-子表 | 18 | [cad_costupdateestablished.md](./cad_costupdateestablished.md) |
| 43 | `t_cad_difdtlentry` | 单据体-子表 | 13 | [cad_costrenewaldif.md](./cad_costrenewaldif.md) |
| 44 | `t_cad_keycol` | 卷算维度数据表-主表 | 10 | [cad_keycol.md](./cad_keycol.md) |
| 45 | `t_cad_matcalcseting` | 物料卷算维度设置-主表 | 12 | [cad_matcalcseting.md](./cad_matcalcseting.md) |
| 46 | `t_cad_matcalcseting_l` | 物料卷算维度设置-多语言表 | 4 | [cad_matcalcseting.md](./cad_matcalcseting.md) |
| 47 | `t_cad_matcalcsetingentry` | 单据体-子表 | 6 | [cad_matcalcseting.md](./cad_matcalcseting.md) |
| 48 | `t_cad_outprocessesprice` | 工序委外加工价目表-主表 | 13 | [cad_outprocessesprice.md](./cad_outprocessesprice.md) |
| 49 | `t_cad_outprocessesprice_l` | 工序委外加工价目表-多语言表 | 4 | [cad_outprocessesprice.md](./cad_outprocessesprice.md) |
| 50 | `t_cad_outsourceprice` | 产品委外标准价目表-主表 | 28 | [cad_outsourceprice.md](./cad_outsourceprice.md) |
| 51 | `t_cad_outsourceprice_l` | 产品委外标准价目表-多语言表 | 4 | [cad_outsourceprice.md](./cad_outsourceprice.md) |
| 52 | `t_cad_outsourcepriceentry` | 附加费用-子表 | 6 | [cad_outsourceprice.md](./cad_outsourceprice.md) |
| 53 | `t_cad_price_billtypecon` | 单据类型-多选基础资料表 | 3 | [cad_purpricingrule.md](./cad_purpricingrule.md) |
| 54 | `t_cad_price_billtypeorder` | 单据类型-多选基础资料表 | 3 | [cad_purpricingrule.md](./cad_purpricingrule.md) |
| 55 | `t_cad_price_purorgcon` | 采购组织-多选基础资料表 | 3 | [cad_purpricingrule.md](./cad_purpricingrule.md) |
| 56 | `t_cad_price_purorgorder` | 采购组织-多选基础资料表 | 3 | [cad_purpricingrule.md](./cad_purpricingrule.md) |
| 57 | `t_cad_purpricedatasrc` | 取价来源数据-主表 | 13 | [cad_purpricedatasrcnew.md](./cad_purpricedatasrcnew.md) |
| 58 | `t_cad_purprices` | 外购物料标准价目表(废弃)-主表 | 28 | [cad_purprices.md](./cad_purprices.md) |
| 59 | `t_cad_purprices_l` | 外购物料标准价目表(废弃)-多语言表 | 4 | [cad_purprices.md](./cad_purprices.md) |
| 60 | `t_cad_purpricesentry` | 物料对应成本子要素信息-子表 | 7 | [cad_purprices.md](./cad_purprices.md) |
| 61 | `t_cad_purpricingrule` | 采购取价规则-主表 | 15 | [cad_purpricingrule.md](./cad_purpricingrule.md) |
| 62 | `t_cad_purpricingruleres` | 采购取价规则(资源)-主表 | 13 | [cad_purpricingrule_res.md](./cad_purpricingrule_res.md) |
| 63 | `t_cad_refreshbomrecord` | 刷新bom操作记录-主表 | 6 | [cad_refreshbomrecord.md](./cad_refreshbomrecord.md) |
| 64 | `t_cad_res_billtypeorder` | 单据类型-多选基础资料表 | 3 | [cad_purpricingrule_res.md](./cad_purpricingrule_res.md) |
| 65 | `t_cad_res_purorg` | 采购组织-多选基础资料表 | 3 | [cad_purpricingrule_res.md](./cad_purpricingrule_res.md) |
| 66 | `t_cad_resourcerate` | 资源标准费用价目表-主表 | 28 | [cad_resourcerate.md](./cad_resourcerate.md) |
| 67 | `t_cad_resourcerate_l` | 资源标准费用价目表-多语言表 | 4 | [cad_resourcerate.md](./cad_resourcerate.md) |
| 68 | `t_cad_resourcerateentry` | 附加制造费用-子表 | 7 | [cad_resourcerate.md](./cad_resourcerate.md) |
| 69 | `t_cad_routersetting` | 成本工艺路线设置-主表 | 20 | [cad_routersetting.md](./cad_routersetting.md) |
| 70 | `t_cad_routersetting_entry` | 物料单据体-子表 | 11 | [cad_routersetting.md](./cad_routersetting.md) |
| 71 | `t_cad_routersetting_l` | 成本工艺路线设置-多语言表 | 4 | [cad_routersetting.md](./cad_routersetting.md) |
| 72 | `t_cad_stdcalbatchsizepara` | 标准成本卷算批次计算参数-主表 | 2 | [cad_stdcalbatchsizeparam.md](./cad_stdcalbatchsizeparam.md) |
| 73 | `t_cad_stdcalcmatfiltersv` | 物料主数据信息归档-主表 | 5 | [cad_stdcalcmatfiltersava.md](./cad_stdcalcmatfiltersava.md) |
| 74 | `t_cad_stdratesetting` | 物料费用附加率设置-主表 | 2 | [cad_stdratesetting.md](./cad_stdratesetting.md) |
| 75 | `t_cad_stdratesettingentry` | 单据体-子表 | 6 | [cad_stdratesetting.md](./cad_stdratesetting.md) |
| 76 | `t_cad_syncbom_log` | 成本BOM同步日志-主表 | 5 | [cad_syncbom_log.md](./cad_syncbom_log.md) |
| 77 | `t_cad_syncbom_rule` | 成本BOM同步规则-主表 | 13 | [cad_syncbom_rule.md](./cad_syncbom_rule.md) |
| 78 | `t_cad_syncbom_rule_l` | 成本BOM同步规则-多语言表 | 4 | [cad_syncbom_rule.md](./cad_syncbom_rule.md) |
| 79 | `t_cad_syncrouter_log` | 成本工艺路线同步日志-主表 | 5 | [cad_syncrouter_log.md](./cad_syncrouter_log.md) |
| 80 | `t_cad_syncrouter_rule` | 成本工艺路线同步规则-主表 | 11 | [cad_syncrouter_rule.md](./cad_syncrouter_rule.md) |
| 81 | `t_cad_syncrouter_rule_l` | 成本工艺路线同步规则-多语言表 | 4 | [cad_syncrouter_rule.md](./cad_syncrouter_rule.md) |
| 82 | `t_cad_taskexecutelog` | 任务执行日志-主表 | 16 | [cad_taskexecutelog.md](./cad_taskexecutelog.md) |
| 83 | `t_cad_taskexecutelog_l` | 任务执行日志-多语言表 | 4 | [cad_taskexecutelog.md](./cad_taskexecutelog.md) |
| 84 | `t_cad_userdatarecord` | 用户数据记录-主表 | 11 | [cad_userdatarecord.md](./cad_userdatarecord.md) |
