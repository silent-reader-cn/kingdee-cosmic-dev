# 系统参数-dcsplat_keyparams

## 系统参数-主表 t_dcsplat_keyparams

- **表名称：** 系统参数-主表
- **表名：** t_dcsplat_keyparams

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvalue | 值 | varchar | 1000 |  | √ | ' ' | 值 |
| 3 | fkey | 键 | varchar | 255 |  | √ | ' ' | 键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_dcsplat_keyparams |  | fid |
| 2 | idx_dcsplat_params_key |  | fkey |
