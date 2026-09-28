# 应付结算清单-ism_apsettlebill

## 单据体-子表 t_ism_apsettlebillentry

- **表名称：** 单据体-子表
- **表名：** t_ism_apsettlebillentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | frelatebaseqty | 应付基本数量 | numeric | 23 | 10 | √ | 0 | 应付基本数量 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | festimatedapqty | 已暂估应付数量 | numeric | 23 | 10 | √ | 0 | 已暂估应付数量 |
| 7 | fbizcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 8 | fseq | 分录行号 | numeric | 23 | 10 | √ | 0 | 分录行号 |
| 9 | foutownerid | 调出货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 11 | fistax | 含税 | bpchar | 1 |  | √ | ' ' | 含税 |
| 12 | fparentproduct | 父项产品 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 13 | festimatedapbaseqty | 已暂估应付基本数量 | numeric | 23 | 10 | √ | 0 | 已暂估应付基本数量 |
| 14 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 15 | fcuramount | 金额本位币 | numeric | 23 | 10 | √ | 0 | 金额本位币 |
| 16 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | finownerid | 调入货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fresidueqty | 剩余应付数量 | numeric | 23 | 10 | √ | 0 | 剩余应付数量 |
| 20 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 21 | finnerformmig | 内部单据实体（迁移） | varchar | 100 |  | √ | ' ' | 内部单据实体（迁移） |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 23 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 24 | fprocessplanid | 工序计划 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 25 | fprocessplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 26 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 29 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 30 | festpayunbackbaseqty | 暂估应付未冲回基本数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回基本数量 |
| 31 | fbizsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 32 | fparentrowid | 父项行ID | int8 | 64 |  | √ | 0 | 父项行ID |
| 33 | freturntype | 退货类型 | varchar | 50 |  | √ | ' ' | 退货类型,枚举: 1 :退货 2 :退补货 3 :仅退款不退货 |
| 34 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 35 | fcuramountandtax | 价税合计本位币 | numeric | 23 | 10 | √ | 0 | 价税合计本位币 |
| 36 | fsuitegroupid | 套件分组号 | int8 | 64 |  | √ | 0 | 套件分组号 |
| 37 | fresiduebaseqty | 剩余应付基本数量 | numeric | 23 | 10 | √ | 0 | 剩余应付基本数量 |
| 38 | fexchangetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 41 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | flotnumber | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 43 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 44 | fbizformmig | 业务单据实体（迁移） | varchar | 100 |  | √ | ' ' | 业务单据实体（迁移） |
| 45 | fhasapbusbill | 是否生成暂估应付单 | bpchar | 1 |  | √ | ' ' | 是否生成暂估应付单 |
| 46 | famount | 结算金额 | numeric | 23 | 10 | √ | 0 | 结算金额 |
| 47 | fsettledirection | 结算方向 | varchar | 50 |  | √ | ' ' | 结算方向,枚举: 0 :普通 1 :退货 |
| 48 | fprice | 结算单价 | numeric | 23 | 10 | √ | 0 | 结算单价 |
| 49 | finnerbilldate | 内部交易单据日期 | timestamp | 0 |  |  | null | 内部交易单据日期 |
| 50 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 51 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 52 | fpricelist | 结算价目表 | int8 | 64 |  | √ | 0 | [组织间结算价目表 ism_settlepricelist](../ism_files/ism_settlepricelist.md) |
| 53 | frelateqty | 应付数量 | numeric | 23 | 10 | √ | 0 | 应付数量 |
| 54 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | foutownertype | 调出货主类型 | varchar | 50 |  | √ | ' ' | 调出货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |
| 56 | fsettlesource | 取价来源 | varchar | 50 |  | √ | ' ' | 取价来源,枚举: 2 :来源业务单据价格 3 :来源订单价格 6 :指定固定价格 7 :实际成本价 8 :结算价目表 9 :结算取价策略 5 :自定义插件 10 :最新入库成本价 11 :往期最新出库成本价 12 :期初加权平均成本价 13 :当期加权平均成本价 14 :来源业务单据金额 |
| 57 | fismanualprice | 手工改价 | bpchar | 1 |  | √ | '0' | 手工改价 |
| 58 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 59 | fproducttype | 产品类别 | varchar | 50 |  | √ | ' ' | 产品类别,枚举: standard :标准产品 kitparent :套件父项 kitchild :套件子项 |
| 60 | frealcardid | 资产编码 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 61 | festpayunbackqty | 暂估应付未冲回数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回数量 |
| 62 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 63 | fbizmainorgid | 单据主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 64 | fcurtaxamount | 税额本位币 | numeric | 23 | 10 | √ | 0 | 税额本位币 |
| 65 | fcostincludetax | 应付税额计入成本 | bpchar | 1 |  | √ | ' ' | 应付税额计入成本 |
| 66 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 67 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 68 | finnerbiztype | 内部交易单据业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 69 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 70 | fconfirmrectiming | fconfirmrectiming | varchar | 50 |  | √ | ' ' |  |
| 71 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 72 | finownertype | 调入货主类型 | varchar | 50 |  | √ | ' ' | 调入货主类型,枚举: bos_org :业务单元 bd_supplier :供应商 bd_customer :客户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_apsettlebillentry |  | fentryid |
| 2 | idx_ism_apsettlebillentry |  | fid |

