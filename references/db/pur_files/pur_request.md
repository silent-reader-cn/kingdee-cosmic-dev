# 退货申请查询-pur_request

## 申请单分录-子表 t_pur_requestentry

- **表名称：** 申请单分录-子表
- **表名：** t_pur_requestentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fretdate | 退货日期 | timestamp | 0 |  |  | null | 退货日期 |
| 3 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fproddate | 生产日期 | timestamp | 0 |  |  | null | 生产日期 |
| 5 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.000000 | 税率(%) |
| 6 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 7 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 8 | fentrystatus | 行状态 | bpchar | 1 |  | √ | ' ' | 行状态,枚举: A :正常 B :已关闭 C :已冻结 D :已终止 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fnote | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 11 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 12 | famount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 13 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 14 | fpurtypeid | fpurtypeid | int8 | 64 |  | √ | 0 |  |
| 15 | fretreason | 退货原因 | varchar | 255 |  | √ | ' ' | 退货原因 |
| 16 | fdctamount | 折扣额 | numeric | 23 | 10 | √ | 0.000000 | 折扣额 |
| 17 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 18 | fqty | 退货数量 | numeric | 23 | 10 | √ | 0.000000 | 退货数量 |
| 19 | ftaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.000000 | 价税合计 |
| 20 | fdctrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0.000000 | 单位折扣(率) |
| 21 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | ftraceid | 跟踪号（废弃） | int8 | 64 |  | √ | 0 | [跟踪号 pur_trace](../pbd_files/pur_trace.md) |
| 23 | fmaterialnewid | 补货物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 24 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | fdiscounttype | 折扣方式 | varchar | 5 |  | √ | 'NULL' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 C :折扣额 NULL :无 |
| 26 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fpcbillno | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 28 | fispresent | 赠品 | bpchar | 1 |  | √ | ' ' | 赠品 |
| 29 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 30 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | finvorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 32 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 33 | flotid | 批号（废弃） | int8 | 64 |  | √ | 0 | [批号 pur_lot](../pbd_files/pur_lot.md) |
| 34 | ftax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 35 | fsuplot | 供应商批号 | varchar | 80 |  | √ | ' ' | 供应商批号 |
| 36 | freplenishqty | 补货数量 | numeric | 23 | 10 | √ | 0.000000 | 补货数量 |
| 37 | fmaterialnametext | 品类物料名称 | varchar | 255 |  | √ | ' ' | 品类物料名称 |
| 38 | ftraceno | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 39 | fasstproid | fasstproid | varchar | 50 |  | √ | ' ' |  |
| 40 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fmaterialdesc | 物料描述 | varchar | 255 |  | √ | ' ' | 物料描述 |
| 42 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 43 | fpobillno | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 44 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_requestentry_fmatid |  | fmaterialid |
| 2 | idx_pur_requestentry_fid_fseq |  | fid,fseq |
| 3 | t_pur_requestentry_pkey |  | fentryid |

---

## 退货申请查询-关联追踪表 t_pur_request_tc

- **表名称：** 退货申请查询-关联追踪表
- **表名：** t_pur_request_tc

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
| 1 | t_pur_request_tc_pkey |  | fid |
| 2 | idx_pur_request_tc_tbill |  | ftbillid |
| 3 | idx_pur_request_tc_tid |  | ftid |

---

## 申请单分录-分表 t_pur_requestentry_a

