# 比对单据体明细-gtcp_compare_entry_info

## 比对单据体明细-主表 t_gtcp_compare_entry_info

- **表名称：** 比对单据体明细-主表
- **表名：** t_gtcp_compare_entry_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 底稿id | int8 | 64 |  | √ | 0 | 底稿id |
| 2 | fdifference | 申报与计提差额 | numeric | 23 | 10 | √ | 0 | 申报与计提差额 |
| 3 | fdeclaretax | 申报税金 | numeric | 23 | 10 | √ | 0 | 申报税金 |
| 4 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 5 | ftaxaccrual | 计提税金 | numeric | 23 | 10 | √ | 0 | 计提税金 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtcp_entry_id |  | fid |
| 2 | pk_gtcp_compare_entry_info |  | fentryid |
