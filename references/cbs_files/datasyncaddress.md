# 目标地址管理-datasyncaddress

## 目标地址管理-主表 t_dts_datasyncaddress

- **表名称：** 目标地址管理-主表
- **表名：** t_dts_datasyncaddress

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faddressproperties | 连接属性 | varchar | 1000 |  | √ | ' ' | 连接属性 |
| 3 | fregion | 目标名称 | varchar | 100 |  | √ | ' ' | 目标名称 |
| 4 | fdestinationtype | 目标类型 | varchar | 100 |  | √ | ' ' | 目标类型,枚举: fulltext :全文索引(elasticsearch) mongdb :mongodb |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dts_datasyncaddress |  | fregion |
| 2 | t_dts_datasyncaddress_pkey |  | fid |
