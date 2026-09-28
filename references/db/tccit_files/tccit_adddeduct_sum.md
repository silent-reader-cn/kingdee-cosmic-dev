# 加计扣除底稿-tccit_adddeduct_sum

## 加计扣除底稿-主表 t_tccit_adddeduct_sum

- **表名称：** 加计扣除底稿-主表
- **表名：** t_tccit_adddeduct_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdiscounttype | 优惠类型 | varchar | 50 |  | √ | ' ' | 优惠类型,枚举: |
| 3 | fserialno | 流水号 | varchar | 50 |  | √ | ' ' | 流水号 |
| 4 | fskssqz | 日期范围.结束 | timestamp | 0 |  |  | null | 日期范围.结束 |
| 5 | forgid | 运行组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | ftaxorgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fruleid | 优惠项目取数规则 | int8 | 64 |  | √ | 0 | [优惠项目取数规则 tccit_preferential_item](../tccit_files/tccit_preferential_item.md) |
| 8 | fincome | 项目费用 | numeric | 23 | 10 | √ | 0 | 项目费用 |
| 9 | fskssqq | 日期范围.开始 | timestamp | 0 |  |  | null | 日期范围.开始 |
| 10 | fbnyffyjjkcze | 本年研发费用加计扣除总额 | numeric | 23 | 10 | √ | 0 | 本年研发费用加计扣除总额 |
| 11 | fjjkcpercent | 加计扣除比例 | numeric | 23 | 10 | √ | 0 | 加计扣除比例 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_adddeduct_sum |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_adddeduct_sum |  | fid |
