# 技术转让所得减免台账单据税金计提实体表-tccit_tech_sum_sjjt

## 技术转让所得减免台账单据税金计提实体表-主表 t_tccit_tech_sum_sjjt

- **表名称：** 技术转让所得减免台账单据税金计提实体表-主表
- **表名：** t_tccit_tech_sum_sjjt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemtypeid | 项目类型 | int8 | 64 |  | √ | 0 | 优惠项目（树） tpo_discount_tree |
| 3 | fincredpresent | 本期项目所得 | numeric | 23 | 10 | √ | 0 | 本期项目所得 |
| 4 | fdiscounttype | 优惠类型 | varchar | 50 |  | √ | ' ' | 优惠类型,枚举: 1 :全额免税 2 :收入减计10% 3 :收入减计50% 4 :减半征收 5 :三免三减半 6 :超五百万部分减半 7 :两免三减半 8 :五免五减半 9 :其他 10 :500万以内免税，超500万减半 11 :加计100% 12 :2000万以内免税，超2000万减半 13 :十年内免税 14 :研发费用加计扣除 15 :按10%抵免税额 |
| 5 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 6 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 7 | forgid | 运行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | ftaxorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fruleid | 优惠项目取数规则 | int8 | 64 |  | √ | 0 | [优惠项目取数规则 tccit_preferential_item](../tccit_files/tccit_preferential_item.md) |
| 10 | fincredtotal | 累计项目所得 | numeric | 23 | 10 | √ | 0 | 累计项目所得 |
| 11 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tccit_tech_sum_sjjt_1 |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_tech_sum_sjjt |  | fid |
