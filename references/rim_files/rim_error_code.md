# 错误代码定义-rim_error_code

## 错误代码定义-主表 t_rim_error_code

- **表名称：** 错误代码定义-主表
- **表名：** t_rim_error_code

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frim_desc | 自定义描述 | varchar | 150 |  | √ | ' ' | 自定义描述 |
| 3 | fout_desc | 外部系统错误描述 | varchar | 150 |  | √ | ' ' | 外部系统错误描述 |
| 4 | fcreate_time | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | finterface | 接口类型 | varchar | 50 |  | √ | ' ' | 接口类型,枚举: check :发票查验 |
| 7 | frim_code | 自定义编码 | varchar | 30 |  | √ | ' ' | 自定义编码 |
| 8 | fout_code | 外部系统错误代码 | varchar | 30 |  | √ | ' ' | 外部系统错误代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_rim_error_code |  | finterface,fout_code |
| 2 | pk_rim_error_code |  | fid |
