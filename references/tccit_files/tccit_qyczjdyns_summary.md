# 企业重组及递延纳税事项调整底稿-tccit_qyczjdyns_summary

## 企业重组及递延纳税事项调整底稿-主表 t_tccit_qyczjdyns_sum

- **表名称：** 企业重组及递延纳税事项调整底稿-主表
- **表名：** t_tccit_qyczjdyns_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | varchar | 50 |  | √ | ' ' | 行次 |
| 3 | ftsswclzzje | 特殊税务处理的账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 特殊税务处理的账载金额 |
| 4 | fnstzhjje | 纳税调整的合计金额 | numeric | 23 | 10 | √ | 0.0000000000 | 纳税调整的合计金额 |
| 5 | ftsswclssje | 特殊税务处理的税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 特殊税务处理的税收金额 |
| 6 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 7 | ftsczlxnumber | 特殊重组类型编码 | varchar | 50 |  | √ | ' ' | 特殊重组类型编码 |
| 8 | ftsswclnstzje | 特殊税务处理的纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 特殊税务处理的纳税调整金额 |
| 9 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 11 | fybswclzzje | 一般税务处理的账载金额 | numeric | 23 | 10 | √ | 0.0000000000 | 一般税务处理的账载金额 |
| 12 | ftsczlx | 特殊重组类型 | varchar | 200 |  | √ | ' ' | 特殊重组类型 |
| 13 | fybswclnstzje | 一般税务处理的纳税调整金额 | numeric | 23 | 10 | √ | 0.0000000000 | 一般税务处理的纳税调整金额 |
| 14 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 15 | fitemname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 16 | fybswclssje | 一般税务处理的税收金额 | numeric | 23 | 10 | √ | 0.0000000000 | 一般税务处理的税收金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_qyczjdyns_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_qyczjdyns_sum |  | fid |
