# 凭证列表弹框-eafc_voucher_list

## 凭证分录-子表 tk_eafc_voucher_item

- **表名称：** 凭证分录-子表
- **表名：** tk_eafc_voucher_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_account_dimension_tag | 核算维度_详情 | text | 0 |  |  | null | 核算维度_详情 |
| 3 | fk_eafc_debit_loc | 借方本币金额 | numeric | 23 | 10 |  | null | 借方本币金额 |
| 4 | fk_eafc_cost_center | 成本中心 | varchar | 32 |  | √ | ' ' | 成本中心 |
| 5 | fk_eafc_credit_loc | 贷方本币金额 | numeric | 23 | 10 |  | null | 贷方本币金额 |
| 6 | fk_eafc_debit | 借方原币金额 | numeric | 23 | 10 |  | null | 借方原币金额 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fk_eafc_account_dimension | 核算维度 | varchar | 255 |  | √ | ' ' | 核算维度 |
| 9 | fk_eafc_credit | 贷方原币金额 | numeric | 23 | 10 |  | null | 贷方原币金额 |
| 10 | fk_eafc_account_name | 会计科目名称 | varchar | 200 |  | √ | ' ' | 会计科目名称 |
| 11 | fk_fpy_ext_item_field1 | fk_fpy_ext_item_field1 | varchar | 50 |  | √ | ' ' |  |
| 12 | fk_eafc_abstract | 凭证摘要 | varchar | 1000 |  | √ | ' ' | 凭证摘要 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 14 | fk_eafc_account_code | 会计科目代码 | varchar | 80 |  | √ | ' ' | 会计科目代码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_voucher_item |  | fentryid |
| 2 | idx_vou_item_accountcode |  | fk_eafc_account_code |
| 3 | idx__eafc_voucher_item_fk |  | fid |

---

## 单据体-子表 tk_eafc_file

- **表名称：** 单据体-子表
- **表名：** tk_eafc_file

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_eafc_sign | 文件标识 | varchar | 1000 |  | √ | ' ' | 文件标识 |
| 3 | fk_fpy_file_label | 文件标签 | varchar | 500 |  | √ | ' ' | 文件标签 |
| 4 | fk_eafc_filetype | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型 |
| 5 | fk_eafc_doc_filefd | 文档中心文件ID | varchar | 49 |  | √ | ' ' | 文档中心文件ID |
| 6 | fk_eafc_decimalfield | 文件大小 | numeric | 23 | 10 |  | null | 文件大小 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fk_eafc_filehash | 文件hash | varchar | 200 |  | √ | ' ' | 文件hash |
| 9 | fk_fpy_collect_type | 采集方式 | varchar | 50 |  | √ | ' ' | 采集方式,枚举: 1 :在线 2 :手工 |
| 10 | fk_eafc_file_order | 文件顺序 | int4 | 32 |  | √ | 0 | 文件顺序 |
| 11 | fk_eafc_file_createtime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fk_eafc_filename | 文件名称 | varchar | 500 |  | √ | ' ' | 文件名称 |
| 13 | fk_eafc_file_source | 文件来源 | varchar | 50 |  | √ | ' ' | 文件来源,枚举: 1 :星瀚影像 2 :aws影像 |
| 14 | fk_eafc_pdf_fileurl | pdf文件地址 | varchar | 500 |  | √ | ' ' | pdf文件地址 |
| 15 | fk_fpy_rotation_angle | 文件旋转角度 | varchar | 50 |  | √ | ' ' | 文件旋转角度 |
| 16 | fk_eafc_fileurl | 文件地址 | varchar | 500 |  | √ | ' ' | 文件地址 |
| 17 | fk_eafc_scan_type | 影像文件类型 | varchar | 50 |  | √ | ' ' | 影像文件类型,枚举: 0 :封面 1 :发票 2 :附件 |
| 18 | fk_fpy_file_creater | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fk_eafc_pdf_filename | pdf文件名称 | varchar | 100 |  | √ | ' ' | pdf文件名称 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 21 | fk_eafc_file_updatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 22 | fk_eafc_code | 文件编码 | varchar | 50 |  | √ | ' ' | 文件编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__eafc_file_fk |  | fid |
| 2 | idx_eafc_file_url |  | fk_eafc_fileurl |
| 3 | pk__eafc_file |  | fentryid |

---

