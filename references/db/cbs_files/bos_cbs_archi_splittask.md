# 归档切分任务-bos_cbs_archi_splittask

## 归档切分任务-主表 t_cbs_archi_splittask

- **表名称：** 归档切分任务-主表
- **表名：** t_cbs_archi_splittask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpagenum | 页标 | int8 | 64 |  | √ | 0 | 页标 |
| 3 | findex | 分片下标 | int8 | 64 |  | √ | 0 | 分片下标 |
| 4 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | ftailpk | 页尾 | varchar | 50 |  | √ | ' ' | 页尾 |
| 6 | fentitynumber | 表单编码 | varchar | 50 |  | √ | ' ' | 表单编码 |
| 7 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 8 | fstarttime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 9 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 10 | ftasknode | 任务节点 | varchar | 100 |  | √ | ' ' | 任务节点,枚举: pkinsert :pk数据生成 datamove :同库迁移 crossmove :跨库迁移 dataclean :数据清理 tempclean :临时数据清理 |
| 11 | fheadpk | 页头 | varchar | 50 |  | √ | ' ' | 页头 |
| 12 | fprogresssign | 进度标记 | text | 0 |  |  | null | 进度标记 |
| 13 | ftaskstatus | 任务状态 | bpchar | 1 |  | √ | ' ' | 任务状态 |
| 14 | fpagesize | 页长 | int8 | 64 |  | √ | 0 | 页长 |
| 15 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 16 | ftaskid | 主任务id | int8 | 64 |  | √ | 0 | 主任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_splittask |  | fentitynumber |
| 2 | pk_cbs_archi_splittask |  | fid |
| 3 | idx_cbs_archi_splittask_tid |  | ftaskid |
