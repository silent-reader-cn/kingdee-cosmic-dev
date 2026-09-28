# 预算维度组合-xkbm_bd_dimension

## 预算维度组合-主表 t_xkbm_bd_dimension

- **表名称：** 预算维度组合-主表
- **表名：** t_xkbm_bd_dimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 预算维度 | varchar | 2000 |  | √ | ' ' | 预算维度 |
| 3 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_xkbm_bd_dimension |  | fid |
| 2 | idx_xkbm_bd_dimension_fid |  | fcreatetime |