## 凭证列表弹框-主表 tk_eafc_voucher

- **表名称：** 凭证列表弹框-主表
- **表名：** tk_eafc_voucher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fk_eafc_title | 凭证抬头 | varchar | 64 |  | √ | ' ' | 凭证抬头 |
| 3 | fk_eafc_rate | 汇率(弃用) | varchar | 8 |  | √ | ' ' | 汇率(弃用) |
| 4 | fk_eafc_transfer_time | 移交时间 | timestamp | 0 |  |  | null | 移交时间 |
| 5 | fk_eafc_open_log | 开放标识 | varchar | 50 |  | √ | ' ' | 开放标识,枚举: 1 :开放 2 :控制 3 :延期开放 |
| 6 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fk_eafc_fexpire_time | 保管到期时间 | timestamp | 0 |  |  | null | 保管到期时间 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fk_eafc_filecount | 文件数 | int8 | 64 |  |  | null | 文件数 |
| 10 | fk_eafc_register_time | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 11 | fk_eafc_shelf_location_ob | 上架位置（层-节） | int8 | 64 |  |  | null | [层节设置(基础资料) eafc_floor_config_base](../estore_files/eafc_floor_config_base.md) |
| 12 | fk_eafc_review_date | 复核日期 | timestamp | 0 |  |  | null | 复核日期 |
| 13 | fk_eafc_voucher_type | 凭证字 | varchar | 18 |  | √ | ' ' | 凭证字 |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fk_eafc_accounter | 过账人 | varchar | 32 |  | √ | ' ' | 过账人 |
| 16 | fk_eafc_period | 属期 | timestamp | 0 |  |  | null | 属期 |
| 17 | fk_eafc_register | 归档人 | varchar | 50 |  | √ | ' ' | 归档人 |
| 18 | fk_eafc_box_status | 装盒状态 | varchar | 50 |  | √ | ' ' | 装盒状态,枚举: 1 :未装盒 2 :虚拟装盒 3 :已装盒 |
| 19 | fk_eafc_relation | 关联id | int8 | 64 |  |  | null | 关联id |
| 20 | fk_eafc_attach_num | 附件张数 | int8 | 64 |  |  | null | 附件张数 |
| 21 | fk_eafc_batchnum | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 22 | fk_eafc_volume_relationid | 卷id | int8 | 64 |  |  | null | 卷id |
| 23 | fk_eafc_subjectword | 主题词 | varchar | 200 |  | √ | ' ' | 主题词 |
| 24 | fk_eafc_book_relationid | 册id | int8 | 64 |  |  | null | 册id |
| 25 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 27 | fk_fpy_modifytime | 修订时间 | timestamp | 0 |  |  | null | 修订时间 |
| 28 | fk_eafc_volume_time | 入卷时间 | timestamp | 0 |  |  | null | 入卷时间 |
| 29 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fk_eafc_entity_status | 存储形式 | varchar | 50 |  | √ | ' ' | 存储形式,枚举: 1 :电子 2 :电子+纸质 |
| 31 | fk_eafc_uniqueid | 唯一编号 | varchar | 100 |  | √ | ' ' | 唯一编号 |
| 32 | fk_eafc_making_date | 制单日期(弃用) | timestamp | 0 |  |  | null | 制单日期(弃用) |
| 33 | fk_eafc_data_stauts | 文件状态 | varchar | 50 |  | √ | ' ' | 文件状态,枚举: 1 :待匹配 2 :待组卷 3 :已组卷 4 :归档中 5 :已归档 9 :被移除 11 :异常 12 :检测中 |
| 34 | fk_eafc_org_name | 核算单位名字 | varchar | 50 |  | √ | ' ' | 核算单位名字 |
| 35 | fk_eafc_account_date | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 36 | fk_eafc_file_cod | 文件编码 | varchar | 500 |  | √ | ' ' | 文件编码 |
| 37 | fk_eafc_business | 三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 38 | fk_eafc_creater | 制单人 | varchar | 32 |  | √ | ' ' | 制单人 |
| 39 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fk_fpy_modifier | 修订人 | varchar | 50 |  | √ | ' ' | 修订人 |
| 41 | fk_eafc_check_status | 占用状态 | varchar | 50 |  | √ | ' ' | 占用状态,枚举: 1 :未占用 2 :已占用 3 :占用超时 4 :已占用（不展示数据） 5 :占用超时（不展示数据） |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fk_eafc_auditing | 审核人 | varchar | 32 |  | √ | ' ' | 审核人 |
| 44 | fk_eafc_transfer_status | 是否移交 | varchar | 50 |  | √ | ' ' | 是否移交,枚举: 1 :未移交 2 :已移交 |
| 45 | fk_eafc_stock_status | 是否出库 | varchar | 50 |  | √ | ' ' | 是否出库,枚举: 1 :未出库 2 :已出库 |
| 46 | fk_eafc_volcheck_status | 组卷检测状态 | varchar | 50 |  | √ | ' ' | 组卷检测状态,枚举: 1 :通过 2 :不通过 |
| 47 | fk_eafc_remove_reason | 移除原因 | varchar | 20 |  | √ | ' ' | 移除原因 |
| 48 | fk_eafc_scanbillno | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 49 | fk_eafc_create_date | 制单日期 | timestamp | 0 |  |  | null | 制单日期 |
| 50 | fk_eafc_duty_user | 责任者 | varchar | 50 |  | √ | ' ' | 责任者 |
| 51 | fk_eafc_arc_year | 年度 | timestamp | 0 |  |  | null | 年度 |
| 52 | fk_eafc_update_time | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 53 | fk_eafc_volume_serial_no | 卷内序号 | int8 | 64 |  |  | null | 卷内序号 |
| 54 | fk_eafc_total_credit_loc | 贷方本币合计 | numeric | 23 | 10 |  | null | 贷方本币合计 |
| 55 | fk_eafc_general_org | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 56 | fk_eafc_remove_symbol | 移除标记 | bpchar | 1 |  | √ | '0' | 移除标记 |
| 57 | fk_fpy_box_serial | 盒内序号 | int8 | 64 |  | √ | 0 | 盒内序号 |
| 58 | fk_eafc_box_no | 盒号 | varchar | 50 |  | √ | ' ' | 盒号 |
| 59 | fk_eafc_attachment_count | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 60 | fk_fpy_createtime | 编制时间 | timestamp | 0 |  |  | null | 编制时间 |
| 61 | fk_eafc_volcheck_result | 组卷检测结果 | varchar | 200 |  | √ | ' ' | 组卷检测结果 |
| 62 | fk_eafc_storage_period | 保管期限 | varchar | 50 |  | √ | ' ' | 保管期限,枚举: 1 :10年 2 :30年 3 :永久 |
| 63 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 64 | fk_eafc_currencyfield | 币别 | int8 | 64 |  |  | null | [币种 bd_currency](../base_files/bd_currency.md) |
| 65 | fk_eafc_volume_oldrelid | 调整前_卷id | int8 | 64 |  | √ | 0 | 调整前_卷id |
| 66 | fk_eafc_pagecount | 页数 | int8 | 64 |  |  | null | 页数 |
| 67 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 68 | fk_fpy_box_user | 装盒人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 69 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 70 | fk_eafc_manual_items | 人工复核项 | varchar | 500 |  | √ | ' ' | 人工复核项 |
| 71 | fk_eafc_review | 复核人 | varchar | 32 |  | √ | ' ' | 复核人 |
| 72 | fk_fpy_storage_status | 是否出库 | varchar | 50 |  | √ | '1' | 是否出库,枚举: 1 :未出库 2 :已出库 |
| 73 | fk_eafc_inspect_detail | 四性检测详情id | int8 | 64 |  |  | null | 四性检测详情id |
| 74 | fk_eafc_box_serialno | 盒内顺序 | int4 | 32 |  | √ | 0 | 盒内顺序 |
| 75 | fk_eafc_encrypt_type | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 76 | fk_eafc_inspect_status | 检测状态 | varchar | 30 |  | √ | ' ' | 检测状态,枚举: 0 :检测不通过 1 :检测通过 |
| 77 | fk_eafc_check_result | 状态描述 | varchar | 200 |  | √ | ' ' | 状态描述 |
| 78 | fk_eafc_voucher_num | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 79 | fk_eafc_desc | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 80 | fk_eafc_total_debit_loc | 借方本币合计 | numeric | 23 | 10 |  | null | 借方本币合计 |
| 81 | fk_eafc_period_new | 会计期间 | varchar | 50 |  | √ | ' ' | 会计期间 |
| 82 | fk_eafc_archive_user | 接收人 | varchar | 50 |  | √ | ' ' | 接收人 |
| 83 | fk_eafc_audit_date | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 84 | fk_eafc_file_sign | 文件题名 | varchar | 500 |  | √ | ' ' | 文件题名 |
| 85 | fk_fpy_box_date | 装盒日期 | timestamp | 0 |  |  | null | 装盒日期 |
| 86 | fk_eafc_cashier | 出纳 | varchar | 28 |  | √ | ' ' | 出纳 |
| 87 | fk_eafc_total_debit_tra | 借方原币合计 | numeric | 23 | 10 |  | null | 借方原币合计 |
| 88 | fk_eafc_file_status | 实物状态 | varchar | 50 |  | √ | ' ' | 实物状态,枚举: 1 :已装盒 2 :虚拟装盒 3 :未装盒 |
| 89 | fk_eafc_basedatafield | 二级门类 | int8 | 64 |  |  | null | [档案门类（二级） eafc_category](../ebase_files/eafc_category.md) |
| 90 | fk_eafc_volume | 案卷号 | varchar | 50 |  | √ | ' ' | 案卷号 |
| 91 | fk_eafc_archivenum | 档案号 | varchar | 500 |  | √ | ' ' | 档案号 |
| 92 | fk_eafc_archive_time | 接收时间 | timestamp | 0 |  |  | null | 接收时间 |
| 93 | fk_eafc_approval | 会计主管 | varchar | 32 |  | √ | ' ' | 会计主管 |
| 94 | fk_eafc_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 95 | fk_eafc_file_way | 文件组合类型 | varchar | 50 |  | √ | ' ' | 文件组合类型,枚举: 1 :散文件 2 :组合文件 3 :复合文件 |
| 96 | fk_eafc_posting | 记账人 | varchar | 32 |  | √ | ' ' | 记账人 |
| 97 | fk_eafc_arc_month | 月份 | varchar | 50 |  | √ | ' ' | 月份,枚举: 1 :1月 2 :2月 3 :3月 4 :4月 5 :5月 6 :6月 7 :7月 8 :8月 9 :9月 10 :10月 11 :11月 12 :12月 |
| 98 | fk_eafc_sign_status | 签收状态 | varchar | 50 |  | √ | ' ' | 签收状态,枚举: 0 :待签收 1 :已签收 2 :无需签收 |
| 99 | fk_fpy_creator | 编制人 | varchar | 50 |  | √ | ' ' | 编制人 |
| 100 | fk_eafc_operator | 经办人 | varchar | 32 |  | √ | ' ' | 经办人 |
| 101 | fk_eafc_box | 盒子id | int8 | 64 |  | √ | 0 | 盒子id |
| 102 | fk_eafc_total_credit_tra | 贷方原币合计 | numeric | 23 | 10 |  | null | 贷方原币合计 |
| 103 | fk_eafc_org_no | 核算单位编码 | varchar | 50 |  | √ | ' ' | 核算单位编码 |
| 104 | fk_eafc_posting_date | 过账日期 | timestamp | 0 |  |  | null | 过账日期 |
| 105 | fk_fpy_rate | 汇率 | numeric | 23 | 4 |  | null | 汇率 |
| 106 | fk_eafc_volume_type | 组卷方式 | varchar | 50 |  | √ | ' ' | 组卷方式,枚举: 1 :自动 2 :手动 3 :扫码组卷 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__eafc_voucher |  | fid |
| 2 | idx_eafc_voucher_vrid |  | fk_eafc_volume_relationid |
| 3 | idx_voucher_type |  | fk_eafc_voucher_type |
| 4 | idx_eafc_voucher_uidstatus |  | fk_eafc_uniqueid,fk_eafc_data_stauts |
| 5 | idx_eafc_voucher_num_type2 |  | fk_eafc_arcorg,fk_eafc_book_type,fk_eafc_period_new,fk_eafc_voucher_type,fk_eafc_voucher_num |
| 6 | idx_voucher_arcorg |  | fk_eafc_arcorg |
| 7 | idx_eafc_voucher_num_type |  | forgid,fk_eafc_book_type,fk_eafc_period,fk_eafc_voucher_type,fk_eafc_voucher_num |
| 8 | idx_eafc_voucher_uid |  | fk_eafc_uniqueid |
