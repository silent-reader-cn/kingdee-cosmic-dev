# 备份申请单-fpy_offline_backup

## 机构问题-多选基础资料表 tk_fpy_backup_mul_book

- **表名称：** 机构问题-多选基础资料表
- **表名：** tk_fpy_backup_mul_book

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_backup_mul_book |  | fpkid |

---

## 备份申请单-主表 tk_fpy_backup

- **表名称：** 备份申请单-主表
- **表名：** tk_fpy_backup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fk_fpy_start_time | 备份开始月份 | timestamp | 0 |  |  | null | 备份开始月份 |
| 4 | fk_fpy_backup_type | 备份方式 | varchar | 50 |  | √ | ' ' | 备份方式,枚举: 1 :案卷 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 申请人业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fk_fpy_end_time | 备份结束月份 | timestamp | 0 |  |  | null | 备份结束月份 |
| 11 | fcreatorid | 申请人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fk_fpy_general_archive | 备份组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 13 | fk_fpy_description | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 14 | fbillno | 备份任务编码 | varchar | 30 |  | √ | ' ' | 备份任务编码 |
| 15 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fk_eafc_arcorg | 申请人组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_backup_billno |  | fbillno |
| 2 | pk_fpy_backup |  | fid |

---

## 备份目录-子表 tk_fpy_backup_item

- **表名称：** 备份目录-子表
- **表名：** tk_fpy_backup_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_fpy_category_no | 类别号 | varchar | 50 |  | √ | ' ' | 类别号 |
| 3 | fk_fpy_category_name | 类别名称 | varchar | 50 |  | √ | ' ' | 类别名称 |
| 4 | fk_fpy_volume_num | 案卷数 | int4 | 32 |  | √ | 0 | 案卷数 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_backup_item |  | fentryid |
