# 汇缴扣除其他调整底稿-tccit_deduct_other_sum

## 汇缴扣除其他调整底稿-主表 t_tccit_deduct_other_sum

- **表名称：** 汇缴扣除其他调整底稿-主表
- **表名：** t_tccit_deduct_other_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 4 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 5 | fssje | 税收金额 | numeric | 23 | 10 | √ | 0 | 税收金额 |
| 6 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 8 | fzzje | 账载金额 | numeric | 23 | 10 | √ | 0 | 账载金额 |
| 9 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0 | 纳税调整金额 |
| 10 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 11 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tccit_deduct_other_sum_1 |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_deduct_other_sum |  | fid |
