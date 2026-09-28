# 凭证-rim_vouch

## 凭证-主表 t_rim_vouch

- **表名称：** 凭证-主表
- **表名：** t_rim_vouch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouch_id | 凭证id | varchar | 50 |  | √ | ' ' | 凭证id |
| 3 | fbusiness_date | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 5 | fupdate_time | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 6 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 7 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fvouch_no | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 9 | fvouch_date | 凭证记账日期 | timestamp | 0 |  |  | null | 凭证记账日期 |
| 10 | fresource | 凭证来源 | varchar | 50 |  | √ | ' ' | 凭证来源,枚举: 1 :全票池维护 4 :苍穹 9 :第三方系统 |
| 11 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |
| 12 | fvouch_type | 凭证类型 | varchar | 20 |  | √ | ' ' | 凭证类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_vouch |  | fvouch_no |
| 2 | pk_rim_vouch |  | fid |
