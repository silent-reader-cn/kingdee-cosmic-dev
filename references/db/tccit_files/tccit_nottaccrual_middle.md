# 未按权责发生制确认收入中间表-tccit_nottaccrual_middle

## 未按权责发生制确认收入中间表-主表 t_tccit_nottacc_midd

- **表名称：** 未按权责发生制确认收入中间表-主表
- **表名：** t_tccit_nottacc_midd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 关联id | int8 | 64 |  | √ | 0 | 关联id |
| 2 | fname | 项目名称 | varchar | 50 |  | √ | ' ' | 项目名称 |
| 3 | fsyjzje | 当年剩余结转 | numeric | 23 | 10 | √ | 0.0000000000 | 当年剩余结转 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 0 :禁用 1 :可用 |
| 5 | fljtaxincome | 累计税收收入金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计税收收入金额 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdnzzsr | 本年账载收入 | numeric | 23 | 10 | √ | 0.0000000000 | 本年账载收入 |
| 8 | fdnsssr | 本年税收收入 | numeric | 23 | 10 | √ | 0.0000000000 | 本年税收收入 |
| 9 | fsyjzamount | 剩余结转金额 | numeric | 23 | 10 | √ | 0.0000000000 | 剩余结转金额 |
| 10 | fljsssr | 累计税收收入 | numeric | 23 | 10 | √ | 0.0000000000 | 累计税收收入 |
| 11 | fljzzsr | 累计账载收入 | numeric | 23 | 10 | √ | 0.0000000000 | 累计账载收入 |
| 12 | fyear | 年份 | timestamp | 0 |  |  | null | 年份 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fhtzje | 合同总金额 | numeric | 23 | 10 | √ | 0.0000000000 | 合同总金额 |
| 15 | fincometype | 收入类型 | int8 | 64 |  | √ | 0 | 项目取数（树） tpo_yearitems_tree |
| 16 | fbillno | 项目编号 | varchar | 50 |  | √ | ' ' | 项目编号 |
| 17 | fljbookincome | 累计账载收入金额 | numeric | 23 | 10 | √ | 0.0000000000 | 累计账载收入金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_nottacc_midd |  | fentryid |
| 2 | idx_tccit_nottacc_midd |  | fbillno |
