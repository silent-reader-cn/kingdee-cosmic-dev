# 销售折扣、折让和退回底稿-tccit_sale_zkzrth_summary

## 销售折扣、折让和退回底稿-主表 t_tccit_sale_zkzrth_sum

- **表名称：** 销售折扣、折让和退回底稿-主表
- **表名：** t_tccit_sale_zkzrth_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 3 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 4 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 6 | fjrdqsyje | 计入当期损益的金额 | numeric | 23 | 10 | √ | 0.0000000000 | 计入当期损益的金额 |
| 7 | fnstzje | 纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整金额 |
| 8 | fruleid | 规则ID | int8 | 64 |  | √ | 0 | 规则ID |
| 9 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fksqkcje | 可税前扣除的金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可税前扣除的金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_sale_zkzrth_sum |  | fid |
| 2 | idx_tccit_sale_zkzrth_sum |  | forgid,fskssqq,fskssqz |
