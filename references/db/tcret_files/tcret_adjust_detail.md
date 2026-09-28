# 调整明细-tcret_adjust_detail

## 调整明细-主表 t_tcret_adjust_detail

- **表名称：** 调整明细-主表
- **表名：** t_tcret_adjust_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadjustamount | 调整额 | numeric | 23 | 10 | √ | 0 | 调整额 |
| 3 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 4 | ftotalamount | 总额 | numeric | 23 | 10 | √ | 0 | 总额 |
| 5 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 6 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 7 | fitemname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | ftitlename | 调整项目 | varchar | 50 |  | √ | ' ' | 调整项目 |
| 10 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 11 | frentid | 租金项目id | varchar | 50 |  | √ | ' ' | 租金项目id |
| 12 | fitemid | 项目id | varchar | 50 |  | √ | ' ' | 项目id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_adjust_detail |  | fid |
| 2 | idx_taxc_tad_frentid |  | frentid,forgid,fskssqq,fskssqz |
