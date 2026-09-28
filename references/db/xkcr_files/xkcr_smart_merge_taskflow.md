# 自动合并执行-xkcr_smart_merge_taskflow

## 自动合并执行-主表 t_xkcr_sm_taskflow

- **表名称：** 自动合并执行-主表
- **表名：** t_xkcr_sm_taskflow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fflowendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 6 | fflowstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fflowstatus | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: 0 :未执行 1 :执行中 2 :部分成功 3 :成功 4 :失败 5 :手动终止 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsmartmergeplan | 自动合并方案 | int8 | 64 |  | √ | 0 | [自动合并方案 xkcr_smart_merge_plan](../xkcr_files/xkcr_smart_merge_plan.md) |
| 11 | fyear | 年 | int4 | 32 |  | √ | 0 | 年 |
| 12 | fflowname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 13 | fperiod | 期间 | int4 | 32 |  | √ | 0 | 期间 |
| 14 | fbillno | 执行编号 | varchar | 50 |  | √ | ' ' | 执行编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkcr_sm_taskflow_syp |  | fsmartmergeplan,fyear,fperiod |
| 2 | pk_xkcr_sm_taskflow |  | fid |

---

## 单据体-子表 t_xkcr_sm_task

- **表名称：** 单据体-子表
- **表名：** t_xkcr_sm_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmessage | 执行消息 | varchar | 500 |  | √ | ' ' | 执行消息 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftaskname | 任务名称 | varchar | 100 |  | √ | ' ' | 任务名称 |
| 5 | fbosorg | 合并组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | ftaskclass | 任务执行类 | varchar | 200 |  | √ | ' ' | 任务执行类 |
| 8 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 9 | ferrordetail | 错误详情 | varchar | 2000 |  | √ | ' ' | 错误详情 |
| 10 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdependencies | 依赖的前置任务 | text | 0 |  |  | null | 依赖的前置任务 |
| 12 | fpara | 任务参数 | varchar | 2000 |  | √ | ' ' | 任务参数 |
| 13 | ftaskstatus | 任务状态 | varchar | 50 |  | √ | 'UNDO' | 任务状态,枚举: SUCCESS :成功 SKIP :跳过 FAIL :失败 UNDO :初始 INEXECUTION :执行中 |
| 14 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 15 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fscope | 合并范围 | int8 | 64 |  | √ | 0 | [合并范围 xkcr_scope](../xkcr_files/xkcr_scope.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkcr_sm_task |  | fentryid |
| 2 | idx_xkcr_sm_task_fid |  | fid |
| 3 | idx_xkcr_sm_task_taskid |  | ftaskid |
