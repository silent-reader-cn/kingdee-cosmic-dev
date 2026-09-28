# 异步任务-fbd_asyncinvocationtask

## 调用参数-子表 t_fbd_asynctaskentry

- **表名称：** 调用参数-子表
- **表名：** t_fbd_asynctaskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpvalue | 参数值 | varchar | 2000 |  | √ | ' ' | 参数值 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_asynctaskentry_fid |  | fid |
| 2 | t_fbd_asynctaskentry_pkey |  | fentryid |

---

## 异步任务-主表 t_fbd_asynctask

- **表名称：** 异步任务-主表
- **表名：** t_fbd_asynctask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fresultmessage_tag | 调用结果_详情 | text | 0 |  |  | null | 调用结果_详情 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fnexttriggertime | 预计下次触发时间 | timestamp | 0 |  |  | null | 预计下次触发时间 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmethod | 调用方法 | varchar | 100 |  | √ | ' ' | 调用方法 |
| 7 | fresultmessage | 调用结果 | varchar | 255 |  | √ | ' ' | 调用结果 |
| 8 | fidentificationcode | 任务校验码 | varchar | 255 |  |  | ' ' | 任务校验码 |
| 9 | fretrycount | 已尝试次数 | int8 | 64 |  | √ | 0 | 已尝试次数 |
| 10 | fappid | 目标应用 | varchar | 50 |  | √ | ' ' | 目标应用 |
| 11 | flaststarttime | 最近调用开始时间 | timestamp | 0 |  |  | null | 最近调用开始时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 状态 | varchar | 30 |  | √ | '1' | 状态,枚举: 1 :待执行 2 :正在执行 3 :执行成功 4 :失败 5 :终止 |
| 14 | flastendtime | 最近调用完成时间 | timestamp | 0 |  |  | null | 最近调用完成时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fcloudid | 目标云 | varchar | 50 |  | √ | ' ' | 目标云 |
| 17 | fmaxretrycount | 最大尝试次数 | int8 | 64 |  | √ | 0 | 最大尝试次数 |
| 18 | flongtimetask | 是否耗时任务 | bpchar | 1 |  | √ | '0' | 是否耗时任务 |
| 19 | fservicename | 服务名称 | varchar | 100 |  | √ | ' ' | 服务名称 |
| 20 | fretryratethreshhold | 降频阀值次数 | int8 | 64 |  | √ | 0 | 降频阀值次数 |
| 21 | ftimeout | 超时时间 | int8 | 64 |  | √ | 0 | 超时时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_asytask_fidentcode |  | fidentificationcode |
| 2 | idx_fbd_asytask_fcreatetime |  | fcreatetime |
| 3 | t_fbd_asynctask_pkey |  | fid |
| 4 | idx_fbd_asytask_fstatus |  | fstatus |
