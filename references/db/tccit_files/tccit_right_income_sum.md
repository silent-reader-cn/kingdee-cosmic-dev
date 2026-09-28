# 未按权责发生制确认收入单据-tccit_right_income_sum

## 未按权责发生制确认收入单据-主表 t_tccit_right_income_sum

- **表名称：** 未按权责发生制确认收入单据-主表
- **表名：** t_tccit_right_income_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 3 | ftaxincomesum | 税收累计 | numeric | 23 | 10 | √ | 0.0000000000 | 税收累计 |
| 4 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 5 | fsignamount | 合同金额（交易金额） | numeric | 23 | 10 | √ | 0.0000000000 | 合同金额（交易金额） |
| 6 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 7 | fzzjecurrent | 账载本年 | numeric | 23 | 10 | √ | 0.0000000000 | 账载本年 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 9 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 10 | ftaxincomecurrent | 税收本年 | numeric | 23 | 10 | √ | 0.0000000000 | 税收本年 |
| 11 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 12 | fzzjesum | 账载累计 | numeric | 23 | 10 | √ | 0.0000000000 | 账载累计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_right_income_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_right_income_sum |  | fid |
