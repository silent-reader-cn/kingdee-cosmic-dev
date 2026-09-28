# 供应商状态排除-bd_supplierstatusexclude

## 供应商状态排除-主表 t_bd_supplierstatusexclud

- **表名称：** 供应商状态排除-主表
- **表名：** t_bd_supplierstatusexclud

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsupplierstatus | 供应商状态 | int8 | 64 |  | √ | 0 | 供应商状态 bd_supplierstatus |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_supplierstatusexclud |  | fsupplierstatus |
| 2 | pk_t_bd_supplierstatusexclud |  | fid |
