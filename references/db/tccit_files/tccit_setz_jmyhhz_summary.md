# 税额调整减免优惠汇总底稿单据-tccit_setz_jmyhhz_summary

## 税额调整减免优惠汇总底稿单据-主表 t_tccit_setz_jmyhhz

- **表名称：** 税额调整减免优惠汇总底稿单据-主表
- **表名：** t_tccit_setz_jmyhhz

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 展示序号 | varchar | 50 |  | √ | ' ' | 展示序号 |
| 3 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 4 | famountorratio | 金额或比例 | numeric | 23 | 10 | √ | 0.0000000000 | 金额或比例 |
| 5 | fcanuse | 勾选适用 | bpchar | 1 |  | √ | ' ' | 勾选适用 |
| 6 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 7 | fdeductibleratio | 减免比例 | numeric | 23 | 10 | √ | 0.0000000000 | 减免比例 |
| 8 | fitemtype | 项目 | varchar | 50 |  | √ | ' ' | 项目 |
| 9 | fmypkid | 行id | int8 | 64 |  | √ | 0 | 行id |
| 10 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 11 | foriitemno | 原序号 | varchar | 50 |  | √ | ' ' | 原序号 |
| 12 | fqualified | 满足条件 | bpchar | 1 |  | √ | ' ' | 满足条件 |
| 13 | fmyparentid | 父级id | int8 | 64 |  | √ | 0 | 父级id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_setz_jmyhhz |  | fid |
| 2 | idx_tccit_setz_jmyhhz |  | forgid,fskssqq,fskssqz |
