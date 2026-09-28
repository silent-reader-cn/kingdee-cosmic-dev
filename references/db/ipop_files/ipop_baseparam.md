# 基础参数-ipop_baseparam

## 基础参数-主表 t_ipop_baseparam

- **表名称：** 基础参数-主表
- **表名：** t_ipop_baseparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparamvalue | 参数值 | varchar | 2000 |  | √ | ' ' | 参数值 |
| 3 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fparamkey | 参数标识 | varchar | 255 |  | √ | ' ' | 参数标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipop_baseparam |  | fparamkey |
| 2 | pk_t_ipop_baseparam |  | fid |
