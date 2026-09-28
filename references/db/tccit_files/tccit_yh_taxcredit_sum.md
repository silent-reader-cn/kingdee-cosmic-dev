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
| 4 | fitemtype | 取数项目类型 | varchar | 50 |  | √ | ' ' | 取数项目类型 |
| 5 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 6 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 7 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 8 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 9 | fitemname | 取数项目名称 | varchar | 50 |  | √ | ' ' | 取数项目名称 |
| 10 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_yh_taxcredit_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_yh_taxcredit_sum |  | fid |
