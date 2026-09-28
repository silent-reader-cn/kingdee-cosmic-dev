# 国内/国际差旅报销单-er_tripreimburse_cardgrid

## 交通工具标准ID-多选基础资料表 t_er_vehstands

- **表名称：** 交通工具标准ID-多选基础资料表
- **表名：** t_er_vehstands

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [全球交通工具标准 er_trip_vehicle_standard](../em_files/er_trip_vehicle_standard.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_vehstands_fdetailid |  | fdetailid |
| 2 | pk_t_er_vehstands |  | fpkid |

---

## 标准座位等级-多选基础资料表 t_er_ntripstdseatgrade

- **表名称：** 标准座位等级-多选基础资料表
- **表名：** t_er_ntripstdseatgrade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [座位等级设置 er_seatgradestd](../em_files/er_seatgradestd.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ntripstdseatgra_detail |  | fdetailid |
| 2 | pk_t_er_ntripstdseatgrade |  | fpkid |

---

## 附件信息-子表 t_er_invoiceattachinfo

- **表名称：** 附件信息-子表
- **表名：** t_er_invoiceattachinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 3 | fattlargetxt | 长文本 | varchar | 255 |  |  | null | 长文本 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachserialno | 发票序列号 | varchar | 255 |  | √ | ' ' | 发票序列号 |
| 6 | fattsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: 1 :发票云 2 :大模型 |
| 7 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 8 | frotationangle | 旋转角度 | varchar | 30 |  |  | null | 旋转角度 |
| 9 | fattaffairdiscription | 事务描述 | varchar | 1024 |  |  | null | 事务描述 |
| 10 | fattheadcount | 人数 | int8 | 64 |  | √ | 0 | 人数 |
| 11 | fattcity | 城市 | varchar | 255 |  |  | null | 城市 |
| 12 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 13 | fattenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 14 | fattinvoiceentyid | 发票分录id | int8 | 64 |  | √ | 0 | 发票分录id |
| 15 | fattfrom | 出发地 | varchar | 255 |  |  | null | 出发地 |
| 16 | fattlargetxt_tag | 长文本_详情 | text | 0 |  |  | null | 长文本_详情 |
| 17 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 18 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 19 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 20 | fattto | 目的地 | varchar | 255 |  |  | null | 目的地 |
| 21 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 22 | fattendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 23 | fattapplydate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 24 | fattstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fatttotalamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 27 | fsnapshoturl | 快照 url | varchar | 512 |  |  | null | 快照 url |
| 28 | fattachtype | 文件类型 | varchar | 30 |  |  | null | 文件类型,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_invoiceattachinfo |  | fentryid |
| 2 | idx_er_invoiceattachinfo_fid |  | fid |

---

## 国内/国际差旅报销单-反写记录表 t_er_ntripreimburse_wb

- **表名称：** 国内/国际差旅报销单-反写记录表
- **表名：** t_er_ntripreimburse_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ntripreimbursen_wb |  | fid |
| 2 | pk_t_er_ntripreimburse_wb |  | fentryid |

---

## 关联子实体-子表 t_er_tripclearloanentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_tripclearloanentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_tripclearloanentry_lk |  | fpkid |
| 2 | idx_triploanentry_fentryid |  | fentryid |

---

## 国内/国际差旅报销单-多语言表 t_er_cgrid_tripreimburse_l

- **表名称：** 国内/国际差旅报销单-多语言表
- **表名：** t_er_cgrid_tripreimburse_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 4 | fapplierposition | 职位 | varchar | 100 |  | √ | ' ' | 职位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_nreimbursebill_l_fid |  | fid,flocaleid |
| 2 | pk_t_er_cgrid_tripreimburse_l |  | fpkid |

---

## 出差人-多选基础资料表 t_er_ntrip2reimpartner

- **表名称：** 出差人-多选基础资料表
- **表名：** t_er_ntrip2reimpartner

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_ntrip2reimpartner |  | fpkid |
| 2 | idx_er_ntrip2reimpartner |  | fdetailid |

---

## 发票信息-子表 t_er_ninvoiceinfo

- **表名称：** 发票信息-子表
- **表名：** t_er_ninvoiceinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwithholdingtaxrate | 预扣税率 | numeric | 23 | 10 | √ | 0 | 预扣税率 |
| 3 | fmapexpenseinfo | 关联费用 | varchar | 255 |  | √ | ' ' | 关联费用 |
| 4 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 5 | fuploadseq | 采集顺序 | int8 | 64 |  | √ | 0 | 采集顺序 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcarrierdate | 乘车/机日期 | timestamp | 0 |  |  | null | 乘车/机日期 |
| 8 | foffset | 可抵扣 | bpchar | 1 |  | √ | ' ' | 可抵扣 |
| 9 | finvoiceitemequal | 对平 | bpchar | 1 |  | √ | '1' | 对平 |
| 10 | fbuyeraddressphone | 地址电话 | varchar | 100 |  | √ | ' ' | 地址电话 |
| 11 | fpassengername | 旅客 | varchar | 255 |  | √ | ' ' | 旅客 |
| 12 | fisexcessreim | 允许超额 | bpchar | 1 |  | √ | ' ' | 允许超额 |
| 13 | fenddate | 通行日期止 | timestamp | 0 |  |  | null | 通行日期止 |
| 14 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 15 | ffuelsurcharge | 燃油附加费 | numeric | 23 | 10 | √ | 0 | 燃油附加费 |
| 16 | fordertype | 商旅订单类型 | bpchar | 1 |  | √ | ' ' | 商旅订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 17 | finvoicecode | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 18 | foribalanceamount | 账单余额 | numeric | 23 | 10 | √ | 0 | 账单余额 |
| 19 | fcity | 发票所在地 | varchar | 50 |  | √ | ' ' | 发票所在地 |
| 20 | fbuyername | 收票公司 | varchar | 250 |  | √ | ' ' | 收票公司 |
| 21 | finvoiceno | 发票号码 | varchar | 129 |  | √ | ' ' | 发票号码 |
| 22 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |
| 23 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 24 | fisemployee | 职员 | bpchar | 1 |  | √ | '0' | 职员 |
| 25 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 26 | ftaxdetails | 多税率信息 | varchar | 500 |  | √ | ' ' | 多税率信息 |
| 27 | fpoolreimburseamount | 本次报销金额 | numeric | 23 | 10 | √ | 0 | 本次报销金额 |
| 28 | foffsetamount | 抵扣税额 | numeric | 23 | 10 | √ | 0 | 抵扣税额 |
| 29 | fsellerorgid | 销方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 30 | finvoicecurrencyid | 发票币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fcustomeridnumber | 身份证 | varchar | 50 |  | √ | ' ' | 身份证 |
| 32 | fairportconstructionfee | 民航发展基金及其他 | numeric | 23 | 10 | √ | 0 | 民航发展基金及其他 |
| 33 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 34 | fstartdate | 通行日期起 | timestamp | 0 |  |  | null | 通行日期起 |
| 35 | ffairtime | 飞机乘机时间 | varchar | 20 |  | √ | ' ' | 飞机乘机时间 |
| 36 | fsequencenum | 连号 | varchar | 30 |  | √ | ' ' | 连号,枚举: 1 :是 2 :否 |
| 37 | ftransportnote | 运输票据 | varchar | 30 |  | √ | ' ' | 运输票据,枚举: 1 :是 0 :否 |
| 38 | ffrominvoicecloud | 发票云导入 | bpchar | 1 |  | √ | ' ' | 发票云导入 |
| 39 | fexcessdesc | 超额说明 | varchar | 50 |  | √ | ' ' | 超额说明 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | finoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 42 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 43 | fsequencenuminfo | 连号信息 | varchar | 255 |  | √ | ' ' | 连号信息 |
| 44 | fticketchanges | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :正常 2 :改签 3 :售票 4 :退票 1001 :失控 1002 :作废 1003 :红冲 1004 :异常 1005 :非正常 1006 :红字发票待确认 1007 :部分红冲 1008 :全部红冲 |
| 45 | finvoicesrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 46 | finvoiceischange | 修改 | varchar | 30 |  | √ | ' ' | 修改,枚举: 1 :否 2 :是 |
| 47 | falltaxrate | 税率(%) | varchar | 100 |  | √ | ' ' | 税率(%) |
| 48 | fievalidatest | 查验状态 | bpchar | 1 |  | √ | ' ' | 查验状态,枚举: 1 :通过 2 :不通过 3 :- |
| 49 | fspecialtypemark | 特定业务类型 | varchar | 4 |  | √ | '0' | 特定业务类型,枚举: 1 :成品油发票 2 :稀土发票 3 :机动车发票 4 :农产品收购发票 5 :石脑油发票 6 :卷烟发票 7 :建筑服务发票 8 :货物运输服务发票 9 :不动产销售服务发票 10 :不动产经营租赁服务 11 :代收车船税发票 12 :旅客运输服务发票 13 :自产农产品销售发票 14 :通行费发票 15 :医疗服务（住院）发票 16 :医疗服务（门诊）发票 17 :拖拉机和联合收割机发票 18 :二手车发票 19 :光伏收购发票 20 :出口发票 21 :农产品发票 22 :稀土矿产品发票 23 :稀土产成品发票 24 :铁路电子客票 25 :航空运输电子客票行程单 26 :电子烟 27 :正常开具 28 :反向开具 |
| 50 | fothertotaltaxamount | 其他税费 | numeric | 23 | 10 | √ | 0 | 其他税费 |
| 51 | fcurwithholdingtaxamount | 预扣税额（本位币） | numeric | 23 | 10 | √ | 0 | 预扣税额（本位币） |
| 52 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 53 | finvoicesrcentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 54 | finsurancepremium | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 55 | fspecmodel | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 56 | fvalidatemessage | 发票校验结果 | varchar | 255 |  | √ | ' ' | 发票校验结果 |
| 57 | fairconstfee | 民航发展基金 | numeric | 23 | 10 | √ | 0 | 民航发展基金 |
| 58 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 59 | finvoicealltaxcode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 60 | fbuyerorg | 收票公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 61 | fislinkagedetail | 费用联动 | bpchar | 1 |  | √ | ' ' | 费用联动 |
| 62 | fcount | 发票张数 | int8 | 64 |  | √ | 0 | 发票张数 |
| 63 | finvoicenotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 64 | fismutilreimburse | 多次报销 | bpchar | 1 |  | √ | ' ' | 多次报销 |
| 65 | fispool | 账单池 | bpchar | 1 |  | √ | ' ' | 账单池 |
| 66 | finvexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 67 | fbillcreatetime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 68 | finvoicefrom | 发票来源 | varchar | 30 |  | √ | ' ' | 发票来源,枚举: 1 :发票云 2 :OCR识别 3 :商旅月结 |
| 69 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 70 | fbuyertaxno | 收票方税号 | varchar | 50 |  | √ | ' ' | 收票方税号 |
| 71 | finvexpquotetype | 换算方式 | bpchar | 4 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 72 | fmakeoutcompname | 开票公司 | varchar | 250 |  | √ | ' ' | 开票公司 |
| 73 | fflighttrainnums | 航班号/车次 | varchar | 30 |  | √ | ' ' | 航班号/车次 |
| 74 | fbillingpoolid | 账单id | int8 | 64 |  | √ | 0 | 账单id |
| 75 | fwithholdingtaxamount | 预扣税额 | numeric | 23 | 10 | √ | 0 | 预扣税额 |
| 76 | fismapexpense | 关联 | bpchar | 1 |  | √ | ' ' | 关联,枚举: 1 :是 0 :否 |
| 77 | finvoicesrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: er_expense_recordbill :费用记录 er_trip_recordbill :差旅记录 |
| 78 | fcurrtotalamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 79 | finvoicegoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ninvoiceinfo_query |  | finvoicetype,finvoicedate |
| 2 | pk_t_er_ninvoiceinfo |  | fentryid |
| 3 | idx_er_ninvoice_fserialno |  | fserialno |
| 4 | idx_er_ninvoiceinfo_fseq |  | fid,fseq |
| 5 | idx_er_ninvoiceinfo_invq |  | finvoiceno,finvoicecode |

---

## 差旅明细-子表 t_er_nreimburseentry

- **表名称：** 差旅明细-子表
- **表名：** t_er_nreimburseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftravelexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 2 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0 | 抵扣税额 |
| 3 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 4 | fordernum | 关联订单号 | varchar | 2000 |  | √ | ' ' | 关联订单号 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | foffset | 可抵扣 | bpchar | 1 |  | √ | ' ' | 可抵扣 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 8 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0 | 核定不含税金额（本位币） |
| 9 | fsettlementtype | 结算方式 | bpchar | 1 |  | √ | ' ' | 结算方式,枚举: 1 :现付 2 :月结 |
| 10 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | ' ' | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 11 | finvoicefromparent | 发票来源父节点 | bpchar | 1 |  | √ | ' ' | 发票来源父节点 |
| 12 | fiscancelorder | 退订订单 | bpchar | 1 |  | √ | ' ' | 退订订单 |
| 13 | forderformid | 订单表单ID | varchar | 1000 |  | √ | ' ' | 订单表单ID |
| 14 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 15 | ftaxclasscodeid | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | [税收分类编码 er_taxclasscode](../basedata_files/er_taxclasscode.md) |
| 16 | ftravelcostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 18 | foverdesc | 超差旅标准说明 | varchar | 255 |  | √ | ' ' | 超差旅标准说明 |
| 19 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 20 | fexpenseitemid | 差旅项目 | int8 | 64 |  | √ | 0 | [差旅项目 er_tripexpenseitem](../em_files/er_tripexpenseitem.md) |
| 21 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 22 | fstdexchangerate | 汇率(标准币折本位币) | numeric | 23 | 10 | √ | 0 | 汇率(标准币折本位币) |
| 23 | fnotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 24 | fcheckindatestr | 出发(入住)日期 | varchar | 30 |  | √ | ' ' | 出发(入住)日期 |
| 25 | fcaldaycount | 标准天数 | numeric | 23 | 10 | √ | 0 | 标准天数 |
| 26 | fcheckoutdatestr | 离店日期 | varchar | 30 |  | √ | ' ' | 离店日期 |
| 27 | fcontrolamt | 可报销金额(标准币) | numeric | 23 | 10 | √ | 0 | 可报销金额(标准币) |
| 28 | ffromcitystr | 出发(入住)地 | varchar | 255 |  | √ | ' ' | 出发(入住)地 |
| 29 | fdistance | 里程 | numeric | 23 | 10 | √ | 0 | 里程 |
| 30 | fisovercheck | 校验超额报销 | bpchar | 1 |  | √ | '0' | 校验超额报销 |
| 31 | fairportconstructionfee | 民航发展基金及其他 | numeric | 23 | 10 | √ | 0 | 民航发展基金及其他 |
| 32 | foristdquotetype | 换算方式(报销币折标准币) | bpchar | 1 |  | √ | ' ' | 换算方式(报销币折标准币),枚举: 0 :直接汇率 1 :间接汇率 |
| 33 | forientryappamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fisdefault | 默认推出明细 | bpchar | 1 |  | √ | ' ' | 默认推出明细 |
| 36 | fprovider | 服务商 | varchar | 100 |  | √ | ' ' | 服务商 |
| 37 | fentryappamount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0 | 核定金额(本位币) |
| 38 | ftravelhappendate | 费用归属月份 | timestamp | 0 |  |  | null | 费用归属月份 |
| 39 | fstdexpquotetype | 换算方式(标准币折本位币) | bpchar | 1 |  | √ | ' ' | 换算方式(标准币折本位币),枚举: 0 :直接汇率 1 :间接汇率 |
| 40 | foriamount | 报销金额 | numeric | 23 | 10 | √ | 0 | 报销金额 |
| 41 | fhighseasondaycount | 旺季天数 | numeric | 23 | 10 | √ | 0 | 旺季天数 |
| 42 | foristdexchangerate | 汇率(报销币折标准币) | numeric | 23 | 10 | √ | 0 | 汇率(报销币折标准币) |
| 43 | famount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 报销金额(本位币) |
| 44 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0 | 核定不含税金额 |
| 45 | fisvactax | 专票 | bpchar | 1 |  | √ | ' ' | 专票 |
| 46 | ftravelcostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 47 | ftaxamounttwo | 税额2 | numeric | 23 | 10 | √ | 0 | 税额2 |
| 48 | fpulltravelorder | 商旅上拉订单 | bpchar | 1 |  | √ | ' ' | 商旅上拉订单 |
| 49 | ftocitystr | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 50 | ftravelcostcenter | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 51 | fitemfrom | 来源 | varchar | 2 |  | √ | ' ' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 |
| 52 | ftravelquotactldept | 额度控制部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | fstdentrycurrency | 币种(标准) | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 54 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 55 | fapprovetaxtwo | 核定税额2 | numeric | 23 | 10 | √ | 0 | 核定税额2 |
| 56 | fitemreasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 57 | fentryappamountstd | 核定金额(折标准币) | numeric | 23 | 10 | √ | 0 | 核定金额(折标准币) |
| 58 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 59 | fcurcontrolamt | 可报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 可报销金额(本位币) |
| 60 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 61 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 62 | fquotetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_nreimburseentry_fseq |  | fentryid,fseq |
| 2 | pk_t_er_nreimburseentry |  | fdetailid |

---

## 国内/国际差旅报销单-分表 t_er_cgrid_tripreimburse_a

- **表名称：** 国内/国际差旅报销单-分表
- **表名：** t_er_cgrid_tripreimburse_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fheadexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | ftel | 联系方式 | varchar | 25 |  | √ | ' ' | 联系方式 |
| 4 | ftotalcurinvwhtaxamount | 预扣税合计（发票） | numeric | 23 | 10 | √ | 0 | 预扣税合计（发票） |
| 5 | funrepaymentamount | 申请人未还款 | numeric | 23 | 10 | √ | 0 | 申请人未还款 |
| 6 | ftarbillstatus | 目标单据 | varchar | 30 |  | √ | ' ' | 目标单据,枚举: B1 :项目成本分摊单 |
| 7 | freceiveimagetime | 接收影像或附件日期 | timestamp | 0 |  |  | null | 接收影像或附件日期 |
| 8 | ftotalinvwhtaxamount | 预扣税原币合计（发票） | numeric | 23 | 10 | √ | 0 | 预扣税原币合计（发票） |
| 9 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 10 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | [业务分类 er_projecttype](../em_files/er_projecttype.md) |
| 11 | fheadproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 12 | fcountry | 国家 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_cgrid_tripreimburse_a |  | fid |

---

## 发票信息-分表 t_er_ninvoiceinfo_a

- **表名称：** 发票信息-分表
- **表名：** t_er_ninvoiceinfo_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisxbrl | 是否xbrl | bpchar | 1 |  | √ | ' ' | 是否xbrl |
| 3 | fidestprovince | 目的省份 | varchar | 50 |  | √ | ' ' | 目的省份 |
| 4 | fisred | 红字发票 | bpchar | 1 |  | √ | ' ' | 红字发票,枚举: 0 :否 1 :是 |
| 5 | fissupplement | 后补发票 | bpchar | 1 |  | √ | ' ' | 后补发票,枚举: 0 :否 1 :是 |
| 6 | fregion | 地域 | bpchar | 1 |  | √ | ' ' | 地域,枚举: 1 :国内 2 :国际 |
| 7 | fpassverifybuyername | 发票抬头一致 | varchar | 30 |  | √ | ' ' | 发票抬头一致,枚举: 1 :是 0 :否 |
| 8 | fpassverifybuyertaxno | 发票税号一致 | varchar | 30 |  | √ | ' ' | 发票税号一致,枚举: 1 :是 0 :否 |
| 9 | fexpirypaydate | 付款到期日 | timestamp | 0 |  |  | null | 付款到期日 |
| 10 | ffromcity | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 11 | freasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 12 | finvoiceordernum | 订单号 | varchar | 500 |  | √ | ' ' | 订单号 |
| 13 | fseatgrade | 座位等级 | varchar | 50 |  | √ | ' ' | 座位等级,枚举: |
| 14 | fistartprovince | 出发省份 | varchar | 50 |  | √ | ' ' | 出发省份 |
| 15 | fistartcity | 出发城市 | varchar | 50 |  | √ | ' ' | 出发城市 |
| 16 | fnodeductionreason | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或个人消费 4 :遭受非正常损失 5 :其他 |
| 17 | ftocity | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 18 | fpersonalinvoice | 个人发票 | varchar | 30 |  | √ | ' ' | 个人发票,枚举: 1 :是 0 :否 |
| 19 | ftimegetoff | 下车时间 | timestamp | 0 |  |  | null | 下车时间 |
| 20 | fcountrystr | 国家 | varchar | 500 |  | √ | ' ' | 国家 |
| 21 | fblockchain | 区块链 | bpchar | 1 |  | √ | ' ' | 区块链 |
| 22 | fendorsement | 签注 | varchar | 255 |  | √ | ' ' | 签注 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 24 | ftimegeton | 上车时间 | timestamp | 0 |  |  | null | 上车时间 |
| 25 | fidestcity | 目的城市 | varchar | 50 |  | √ | ' ' | 目的城市 |
| 26 | fcountry | 国家 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_ninvoiceinfo_a |  | fentryid |

---

## 分摊明细-子表 t_er_ntripresharerule

- **表名称：** 分摊明细-子表
- **表名：** t_er_ntripresharerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 3 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fshareremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fsharerulekey | 分摊规则关键字段 | bpchar | 1 |  | √ | ' ' | 分摊规则关键字段 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fshareamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |
| 10 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0 | 分摊比例（%） |
| 12 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ntripresharerule_fseq |  | fid,fseq |
| 2 | pk_t_er_ntripresharerule |  | fdetailid |

---

## 摊销明细-子表 t_er_ntripresharedetail

- **表名称：** 摊销明细-子表
- **表名：** t_er_ntripresharedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 3 | fentrycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0 | 抵扣税额 |
| 5 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 6 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 9 | foffset | 可抵扣 | bpchar | 1 |  | √ | ' ' | 可抵扣 |
| 10 | ftripitemid | 差旅项目 | int8 | 64 |  | √ | 0 | [差旅项目 er_tripexpenseitem](../em_files/er_tripexpenseitem.md) |
| 11 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0 | 核定不含税金额 |
| 12 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0 | 报销金额 |
| 13 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 15 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 报销金额(本位币) |
| 16 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | ' ' | 专票 |
| 17 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 18 | fcurprice | 核定不含税金额本位币 | numeric | 23 | 10 | √ | 0 | 核定不含税金额本位币 |
| 19 | finvoicetypeitem | finvoicetypeitem | varchar | 50 |  | √ | ' ' |  |
| 20 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 21 | ftaxclasscodeid | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | [税收分类编码 er_taxclasscode](../basedata_files/er_taxclasscode.md) |
| 22 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0 | 分摊比例（%） |
| 23 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 24 | fitemfrom | 来源 | varchar | 2 |  | √ | ' ' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 4 :分录导入 |
| 25 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 26 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 27 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 28 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 29 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 30 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 31 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 32 | fsdinvoicetypeitem | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 33 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0 | 核定金额（本位币） |
| 34 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 35 | fairportconstructionfee | 民航发展基金及其他 | numeric | 23 | 10 | √ | 0 | 民航发展基金及其他 |
| 36 | flkwaitentryid | 待摊明细id | varchar | 200 |  | √ | ' ' | 待摊明细id |
| 37 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 38 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fquotetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 40 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_ntripresharedetail |  | fdetailid |
| 2 | idx_er_ntripresharedetai_fseq |  | fid,fseq |

---

## 国内/国际差旅报销单-关联追踪表 t_er_ntripreimburse_tc

- **表名称：** 国内/国际差旅报销单-关联追踪表
- **表名：** t_er_ntripreimburse_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_nreimbursebill_tc_tbill |  | ftbillid |
| 2 | pk_t_er_ntripreimburse_tc |  | fid |
| 3 | idx_er_ntripreimburse_tc_tid |  | ftid |
| 4 | idx_er_ntripreimburse_tc_tbill |  | ftbillid |
| 5 | idx_er_nreim_tc_fsbillid |  | fsbillid |

---

## 收款信息-子表 t_er_ntripaccount

- **表名称：** 收款信息-子表
- **表名：** t_er_ntripaccount

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbuildedamount | 已出单金额 | numeric | 23 | 10 | √ | 0 | 已出单金额 |
| 3 | foriamount | 收款金额 | numeric | 23 | 10 | √ | 0 | 收款金额 |
| 4 | fpayeraccount01 | 银行账号4位 | varchar | 50 |  | √ | ' ' | 银行账号4位 |
| 5 | fpayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 |
| 6 | fentrystatus | 分录状态 | bpchar | 1 |  | √ | ' ' | 分录状态,枚举: F :等待付款 G :已付款 E :审核通过 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | foriaccnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 9 | famount | 收款金额（本位币） | numeric | 23 | 10 | √ | 0 | 收款金额（本位币） |
| 10 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 11 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 12 | fsupplier | 收款人（供应商） | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 13 | fpayeraccountname | 账户名称 | varchar | 50 |  | √ | ' ' | 账户名称 |
| 14 | fpayerid | 收款人 | int8 | 64 |  | √ | 0 | [收款信息 er_payeer](../em_files/er_payeer.md) |
| 15 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0 | 可用余额（本位币） |
| 16 | facccostcompany | 付款公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fcustomer | 收款人（客户） | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 18 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 19 | foriaccpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 20 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 21 | foriaccbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0 | 可用余额 |
| 22 | faccpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已付金额（本位币） |
| 23 | fcasorg | 收款人（内部公司） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | faccnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0 | 未付金额(本位币) |
| 25 | fbanklogo | 银行卡logo图标 | varchar | 255 |  | √ | ' ' | 银行卡logo图标 |
| 26 | fpayeraccount02 | 银行账号(显示_old) | varchar | 50 |  | √ | ' ' | 银行账号(显示_old) |
| 27 | fpayeraccount | 银行账号 | varchar | 50 |  | √ | ' ' | 银行账号 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fquotetype | 换算方式(收款) | bpchar | 1 |  | √ | ' ' | 换算方式(收款),枚举: 0 :直接汇率 1 :间接汇率 |
| 30 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ntripaccount_fseq |  | fid,fseq |
| 2 | pk_t_er_ntripaccount |  | fentryid |

---

## 发票税务明细-子表 t_er_cgridwhinvtaxdetail

- **表名称：** 发票税务明细-子表
- **表名：** t_er_cgridwhinvtaxdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fwhtaxcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 2 | fwhoffsetlogo | 抵销标识 | bpchar | 1 |  | √ | '0' | 抵销标识 |
| 3 | fwhtaxratepercent | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fwhtaxratebase | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 6 | fwhtaxdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | fwhinvdetailid | fwhinvdetailid | int8 | 64 |  | √ | 0 | id |
| 8 | fwhtaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fwhtaxcode | 税码 | int8 | 64 |  | √ | 0 | [税码 bastax_taxcode](../bastax_files/bastax_taxcode.md) |
| 11 | fwhtaxcategory | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fwhinvdetailid | fwhinvdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_cgridwhinvtaxdetail |  | fwhinvdetailid |

---

## 冲申请-子表 t_er_nreimapplyentry

- **表名称：** 冲申请-子表
- **表名：** t_er_nreimapplyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapplytocity | 目的城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 3 | freimbursedamount | 申请金额 | numeric | 23 | 10 | √ | 0 | 申请金额 |
| 4 | fapplystartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 5 | fapplyfromcity | 出发城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fapplyrvehicle | 交通工具 | varchar | 10 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 6 :中转 |
| 8 | fapplyperson | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fapplybilldate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 10 | fapplycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | fsourceapplybillid | 源单ID | varchar | 100 |  | √ | ' ' | 源单ID |
| 12 | fsrcapplybilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: er_tripreqbill_inter :出差申请(全球) er_tripreqbill :出差申请 |
| 13 | fapplybillno | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 14 | fapplydescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 15 | fapplyenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 16 | fapplyexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_nreimapplyentry |  | fentryid |
| 2 | idx_er_nclearapplyent_fapplyno |  | fapplybillno |
| 3 | idx_er_nclearapplyent_fid |  | fid |

---

## 途经地-多选基础资料表 t_er_ntripentrymulwayto

- **表名称：** 途经地-多选基础资料表
- **表名：** t_er_ntripentrymulwayto

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_nmulwayto_entryid |  | fentryid |
| 2 | pk_t_er_ntripentrymulwayto |  | fpkid |

---

## 差旅明细-分表 t_er_nreimburseentry_a

- **表名称：** 差旅明细-分表
- **表名：** t_er_nreimburseentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftrip2travelerscount | 出差人数 | int8 | 64 |  | √ | 0 | 出差人数 |
| 2 | fsplitparent | 拆分父分录 | varchar | 32 |  | √ | ' ' | 拆分父分录 |
| 3 | ftripstanddesc | 差旅标准 | varchar | 50 |  | √ | ' ' | 差旅标准 |
| 4 | fitemreasonfortransferout | fitemreasonfortransferout | varchar | 30 |  | √ | ' ' |  |
| 5 | fisover | 超差旅标准 | bpchar | 1 |  | √ | ' ' | 超差旅标准,枚举: 1 :是 0 :否 |
| 6 | faccstandjson | 住宿补助标准json | text | 0 |  |  | null | 住宿补助标准json |
| 7 | fuseroutstdctrl | 实报实销 | bpchar | 1 |  | √ | ' ' | 实报实销 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | ftripstanddesc_tag | 差旅标准_详情 | text | 0 |  |  | null | 差旅标准_详情 |
| 11 | fitemnodeductionreason | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或个人消费 4 :遭受非正常损失 5 :其他 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_nreimburseentry_a_fseq |  | fentryid |
| 2 | pk_t_er_nreimburseentry_a |  | fdetailid |

---

## 发票与费用明细-子表 t_er_ninvoiceandexp

- **表名称：** 发票与费用明细-子表
- **表名：** t_er_ninvoiceandexp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkeyproperty | 关键字段 | bpchar | 1 |  | √ | ' ' | 关键字段,枚举: 0 :默认值 |
| 3 | finvoiceexpisunbind | 解绑 | bpchar | 1 |  | √ | ' ' | 解绑 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | finvoiceentryid | 发票分录id | int8 | 64 |  | √ | 0 | 发票分录id |
| 6 | finvoiceexpserialno | 发票序列号 | varchar | 255 |  | √ | ' ' | 发票序列号 |
| 7 | fexpenseentryid | 费用明细分录id | int8 | 64 |  | √ | 0 | 费用明细分录id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ninvoiceentryid |  | finvoiceentryid |
| 2 | pk_t_er_ninvoiceandexp |  | fentryid |
| 3 | idx_er_ninvoiceexpenseid |  | fid |
| 4 | idx_er_ninvoiceexpenseentryid |  | fexpenseentryid |

---

## 冲借款-子表 t_er_tripclearloanentry

- **表名称：** 冲借款-子表
- **表名：** t_er_tripclearloanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 3 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 4 | floanbillid | 借款单id | int8 | 64 |  | √ | 0 | 借款单id |
| 5 | fsnapclearoriamount | 快照冲销金额（原币） | numeric | 23 | 10 | √ | 0 | 快照冲销金额（原币） |
| 6 | floanbillno | 借款单编号 | varchar | 30 |  | √ | ' ' | 借款单编号 |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 11 | fsnapclearamount | 快照冲销金额（本位币） | numeric | 23 | 10 | √ | 0 | 快照冲销金额（本位币） |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 13 | fclearoriamount | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 14 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 15 | fclearamount | 冲销金额（本位币） | numeric | 23 | 10 | √ | 0 | 冲销金额（本位币） |
| 16 | freqaccountentryid | 借款分录ID | int8 | 64 |  | √ | 0 | 借款分录ID |
| 17 | foribalanceamount | 借款余额 | numeric | 23 | 10 | √ | 0 | 借款余额 |
| 18 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型,枚举: er_dailyloanbill :借款单 er_tripreqbill :出差借款单 |
| 20 | faccbalanceamount | 借款余额（本位币） | numeric | 23 | 10 | √ | 0 | 借款余额（本位币） |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | fquotetype | 换算方式（冲借款） | bpchar | 1 |  | √ | ' ' | 换算方式（冲借款）,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_tripclearloanentry |  | fentryid |
| 2 | idx_er_nreimclelanent_fseq |  | fid,fseq |

---

## 关联子实体-子表 t_er_ntripreimburse_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_ntripreimburse_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_ntripreimburse_lk |  | fpkid |
| 2 | idx_er_reimbursebill_lk_fid |  | fid |

---

## 出差人-多选基础资料表 t_er_ntripreimbursepartne

- **表名称：** 出差人-多选基础资料表
- **表名：** t_er_ntripreimbursepartne

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ntrippartner_fentryid |  | fentryid |
| 2 | pk_t_er_ntripreimbursepartne |  | fpkid |

---

## 国内/国际差旅报销单-主表 t_er_cgrid_tripreimburse

- **表名称：** 国内/国际差旅报销单-主表
- **表名：** t_er_cgrid_tripreimburse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  | √ | ' ' | 反审核意见 |
| 3 | fautogenshare | 自动生成分摊单 | bpchar | 1 |  | √ | ' ' | 自动生成分摊单 |
| 4 | fpaycompanyid | 支付公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | finvokeinvoicecloud | 与发票云交互 | bpchar | 1 |  | √ | ' ' | 与发票云交互 |
| 6 | fnoinvoice | 无票 | bpchar | 1 |  | √ | ' ' | 无票 |
| 7 | fcheckloanamount | 冲销借款金额 | numeric | 23 | 10 | √ | 0 | 冲销借款金额 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fhasvoucher | 生成凭证 | bpchar | 1 |  | √ | ' ' | 生成凭证 |
| 11 | fisbeforeshare | 费用分摊 | bpchar | 1 |  | √ | ' ' | 费用分摊 |
| 12 | fmonthrulestartdate | 开始月份 | timestamp | 0 |  |  | null | 开始月份 |
| 13 | fhead_paydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 14 | frvehicle | 交通工具 | varchar | 10 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 6 :中转 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 17 | fattachmentcount | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 18 | forigin | 来源 | varchar | 10 |  | √ | ' ' | 来源,枚举: 1 :WEB 2 :移动端 3 :语音助手 |
| 19 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 20 | fneeduploadinvoice | 有待上传的纸票/附件 | bpchar | 1 |  | √ | ' ' | 有待上传的纸票/附件 |
| 21 | fimageno | 影像编码 | varchar | 255 |  | √ | ' ' | 影像编码 |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | floanchecktype | 核销类型 | varchar | 1 |  | √ | ' ' | 核销类型 |
| 24 | fstdbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 25 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0 | 已预提金额 |
| 26 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 27 | fmonthsettleamount | 月结金额 | numeric | 23 | 10 | √ | 0 | 月结金额 |
| 28 | finvoiceoffsetamount | 抵扣税额合计（发票） | numeric | 23 | 10 | √ | 0 | 抵扣税额合计（发票） |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fautomapinvoice | fautomapinvoice | bpchar | 1 |  | √ | ' ' |  |
| 31 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 32 | foffsetamount | 抵扣税额合计（费用） | numeric | 23 | 10 | √ | 0 | 抵扣税额合计（费用） |
| 33 | fsharerule | 分摊规则 | varchar | 30 |  | √ | ' ' | 分摊规则,枚举: orgrule :按部门分摊 monthrule :按月分摊 yearrule :按年分摊 |
| 34 | frstartdate | 出发日期 | timestamp | 0 |  |  | null | 出发日期 |
| 35 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 36 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 37 | fnextauditor | fnextauditor | varchar | 80 |  | √ | ' ' |  |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | ' ' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 40 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fisoverbudget | 超预算 | bpchar | 1 |  | √ | ' ' | 超预算 |
| 42 | fisshared | 已分摊 | bpchar | 1 |  | √ | ' ' | 已分摊 |
| 43 | fistravelers | 多出差人 | bpchar | 1 |  | √ | ' ' | 多出差人 |
| 44 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 45 | fprojectsharecount | 下游项目成本分摊单数 | int8 | 64 |  | √ | 0 | 下游项目成本分摊单数 |
| 46 | fpayamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 47 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fsharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0 | 已分摊金额 |
| 49 | fbillkind | 单据种类 | bpchar | 1 |  | √ | ' ' | 单据种类,枚举: 0 :卡片展示的差旅报销单 1 :表格展示的差旅报销单 |
| 50 | fabovequotadept | 部门额度超额 | varchar | 30 |  | √ | ' ' | 部门额度超额,枚举: 1 :超额 2 :未超额 0 :- |
| 51 | fencashamount | 付现金额 | numeric | 23 | 10 | √ | 0 | 付现金额 |
| 52 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_tripreimburse_cardgrid :差旅费报销单 |
| 54 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fis_all_einvoice | 发票状态 | bpchar | 1 |  | √ | ' ' | 发票状态,枚举: 0 :无发票 1 :全电票 2 :含纸票 3 :其它 |
| 56 | ftriptypeid | 出差类型 | int8 | 64 |  | √ | 0 | [出差类型 er_triptype](../em_files/er_triptype.md) |
| 57 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 58 | fabovequotaemp | 员工额度超额 | varchar | 30 |  | √ | ' ' | 员工额度超额,枚举: 1 :超额 2 :未超额 0 :- |
| 59 | fisstdover | 是否超差旅标准 | bpchar | 1 |  | √ | ' ' | 是否超差旅标准 |
| 60 | fiscurrency | 多币种 | bpchar | 1 |  | √ | ' ' | 多币种 |
| 61 | fisinvoicemodified | 发票修改 | bpchar | 1 |  | √ | ' ' | 发票修改 |
| 62 | fissmallreim | 大票小报 | bpchar | 1 |  | √ | ' ' | 大票小报 |
| 63 | fmonthruleenddate | 结束月份 | timestamp | 0 |  |  | null | 结束月份 |
| 64 | fapplierposition | 职位 | varchar | 100 |  | √ | ' ' | 职位 |
| 65 | fisloan | 冲销出差借款单 | bpchar | 1 |  | √ | ' ' | 冲销出差借款单 |
| 66 | fbizitem | 业务事项 | int8 | 64 |  | √ | 0 | [业务事项 er_standard_type](../em_files/er_standard_type.md) |
| 67 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 68 | frfrom | 出发地 | varchar | 80 |  | √ | ' ' | 出发地 |
| 69 | fsharemethod | 分摊方法 | varchar | 30 |  | √ | ' ' | 分摊方法,枚举: rate :比例分摊 avg :金额平均 amount :金额分摊 |
| 70 | fispaybyhead | 按单头付款 | bpchar | 1 |  | √ | ' ' | 按单头付款 |
| 71 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 72 | frto | 目的地 | varchar | 80 |  | √ | ' ' | 目的地 |
| 73 | frenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 74 | fcurrencyid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_nreim_fcompanyid |  | fcompanyid |
| 2 | idx_er_nreim_ccom_adate |  | fcostcompanyid,fauditdate |
| 3 | idx_er_nreim_fbillno |  | fbillno |
| 4 | pk_t_er_cgrid_tripreimburse |  | fid |
| 5 | idx_er_nreim_fapplierid |  | fapplierid |
| 6 | idx_er_nreim_fcreatorid |  | fcreatorid |
| 7 | idx_er_nreim_fbillstatus |  | fbillstatus |
| 8 | idx_er_nreim_fbizdate_fbillno |  | fbizdate,fbillno |

---

## 付款信息-子表 t_er_ntrippayentry

- **表名称：** 付款信息-子表
- **表名：** t_er_ntrippayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetpayorg | 付款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftargetbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | ftargetbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 5 | fdpcurrency | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | ffee | 手续费 | numeric | 23 | 10 | √ | 0 | 手续费 |
| 8 | fdpexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0 | 付款汇率 |
| 9 | flossamt | 汇兑损益 | numeric | 23 | 10 | √ | 0 | 汇兑损益 |
| 10 | ftargetentrustorg | 委托付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fdpamt | 付款金额 | numeric | 23 | 10 | √ | 0 | 付款金额 |
| 12 | fagreedrate | 兑换汇率 | numeric | 23 | 10 | √ | 0 | 兑换汇率 |
| 13 | ftargetpayacctid | 付款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 14 | ftargetlocalamount | 收款金额(本位币) | numeric | 23 | 10 | √ | 0 | 收款金额(本位币) |
| 15 | ftargetexchange | 收款汇率 | numeric | 23 | 10 | √ | 0 | 收款汇率 |
| 16 | ftargetpaybank | 付款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 17 | ffeecurrency | 手续费币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fdplocalamt | 付款金额(本位币) | numeric | 23 | 10 | √ | 0 | 付款金额(本位币) |
| 19 | ftargetpayamt | 收款金额 | numeric | 23 | 10 | √ | 0 | 收款金额 |
| 20 | ftargetpayacct | 付款账号（文本） | varchar | 50 |  | √ | ' ' | 付款账号（文本） |
| 21 | ftargetopenorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | ftargetpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 23 | ftargetbillid | 目标单据id | int8 | 64 |  | √ | 0 | 目标单据id |
| 24 | ftargetcurrency | 收款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | ftargetsettletype | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ntrippayent_ftarget |  | ftargetbillid |
| 2 | pk_t_er_ntrippayentry |  | fentryid |
| 3 | idx_er_ntrippayentry_fid |  | fid,fseq |

---

## 发票明细-子表 t_er_ninvoiceitem

- **表名称：** 发票明细-子表
- **表名：** t_er_ninvoiceitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexcludeamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 4 | finvoiceitemoffset | 可抵扣 | bpchar | 1 |  | √ | ' ' | 可抵扣 |
| 5 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | finvoiceitemisunbind | 解绑 | bpchar | 1 |  | √ | ' ' | 解绑 |
| 8 | finvoicetaxamount | 单头税额 | numeric | 23 | 10 | √ | 0 | 单头税额 |
| 9 | finvoicecurrency | 发票币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 11 | funitprice | 不含税单价 | numeric | 23 | 10 | √ | 0 | 不含税单价 |
| 12 | fspecmodel | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 13 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 14 | finvoicecloudoffset | 发票抵扣 | bpchar | 1 |  | √ | ' ' | 发票抵扣 |
| 15 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 16 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 17 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |
| 18 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 19 | finvoiceitemserialno | 发票序列号 | varchar | 255 |  | √ | ' ' | 发票序列号 |
| 20 | finvoiceheadentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 21 | fgoodscode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 22 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 23 | finvoicetaxrate | 单头税率 | varchar | 500 |  | √ | ' ' | 单头税率 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ninvoiceitem_invhea |  | finvoiceheadentryid |
| 2 | pk_t_er_ninvoiceitem |  | fentryid |
| 3 | idx_er_ninvoiceitem_fid |  | fid |

---

## 座位等级-多选基础资料表 t_er_ntripitemseatgrade

- **表名称：** 座位等级-多选基础资料表
- **表名：** t_er_ntripitemseatgrade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [座位等级设置 er_seatgradestd](../em_files/er_seatgradestd.md) |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_ntripitemseatgrade |  | fpkid |
| 2 | idx_er_ntripitemseatgra_detail |  | fdetailid |

---

## 汇总金额-子表 t_er_summaryamountentry

- **表名称：** 汇总金额-子表
- **表名：** t_er_summaryamountentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsummonthsettle | 月结 | bpchar | 1 |  | √ | ' ' | 月结 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fsumoritripamount | 报销金额 | numeric | 23 | 10 | √ | 0 | 报销金额 |
| 5 | fsumtaxamountinvoice | 税额(发票) | numeric | 23 | 10 | √ | 0 | 税额(发票) |
| 6 | fsumoffsetamount | 抵扣税额(发票) | numeric | 23 | 10 | √ | 0 | 抵扣税额(发票) |
| 7 | fsumdeductibletax | 抵扣税额(费用) | numeric | 23 | 10 | √ | 0 | 抵扣税额(费用) |
| 8 | fsumcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fsumoritripappamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 10 | fsumtripappamount | 核定金额(本位币) | numeric | 23 | 10 | √ | 0 | 核定金额(本位币) |
| 11 | fsumtripamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 报销金额(本位币) |
| 12 | fsumtaxamount | 税额(费用) | numeric | 23 | 10 | √ | 0 | 税额(费用) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_summaryamountentry |  | fentryid |
| 2 | idx_er_summtentry_fenttryid |  | fid |

---

## 关联子实体-子表 t_er_nreimapplyentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_nreimapplyentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_nreimapplyentry_lk |  | fpkid |
| 2 | idx_t_er_nreimapplyent_lk_fent |  | fentryid |

---

## 项目干系人-多选基础资料表 t_er_ntripreimburseower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_ntripreimburseower

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_ntripreimburseower_fid |  | fid |
| 2 | pk_t_er_ntripreimburseower |  | fpkid |

---

## 申请单出差人-多选基础资料表 t_er_ntripapplytravelers

- **表名称：** 申请单出差人-多选基础资料表
- **表名：** t_er_ntripapplytravelers

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_napptravelers_fentryid |  | fentryid |
| 2 | pk_t_er_ntripapplytravelers |  | fpkid |

---

## 行程信息-子表 t_er_nreimbursetripentry

- **表名称：** 行程信息-子表
- **表名：** t_er_nreimbursetripentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamounttotalori | 税额汇总（原币） | numeric | 23 | 10 | √ | 0 | 税额汇总（原币） |
| 3 | ftripdeductibletax | 行程抵扣税额合计 | numeric | 23 | 10 | √ | 0 | 行程抵扣税额合计 |
| 4 | fiscreateprojectcostshare | 生成项目分摊单 | int8 | 64 |  | √ | 0 | 生成项目分摊单 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftripentrystatus | 行程状态 | varchar | 5 |  | √ | ' ' | 行程状态,枚举: A :暂存 B :提交 C :审核中 D :审核不通过 E :审核通过 |
| 7 | fnotaxamounttotalori | 不含税金额汇总（原币） | numeric | 23 | 10 | √ | 0 | 不含税金额汇总（原币） |
| 8 | ftripamount | 本位币金额 | numeric | 23 | 10 | √ | 0 | 本位币金额 |
| 9 | ftoadm | 目的地 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 10 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fenddate | 行程期间.结束 | timestamp | 0 |  |  | null | 行程期间.结束 |
| 12 | ffromadm | 出发地 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 13 | ftoplaceid | 目的地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 14 | fsharedamount | 已分摊金额（本位币） | numeric | 23 | 10 | √ | 0 | 已分摊金额（本位币） |
| 15 | fexpwithholdingamount | 已预提金额本位币 | numeric | 23 | 10 | √ | 0 | 已预提金额本位币 |
| 16 | ftriphappendate | 费用归属月份 | timestamp | 0 |  |  | null | 费用归属月份 |
| 17 | fvehicle | 交通工具 | varchar | 50 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 |
| 18 | ffromplaceid | 出发地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 19 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 20 | ftripentrysourceid | 源单行程分录ID | int8 | 64 |  | √ | 0 | 源单行程分录ID |
| 21 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | ftripappamount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0 | 核定金额（本位币） |
| 23 | fisexistmonthly | 是否存在月结订单 | bpchar | 1 |  | √ | ' ' | 是否存在月结订单 |
| 24 | ftripappnottaxamount | 核定不含税金额（本位币）合计 | numeric | 23 | 10 | √ | 0 | 核定不含税金额（本位币）合计 |
| 25 | ftripentrykey | 关键字段 | bpchar | 1 |  | √ | ' ' | 关键字段 |
| 26 | ftripexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 27 | ftripentryarea | 出差地域 | int8 | 64 |  | √ | 0 | [出差地域 er_triparea](../em_files/er_triparea.md) |
| 28 | ftripisoverbudget | 超标(预算) | bpchar | 1 |  | √ | ' ' | 超标(预算) |
| 29 | fstartdate | 行程期间.开始 | timestamp | 0 |  |  | null | 行程期间.开始 |
| 30 | forisharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0 | 已分摊金额 |
| 31 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 32 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | ftripday | 行程天数 | int8 | 64 |  | √ | 0 | 行程天数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_nreimbursetripentry_fid |  | fid |
| 2 | pk_t_er_nreimbursetripentry |  | fentryid |
