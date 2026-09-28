# 非公益性捐赠支出计算底稿单据-tccit_dg_b105019_sum

## 非公益性捐赠支出计算底稿单据-主表 t_tccit_dg_b105019_sum

- **表名称：** 非公益性捐赠支出计算底稿单据-主表
- **表名：** t_tccit_dg_b105019_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fnstz | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 1 :项目 count :合计 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 7 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |
| 9 | fitemtype | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 10 | fssje | 税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 税收金额 |
| 11 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fzzje | 账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 账载金额 |
| 13 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 14 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_dg_b105019_sum |  | fid |
| 2 | idx_tccit_dg_b105019_sum |  | forgid,fskssqq,fskssqz |
