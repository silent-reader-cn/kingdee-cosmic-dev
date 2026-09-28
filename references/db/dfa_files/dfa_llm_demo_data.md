# 财务LLM演示数据-dfa_llm_demo_data

## 财务LLM演示数据-主表 t_dfa_llm_demo_data

- **表名称：** 财务LLM演示数据-主表
- **表名：** t_dfa_llm_demo_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreaterfield | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fdemo_data_tag | 演示数据_详情 | text | 0 |  |  | null | 演示数据_详情 |
| 5 | fcreatedatefield | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdesc | 说明 | varchar | 50 |  | √ | ' ' | 说明 |
| 7 | fdata_key | 数据key | varchar | 50 |  | √ | ' ' | 数据key |
| 8 | fenabled | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用 |
| 9 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fdemo_data | 演示数据 | varchar | 500 |  | √ | ' ' | 演示数据 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_llm_demo_data |  | fid |
| 2 | idxt_dfa_llm_demo_data |  | fdata_key |
