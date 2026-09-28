# 集成云后台任务类型-isc_job_type

## 集成云后台任务类型-主表 t_isc_job_type

- **表名称：** 集成云后台任务类型-主表
- **表名：** t_isc_job_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 30 |  | √ | ' ' | id |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 3 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_job_type_num |  | fnumber |
| 2 | pk_t_isc_job_type |  | fid |

---

## 集成云后台任务类型-多语言表 t_isc_job_type_l

- **表名称：** 集成云后台任务类型-多语言表
- **表名：** t_isc_job_type_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 30 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 100 |  |  | null | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | null | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_job_type_l |  | fpkid |
| 2 | idx_isc_job_type_l_id |  | fid,flocaleid |
