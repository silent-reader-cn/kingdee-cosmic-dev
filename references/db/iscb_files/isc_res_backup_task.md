# 资源备份管理-isc_res_backup_task

## 资源备份管理-主表 t_iscb_backup_task

- **表名称：** 资源备份管理-主表
- **表名：** t_iscb_backup_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 500 |  |  | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 备份任务名称 | varchar | 50 |  |  | ' ' | 备份任务名称 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fbillstatus | 任务状态 | varchar | 50 |  |  | ' ' | 任务状态,枚举: A :暂存 B :备份中 C :备份成功 |
| 7 | fpush_url | 推送地址 | varchar | 500 |  |  | ' ' | 推送地址 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 9 | fbillno | 备份任务编码 | varchar | 50 |  |  | ' ' | 备份任务编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_backup_task |  | fid |
| 2 | idx_backup_task |  | fbillno |

---

## 备份主资源-子表 t_iscb_backup_task_main

- **表名称：** 备份主资源-子表
- **表名：** t_iscb_backup_task_main

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fres_type | 资源类型 | varchar | 36 |  |  | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  |  | null | 分录行号 |
| 4 | fres_pk | 资源ID | varchar | 50 |  |  | ' ' | 资源ID |
| 5 | fres_name | 资源名称 | varchar | 100 |  |  | ' ' | 资源名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fres_number | 资源编码 | varchar | 100 |  |  | ' ' | 资源编码 |
| 8 | fres_time | 最近修改时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 最近修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iscb_backup_task_main |  | fentryid |
| 2 | idx_iscb_backup_task_main_fk |  | fid |
