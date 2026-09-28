# 减计收入台账单据税金计提实体表-tccit_treduced_sum_sjjt

## 减计收入台账单据税金计提实体表-主表 t_tccit_treduced_sum_sjjt

- **表名称：** 减计收入台账单据税金计提实体表-主表
- **表名：** t_tccit_treduced_sum_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdiscounttype | 优惠类型 | varchar | 50 |  | √ | ' ' | 优惠类型,枚举: 1 :全额免税 2 :收入减计10% 3 :收入减计50% 4 :减半征收 |
| 3 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 4 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 5 | forgid | 运行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftreducedpresent | 减计收入本期数 | numeric | 23 | 10 | √ | 0 | 减计收入本期数 |
| 7 | ftaxorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fruleid | 优惠项目取数规则 | int8 | 64 |  | √ | 0 | [优惠项目取数规则 tccit_preferential_item](../tccit_files/tccit_preferential_item.md) |
| 9 | ftreducedpercent | 减计比例 | int8 | 64 |  | √ | 0 | [优惠项目取数规则 tccit_preferential_item](../tccit_files/tccit_preferential_item.md) |
| 10 | ftreducedtotal | 减计收入累计数 | numeric | 23 | 10 | √ | 0 | 减计收入累计数 |
| 11 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 12 | ftreducedincome | 项目收入 | numeric | 23 | 10 | √ | 0 | 项目收入 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_treduced_sum_sjjt |  | fid |
| 2 | idx_t_tccit_treduced_sum_sjjt1 |  | forgid,fskssqq,fskssqz |
