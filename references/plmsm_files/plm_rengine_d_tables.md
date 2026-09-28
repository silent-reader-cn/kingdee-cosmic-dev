# 决策表-plm_rengine_d_tables

## 决策表-主表 t_plm_egn_decisiontable

- **表名称：** 决策表-主表
- **表名：** t_plm_egn_decisiontable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftablebody | 规则 | text | 0 |  |  | null | 规则 |
| 3 | ftablehead | 参数 | text | 0 |  |  | null | 参数 |
| 4 | fpolicyid | 所属策略 | int8 | 64 |  | √ | 0 | 策略管理 plm_rengine_policy |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_egn_decisiontable |  | fid |
| 2 | idx_plm_deci_policy |  | fpolicyid |
