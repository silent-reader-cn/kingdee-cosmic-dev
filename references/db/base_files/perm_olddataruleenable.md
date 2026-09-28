# 旧数据规则启用开关-perm_olddataruleenable

## 旧数据规则启用开关-主表 t_perm_olddataruleenable

- **表名称：** 旧数据规则启用开关-主表
- **表名：** t_perm_olddataruleenable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fenable | 启用旧数据规则 | bpchar | 1 |  | √ | '1' | 启用旧数据规则 |
| 4 | fispropcollapse | 启用属性压缩 | bpchar | 1 |  | √ | '0' | 启用属性压缩 |
| 5 | fisnewmodel | 启用新模型 | bpchar | 1 |  | √ | '0' | 启用新模型 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_perm_olddataruleenable |  | fmodifierid |
| 2 | t_perm_olddataruleenable_pkey |  | fid |
