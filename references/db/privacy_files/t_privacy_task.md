# 数据处理-t_privacy_task

## 数据处理-主表 t_privacy_task

- **表名称：** 数据处理-主表
- **表名：** t_privacy_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fstart_date | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 3 | ffield_type | ffield_type | varchar | 50 |  |  | ' ' |  |
| 4 | fpkvalue | fpkvalue | varchar | 255 |  |  | null |  |
| 5 | ftask_type | 任务类型 | varchar | 100 |  |  | null | 任务类型,枚举: 1 :字段加密 2 :字段解密 3 :替换加密 |
| 6 | fupgrade | fupgrade | int4 | 32 |  |  | null |  |
| 7 | fschemeid | 所属方案 | int8 | 64 |  |  | null | 所属方案 |
| 8 | fislocale | 是否多语言 | varchar | 50 |  |  | ' ' | 是否多语言,枚举: TRUE :是 FALSE :否 |
| 9 | ftask_status | 任务状态 | varchar | 50 |  | √ | ' ' | 任务状态,枚举: 0 :未开始 1 :等待 2 :进行中 3 :完成 4 :失败 |
| 10 | forderby_value | forderby_value | varchar | 255 |  |  | null |  |
| 11 | fentityname | fentityname | varchar | 50 |  |  | null |  |
| 12 | foldencrypt_type | 旧的加密算法 | varchar | 50 |  |  | ' ' | 旧的加密算法 |
| 13 | fdbrouter | DBRouter | varchar | 50 |  |  | ' ' | DBRouter |
| 14 | ffielddesc | 字段名称 | varchar | 50 |  |  | null | 字段名称 |
| 15 | fcreater | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ffieldident | 字段标识 | varchar | 50 |  |  | null | 字段标识 |
| 17 | fiscommonlang | 是否通用语言 | varchar | 50 |  | √ | ' ' | 是否通用语言,枚举: FALSE :否 TRUE :是 |
| 18 | fpytable_name | fpytable_name | varchar | 50 |  | √ | ' ' |  |
| 19 | fpkname | fpkname | varchar | 50 |  |  | ' ' |  |
| 20 | fversion | fversion | int4 | 32 |  |  | null |  |
| 21 | fentity_number | 实体编码 | varchar | 50 |  |  | ' ' | 实体编码 |
| 22 | ferrorlogs | 错误日志 | varchar | 2000 |  |  | ' ' | 错误日志 |
| 23 | ffield_name | 物理字段名 | varchar | 50 |  | √ | ' ' | 物理字段名 |
| 24 | fend_date | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 25 | fpktype | fpktype | int4 | 32 |  |  | null |  |
| 26 | ftable_name | 物理表名 | varchar | 50 |  | √ | ' ' | 物理表名 |
| 27 | finstanceid | 实例id | varchar | 75 |  | √ | ' ' | 实例id |
| 28 | fcreate_by | fcreate_by | int8 | 64 |  |  | null |  |
| 29 | foldencrypt | foldencrypt | varchar | 50 |  |  | null |  |
| 30 | forderby | forderby | varchar | 50 |  |  | ' ' |  |
| 31 | ftasknumber | 任务ID | varchar | 50 |  |  | null | 任务ID |
| 32 | fcreate_date | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_privacy_task_pkey |  | fid |

---

## 数据处理-多语言表 t_privacy_task_l

- **表名称：** 数据处理-多语言表
- **表名：** t_privacy_task_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | fentityname | varchar | 200 |  | √ | ' ' |  |
| 3 | ffielddesc | 字段名称 | varchar | 100 |  | √ | ' ' | 字段名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_privacy_task_l |  | fpkid |
| 2 | idx_privacy_task_l_fid |  | fid,flocaleid |