- **表名称：** 申请单分录-分表
- **表名：** t_pur_requestentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floctax | 税额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 税额(本位币) |
| 3 | fsrcentryid | 来源单据行ID | varchar | 50 |  | √ | ' ' | 来源单据行ID |
| 4 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [商品档案 pbd_goods](../pbd_files/pbd_goods.md) |
| 5 | fecorder | fecorder | int8 | 64 |  | √ | 0 |  |
| 6 | fbasicqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 7 | fasstunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fpickwaretype | 取件方式 | varchar | 10 |  | √ | ' ' | 取件方式,枚举: 4 :上门取件 7 :客户送货 40 :客户发货 1 :客户自发 61 :晨光上门取件 62 :晨光第三方物流 10 :上门取货 20 :客户邮寄 91 :上门取件 92 :客户发货 |
| 9 | fsumreturnqty | 关联退货数量 | numeric | 23 | 10 | √ | 0.000000 | 关联退货数量 |
| 10 | fbasicunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 12 | floctaxamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0.000000 | 价税合计(本位币) |
| 13 | fasstqty | 辅助数量 | numeric | 23 | 10 | √ | 0.000000 | 辅助数量 |
| 14 | fjdchildorderid | 京东子订单号 | varchar | 50 |  | √ | ' ' | 京东子订单号 |
| 15 | fsrcbillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 16 | facttaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际含税单价 |
| 17 | fgoodsdesc | 商品描述 | varchar | 255 |  | √ | ' ' | 商品描述 |
| 18 | fretreasoncode | fretreasoncode | varchar | 10 |  | √ | ' ' |  |
| 19 | factprice | 实际单价 | numeric | 23 | 10 | √ | 0.0000000000 | 实际单价 |
| 20 | fpoentryid | 订单行ID | varchar | 50 |  | √ | ' ' | 订单行ID |
| 21 | freturntype | 售后类型 | varchar | 10 |  | √ | ' ' | 售后类型,枚举: 1 :退货 2 :换货 3 :维修 10 :退货 20 :换货 30 :维修 4 :退货 5 :换货 |
| 22 | flocamount | 金额(本位币) | numeric | 23 | 10 | √ | 0.000000 | 金额(本位币) |
| 23 | fservicetime | fservicetime | varchar | 50 |  | √ | ' ' |  |
| 24 | fsrcbilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 26 | fpcbillid | 合同ID | varchar | 50 |  | √ | ' ' | 合同ID |
| 27 | fshoprettype | 商城补货方式 | varchar | 10 |  | √ | ' ' | 商城补货方式,枚举: |
| 28 | fpcentryid | 合同行ID | varchar | 50 |  | √ | ' ' | 合同行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_requestentry_a_fpoid |  | fpoentryid |
| 2 | t_pur_requestentry_a_pkey |  | fentryid |
| 3 | idx_pur_requestentry_a_fid |  | fid |

---

## 退货申请查询-主表 t_pur_request

