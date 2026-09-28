# 云之家组织ID映射表-ds_yzj_id_mapping

## 云之家组织ID映射表-主表 t_ds_yzj_id_mapping

- **表名称：** 云之家组织ID映射表-主表
- **表名：** t_ds_yzj_id_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 22 |  | √ | ' ' | id |
| 2 | fcreated_time | 时间戳（服务器时间） | int8 | 64 |  | √ | 0 | 时间戳（服务器时间） |
| 3 | fyzj_org_name | 云之家组织长名称 | varchar | 255 |  | √ | ' ' | 云之家组织长名称 |
| 4 | fierp_orgid | 苍穹组织ID | varchar | 255 |  | √ | ' ' | 苍穹组织ID |
| 5 | fyzj_orgid | 云之家组织ID | varchar | 255 |  | √ | ' ' | 云之家组织ID |
| 6 | fierp_org_name | 苍穹组织长名称 | varchar | 255 |  | √ | ' ' | 苍穹组织长名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ds_yzj_id_mapping_t |  | fyzj_orgid |
| 2 | t_ds_yzj_id_mapping_c |  | fcreated_time |
| 3 | t_ds_yzj_id_mapping_s |  | fierp_orgid |
| 4 | pk_t_ds_yzj_id_mapping |  | fid |
