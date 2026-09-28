# 比价查询-quo_compare

## 比价单分录-子表 t_pur_comparentry

- **表名称：** 比价单分录-子表
- **表名：** t_pur_comparentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 3 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftaxrate | 税率(%) | numeric | 19 | 6 | √ | 0.000000 | 税率(%) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | finquiryqty | 询价数量 | numeric | 19 | 6 | √ | 0.000000 | 询价数量 |
| 7 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 10 | ftaxprice | 确认含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 确认含税单价 |
| 11 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 12 | fincludeunittax | fincludeunittax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 13 | fprice | 确认单价 | numeric | 23 | 10 | √ | 0.0000000000 | 确认单价 |
| 14 | fdctamount | 折扣额 | numeric | 19 | 6 | √ | 0.000000 | 折扣额 |
| 15 | ftaxrateid | ftaxrateid | int8 | 64 |  | √ | 0 |  |
| 16 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 17 | fexrate | fexrate | numeric | 23 | 10 | √ | 0 |  |
| 18 | fqty | 确认数量 | numeric | 19 | 6 | √ | 0.000000 | 确认数量 |
| 19 | ftaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 20 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fdctrate | 单位折扣(率) | numeric | 19 | 6 | √ | 0.000000 | 单位折扣(率) |
| 22 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | ftraceid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 24 | fmaintainladder | fmaintainladder | varchar | 1 |  | √ | ' ' |  |
| 25 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fexcludeunittax | fexcludeunittax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 27 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 28 | fpcbillno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 29 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fquotecurr | fquotecurr | int8 | 64 |  | √ | 0 |  |
| 31 | fsupplierid | 销售方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 32 | fdelitypeid | 交货方式 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 33 | ftax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 34 | fmaterialnametext | 物料名称 | varchar | 255 |  | √ | ' ' | 物料名称 |
| 35 | fentryquotation | fentryquotation | bpchar | 1 |  | √ | '0' |  |
| 36 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 37 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fmaterialdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 41 | fvalidnum | fvalidnum | int4 | 32 |  | √ | 0 |  |
| 42 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 43 | fisupdateasinfo | fisupdateasinfo | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_comparentry_fid_fseq |  | fid,fseq |
| 2 | idx_pur_comparentry_fmatid |  | fmaterialid |
| 3 | t_pur_comparentry_pkey |  | fentryid |

---

## 比价查询-分表 t_pur_compare_a

- **表名称：** 比价查询-分表
- **表名：** t_pur_compare_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fpushprice | fpushprice | int8 | 64 |  | √ | 0 |  |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fcfmdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 8 | fcfmid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 11 | fpushsouce | fpushsouce | int8 | 64 |  | √ | 0 |  |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fpushresult | fpushresult | bpchar | 1 |  | √ | ' ' |  |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_compare_a_pkey |  | fid |
| 2 | idx_pur_compare_a_fcreatetime |  | fcreatetime |

---

## 比价查询-主表 t_pur_compare

- **表名称：** 比价查询-主表
- **表名：** t_pur_compare

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcontrolqty | fcontrolqty | varchar | 1 |  | √ | '1' |  |
| 3 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 5 | fratedate | fratedate | timestamp | 0 |  |  | null |  |
| 6 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | foperatorid | foperatorid | int8 | 64 |  | √ | 0 |  |
| 8 | forgid | 采购方 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fqtysource | fqtysource | bpchar | 1 |  | √ | '2' |  |
| 10 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 11 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 12 | fsupcurrtype | fsupcurrtype | bpchar | 1 |  | √ | '2' |  |
| 13 | fbiztype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 |
| 14 | fquotation | fquotation | bpchar | 1 |  | √ | '0' |  |
| 15 | fsumamount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 16 | fdatefrom | fdatefrom | timestamp | 0 |  |  | null |  |
| 17 | fdeliaddr | 交货地址 | varchar | 255 |  | √ | ' ' | 交货地址 |
| 18 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 19 | fbillno | 比价单号 | varchar | 80 |  | √ | ' ' | 比价单号 |
| 20 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 22 | fcurrid | 结算币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 23 | fdateto | fdateto | timestamp | 0 |  |  | null |  |
| 24 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 25 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 26 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fsumqty | 数量 | numeric | 19 | 6 | √ | 0.000000 | 数量 |
| 29 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 30 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 31 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 32 | fopenladder | fopenladder | varchar | 1 |  | √ | '0' |  |
| 33 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 |
| 34 | fcomparerange | fcomparerange | bpchar | 1 |  | √ | 'B' |  |
| 35 | fpersonid | 采购员 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 36 | finquiryno | 询价单号 | varchar | 80 |  | √ | ' ' | 询价单号 |
| 37 | fsumtaxamount | 价税合计 | numeric | 19 | 6 | √ | 0.000000 | 价税合计 |
| 38 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fsumtax | 税额 | numeric | 19 | 6 | √ | 0.000000 | 税额 |
| 40 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 41 | fexchrate | 汇率 | numeric | 19 | 6 | √ | 1.000000 | 汇率 |
| 42 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_compare_pkey |  | fid |
| 2 | idx_pur_compare_fbizpartnerid |  | fbizpartnerid |
| 3 | idx_pur_compare_fbilldate |  | fbilldate |
| 4 | idx_pur_compare_fbillno |  | fbillno |
| 5 | idx_pur_compare_finquiryno |  | finquiryno |

