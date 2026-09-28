# 档案销毁-eafc_destruction_info

## 档案销毁-主表 tk_eafc_destruction_info

- **表名称：** 档案销毁-主表
- **表名：** tk_eafc_destruction_info

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_destruction_name | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 3 | fk_eafc_backup_desc | 异地容灾备份内容处置说明 | varchar | 50 |  | √ | ' ' | 异地容灾备份内容处置说明 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fk_eafc_destruction_time | 处置时间 | timestamp | 0 |  |  | null | 处置时间 |
| 6 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatetime | 提交时间 | timestamp | 0 |  |  | null | 提交时间 |
| 8 | forgid | 申请人业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fk_eafc_operator | 操作者 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 11 | fk_eafc_batchnum | 处置批次 | varchar | 50 |  | √ | ' ' | 处置批次 |
| 12 | fk_eafc_item_count | 数量 | int8 | 64 |  |  | null | 数量 |
| 13 | fk_eafc_operator_org | 操作者组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fk_eafc_status | 处置状态 | varchar | 50 |  | √ | ' ' | 处置状态,枚举: 1 :待处置 2 :处置中 3 :已处置 |
| 15 | fk_eafc_appraise_batchnum | 鉴定批次号 | varchar | 50 |  | √ | ' ' | 鉴定批次号 |
| 16 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 17 | fcreatorid | 申请人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fk_eafc_dimension | 档案维度 | varchar | 50 |  | √ | ' ' | 档案维度,枚举: 1 :案卷级 2 :文件级 |
| 19 | fk_eafc_reason | 处置原因 | varchar | 50 |  | √ | ' ' | 处置原因 |
| 20 | fk_eafc_offline_desc | 离线存储介质处置说明 | varchar | 50 |  | √ | ' ' | 离线存储介质处置说明 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fk_eafc_arcorg | 申请人组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 24 | fk_eafc_online_desc | 在线存储内容处置说明 | varchar | 50 |  | √ | ' ' | 在线存储内容处置说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_destruction_info |  | fid |

---

## 单据体-子表 tk_eafc_destruction_item

- **表名称：** 单据体-子表
- **表名：** tk_eafc_destruction_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_relation_fid | 关联ID | varchar | 50 |  | √ | ' ' | 关联ID |
| 3 | fk_eafc_archive_num | 档案号 | varchar | 50 |  | √ | ' ' | 档案号 |
| 4 | fk_eafc_period | 期间 | timestamp | 0 |  |  | null | 期间 |
| 5 | fk_eafc_item_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fk_eafc_fexpire_time | 档案到期时间 | timestamp | 0 |  |  | null | 档案到期时间 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fk_eafc_file_sign | 题名 | varchar | 50 |  | √ | ' ' | 题名 |
| 9 | fk_eafc_archivetime | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 10 | fk_eafc_box_no_c | 盒号 | varchar | 50 |  | √ | ' ' | 盒号 |
| 11 | fk_eafc_appraise_batchnum | 关联鉴定批次 | varchar | 50 |  | √ | ' ' | 关联鉴定批次 |
| 12 | fk_eafc_volume_c | 卷号 | varchar | 50 |  | √ | ' ' | 卷号 |
| 13 | fk_eafc_entity_status | 载体形态 | varchar | 50 |  | √ | ' ' | 载体形态,枚举: 1 :实物 2 :电子 3 :混合 |
| 14 | fk_eafc_basedatafield | 账簿类型 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 15 | fk_eafc_encrypt_type | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 16 | fk_eafc_file_count | 文件数 | int8 | 64 |  |  | null | 文件数 |
| 17 | fk_eafc_item_dimension | 鉴定维度 | varchar | 50 |  | √ | ' ' | 鉴定维度,枚举: |
| 18 | fk_eafc_combofield | 开放标识 | varchar | 50 |  | √ | ' ' | 开放标识,枚举: 1 :开放 2 :控制 3 :延期开放 |
| 19 | fk_eafc_store_info | 存储位置 | varchar | 50 |  | √ | ' ' | 存储位置 |
| 20 | fk_eafc_item_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 21 | fk_eafc_storage_period | 保管期限 | varchar | 50 |  | √ | ' ' | 保管期限,枚举: 1 :10年 2 :30年 3 :永久 |
| 22 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 23 | fk_eafc_file_page | 页数 | int8 | 64 |  |  | null | 页数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_destruction_item |  | fentryid |
| 2 | idx__eafc_destruction_item_fk |  | fid |
