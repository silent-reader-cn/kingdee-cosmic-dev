# 申报底稿补退税额附表-gtcp_declare_payrefund

## 申报底稿补退税额附表-主表 t_gtcp_declare_payrefund

- **表名称：** 申报底稿补退税额附表-主表
- **表名：** t_gtcp_declare_payrefund

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 底稿id | int8 | 64 |  | √ | 0 | 底稿id |
| 2 | fdeclarestatus | 申报状态 | varchar | 50 |  | √ | 'editing' | 申报状态,枚举: editing :未申报 declared :已申报 |
| 3 | fdeclaredate | 申报日期 | timestamp | 0 |  |  | null | 申报日期 |
| 4 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 5 | fpayrefunddate | 缴/退税日期 | timestamp | 0 |  |  | null | 缴/退税日期 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fbqybtse | 本期应补(退)税额 | numeric | 23 | 10 | √ | 0 | 本期应补(退)税额 |
| 8 | fpayrefundstatus | 缴/退税状态 | varchar | 50 |  | √ | 'unpayrefund' | 缴/退税状态,枚举: unpaid :未缴退 paid :已缴退 nopay :无需缴退 partpaid :部分缴退 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gtcp_declare_payr_draftid |  | fid |
| 2 | pk_gtcp_declare_payrefund |  | fentryid |
