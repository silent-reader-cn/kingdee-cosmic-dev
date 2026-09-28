# 银企云日志-aqap_new_log

## 银企云日志-主表 t_aqap_new_log

- **表名称：** 银企云日志-主表
- **表名：** t_aqap_new_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbank_login | 银行前置机 | varchar | 50 |  | √ | ' ' | 银行前置机 |
| 5 | flogger_detail_no | 银企日志明细号 | varchar | 50 |  | √ | ' ' | 银企日志明细号 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | flog_time | 请求时间 | varchar | 50 |  | √ | ' ' | 请求时间 |
| 8 | fbd_biz_name | 基础资料_业务类型 | int8 | 64 |  |  | null | [业务类型 aqap_business_type](../aqap_files/aqap_business_type.md) |
| 9 | fbiz_seq | 业务流水号 | varchar | 50 |  | √ | ' ' | 业务流水号 |
| 10 | fdt_query | 查询时间 | timestamp | 0 |  |  | null | 查询时间 |
| 11 | fsubbiztype | 子业务类型 | int8 | 64 |  |  | null | [日志子业务类型 aqap_sub_biz_type](../aqap_files/aqap_sub_biz_type.md) |
| 12 | flogger_batch_no | 银企日志跟踪号 | varchar | 50 |  | √ | ' ' | 银企日志跟踪号 |
| 13 | faccount | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 14 | flogger_bank_no | 银行日志跟踪号 | varchar | 50 |  | √ | ' ' | 银行日志跟踪号 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | flogger_type | 日志类型 | varchar | 50 |  | √ | ' ' | 日志类型,枚举: 0 :业务日志 1 :业务日志+银行日志 |
| 17 | fbank_version | 银行版本 | varchar | 50 |  | √ | ' ' | 银行版本 |
| 18 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 21 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fbd_bank_version | 基础资料_银行版本 | int8 | 64 |  |  | null | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fbiz_name | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_new_log_pkey |  | fid |
| 2 | idx_aqap_new_log_batch_no |  | flogger_batch_no |
| 3 | idx_aqap_new_log_login |  | fbank_login |
| 4 | idx_aqap_new_log_bank_no |  | flogger_bank_no |
| 5 | idx_aqap_new_log_type |  | flogger_type |
| 6 | idx_aqap_new_log_dtquery |  | fdt_query |

---

## 银企云日志-多语言表 t_aqap_new_log_l

- **表名称：** 银企云日志-多语言表
- **表名：** t_aqap_new_log_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_new_log_l_pkey |  | fpkid |
