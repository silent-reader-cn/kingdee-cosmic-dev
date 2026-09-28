# 对账单-scp_check

## 发票分录-子表 t_pur_checkinvoice

- **表名称：** 发票分录-子表
- **表名：** t_pur_checkinvoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvoiceamt | 开票金额 | numeric | 19 | 6 | √ | 0.000000 | 开票金额 |
| 3 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 4 | finvoiceid | 发票标识 | varchar | 50 |  | √ | ' ' | 发票标识 |
| 5 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | finvoicecode | 发票代码 | varchar | 255 |  | √ | ' ' | 发票代码 |
| 8 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_checkinvoice_pkey |  | fentryid |
| 2 | idx_pur_checkinvoice_fid_fseq |  | fid,fseq |

---

## 对账单-主表 t_pur_check

- **表名称：** 对账单-主表
- **表名：** t_pur_check

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | foperatorid | 采购方联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 5 | forgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 8 | fpayeesupid | 收款方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 9 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 10 | fsumamount | 发货/退回金额 | numeric | 19 | 6 | √ | 0.000000 | 发货/退回金额 |
| 11 | fsupgroupid | fsupgroupid | int8 | 64 |  | √ | 0 |  |
| 12 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 16 | fsumdiffqty | fsumdiffqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 17 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 20 | finvoicesupid | 开票供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 21 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 22 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fdelisupid | 送货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 24 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 26 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 27 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 28 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 29 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 30 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 31 | fsumdiffamt | 金额差异 | numeric | 19 | 6 | √ | 0.000000 | 金额差异 |
| 32 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 33 | fpersonid | 采购方联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 34 | fsumtaxamount | 确认金额 | numeric | 19 | 6 | √ | 0.000000 | 确认金额 |
| 35 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 36 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 37 | fcontacterid | 销售方联系人 | int8 | 64 |  | √ | 0 | 协同业务员 scp_bizperson |
| 38 | fsumamount_in | 入库/收货金额 | numeric | 19 | 6 | √ | 0.000000 | 入库/收货金额 |
| 39 | finvstatus | 开票状态 | bpchar | 1 |  | √ | 'A' | 开票状态,枚举: A :未完成 B :已完成 |
| 40 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_check_pkey |  | fid |
| 2 | idx_pur_check_fbilldate |  | fbilldate |
| 3 | idx_pur_check_fbillno |  | fbillno |
| 4 | idx_pur_check_fbizpartnerid |  | fbizpartnerid |

---

## 关联子实体-子表 t_pur_checkentry2_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_checkentry2_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | finqty | finqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsuminvqty_old | 已开票数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票数量_原始携带值 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsuminvqty | 已开票数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票数量_确认携带值 |
| 8 | fsuminvamt_old | 已开票价税合计_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票价税合计_原始携带值 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fpkid | fpkid | int8 | 64 |  | √ | null | id |
| 11 | finqty_old | finqty_old | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 12 | fsuminvamt | 已开票价税合计_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票价税合计_确认携带值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_checkentry2_lk_pkey |  | fpkid |

---

## 发货明细-子表 t_pur_checkentry

- **表名称：** 发货明细-子表
- **表名：** t_pur_checkentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutqty | 发货数量 | numeric | 19 | 6 | √ | 0.000000 | 发货数量 |
| 3 | finqty | 入库/收货数量 | numeric | 19 | 6 | √ | 0.000000 | 入库/收货数量 |
| 4 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fintaxamount | 入库/收货金额 | numeric | 19 | 6 | √ | 0.000000 | 入库/收货金额 |
| 8 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 11 | fdiffqty | 数量差异 | numeric | 19 | 6 | √ | 0.000000 | 数量差异 |
| 12 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 13 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 14 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 15 | foutbilldate | 发货日期 | timestamp | 0 |  |  | null | 发货日期 |
| 16 | foutbillno | 发货单号 | varchar | 255 |  | √ | ' ' | 发货单号 |
| 17 | finbillno | 匹配入库单号 | varchar | 255 |  | √ | ' ' | 匹配入库单号 |
| 18 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 19 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 20 | fouttaxamount | 发货金额 | numeric | 19 | 6 | √ | 0.000000 | 发货金额 |
| 21 | fdiffamt | 金额差异 | numeric | 19 | 6 | √ | 0.000000 | 金额差异 |
| 22 | fqty | 确认数量 | numeric | 19 | 6 | √ | 0.000000 | 确认数量 |
| 23 | ftaxamount | 确认金额 | numeric | 19 | 6 | √ | 0.000000 | 确认金额 |
| 24 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 26 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 27 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 29 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 30 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 31 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 32 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 33 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 35 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 36 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 37 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 38 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 42 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_checkentry_fid_fseq |  | fid,fseq |
| 2 | idx_pur_checkentry_fmaterialid |  | fmaterialid |
| 3 | t_pur_checkentry_pkey |  | fentryid |

