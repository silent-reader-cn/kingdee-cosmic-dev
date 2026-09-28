# 移交归档日志-eafc_record_save

## 关联文件分录-子表 tk_eafc_record_save_file

- **表名称：** 关联文件分录-子表
- **表名：** tk_eafc_record_save_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_file_code | 文件编码 | varchar | 50 |  | √ | ' ' | 文件编码 |
| 3 | fk_eafc_file_uniqueid | 文件唯一编号 | varchar | 50 |  | √ | ' ' | 文件唯一编号 |
| 4 | fk_eafc_file_business | 三级分类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 5 | fk_eafc_file_pkid | 文件 | varchar | 50 |  | √ | ' ' | 文件 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fk_eafc_file_sign | 文件题名 | varchar | 50 |  | √ | ' ' | 文件题名 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_record_save_file |  | fentryid |
| 2 | idx__eafc_record_save_file_fk |  | fid |

---

## 移交归档日志-主表 tk_eafc_record_save

- **表名称：** 移交归档日志-主表
- **表名：** tk_eafc_record_save

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_inspect_virus | 病毒检测 | varchar | 50 |  | √ | ' ' | 病毒检测,枚举: 1 :通过 2 :不通过 |
| 3 | fk_eafc_outline | 是否离线 | varchar | 50 |  | √ | ' ' | 是否离线,枚举: 1 :√ 2 :× |
| 4 | fk_eafc_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fk_eafc_record_name | 登记名称 | varchar | 100 |  | √ | ' ' | 登记名称 |
| 6 | fk_eafc_inspect_form | 载体外观检测 | varchar | 50 |  | √ | ' ' | 载体外观检测,枚举: 1 :通过 2 :不通过 |
| 7 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 8 | fk_eafc_archivetime | 编目时间 | timestamp | 0 |  |  | null | 编目时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fk_eafc_inspect_trust | 真实性检测 | varchar | 50 |  | √ | ' ' | 真实性检测,枚举: 1 :通过 2 :不通过 |
| 11 | fk_eafc_inspect_tech | 技术方法检测 | varchar | 50 |  | √ | ' ' | 技术方法检测,枚举: 1 :通过 2 :不通过 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fk_eafc_archive_type | 一级门类 | int8 | 64 |  |  | null | [档案类型（一级） eafc_archive_type](../ebase_files/eafc_archive_type.md) |
| 14 | fk_eafc_dimension | 档案维度 | varchar | 50 |  | √ | ' ' | 档案维度,枚举: 1 :案卷级 2 :文件级 |
| 15 | fk_eafc_record_org | 登记单位 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fk_eafc_mark_tag | 内容描述_详情 | text | 0 |  |  | null | 内容描述_详情 |
| 17 | fk_eafc_inspect | 四性检测 | varchar | 50 |  | √ | ' ' | 四性检测,枚举: 1 :通过 2 :不通过 |
| 18 | fk_eafc_count | 文件数 | int8 | 64 |  |  | null | 文件数 |
| 19 | fk_eafc_inspect_safety | 安全性检测 | varchar | 50 |  | √ | ' ' | 安全性检测,枚举: 1 :通过 2 :不通过 |
| 20 | fk_eafc_line_type | 归档方式 | varchar | 50 |  | √ | ' ' | 归档方式,枚举: 1 :在线 2 :离线 3 :在线+离线 |
| 21 | fbillno | 批次号 | varchar | 30 |  | √ | ' ' | 批次号 |
| 22 | fk_eafc_record_user | 登记人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fk_eafc_business | 三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 24 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 25 | fk_eafc_volume_count | 卷数 | int8 | 64 |  |  | null | 卷数 |
| 26 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fk_eafc_pagecount | 页数 | int8 | 64 |  |  | null | 页数 |
| 28 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fk_eafc_format | 存储形式 | varchar | 50 |  | √ | ' ' | 存储形式,枚举: 1 :电子 2 :电子+纸质 3 :混合 |
| 31 | fk_eafc_inspect_usability | 可用性检测 | varchar | 50 |  | √ | ' ' | 可用性检测,枚举: 1 :通过 2 :不通过 |
| 32 | fk_eafc_checktime | 检测时间 | timestamp | 0 |  |  | null | 检测时间 |
| 33 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 34 | fk_eafc_status | 归档状态 | varchar | 50 |  | √ | ' ' | 归档状态,枚举: 1 :归档中 2 :已归档 3 :归档失败 4 :反归档中 5 :反归档 6 :反归档失败 |
| 35 | fk_eafc_online | 是否在线 | varchar | 50 |  | √ | ' ' | 是否在线,枚举: 1 :√ 2 :× |
| 36 | fk_eafc_inspect_type | 检测方式 | varchar | 50 |  | √ | ' ' | 检测方式,枚举: 1 :系统检测 2 :人工检测 |
| 37 | fk_eafc_mark | 内容描述 | varchar | 255 |  | √ | ' ' | 内容描述 |
| 38 | fk_eafc_inspect_complete | 完整性检测 | varchar | 50 |  | √ | ' ' | 完整性检测,枚举: 1 :通过 2 :不通过 |
| 39 | fk_eafc_step | 进行步骤 | int8 | 64 |  |  | null | 进行步骤 |
| 40 | fk_eafc_file_count | 件数 | int8 | 64 |  |  | null | 件数 |
| 41 | fk_eafc_record_date | 登记时间 | timestamp | 0 |  |  | null | 登记时间 |
| 42 | fk_eafc_recordtab_url | 登记表下载地址 | varchar | 500 |  | √ | ' ' | 登记表下载地址 |
| 43 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_record_save |  | fid |
