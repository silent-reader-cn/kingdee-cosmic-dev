# 钉钉待办-wf_msg_dingtodo

## 钉钉待办-主表 t_wf_dingtodo

- **表名称：** 钉钉待办-主表
- **表名：** t_wf_dingtodo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftodoresult | 待办处理结果 | varchar | 100 |  | √ | ' ' | 待办处理结果 |
| 3 | fdprocinstid | 钉钉实例ID | varchar | 200 |  | √ | ' ' | 钉钉实例ID |
| 4 | fuserid | 用户ID | int8 | 64 |  | √ | 0 | 用户ID |
| 5 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 6 | ftodoreties | 待办重试次数 | int8 | 64 |  | √ | 0 | 待办重试次数 |
| 7 | ftodostate | 钉钉待办状态 | varchar | 100 |  | √ | ' ' | 钉钉待办状态 |
| 8 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdtplid | 钉钉模板ID | varchar | 200 |  | √ | ' ' | 钉钉模板ID |
| 11 | finststate | 钉实例状态 | varchar | 100 |  | √ | ' ' | 钉实例状态 |
| 12 | finstreslut | 实例处理结果 | varchar | 100 |  | √ | ' ' | 实例处理结果 |
| 13 | finstretries | 实例重试次数 | int8 | 64 |  | √ | 0 | 实例重试次数 |
| 14 | fdtodoid | 钉钉待办ID | varchar | 200 |  | √ | ' ' | 钉钉待办ID |
| 15 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_dingtodo_pkey |  | fid |
| 2 | idx_wf_dingtodo |  | ftaskid,fdtodoid |
