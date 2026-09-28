# 底稿风险事项单-bdtaxr_draft_risk

## 底稿风险事项单-主表 t_bdtaxr_draft_risk

- **表名称：** 底稿风险事项单-主表
- **表名：** t_bdtaxr_draft_risk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | friskresolveid | 风险处理id | int8 | 64 |  | √ | 0 | 风险处理id |
| 3 | fdraftid | 底稿id | int8 | 64 |  | √ | 0 | 底稿id |
| 4 | fitemtype | 事项类型 | varchar | 50 |  | √ | ' ' | 事项类型,枚举: 1 :申报事项 2 :风险事项 |
| 5 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fsbbid | 申报表id | int8 | 64 |  | √ | 0 | 申报表id |
| 8 | fitemname | 事项名称 | varchar | 1000 |  | √ | ' ' | 事项名称 |
| 9 | fdrafttable | 底稿元数据 | varchar | 50 |  | √ | ' ' | 底稿元数据 |
| 10 | friskdesc | 风险说明 | varchar | 2000 |  | √ | ' ' | 风险说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_draft_risk |  | fid |
| 2 | idxt_bdtaxr_draft_risk_1 |  | fdraftid |
