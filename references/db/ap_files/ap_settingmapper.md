# 映射关系-ap_settingmapper

## 映射关系-主表 t_ap_settingmapper

- **表名称：** 映射关系-主表
- **表名：** t_ap_settingmapper

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 值 | varchar | 255 |  | √ | ' ' | 值 |
| 3 | ftype | 映射类型 | varchar | 50 |  | √ | ' ' | 映射类型 |
| 4 | fkey | 键 | varchar | 100 |  | √ | ' ' | 键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ap_settingmapper_pkey |  | fid |
| 2 | idx_ap_mapper_type |  | ftype |
