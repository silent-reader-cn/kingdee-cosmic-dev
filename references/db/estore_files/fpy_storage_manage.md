# 出库管理单-fpy_storage_manage

## 出库管理单-主表 tk_fpy_storage_manage

- **表名称：** 出库管理单-主表
- **表名：** tk_fpy_storage_manage

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_fpy_total_amount | 应出库数量 | int4 | 32 |  | √ | 0 | 应出库数量 |
| 3 | fk_fpy_storage_out_amount | 已出库数量 | int4 | 32 |  | √ | 0 | 已出库数量 |
| 4 | fk_fpy_carrier_type | 载体形态 | varchar | 50 |  | √ | ' ' | 载体形态,枚举: 1 :档案盒 2 :案卷 3 :文件 |
| 5 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fk_fpy_batch_no | 出库批次 | varchar | 50 |  | √ | ' ' | 出库批次 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fk_fpy_giveback | 是否需要归还 | varchar | 50 |  | √ | ' ' | 是否需要归还,枚举: 1 :是 2 :否 |
| 10 | fk_fpy_giveback_date | 归还到期日期 | timestamp | 0 |  |  | null | 归还到期日期 |
| 11 | fk_fpy_manuscript | 稿本 | varchar | 50 |  | √ | ' ' | 稿本,枚举: 1 :原件 2 :打印副本 |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fk_eafc_arcorg | 申请人组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 14 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 1 :待出库 2 :已出库 3 :已作废 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fk_fpy_apply_time | 申请时间 | timestamp | 0 |  |  | null | 申请时间 |
| 18 | fk_fpy_remark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fk_fpy_applicant | 申请人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fk_fpy_store_type | 出库类型 | varchar | 50 |  | √ | ' ' | 出库类型,枚举: 1 :库房移交 2 :档案盘点 3 :其他 4 :档案借阅 5 :档案鉴定 6 :档案销毁 7 :档案移交 |
| 22 | fk_fpy_store_reason | 出库事由 | varchar | 200 |  | √ | ' ' | 出库事由 |
| 23 | fk_fpy_invalid_reason | 作废原因 | varchar | 200 |  | √ | ' ' | 作废原因 |
| 24 | fk_fpy_store_time | 出库时间 | timestamp | 0 |  |  | null | 出库时间 |
| 25 | fk_fpy_apply_no | 关联申请单号 | varchar | 50 |  | √ | ' ' | 关联申请单号 |
| 26 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fk_fpy_store_user | 出库人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_storage_manage |  | fid |

---

## 单据体-子表 tk_fpy_storage_manag_item

- **表名称：** 单据体-子表
- **表名：** tk_fpy_storage_manag_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_fpy_volume_amount | 案卷数 | int4 | 32 |  | √ | 0 | 案卷数 |
| 3 | fk_fpy_related_id | 关联id | int8 | 64 |  | √ | 0 | 关联id |
| 4 | fk_fpy_box_name | 盒子题名 | varchar | 100 |  | √ | ' ' | 盒子题名 |
| 5 | fk_fpy_bill_amount | 文件数 | int4 | 32 |  | √ | 0 | 文件数 |
| 6 | fk_fpy_file_sign | 文件题名 | varchar | 200 |  | √ | ' ' | 文件题名 |
| 7 | fk_fpy_storage_out_flag | 是否要出库 | varchar | 50 |  | √ | ' ' | 是否要出库,枚举: 1 :是 2 :否 |
| 8 | fk_fpy_shelf_location_obj | 上架位置（层-节） | int8 | 64 |  |  | null | [层节设置(基础资料) eafc_floor_config_base](../estore_files/eafc_floor_config_base.md) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fk_fpy_box_no | 盒号 | varchar | 100 |  | √ | ' ' | 盒号 |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fk_fpy_volume_name | 案卷题名 | varchar | 200 |  | √ | ' ' | 案卷题名 |
| 13 | fk_fpy_archivenum | 档号 | varchar | 100 |  | √ | ' ' | 档号 |
| 14 | fk_fpy_storage_status | 出库状态 | varchar | 50 |  | √ | ' ' | 出库状态,枚举: 1 :未出库 2 :已出库 |
| 15 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_storage_manag_item |  | fentryid |
