# 财务基础版本控制-bd_versioncontrol

## 财务基础版本控制-主表 t_bd_finversioncontrol

- **表名称：** 财务基础版本控制-主表
- **表名：** t_bd_finversioncontrol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvno | 版本号 | int4 | 32 |  | √ | 0 | 版本号 |
| 3 | fnumber | 业务标识 | varchar | 50 |  | √ | ' ' | 业务标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_finvcontrol_number |  | fnumber |
| 2 | pk_bd_finversioncontrol |  | fid |
