# 房地产特定业务底稿单据（毛利额计算）-tccit_dg_b105093mle_sum

## 房地产特定业务底稿单据（毛利额计算）-主表 t_tccit_dg_b105093mle_sum

- **表名称：** 房地产特定业务底稿单据（毛利额计算）-主表
- **表名：** t_tccit_dg_b105093mle_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 5 | fyjmle | 预计毛利额 | numeric | 23 | 10 | √ | 0 | 预计毛利额 |
| 6 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | ffetchok | 规则是否取到数据 | bpchar | 1 |  | √ | '0' | 规则是否取到数据 |
| 8 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 9 | fsrje | 收入金额 | numeric | 23 | 10 | √ | 0 | 收入金额 |
| 10 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 11 | fitemnumber | fitemnumber | varchar | 50 |  | √ | ' ' |  |
| 12 | fmll | 毛利率 | numeric | 23 | 10 | √ | 0 | 毛利率 |
| 13 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 14 | fitemname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_dg_b105093mle_sum |  | fid |
| 2 | idx_tccit_b105093mle_sum |  | forgid,fskssqq,fskssqz |
