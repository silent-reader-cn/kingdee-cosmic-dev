# 档案盒盘点-eafc_voucher_soft_box

## 档案盒盘点-主表 tk_eafc_voucher_soft_box

- **表名称：** 档案盒盘点-主表
- **表名：** tk_eafc_voucher_soft_box

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_volume_pk | 卷id | varchar | 50 |  | √ | ' ' | 卷id |
| 3 | fk_eafc_box_source | 盒子来源 | varchar | 50 |  | √ | ' ' | 盒子来源,枚举: 1 :收单机 2 :手工 |
| 4 | fk_eafc_min_file_code | 最小文件编号 | varchar | 500 |  | √ | ' ' | 最小文件编号 |
| 5 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 6 | fk_eafc_catalogue | 目录 | int4 | 32 |  | √ | 0 | 目录 |
| 7 | fk_eafc_daterange_s | 起止时间.开始 | timestamp | 0 |  |  | null | 起止时间.开始 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fk_eafc_book | 册数 | varchar | 50 |  | √ | ' ' | 册数 |
| 10 | fk_eafc_daterange_e | 起止时间.结束 | timestamp | 0 |  |  | null | 起止时间.结束 |
| 11 | fk_eafc_mask | 标记 | varchar | 50 |  | √ | ' ' | 标记 |
| 12 | fk_eafc_general_org | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fk_eafc_volume | 案卷号 | varchar | 500 |  | √ | ' ' | 案卷号 |
| 15 | fk_eafc_month | 月份 | varchar | 50 |  | √ | ' ' | 月份,枚举: 1 :1 2 :2 3 :3 4 :4 5 :5 6 :6 7 :7 8 :8 9 :9 10 :10 11 :11 12 :12 |
| 16 | fk_eafc_shelf_location_ob | 上架位置（层-节） | int8 | 64 |  |  | null | [层节设置(基础资料) eafc_floor_config_base](../estore_files/eafc_floor_config_base.md) |
| 17 | fk_eafc_storage_period | 保管期限 | varchar | 50 |  | √ | ' ' | 保管期限,枚举: 1 :10年 2 :30年 3 :永久 |
| 18 | fk_eafc_max_file_code | 最大文件编号 | varchar | 500 |  | √ | ' ' | 最大文件编号 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fk_eafc_business | 三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 21 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 22 | fk_eafc_boxwidth | 盒脊宽度 | varchar | 50 |  | √ | ' ' | 盒脊宽度,枚举: 1 :20mm 2 :40mm 3 :60mm |
| 23 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fk_eafc_pagecount | 页数 | int8 | 64 |  |  | null | 页数 |
| 25 | fk_eafc_box_name | 盒子题名 | varchar | 500 |  | √ | ' ' | 盒子题名 |
| 26 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fk_eafc_capacity | 总容量 | int8 | 64 |  |  | null | 总容量 |
| 29 | fk_eafc_used_capacity | 已占用 | int8 | 64 |  |  | null | 已占用 |
| 30 | fk_eafc_box_status | 盒状态 | varchar | 50 |  | √ | ' ' | 盒状态,枚举: 1 :已上架 2 :未上架 |
| 31 | fk_eafc_billcount | 件数 | int8 | 64 |  |  | null | 件数 |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | fk_eafc_billnumrange | 起止件号 | varchar | 50 |  | √ | ' ' | 起止件号 |
| 34 | fk_fpy_storage_status | 是否出库 | varchar | 50 |  | √ | '1' | 是否出库,枚举: 1 :未出库 2 :已出库 |
| 35 | fk_eafc_encrypt_type | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 36 | fk_eafc_shelf_location | fk_eafc_shelf_location | varchar | 50 |  | √ | ' ' |  |
| 37 | fk_eafc_year | 年度 | timestamp | 0 |  |  | null | 年度 |
| 38 | fk_eafc_orgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fk_eafc_userate | 使用率 | int8 | 64 |  |  | null | 使用率 |
| 40 | fk_eafc_box_num | 盒号 | varchar | 500 |  | √ | ' ' | 盒号 |
| 41 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_voucher_soft_box |  | fid |