---

## 入库明细-子表 t_pur_checkentry2

- **表名称：** 入库明细-子表
- **表名：** t_pur_checkentry2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 4 | factcheckamount | 实际对账金额 | numeric | 23 | 10 | √ | 0 | 实际对账金额 |
| 5 | fintaxamount | 入库/收货金额 | numeric | 19 | 6 | √ | 0.000000 | 入库/收货金额 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 8 | finbillno | 入库/收货单号 | varchar | 80 |  | √ | ' ' | 入库/收货单号 |
| 9 | fouttaxamount | 发货/退回金额 | numeric | 19 | 6 | √ | 0.000000 | 发货/退回金额 |
| 10 | funmatchqty | 可开票数量 | numeric | 23 | 10 | √ | 0 | 可开票数量 |
| 11 | fqty | 确认数量 | numeric | 19 | 6 | √ | 0.000000 | 确认数量 |
| 12 | ftaxamount | 确认金额 | numeric | 19 | 6 | √ | 0.000000 | 确认金额 |
| 13 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 14 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | factchecktaxamount | 实际对账价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 实际对账价税合计 |
| 16 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目号 pur_project |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 18 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 19 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 20 | funmatchamt | 可开票价税合计 | numeric | 23 | 10 | √ | 0 | 可开票价税合计 |
| 21 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 22 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 23 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 24 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 25 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 27 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 30 | finqty | 入库/收货数量 | numeric | 19 | 6 | √ | 0.000000 | 入库/收货数量 |
| 31 | foutqty | 发货/退回数量 | numeric | 19 | 6 | √ | 0.000000 | 发货/退回数量 |
| 32 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 33 | fwriteoffflag | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 34 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 35 | fdiffqty | 数量差异 | numeric | 19 | 6 | √ | 0.000000 | 数量差异 |
| 36 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 37 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 38 | factcheckprice | 实际对账单价 | numeric | 23 | 10 | √ | 0 | 实际对账单价 |
| 39 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 40 | foutbillno | 发货/退回单号 | varchar | 255 |  | √ | ' ' | 发货/退回单号 |
| 41 | factchecktaxprice | 实际对账含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际对账含税单价 |
| 42 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 43 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 44 | fdiffamt | 金额差异 | numeric | 19 | 6 | √ | 0.000000 | 金额差异 |
| 45 | funmatchamount | 可开票金额 | numeric | 23 | 10 | √ | 0 | 可开票金额 |
| 46 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 47 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 48 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 49 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 50 | finbilldate | 入库/收货日期 | timestamp | 0 |  |  | null | 入库/收货日期 |
| 51 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_checkentry2_fid_fseq |  | fid,fseq |
| 2 | idx_pur_checkentry2_fmatid |  | fmaterialid |
| 3 | t_pur_checkentry2_pkey |  | fentryid |

---

## 对账单-关联追踪表 t_pur_check_tc

- **表名称：** 对账单-关联追踪表
- **表名：** t_pur_check_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_check_tc_tid |  | ftid |
| 2 | t_pur_check_tc_pkey |  | fid |
| 3 | idx_pur_check_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_pur_checkentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_checkentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | fqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fqty_old | fqty_old | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_checkentry_lk_pkey |  | fpkid |

---

## 对账单-反写记录表 t_pur_check_wb

- **表名称：** 对账单-反写记录表
- **表名：** t_pur_check_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_check_wb_pkey |  | fentryid |

---

## 对账单-多语言表 t_pur_check_l

- **表名称：** 对账单-多语言表
- **表名：** t_pur_check_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_check_l_fid |  | fid,flocaleid |
| 2 | t_pur_check_l_pkey |  | fpkid |

---

## 对账单-分表 t_pur_check_a

