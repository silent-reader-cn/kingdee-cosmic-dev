# 扫码单据-fpy_scan_bill

## 扫码单据-主表 tk_fpy_scan_bill

- **表名称：** 扫码单据-主表
- **表名：** tk_fpy_scan_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_fpy_period | 属期 | timestamp | 0 |  |  | null | 属期 |
| 3 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 5 | fk_fpy_billno | 单据编号 | varchar | 32 |  | √ | ' ' | 单据编号 |
| 6 | fk_fpy_file_status | 实物状态 | varchar | 50 |  | √ | ' ' | 实物状态,枚举: 1 :已装盒 2 :虚拟装盒 3 :未装盒 |
| 7 | fk_fpy_entity_status | 存储形式 | varchar | 50 |  | √ | ' ' | 存储形式,枚举: 1 :电子 2 :电子+纸质 |
| 8 | fk_fpy_box_no | 盒号 | varchar | 50 |  | √ | ' ' | 盒号 |
| 9 | fk_fpy_scanbillno | 单据的影像编号 | varchar | 32 |  | √ | ' ' | 单据的影像编号 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fk_fpy_archivenum | 档案号 | varchar | 100 |  | √ | ' ' | 档案号 |
| 12 | fk_eafc_general_org | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fk_fpy_page_id | 页面id | varchar | 50 |  | √ | ' ' | 页面id |
| 15 | fk_fpy_data_status | 文件状态 | varchar | 50 |  | √ | ' ' | 文件状态,枚举: 1 :待匹配 2 :待组卷 3 :已组卷 4 :归档中 5 :已归档 9 :被移除 11 :异常 12 :检测中 |
| 16 | fk_fpy_billtime | 单据创建时间 | timestamp | 0 |  |  | null | 单据创建时间 |
| 17 | fk_fpy_box | 盒子id | int8 | 64 |  |  | null | 盒子id |
| 18 | fk_fpy_box_status | 装盒状态 | varchar | 50 |  | √ | ' ' | 装盒状态,枚举: 1 :未装盒 2 :虚拟装盒 3 :已装盒 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fk_fpy_isrel_voucher | 是否已关联凭证 | bpchar | 1 |  | √ | '0' | 是否已关联凭证 |
| 21 | fk_fpy_billname | 单据名称 | varchar | 32 |  | √ | ' ' | 单据名称 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fk_fpy_bill_id | 单据id | int8 | 64 |  | √ | null | 单据id |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fk_fpy_file_sign | 文件题名 | varchar | 200 |  | √ | ' ' | 文件题名 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fk_fpy_volume_relationid | 卷id | int8 | 64 |  |  | null | 卷id |
| 28 | fk_fpy_creater | 制单人 | varchar | 32 |  | √ | ' ' | 制单人 |
| 29 | fk_fpy_relate_archivenum | 关联凭证档号 | varchar | 500 |  | √ | ' ' | 关联凭证档号 |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fk_fpy_volume | 案卷号 | varchar | 50 |  | √ | ' ' | 案卷号 |
| 32 | fk_fpy_file_code | 文件编码 | varchar | 100 |  | √ | ' ' | 文件编码 |
| 33 | fk_fpy_shelf_location | 上架位置（层-节） | int8 | 64 |  |  | null | [层节设置(基础资料) eafc_floor_config_base](../estore_files/eafc_floor_config_base.md) |
| 34 | fk_fpy_relate_voucherno | 关联凭证字号 | varchar | 500 |  | √ | ' ' | 关联凭证字号 |
| 35 | fk_fpy_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 36 | fk_fpy_amount | 单据金额 | numeric | 23 | 10 |  | null | 单据金额 |
| 37 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fpy_scan_bill |  | fid |
| 2 | idx_scan_bill_billid |  | fk_fpy_bill_id |
| 3 | idx_scan_bill_pageid |  | fk_fpy_page_id |
