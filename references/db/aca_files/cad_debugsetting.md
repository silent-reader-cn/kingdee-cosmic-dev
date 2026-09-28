# 成本模块调试开关-cad_debugsetting

## 成本模块调试开关-主表 t_cad_debugsetting

- **表名称：** 成本模块调试开关-主表
- **表名：** t_cad_debugsetting

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fisenable | 启用调试 | bpchar | 1 |  | √ | '0' | 启用调试 |
| 4 | flogmod | 日志模式 | varchar | 10 |  | √ | ' A' | 日志模式,枚举: A :日志 B :数据库 |
| 5 | fmod | 功能标识 | varchar | 255 |  | √ | ' ' | 功能标识 |
| 6 | fkeyword | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cad_debugsetting |  | fid |
| 2 | idx_t_cad_debugsetting |  | fmod |
