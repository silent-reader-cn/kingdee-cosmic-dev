# 收货查询-scp_receipt

## 收货查询-主表 t_pur_receipt

- **表名称：** 收货查询-主表
- **表名：** t_pur_receipt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | foperatorid | 采购方联系人 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 5 | fwriteoffflag | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 6 | forgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 8 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 9 | fpurdeptid | fpurdeptid | int8 | 64 |  | √ | 0 |  |
| 10 | freplenishtype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :退货需补 2 :创建补货订单 3 :退货不补 |
| 11 | fpayeesupid | 收款方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 12 | freqpersonid | freqpersonid | int8 | 64 |  | √ | 0 |  |
| 13 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 14 | fsumamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 15 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 18 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 21 | finvoicesupid | 开票方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | 付款条件 bd_paycondition |
| 23 | fvmisettle | VMI结算 | bpchar | 1 |  | √ | '0' | VMI结算 |
| 24 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fdelisupid | 发货方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 26 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 28 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | 商务伙伴 bd_bizpartner |
| 29 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 30 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 31 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 32 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 33 | finputamount | 录入金额 | bpchar | 1 |  | √ | '0' | 录入金额 |
| 34 | fpersonid | 采购方联系人（废弃） | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 35 | fsumtaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 36 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 38 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 39 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 40 | fcontacterid | 销售方联系人 | int8 | 64 |  | √ | 0 | 业务员 pur_bizperson |
| 41 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_receipt_pkey |  | fid |
| 2 | idx_pur_receipt_fbizpartnerid |  | fbilldate,fbizpartnerid |
| 3 | idx_pur_receipt_fsupplierid |  | fsupplierid |
| 4 | idx_pur_receipt_fbillno |  | fbillno |

---

## 收货查询分录-子表 t_pur_receiptentry

- **表名称：** 收货查询分录-子表
- **表名：** t_pur_receiptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproddate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 3 | freqorgid | 需求方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 5 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 7 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 11 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 12 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 13 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 14 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 15 | fqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 16 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 17 | frcvorgid | 收货方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 19 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 pur_trace |
| 20 | fpurorgid | 采购方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 23 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 24 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 25 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 26 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 27 | fpayorgid | 付款方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 28 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 29 | fjointdatachannelid | 对接渠道主键 | varchar | 80 |  | √ | ' ' | 对接渠道主键 |
| 30 | flotid | 批号（废弃） | int8 | 64 |  | √ | 0 | 批号 pur_lot |
| 31 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 32 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 33 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 34 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 35 | fsettleorgid | 核算方 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 38 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 39 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_receiptentry_fpobillno |  | fpobillno |
| 2 | t_pur_receiptentry_pkey |  | fentryid |
| 3 | idx_pur_receiptentry_fmatid |  | fmaterialid |
| 4 | idx_pur_receiptentry_fid_fseq |  | fid,fseq |

---

## 收货查询分录-分表 t_pur_receiptentry_a

- **表名称：** 收货查询分录-分表
- **表名：** t_pur_receiptentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 税额(本位币) |
| 3 | fsumcheckqty | 关联对账数量 | numeric | 19 | 6 | √ | 0.000000 | 关联对账数量 |
| 4 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 5 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | 商品档案 pbd_goods |
| 6 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 7 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | 协同辅助资料 pbd_mallextdata |
| 9 | fsettlesupid | 结算供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 10 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 12 | floctaxamount | 价税合计(本位币) | numeric | 19 | 6 | √ | 0.000000 | 价税合计(本位币) |
| 13 | funmatchbaseqty | 未核销基本数量 | numeric | 23 | 10 | √ | 0 | 未核销基本数量 |
| 14 | funmatchqty | 未核销数量 | numeric | 23 | 10 | √ | 0 | 未核销数量 |
| 15 | finvoiceqty | 已开票数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票数量 |
| 16 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 17 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 18 | fischeckorinvoice | 对账/开票 | bpchar | 1 |  | √ | '0' | 对账/开票 |
| 19 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 20 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 21 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 22 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 23 | fsuminvoiceqty | 关联数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联数量 |
| 24 | fsumrecretqty | 已退货数量 | numeric | 23 | 10 | √ | 0 | 已退货数量 |
| 25 | flocamount | 金额(本位币) | numeric | 19 | 6 | √ | 0.000000 | 金额(本位币) |
| 26 | finvoiceamt | 已开票金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已开票金额 |
| 27 | fsaloutnum | fsaloutnum | varchar | 80 |  | √ | ' ' |  |
| 28 | fsumcheckamt | 关联对账金额 | numeric | 19 | 6 | √ | 0.000000 | 关联对账金额 |
| 29 | fsaloutid | fsaloutid | int8 | 64 |  | √ | 0 |  |
| 30 | fsaloutentryid | fsaloutentryid | int8 | 64 |  | √ | 0 |  |
| 31 | fsumrecretbaseqty | 已退货基本数量 | numeric | 23 | 10 | √ | 0 | 已退货基本数量 |
| 32 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 34 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 35 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_receiptentry_a_pkey |  | fentryid |
| 2 | idx_pur_receiptentry_a_fid |  | fid |
| 3 | idx_pur_receiptentry_a_fpoid |  | fpoentryid |

---

## 收货查询-分表 t_pur_receipt_a

- **表名称：** 收货查询-分表
- **表名：** t_pur_receipt_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 7 | fchkbillno | 对账单号 | varchar | 80 |  | √ | ' ' | 对账单号 |
| 8 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fisreturn | 退货单 | bpchar | 1 |  | √ | ' ' | 退货单 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fischeck | 已对账 | bpchar | 1 |  | √ | ' ' | 已对账 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_receipt_a_fcreatetime |  | fcreatetime |
| 2 | t_pur_receipt_a_pkey |  | fid |

---

## 收货查询-多语言表 t_pur_receipt_l

- **表名称：** 收货查询-多语言表
- **表名：** t_pur_receipt_l

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
| 1 | idx_pur_receipt_l_fid |  | fid,flocaleid |
| 2 | t_pur_receipt_l_pkey |  | fpkid |
