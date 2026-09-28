# 后台任务组-isc_job_mutex

## 锁分配明细-子表 t_isc_job_mutex_instance

- **表名称：** 锁分配明细-子表
- **表名：** t_isc_job_mutex_instance

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finstance | 服务器ID | varchar | 50 |  | √ | ' ' | 服务器ID |
| 3 | foccupied_time | 分配时间 | timestamp | 0 |  |  | null | 分配时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fip | 服务器IP | varchar | 50 |  | √ | ' ' | 服务器IP |
| 6 | flast_modified_time | 状态更新时间 | timestamp | 0 |  |  | null | 状态更新时间 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_job_mutex_ins_fk |  | fid |
| 2 | pk_t_isc_job_mutex_instance |  | fentryid |

---

## 后台任务组-主表 t_isc_job_mutex

- **表名称：** 后台任务组-主表
- **表名：** t_isc_job_mutex

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flast_modifier_id | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fmax_threads | 最大线程数 | int4 | 32 |  | √ | 0 | 最大线程数 |
| 5 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 6 | flast_modified_time | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fscope | 范围 | varchar | 50 |  | √ | ' ' | 范围,枚举: LOCAL :本地 GLOBAL :全局 |
| 8 | fappid | 集成云应用ID | varchar | 50 |  | √ | ' ' | 集成云应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_job_mutex_i |  | fnumber |
| 2 | pk_t_isc_job_mutex |  | fid |

---

## 后台任务组-多语言表 t_isc_job_mutex_l

- **表名称：** 后台任务组-多语言表
- **表名：** t_isc_job_mutex_l

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
| 1 | pk_t_isc_job_mutex_l |  | fpkid |
| 2 | idx_isc_job_mutex_l_0 |  | fid,flocaleid |
