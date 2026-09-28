# 出库申请单-fpy_storage_out

## 单据体-子表 tk_fpy_storage_out_item

- **表名称：** 单据体-子表
- **表名：** tk_fpy_storage_out_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fk_fpy_volume_amount | 案卷数 | int4 | 32 |  | √ | 0 | 案卷数 |
| 3 | fk_fpy_related_id | 关联id | int8 | 64 |  | √ | 0 | 关联id |
| 4 | fk_fpy_box_name | 盒子题名 | varchar | 100 |  | √ | ' ' | 盒子题名 |
| 5 | fk_fpy_bill_amount | 文件数 | int4 | 32 |  | √ | 0 | 文件数 |
| 6 | fk_fpy_file_sign | 文件题名 | varchar | 200 |  | √ | ' ' | 文件题名 |
| 7 | fk_fpy_shelf_location_obj | 上架位置（层-节） | int8 | 64 |  |  | null | [层节设置(基础资料) eafc_floor_config_base](../estore_files/eafc_floor_config_base.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fk_fpy_box_no | 盒号 | varchar | 100 |  | √ | ' ' | 盒号 |
| 10 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fk_fpy_volume_name | 案卷题名 | varchar | 200 |  | √ | ' ' | 案卷题名 |
| 12 | fk_fpy_archivenum | 档号 | varchar | 100 |  | √ | ' ' | 档号 |
| 13 | fk_fpy_storage_status | 出库状态 | varchar | 50 |  | √ | ' ' | 出库状态,枚举: 1 :未出库 2 :已出库 |
| 14 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_storage_out_item |  | fentryid |

---

## 出库申请单-主表 tk_fpy_storage_out

- **表名称：** 出库申请单-主表
- **表名：** tk_fpy_storage_out

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fk_fpy_carrier_type | 载体形态 | varchar | 50 |  | √ | ' ' | 载体形态,枚举: 1 :档案盒 2 :案卷 3 :文件 |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 1 :待提交 2 :审批中 3 :已审批 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fk_fpy_remark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 7 | forgid | 申请人业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fk_fpy_store_type | 出库类型 | varchar | 50 |  | √ | ' ' | 出库类型,枚举: 1 :库房移交 2 :档案盘点 3 :其他 |
| 10 | fk_fpy_store_reason | 出库事由 | varchar | 200 |  | √ | ' ' | 出库事由 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcreatorid | 申请人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fk_fpy_giveback | 是否需要归还 | varchar | 50 |  | √ | ' ' | 是否需要归还,枚举: 1 :是 2 :否 |
| 14 | fk_fpy_giveback_date | 归还到期日期 | timestamp | 0 |  |  | null | 归还到期日期 |
| 15 | fk_fpy_store_out_no | 申请单号 | varchar | 50 |  | √ | ' ' | 申请单号 |
| 16 | fk_fpy_store_amount | 应出库数量 | int4 | 32 |  | √ | 0 | 应出库数量 |
| 17 | fk_fpy_manuscript | 稿本 | varchar | 50 |  | √ | ' ' | 稿本,枚举: 1 :原件 2 :打印副本 |
| 18 | fbillno | 订单号 | varchar | 30 |  | √ | ' ' | 订单号 |
| 19 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fk_eafc_arcorg | 申请人组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_storage_out |  | fid |
