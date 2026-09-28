# 前置机锁监控-aqap_login_lock_monitor

## 前置机锁监控-主表 t_aqap_login_lock_monitor

- **表名称：** 前置机锁监控-主表
- **表名：** t_aqap_login_lock_monitor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | flock_path | 所节点路径 | varchar | 500 |  | √ | ' ' | 所节点路径 |
| 5 | ftime_stamp | 时间戳 | varchar | 50 |  | √ | ' ' | 时间戳 |
| 6 | fthread_name | 线程名称 | varchar | 500 |  | √ | ' ' | 线程名称 |
| 7 | fbank_login | 银行前置机 | varchar | 50 |  | √ | ' ' | 银行前置机 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fbiz_type | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbank_version | 银行版本 | varchar | 50 |  | √ | ' ' | 银行版本 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | flog_no | 业务日志号 | varchar | 50 |  | √ | ' ' | 业务日志号 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fdate_time | 登记时间 | varchar | 50 |  | √ | ' ' | 登记时间 |
| 17 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnode | 实例节点 | varchar | 50 |  | √ | ' ' | 实例节点 |
| 19 | ftrace_no | monitor日志跟踪号 | varchar | 50 |  | √ | ' ' | monitor日志跟踪号 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aqap_login_lock_monitor |  | fid |
| 2 | idx_c_aqap_login_lock_monitor |  | fnumber |
| 3 | idx_login_lock_monitor_3 |  | flock_path |
| 4 | idx_login_lock_monitor_2 |  | fbank_login |
| 5 | idx_login_lock_monitor_1 |  | fbank_version |

---

## 前置机锁监控-多语言表 t_aqap_login_lock_monitor_l

- **表名称：** 前置机锁监控-多语言表
- **表名：** t_aqap_login_lock_monitor_l

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
| 1 | idx_login_lock_monitor_l_0 |  | fid,flocaleid |
| 2 | idx_c_lock_monitor_l |  | fname |
| 3 | pk_aqap_login_lock_monitor_l |  | fpkid |
