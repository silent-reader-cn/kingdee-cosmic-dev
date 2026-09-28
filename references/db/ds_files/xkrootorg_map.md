# 根组织ID映射-xkrootorg_map

## 根组织ID映射-主表 t_xkrootorg_map

- **表名称：** 根组织ID映射-主表
- **表名：** t_xkrootorg_map

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkqyrootorgid | 企业版根组织ID | varchar | 50 |  | √ | ' ' | 企业版根组织ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_xkrootorg_map_orgid |  | fxkqyrootorgid |
| 2 | pk_t_xkrootorg_map |  | fid |
