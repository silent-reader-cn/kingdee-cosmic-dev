# 发票匹配记录-invoice_match_record

## 发票匹配记录-主表 t_ap_invoice_match_record

- **表名称：** 发票匹配记录-主表
- **表名：** t_ap_invoice_match_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fchooserule | 选单规则 | varchar | 30 |  | √ | ' ' | 选单规则,枚举: ORDER :仅订单 DETAIL :明细单据 |
| 4 | fmatchtype | 匹配基准 | varchar | 30 |  | √ | ' ' | 匹配基准,枚举: AMT :金额基准 QTY :数量基准 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmatchrec | 匹配收货 | bpchar | 1 |  | √ | ' ' | 匹配收货 |
| 7 | finvmatch | 匹配类型 | varchar | 30 |  | √ | ' ' | 匹配类型,枚举: BILL :整单匹配 ENTRY :明细匹配 |
| 8 | finvoicebillid | 收票单ID | int8 | 64 |  | √ | 0 | 收票单ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_invoice_match_record |  | fid |
| 2 | idx_ap_invmatch_invid |  | finvoicebillid |

---

## 单据体-子表 t_ap_invoice_matchentry

- **表名称：** 单据体-子表
- **表名：** t_ap_invoice_matchentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatchqty | 匹配数量 | numeric | 23 | 10 | √ | 0.0000000000 | 匹配数量 |
| 3 | fapbillid | 应付单id | int8 | 64 |  | √ | 0 | 应付单id |
| 4 | fbillentryid | 单据行ID | int8 | 64 |  | √ | 0 | 单据行ID |
| 5 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fapbillentryid | 应付单分录id | int8 | 64 |  | √ | 0 | 应付单分录id |
| 8 | fupentrypk | 上游分录id | int8 | 64 |  | √ | 0 | 上游分录id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fbilltype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型 |
| 11 | finvpk | 收票单id | int8 | 64 |  | √ | 0 | 收票单id |
| 12 | fmatchamt | 匹配金额 | numeric | 23 | 10 | √ | 0.0000000000 | 匹配金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_invoice_matchentry |  | fentryid |
| 2 | idx_ap_matchentry_fid |  | fid |
| 3 | idx_ap_matchentry_apid |  | fapbillid,fapbillentryid |
| 4 | idx_ap_matchentry_fbid |  | fbillid,fbillentryid |
