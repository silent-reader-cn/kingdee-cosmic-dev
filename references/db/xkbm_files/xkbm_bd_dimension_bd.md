# 预算维度组合纵表（基础资料）-xkbm_bd_dimension_bd

## 预算维度组合纵表（基础资料）-主表 t_xkbm_bd_dimension_bd

- **表名称：** 预算维度组合纵表（基础资料）-主表
- **表名：** t_xkbm_bd_dimension_bd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 横表 | int8 | 64 |  | √ | 0 | [预算维度组合 xkbm_bd_dimension](../xkbm_files/xkbm_bd_dimension.md) |
| 2 | fvalue | 长整数 | int8 | 64 |  | √ | 0 | 长整数 |
| 3 | fflexfield | 预算类型 | varchar | 100 |  | √ | ' ' | 预算类型 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_bd_dimension_bd |  | fentryid |
| 2 | idx_xkbm_bd_dimension_bd |  | fid |
