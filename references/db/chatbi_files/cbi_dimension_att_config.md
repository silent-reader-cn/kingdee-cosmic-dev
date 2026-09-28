# 维度归因配置-cbi_dimension_att_config

## 维度归因配置-主表 t_cbi_dimen_att_config

- **表名称：** 维度归因配置-主表
- **表名：** t_cbi_dimen_att_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatasetid | 基础资料 | int8 | 64 |  | √ | 0 | [数据集 gai_cbi_dataset](../chatbi_files/gai_cbi_dataset.md) |
| 3 | fundimension | 多选下拉列表1 | varchar | 2000 |  | √ | ' ' | 多选下拉列表1,枚举: |
| 4 | fischeckdimension2 | fischeckdimension2 | bpchar | 1 |  | √ | '0' |  |
| 5 | fdimensionnumber | 文本 | varchar | 50 |  | √ | ' ' | 文本 |
| 6 | flargetextfield_tag | flargetextfield_tag | text | 0 |  |  | null |  |
| 7 | fdimensionvalue | 维度值≤ | bpchar | 1 |  | √ | '0' | 维度值≤ |
| 8 | fundimensionvalue | 排除部分维度 | bpchar | 1 |  | √ | '0' | 排除部分维度 |
| 9 | fischeckdimension | 复选框3 | bpchar | 1 |  | √ | '0' | 复选框3 |
| 10 | feffindicators | 多选下拉列表 | varchar | 2000 |  | √ | ' ' | 多选下拉列表,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_dimen_att_config |  | fid |
| 2 | idx_t_cbi_dimen_att_config_fd |  | fdatasetid |
