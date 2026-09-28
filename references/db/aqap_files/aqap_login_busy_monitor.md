# 前置机繁忙度监控-aqap_login_busy_monitor

## 前置机繁忙度监控-主表 t_aqap_login_busy_monitor

- **表名称：** 前置机繁忙度监控-主表
- **表名：** t_aqap_login_busy_monitor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fbank_login | 银行前置机 | varchar | 50 |  | √ | ' ' | 银行前置机 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fblock_num | 阻塞次数 | int8 | 64 |  |  | null | 阻塞次数 |
| 7 | fprocess_time | 处理耗时(s) | int8 | 64 |  |  | null | 处理耗时(s) |
| 8 | fwait_time | 等待耗时(s) | int8 | 64 |  |  | null | 等待耗时(s) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fbd_bank_login | 银行前置机 | int8 | 64 |  |  | null | [银企连接通道配置 aqap_bank_login](../aqap_files/aqap_bank_login.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fblock_rate | 阻塞率 | varchar | 50 |  | √ | ' ' | 阻塞率 |
| 14 | ftime_slot | 统计期间 | varchar | 50 |  | √ | ' ' | 统计期间 |
| 15 | fnormal_num | 非阻塞次数 | int8 | 64 |  |  | null | 非阻塞次数 |
| 16 | fquery_date | 监控日期 | timestamp | 0 |  |  | null | 监控日期 |
| 17 | fbd_bank_version | 银行版本 | int8 | 64 |  |  | null | [银行启用管理 aqap_bank](../aqap_files/aqap_bank.md) |
| 18 | fuse_rate | 利用率 | varchar | 50 |  | √ | ' ' | 利用率 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_login_busy_monitor_pkey |  | fid |
