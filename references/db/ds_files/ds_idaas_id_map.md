# 苍穹与玉符人员ID映射-ds_idaas_id_map

## 苍穹与玉符人员ID映射-主表 t_ds_idaas_id_map

- **表名称：** 苍穹与玉符人员ID映射-主表
- **表名：** t_ds_idaas_id_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fidaaspersonid | 玉符人员id | varchar | 100 |  | √ | ' ' | 玉符人员id |
| 3 | ferppersonid | 苍穹人员id | int8 | 64 |  | √ | 0 | 苍穹人员id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ds_idaas_id_map |  | fid |
| 2 | idx_t_ds_idaas_id_map |  | ferppersonid |
