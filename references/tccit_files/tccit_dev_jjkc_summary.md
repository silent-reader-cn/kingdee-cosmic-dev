# 研发费用加计扣除底稿-tccit_dev_jjkc_summary

## 研发费用加计扣除底稿-主表 t_tccit_dev_jjkc_sum

- **表名称：** 研发费用加计扣除底稿-主表
- **表名：** t_tccit_dev_jjkc_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行号 | int8 | 64 |  | √ | 0 | 行号 |
| 3 | fitemtype | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 4 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 7 | foriginalamount | 原始金额 | numeric | 23 | 10 | √ | 0.0000000000 | 原始金额 |
| 8 | fskssqq | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | fdeductiontype | 选择适用优惠政策 | varchar | 50 |  | √ | ' ' | 选择适用优惠政策,枚举: 1 :开发新技术、新产品、新工艺发生的研究开发费用加计扣除 2 :科技型中小企业开发新技术、新产品、新工艺发生的研究开发费用加计扣除 3 :企业为获得创新性、创意性、突破性的产品进行创意设计活动而发生的相关费用加计扣除 |
| 10 | fjjkcbljjsff | 加计扣除比例及计算方法 | int8 | 64 |  | √ | 0 | 业务定义分录 tpo_tccit_bizdef_entry |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_dev_jjkc_sum |  | fid |
| 2 | idx_tccit_dev_jjkc_sum |  | forgid,fskssqq,fskssqz |
