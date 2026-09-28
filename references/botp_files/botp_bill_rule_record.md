# 单据_转换规则记录-botp_bill_rule_record

## 单据_转换规则记录-主表 t_botp_bill_rule_record

- **表名称：** 单据_转换规则记录-主表
- **表名：** t_botp_bill_rule_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frule | 转换规则 | varchar | 50 |  | √ | ' ' | 转换规则 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 4 | fbill | 单据 | varchar | 50 |  | √ | ' ' | 单据 |
| 5 | foptype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型 |
| 6 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 7 | fopcode | 操作编码 | varchar | 50 |  | √ | ' ' | 操作编码 |
| 8 | fcurbill | 当前操作单据 | varchar | 50 |  | √ | ' ' | 当前操作单据 |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_botp_bill_rule_record |  | fid |
| 2 | idx_botp_br_record_userid_co |  | fuserid,foptype,fcurbill |
