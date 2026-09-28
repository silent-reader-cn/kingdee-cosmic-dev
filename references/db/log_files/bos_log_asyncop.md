# 异步服务日志-bos_log_asyncop

## 异步服务日志-主表 t_log_asyncop

- **表名称：** 异步服务日志-主表
- **表名：** t_log_asyncop

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparam | 参数 | varchar | 255 |  | √ | ' ' | 参数 |
| 3 | fexetime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 4 | flog_tag | 日志_详情 | text | 0 |  |  | null | 日志_详情 |
| 5 | foperator | 操作类型 | varchar | 36 |  | √ | ' ' | 操作类型 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fuserid | 操作用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | flog | 日志 | varchar | 255 |  | √ | ' ' | 日志 |
| 9 | fentity | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 10 | fsuccess | 是否成功 | bpchar | 1 |  | √ | '0' | 是否成功 |
| 11 | fbillid | 业务单据ID | varchar | 36 |  | √ | ' ' | 业务单据ID |
| 12 | fconsume | 是否执行完成 | bpchar | 1 |  | √ | '0' | 是否执行完成 |
| 13 | foprulekey | 服务标识 | varchar | 36 |  | √ | ' ' | 服务标识 |
| 14 | fparam_tag | 参数_详情 | text | 0 |  |  | null | 参数_详情 |
| 15 | fbillno | 业务单据编码 | varchar | 200 |  | √ | ' ' | 业务单据编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_log_asyncop_op |  | foperator |
| 2 | idx_log_asyncop_entity |  | fentity |
| 3 | idx_log_asyncop_rule |  | foprulekey |
| 4 | idx_log_asyncop_time |  | fexetime |
| 5 | t_log_asyncop_pkey |  | fid |
| 6 | idx_log_asyncop_billid |  | fbillid |
| 7 | idx_log_asyncop_org |  | forgid |

---

## 异步服务日志-多语言表 t_log_asyncop_l

- **表名称：** 异步服务日志-多语言表
- **表名：** t_log_asyncop_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperatorname | 操作名称 | varchar | 80 |  | √ | ' ' | 操作名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | foprulename | 服务名称 | varchar | 80 |  | √ | ' ' | 服务名称 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_log_asyncop_l_pkey |  | fpkid |
| 2 | idx_log_asyncop_l_id |  | fid |
