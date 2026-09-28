# 银行业务日志-aqap_business_log

## 银行业务日志-多语言表 t_aqap_business_log_l

- **表名称：** 银行业务日志-多语言表
- **表名：** t_aqap_business_log_l

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
| 1 | t_aqap_business_log_l_pkey |  | fpkid |
| 2 | idx_aqap_business_log_l_0 |  | fid,flocaleid |

---

## 银行业务日志-主表 t_aqap_business_log

- **表名称：** 银行业务日志-主表
- **表名：** t_aqap_business_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fbank_login | 银行前置机 | varchar | 128 |  | √ | ' ' | 银行前置机 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | flog_time | 记录时间 | varchar | 50 |  | √ | ' ' | 记录时间 |
| 6 | fbd_biz_name | 基础资料_业务类型 | int8 | 64 |  |  | null | 业务类型 aqap_business_type |
| 7 | fbiz_seq | 业务流水号 | varchar | 50 |  | √ | ' ' | 业务流水号 |
| 8 | fdt_query | 查询时间 | timestamp | 0 |  |  | null | 查询时间 |
| 9 | faccount | 账号 | varchar | 128 |  | √ | ' ' | 账号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbank_version | 银行版本 | varchar | 50 |  | √ | ' ' | 银行版本 |
| 12 | frequest_seq | 请求流水号 | varchar | 50 |  | √ | ' ' | 请求流水号 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 16 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fbd_bank_version | 基础资料_银行版本 | int8 | 64 |  |  | null | 银行启用管理 aqap_bank |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fbiz_name | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_business_log_pkey |  | fid |
