# 房地产特定业务台账（毛利额）-tccit_fdctdyw_mle_sum

## 房地产特定业务台账（毛利额）-主表 t_tccit_fdctdyw_mle_sum

- **表名称：** 房地产特定业务台账（毛利额）-主表
- **表名：** t_tccit_fdctdyw_mle_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fyjbqmll | fyjbqmll | numeric | 23 | 10 | √ | 0 |  |
| 3 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 4 | fyjbqmle | 预计本期毛利额 | numeric | 23 | 10 | √ | 0 | 预计本期毛利额 |
| 5 | forgid | 运行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbqsrje | 本期收入金额 | numeric | 23 | 10 | √ | 0 | 本期收入金额 |
| 7 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 8 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 9 | fitemnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 10 | fmll | 毛利率 | numeric | 23 | 10 | √ | 0 | 毛利率 |
| 11 | fentrytype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型 |
| 12 | ftaxorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fruleid | 项目取数规则 | int8 | 64 |  | √ | 0 | [其它取数规则 tccit_other_rule](../tccit_files/tccit_other_rule.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_fdctdyw_mle_sum |  | fid |
| 2 | idx_tccit_fdctdyw_mle_sum |  | forgid,fskssqq,fskssqz |
