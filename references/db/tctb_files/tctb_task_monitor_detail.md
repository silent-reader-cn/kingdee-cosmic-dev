# 任务监控详情-tctb_task_monitor_detail

## 任务监控详情-主表 t_tctb_task_detail

- **表名称：** 任务监控详情-主表
- **表名：** t_tctb_task_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbatchnumber | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 3 | ftaxorg | 税务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fparentid | 父任务id | varchar | 50 |  | √ | ' ' | 父任务id |
| 5 | fexecutedetail | 执行详情 | varchar | 1000 |  | √ | ' ' | 执行详情 |
| 6 | fretry | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 7 | fprogress | 进度 | int8 | 64 |  | √ | 0 | 进度 |
| 8 | ftaskname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 9 | ftaskclassname | 任务全限定类名 | varchar | 100 |  | √ | ' ' | 任务全限定类名 |
| 10 | fexpire_time | 执行超时时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 执行超时时间 |
| 11 | fskssqq | 所属税期起 | timestamp | 0 |  |  | null | 所属税期起 |
| 12 | fstarttime | 开始运行时间 | timestamp | 0 |  |  | null | 开始运行时间 |
| 13 | fappid | 应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 14 | fstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: SCHEDULED :计划 BEGIN :运行中 COMPLETED :完成 FAILED :失败 ABORTED :终止 SKIP :跳过 TIMEOUT :超时 |
| 15 | fbusinessparams | 业务参数 | varchar | 500 |  | √ | ' ' | 业务参数 |
| 16 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 17 | fmodifydate | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |
| 18 | fskssqz | 所属税期止 | timestamp | 0 |  |  | null | 所属税期止 |
| 19 | ftaskappid | 任务appid | varchar | 50 |  | √ | ' ' | 任务appid |
| 20 | foperater | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fendtime | 结束运行时间 | timestamp | 0 |  |  | null | 结束运行时间 |
| 22 | ftaskdefine | 任务 | varchar | 36 |  | √ | ' ' | [调度执行程序 sch_taskdefine](../sys_files/sch_taskdefine.md) |
| 23 | ftaskid | 任务id | varchar | 50 |  | √ | ' ' | 任务id |
| 24 | fdispatchflag | 触发标识 | varchar | 50 |  | √ | ' ' | 触发标识,枚举: YES :已触发 NO :未触发 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tctb_task_detail |  | fid |
| 2 | idx_tctb_task_detaskid |  | ftaskid |
