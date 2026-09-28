# 任务执行日志-cad_taskexecutelog

## 任务执行日志-多语言表 t_cad_taskexecutelog_l

- **表名称：** 任务执行日志-多语言表
- **表名：** t_cad_taskexecutelog_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | null | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_cad_taskexecutelog_l |  | fid,flocaleid |
| 2 | t_cad_taskexecutelog_l_pkey |  | fpkid |

---

## 任务执行日志-主表 t_cad_taskexecutelog

- **表名称：** 任务执行日志-主表
- **表名：** t_cad_taskexecutelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 耗时 | int8 | 64 |  | √ | 0 | 耗时 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :执行中 2 :失败 3 :成功 4 :通过 5 :提醒 6 :不通过 7 :警告 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | ferrlog | 错误日志 | varchar | 2000 |  | √ | ' ' | 错误日志 |
| 11 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 13 | ferrlog_tag | 错误日志_详情 | text | 0 |  |  | ' ' | 错误日志_详情 |
| 14 | ftimestamp | 开始时间戳 | int8 | 64 |  | √ | 0 | 开始时间戳 |
| 15 | fcontent | 提示 | varchar | 2000 |  | √ | ' ' | 提示 |
| 16 | ftaskid | 任务 | int8 | 64 |  | √ | 0 | [标准成本任务 sco_task](../sco_files/sco_task.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cad_taskexecutelog_pkey |  | fid |
| 2 | idx_cad_taskexecutelog2 |  | ftaskid |
| 3 | index_cad_taskexecutelog |  | fstarttime,ftaskid |
