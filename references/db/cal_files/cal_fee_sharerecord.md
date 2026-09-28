# 采购费用分摊记录-cal_fee_sharerecord

## 采购费用分摊记录-主表 t_cal_feerecord

- **表名称：** 采购费用分摊记录-主表
- **表名：** t_cal_feerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 分摊时间 | timestamp | 0 |  |  | null | 分摊时间 |
| 5 | forgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fiswrittenoff | 冲销分摊 | bpchar | 1 |  | √ | '0' | 冲销分摊 |
| 7 | fsharestandard | 分摊标准 | varchar | 255 |  | √ | ' ' | 分摊标准,枚举: baseqty :数量 materialcost :材料成本 actualcost :实际成本 volume :体积 netweight :净重 customization :自定义权重 |
| 8 | fhooksource | 分摊方式 | varchar | 30 |  | √ | ' ' | 分摊方式,枚举: 1 :手动分摊 2 :自动分摊 3 :关联单据分摊 |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 分摊人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fhooktype | 分摊类型 | varchar | 30 |  | √ | ' ' | 分摊类型,枚举: A :采购暂估费用分摊 B :采购财务费用分摊 C :采购应付款项调整分摊 D :委外采购暂估费用分摊 E :委外采购财务费用分摊 F :委外采购应付款项调整分摊 |
| 13 | fsharedate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 14 | fmaincurrencyid | 原币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 16 | fbillno | 分摊编号 | varchar | 80 |  | √ | ' ' | 分摊编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cal_feerecord_pkey |  | fid |
| 2 | idx_cal_feerec_createtime |  | fcreatetime |
| 3 | idx_cal_feerec_billno |  | fbillno |

---

## 分录-子表 t_cal_feerecordentry

- **表名称：** 分录-子表
- **表名：** t_cal_feerecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillformid | 单据名称 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fcostadjustid | 成本调整单ID | int8 | 64 |  | √ | 0 | 成本调整单ID |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fsharetaxamount | 分摊价税合计(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 分摊价税合计(本位币) |
| 7 | fasstacttype | 往来类型 | varchar | 30 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bos_user :人员 bd_customer :客户 |
| 8 | famount | 分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊金额 |
| 9 | fshareamount | 分摊金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 分摊金额(本位币) |
| 10 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | frelationalentryid | 关联分摊源暂估分录ID | int8 | 64 |  | √ | 0 | 关联分摊源暂估分录ID |
| 12 | ftaxcategory | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |
| 13 | fshareuserid | 分摊人（废弃） | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsourceresultentryid | 上游分配结果单分录id | int8 | 64 |  | √ | 0 | 上游分配结果单分录id |
| 15 | fbillnum | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | ffinapwriteoffentryid | 关联财务被冲销分录ID | int8 | 64 |  | √ | 0 | 关联财务被冲销分录ID |
| 17 | fdistributevalue | 分摊权重 | numeric | 23 | 10 | √ | 0 | 分摊权重 |
| 18 | fcostadjustentryid | 成本调整单分录ID | int8 | 64 |  | √ | 0 | 成本调整单分录ID |
| 19 | fexpenseitemid | 费用项目编码 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 20 | ftaxamount | 分摊价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 分摊价税合计 |
| 21 | fasstactid | 往来户 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | fismianbill | 是否主方单据 | bpchar | 1 |  | √ | '0' | 是否主方单据 |
| 23 | fcalentryid | 核算单分录ID（废弃） | int8 | 64 |  | √ | 0 | 核算单分录ID（废弃） |
| 24 | fsharecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fbillentryid | 业务单据分录ID | int8 | 64 |  | √ | 0 | 业务单据分录ID |
| 26 | fcostadjustbillno | 成本调整单单号 | varchar | 80 |  | √ | ' ' | 成本调整单单号 |
| 27 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 28 | fbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 29 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 30 | fallocationratio | 分摊比例 | numeric | 23 | 10 | √ | 0 | 分摊比例 |
| 31 | fhascostadjust | 已生成成本调整单 | bpchar | 1 |  | √ | '0' | 已生成成本调整单 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 34 | fbillseq | 单据行号 | int8 | 64 |  | √ | 0 | 单据行号 |
| 35 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 36 | fbizbillentryid | 业务单据分录ID（废弃） | int8 | 64 |  | √ | 0 | 业务单据分录ID（废弃） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_feereentry_bizentryismid |  | fbizbillentryid,fismianbill,fid |
| 2 | idx_cal_feereentry_billentryid |  | fbillentryid |
| 3 | idx_cal_feereentry_billid |  | fbillid |
| 4 | t_cal_feerecordentry_pkey |  | fentryid |
| 5 | idx_cal_feereentry_relentryid |  | frelationalentryid |
| 6 | idx_cal_feereentry_id |  | fid |