- **表名称：** 对账单-分表
- **表名：** t_pur_check_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fdateto | 对账截止日期 | timestamp | 0 |  |  | null | 对账截止日期 |
| 5 | finvdetail | 开票要求 | bpchar | 1 |  | √ | ' ' | 开票要求,枚举: 1 :汇总开具 2 :按明细开具 |
| 6 | finvtypeid | 发票种类 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fsuggestion | 处理意见 | varchar | 255 |  | √ | ' ' | 处理意见 |
| 9 | frejectreason | 打回原因 | varchar | 512 |  |  | ' ' | 打回原因 |
| 10 | frejecterid | 打回人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 13 | fispayrequest | fispayrequest | bpchar | 1 |  | √ | ' ' |  |
| 14 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :企业 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fchkschemeid | 对账方案 | int8 | 64 |  | √ | 0 | 对账方案 scp_chkscheme |
| 19 | fchecksource | 对账来源 | bpchar | 1 |  | √ | ' ' | 对账来源,枚举: 1 :订单对账 2 :手工对账 |
| 20 | fpayreqbillno | fpayreqbillno | varchar | 80 |  | √ | ' ' |  |
| 21 | finvtype | 发票种类 | bpchar | 1 |  | √ | ' ' | 发票种类,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 |
| 22 | frejectdate | 打回时间 | timestamp | 0 |  |  | null | 打回时间 |
| 23 | fdatefrom | 对账起始日期 | timestamp | 0 |  |  | null | 对账起始日期 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_check_a_ftime |  | fcreatetime |
| 2 | t_pur_check_a_pkey |  | fid |

---

## 附件-附件表 t_pur_checrejectreasonatt

- **表名称：** 附件-附件表
- **表名：** t_pur_checrejectreasonatt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 附件字段实体 bd_attachment |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | FPKID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pur_checrejectreasonatt |  | fpkid |
| 2 | idx_checrejectatt_fbasedataid |  | fbasedataid |

---

## 入库明细-分表 t_pur_checkentry2_a

- **表名称：** 入库明细-分表
- **表名：** t_pur_checkentry2_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 5 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 6 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fentryloccurr | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 8 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 9 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 10 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 11 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 12 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 13 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 14 | fsuminvqty | 已开票数量 | numeric | 19 | 6 | √ | 0.000000 | 已开票数量 |
| 15 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 16 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 17 | fpoentryid | 订单分录ID | varchar | 50 |  | √ | ' ' | 订单分录ID |
| 18 | flocamount | 金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 金额(本位币) |
| 19 | finvoiceid | 发票标识 | varchar | 50 |  | √ | ' ' | 发票标识 |
| 20 | fentryexchrate | 汇率 | numeric | 23 | 10 | √ | 1 | 汇率 |
| 21 | factbillno | 实际入库单号 | varchar | 50 |  | √ | ' ' | 实际入库单号 |
| 22 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 25 | fsuminvamount | 已开票金额 | numeric | 23 | 10 | √ | 0 | 已开票金额 |
| 26 | fpcentryid | 合同分录ID | varchar | 50 |  | √ | ' ' | 合同分录ID |
| 27 | fsuminvamt | 已开票价税合计 | numeric | 19 | 6 | √ | 0.000000 | 已开票价税合计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_checkentry2_a_fpoid |  | fpoentryid |
| 2 | t_pur_checkentry2_a_pkey |  | fentryid |
| 3 | idx_pur_checkentry2_a_fid |  | fid |

---

## 发货明细-分表 t_pur_checkentry_a

- **表名称：** 发货明细-分表
- **表名：** t_pur_checkentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 4 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 5 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 6 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 7 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 8 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 9 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 10 | fsuminvqty | 关联开票数量 | numeric | 19 | 6 | √ | 0.000000 | 关联开票数量 |
| 11 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 12 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 13 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 14 | flocamount | 金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 金额(本位币) |
| 15 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 16 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 17 | finvoiceid | 发票标识 | varchar | 50 |  | √ | ' ' | 发票标识 |
| 18 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 19 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 22 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |
| 23 | fsuminvamt | 关联开票金额 | numeric | 19 | 6 | √ | 0.000000 | 关联开票金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_checkentry_a_fid |  | fid |
| 2 | idx_pur_checkentry_a_fpoid |  | fpoentryid |
| 3 | t_pur_checkentry_a_pkey |  | fentryid |
