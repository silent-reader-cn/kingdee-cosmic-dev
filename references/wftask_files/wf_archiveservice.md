# 归档服务-wf_archiveservice

## 归档服务-主表 t_msg_archive

- **表名称：** 归档服务-主表
- **表名：** t_msg_archive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreator | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | farchivemsg | 消息通知 | text | 0 |  |  | null | 消息通知 |
| 4 | farchenddate | 归档数据结束时间 | varchar | 100 |  | √ | ' ' | 归档数据结束时间,枚举: |
| 5 | farchservicestartdate | 归档服务实际开始时间 | timestamp | 0 |  |  | null | 归档服务实际开始时间 |
| 6 | fdbzonename | 归档库名称 | varchar | 100 |  | √ | ' ' | 归档库名称 |
| 7 | farchiveentity | 归档实体 | varchar | 100 |  | √ | ' ' | 归档实体,枚举: |
| 8 | fprogress | 归档进度 | varchar | 100 |  | √ | ' ' | 归档进度 |
| 9 | fdatabase | 物理库 | varchar | 100 |  | √ | ' ' | 物理库,枚举: |
| 10 | falldatasum | 预估归档数据总量（万） | numeric | 19 | 6 | √ | 0 | 预估归档数据总量（万） |
| 11 | fenddate | 历史数据日期范围(以流程最终结束时间计算).结束 | timestamp | 0 |  |  | null | 历史数据日期范围(以流程最终结束时间计算).结束 |
| 12 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 13 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | farchstartdate | 归档数据开始时间 | varchar | 100 |  | √ | ' ' | 归档数据开始时间,枚举: |
| 15 | ffailreason | 失败详情 | varchar | 100 |  | √ | ' ' | 失败详情 |
| 16 | fscheduletotalsum | 迭代归档数据总量 | int8 | 64 |  | √ | 0 | 迭代归档数据总量 |
| 17 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 18 | fdatabasezone | 归档库 | varchar | 100 |  | √ | ' ' | 归档库,枚举: |
| 19 | fmodifier | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | farchserviceenddate | 归档服务结束时间 | timestamp | 0 |  |  | null | 归档服务结束时间 |
| 21 | fstate | 归档状态 | varchar | 100 |  | √ | ' ' | 归档状态,枚举: archivewill :未开始 archiveing :归档中 archivefail :归档失败 archiveok :归档成功 |
| 22 | fstartdate | 历史数据日期范围(以流程最终结束时间计算).开始 | timestamp | 0 |  |  | null | 历史数据日期范围(以流程最终结束时间计算).开始 |
| 23 | fpredicttime | 预估执行耗时（分钟） | numeric | 19 | 6 | √ | 0 | 预估执行耗时（分钟） |
| 24 | farchplanstartdate | 归档服务开始时间 | timestamp | 0 |  |  | null | 归档服务开始时间 |
| 25 | fschedulesize | 归档调度单次执行数量（条） | int4 | 32 |  | √ | 0 | 归档调度单次执行数量（条） |
| 26 | farchiverange | 归档数据时间范围（年） | varchar | 100 |  | √ | ' ' | 归档数据时间范围（年） |
| 27 | fnumber | 编码 | varchar | 100 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_archive_state |  | fstate |
| 2 | pk_t_msg_archive |  | fid |
| 3 | idx_msg_archive_entity |  | farchiveentity |
| 4 | idx_msg_archive_number |  | fnumber |

---

## 归档数据详情-子表 t_msg_archivedetail

- **表名称：** 归档数据详情-子表
- **表名：** t_msg_archivedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 业务对象 | varchar | 100 |  | √ | ' ' | 业务对象 |
| 3 | fentrydaterange | 归档时间范围（年） | varchar | 100 |  | √ | ' ' | 归档时间范围（年） |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentitynumber | 业务编码 | varchar | 100 |  | √ | ' ' | 业务编码 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fentitytotalsum | 历史数据总量 | int8 | 64 |  | √ | 0 | 历史数据总量 |
| 8 | fentityarchivesum | 归档数据量 | int8 | 64 |  | √ | 0 | 归档数据量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_archivedetail |  | fid |
| 2 | pk_t_msg_archivedetail |  | fentryid |

---

## 归档数据详情-多语言表 t_msg_archivedetail_l

- **表名称：** 归档数据详情-多语言表
- **表名：** t_msg_archivedetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentityname | 业务对象 | varchar | 100 |  | √ | ' ' | 业务对象 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msg_archivedetail_l |  | fpkid |
| 2 | idx_msg_archivedetail_l |  | fentryid,flocaleid |

---

## 归档服务-多语言表 t_msg_archive_l

- **表名称：** 归档服务-多语言表
- **表名：** t_msg_archive_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fdbzonename | 归档库名称 | varchar | 100 |  | √ | ' ' | 归档库名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_archive_l |  | fid,flocaleid |
| 2 | pk_t_msg_archive_l |  | fpkid |
