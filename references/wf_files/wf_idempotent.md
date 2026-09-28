# 外部接口执行幂等性-wf_idempotent

## 外部接口执行幂等性-主表 t_wf_idempotent

- **表名称：** 外部接口执行幂等性-主表
- **表名：** t_wf_idempotent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factinstid | 活动实例ID | int8 | 64 |  | √ | 0 | 活动实例ID |
| 3 | fresult | 执行结果 | text | 0 |  |  | null | 执行结果 |
| 4 | factivityid | 节点ID | varchar | 255 |  | √ | ' ' | 节点ID |
| 5 | flog | 日志信息 | text | 0 |  |  | null | 日志信息 |
| 6 | fvalue | 执行内容 | varchar | 255 |  | √ | ' ' | 执行内容 |
| 7 | fstate | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: successed :成功 failed :失败 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: process :流程 event :事件 |
| 10 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | finstanceid | 实例ID | int8 | 64 |  | √ | 0 | 实例ID |
| 12 | fbusinesskey | 单据ID | varchar | 36 |  | √ | ' ' | 单据ID |
| 13 | fscene | 场景 | varchar | 100 |  | √ | ' ' | 场景 |
| 14 | fxid | xid | varchar | 80 |  | √ | ' ' | xid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_idempotent |  | fxid |
| 2 | t_wf_idempotent_pkey |  | fid |
| 3 | idx_wf_idempotent_instid |  | finstanceid |
| 4 | idx_wf_idempotent_buskey |  | fbusinesskey,factinstid |
