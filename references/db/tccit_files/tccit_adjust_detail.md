# 调整明细-tccit_adjust_detail

## 调整明细-主表 t_tccit_adjust_detail

- **表名称：** 调整明细-主表
- **表名：** t_tccit_adjust_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalamount | 总额 | numeric | 23 | 10 | √ | 0.0000000000 | 总额 |
| 3 | forgid | 组织id | int8 | 64 |  | √ | 0 | 组织id |
| 4 | famount | 金额 | numeric | 23 | 10 | √ | 0.0000000000 | 金额 |
| 5 | fadjustexplain | 调整说明 | varchar | 1000 |  | √ | ' ' | 调整说明 |
| 6 | fskssqq | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 7 | fadjustamount | 调整额 | numeric | 23 | 10 | √ | 0.0000000000 | 调整额 |
| 8 | fskssqz | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 9 | fitemnumber | 项目编码 | varchar | 50 |  | √ | ' ' | 项目编码 |
| 10 | fentrytype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型 |
| 11 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 12 | ftaxorgid | 取数组织id | int8 | 64 |  | √ | 0 | 取数组织id |
| 13 | fitemname | 名称 | varchar | 200 |  | √ | ' ' | 名称 |
| 14 | ftitlename | 调整项目 | varchar | 200 |  | √ | ' ' | 调整项目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tccit_adjust_detail |  | fid |
| 2 | idx_tccit_adjust_detail |  | forgid,fskssqq,fskssqz |
