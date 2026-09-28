# 组卷-eafc_volume

## 单据体-子表 tk_eafc_volume_ent

- **表名称：** 单据体-子表
- **表名：** tk_eafc_volume_ent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_ent_book | 册/次 | varchar | 50 |  | √ | ' ' | 册/次 |
| 3 | fk_eafc_ent_billcount | 件数 | int8 | 64 |  |  | null | 件数 |
| 4 | fk_eafc_ent_box_pk | 盒id | varchar | 50 |  | √ | ' ' | 盒id |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fk_eafc_ent_attachment | 附件数 | int8 | 64 |  |  | null | 附件数 |
| 7 | fk_eafc_ent_daterange_e | 起止时间(册).结束 | timestamp | 0 |  |  | null | 起止时间(册).结束 |
| 8 | fk_eafc_ent_maskmsg | 标记信息 | varchar | 200 |  | √ | ' ' | 标记信息 |
| 9 | fk_eafc_ent_pagecount | 页数 | int8 | 64 |  |  | null | 页数 |
| 10 | fk_eafc_ent_boxnum | 盒号 | varchar | 50 |  | √ | ' ' | 盒号 |
| 11 | fk_eafc_ent_billnumrange | 文件起止号(册) | varchar | 50 |  | √ | ' ' | 文件起止号(册) |
| 12 | fk_eafc_ent_picturetype | 提示图片类型 | varchar | 50 |  | √ | ' ' | 提示图片类型,枚举: type1 :保存 type2 :归档中 type3 :可归档 type4 :已标记 type5 :检测异常 type6 :归档失败 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 14 | fk_eafc_ent_daterange_s | 起止时间(册).开始 | timestamp | 0 |  |  | null | 起止时间(册).开始 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_volume_ent |  | fentryid |
| 2 | idx__eafc_volume_ent_fk |  | fid |

---

## 组卷-主表 tk_eafc_volume

