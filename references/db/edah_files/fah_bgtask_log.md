# 迁入迁出日志-fah_bgtask_log

## 迁入迁出日志-主表 t_fah_bgtask_log

- **表名称：** 迁入迁出日志-主表
- **表名：** t_fah_bgtask_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ftasktype | 任务类型 | varchar | 5 |  | √ | ' ' | 任务类型,枚举: 0 :外部数据模型迁出 1 :外部数据模型迁入 |
| 5 | finstanceid | 运行任务的实例ID | varchar | 50 |  | √ | ' ' | 运行任务的实例ID |
| 6 | fcreatetime | 任务启动时间 | timestamp | 0 |  |  | null | 任务启动时间 |
| 7 | fcmpworkpoint | 任务已完成的工作点数 | int4 | 32 |  | √ | 0 | 任务已完成的工作点数 |
| 8 | ftaskstatus | 任务状态 | bpchar | 1 |  | √ | ' ' | 任务状态,枚举: 0 :新建/等待执行 2 :处理中 3 :挂起 4 :成功 5 :取消 7 :警告 8 :失败 9 :（标记）删除 |
| 9 | ftotalworkpoint | 任务总点数 | int4 | 32 |  | √ | 0 | 任务总点数 |
| 10 | ftaskname | 任务名称 | varchar | 30 |  | √ | ' ' | 任务名称 |
| 11 | fcomptime | 任务完成时间 | timestamp | 0 |  |  | null | 任务完成时间 |
| 12 | fmodifytime | 修改日期 | timestamp | 0 |  |  | null | 修改日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fah_bgtask_log |  | ftasktype |
| 2 | pk_fah_bgtask_log |  | fid |

---

## 日志明细记录-子表 t_fah_bgtask_log_detail

- **表名称：** 日志明细记录-子表
- **表名：** t_fah_bgtask_log_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmsg_tag | 说明_详情 | text | 0 |  |  | null | 说明_详情 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftaskstepstatus | 任务执行步骤状态 | bpchar | 1 |  | √ | ' ' | 任务执行步骤状态,枚举: 0 :新建/等待执行 2 :处理中 3 :挂起 4 :成功 5 :取消 7 :警告 8 :失败 9 :（标记）删除 |
| 5 | fmsg | 说明 | varchar | 255 |  |  | ' ' | 说明 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | floglevel | 日志级别 | bpchar | 1 |  | √ | ' ' | 日志级别,枚举: 0 :致命错误 1 :错误 2 :警告 3 :信息 4 :调试 5 :跟踪 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fah_bgtask_log_detail |  | fentryid |
| 2 | idx_fah_bgtask_log_detail |  | fid |
