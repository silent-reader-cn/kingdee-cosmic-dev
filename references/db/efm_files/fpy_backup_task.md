# 备份任务单-fpy_backup_task

## 备份任务单-主表 tk_fpy_backup_task

- **表名称：** 备份任务单-主表
- **表名：** tk_fpy_backup_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :待备份 B :备份中 C :备份成功 D :备份失败 |
| 4 | fk_fpy_reason | 原因描述 | varchar | 1000 |  | √ | ' ' | 原因描述 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fk_fpy_execution_time | 执行耗时 | varchar | 50 |  | √ | ' ' | 执行耗时 |
| 7 | fk_eafc_book_type | 机构问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 8 | fk_fpy_volume_relationid | 案卷id | int8 | 64 |  | √ | 0 | 案卷id |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fk_eafc_start_time | 备份开始时间 | timestamp | 0 |  |  | null | 备份开始时间 |
| 11 | fk_fpy_total_size | 文件大小 | varchar | 50 |  | √ | ' ' | 文件大小 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fk_fpy_file_name | 文件名称 | varchar | 100 |  | √ | ' ' | 文件名称 |
| 15 | fk_fpy_file_address | 文件地址 | varchar | 200 |  | √ | ' ' | 文件地址 |
| 16 | fk_fpy_apply_no | 关联申请单号 | varchar | 50 |  | √ | ' ' | 关联申请单号 |
| 17 | fbillno | 备份任务编号 | varchar | 30 |  | √ | ' ' | 备份任务编号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fk_eafc_arcorg | 备份组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 20 | fk_eafc_business | 三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_backup_task_billno |  | fbillno |
| 2 | idx_backup_task_applyno |  | fk_fpy_apply_no |
| 3 | pk_fpy_backup_task |  | fid |

---

## 单据体-子表 tk_fpy_backup_task_item

- **表名称：** 单据体-子表
- **表名：** tk_fpy_backup_task_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_fpy_eafc_arcorg_bill | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 3 | fk_eafc_period | 属期 | timestamp | 0 |  |  | null | 属期 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fk_eafc_file_sign | 文件题名 | varchar | 200 |  | √ | ' ' | 文件题名 |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fk_fpy_eafc_book_type_bill | 机构问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 8 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fk_eafc_file_code | 文件编号 | varchar | 100 |  | √ | ' ' | 文件编号 |
| 10 | fk_fpy_relation_id | 文件检索id | varchar | 50 |  | √ | ' ' | 文件检索id |
| 11 | fk_eafc_entity_status | 存储形式 | varchar | 50 |  | √ | ' ' | 存储形式,枚举: 1 :电子 2 :电子+纸质 |
| 12 | fk_eafc_archivenum | 档号 | varchar | 100 |  | √ | ' ' | 档号 |
| 13 | fk_eafc_shelf_location | 存储位置 | int8 | 64 |  |  | null | [层节设置(基础资料) eafc_floor_config_base](../estore_files/eafc_floor_config_base.md) |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fk_eafc_business_type | 分类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_backup_task_item |  | fentryid |
