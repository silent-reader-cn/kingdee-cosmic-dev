# 维度归因-cbi_dm_dim_attr_config

## 维度归因-主表 t_cbi_dm_dim_attr_config

- **表名称：** 维度归因-主表
- **表名：** t_cbi_dm_dim_attr_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdimensionattrlimit | 维度归因限制 | int4 | 32 |  | √ | 1000 | 维度归因限制 |
| 3 | fdatamodelid | 基础资料 | int8 | 64 |  | √ | 0 | [指标模型 cbi_agent_datamodel](../chatbi_files/cbi_agent_datamodel.md) |
| 4 | fexcludeddimension_tag | 排除维度_详情 | text | 0 |  |  | null | 排除维度_详情 |
| 5 | fdimensionvalue | 维度值 ≤ | bpchar | 1 |  | √ | '1' | 维度值 ≤ |
| 6 | fundimensionvalue | 排除部分维度 | bpchar | 1 |  | √ | '0' | 排除部分维度 |
| 7 | fexcludeddimension | 排除维度 | varchar | 10 |  | √ | ' ' | 排除维度 |
| 8 | flargeeffindicators | 指标名称 | varchar | 10 |  | √ | ' ' | 指标名称 |
| 9 | flargeeffindicators_tag | 指标名称_详情 | text | 0 |  |  | null | 指标名称_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_dm_dim_attr_config_fk |  | fdatamodelid |
| 2 | pk_cbi_dm_dim_attr_config |  | fid |
