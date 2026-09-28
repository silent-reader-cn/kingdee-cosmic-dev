# 日志详情存储表-aqap_new_log_detail

## 日志详情存储表-多语言表 t_aqap_new_log_detail_l

- **表名称：** 日志详情存储表-多语言表
- **表名：** t_aqap_new_log_detail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_aqap_new_log_detail_l_0 |  | fid,flocaleid |
| 2 | pk_aqap_new_log_detail_l |  | fpkid |
| 3 | idx_cluster_aqap_log_detail_l |  | fname |

---

## 日志详情存储表-主表 t_aqap_new_log_detail

- **表名称：** 日志详情存储表-主表
- **表名：** t_aqap_new_log_detail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flogger_detail_no | 银企日志明细号 | varchar | 50 |  | √ | ' ' | 银企日志明细号 |
| 3 | flog_time | 请求时间 | varchar | 50 |  | √ | ' ' | 请求时间 |
| 4 | fbd_biz_name | 基础资料_业务类型 | int8 | 64 |  | √ | 0 | 业务类型 aqap_business_type |
| 5 | faccount | 账号 | varchar | 50 |  | √ | ' ' | 账号 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fbiz_name | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 11 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 12 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | flog_content_tag | 日志内容_详情 | text | 0 |  |  | null | 日志内容_详情 |
| 14 | fbank_login | 银行前置机 | varchar | 50 |  | √ | ' ' | 银行前置机 |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fbiz_seq | 业务流水号 | varchar | 50 |  | √ | ' ' | 业务流水号 |
| 17 | fdt_query | 查询时间 | timestamp | 0 |  |  | null | 查询时间 |
| 18 | flogger_batch_no | 银企日志跟踪号 | varchar | 50 |  | √ | ' ' | 银企日志跟踪号 |
| 19 | flogger_bank_no | 银行日志跟踪号 | varchar | 50 |  | √ | ' ' | 银行日志跟踪号 |
| 20 | flogger_type | 日志类型 | varchar | 50 |  | √ | ' ' | 日志类型 |
| 21 | fbank_version | 银行版本 | varchar | 50 |  | √ | ' ' | 银行版本 |
| 22 | flog_content | 日志内容 | varchar | 255 |  | √ | ' ' | 日志内容 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fbd_bank_version | 基础资料_银行版本 | int8 | 64 |  | √ | 0 | 银行启用管理 aqap_bank |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_new_log_detail_type |  | flogger_type |
| 2 | idx_aqap_new_log_detail_logger |  | flogger_batch_no,flogger_bank_no |
| 3 | t_aqap_new_log_detail_biz |  | fbiz_name |
| 4 | pk_aqap_new_log_detail |  | fid |
| 5 | idx_cluster_aqap_log_detail |  | fnumber |
