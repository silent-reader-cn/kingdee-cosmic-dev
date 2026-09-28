# 城镇垃圾处理费取数明细调整-totf_czljclf_adjust

## 城镇垃圾处理费取数明细调整-主表 t_totf_czljclf_adjust

- **表名称：** 城镇垃圾处理费取数明细调整-主表
- **表名：** t_totf_czljclf_adjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fadjustamount | 调整额 | numeric | 23 | 10 | √ | 0 | 调整额 |
| 3 | fserialno | 台账流水号 | varchar | 50 |  | √ | ' ' | 台账流水号 |
| 4 | fskssqz | 税款所属期.结束 | timestamp | 0 |  |  | null | 税款所属期.结束 |
| 5 | ftaxitem | 税目名称 | varchar | 50 |  | √ | ' ' | 税目名称 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | ftotalamount | 总额 | numeric | 23 | 10 | √ | 0 | 总额 |
| 8 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 9 | fskssqq | 税款所属期.开始 | timestamp | 0 |  |  | null | 税款所属期.开始 |
| 10 | ftitlename | 调整项目 | varchar | 50 |  | √ | ' ' | 调整项目 |
| 11 | fmappingid | 映射字段ID | int8 | 64 |  | √ | 0 | 映射字段ID |
| 12 | flongruleid | 规则ID | int8 | 64 |  | √ | 0 | [城镇垃圾处理费规则 totf_rule_czljclf](../totf_files/totf_rule_czljclf.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_totf_czljadjust_serialno |  | fserialno |
| 2 | pk_totf_czljclf_adjust |  | fid |
