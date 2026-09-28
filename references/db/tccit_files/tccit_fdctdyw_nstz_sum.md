# 房地产特定业务台账（纳税调整）-tccit_fdctdyw_nstz_sum

## 房地产特定业务台账（纳税调整）-主表 t_tccit_fdctdyw_nstz_sum

- **表名称：** 房地产特定业务台账（纳税调整）-主表
- **表名：** t_tccit_fdctdyw_nstz_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 3 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 4 | fitemnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 5 | forgid | 运行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fentrytype | 取数类型 | varchar | 50 |  | √ | ' ' | 取数类型 |
| 7 | ftaxorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fbqje | 本期金额 | numeric | 23 | 10 | √ | 0 | 本期金额 |
| 9 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 10 | fbnljje | 本年累计金额 | numeric | 23 | 10 | √ | 0 | 本年累计金额 |
| 11 | fsqbnljje | 上期（本年累计金额） | numeric | 23 | 10 | √ | 0 | 上期（本年累计金额） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_fdctdyw_nstz_sum |  | fid |
| 2 | idx_tccit_fdctdyw_nstz_su |  | forgid,fskssqq,fskssqz |