- **表名称：** 组卷-主表
- **表名：** tk_eafc_volume

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_volume_name | 案卷题名 | varchar | 500 |  | √ | ' ' | 案卷题名 |
| 3 | fk_eafc_open_log | 开放标识 | varchar | 50 |  | √ | ' ' | 开放标识,枚举: 1 :开放 2 :控制 3 :延期开放 |
| 4 | fk_eafc_book_show | 册号 | varchar | 50 |  | √ | ' ' | 册号 |
| 5 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fk_eafc_update_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fk_eafc_book | 册号(存储) | int8 | 64 |  |  | null | 册号(存储) |
| 9 | fk_eafc_certificates | 凭证合计 | varchar | 50 |  | √ | ' ' | 凭证合计 |
| 10 | fk_eafc_expire_time | 到期时间 | timestamp | 0 |  |  | null | 到期时间 |
| 11 | fk_fpy_examiner | 检查人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fk_eafc_errmsg | 异常信息 | varchar | 200 |  | √ | ' ' | 异常信息 |
| 13 | fk_eafc_general_org | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 14 | fk_eafc_filecount | 单据件数 | int8 | 64 |  |  | null | 单据件数 |
| 15 | fk_fpy_box_serial | 盒内序号 | int8 | 64 |  | √ | 0 | 盒内序号 |
| 16 | fk_eafc_register_time | 登记时间 | timestamp | 0 |  |  | null | 登记时间 |
| 17 | fk_eafc_record_pk | 登记归档id | int8 | 64 |  |  | null | 登记归档id |
| 18 | fk_eafc_month | 月份 | varchar | 50 |  | √ | ' ' | 月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 19 | fk_eafc_quarter | 季度 | varchar | 50 |  | √ | ' ' | 季度,枚举: 1 :第一季度 2 :第二季度 3 :第三季度 4 :第四季度 |
| 20 | fk_eafc_shelf_location_ob | 上架位置（层-节） | int8 | 64 |  |  | null | [层节设置(基础资料) eafc_floor_config_base](../estore_files/eafc_floor_config_base.md) |
| 21 | fk_eafc_voucher_type | 凭证字 | varchar | 50 |  | √ | ' ' | 凭证字 |
| 22 | fk_eafc_storage_period | 保管期限 | varchar | 50 |  | √ | ' ' | 保管期限,枚举: 1 :10年 2 :30年 3 :永久 |
| 23 | fk_eafc_volume_stauts | 案卷状态 | varchar | 50 |  | √ | ' ' | 案卷状态,枚举: 1 :保存 2 :待归档 3 :归档中 10 :反归档中 4 :检测异常 5 :归档失败 6 :已标记 7 :存在异常 8 :已归档 9 :删除 |
| 24 | fk_eafc_arch_detail | 明细维度 | varchar | 2000 |  | √ | ' ' | 明细维度 |
| 25 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 26 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 27 | fk_eafc_boxwidth | 盒脊宽度 | varchar | 50 |  | √ | ' ' | 盒脊宽度 |
| 28 | fk_eafc_boxcapacity | 容量 | varchar | 50 |  | √ | ' ' | 容量 |
| 29 | fk_eafc_pagecount | 页数 | int8 | 64 |  |  | null | 页数 |
| 30 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 31 | fk_eafc_period | 期属 | timestamp | 0 |  |  | null | 期属 |
| 32 | fk_eafc_register | 登记人 | varchar | 50 |  | √ | ' ' | 登记人 |
| 33 | fk_fpy_box_user | 装盒人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fk_eafc_record_no | 归档批次号 | varchar | 50 |  | √ | ' ' | 归档批次号 |
| 35 | fk_eafc_record_person | 归档人 | varchar | 50 |  | √ | ' ' | 归档人 |
| 36 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 37 | fk_eafc_billnumrange | 文件起止号 | varchar | 200 |  | √ | ' ' | 文件起止号 |
| 38 | fk_fpy_storage_status | 是否出库 | varchar | 50 |  | √ | '1' | 是否出库,枚举: 1 :未出库 2 :已出库 |
| 39 | fk_eafc_maskmsg | 标记信息 | varchar | 200 |  | √ | ' ' | 标记信息 |
| 40 | fk_eafc_inspect_detail | 四性检测详情id | int8 | 64 |  |  | null | 四性检测详情id |
| 41 | fk_eafc_box_serialno | 盒内顺序 | int4 | 32 |  | √ | 0 | 盒内顺序 |
| 42 | fk_eafc_encrypt_type | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 43 | fk_eafc_check_result | 检测结果 | varchar | 200 |  | √ | ' ' | 检测结果 |
| 44 | fk_fpy_volume_mode | 组卷方式 | varchar | 50 |  | √ | ' ' | 组卷方式,枚举: 1 :自动组卷 2 :手动组卷 3 :扫码组卷 |
| 45 | fk_eafc_desc | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 46 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fk_eafc_billdateend | 起止时间.结束 | timestamp | 0 |  |  | null | 起止时间.结束 |
| 48 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 49 | fk_eafc_catalogue | 目录 | int8 | 64 |  |  | null | 目录 |
| 50 | fk_fpy_box_date | 装盒日期 | timestamp | 0 |  |  | null | 装盒日期 |
| 51 | fk_eafc_volume_user | 立卷人 | varchar | 50 |  | √ | ' ' | 立卷人 |
| 52 | fk_eafc_save_location | 存储位置 | varchar | 2000 |  | √ | ' ' | 存储位置 |
| 53 | fk_eafc_reviewer | 审核人 | varchar | 50 |  | √ | ' ' | 审核人 |
| 54 | fk_eafc_boxcount | 占用盒数 | int8 | 64 |  |  | null | 占用盒数 |
| 55 | fcreatorid | 责任者 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fk_eafc_book_total_show | 册数 | varchar | 50 |  | √ | ' ' | 册数 |
| 57 | fk_eafc_entity_status | 载体形态 | varchar | 50 |  | √ | ' ' | 载体形态,枚举: 1 :电子 2 :实物 3 :混合 |
| 58 | fk_eafc_basedatafield | 二级门类 | int8 | 64 |  |  | null | [档案门类（二级） eafc_category](../ebase_files/eafc_category.md) |
| 59 | fk_eafc_archivenum | 档案号 | varchar | 500 |  | √ | ' ' | 档案号 |
| 60 | fk_eafc_volume | 卷号 | varchar | 500 |  | √ | ' ' | 卷号 |
| 61 | fk_eafc_archive_time | 立卷时间 | timestamp | 0 |  |  | null | 立卷时间 |
| 62 | fk_eafc_data_stauts | 明细状态 | varchar | 50 |  | √ | ' ' | 明细状态,枚举: 1 :预归档 2 :待整理 3 :已组件 4 :已组卷 5 :待编目 6 :已入库 9 :已删除 |
| 63 | fk_eafc_showperiod | 展示期间 | varchar | 50 |  | √ | ' ' | 展示期间 |
| 64 | fk_eafc_record_time | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 65 | fk_eafc_business | 三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 66 | fk_eafc_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 67 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 68 | fk_eafc_book_total | 册数(存储) | int8 | 64 |  |  | null | 册数(存储) |
| 69 | fk_eafc_check_status | 检测状态 | varchar | 50 |  | √ | ' ' | 检测状态,枚举: 1 :通过 2 :不通过 |
| 70 | fk_eafc_billdatestart | 起止时间.开始 | timestamp | 0 |  |  | null | 起止时间.开始 |
| 71 | fk_eafc_box_name | 盒子题名 | varchar | 50 |  |  | null | 盒子题名 |
| 72 | fk_eafc_boxnumber | 盒号 | varchar | 50 |  | √ | ' ' | 盒号 |
| 73 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 74 | fk_eafc_box | 盒子id | int8 | 64 |  |  | null | 盒子id |
| 75 | fk_eafc_box_width | 盒脊宽度 | varchar | 50 |  |  | null | 盒脊宽度,枚举: 1 :20mm 2 :40mm 3 :60mm |
| 76 | fk_eafc_year | 年度 | timestamp | 0 |  |  | null | 年度 |
| 77 | fk_eafc_halfyear | 半年度 | varchar | 50 |  | √ | ' ' | 半年度,枚举: 1 :上半年 2 :下半年 |
| 78 | fk_eafc_box_num | 盒号 | varchar | 50 |  |  | null | 盒号 |
| 79 | fk_eafc_duty_user | 责任人 | varchar | 50 |  | √ | ' ' | 责任人 |
| 80 | fk_eafc_attachmentcount | 附件数 | int8 | 64 |  |  | null | 附件数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_volume |  | fid |
