# 航空运输电子客票-eafc_inv_aviation

## 单据体-子表 t_eafc_inv_aviation_item

- **表名称：** 单据体-子表
- **表名：** t_eafc_inv_aviation_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdestination_i | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 3 | fair_time_i | 乘机时间 | varchar | 50 |  | √ | ' ' | 乘机时间 |
| 4 | fcarrier_date_i | 承运日期 | varchar | 50 |  | √ | ' ' | 承运日期 |
| 5 | ffree_baggage_allowance_i | 免费行李额 | varchar | 50 |  | √ | ' ' | 免费行李额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fplace_of_departure_i | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 8 | fflight_num_i | 航班号 | varchar | 50 |  | √ | ' ' | 航班号 |
| 9 | ffare_basis_i | 客票级别 | varchar | 50 |  | √ | ' ' | 客票级别 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcarrier_i | 承运人 | varchar | 50 |  | √ | ' ' | 承运人 |
| 12 | fseat_grade_i | 座位等级 | varchar | 50 |  | √ | ' ' | 座位等级 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_aviation_item |  | fentryid |

---

## 航空运输电子客票-主表 t_eafc_inv_aviation

- **表名称：** 航空运输电子客票-主表
- **表名：** t_eafc_inv_aviation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbill_create_time | 入库日期 | timestamp | 0 |  |  | null | 入库日期 |
| 3 | fseller_name | 销方名称 | varchar | 100 |  | √ | ' ' | 销方名称 |
| 4 | finsurance_premium | 保险费 | numeric | 23 | 2 |  | null | 保险费 |
| 5 | finternational_flag | 国际航班标识 | varchar | 50 |  | √ | ' ' | 国际航班标识,枚举: 0 :无 1 :国内 2 :国际 |
| 6 | ffile_name | 文件名 | varchar | 100 |  | √ | ' ' | 文件名 |
| 7 | fpixel | 像素 | varchar | 20 |  | √ | ' ' | 像素 |
| 8 | freceive_xbrl_name | 接收端xbrl的文件名 | varchar | 1000 |  | √ | ' ' | 接收端xbrl的文件名 |
| 9 | ffilling_unit | 填开单位 | varchar | 100 |  | √ | ' ' | 填开单位 |
| 10 | frotation_angle | 旋转角度 | varchar | 4 |  | √ | ' ' | 旋转角度 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcarrie_date | 乘机日期 | timestamp | 0 |  |  | null | 乘机日期 |
| 13 | fcarrier | 承运人 | varchar | 32 |  | √ | ' ' | 承运人 |
| 14 | felectronic_ticket_num | 电子客票号码 | varchar | 32 |  | √ | ' ' | 电子客票号码 |
| 15 | fcheck_code | 验证码 | varchar | 32 |  | √ | ' ' | 验证码 |
| 16 | fpdf_url | 原件下载地址 | varchar | 512 |  | √ | ' ' | 原件下载地址 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 19 | fxbrl_url | 开具端xbrl的下载地址 | varchar | 512 |  | √ | ' ' | 开具端xbrl的下载地址 |
| 20 | ftotal_amount | 合计金额 | numeric | 23 | 2 |  | null | 合计金额 |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | ffuel_surcharge | 燃油附加费 | numeric | 23 | 2 |  | null | 燃油附加费 |
| 23 | fissue_date | 填开日期 | timestamp | 0 |  |  | null | 填开日期 |
| 24 | fnumber_gporder | GP单号 | varchar | 29 |  | √ | ' ' | GP单号 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fprompt_info | 提示信息 | varchar | 59 |  | √ | ' ' | 提示信息 |
| 27 | fcustomer_name | 旅客姓名 | varchar | 20 |  | √ | ' ' | 旅客姓名 |
| 28 | freceive_xbrl_url | 接收端xbrl的下载地址 | varchar | 512 |  | √ | ' ' | 接收端xbrl的下载地址 |
| 29 | fcustomer_identity_num | 身份证号 | varchar | 25 |  | √ | ' ' | 身份证号 |
| 30 | fxbrl_local_url | 开具端凭证原件地址 | varchar | 512 |  | √ | ' ' | 开具端凭证原件地址 |
| 31 | ffile_type | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: 1 :pdf 2 :图片 4 :ofd 9 :xml |
| 32 | freceive_xbrl_local_url | 接收端凭证原件地址 | varchar | 512 |  | √ | ' ' | 接收端凭证原件地址 |
| 33 | fseat_grade | 座位等级 | varchar | 10 |  | √ | ' ' | 座位等级 |
| 34 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fbuyer_name | fbuyer_name | varchar | 100 |  | √ | ' ' |  |
| 36 | finvoice_amount | 票价 | numeric | 23 | 2 |  | null | 票价 |
| 37 | fpurchaser_name | 购方名称 | varchar | 100 |  | √ | ' ' | 购方名称 |
| 38 | fplace_departure | 出发地 | varchar | 32 |  | √ | ' ' | 出发地 |
| 39 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 40 | fdownload_url | pdf下载地址 | varchar | 512 |  | √ | ' ' | pdf下载地址 |
| 41 | fsales_unit_code | 销售网点代号 | varchar | 32 |  | √ | ' ' | 销售网点代号 |
| 42 | freason_rushred | 红冲原因 | varchar | 32 |  | √ | ' ' | 红冲原因 |
| 43 | finvoice_status | 开具状态 | varchar | 50 |  | √ | ' ' | 开具状态,枚举: 0 :正常 红冲 :红冲 |
| 44 | fkd_cloud_url | 金蝶云公共下载地址 | varchar | 512 |  | √ | ' ' | 金蝶云公共下载地址 |
| 45 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 46 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fflight_num | 航班号 | varchar | 32 |  | √ | ' ' | 航班号 |
| 48 | fregion | 发票区域 | varchar | 35 |  | √ | ' ' | 发票区域 |
| 49 | fother_total_tax_amount | 其他税费 | numeric | 23 | 2 |  | null | 其他税费 |
| 50 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 51 | ftax_rate | 增值税税率 | numeric | 23 | 4 |  | null | 增值税税率 |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | finvoice_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 54 | ftotal_tax_amount | 增值税税额 | numeric | 23 | 2 |  | null | 增值税税额 |
| 55 | fdestination | 目的地 | varchar | 32 |  | √ | ' ' | 目的地 |
| 56 | fsnapshot_url | 发票快照地址 | varchar | 512 |  | √ | ' ' | 发票快照地址 |
| 57 | finvoice_no | 发票号码 | varchar | 32 |  | √ | ' ' | 发票号码 |
| 58 | fxbrl_name | 开具端xbrl的文件名 | varchar | 1000 |  | √ | ' ' | 开具端xbrl的文件名 |
| 59 | fvalidate_message | 合规性校验结果描述 | varchar | 500 |  | √ | ' ' | 合规性校验结果描述 |
| 60 | fqrcode | 二维码 | varchar | 100 |  | √ | ' ' | 二维码 |
| 61 | ferror_level | 合规性校验结果等级 | varchar | 50 |  | √ | ' ' | 合规性校验结果等级,枚举: 0 :严格管控 1 :中度警示 2 :轻度提醒 3 :不控制 |
| 62 | fairport_construction_fee | 民航发展基金 | numeric | 23 | 2 |  | null | 民航发展基金 |
| 63 | fsaler_name | fsaler_name | varchar | 100 |  | √ | ' ' |  |
| 64 | fcheck_status | 查验状态 | varchar | 50 |  | √ | ' ' | 查验状态,枚举: 1 :通过 2 :不通过 3 :未查验 |
| 65 | fexpend_status | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 1 :未报销 2 :已打包 25 :已提交 30 :审批中 60 :审批通过 65 :等待付款 70 :已付款 27 :已废弃 40 :审核不通过 80 :已关闭 |
| 66 | fair_time | 乘机时间 | varchar | 10 |  | √ | ' ' | 乘机时间 |
| 67 | finvoice_type | 发票类型 | int8 | 64 |  |  | null | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 68 | fendorsement | 签注 | varchar | 32 |  | √ | ' ' | 签注 |
| 69 | fsocial_credit_code_pur | 购买方统一社会信用代码 | varchar | 20 |  | √ | ' ' | 购买方统一社会信用代码 |
| 70 | foriginal_invoice_no | 原票号码 | varchar | 32 |  | √ | ' ' | 原票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_aviation |  | fid |
