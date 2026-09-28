# 发票云发票识别结果-idi_invoice

## 发票云发票识别结果-主表 t_idi_invoice

- **表名称：** 发票云发票识别结果-主表
- **表名：** t_idi_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsecret | 客户加密 | varchar | 128 |  | √ | ' ' | 客户加密 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fclientid | 客户标识 | varchar | 64 |  | √ | ' ' | 客户标识 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | findexfield | 火车票飞机票重复键 | varchar | 255 |  | √ | ' ' | 火车票飞机票重复键 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fimagenumber | 影像编号 | varchar | 100 |  | √ | ' ' | 影像编号 |
| 11 | fimagepage | 影像页码 | varchar | 10 |  | √ | ' ' | 影像页码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | finvoicetype | 发票类型 | varchar | 100 |  | √ | ' ' | 发票类型 |
| 14 | fbillid | 单据id | varchar | 50 |  | √ | ' ' | 单据id |
| 15 | finvoicedate | 开票日期 | varchar | 50 |  | √ | ' ' | 开票日期 |
| 16 | finvoicecode | 发票代码 | varchar | 100 |  | √ | ' ' | 发票代码 |
| 17 | flocalurl | 原件预览url | varchar | 255 |  | √ | ' ' | 原件预览url |
| 18 | finvoiceno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 19 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fbilltype | 单据类型 | varchar | 36 |  | √ | ' ' | 单据类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_idi_invoice |  | fid |
| 2 | idx_idi__invoice_dup |  | findexfield |
| 3 | idx_idi__invoice |  | fbillid |

---

## 单据体-子表 t_idi_invoiceentrykey

- **表名称：** 单据体-子表
- **表名：** t_idi_invoiceentrykey

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
| 1 | pk_t_idi_invoiceentrykey |  | fentryid |
| 2 | idx_idi_invoiceentrykey |  | fid |

---

## 单据体-子表 t_idi_invoicekey

- **表名称：** 单据体-子表
- **表名：** t_idi_invoicekey

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
| 1 | pk_t_idi_invoicekey |  | fentryid |
| 2 | idx_idi_invoicekey |  | fid |
