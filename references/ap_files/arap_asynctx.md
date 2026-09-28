# 异步任务-arap_asynctx

## 异步任务-主表 t_arap_asynctx

- **表名称：** 异步任务-主表
- **表名：** t_arap_asynctx

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecuteclass | 事务消费程序 | varchar | 200 |  | √ | ' ' | 事务消费程序 |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fparams | 事务参数 | varchar | 510 |  | √ | ' ' | 事务参数 |
| 5 | fbizid | 分组事务ID | varchar | 50 |  | √ | ' ' | 分组事务ID |
| 6 | fexecutetimes | 执行次数 | int8 | 64 |  | √ | 0 | 执行次数 |
| 7 | fstate | 运行状态 | varchar | 30 |  | √ | ' ' | 运行状态,枚举: running :MQ运行中 err :错误 success :运行成功 |
| 8 | fparams_tag | 事务参数_详情 | text | 0 |  |  | null | 事务参数_详情 |
| 9 | fgroup | 事务分组 | varchar | 50 |  | √ | ' ' | 事务分组 |
| 10 | ferrormessage | 错误信息 | varchar | 510 |  | √ | ' ' | 错误信息 |
| 11 | faction | 业务动作 | varchar | 50 |  | √ | ' ' | 业务动作 |
| 12 | ftask | 子任务 | varchar | 50 |  | √ | ' ' | 子任务 |
| 13 | ferrormessage_tag | 错误信息_详情 | text | 0 |  |  | null | 错误信息_详情 |
| 14 | fxid | fxid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_arap_asynctx_pkey |  | fid |
| 2 | idx_arap_tx_xid |  | fxid |
