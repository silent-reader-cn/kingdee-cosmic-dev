# 前置机连接检查-aqap_login_link_check

## 前置机连接检查-主表 t_aqap_login_link_check

- **表名称：** 前置机连接检查-主表
- **表名：** t_aqap_login_link_check

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fmessage | 备注信息 | varchar | 500 |  | √ | ' ' | 备注信息 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fupdate_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbank_version_id | 银行版本 | varchar | 50 |  | √ | ' ' | 银行版本 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fbank_login_id | 前置机号 | varchar | 50 |  | √ | ' ' | 前置机号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 连接状态 | varchar | 50 |  | √ | ' ' | 连接状态 |
| 12 | fcustom_id | 租户号 | varchar | 50 |  | √ | ' ' | 租户号 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 14 | ftype | 监控方式 | varchar | 50 |  | √ | ' ' | 监控方式 |
| 15 | fnotify_time | 通知时间 | timestamp | 0 |  |  | null | 通知时间 |
| 16 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  |  | null | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_login_link_check_pkey |  | fid |
