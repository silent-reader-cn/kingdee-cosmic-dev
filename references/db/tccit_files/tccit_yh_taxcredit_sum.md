# 所得税额抵免底稿-tccit_yh_taxcredit_sum

## 所得税额抵免底稿-主表 t_tccit_yh_taxcredit_sum

- **表名称：** 所得税额抵免底稿-主表
- **表名：** t_tccit_yh_taxcredit_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | int8 | 64 |  | √ | 0 | 行次 |
| 3 | ftaxamount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 4 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 5 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 901 :环境保护专用设备投资额 902 :节能节水专用设备 903 :安全生产专用设备 hj :合计 |
| 6 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 7 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 8 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |
| 9 | fitemtype | 取数项目类型 | varchar | 50 |  | √ | ' ' | 取数项目类型 |
| 10 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 11 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 12 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 13 | fitemname | 取数项目名称 | varchar | 50 |  | √ | ' ' | 取数项目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_yh_taxcredit_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_yh_taxcredit_sum |  | fid |
