# 公有云数据同步-bdm_his_sync_log

## 公有云数据同步-主表 t_rim_his_sync_log

- **表名称：** 公有云数据同步-主表
- **表名：** t_rim_his_sync_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fclientid | clientId | varchar | 50 |  | √ | ' ' | clientId |
| 3 | fsync_type | 同步方式 | varchar | 4 |  | √ | ' ' | 同步方式,枚举: 1 :手工触发 2 :定时任务 |
| 4 | ftax_no | 税号 | varchar | 30 |  | √ | ' ' | 税号 |
| 5 | fend_time | 处理完成时间 | timestamp | 0 |  |  | null | 处理完成时间 |
| 6 | fstart_time | 处理开始时间 | timestamp | 0 |  |  | null | 处理开始时间 |
| 7 | fdeal_times | 处理次数 | int4 | 32 |  | √ | 0 | 处理次数 |
| 8 | fmsg | 同步信息 | varchar | 1000 |  | √ | ' ' | 同步信息 |
| 9 | fdata_date_start | 数据开始日期 | timestamp | 0 |  |  | null | 数据开始日期 |
| 10 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fdata_date | 数据日期文本 | varchar | 20 |  | √ | ' ' | 数据日期文本 |
| 12 | fdata_date_end | 数据结束日期 | timestamp | 0 |  |  | null | 数据结束日期 |
| 13 | fappid | 类型 | varchar | 20 |  | √ | ' ' | 类型,枚举: sim :销项 rim :进项 |
| 14 | fsuccess | 成功记录 | int4 | 32 |  | √ | 0 | 成功记录 |
| 15 | fstatus | 同步结果 | varchar | 4 |  | √ | ' ' | 同步结果,枚举: 0 :失败 1 :成功 2 :待处理 3 :处理中 |
| 16 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fpage_no | 请求次数 | int4 | 32 |  | √ | 0 | 请求次数 |
| 18 | fcompany_name | 企业名称 | varchar | 150 |  | √ | ' ' | 企业名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_rim_his_sync_log |  | fid |
| 2 | idx_rim_his_sync_log |  | forg,fclientid,fdata_date |
