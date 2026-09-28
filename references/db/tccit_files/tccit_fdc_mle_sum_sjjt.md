# 房地产特定业务台账（毛利额）税金计提实体表-tccit_fdc_mle_sum_sjjt

## 房地产特定业务台账（毛利额）税金计提实体表-主表 t_tccit_fdc_mle_sum_sjjt

- **表名称：** 房地产特定业务台账（毛利额）税金计提实体表-主表
- **表名：** t_tccit_fdc_mle_sum_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 3 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 4 | fitemnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 5 | fyjbqmle | 预计本期毛利额 | numeric | 23 | 10 | √ | 0 | 预计本期毛利额 |
| 6 | forgid | 运行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmll | 毛利率 | numeric | 23 | 10 | √ | 0 | 毛利率 |
| 8 | fentrytype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型 |
| 9 | ftaxorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fruleid | 项目取数规则 | int8 | 64 |  | √ | 0 | [其它取数规则 tccit_other_rule](../tccit_files/tccit_other_rule.md) |
| 11 | fbqsrje | 本期收入金额 | numeric | 23 | 10 | √ | 0 | 本期收入金额 |
| 12 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_fdc_mle_sum_sjjt |  | fid |
| 2 | idx_t_tccit_fdc_mle_sum_sjjt_1 |  | forgid,fskssqq,fskssqz |
