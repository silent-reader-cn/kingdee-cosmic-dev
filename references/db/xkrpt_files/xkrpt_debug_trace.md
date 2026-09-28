# 调试日志统一管控-xkrpt_debug_trace

## 调试日志统一管控-主表 t_bd_debugtrace

- **表名称：** 调试日志统一管控-主表
- **表名：** t_bd_debugtrace

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappnumber | 应用编码 | varchar | 50 |  | √ | ' ' | 应用编码 |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fexpireddate | 过期时间 | timestamp | 0 |  |  | null | 过期时间 |
| 6 | fformnumber | 表单编码 | varchar | 50 |  | √ | ' ' | 表单编码 |
| 7 | faction | 操作标识 | varchar | 50 |  | √ | ' ' | 操作标识 |
| 8 | fclienttype | 客户端类型 | varchar | 50 |  | √ | ' ' | 客户端类型,枚举: web :web界面请求 webservice :webservice api :api mobile :移动端 batch :后台批处理程序 workflow :工作流驱动 chat :聊天程序驱动 TRIPSI :后台批处理程序 MQ :MQ消息处理 |
| 9 | frequesttimes | 请求次数 | int4 | 32 |  | √ | 0 | 请求次数 |
| 10 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_debugtrace |  | fid |
| 2 | idx_bd_debugtrace |  | fformnumber |
