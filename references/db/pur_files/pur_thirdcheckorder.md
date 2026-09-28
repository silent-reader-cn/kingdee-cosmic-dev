# 电商对账单-pur_thirdcheckorder

## 电商对账单-主表 t_pur_thirdcheckorder

- **表名称：** 电商对账单-主表
- **表名：** t_pur_thirdcheckorder

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frcvorgid | 收货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fcurrid | 结算币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | freqorgid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsumsaloutamount | 电商结算总金额 | numeric | 19 | 6 | √ | 0.000000 | 电商结算总金额 |
| 7 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbilldate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 9 | fsupplierid | 电商平台 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 10 | fpaymentbillno | 账单编号 | varchar | 80 |  | √ | ' ' | 账单编号 |
| 11 | finvoicestate | 开票状态 | varchar | 10 |  | √ | ' ' | 开票状态,枚举: 1 :待申请 2 :待审核 3 :驳回 4 :部分开票成功 5 :待出票 6 :开票成功 7 :处理中 8 :开票失败 9 :取消开票成功 |
| 12 | freqpersonid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmalbillno | 商城订单号 | varchar | 80 |  | √ | ' ' | 商城订单号 |
| 14 | frcvpersonid | 收货人 | int8 | 64 |  | √ | 0 | [收货地址 mal_address](../mal_files/mal_address.md) |
| 15 | fpurbillno | 采购订单编号 | varchar | 80 |  | √ | ' ' | 采购订单编号 |
| 16 | fsumdiffamount | 差异金额 | numeric | 19 | 6 | √ | 0.000000 | 差异金额 |
| 17 | fpersonid | 采购员 | int8 | 64 |  | √ | 0 | [业务员 pur_bizperson](../pbd_files/pur_bizperson.md) |
| 18 | fsumtaxamount | 电商订单总金额 | numeric | 19 | 6 | √ | 0.000000 | 电商订单总金额 |
| 19 | fbusinesstypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 20 | fchildbillno | 电商子订单号 | varchar | 80 |  | √ | ' ' | 电商子订单号 |
| 21 | fbillno | 电商订单号 | varchar | 80 |  | √ | ' ' | 电商订单号 |
| 22 | fsumsettleamount | 收货金额 | numeric | 19 | 6 | √ | 0.000000 | 收货金额 |
| 23 | fcheckstatus | 对账结果 | bpchar | 1 |  | √ | ' ' | 对账结果,枚举: A :有差异 B :无差异 |
| 24 | fthirdorderid | 京东单 | int8 | 64 |  | √ | 0 | [京东订单 pbd_jdorder](../pbd_files/pbd_jdorder.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pur_thirdcheck_fcnumber |  | fchildbillno |
| 2 | t_pur_thirdcheckorder_pkey |  | fid |

---

## 单据体-子表 t_pur_thirdcheckentry

- **表名称：** 单据体-子表
- **表名：** t_pur_thirdcheckentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frcvno | 收货/入库单号 | varchar | 80 |  | √ | ' ' | 收货/入库单号 |
| 3 | fgoodsid | 商品编码 | int8 | 64 |  | √ | 0 | [自建商品池 pmm_prodmanage](../pmm_files/pmm_prodmanage.md) |
| 4 | fmaterialid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ftaxprice | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 8 | fpurtypeid | 采购类型 | int8 | 64 |  | √ | 0 | [协同辅助资料 pbd_mallextdata](../pbd_files/pbd_mallextdata.md) |
| 9 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: |
| 10 | frcvdate | 收货/入库日期 | timestamp | 0 |  |  | null | 收货/入库日期 |
| 11 | frcvqty | 收货/入库数量 | numeric | 19 | 6 | √ | 0.000000 | 收货/入库数量 |
| 12 | frcventryid | frcventryid | int8 | 64 |  | √ | 0 |  |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | frcvamount | 收货/入库金额 | numeric | 19 | 6 | √ | 0.000000 | 收货/入库金额 |
| 15 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pur_thirdcheckentry_pkey |  | fentryid |
| 2 | idx_pur_thirdcheckentry_fid |  | fid |
