# 纳税汇总调整表明细-tccit_calc_summary_detail

## 纳税汇总调整表明细-主表 t_tccit_calc_summary_det

- **表名称：** 纳税汇总调整表明细-主表
- **表名：** t_tccit_calc_summary_det

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fitemno | 行次 | varchar | 50 |  | √ | ' ' | 行次 |
| 3 | fitemtype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型 |
| 4 | fmypkid | 行id | int8 | 64 |  | √ | 0 | 行id |
| 5 | fpreyearamount | 去年金额 | numeric | 23 | 10 | √ | 0.0000000000 | 去年金额 |
| 6 | fcuryearamount | 今年金额 | numeric | 23 | 10 | √ | 0.0000000000 | 今年金额 |
| 7 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 8 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 9 | fincrease | 涨幅 | varchar | 50 |  | √ | ' ' | 涨幅 |
| 10 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 11 | fmyparentid | 父级id | int8 | 64 |  | √ | 0 | 父级id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tccit_calc_summary_det |  | forgid,fskssqq,fskssqz |
| 2 | pk_tccit_calc_summary_det |  | fid |
