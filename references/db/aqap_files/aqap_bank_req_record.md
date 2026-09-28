# 业务请求记录表-aqap_bank_req_record

## 业务请求记录表-多语言表 t_aqap_bank_req_record_l

- **表名称：** 业务请求记录表-多语言表
- **表名：** t_aqap_bank_req_record_l

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
| 1 | idx_aqap_bank_req_record_l_0 |  | fid,flocaleid |
| 2 | t_aqap_bank_req_record_l_pkey |  | fpkid |

---

## 业务请求记录表-主表 t_aqap_bank_req_record

- **表名称：** 业务请求记录表-主表
- **表名：** t_aqap_bank_req_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fblock_flag | 阻塞标识 | varchar | 10 |  | √ | ' ' | 阻塞标识 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fwait_lock_time | 开始获取锁时间 | timestamp | 0 |  |  | null | 开始获取锁时间 |
| 6 | fbiz_type | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 7 | fext_data | 备用字段 | varchar | 600 |  | √ | ' ' | 备用字段 |
| 8 | fget_lock_time | 获取锁时间 | timestamp | 0 |  |  | null | 获取锁时间 |
| 9 | fbank_login_id | 前置机号 | varchar | 50 |  | √ | ' ' | 前置机号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | flock_num | 前置机并发数 | int8 | 64 |  | √ | 1 | 前置机并发数 |
| 12 | fbank_version | 银行版本 | varchar | 50 |  | √ | ' ' | 银行版本 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | freq_number | 请求编号 | varchar | 50 |  | √ | ' ' | 请求编号 |
| 15 | fprocess_millis | 请求处理耗时 | int8 | 64 |  |  | null | 请求处理耗时 |
| 16 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 19 | fblock_millis | 锁等待耗时 | int8 | 64 |  |  | null | 锁等待耗时 |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_bank_req_record_pkey |  | fid |
| 2 | idx_aqap_bank_req_record_1 |  | fcustom_id,fbank_login_id,fwait_lock_time |
| 3 | idx_aqap_bank_req_record |  | freq_number |
