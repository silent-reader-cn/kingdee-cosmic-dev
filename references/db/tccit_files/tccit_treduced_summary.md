# 减计收入台账单据-tccit_treduced_summary

## 减计收入台账单据-主表 t_tccit_treduced_summary

- **表名称：** 减计收入台账单据-主表
- **表名：** t_tccit_treduced_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdiscounttype | 优惠类型 | varchar | 30 |  | √ | ' ' | 优惠类型,枚举: 1 :全额免税 2 :收入减计10% 3 :收入减计50% 4 :减半征收 |
| 3 | fserialno | 流水号 | varchar | 100 |  | √ | ' ' | 流水号 |
| 4 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 5 | forgid | 运行组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | ftreducedpresent | 减计收入本期数 | numeric | 23 | 10 | √ | 0.0000000000 | 减计收入本期数 |
| 7 | fruleid | 优惠项目取数规则 | int8 | 64 |  | √ | 0 | 优惠项目取数规则 tccit_preferential_item |
| 8 | ftaxorgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | ftreducedtotal | 减计收入累计数 | numeric | 23 | 10 | √ | 0.0000000000 | 减计收入累计数 |
| 10 | ftreducedpercent | 减计比例 | int8 | 64 |  | √ | 0 | 优惠项目取数规则 tccit_preferential_item |
| 11 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 12 | ftreducedincome | 项目收入 | numeric | 23 | 10 | √ | 0.0000000000 | 项目收入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tccit_treduced_summary_pkey |  | fid |
| 2 | idx_tccit_treduced_summary |  | forgid,fskssqq,fskssqz |
