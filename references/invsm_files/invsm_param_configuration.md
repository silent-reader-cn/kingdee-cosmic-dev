# 参数配置单据-invsm_param_configuration

## 参数配置单据-主表 t_invsm_param_config

- **表名称：** 参数配置单据-主表
- **表名：** t_invsm_param_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fconfig_value | 配置项值 | varchar | 1024 |  | √ | ' ' | 配置项值 |
| 3 | fconfig_type | 配置项类型 | varchar | 50 |  | √ | ' ' | 配置项类型 |
| 4 | fconfigdescription | 配置项描述 | varchar | 500 |  | √ | ' ' | 配置项描述 |
| 5 | fconfig_key | 配置项key | varchar | 50 |  | √ | ' ' | 配置项key |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invsm_param_config |  | fconfig_type,fconfig_key |
| 2 | pk_invsm_param_config |  | fid |