- **表名称：** 退货申请查询-主表
- **表名：** t_pur_request

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddress | 取件地址 | varchar | 80 |  | √ | ' ' | 取件地址 |
| 3 | freqorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | floccurrid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | frettype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :库存退货 2 :暂收退货 |
| 6 | forgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fexchtypeid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 8 | freplenishtype | 退货类型 | bpchar | 1 |  | √ | ' ' | 退货类型,枚举: 1 :退货需补 2 :新补货订单 3 :退货不补 |
| 9 | fpurorderno | 采购订单号 | varchar | 80 |  | √ | ' ' | 采购订单号 |
| 10 | fsumamount | 金额 | numeric | 23 | 10 | √ | 0.000000 | 金额 |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | fphone | 联系电话（手机） | varchar | 80 |  | √ | ' ' | 联系电话（手机） |
| 13 | fpurorgid | 退货申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fdeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :保存 B :已提交 C :已审核 D :已关闭 Z :已作废 |
| 16 | femail | 邮箱 | varchar | 80 |  | √ | ' ' | 邮箱 |
| 17 | fpaycondid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 18 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 19 | fpersonid | 申请人（废弃） | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 20 | fsettleorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fsupaddr | fsupaddr | varchar | 255 |  | √ | ' ' |  |
| 22 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 23 | flinkman | 退货联系人 | varchar | 80 |  | √ | ' ' | 退货联系人 |
| 24 | fcontacterid | 供应商联系人 | int8 | 64 |  | √ | 0 | [协同业务员 scp_bizperson](../scp_files/scp_bizperson.md) |
| 25 | fcardnumber | fcardnumber | varchar | 80 |  | √ | ' ' |  |
| 26 | fbilltypeid | fbilltypeid | int8 | 64 |  | √ | 0 |  |
| 27 | fmalorderno | fmalorderno | varchar | 80 |  | √ | ' ' |  |
| 28 | foperatorid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 29 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 30 | fpickwaretype | fpickwaretype | bpchar | 10 |  | √ | ' ' |  |
| 31 | fpayeesupid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 32 | fbiztype | 业务类型(作废) | bpchar | 1 |  | √ | ' ' | 业务类型(作废),枚举: 1 :标准采购 2 :协议采购 3 :VMI采购 4 :JIT采购 5 :委外采购 6 :直运采购 7 :资产采购 8 :费用采购 9 :项目采购 10 :样品采购 : |
| 33 | fplatform | 单据来源 | bpchar | 1 |  | √ | ' ' | 单据来源,枚举: 0 :协同 1 :自建商城 2 :京东商城 3 :苏宁商城 5 :西域商城 6 :晨光商城 4 :得力商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 34 | fadmindivision | fadmindivision | varchar | 50 |  | √ | ' ' |  |
| 35 | ftaxtype | 计税类型 | bpchar | 1 |  | √ | ' ' | 计税类型,枚举: 1 :价外税(含税) 2 :价外税(不含税) 3 :价内税(含税) |
| 36 | frcvorgid | frcvorgid | int8 | 64 |  | √ | 0 |  |
| 37 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 38 | fcurrid | 结算币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 39 | fcardusername | fcardusername | varchar | 80 |  | √ | ' ' |  |
| 40 | foperatorgroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 41 | finvoicesupid | 开票供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 42 | fbank | fbank | varchar | 80 |  | √ | ' ' |  |
| 43 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fdelisupid | 送货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 45 | fpayorgid | 付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fsumqty | 数量 | numeric | 23 | 10 | √ | 0.000000 | 数量 |
| 47 | fbizpartnerid | 商务伙伴 | int8 | 64 |  | √ | 0 | [商务伙伴 bd_bizpartner](../base_files/bd_bizpartner.md) |
| 48 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 49 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 50 | fcfmstatus | 确认状态 | bpchar | 1 |  | √ | ' ' | 确认状态,枚举: A :待确认 B :已确认 C :已打回 D :变更中 E :取消 F :完成 G :自动确认 |
| 51 | fsumtaxamount | 价税合计 | numeric | 23 | 10 | √ | 0.000000 | 价税合计 |
| 52 | fsumtax | 税额 | numeric | 23 | 10 | √ | 0.000000 | 税额 |
| 53 | fexchrate | 汇率 | numeric | 23 | 10 | √ | 1.000000 | 汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_request_pkey |  | fid |
| 2 | idx_pur_request_fbillno |  | fbillno |
| 3 | idx_pur_request_fbizpartnerid |  | fbizpartnerid |
| 4 | idx_pur_request_fbilldate |  | fbilldate |

---

## 关联子实体-子表 t_pur_requestentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pur_requestentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 退货数量_确认携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 退货数量_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fqty_old | 退货数量_原始携带值 | numeric | 23 | 10 | √ | 0.0000000000 | 退货数量_原始携带值 |
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
| 1 | t_pur_requestentry_lk_pkey |  | fpkid |

---

## 退货申请查询-反写记录表 t_pur_request_wb

- **表名称：** 退货申请查询-反写记录表
- **表名：** t_pur_request_wb

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
| 1 | t_pur_request_wb_pkey |  | fentryid |

---

## 退货申请查询-分表 t_pur_request_a

- **表名称：** 退货申请查询-分表
- **表名：** t_pur_request_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmalorderno | fmalorderno | varchar | 50 |  | √ | ' ' |  |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fjdserviceid | fjdserviceid | varchar | 50 |  | √ | ' ' |  |
| 7 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 8 | fecsource | fecsource | varchar | 80 |  | √ | ' ' |  |
| 9 | fcfmdate | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 10 | fcfmid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | forigin | 发起方 | bpchar | 1 |  | √ | ' ' | 发起方,枚举: 1 :供应商 2 :采购方 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsupaddr | 供应商地址 | varchar | 255 |  | √ | ' ' | 供应商地址 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_request_a_pkey |  | fid |
| 2 | idx_pur_request_a_fcreatetime |  | fcreatetime |

---

## 退货申请查询-多语言表 t_pur_request_l

- **表名称：** 退货申请查询-多语言表
- **表名：** t_pur_request_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fsupaddr | fsupaddr | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_request_l_fid |  | fid,flocaleid |
| 2 | t_pur_request_l_pkey |  | fpkid |