---

## 比价查询-多语言表 t_pur_compare_l

- **表名称：** 比价查询-多语言表
- **表名：** t_pur_compare_l

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
| 1 | t_pur_compare_l_pkey |  | fpkid |
| 2 | idx_pur_compare_l_fid |  | fid,flocaleid |

---

## 比价单分录-分表 t_pur_comparentry_a

- **表名称：** 比价单分录-分表
- **表名：** t_pur_comparentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 本位币税额 | numeric | 19 | 6 | √ | 0.000000 | 本位币税额 |
| 3 | fsrcentryid | 源单分录ID | varchar | 50 |  | √ | ' ' | 源单分录ID |
| 4 | fgoodsid | 供方商品编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 5 | fnewprice | fnewprice | numeric | 19 | 6 | √ | 0.000000 |  |
| 6 | flastwinbillid | flastwinbillid | varchar | 50 |  | √ | ' ' |  |
| 7 | favgprice | favgprice | numeric | 19 | 6 | √ | 0.000000 |  |
| 8 | fsumorderqty | fsumorderqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 9 | flastcompareid | flastcompareid | varchar | 50 |  | √ | ' ' |  |
| 10 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 11 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fprbillid | 申请单id | varchar | 50 |  | √ | ' ' | 申请单id |
| 13 | fmaxprice | fmaxprice | numeric | 19 | 6 | √ | 0.000000 |  |
| 14 | fhisminprice | fhisminprice | numeric | 19 | 6 | √ | 0.000000 |  |
| 15 | fquote6 | fquote6 | numeric | 19 | 6 | √ | 0.000000 |  |
| 16 | flastwinprice | flastwinprice | numeric | 19 | 6 | √ | 0 |  |
| 17 | fquote7 | fquote7 | numeric | 19 | 6 | √ | 0.000000 |  |
| 18 | fminorderqty | fminorderqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 19 | fquote8 | fquote8 | numeric | 19 | 6 | √ | 0.000000 |  |
| 20 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 22 | floctaxamount | 本位币价税合计 | numeric | 19 | 6 | √ | 0.000000 | 本位币价税合计 |
| 23 | fsupname | fsupname | varchar | 100 |  | √ | ' ' |  |
| 24 | fsumcontractqty | fsumcontractqty | numeric | 19 | 6 | √ | 0.000000 |  |
| 25 | fasstqty | 辅助数量 | numeric | 19 | 6 | √ | 0.000000 | 辅助数量 |
| 26 | fsrcbillid | 源单ID | varchar | 50 |  | √ | ' ' | 源单ID |
| 27 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 28 | fquote2 | fquote2 | numeric | 19 | 6 | √ | 0.000000 |  |
| 29 | fquote3 | fquote3 | numeric | 19 | 6 | √ | 0.000000 |  |
| 30 | fquote4 | fquote4 | numeric | 19 | 6 | √ | 0.000000 |  |
| 31 | fgoodsdesc | 供方商品描述 | varchar | 255 |  | √ | ' ' | 供方商品描述 |
| 32 | fquote5 | fquote5 | numeric | 19 | 6 | √ | 0.000000 |  |
| 33 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 34 | fquote1 | fquote1 | numeric | 19 | 6 | √ | 0.000000 |  |
| 35 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 36 | fprbillno | 申请单编号 | varchar | 80 |  | √ | ' ' | 申请单编号 |
| 37 | fpurleadday | fpurleadday | int8 | 64 |  | √ | 0 |  |
| 38 | flocamount | 本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 本位币金额 |
| 39 | fprentryid | 申请单分录id | varchar | 50 |  | √ | ' ' | 申请单分录id |
| 40 | fminprice | fminprice | numeric | 19 | 6 | √ | 0.000000 |  |
| 41 | fsrcbilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 43 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 44 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |
| 45 | flastcompareprice | flastcompareprice | numeric | 19 | 6 | √ | 0.000000 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_comparentry_a_pkey |  | fentryid |
| 2 | idx_pur_comparentry_a_fpoid |  | fpoentryid |
| 3 | idx_pur_comparentry_a_fid |  | fid |
