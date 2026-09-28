# 付款规则-aqap_pay_rule

## 付款规则-主表 t_aqap_pay_rule

- **表名称：** 付款规则-主表
- **表名：** t_aqap_pay_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | int8 | 64 |  |  | null | 创建时间 |
| 5 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | flogic | 逻辑 | varchar | 50 |  | √ | ' ' | 逻辑 |
| 8 | fmodifytime | 修改时间 | int8 | 64 |  |  | null | 修改时间 |
| 9 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fkey | 匹配规则 | varchar | 50 |  | √ | ' ' | 匹配规则 |
| 12 | fcondition | 条件 | varchar | 50 |  | √ | ' ' | 条件 |
| 13 | fentryid | 分录id | int8 | 64 |  | √ | 0 | 分录id |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cluster_pay_rule |  | fkey |
| 2 | idx_aqap_pay_rule_fk |  | fid |
| 3 | pk_aqap_pay_rule |  | fentryid |
