# 查询任务记录-cdm_querytaskinfo

## 查询任务记录-主表 t_cdm_querytask

- **表名称：** 查询任务记录-主表
- **表名：** t_cdm_querytask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 4 | fquerytype | 查询类型 | varchar | 50 |  | √ | ' ' | 查询类型,枚举: reply :待签收票据 hold :在手票据 |
| 5 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fexecuteway | 执行方式 | varchar | 50 |  | √ | ' ' | 执行方式,枚举: hand :手工 schedule :调度 |
| 7 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 8 | fnumber | taskId | varchar | 50 |  | √ | ' ' | taskId |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cdm_querytask |  | fid |

---

## 查询任务记录-多语言表 t_cdm_querytask_l

- **表名称：** 查询任务记录-多语言表
- **表名：** t_cdm_querytask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
