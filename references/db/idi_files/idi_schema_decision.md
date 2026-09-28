# 决策方案检查项-idi_schema_decision

## 决策方案检查项-主表 t_idi_schema_decision

- **表名称：** 决策方案检查项-主表
- **表名：** t_idi_schema_decision

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fschema_num | 方案编码 | varchar | 80 |  | √ | ' ' | 方案编码 |
| 3 | fdecision_num | 检查项编码 | varchar | 80 |  | √ | ' ' | 检查项编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_idi_schema_decision |  | fid |
| 2 | idx_idi_schema_decision_dn |  | fdecision_num |
| 3 | idx_idi_schema_decision_sn |  | fschema_num |
