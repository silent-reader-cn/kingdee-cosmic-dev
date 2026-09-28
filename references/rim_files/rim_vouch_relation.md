# 凭证关系-rim_vouch_relation

## 凭证关系-主表 t_rim_vouch_relation

- **表名称：** 凭证关系-主表
- **表名：** t_rim_vouch_relation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvouch_id | 凭证id | varchar | 50 |  | √ | ' ' | 凭证id |
| 3 | fbill_type | 单据类型 | varchar | 10 |  | √ | ' ' | 单据类型,枚举: 1 :报销单 2 :发票 |
| 4 | fbill_id | 单据id | varchar | 50 |  | √ | ' ' | 单据id |
| 5 | faccount_time | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 6 | fvouch_no | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 7 | fresource | 凭证来源 | varchar | 50 |  | √ | ' ' | 凭证来源,枚举: 1 :全票池维护 2 :苍穹 9 :第三方系统 |
| 8 | faccount_date | 会计属期 | timestamp | 0 |  |  | null | 会计属期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_vouch_relation |  | fbill_type,fvouch_id |
| 2 | pk_rim_vouch_relation |  | fid |
