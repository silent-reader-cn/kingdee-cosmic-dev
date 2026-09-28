# 方案模板映射配置-cvp_plan_config

## 方案模板映射配置-主表 t_cvp_plan_config

- **表名称：** 方案模板映射配置-主表
- **表名：** t_cvp_plan_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftemplatenumber | 模板ID | int8 | 64 |  | √ | 0 | 模板ID |
| 3 | ftemplateconfig | 模板配置 | text | 0 |  |  | ' ' | 模板配置 |
| 4 | fplannumber | 方案ID | int8 | 64 |  | √ | 0 | 方案ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cvp_plan_config_template |  | ftemplatenumber |
| 2 | idx_cvp_plan_config_paln |  | fplannumber |
| 3 | pk_t_cvp_plan_config |  | fid |
