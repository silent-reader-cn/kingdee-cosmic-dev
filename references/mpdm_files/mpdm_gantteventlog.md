# 甘特图事件日志-mpdm_gantteventlog

## 甘特图事件日志-主表 t_mpdm_gteventlog

- **表名称：** 甘特图事件日志-主表
- **表名：** t_mpdm_gteventlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 操作事件 | varchar | 100 |  | √ | ' ' | 操作事件 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | faftercontent | 操作后内容 | varchar | 1000 |  | √ | ' ' | 操作后内容 |
| 5 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | fbusinessobjid | 业务对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 7 | fresult | 执行结果 | varchar | 50 |  | √ | ' ' | 执行结果,枚举: 0 :失败 1 :成功 |
| 8 | fdatasourceid | 页面 | varchar | 50 |  | √ | ' ' | 页面 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fbeforecontent | 操作前内容 | varchar | 1000 |  | √ | ' ' | 操作前内容 |
| 11 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fclientip | 客户端地址 | varchar | 50 |  | √ | ' ' | 客户端地址 |
| 13 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | ffailcause | 失败原因 | varchar | 1000 |  | √ | ' ' | 失败原因 |
| 16 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 事件编码 | varchar | 30 |  | √ | ' ' | 事件编码 |
| 18 | fclientname | 客户端名称 | varchar | 50 |  | √ | ' ' | 客户端名称 |
| 19 | fbillno | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_gantog_fcreatetime |  | fcreatetime |
| 2 | pk_mpdm_gteventlog |  | fid |
| 3 | idx_mpdm_gantog_fnumber |  | fnumber |

---

## 甘特图事件日志-多语言表 t_mpdm_gteventlog_l

- **表名称：** 甘特图事件日志-多语言表
- **表名：** t_mpdm_gteventlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 操作事件 | varchar | 100 |  | √ | ' ' | 操作事件 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_gteventlog_l |  | fpkid |
| 2 | idx_mpdm_gantogl_fid |  | fid,flocaleid |
| 3 | idx_mpdm_gantogl_fname |  | fname |
