# 出库核算任务-cal_task

## 出库核算任务-主表 t_cal_task

- **表名称：** 出库核算任务-主表
- **表名：** t_cal_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 子任务名称 | varchar | 255 |  | √ | ' ' | 子任务名称 |
| 3 | ftimes | 重试次数 | int4 | 32 |  | √ | 0 | 重试次数 |
| 4 | fismaintask | 主任务 | bpchar | 1 |  | √ | '1' | 主任务 |
| 5 | ftasktype | 任务类型 | bpchar | 1 |  | √ | 'A' | 任务类型,枚举: A :出库核算 B :关账 C :结账 |
| 6 | fresultparams | 结果参数 | varchar | 80 |  | √ | ' ' | 结果参数 |
| 7 | fparams | 参数 | varchar | 80 |  | √ | ' ' | 参数 |
| 8 | fprogress | 进度 | int8 | 64 |  | √ | 0 | 进度展示 cal_progress |
| 9 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 10 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :完成 B :运行中 C :等待 D :失败 E :关闭 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | frunat | 执行服务器 | varchar | 80 |  | √ | ' ' | 执行服务器 |
| 13 | fcalnumber | 计算任务号 | varchar | 80 |  | √ | ' ' | 计算任务号 |
| 14 | fqueryschemeid | 查询方案 | int8 | 64 |  | √ | 0 | 查询方案 cal_query_scheme |
| 15 | fparams_tag | 参数_详情 | text | 0 |  |  | null | 参数_详情 |
| 16 | fresultparams_tag | 结果参数_详情 | text | 0 |  |  | null | 结果参数_详情 |
| 17 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 18 | ftaskid | 调度任务 | int8 | 64 |  | √ | 0 | 调度任务 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_task |  | fid |
| 2 | idx_cal_task_task |  | ftaskid |
| 3 | idx_cal_task_stime |  | fstarttime |
| 4 | idx_cal_task_calnum |  | fcalnumber |
