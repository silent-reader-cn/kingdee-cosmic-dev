# 清理结算垃圾数据设置-ism_cleardirtyset

## 清理结算垃圾数据设置-主表 t_ism_cleardirtyset

- **表名称：** 清理结算垃圾数据设置-主表
- **表名：** t_ism_cleardirtyset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatekey | 日期字段标识 | varchar | 50 |  | √ | ' ' | 日期字段标识 |
| 3 | ftimeunit | 时间单位 | varchar | 20 |  | √ | ' ' | 时间单位,枚举: D :天 H :小时 M :分钟 S :秒 |
| 4 | fentitykey | 实体标识 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 5 | fdifftimes | 时间间隔 | int4 | 32 |  | √ | 0 | 时间间隔 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ism_cleardirtyset |  | fentitykey |
| 2 | pk_ism_cleardirtyset |  | fid |
