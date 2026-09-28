# OCR发票识别-bos_invoice

## 单据体-子表 t_bas_invoiceentrykey

- **表名称：** 单据体-子表
- **表名：** t_bas_invoiceentrykey

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvoiceentryindex | 发票分录序号 | int8 | 64 |  | √ | 0 | 发票分录序号 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | finvoiceentrykey | 发票分录属性 | varchar | 100 |  | √ | ' ' | 发票分录属性 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | finvoiceentryvalue | 发票分录值 | varchar | 2000 |  | √ | ' ' | 发票分录值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_bas_invoiceentrykey |  | fid |
| 2 | pk_t_bas_invoiceentrykey |  | fentryid |

---

## OCR发票识别-主表 t_bas_invoice

- **表名称：** OCR发票识别-主表
- **表名：** t_bas_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fbillstatue | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 6 | findexfield | 索引字段 | varchar | 255 |  | √ | ' ' | 索引字段 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fimagenumber | 影像编码 | varchar | 100 |  | √ | ' ' | 影像编码 |
| 9 | fimagepage | 影像页码 | varchar | 10 |  | √ | ' ' | 影像页码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | finvoicetype | 发票类型 | varchar | 100 |  | √ | ' ' | 发票类型 |
| 12 | fbillid | 单据id | varchar | 50 |  | √ | ' ' | 单据id |
| 13 | finvoicedate | 开票日期 | varchar | 50 |  | √ | ' ' | 开票日期 |
| 14 | finvoicecode | 发票代码 | varchar | 100 |  | √ | ' ' | 发票代码 |
| 15 | finvoiceno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_invoice |  | fid |
| 2 | index_bas_invoice_indexf |  | findexfield |
| 3 | index_bas_invoice_no |  | finvoiceno |
| 4 | index_bas_invoice |  | fbillid |

---

## 单据体-子表 t_bas_invoicekey

- **表名称：** 单据体-子表
- **表名：** t_bas_invoicekey

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | finvoicekey | 发票属性 | varchar | 100 |  | √ | ' ' | 发票属性 |
| 4 | finvoicevalue | 发票值 | varchar | 2000 |  | √ | ' ' | 发票值 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bas_invoicekey |  | fentryid |
| 2 | index_bas_invoicekey |  | fid |
