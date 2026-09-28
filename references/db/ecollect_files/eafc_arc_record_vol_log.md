# 登记归档日志-案卷-eafc_arc_record_vol_log

## 登记归档日志-案卷-主表 tk_eafc_arc_record_vollog

- **表名称：** 登记归档日志-案卷-主表
- **表名：** tk_eafc_arc_record_vollog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fk_eafc_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fk_eafc_volume_name | 案卷题名 | varchar | 500 |  | √ | ' ' | 案卷题名 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fk_eafc_catalogue | 目录号 | varchar | 50 |  | √ | ' ' | 目录号 |
| 8 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fk_eafc_status | 归档状态 | varchar | 50 |  | √ | ' ' | 归档状态,枚举: 1 :归档中 2 :已归档 3 :归档失败 4 :反归档中 5 :反归档 6 :反归档失败 |
| 11 | fk_eafc_pkid | 案卷id | int8 | 64 |  | √ | 0 | 案卷id |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fk_eafc_basedatafield | 二级门类 | int8 | 64 |  |  | null | [档案门类（二级） eafc_category](../ebase_files/eafc_category.md) |
| 15 | fk_eafc_archivenum | 档号 | varchar | 500 |  | √ | ' ' | 档号 |
| 16 | fk_eafc_volume | 案卷号 | varchar | 500 |  | √ | ' ' | 案卷号 |
| 17 | fk_eafc_status_desc | 状态描述 | varchar | 2000 |  | √ | ' ' | 状态描述 |
| 18 | fk_eafc_showperiod | 期间 | varchar | 50 |  | √ | ' ' | 期间 |
| 19 | fbillno | 批次号 | varchar | 30 |  | √ | ' ' | 批次号 |
| 20 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fk_eafc_business | 三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 22 | fk_eafc_arcorg | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_arc_record_vollog |  | fid |
