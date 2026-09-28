# 所得减免台账单据-tccit_incred_summary

## 所得减免台账单据-主表 t_tccit_incred_summary

- **表名称：** 所得减免台账单据-主表
- **表名：** t_tccit_incred_summary

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fincredtype | fincredtype | int8 | 64 |  | √ | 0 |  |
| 3 | fdiscounttype | 优惠类型 | varchar | 30 |  | √ | ' ' | 优惠类型,枚举: 1 :全额免税 2 :收入减计10% 3 :收入减计50% 4 :减半征收 |
| 4 | fserialno | 流水号 | varchar | 100 |  | √ | ' ' | 流水号 |
| 5 | forgid | 运行组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fincredincome | 项目所得 | numeric | 23 | 10 | √ | 0.0000000000 | 项目所得 |
| 7 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 8 | fincredpresent | 所得减免本期数 | numeric | 23 | 10 | √ | 0.0000000000 | 所得减免本期数 |
| 9 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 10 | fincredtotal | 所得减免累计数 | numeric | 23 | 10 | √ | 0.0000000000 | 所得减免累计数 |
| 11 | fruleid | 优惠项目取数规则 | int8 | 64 |  | √ | 0 | 优惠项目取数规则 tccit_preferential_item |
| 12 | ftaxorgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | freductratio | 减免比例 | numeric | 23 | 10 | √ | 0.0000000000 | 减免比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_incred_summary |  | forgid,fskssqq,fskssqz |
| 2 | t_tccit_incred_summary_pkey |  | fid |
