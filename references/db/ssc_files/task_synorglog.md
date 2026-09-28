# 同步日志查看-task_synorglog

## 同步日志查看-主表 t_tk_synorglog

- **表名称：** 同步日志查看-主表
- **表名：** t_tk_synorglog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbizbill | 业务单据 | int8 | 64 |  | √ | 0 | [业务单据 task_taskbill](../ssc_files/task_taskbill.md) |
| 4 | fstackinfo_tag | 错误堆栈_详情 | text | 0 |  |  | null | 错误堆栈_详情 |
| 5 | fstackinfo | 错误堆栈 | varchar | 255 |  | √ | ' ' | 错误堆栈 |
| 6 | ffailurereason | 失败原因 | varchar | 150 |  | √ | ' ' | 失败原因 |
| 7 | fsyntime | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 8 | fsynstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :成功 1 :失败 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_ssc_synlog_bizbill |  | fbizbill |
| 2 | pk_t_tk_synorglog |  | fid |
| 3 | index_ssc_synlog_ssc |  | fsscid |
