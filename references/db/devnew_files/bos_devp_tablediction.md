# 数据表字典-bos_devp_tablediction

## 数据表字典-主表 t_meta_tablediction

- **表名称：** 数据表字典-主表
- **表名：** t_meta_tablediction

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fmainentityid | 主实体 | varchar | 36 |  | √ | ' ' | [实体元数据 bos_entitymeta](../mdl_files/bos_entitymeta.md) |
| 3 | ftablename | 表名 | varchar | 64 |  | √ | ' ' | 表名 |
| 4 | fdata | fdata | text | 0 |  |  | null |  |
| 5 | fappid | fappid | varchar | 36 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_meta_tabledict_ftbname |  | ftablename |
| 2 | idx_meta_tabledict_fentity |  | fmainentityid |
| 3 | pk_t_meta_tablediction |  | fid |
