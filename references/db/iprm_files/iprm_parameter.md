# 云内容参数管理-iprm_parameter

## 云内容参数管理-主表 t_iprm_parameter

- **表名称：** 云内容参数管理-主表
- **表名：** t_iprm_parameter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparamvalue | 参数值 | varchar | 255 |  | √ | ' ' | 参数值 |
| 3 | fparamkey | 参数键 | varchar | 50 |  | √ | ' ' | 参数键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iprm_parameter |  | fid |
| 2 | idx_iprm_parameter |  | fparamkey |
