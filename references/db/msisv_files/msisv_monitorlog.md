# 监听日志-msisv_monitorlog

## 监听日志-主表 t_msisv_monitorlog

- **表名称：** 监听日志-主表
- **表名：** t_msisv_monitorlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 3 | fissuccess | 是否成功 | bpchar | 1 |  | √ | '0' | 是否成功 |
| 4 | flog_tag | 日志_详情 | text | 0 |  |  | null | 日志_详情 |
| 5 | ftraceid | 追踪号 | varchar | 50 |  | √ | ' ' | 追踪号 |
| 6 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 7 | fecologicmonitor | 生态接入监听 | varchar | 50 |  | √ | ' ' | 生态接入监听 |
| 8 | foperationname | 监听操作名称 | varchar | 50 |  | √ | ' ' | 监听操作名称 |
| 9 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fbizno | 业务编号 | varchar | 50 |  | √ | ' ' | 业务编号 |
| 11 | flog | 日志 | varchar | 50 |  | √ | ' ' | 日志 |
| 12 | fentity | 单据实体 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | ftype | 集成类型 | varchar | 50 |  | √ | ' ' | 集成类型,枚举: A :联合下推 B :关联更新 C :服务调用 |
| 14 | factionnumber | 集成活动编码 | varchar | 50 |  | √ | ' ' | 集成活动编码 |
| 15 | fisfinish | 是否执行完成 | bpchar | 1 |  | √ | '0' | 是否执行完成 |
| 16 | faction | 集成活动 | varchar | 50 |  | √ | ' ' | 集成活动 |
| 17 | fbillid | 业务单据ID | int8 | 64 |  | √ | 0 | 业务单据ID |
| 18 | foperation | 监听操作 | varchar | 50 |  | √ | ' ' | 监听操作 |
| 19 | fbillno | 业务单据编码 | varchar | 50 |  | √ | ' ' | 业务单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msisv_monitorlog |  | fid |
| 2 | idx_msisv_molog_billno |  | fbillno |

---

## 监听日志-多语言表 t_msisv_monitorlog_l

- **表名称：** 监听日志-多语言表
- **表名：** t_msisv_monitorlog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fecologicmonitor | 生态接入监听 | varchar | 50 |  | √ | ' ' | 生态接入监听 |
| 3 | foperationname | 监听操作名称 | varchar | 50 |  | √ | ' ' | 监听操作名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msisv_monitorlog_l |  | fpkid |
| 2 | idx_msisv_monitorlog_l_id |  | fid,flocaleid |
