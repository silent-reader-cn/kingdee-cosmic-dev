# 发票类型和电子凭证映射-er_aeftickettype

## 发票类型和电子凭证映射-主表 t_er_aeftickettype

- **表名称：** 发票类型和电子凭证映射-主表
- **表名：** t_er_aeftickettype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvoicetypeid | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型(发票云) er_invoicetype |
| 3 | ftickettype | 电子凭证类型 | varchar | 80 |  | √ | ' ' | 电子凭证类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_aeftic_invtp |  | finvoicetypeid |
| 2 | pk_t_er_aeftickettype |  | fid |