---

## 单据体-分表 t_ism_apsettlebillentry_b

- **表名称：** 单据体-分表
- **表名：** t_ism_apsettlebillentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmidid | 取价策略取价分录ID | int8 | 64 |  | √ | 0 | 取价策略取价分录ID |
| 3 | finnerbillno | 内部交易单据编号 | varchar | 50 |  | √ | ' ' | 内部交易单据编号 |
| 4 | funiqueid | 唯一标识（应收应付匹配） | varchar | 100 |  | √ | ' ' | 唯一标识（应收应付匹配） |
| 5 | fcorebillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 6 | finnerbillentryid | 内部交易单据分录ID | int8 | 64 |  | √ | 0 | 内部交易单据分录ID |
| 7 | fbizbillno | 业务单据编号 | varchar | 50 |  | √ | ' ' | 业务单据编号 |
| 8 | fcorebillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 9 | finnerbillentityid | 内部交易单据名称 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 10 | finnerbilltypeid | 内部交易单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 11 | finnerbillid | 内部交易单据ID | int8 | 64 |  | √ | 0 | 内部交易单据ID |
| 12 | fcorebillno | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 13 | fbizbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 14 | fbizbillentityid | 业务单据名称 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 15 | fcorebillrowseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 16 | fbizbilltypeid | 业务单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 17 | fbizbillseq | 业务单据行号 | int8 | 64 |  | √ | 0 | 业务单据行号 |
| 18 | fbizbilldate | 业务单据日期 | timestamp | 0 |  |  | null | 业务单据日期 |
| 19 | fbizbillbiztypeid | 业务单据业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fbizbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |
| 22 | fcorebillrowid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_apsettlebillentry_b |  | fentryid |
| 2 | idx_ism_apsetety_bizid |  | fbizbillid |
| 3 | idx_ism_apsettlebillety_b |  | fid |
| 4 | idx_ism_apsetety_bizdate |  | fbizbilldate |
| 5 | idx_ism_apsetety_innerid |  | finnerbillid |

---

## 应付结算清单-主表 t_ism_apsettlebill

- **表名称：** 应付结算清单-主表
- **表名：** t_ism_apsettlebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | facctsysid | 会计核算体系 | int8 | 64 |  | √ | 0 | [核算体系 xkbd_accountingsys](../fibd_files/xkbd_accountingsys.md) |
| 4 | faraptype | 应收应付类型 | varchar | 50 |  | √ | ' ' | 应收应付类型,枚举: ar :应收 ap :应付 |
| 5 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fbizenddate | 业务截止日期 | timestamp | 0 |  |  | null | 业务截止日期 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fhasapbusbill | fhasapbusbill | bpchar | 1 |  | √ | ' ' |  |
| 10 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fisdefaultaccsys | 是否默认核算体系 | bpchar | 1 |  | √ | ' ' | 是否默认核算体系 |
| 12 | fsupplierid | 对应供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsessionid | 创建线程ID | varchar | 50 |  | √ | ' ' | 创建线程ID |
| 16 | fmaporgid | 供应方核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 19 | fmapsettleorgid | 供应方结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fcustomerid | 对应客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 23 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ism_apsettlebill |  | fid |
| 2 | idx_ism_apsettlebill |  | forgid |
| 3 | idx_ism_apsetbill_edate |  | fbizenddate |
