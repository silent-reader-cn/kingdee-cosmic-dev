# 采购收货同步-srm_receipt_sync

## 单据体-子表 t_srm_receipt_syncentity

- **表名称：** 单据体-子表
- **表名：** t_srm_receipt_syncentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fqty | 收货数量 | numeric | 23 | 10 | √ | 0 | 收货数量 |
| 3 | fdelidate | 交货日期 | timestamp | 0 |  |  | null | 交货日期 |
| 4 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 5 | floccurrid | 本位币币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | ftimelyreceiptqty | 基本及时收货数 | numeric | 23 | 10 | √ | 0 | 基本及时收货数 |
| 8 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | freceiptqty | 基本收货数量 | numeric | 23 | 10 | √ | 0 | 基本收货数量 |
| 11 | funtimelyreceiptqty | 基本不及时收货数 | numeric | 23 | 10 | √ | 0 | 基本不及时收货数 |
| 12 | fpoentryid | 订单分录ID | varchar | 50 |  | √ | ' ' | 订单分录ID |
| 13 | freceiptreturnqty | 基本退货数 | numeric | 23 | 10 | √ | 0 | 基本退货数 |
| 14 | fpobillid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 15 | fbasicunitid | 基本计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | forderqty | 基本订单数量 | numeric | 23 | 10 | √ | 0 | 基本订单数量 |
| 17 | floctaxamount | 本位币价税合计 | numeric | 23 | 10 | √ | 0 | 本位币价税合计 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fpobillno | 采购订单号 | varchar | 80 |  | √ | ' ' | 采购订单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_receiptentry_fmatid |  | fmaterialid |
| 2 | idx_srm_receiptentry_fpobillno |  | fpobillno |
| 3 | idx_srm_receiptentry_fid_fseq |  | fid,fseq |
| 4 | pk_srm_receipt_syncentity |  | fentryid |
| 5 | idx_srm_receiptentry_fpobillid |  | fpobillid |

---

## 采购收货同步-主表 t_srm_receipt_sync

- **表名称：** 采购收货同步-主表
- **表名：** t_srm_receipt_sync

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 同步状态 | bpchar | 1 |  | √ | '0' | 同步状态 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_srm_receiptsync_fbilldate |  | fbilldate |
| 2 | idx_srm_receiptsync_fbillno |  | fbillno |
| 3 | pk_srm_receipt_sync |  | fid |
| 4 | idx_srm_receiptsync_forgid |  | forgid |
| 5 | idx_srm_receiptsync_fsupid |  | fsupplierid |
