# 发票主表-eafc_invoice

## 发票主表-主表 t_eafc_invoice

- **表名称：** 发票主表-主表
- **表名：** t_eafc_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fpreset_deduction_purpose | 单据抵扣用途 | varchar | 50 |  | √ | ' ' | 单据抵扣用途,枚举: 1 :抵扣 2 :不抵扣 3 :退税 |
| 3 | ftenant_no | 租户 | varchar | 30 |  | √ | ' ' | 租户 |
| 4 | ffile_name | 发票文件名 | varchar | 200 |  | √ | ' ' | 发票文件名 |
| 5 | fk_eafc_open_log | 开放标识 | varchar | 50 |  | √ | ' ' | 开放标识,枚举: 1 :开放 2 :控制 3 :延期开放 |
| 6 | fk_eafc_isrel_voucher | 是否已关联凭证 | bpchar | 1 |  | √ | '0' | 是否已关联凭证 |
| 7 | fk_eafc_fexpire_time | 保管到期时间 | timestamp | 0 |  |  | null | 保管到期时间 |
| 8 | fauthenticate_time | 认证时间 | timestamp | 0 |  |  | null | 认证时间 |
| 9 | fk_eafc_region | 发票区域 | varchar | 38 |  | √ | ' ' | 发票区域 |
| 10 | fmain_goods_name | 主要商品名片 | varchar | 120 |  | √ | ' ' | 主要商品名片 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fk_eafc_open_xbrl | 开具端的xbrl文件下载地址 | varchar | 500 |  | √ | ' ' | 开具端的xbrl文件下载地址 |
| 13 | fk_eafc_file_source | 文件来源 | varchar | 50 |  | √ | ' ' | 文件来源,枚举: 1 :星瀚影像 2 :aws影像 |
| 14 | fk_eafc_register_time | 登记时间 | timestamp | 0 |  |  | null | 登记时间 |
| 15 | fk_pdf_download_url | pdf下载地址 | varchar | 500 |  | √ | ' ' | pdf下载地址 |
| 16 | fk_eafc_shelf_location_ob | 上架位置（层-节） | int8 | 64 |  |  | null | [层节设置(基础资料) eafc_floor_config_base](../estore_files/eafc_floor_config_base.md) |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | ftotal_amount | 价税合计 | numeric | 23 | 2 |  | null | 价税合计 |
| 19 | fdeduction_purpose | 抵扣用途 | varchar | 50 |  | √ | ' ' | 抵扣用途,枚举: 1 :抵扣 2 :不抵扣 3 :退税 |
| 20 | fk_eafc_register | 登记人 | varchar | 50 |  | √ | ' ' | 登记人 |
| 21 | finvoice_code | 发票代码 | varchar | 32 |  | √ | ' ' | 发票代码 |
| 22 | fcheck_times | 查验次数 | int8 | 64 |  |  | null | 查验次数 |
| 23 | fk_eafc_box_status | 装盒状态 | varchar | 50 |  | √ | ' ' | 装盒状态,枚举: 1 :未装盒 2 :虚拟装盒 3 :已装盒 |
| 24 | fk_eafc_batchnum | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 25 | fk_eafc_volume_relationid | 案卷id | int8 | 64 |  | √ | 0 | 案卷id |
| 26 | fk_eafc_subjectword | 主题词 | varchar | 200 |  | √ | ' ' | 主题词 |
| 27 | fsaler_tax_no | 销方税号 | varchar | 20 |  | √ | ' ' | 销方税号 |
| 28 | fexpense_status | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 1 :未用 30 :在用 60 :已用 65 :已入账 |
| 29 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 30 | ftransport_deduction | 旅客运输抵扣 | varchar | 50 |  | √ | ' ' | 旅客运输抵扣,枚举: 0 :未抵扣 1 :已抵扣 2 :预抵扣 |
| 31 | freceiver | 签收人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 33 | fmanage_status | 管理状态 | varchar | 50 |  | √ | ' ' | 管理状态,枚举: 0 :正常 1 :非正常 |
| 34 | finvoice_status | 发票状态 | varchar | 50 |  | √ | ' ' | 发票状态,枚举: 0 :正常 1 :失控 2 :作废 3 :红冲 4 :异常 7 :部分红冲 |
| 35 | fexpense_no | 报销单号 | varchar | 50 |  | √ | ' ' | 报销单号 |
| 36 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fk_eafc_entity_status | 存储形式 | varchar | 50 |  | √ | ' ' | 存储形式,枚举: 1 :电子 2 :电子+纸质 |
| 39 | fk_eafc_data_stauts | 文件状态 | varchar | 50 |  | √ | ' ' | 文件状态,枚举: 1 :待匹配 2 :待组卷 3 :已组卷 4 :归档中 5 :已归档 9 :被移除 11 :异常 12 :检测中 |
| 40 | fk_eafc_file_cod | 文件编码 | varchar | 500 |  | √ | ' ' | 文件编码 |
| 41 | fk_eafc_business | 三级门类 | int8 | 64 |  |  | null | [资料形式（三级类别） eafc_business_type](../ebase_files/eafc_business_type.md) |
| 42 | fk_eafc_receive_xbrl | 接收端的xbrl文件下载地址 | varchar | 500 |  | √ | ' ' | 接收端的xbrl文件下载地址 |
| 43 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fk_eafc_check_status | 检测状态 | varchar | 50 |  | √ | ' ' | 检测状态,枚举: 1 :通过 2 :不通过 |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | ftotal_tax_amount | 发票税额 | numeric | 23 | 2 |  | null | 发票税额 |
| 48 | fk_eafc_source_in_out | 销方/购方 | varchar | 50 |  | √ | ' ' | 销方/购方,枚举: 1 :购方 2 :销方 |
| 49 | fsnapshot_url | 快照地址 | varchar | 500 |  | √ | ' ' | 快照地址 |
| 50 | fk_eafc_tax_ofd_url | 税局数电票OFD地址 | varchar | 500 |  | √ | ' ' | 税局数电票OFD地址 |
| 51 | fk_eafc_rotation_angle | 旋转角度 | int4 | 32 |  | √ | 0 | 旋转角度 |
| 52 | ftax_org | 税务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | fk_eafc_remove_reason | 移除原因 | varchar | 20 |  | √ | ' ' | 移除原因 |
| 54 | fpy_box_serial | fpy_box_serial | int8 | 64 |  | √ | 0 |  |
| 55 | finvoice_type | 发票类型 | int8 | 64 |  |  | null | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 56 | fk_eafc_duty_user | 责任者 | varchar | 50 |  | √ | ' ' | 责任者 |
| 57 | fcancel_select_type | 撤销勾选类型 | varchar | 50 |  | √ | ' ' | 撤销勾选类型,枚举: 1 :手工撤销 2 :自动撤销 |
| 58 | finternational_flag | 国内国际标志 | varchar | 50 |  | √ | ' ' | 国内国际标志,枚举: 1 :国内 2 :国际 |
| 59 | fk_fpy_file_label | 文件标签 | varchar | 500 |  | √ | ' ' | 文件标签 |
| 60 | fcheck_result | 查验结果 | varchar | 50 |  | √ | ' ' | 查验结果 |
| 61 | fk_eafc_volume_serial_no | 卷内序号 | int4 | 32 |  | √ | 0 | 卷内序号 |
| 62 | ftax_period | 抵扣税期 | timestamp | 0 |  |  | null | 抵扣税期 |
| 63 | fdeduction_flag | 抵扣标识 | varchar | 50 |  | √ | ' ' | 抵扣标识,枚举: 1 :可抵扣 0 :不可抵扣 |
| 64 | feffective_tax_amount | 可抵扣税额 | numeric | 23 | 2 |  | null | 可抵扣税额 |
| 65 | fk_eafc_general_org | 全宗 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 66 | fk_eafc_remove_symbol | 移除标记 | bpchar | 1 |  | √ | '0' | 移除标记 |
| 67 | fk_fpy_box_serial | 盒内序号 | int8 | 64 |  | √ | 0 | 盒内序号 |
| 68 | fcompany_seal | 是否有公司印章 | varchar | 50 |  | √ | ' ' | 是否有公司印章,枚举: 0 :没有 1 :有 |
| 69 | fselect_time | 勾选时间 | timestamp | 0 |  |  | null | 勾选时间 |
| 70 | fk_eafc_box_no | 盒号 | varchar | 50 |  | √ | ' ' | 盒号 |
| 71 | fnot_deductible_type | 不抵扣原因 | varchar | 50 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或者个人消费 4 :遭受非正常损失 5 :其他 |
| 72 | fresource | 发票来源 | varchar | 50 |  | √ | ' ' | 发票来源 |
| 73 | fk_eafc_delete | 发票的可用状态 | varchar | 50 |  | √ | ' ' | 发票的可用状态,枚举: 0 :不可用 1 :可用 2 :待提交 |
| 74 | fk_eafc_storage_period | 保管期限(下拉) | varchar | 50 |  | √ | ' ' | 保管期限(下拉),枚举: 1 :十年 2 :三十年 3 :永久 |
| 75 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 76 | forg_id | 核算组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 77 | tk_eafc_encrypt_type | 密级 | varchar | 50 |  | √ | ' ' | 密级,枚举: 1 :公开 2 :秘密 3 :机密 4 :绝密 |
| 78 | fk_eafc_pagecount | 页数 | int4 | 32 |  | √ | 0 | 页数 |
| 79 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 80 | fauthenticate_flag | 认证状态 | varchar | 50 |  | √ | ' ' | 认证状态,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 4 :预勾选 5 :勾选中 |
| 81 | fk_pdf_file_name | 发票pdf文件名 | varchar | 200 |  | √ | ' ' | 发票pdf文件名 |
| 82 | fk_fpy_box_user | 装盒人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 83 | fk_eafc_tax_xml_url | 税局数电票XML地址 | varchar | 500 |  | √ | ' ' | 税局数电票XML地址 |
| 84 | fk_eafc_pixel | 像素 | varchar | 30 |  | √ | ' ' | 像素 |
| 85 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 86 | fk_eafc_manual_items | 人工复核项 | varchar | 500 |  | √ | ' ' | 人工复核项 |
| 87 | fk_eafc_tax_pdf_url | 税局数电票PDF地址 | varchar | 500 |  | √ | ' ' | 税局数电票PDF地址 |
| 88 | fcheck_time | 查验时间 | timestamp | 0 |  |  | null | 查验时间 |
| 89 | fk_eafc_inspect_detail | 四性检测详情id | int8 | 64 |  | √ | 0 | 四性检测详情id |
| 90 | fk_eafc_box_serialno | 盒内顺序 | int4 | 32 |  | √ | 0 | 盒内顺序 |
| 91 | fk_eafc_inspect_status | 检测状态 | varchar | 30 |  | √ | ' ' | 检测状态,枚举: 0 :检测不通过 1 :检测通过 |
| 92 | fk_eafc_check_result | 检测结果 | varchar | 200 |  | √ | ' ' | 检测结果 |
| 93 | fsource_area | 发票源地区 | varchar | 150 |  | √ | ' ' | 发票源地区 |
| 94 | foriginal_time | 签收时间 | timestamp | 0 |  |  | null | 签收时间 |
| 95 | fproject | 项目 | int8 | 64 |  |  | null | [项目 bd_project](../basedata_files/bd_project.md) |
| 96 | fk_eafc_import_format | 导入格式 | varchar | 50 |  | √ | ' ' | 导入格式,枚举: 1 :单页PDF文件导入 2 :多页PDF文件导入 |
| 97 | fbuyer_name | 购方名称 | varchar | 120 |  | √ | ' ' | 购方名称 |
| 98 | fk_eafc_org | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 99 | finvoice_amount | 发票金额 | numeric | 23 | 2 |  | null | 发票金额 |
| 100 | fk_eafc_archive_user | 归档人 | varchar | 50 |  | √ | ' ' | 归档人 |
| 101 | fk_eafc_doc_filefd | 文档中心文件ID | varchar | 50 |  | √ | ' ' | 文档中心文件ID |
| 102 | fvouch_no | 凭证号 | varchar | 50 |  | √ | ' ' | 凭证号 |
| 103 | fk_eafc_file_sign | 文件标识 | varchar | 500 |  | √ | ' ' | 文件标识 |
| 104 | fdownload_url | 下载地址 | varchar | 500 |  | √ | ' ' | 下载地址 |
| 105 | fk_fpy_box_date | 装盒日期 | timestamp | 0 |  |  | null | 装盒日期 |
| 106 | fpy_box_date | fpy_box_date | timestamp | 0 |  |  | null |  |
| 107 | fk_eafc_basedatafield | 二级门类 | int8 | 64 |  |  | null | [档案门类（二级） eafc_category](../ebase_files/eafc_category.md) |
| 108 | fk_eafc_archivenum | 档案号 | varchar | 100 |  | √ | ' ' | 档案号 |
| 109 | fk_eafc_volume | 案卷号 | varchar | 50 |  | √ | ' ' | 案卷号 |
| 110 | fk_eafc_archive_time | 归档时间 | timestamp | 0 |  |  | null | 归档时间 |
| 111 | fk_eafc_source_system | 来源系统 | varchar | 50 |  | √ | ' ' | 来源系统 |
| 112 | finvoice_info | 发票信息 | varchar | 50 |  | √ | ' ' | 发票信息,枚举: ty_1 :电子普通发票 ty_2 :电子专用发票 ty_3 :增值税普通发票 ty_4 :增值税专用发票 ty_5 :普通纸质卷票 ty_7 :通用机打发票 ty_8 :出租车票 ty_9 :火车票 ty_10 :飞机行程单 ty_11 :其它票 ty_12 :机动车销售发票 ty_13 :二手车销售发票 ty_14 :定额发票 ty_15 :通行费电子发票 ty_16 :公路汽车票 ty_17 :过路桥费发票 ty_19 :完税证明 ty_20 :轮船票 ty_23 :通用机打电子发票 st_3 :红冲 st_2 :作废 ex_1 :未用 ex_30 :在用 ex_60 :已用 ex_65 :已入账 ch_1 :已验 ch_2 :未验 ch_3 :未验 ch_4 :不查验 or_0 :未签收 or_1 :已签收 au_0 :未勾选 au_1 :已勾选 au_2 :已认证 au_3 :已认证 au_4 :预勾选 au_5 :勾选中 td_1 :旅客运输抵扣 mo_1 :已改 ty_21 :海关缴款书 ty_24 :火车票退票凭证 ty_25 :财政电子票据 ty_26 :全电普票 ty_27 :全电专票 st_7 :部分红冲 st_8 :全额红冲 st_4 :异常 |
| 113 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 114 | fk_eafc_sign_status | 签收状态 | varchar | 50 |  | √ | ' ' | 签收状态,枚举: 0 :待签收 1 :已签收 2 :无需签收 |
| 115 | fk_eafc_box | 盒子id | int8 | 64 |  | √ | 0 | 盒子id |
| 116 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 117 | fbuyer_tax_no | 购方税号 | varchar | 20 |  | √ | ' ' | 购方税号 |
| 118 | fsaler_name | 销方名称 | varchar | 120 |  | √ | ' ' | 销方名称 |
| 119 | fcheck_status | 查验状态 | varchar | 50 |  | √ | ' ' | 查验状态,枚举: 1 :通过 2 :不通过 3 :未查验 4 :不查验 |
| 120 | fk_fpy_rel_archiveent | 跟随归档实体 | varchar | 50 |  | √ | ' ' | 跟随归档实体 |
| 121 | faudit_result | 审计状态 | varchar | 50 |  | √ | ' ' | 审计状态,枚举: 0 :正常 1 :未处理 2 :已处理 |
| 122 | foriginal_state | 原件签收状态 | varchar | 50 |  | √ | ' ' | 原件签收状态,枚举: 0 :未签收 1 :已签收 |
| 123 | fdest_area | 目的地地区 | varchar | 150 |  | √ | ' ' | 目的地地区 |
| 124 | fk_eafc_volume_type | 组卷方式 | varchar | 50 |  | √ | ' ' | 组卷方式,枚举: 1 :自动 2 :手动 3 :扫码组卷 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_invoice |  | fid |
