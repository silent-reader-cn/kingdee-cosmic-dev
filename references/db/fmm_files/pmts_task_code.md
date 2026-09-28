# 任务进度计划编码规则-pmts_task_code

## 任务进度计划编码规则-主表 t_pmts_task_code

- **表名称：** 任务进度计划编码规则-主表
- **表名：** t_pmts_task_code

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fmaxvalue | 编码最大值 | int4 | 32 |  | √ | 0 | 编码最大值 |
| 4 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | finitdata | 初始值 | int4 | 32 |  | √ | 0 | 初始值 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ftaskstring | 作业前缀 | varchar | 50 |  | √ | ' ' | 作业前缀 |
| 12 | ftaskstep | 作业增量 | varchar | 50 |  | √ | ' ' | 作业增量 |
| 13 | fpositionnumber | 位数 | int4 | 32 |  | √ | 0 | 位数 |
| 14 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fmaxnumber | 最大编码 | varchar | 50 |  | √ | ' ' | 最大编码 |
| 17 | ftaskid | 任务进度计划ID | varchar | 50 |  | √ | ' ' | 任务进度计划ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmts_taskc_fnumber |  | fnumber |
| 2 | idx_pmts_taskc_fcreatetime |  | fcreatetime |
| 3 | pk_pmts_task_code |  | fid |

---

## 任务进度计划编码规则-多语言表 t_pmts_task_code_l

- **表名称：** 任务进度计划编码规则-多语言表
- **表名：** t_pmts_task_code_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmts_taskcl_fname |  | fname |
| 2 | pk_pmts_task_code_l |  | fpkid |
| 3 | idx_pmts_taskcl_fid |  | fid,flocaleid |
