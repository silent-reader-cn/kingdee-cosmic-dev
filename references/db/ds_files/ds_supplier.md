# 供应商-ds_supplier

## 供应商-主表 t_ds_supplier

- **表名称：** 供应商-主表
- **表名：** t_ds_supplier

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 20 |  | √ | ' ' | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fssid | 来源系统 | int8 | 64 |  | √ | 0 | 来源系统 ds_srcsys |
| 4 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 5 | fsoid | 来源对象ID | varchar | 100 |  | √ | ' ' | 来源对象ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ds_supplier_pkey |  | fid |
| 2 | idx_ds_supplier_key |  | fssid,fsoid |
