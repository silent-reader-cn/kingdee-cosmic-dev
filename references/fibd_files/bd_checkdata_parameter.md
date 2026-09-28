# 数据检查参数-bd_checkdata_parameter

## 数据检查参数-主表 t_bd_checkdata_parameter

- **表名称：** 数据检查参数-主表
- **表名：** t_bd_checkdata_parameter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fphone | 通知电话号 | varchar | 30 |  | √ | ' ' | 通知电话号 |
| 3 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 4 | fstoptime | 停止时间(整数值) | int4 | 32 |  | √ | 5 | 停止时间(整数值) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_checkdata_parameter |  | fid |
| 2 | idx_bd_checkdata_parameter |  | fphone |
