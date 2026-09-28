# 单据状态转换流水记录表-dhc_billstatusdetail

## 单据状态转换流水记录表-主表 t_dhc_billstatusdetail

- **表名称：** 单据状态转换流水记录表-主表
- **表名：** t_dhc_billstatusdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmessage | 处理意见 | varchar | 36 |  | √ | ' ' | 处理意见 |
| 3 | fcreatetime | 记录创建日期 | timestamp | 0 |  |  | null | 记录创建日期 |
| 4 | fopertime | 节点操作时间 | varchar | 36 |  | √ | ' ' | 节点操作时间 |
| 5 | fexecutionid | 节点操作ID | int8 | 64 |  | √ | 0 | 节点操作ID |
| 6 | fbillid | 单据ID | varchar | 36 |  | √ | ' ' | 单据ID |
| 7 | fnodestatus | 节点状态 | varchar | 18 |  | √ | ' ' | 节点状态 |
| 8 | fuserid | 操作用户ID | int8 | 64 |  | √ | 0 | 操作用户ID |
| 9 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 10 | fassignee | 操作人名称 | varchar | 36 |  | √ | ' ' | 操作人名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_dhc_billstatusdetail_pkey |  | fid |
| 2 | idx_dhc_blstadetail_blid |  | fbillid |
