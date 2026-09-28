# 异步中间表监控-open_asyncdata

## 异步中间表监控-主表 t_openapi_asyncdata

- **表名称：** 异步中间表监控-主表
- **表名：** t_openapi_asyncdata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 异步请求ID | int8 | 64 |  | √ | 0 | 异步请求ID |
| 2 | fstatus | 执行状态 | int4 | 32 |  | √ | 0 | 执行状态,枚举: 302 :302-处理完成 202 :202-已接收 404 :404-NotFound |
| 3 | ftraceid | traceID | varchar | 32 |  | √ | ' ' | traceID |
| 4 | ferrmsg | 错误信息 | varchar | 2000 |  | √ | ' ' | 错误信息 |
| 5 | foutstatus | 处理结果 | bpchar | 1 |  | √ | '2' | 处理结果,枚举: 0 :失败 1 :成功 2 :未执行 |
| 6 | fcreatetime | 入队时间 | timestamp | 0 |  |  | null | 入队时间 |
| 7 | fapiid | APIID | int8 | 64 |  | √ | 0 | APIID |
| 8 | finputpara | finputpara | text | 0 |  |  | ' ' |  |
| 9 | foutputpara | foutputpara | text | 0 |  |  | ' ' |  |
| 10 | furl | URL | varchar | 200 |  | √ | ' ' | URL |
| 11 | fstarttime | 异步处理开始时间 | timestamp | 0 |  |  | null | 异步处理开始时间 |
| 12 | fmodifytime | 异步处理结束时间 | timestamp | 0 |  |  | null | 异步处理结束时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_async_creatrtime |  | fcreatetime |
| 2 | pk_t_openapi_asyncdata |  | fid |
