# 运维中心执行实例信息收集-wf_evtinstance_statistics

## 运维中心执行实例信息收集-主表 t_wf_evtinstancecollect

- **表名称：** 运维中心执行实例信息收集-主表
- **表名：** t_wf_evtinstancecollect

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | feventid | 事件ID | int8 | 64 |  | √ | 0 | 事件ID |
| 4 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fserviceid | 服务ID | int8 | 64 |  | √ | 0 | 服务ID |
| 6 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 7 | ftotal | 总数 | int4 | 32 |  | √ | 0 | 总数 |
| 8 | fsubscriptionid | 订阅ID | int8 | 64 |  | √ | 0 | 订阅ID |

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
