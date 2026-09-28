# 运维中心执行实例信息收集-wf_evtinstance_statistics

## 运维中心执行实例信息收集-主表 t_wf_evtinstancecollect

- **表名称：** 运维中心执行实例信息收集-主表
- **表名：** t_wf_evtinstancecollect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcompletedduration | 完成订阅总服务耗时 | int8 | 64 |  | √ | 0 | 完成订阅总服务耗时 |
| 3 | feventid | 事件ID | int8 | 64 |  | √ | 0 | 事件ID |
| 4 | fsubscriptionid | 订阅ID | int8 | 64 |  | √ | 0 | 订阅ID |
| 5 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcompletedtotal | 完成订阅数 | int4 | 32 |  | √ | 0 | 完成订阅数 |
| 8 | fserviceid | 服务ID | int8 | 64 |  | √ | 0 | 服务ID |
| 9 | ferroredtotal | 异常订阅数 | int4 | 32 |  | √ | 0 | 异常订阅数 |
| 10 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 11 | ftotal | 总数 | int4 | 32 |  | √ | 0 | 总数 |
| 12 | fsubfullduration | 完成订阅总耗时 | int8 | 64 |  | √ | 0 | 完成订阅总耗时 |
| 13 | fovertimeconfig | 超时策略配置 | varchar | 500 |  | √ | ' ' | 超时策略配置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_evtinstancecollect |  | fid |
| 2 | idx_wf_evtinstcollect_credate |  | fcreatedate |
| 3 | idx_wf_evtinstcollect_number |  | fnumber |
