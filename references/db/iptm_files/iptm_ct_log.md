# 日志管理-iptm_ct_log

## 日志管理-主表 t_iptm_ct_log

- **表名称：** 日志管理-主表
- **表名：** t_iptm_ct_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffailedcount | 失败个数 | int8 | 64 |  | √ | 0 | 失败个数 |
| 3 | ftraceid | traceId | varchar | 50 |  | √ | ' ' | traceId |
| 4 | fmessage | 日志内容 | varchar | 255 |  | √ | ' ' | 日志内容 |
| 5 | foptype | 操作类型 | varchar | 50 |  | √ | ' ' | 操作类型,枚举: 0 :同步 1 :在线传输 3 :添加到传输包 4 :快速传输 5 :传输并同步 6 :上传 7 :下载 |
| 6 | fdevmessage_tag | 开发日志内容_详情 | text | 0 |  |  | null | 开发日志内容_详情 |
| 7 | fpacketid | 传输包编码 | int8 | 64 |  | √ | 0 | [传输包管理 iptm_ct_datapacket](../iptm_files/iptm_ct_datapacket.md) |
| 8 | foptime | 执行开始时间 | timestamp | 0 |  |  | null | 执行开始时间 |
| 9 | fstate | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: 1 :成功 2 :失败 3 :部分成功 4 :执行中 |
| 10 | fbatchpackscheme | 批量打包方案 | int8 | 64 |  | √ | 0 | [打包方案 iptm_ct_packscheme](../iptm_files/iptm_ct_packscheme.md) |
| 11 | fopuser | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fopendtime | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 13 | ftargetdatacenterid | 目标数据中心 | int8 | 64 |  | √ | 0 | [连接数据中心管理 iptm_ct_destaccount](../iptm_files/iptm_ct_destaccount.md) |
| 14 | ftaskid | 调度任务ID | varchar | 50 |  | √ | ' ' | 调度任务ID |
| 15 | fdevmessage | 开发日志内容 | varchar | 255 |  | √ | ' ' | 开发日志内容 |
| 16 | fusetime | 用时 | varchar | 50 |  | √ | ' ' | 用时 |
| 17 | fbillno | 编号 | varchar | 200 |  | √ | ' ' | 编号 |
| 18 | fmessage_tag | 日志内容_详情 | text | 0 |  |  | null | 日志内容_详情 |
| 19 | fsuccesscount | 成功个数 | int8 | 64 |  | √ | 0 | 成功个数 |
| 20 | ftargetdatacenteruser | 目标数据中心用户（手机号） | varchar | 50 |  | √ | ' ' | 目标数据中心用户（手机号） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_ct_log |  | fid |
| 2 | idx_iptm_ct_log |  | fbillno |

---

## 单据体-子表 t_iptm_ct_logentry

- **表名称：** 单据体-子表
- **表名：** t_iptm_ct_logentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrysynstatus | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: 0 :未同步 1 :同步完成 2 :同步失败 |
| 3 | fentrysuccesscount | 成功条数 | int8 | 64 |  | √ | 0 | 成功条数 |
| 4 | fentryfailedcount | 失败条数 | int8 | 64 |  | √ | 0 | 失败条数 |
| 5 | fsynlog | 分录行日志 | varchar | 255 |  | √ | ' ' | 分录行日志 |
| 6 | fsynlog_tag | 分录行日志_详情 | text | 0 |  |  | null | 分录行日志_详情 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_ct_logentry |  | fentryid |
| 2 | idx_iptm_ct_logentry |  | fid |

---

## 日志管理-多语言表 t_iptm_ct_log_l

- **表名称：** 日志管理-多语言表
- **表名：** t_iptm_ct_log_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 传输包（废弃） | varchar | 50 |  | √ | ' ' | 传输包（废弃） |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iptm_ct_log_l |  | fpkid |
| 2 | idx_iptm_ct_log_l |  | fid |
| 3 | idx_iptm_ct_log_l_local |  | flocaleid |
