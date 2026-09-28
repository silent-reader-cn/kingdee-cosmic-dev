# 进度展示-cal_progress

## 进度展示-主表 t_cal_progress

- **表名称：** 进度展示-主表
- **表名：** t_cal_progress

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fprogress | 进度 | int4 | 32 |  | √ | 0 | 进度 |
| 3 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_progre_task |  | ftaskid |
| 2 | pk_cal_progress |  | fid |

---

## 单据体-子表 t_cal_progressentry

- **表名称：** 单据体-子表
- **表名：** t_cal_progressentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftime | 耗时（ms） | int8 | 64 |  | √ | 0 | 耗时（ms） |
| 3 | fstatus | 状态 | bpchar | 1 |  | √ | ' ' | 状态,枚举: A :成功 B :失败 C :运行中 D :未运行 E :警告 |
| 4 | ferrorinfo | 异常信息 | varchar | 255 |  | √ | ' ' | 异常信息 |
| 5 | fstepid | 步骤 | int8 | 64 |  | √ | 0 | [步骤 cal_step](../calx_files/cal_step.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ferrorinfo_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_progreen_fid |  | fid |
| 2 | pk_cal_progressentry |  | fentryid |
