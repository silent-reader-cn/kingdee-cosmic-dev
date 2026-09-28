# 调度任务-bos_cbs_archi_task

## 调度任务-主表 t_cbs_archi_task

- **表名称：** 调度任务-主表
- **表名：** t_cbs_archi_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frunnode | 执行节点信息 | varchar | 200 |  | √ | ' ' | 执行节点信息 |
| 3 | fhost | 任务执行ip | varchar | 50 |  | √ | ' ' | 任务执行ip |
| 4 | ftasktype | 任务类型 | varchar | 100 |  | √ | ' ' | 任务类型,枚举: archive :归档转储 unarchive :反归档 datasync :数据同步 dataclean :归档清除 archivesync :归档同步 |
| 5 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 6 | fprogress | 迁移进度 | varchar | 2000 |  | √ | ' ' | 迁移进度 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fruninstance | 执行节点instance | varchar | 50 |  | √ | ' ' | 执行节点instance |
| 9 | fprepk | 前任务同步记录pk | varchar | 50 |  | √ | ' ' | 前任务同步记录pk |
| 10 | fprogresssign | 进度标记 | text | 0 |  |  | null | 进度标记 |
| 11 | ftaskstatus | 任务状态 | bpchar | 1 |  | √ | ' ' | 任务状态,枚举: 0 :等待 1 :执行中 2 :成功 3 :失败 4 :已终止 5 :暂停中 6 :已暂停 7 :级联等待 |
| 12 | fpendingcount | 待迁移数据量 | int8 | 64 |  | √ | 0 | 待迁移数据量 |
| 13 | fparentid | 父任务id | int8 | 64 |  | √ | 0 | 父任务id |
| 14 | fprogressdesc | 进度描述 | varchar | 2000 |  | √ | ' ' | 进度描述 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | findex | findex | int8 | 64 |  | √ | 0 |  |
| 17 | frunhost | 执行节点ip | varchar | 50 |  | √ | ' ' | 执行节点ip |
| 18 | fstarttime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 19 | ftasknode | 任务节点 | varchar | 100 |  | √ | ' ' | 任务节点,枚举: tbstructchk :结构迁移 pkinsert :pk数据生成 datamove :同库迁移 crossmove :跨库迁移 tempclean :临时数据清理 datamigrate :数据迁移 taskend :任务结束 taskstart :任务开始 cascadebarrier :级联等待 dataclean :数据清除 syncmove :同步迁移 |
| 20 | fschedulercdid | fschedulercdid | int8 | 64 |  | √ | 0 |  |
| 21 | fscheduleid | 调度id | int8 | 64 |  | √ | 0 | 调度id |
| 22 | fconfigid | 归档配置id | int8 | 64 |  | √ | 0 | 归档配置id |
| 23 | fretrytimes | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 24 | fbarriercount | 子级任务数 | int8 | 64 |  | √ | 0 | 子级任务数 |
| 25 | frootid | 根任务id | int8 | 64 |  | √ | 0 | 根任务id |
| 26 | fbatchnum | 调度任务号 | varchar | 50 |  | √ | ' ' | 调度任务号 |
| 27 | flastretrytime | 上一次执行重试的时间 | timestamp | 0 |  |  | null | 上一次执行重试的时间 |
| 28 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 29 | ftotalcount | 迁移数据量 | int8 | 64 |  | √ | 0 | 迁移数据量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_task |  | fentitynumber |
| 2 | idx_cbs_archi_task_cid |  | fconfigid |
| 3 | pk_cbs_archi_task |  | fid |
