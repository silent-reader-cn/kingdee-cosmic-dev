# 铁路电子客票-eafc_inv_railway

## 铁路电子客票-主表 t_eafc_inv_railway

- **表名称：** 铁路电子客票-主表
- **表名：** t_eafc_inv_railway

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fvoucher_type | 凭证类型 | varchar | 50 |  | √ | ' ' | 凭证类型 |
| 3 | fseller_name | 销售方名称 | varchar | 100 |  | √ | ' ' | 销售方名称 |
| 4 | fbill_create_time | 入库日期 | timestamp | 0 |  |  | null | 入库日期 |
| 5 | ffile_name | 文件名 | varchar | 30 |  | √ | ' ' | 文件名 |
| 6 | ftrain_num | 车次 | varchar | 50 |  | √ | ' ' | 车次 |
| 7 | famount_refunded | 已退金额 | varchar | 50 |  | √ | ' ' | 已退金额 |
| 8 | fsaler_account | 销方账号 | varchar | 150 |  | √ | ' ' | 销方账号 |
| 9 | fdiscount_mark | 优惠标识 | varchar | 50 |  | √ | ' ' | 优惠标识 |
| 10 | fpixel | 像素 | varchar | 20 |  | √ | ' ' | 像素 |
| 11 | freceive_xbrl_name | 接收端xbrl的文件名 | varchar | 1010 |  | √ | ' ' | 接收端xbrl的文件名 |
| 12 | frotation_angle | 旋转角度 | varchar | 4 |  | √ | ' ' | 旋转角度 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fdeparture_time | 出发时间 | varchar | 50 |  | √ | ' ' | 出发时间 |
| 15 | fpassenger_name | 乘客姓名 | varchar | 50 |  | √ | ' ' | 乘客姓名 |
| 16 | fpdf_url | 原件下载地址 | varchar | 512 |  | √ | ' ' | 原件下载地址 |
| 17 | fair_condi_characteristic | 空调特征 | varchar | 50 |  | √ | ' ' | 空调特征 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | fk_eafc_arcorg | 归档组织 | int8 | 64 |  |  | null | [归档组织 eafc_arc_org](../ebase_files/eafc_arc_org.md) |
| 20 | fxbrl_url | 开具端xbrl的下载地址 | varchar | 512 |  | √ | ' ' | 开具端xbrl的下载地址 |
| 21 | ftotal_amount | 票价 | varchar | 50 |  | √ | ' ' | 票价 |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fissue_date | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 24 | fissue_party_code | 开票单位代码 | varchar | 100 |  | √ | ' ' | 开票单位代码 |
| 25 | fdestination_station | 下车站点 | varchar | 50 |  | √ | ' ' | 下车站点 |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fsaler_address_phone | 销方地址电话 | varchar | 150 |  | √ | ' ' | 销方地址电话 |
| 28 | freceive_xbrl_url | 接收端xbrl的下载地址 | varchar | 512 |  | √ | ' ' | 接收端xbrl的下载地址 |
| 29 | fticket_type | 票种 | varchar | 50 |  | √ | ' ' | 票种 |
| 30 | fdetail_amount | 金额 | numeric | 23 | 2 |  | null | 金额 |
| 31 | fsaler_tax_no | 销方税号 | varchar | 20 |  | √ | ' ' | 销方税号 |
| 32 | fxbrl_local_url | 开具端凭证原件地址 | varchar | 512 |  | √ | ' ' | 开具端凭证原件地址 |
| 33 | ferrorlevel | 合规性校验结果等级 | varchar | 50 |  | √ | ' ' | 合规性校验结果等级,枚举: 0 :严格管控 1 :中度警示 2 :轻度提醒 3 :不控制 |
| 34 | fseat | 席位 | varchar | 50 |  | √ | ' ' | 席位 |
| 35 | ffile_type | 文件类型 | varchar | 50 |  | √ | ' ' | 文件类型,枚举: 1 :pdf 2 :图片 4 :ofd 9 :xml |
| 36 | freceive_xbrl_local_url | 接收端凭证原件地址 | varchar | 512 |  | √ | ' ' | 接收端凭证原件地址 |
| 37 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fsnap_shot_url | 发票快照地址 | varchar | 512 |  | √ | ' ' | 发票快照地址 |
| 39 | fdeparture_station_phonic | 出发站拼音 | varchar | 50 |  | √ | ' ' | 出发站拼音 |
| 40 | fdestin_station_phonics | 到达站拼音 | varchar | 50 |  | √ | ' ' | 到达站拼音 |
| 41 | fpurchaser_name | 购买方名称 | varchar | 100 |  | √ | ' ' | 购买方名称 |
| 42 | fk_eafc_book_type | 机构/问题 | int8 | 64 |  |  | null | [机构问题 eafc_book_type](../ebase_files/eafc_book_type.md) |
| 43 | fdownload_url | pdf下载地址 | varchar | 512 |  | √ | ' ' | pdf下载地址 |
| 44 | fseat_level | 席别 | varchar | 50 |  | √ | ' ' | 席别 |
| 45 | fkd_cloud_url | 金蝶云公共下载地址 | varchar | 512 |  | √ | ' ' | 金蝶云公共下载地址 |
| 46 | fserial_no | 发票流水号 | varchar | 36 |  | √ | ' ' | 发票流水号 |
| 47 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fori_ticket_destination | 原票到达站 | varchar | 50 |  | √ | ' ' | 原票到达站 |
| 49 | fid_number | 证件号 | varchar | 50 |  | √ | ' ' | 证件号 |
| 50 | fpurchaser_addr_phone_num | 购买方地址电话 | varchar | 150 |  | √ | ' ' | 购买方地址电话 |
| 51 | fori_ticket_departurest | 原票出发站 | varchar | 50 |  | √ | ' ' | 原票出发站 |
| 52 | ftax_amount | 税额 | numeric | 23 | 2 |  | null | 税额 |
| 53 | fregion | 发票区域 | varchar | 35 |  | √ | ' ' | 发票区域 |
| 54 | fbuyer_account | 购方账号 | varchar | 150 |  | √ | ' ' | 购方账号 |
| 55 | fissue_party | 开票单位 | varchar | 100 |  | √ | ' ' | 开票单位 |
| 56 | fbusiness_type | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: 1 :售 2 :退 |
| 57 | fdeparture_station | 上车站点 | varchar | 50 |  | √ | ' ' | 上车站点 |
| 58 | fremark | 备注 | varchar | 280 |  | √ | ' ' | 备注 |
| 59 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 60 | ftax_rate | 税率 | numeric | 23 | 4 |  | null | 税率 |
| 61 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 62 | fele_ticket_number | 电子客票号 | varchar | 50 |  | √ | ' ' | 电子客票号 |
| 63 | finvoice_no | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 64 | fxbrl_name | 开具端xbrl的文件名 | varchar | 1000 |  | √ | ' ' | 开具端xbrl的文件名 |
| 65 | ftravel_date | 乘车日期 | timestamp | 0 |  |  | null | 乘车日期 |
| 66 | fvalidate_message | 合规性校验结果描述 | varchar | 500 |  | √ | ' ' | 合规性校验结果描述 |
| 67 | fcarriage | 车厢 | varchar | 50 |  | √ | ' ' | 车厢 |
| 68 | fbuyer_tax_no | 购方税号 | varchar | 20 |  | √ | ' ' | 购方税号 |
| 69 | foriginal_ticket_fare | 原票票价 | varchar | 50 |  | √ | ' ' | 原票票价 |
| 70 | fcheck_status | 查验状态 | varchar | 50 |  | √ | ' ' | 查验状态,枚举: 1 :通过 2 :不通过 3 :未查验 |
| 71 | fexpend_status | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: 1 :未报销 2 :已打包 25 :已提交 30 :审批中 60 :审批通过 65 :等待付款 70 :已付款 27 :已废弃 40 :审核不通过 80 :已关闭 |
| 72 | finvoice_type | 发票类型 | int8 | 64 |  |  | null | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 73 | foriginal_invoice_no | 原发票号码 | varchar | 280 |  | √ | ' ' | 原发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_eafc_inv_railway |  | fid |
