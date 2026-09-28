# 挂起工作-wf_suspendedjob

## 挂起工作-主表 t_wf_suspendedjob

- **表名称：** 挂起工作-主表
- **表名：** t_wf_suspendedjob

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexceptionmsg | 异常信息 | text | 0 |  |  | null | 异常信息 |
| 3 | fhandlercfg | 处理配置 | text | 0 |  |  | null | 处理配置 |
| 4 | frepeat | 重复 | varchar | 255 |  | √ | ' ' | 重复 |
| 5 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 6 | fhandlertype | 处理类型 | varchar | 30 |  | √ | ' ' | 处理类型 |
| 7 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 8 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 9 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 10 | felementid | 异常元素 | varchar | 80 |  | √ | ' ' | 异常元素 |
| 11 | fisactive | 是否存活 | bpchar | 1 |  | √ | '1' | 是否存活 |
| 12 | fretries | 重试次数 | int8 | 64 |  | √ | 3 | 重试次数 |
| 13 | fduedate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 14 | fsrcjobid | 发起job | int8 | 64 |  | √ | 0 | 发起job |
| 15 | fexclusive | 是否排他 | bpchar | 1 |  | √ | '0' | 是否排他 |
| 16 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | froottraceno | 根trace | varchar | 100 |  | √ | ' ' | 根trace |
| 18 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 19 | fprocessinstanceid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 20 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 21 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 22 | foperation | 操作 | varchar | 300 |  | √ | ' ' | 操作 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_suspendjob_procdef |  | fprocdefid |
| 2 | idx_wf_suspendjob_process |  | fprocessinstanceid |
| 3 | t_wf_suspendedjob_pkey |  | fid |
| 4 | idx_wf_suspendjob_execution |  | fexecutionid |
