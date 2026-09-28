# 取数明细调整表-totf_accountdetail_adjust

## 取数明细调整表-主表 t_totf_accdetail_adjust

- **表名称：** 取数明细调整表-主表
- **表名：** t_totf_accdetail_adjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 3 | ftaxitem | 税目名称 | varchar | 50 |  | √ | ' ' | 税目名称 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftotalamount | 总额 | numeric | 23 | 10 | √ | 0 | 总额 |
| 6 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 7 | fskssqq | 税款所属期.开始 | timestamp | 0 |  |  | null | 税款所属期.开始 |
| 8 | flongruleid | 规则ID | int8 | 64 |  | √ | 0 | 水利基金不含税收入规则 totf_rule_waterfund |
| 9 | fmappingid | 映射字段ID | int8 | 64 |  | √ | 0 | 映射字段ID |
| 10 | fadjustamount | 调整额 | numeric | 23 | 10 | √ | 0 | 调整额 |
| 11 | fskssqz | 税款所属期.结束 | timestamp | 0 |  |  | null | 税款所属期.结束 |
| 12 | fruleid | fruleid | varchar | 50 |  | √ | ' ' |  |
| 13 | ftitlename | 调整项目 | varchar | 50 |  | √ | ' ' | 调整项目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_totf_accdetail_adjust |  | fid |
| 2 | idx_taxc_wafunddetadj_serialno |  | fserialno |
