# 移交归档审批-fpy_formal_archive

## 移交归档审批-主表 tk_fpy_formal_archive

- **表名称：** 移交归档审批-主表
- **表名：** tk_fpy_formal_archive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_fpy_eafc_volume_count | 案卷数 | int4 | 32 |  | √ | 0 | 案卷数 |
| 3 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 4 | foptype | 操作类型 | varchar | 2 |  | √ | ' ' | 操作类型,枚举: A :归档 B :反归档 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fk_fpy_eafc_file_count | 文件数 | int4 | 32 |  | √ | 0 | 文件数 |
| 8 | fbillno | 正式归档批次 | varchar | 30 |  | √ | ' ' | 正式归档批次 |
| 9 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 10 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fk_fpy_eafc_archive_org | 归档部门 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fk_fpy_eafc_archive_user | 归档人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 16 | fk_fpy_eafc_user_org | 归档人单位 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fk_eafc_user_org | 归档人单位 | int8 | 64 |  | √ | 0 | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 18 | fk_fpy_eafc_current_org | 所属部门 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fk_fpy_eafc_dimension | 档案维度 | varchar | 50 |  | √ | ' ' | 档案维度,枚举: 1 :案卷级 2 :文件级 |
| 20 | fk_fpy_eafc_business | 归档分类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 21 | fk_fpy_eafc_line_type | 归档方式 | varchar | 50 |  | √ | ' ' | 归档方式,枚举: 1 :在线 2 :离线 3 :在线+离线 |
| 22 | fk_fpy_eafc_mark | 内容描述 | varchar | 255 |  | √ | ' ' | 内容描述 |
| 23 | fk_fpy_eafc_mark_tag | 内容描述_详情 | text | 0 |  |  | null | 内容描述_详情 |
| 24 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fk_fpy_eafc_archive_date | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_formal_archive |  | fid |

---

## 案卷单据体-子表 tk_eafc_formal_volume

- **表名称：** 案卷单据体-子表
- **表名：** tk_eafc_formal_volume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_fpy_eafc_volume_id | 案卷id | varchar | 50 |  | √ | ' ' | 案卷id |
| 3 | fk_fpy_eafc_desc | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 4 | fk_fpy_eafc_volume | 案卷号 | varchar | 50 |  | √ | ' ' | 案卷号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fk_fpy_eafc_arcorg2 | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 8 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fk_fpy_eafc_entity_status | 载体形态 | varchar | 50 |  | √ | ' ' | 载体形态,枚举: 1 :电子 2 :实物 3 :混合 |
| 10 | fk_fpy_eafc_encrypt_type | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 11 | fk_fpy_eafc_period | 期间 | varchar | 50 |  | √ | ' ' | 期间 |
| 12 | fk_fpy_eafc_volume_name | 案卷题名 | varchar | 200 |  | √ | ' ' | 案卷题名 |
| 13 | fk_eafc_storage_period | 保管期限 | varchar | 50 |  | √ | ' ' | 保管期限,枚举: 1 :十年 2 :三十年 3 :永久 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fk_eafc_location_volume | 存储位置 | varchar | 50 |  | √ | ' ' | 存储位置 |
| 16 | fk_fpy_eafc_open_log | 开放标识 | varchar | 50 |  | √ | ' ' | 开放标识,枚举: 1 :开放 2 :控制 3 :延期开放 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_formal_volume |  | fentryid |
