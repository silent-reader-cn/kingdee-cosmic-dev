# 前置机连接监控-aqap_login_link_monitor

## 前置机连接监控-主表 t_aqap_monitor

- **表名称：** 前置机连接监控-主表
- **表名：** t_aqap_monitor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | 人员 bos_user |
| 3 | fmessage | 状态说明 | varchar | 500 |  | √ | ' ' | 状态说明 |
| 4 | fupdate_time | 统计时间 | timestamp | 0 |  |  | null | 统计时间 |
| 5 | facnt | 检查账号 | varchar | 50 |  | √ | ' ' | 检查账号 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbank_login_id | 银行前置机 | varchar | 50 |  | √ | ' ' | 银行前置机 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ftextfield | type | varchar | 50 |  | √ | ' ' | type |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fbank_name | 银行名称 | varchar | 50 |  | √ | ' ' | 银行名称 |
| 12 | fstate | 连接状态 | varchar | 50 |  | √ | ' ' | 连接状态,枚举: 连接正常 :连接正常 连接异常 :连接异常 未检测 :未检测 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fbank_loginid | fbank_loginid | varchar | 50 |  | √ | ' ' |  |
| 17 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_aqap_monitor_pkey |  | fid |

---

## 前置机连接监控-多语言表 t_aqap_monitor_l

- **表名称：** 前置机连接监控-多语言表
- **表名：** t_aqap_monitor_l

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
| 1 | t_aqap_monitor_l_pkey |  | fpkid |
| 2 | idx_aqap_monitor_l_0 |  | fid,flocaleid |
