# 集成云环境变量-isc_env_variable

## 集成云环境变量-主表 t_isc_evn_variable

- **表名称：** 集成云环境变量-主表
- **表名：** t_isc_evn_variable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fvalue | 变量值 | varchar | 250 |  | √ | ' ' | 变量值 |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | ftype | 类型 | int8 | 64 |  | √ | 0 | 数据类型 - 简单值 isc_type_simple_value |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 10 | fdescription | 描述 | varchar | 250 |  | √ | ' ' | 描述 |
| 11 | fis_array | 是否数组 | bpchar | 1 |  | √ | ' ' | 是否数组 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_evn_variable |  | fid |
| 2 | idx_evn_modi_time |  | fmodifydate |
| 3 | idx_evn_number |  | fnumber |
