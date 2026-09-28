# 业务招待费调整汇总单据-tccit_ywzdf_tz_summary

## 业务招待费调整汇总单据-主表 t_tccit_ywzdf_tz_summary

- **表名称：** 业务招待费调整汇总单据-主表
- **表名：** t_tccit_ywzdf_tz_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | int4 | 32 |  | √ | 0 | 行次 |
| 3 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 4 | fewblxh | 二维表序号 | varchar | 50 |  | √ | ' ' | 二维表序号,枚举: 001 :业务招待费账载金额 002 :税务口径业务招待费 003 :扣除限额的计算： 003_01 :销售（营业）收入 003_02 :乘 ：扣除比例（%） 003_03 :扣除限额① 003_04 :税务口径业务招待费 003_05 :乘 ：扣除比例（%） 003_06 :扣除限额② 004 :纳税调整金额计算： 004_01 :税收金额 004_02 :纳税调整金额 |
| 5 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 6 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 7 | fsbbid | 申报表id | varchar | 50 |  | √ | ' ' | 申报表id |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 9 | foriginalamount | 原合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 原合计金额 |
| 10 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 11 | fewblname | 二维表名称 | varchar | 500 |  | √ | ' ' | 二维表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_ywzdf_tz_summary |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_ywzdf_tz_summary |  | fid |
