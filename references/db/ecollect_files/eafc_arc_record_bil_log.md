# 登记归档日志-文件-eafc_arc_record_bil_log

## 登记归档日志-文件-主表 tk_eafc_arc_record_billog

- **表名称：** 登记归档日志-文件-主表
- **表名：** tk_eafc_arc_record_billog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fk_eafc_open_log | 开放标识 | varchar | 50 |  | √ | ' ' | 开放标识,枚举: 1 :开放 2 :控制 3 :延期开放 |
| 4 | fk_eafc_catalogue | 目录号 | varchar | 50 |  | √ | ' ' | 目录号 |
| 5 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 6 | fk_eafc_file_sign | 文件题名 | varchar | 500 |  | √ | ' ' | 文件题名 |
| 7 | fk_eafc_volume_serial_no | 卷内序号 | int4 | 32 |  | √ | 0 | 卷内序号 |
| 8 | fk_eafc_pkid | 文件id | int8 | 64 |  | √ | 0 | 文件id |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fk_eafc_filecount | 文件数 | int4 | 32 |  | √ | 0 | 文件数 |
| 12 | fk_eafc_entity_status | 存储形式 | varchar | 50 |  | √ | ' ' | 存储形式,枚举: 1 :电子 2 :电子+纸质 |
| 13 | fk_eafc_basedatafield | 二级门类 | int8 | 64 |  |  | null | [档案门类（二级） eafc_category](../ebase_files/eafc_category.md) |
| 14 | fk_eafc_archivenum | 档号 | varchar | 500 |  | √ | ' ' | 档号 |
| 15 | fk_eafc_rel_volume_id | 关联案卷id | int8 | 64 |  | √ | 0 | 关联案卷id |
| 16 | fk_eafc_storage_period | 保管期限 | varchar | 50 |  | √ | ' ' | 保管期限,枚举: 1 :十年 2 :三十年 3 :永久 |
| 17 | fbillno | 批次号 | varchar | 30 |  | √ | ' ' | 批次号 |
| 18 | fk_eafc_business | 三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 19 | fk_eafc_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 20 | fk_eafc_arcorg | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 21 | fk_eafc_code | 文件编号 | varchar | 500 |  | √ | ' ' | 文件编号 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fk_eafc_pagecount | 页数 | int4 | 32 |  | √ | 0 | 页数 |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fk_eafc_period | 会计期间 | timestamp | 0 |  |  | null | 会计期间 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fk_eafc_status | 归档状态 | varchar | 50 |  | √ | ' ' | 归档状态,枚举: 1 :归档中 2 :已归档 3 :归档失败 4 :反归档中 5 :反归档 6 :反归档失败 |
| 29 | fk_eafc_encrypt_type | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 30 | fk_eafc_status_desc | 状态描述 | varchar | 2000 |  | √ | ' ' | 状态描述 |
| 31 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fk_eafc_duty_user | 责任人 | varchar | 50 |  | √ | ' ' | 责任人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_arc_record_billog |  | fid |
