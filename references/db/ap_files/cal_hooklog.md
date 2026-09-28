# 入库勾稽日志-cal_hooklog

## 单据体-子表 t_cal_hooklogentry

- **表名称：** 单据体-子表
- **表名：** t_cal_hooklogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvbillid | 单据内码 | int8 | 64 |  | √ | 0 | 单据内码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fhookcostlc | 勾稽成本（本位币） | numeric | 23 | 10 | √ | 0 | 勾稽成本（本位币） |
| 5 | fhookallamount | 本次勾稽含税金额 | numeric | 23 | 10 | √ | 0 | 本次勾稽含税金额 |
| 6 | fhookamount | 本次勾稽金额 | numeric | 23 | 10 | √ | 0 | 本次勾稽金额 |
| 7 | fapbillentryid | 单据分录内码 | int8 | 64 |  | √ | 0 | 单据分录内码 |
| 8 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fapallamountlc | 含税总金额（本位币） | numeric | 23 | 10 | √ | 0 | 含税总金额（本位币） |
| 10 | fapallamount | 含税总金额 | numeric | 23 | 10 | √ | 0 | 含税总金额 |
| 11 | fcostadjustentryid | 成本调整单分录ID | int8 | 64 |  | √ | 0 | 成本调整单分录ID |
| 12 | fapmeasureunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fisgetinvoice | 先到票 | bpchar | 1 |  | √ | '0' | 先到票 |
| 14 | fhookallamountlc | 本次勾稽含税金额（本位币） | numeric | 23 | 10 | √ | 0 | 本次勾稽含税金额（本位币） |
| 15 | fapbusbillid | 暂估应付（先到票冲回）ID | int8 | 64 |  | √ | 0 | 暂估应付（先到票冲回）ID |
| 16 | fapamount | 总金额 | numeric | 23 | 10 | √ | 0 | 总金额 |
| 17 | finvbillseq | 单据行号 | int4 | 32 |  | √ | 0 | 单据行号 |
| 18 | fapamountlc | 总金额（本位币） | numeric | 23 | 10 | √ | 0 | 总金额（本位币） |
| 19 | fapbillid | 单据内码 | int8 | 64 |  | √ | 0 | 单据内码 |
| 20 | fapexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 21 | fcostadjustbillno | 成本调整单单号 | varchar | 80 |  | √ | ' ' | 成本调整单单号 |
| 22 | fhookallcostlc | 勾稽含税成本（本位币） | numeric | 23 | 10 | √ | 0 | 勾稽含税成本（本位币） |
| 23 | fapbillformid | 单据名称 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 24 | finvbillformid | 单据名称 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 25 | fhookamountlc | 本次勾稽金额（本位币） | numeric | 23 | 10 | √ | 0 | 本次勾稽金额（本位币） |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fhookallcost | 勾稽含税成本 | numeric | 23 | 10 | √ | 0 | 勾稽含税成本 |
| 28 | fapbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 29 | finvbillentryid | 单据分录内码 | int8 | 64 |  | √ | 0 | 单据分录内码 |
| 30 | fapexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 31 | fcostadjustid | 成本调整单ID | int8 | 64 |  | √ | 0 | 成本调整单ID |
| 32 | fmaterielid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 33 | finvsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 34 | fapbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 35 | fhookcost | 勾稽成本 | numeric | 23 | 10 | √ | 0 | 勾稽成本 |
| 36 | fapdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 37 | finvbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 38 | fapmeasureqty | 计量单位数量 | numeric | 23 | 10 | √ | 0 | 计量单位数量 |
| 39 | finvallqty | 全部数量 | numeric | 23 | 10 | √ | 0 | 全部数量 |
| 40 | fcurrencylcid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 41 | fismainhook | 是否主勾稽 | bpchar | 1 |  | √ | ' ' | 是否主勾稽 |
| 42 | fapbillseq | 单据行号 | int8 | 64 |  | √ | 0 | 单据行号 |
| 43 | fapsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 44 | finvdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 45 | fhookqty | 本次勾稽数量 | numeric | 23 | 10 | √ | 0 | 本次勾稽数量 |
| 46 | fexratedate | fexratedate | timestamp | 0 |  |  | null |  |
| 47 | finvbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |
| 48 | fhascostadjust | 已生成成本调整单 | bpchar | 1 |  | √ | '0' | 已生成成本调整单 |
| 49 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_hooklogentry_apid |  | fapbillid |
| 2 | idx_cal_hooklogentry_invno |  | finvbillno |
| 3 | idx_cal_hooklogentry_u |  | fapbillentryid,finvbillentryid |
| 4 | idx_cal_hooklogentry_invid |  | finvbillid |
| 5 | idx_cal_hooklogentry_inveid |  | finvbillentryid |
| 6 | pk_cal_hooklogentry |  | fentryid |
| 7 | idx_cal_hooklogentry_id |  | fid |
| 8 | idx_cal_hooklogentry_apno |  | fapbillno |

---

## 入库勾稽日志-主表 t_cal_hooklog

- **表名称：** 入库勾稽日志-主表
- **表名：** t_cal_hooklog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fallocationcriterion | fallocationcriterion | varchar | 30 |  | √ | ' ' |  |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 勾稽时间 | timestamp | 0 |  |  | null | 勾稽时间 |
| 6 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fhooksource | 勾稽方式 | varchar | 30 |  | √ | ' ' | 勾稽方式,枚举: A :自动勾稽 H :手工勾稽 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 勾稽人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fhooktype | 勾稽关系 | varchar | 30 |  | √ | ' ' | 勾稽关系,枚举: A :采购暂估应付勾稽 B :采购财务应付勾稽 IOSA :组织间结算暂估应付勾稽 IOSB :组织间结算财务应付勾稽 COA :跨组织采购暂估应付勾稽 COB :跨组织采购财务应付勾稽 WWA :委外暂估应付勾稽 WWB :委外财务应付勾稽 WWCOA :跨组织委外暂估应付勾稽 WWCOB :跨组织委外财务应付勾稽 IDB :采购入库发票差异勾稽 IDWWB :委外入库发票差异勾稽 DBHXA :暂估应付冲回单单边核销 DBHXAWW :暂估应付冲回单单边核销 DBHXAWWT :暂估应付冲回单单边核销 DBHXB :暂估应付与财务应付手工核销 DBHXBWW :暂估应付与财务应付手工核销 DBHXBWWT :暂估应付与财务应付手工核销 |
| 12 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 13 | fbillno | 勾稽编号 | varchar | 255 |  | √ | ' ' | 勾稽编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_hooklog |  | fid |
| 2 | idx_cal_hooklog_billno |  | fbillno |
