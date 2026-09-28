# 鉴定申请单-eafc_appraise_info

## 鉴定申请单-主表 tk_eafc_appraise_info

- **表名称：** 鉴定申请单-主表
- **表名：** tk_eafc_appraise_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 5 | forgid | 申请人业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fk_eafc_type | 鉴定类型 | varchar | 50 |  | √ | ' ' | 鉴定类型,枚举: 1 :保管期限鉴定 2 :开放性鉴定 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fk_eafc_status | 鉴定状态 | varchar | 50 |  | √ | ' ' | 鉴定状态,枚举: 2 :待审批 3 :已完成 4 :已作废 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fk_eafc_approval_time | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 11 | fcreatorid | 申请人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fk_eafc_filecount | 数量 | int8 | 64 |  |  | null | 数量 |
| 13 | fk_eafc_dimension | 鉴定维度 | varchar | 50 |  | √ | ' ' | 鉴定维度,枚举: 1 :案卷级 2 :文件级 |
| 14 | fk_eafc_textfield | 鉴定标题 | varchar | 50 |  | √ | ' ' | 鉴定标题 |
| 15 | fk_eafc_archive_time | fk_eafc_archive_time | varchar | 50 |  | √ | ' ' |  |
| 16 | fk_eafc_desc | 鉴定说明 | varchar | 50 |  | √ | ' ' | 鉴定说明 |
| 17 | fbillno | 鉴定批次号 | varchar | 60 |  | √ | ' ' | 鉴定批次号 |
| 18 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fk_eafc_arcorg | 申请人组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_appraise_info |  | fid |

---

## 单据体-子表 tk_eafc_appraise_item

- **表名称：** 单据体-子表
- **表名：** tk_eafc_appraise_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_archive_num | 档案号 | varchar | 50 |  | √ | ' ' | 档案号 |
| 3 | fk_eafc_fexpire_time | 档案到期时间 | timestamp | 0 |  |  | null | 档案到期时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fk_eafc_file_sign | 题名 | varchar | 50 |  | √ | ' ' | 题名 |
| 6 | fk_eafc_archivetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 7 | fk_eafc_result_des | 鉴定方案描述 | varchar | 50 |  | √ | ' ' | 鉴定方案描述 |
| 8 | fk_eafc_box_no_c | 盒号 | varchar | 50 |  | √ | ' ' | 盒号 |
| 9 | fk_eafc_planid | 方案id | int8 | 64 |  |  | null | 方案id |
| 10 | fk_eafc_entity_status | 存储形式 | varchar | 50 |  | √ | ' ' | 存储形式,枚举: 1 :电子 2 :电子+纸质 |
| 11 | fk_eafc_basedatafield | 账簿类型 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 12 | fk_eafc_fexpire_time_n | 调整后档案到期时间 | timestamp | 0 |  |  | null | 调整后档案到期时间 |
| 13 | fk_eafc_storage_period | 保管期限 | varchar | 50 |  | √ | ' ' | 保管期限,枚举: 1 :10年 2 :30年 3 :永久 |
| 14 | fk_eafc_relation_fid | 关联ID | varchar | 50 |  | √ | ' ' | 关联ID |
| 15 | fk_eafc_storage_period_n | 调整后保管期限 | varchar | 50 |  | √ | ' ' | 调整后保管期限,枚举: 1 :十年 2 :三十年 3 :永久 |
| 16 | fk_eafc_period | 期间 | timestamp | 0 |  |  | null | 期间 |
| 17 | fk_eafc_item_org | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fk_eafc_volume_c | 卷号 | varchar | 50 |  | √ | ' ' | 卷号 |
| 19 | fk_eafc_encrypt_type | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 20 | fk_eafc_file_count | 文件数 | int8 | 64 |  |  | null | 文件数 |
| 21 | fk_eafc_item_dimension | 鉴定维度 | varchar | 50 |  | √ | ' ' | 鉴定维度,枚举: 1 :案卷级 2 :文件级 |
| 22 | fk_eafc_combofield | 开放标识 | varchar | 50 |  | √ | ' ' | 开放标识,枚举: 1 :开放 2 :控制 3 :延期开放 |
| 23 | fk_eafc_store_info | 存储位置 | varchar | 50 |  | √ | ' ' | 存储位置 |
| 24 | fk_eafc_item_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 25 | fk_eafc_result | 鉴定结果 | varchar | 50 |  | √ | ' ' | 鉴定结果,枚举: 1 :延期 2 :销毁 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 27 | fk_eafc_file_page | 页数 | int8 | 64 |  |  | null | 页数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_appraise_item_fk |  | fid |
| 2 | pk__eafc_appraise_item |  | fentryid |
