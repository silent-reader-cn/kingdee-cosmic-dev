# 渠道待办重试日志-wf_taskjobretrylog

## 渠道待办重试日志-多语言表 t_wf_taskjobretrylog_l

- **表名称：** 渠道待办重试日志-多语言表
- **表名：** t_wf_taskjobretrylog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperator | 重试执行人 | varchar | 50 |  | √ | ' ' | 重试执行人 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_taskjobretrylog_l |  | fpkid |
| 2 | idx_wf_taskjobretrylog_l |  | fid,flocaleid |

---

## 渠道待办重试日志-主表 t_wf_taskjobretrylog

- **表名称：** 渠道待办重试日志-主表
- **表名：** t_wf_taskjobretrylog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fchannellogid | 渠道待办日志ID | int8 | 64 |  | √ | 0 | 渠道待办日志ID |
| 3 | ftraceid | traceid | varchar | 100 |  | √ | ' ' | traceid |
| 4 | foperator | 重试执行人 | varchar | 50 |  | √ | ' ' | 重试执行人 |
| 5 | fretrydate | 重试时间 | timestamp | 0 |  |  | null | 重试时间 |
| 6 | fresult | 重试结果 | varchar | 500 |  | √ | ' ' | 重试结果 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_taskjobrtylog_chanlog |  | fchannellogid |
| 2 | pk_wf_taskjobretrylog |  | fid |
