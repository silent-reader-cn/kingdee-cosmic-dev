# 对公报销单-er_publicreimbursebill

## 关联子实体-子表 t_er_pubreimbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_pubreimbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_pubreimbill_lk |  | fpkid |

---

## 发票云附件-子表 t_er_invoiceattachinfo

- **表名称：** 发票云附件-子表
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

## 发票信息-子表 t_er_pubreiminvoiceinfo

- **表名称：** 发票信息-子表
- **表名：** t_er_pubreiminvoiceinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 3 | fuploadseq | 采集顺序 | int8 | 64 |  | √ | 0 | 采集顺序 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | finvoiceitemequal | 对平 | bpchar | 1 |  | √ | '1' | 对平 |
| 6 | fisexcessreim | 允许超额度 | bpchar | 1 |  | √ | '0' | 允许超额度 |
| 7 | fenddate | 通行日期止 | timestamp | 0 |  |  | null | 通行日期止 |
| 8 | finvoicecode | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 9 | foribalanceamount | 账单余额 | numeric | 23 | 10 | √ | 0 | 账单余额 |
| 10 | fcity | 发票所在地 | varchar | 50 |  | √ | ' ' | 发票所在地 |
| 11 | fbuyername | 收票公司 | varchar | 250 |  | √ | ' ' | 收票公司 |
| 12 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 13 | freasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 14 | foffsetamount | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 15 | fistartcity | 出发城市 | varchar | 50 |  | √ | ' ' | 出发城市 |
| 16 | fstartdate | 通行日期起 | timestamp | 0 |  |  | null | 通行日期起 |
| 17 | fsequencenum | 连号 | varchar | 30 |  | √ | ' ' | 连号,枚举: 1 :是 2 :否 |
| 18 | fblockchain | 区块链 | bpchar | 1 |  | √ | '0' | 区块链 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fidestcity | 目的城市 | varchar | 50 |  | √ | ' ' | 目的城市 |
| 21 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 22 | fsequencenuminfo | 连号信息 | varchar | 255 |  | √ | ' ' | 连号信息 |
| 23 | fticketchanges | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :正常 2 :改签 3 :售票 4 :退票 1001 :失控 1002 :作废 1003 :红冲 1004 :异常 1005 :非正常 1006 :红字发票待确认 1007 :部分红冲 1008 :全部红冲 |
| 24 | falltaxrate | 税率(%) | varchar | 100 |  | √ | ' ' | 税率(%) |
| 25 | fcurwithholdingtaxamount | 预扣税额（本位币） | numeric | 23 | 10 | √ | 0 | 预扣税额（本位币） |
| 26 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 27 | finsurancepremium | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 28 | fvalidatemessage | 发票校验结果 | varchar | 255 |  | √ | ' ' | 发票校验结果 |
| 29 | fairconstfee | 民航发展基金 | numeric | 23 | 10 | √ | 0 | 民航发展基金 |
| 30 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 31 | finvoicealltaxcode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 32 | finvoicenotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 33 | fispool | 账单池 | bpchar | 1 |  | √ | '0' | 账单池 |
| 34 | finvoicefrom | 发票来源 | bpchar | 1 |  | √ | '1' | 发票来源,枚举: 0 :手工新增 1 :发票云 2 :OCR识别 3 :商旅月结 5 :采购商城 6 :excel导入 |
| 35 | ffromcity | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 36 | fbuyertaxno | 收票方税号 | varchar | 50 |  | √ | ' ' | 收票方税号 |
| 37 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 38 | finvexpquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 39 | fflighttrainnums | 航班号/车次 | varchar | 30 |  | √ | ' ' | 航班号/车次 |
| 40 | fbillingpoolid | 账单id | int8 | 64 |  | √ | 0 | 账单id |
| 41 | fwithholdingtaxamount | 预扣税额 | numeric | 23 | 10 | √ | 0 | 预扣税额 |
| 42 | fcurrtotalamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 43 | fendorsement | 签注 | varchar | 255 |  | √ | ' ' | 签注 |
| 44 | fwithholdingtaxrate | 预扣税率 | numeric | 23 | 10 | √ | 0 | 预扣税率 |
| 45 | ftaxrate | 平均税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 平均税率（%） |
| 46 | fcarrierdate | 乘车/机日期 | timestamp | 0 |  |  | null | 乘车/机日期 |
| 47 | foffset | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 48 | fisred | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票,枚举: 0 :否 1 :是 |
| 49 | fbuyeraddressphone | 地址电话 | varchar | 255 |  | √ | ' ' | 地址电话 |
| 50 | fpassengername | 旅客 | varchar | 255 |  |  | null | 旅客 |
| 51 | fissupplement | 后补发票 | bpchar | 1 |  | √ | '0' | 后补发票,枚举: 0 :否 1 :是 |
| 52 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 53 | ffuelsurcharge | 燃油附加费 | numeric | 23 | 10 | √ | 0 | 燃油附加费 |
| 54 | fpassverifybuyername | 发票抬头一致 | varchar | 30 |  | √ | ' ' | 发票抬头一致,枚举: 1 :是 0 :否 |
| 55 | fpassverifybuyertaxno | 发票税号一致 | varchar | 30 |  | √ | ' ' | 发票税号一致,枚举: 1 :是 0 :否 |
| 56 | finvoiceno | 发票号码 | varchar | 129 |  | √ | ' ' | 发票号码 |
| 57 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |
| 58 | fexpirypaydate | 付款到期日 | timestamp | 0 |  |  | null | 付款到期日 |
| 59 | fisemployee | 职员 | bpchar | 1 |  | √ | '0' | 职员 |
| 60 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 61 | ftaxdetails | 多税率信息 | varchar | 500 |  | √ | ' ' | 多税率信息 |
| 62 | fseatgrade | 座位等级 | varchar | 50 |  | √ | ' ' | 座位等级,枚举: |
| 63 | fpoolreimburseamount | 本次报销金额 | numeric | 23 | 10 | √ | 0 | 本次报销金额 |
| 64 | fsellerorgid | 销方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 65 | finvoicecurrencyid | 发票币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 66 | fbuyerorgid | 收票公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 67 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车销售发票 13 :二手车销售发票 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 26 :数电发票（普通发票） 27 :数电发票（增值税专用发票） 28 :数电票（航空运输电子客票行程单） 29 :数电票（铁路电子客票） 30 :形式发票 |
| 68 | fairportconstructionfee | 民航发展基金及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 民航发展基金及其他 |
| 69 | ftocity | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 70 | fcustomeridnumber | 身份证 | varchar | 50 |  | √ | ' ' | 身份证 |
| 71 | ffairtime | 乘车/机时间 | varchar | 20 |  | √ | ' ' | 乘车/机时间 |
| 72 | ftransportnote | 运输票据 | varchar | 30 |  | √ | ' ' | 运输票据,枚举: 1 :是 0 :否 |
| 73 | ffrominvoicecloud | 发票云导入 | bpchar | 1 |  | √ | '0' | 发票云导入 |
| 74 | finvaddr | 发票下载地址 | varchar | 512 |  | √ | ' ' | 发票下载地址 |
| 75 | fexcessdesc | 超额度说明 | varchar | 512 |  | √ | ' ' | 超额度说明 |
| 76 | fcountrystr | 国家 | varchar | 500 |  | √ | ' ' | 国家 |
| 77 | finoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 78 | ftimegeton | 上车时间 | timestamp | 0 |  |  | null | 上车时间 |
| 79 | fcountry | 国家 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 80 | fisxbrl | xbrl | bpchar | 1 |  | √ | '0' | xbrl |
| 81 | finvoiceischange | 已修改 | varchar | 30 |  | √ | ' ' | 已修改,枚举: 1 :否 2 :是 |
| 82 | fievalidatest | 查验状态 | bpchar | 1 |  | √ | '3' | 查验状态,枚举: 1 :通过 2 :不通过 3 :- |
| 83 | fidestprovince | 目的省份 | varchar | 50 |  | √ | ' ' | 目的省份 |
| 84 | fspecialtypemark | 特定业务类型 | varchar | 4 |  | √ | '0' | 特定业务类型,枚举: 1 :成品油发票 2 :稀土发票 3 :机动车发票 4 :农产品收购发票 5 :石脑油发票 6 :卷烟发票 7 :建筑服务发票 8 :货物运输服务发票 9 :不动产销售服务发票 10 :不动产经营租赁服务 11 :代收车船税发票 12 :旅客运输服务发票 13 :自产农产品销售发票 14 :通行费发票 15 :医疗服务（住院）发票 16 :医疗服务（门诊）发票 17 :拖拉机和联合收割机发票 18 :二手车发票 19 :光伏收购发票 20 :出口发票 21 :农产品发票 22 :稀土矿产品发票 23 :稀土产成品发票 24 :铁路电子客票 25 :航空运输电子客票行程单 26 :电子烟 27 :正常开具 28 :反向开具 |
| 85 | fothertotaltaxamount | 其他税费 | numeric | 23 | 10 | √ | 0 | 其他税费 |
| 86 | fspecmodel | 规格型号 | varchar | 600 |  | √ | ' ' | 规格型号 |
| 87 | fislinkagedetail | 费用联动 | bpchar | 1 |  | √ | '0' | 费用联动 |
| 88 | fregion | 地域 | bpchar | 1 |  |  | null | 地域,枚举: 1 :国内 2 :国际 |
| 89 | fcount | 发票张数 | int8 | 64 |  | √ | 0 | 发票张数 |
| 90 | fismutilreimburse | 多次报销 | bpchar | 1 |  | √ | '0' | 多次报销 |
| 91 | finvexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 92 | fbillcreatetime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 93 | finvoicetypeid | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 94 | fmakeoutcompname | 开票公司 | varchar | 250 |  | √ | ' ' | 开票公司 |
| 95 | fistartprovince | 出发省份 | varchar | 50 |  | √ | ' ' | 出发省份 |
| 96 | fnodeductionreason | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或个人消费 4 :遭受非正常损失 5 :其他 |
| 97 | fismapexpense | 关联费用明细 | bpchar | 1 |  | √ | '1' | 关联费用明细,枚举: 1 :是 0 :否 |
| 98 | fpersonalinvoice | 个人发票 | varchar | 30 |  | √ | ' ' | 个人发票,枚举: 1 :是 0 :否 |
| 99 | ftimegetoff | 下车时间 | timestamp | 0 |  |  | null | 下车时间 |
| 100 | finvoicegoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_pubreiminvoiceinfo_pkey |  | fentryid |
| 2 | idx_er_pubreim_ivcif_fseq |  | fid,fseq |
| 3 | idx_er_invoice_pub_invq |  | finvoiceno,finvoicecode |
| 4 | idx_er_invoice_pub_query |  | finvoicetype,finvoicedate |
| 5 | idx_er_invoice_pub_serialno |  | fserialno |

---

## 关联子实体-子表 t_er_pubreimwrioffdet_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_pubreimwrioffdet_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_pubreimwrioffdet_lk |  | fpkid |
| 2 | idx_er_pubreimwroffdt_lk_fid |  | fentryid |

---

## 发票与费用明细-子表 t_er_pubinvoiceandexpense

- **表名称：** 发票与费用明细-子表
- **表名：** t_er_pubinvoiceandexpense

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fkeyproperty | 关键字段 | bpchar | 1 |  | √ | '0' | 关键字段,枚举: 0 :默认值 |
| 3 | finvoiceexpisunbind | 解绑 | bpchar | 1 |  | √ | '0' | 解绑 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | finvoiceentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
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
| 1 | t_er_pubinvoiceandexpense_pkey |  | fentryid |
| 2 | idx_pubinvoiceandexpense_id |  | fid |

---

## 资产与发票明细-子表 t_er_asset_invoiceitem_re

- **表名称：** 资产与发票明细-子表
- **表名：** t_er_asset_invoiceitem_re

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvoiceitementryid | 发票明细分录id | int8 | 64 |  | √ | 0 | 发票明细分录id |
| 3 | fassetdetailid | 资产信息分录id | int8 | 64 |  | √ | 0 | 资产信息分录id |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_asset_invoice_item |  | fassetdetailid,finvoiceitementryid |
| 2 | pk_er_asset_invoiceitem_re |  | fentryid |

---

## 商旅订单-子表 t_er_publicremorderentry

- **表名称：** 商旅订单-子表
- **表名：** t_er_publicremorderentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forderdeductibletax | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |
| 3 | ftotalamount | 订单金额 | numeric | 23 | 10 | √ | 0 | 订单金额 |
| 4 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0 | 服务费 |
| 5 | fendorsementamount | 改签费 | numeric | 23 | 10 | √ | 0 | 改签费 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | forderstatusstr | 订单状态 | varchar | 50 |  | √ | ' ' | 订单状态 |
| 8 | frefundamount | 退票/退订费 | numeric | 23 | 10 | √ | 0 | 退票/退订费 |
| 9 | ffromplace | 出发地 | varchar | 2000 |  | √ | ' ' | 出发地 |
| 10 | ftravelername | 使用人 | varchar | 255 |  | √ | ' ' | 使用人 |
| 11 | frefundamounttax | 退票费可抵扣税额 | numeric | 23 | 10 | √ | 0 | 退票费可抵扣税额 |
| 12 | fbegintime | 出发时间 | timestamp | 0 |  |  | null | 出发时间 |
| 13 | foabillnum | 申请单号 | varchar | 255 |  | √ | ' ' | 申请单号 |
| 14 | foperationtype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 7 :服务费 8 :用餐 |
| 15 | fticketprice | 票价 | numeric | 23 | 10 | √ | 0 | 票价 |
| 16 | fserver | 服务商 | varchar | 50 |  | √ | ' ' | 服务商,枚举: CHAILVYIHAO :差旅壹号 DIDI :滴滴 MEITUAN :美团 XIECHENG :携程 ZHAOSHANG :招商银行 GAODE :高德 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 |
| 17 | ftoplace | 目的地 | varchar | 2000 |  | √ | ' ' | 目的地 |
| 18 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 19 | forderformid | 订单表单ID | varchar | 255 |  | √ | ' ' | 订单表单ID |
| 20 | fparentordernum | 父订单号 | varchar | 255 |  | √ | ' ' | 父订单号 |
| 21 | ffuelprice | 燃油费 | numeric | 23 | 10 | √ | 0 | 燃油费 |
| 22 | fticketstatus | 订单使用状态（机票） | varchar | 50 |  | √ | ' ' | 订单使用状态（机票）,枚举: USED :已使用 UNUSED :未使用 REFOUND :已退票 CHANGED :已改签 |
| 23 | fordercostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | forderbookeddept | 申请人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 26 | fordercompany | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fticketpricedeductibletax | 票价可抵扣税额 | numeric | 23 | 10 | √ | 0 | 票价可抵扣税额 |
| 28 | fordernumber | 订单号 | varchar | 255 |  | √ | ' ' | 订单号 |
| 29 | fordexpenseentryid | 关联费用明细id | int8 | 64 |  | √ | 0 | 关联费用明细id |
| 30 | fordercurrency | 订单币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fservicefeedeductibletax | 服务费可抵扣税额 | numeric | 23 | 10 | √ | 0 | 服务费可抵扣税额 |
| 32 | fordercostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fairportprice | 民航发展基金及其他/税费 | numeric | 23 | 10 | √ | 0 | 民航发展基金及其他/税费 |
| 35 | fassuranceamount | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 36 | fendtime | 到达时间 | timestamp | 0 |  |  | null | 到达时间 |
| 37 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_pubreim_order_fid |  | fid |
| 2 | pk_er_publicremorderentry |  | fentryid |

---

## 关联合同-子表 t_er_pubreimcontract

- **表名称：** 关联合同-子表
- **表名：** t_er_pubreimcontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcontractcode | 合同号 | varchar | 500 |  | √ | ' ' | 合同号 |
| 3 | fcontractapplier | 经办人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | foricontractnonpayamount | 在途金额(原币) | numeric | 23 | 10 | √ | 0 | 在途金额(原币) |
| 5 | fcontractcurrreimamount | 付款金额（本位币） | numeric | 23 | 10 | √ | 0 | 付款金额（本位币） |
| 6 | fsourceentryid | fsourceentryid | int8 | 64 |  | √ | 0 |  |
| 7 | foricontractnotpayamount | 未付金额（原币） | numeric | 23 | 10 | √ | 0 | 未付金额（原币） |
| 8 | fsigndate | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 9 | fcontractproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fcontractexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 12 | fcontractpartatypenew | 甲方类型 | varchar | 50 |  | √ | ' ' | 甲方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司(行政组织) bos_org :公司 cas_othercontactunit :其他往来单位 |
| 13 | fcontractgainorloss | 本次核销汇兑损益 | numeric | 23 | 10 | √ | 0 | 本次核销汇兑损益 |
| 14 | fcontractdescription | 合同说明 | varchar | 1000 |  | √ | ' ' | 合同说明 |
| 15 | fcontractexpquotetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 16 | fcontractcanamount | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 17 | fcontractsrcentryid | 关联合同分录id | int8 | 64 |  | √ | 0 | 关联合同分录id |
| 18 | fcontractpaytypeid | 付款类型 | int8 | 64 |  | √ | 0 | [付款用途 cas_paymentbilltype](../cas_files/cas_paymentbilltype.md) |
| 19 | fcontractpartbtype | 乙方类型 | varchar | 50 |  | √ | ' ' | 乙方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司(行政组织) bos_org :公司 cas_othercontactunit :其他往来单位 |
| 20 | fentryprepayedamount | 已预付金额 | numeric | 23 | 10 | √ | 0 | 已预付金额 |
| 21 | fcontractsid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 22 | fcontractpartanew | 甲方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 23 | fentryinvoiceamount | 到票金额 | numeric | 23 | 10 | √ | 0 | 到票金额 |
| 24 | fentrycurrprepayedamount | 已预付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已预付金额（本位币） |
| 25 | fcontractentrycurrency | 关联合同币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | fcontractnotpayamount | 未付金额（本位币） | numeric | 23 | 10 | √ | 0 | 未付金额（本位币） |
| 27 | fcontractcostorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 28 | fcontractname | 合同名称 | varchar | 500 |  | √ | ' ' | 合同名称 |
| 29 | fcontracthappendate | 预计付款日期 | timestamp | 0 |  |  | null | 预计付款日期 |
| 30 | fcontractwriteoff | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 31 | fcontractpartb | 乙方 | varchar | 100 |  | √ | ' ' | 供应商 bd_supplier |
| 32 | fcontractnonpayamount | 在途金额 | numeric | 23 | 10 | √ | 0 | 在途金额 |
| 33 | fcontractparta | 甲方(old) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 35 | fcontractentrychangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 36 | fcontractcurrcanamount | 可报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 可报销金额(本位币) |
| 37 | fcontractcurrwriteoff | 冲销金额（本位币） | numeric | 23 | 10 | √ | 0 | 冲销金额（本位币） |
| 38 | fcontractreimamount | 付款金额 | numeric | 23 | 10 | √ | 0 | 付款金额 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_pubreimcontract |  | fentryid |
| 2 | idx_er_pubreimcontract_fcontractcode |  | fcontractcode |

---

## 对公报销单-主表 t_er_pubreimbill

- **表名称：** 对公报销单-主表
- **表名：** t_er_pubreimbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fautogenshare | 自动生成分摊单 | bpchar | 1 |  | √ | '0' | 自动生成分摊单 |
| 4 | fpaycompanyid | 支付公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | finvokeinvoicecloud | 与发票云交互 | bpchar | 1 |  | √ | '0' | 与发票云交互 |
| 6 | fassetorgid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fnoinvoice | 无票 | bpchar | 1 |  | √ | '0' | 无票 |
| 8 | forgid | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fbillpayertype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 bos_org :内部公司 cas_othercontactunit :其他往来单位 |
| 11 | fhasvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 12 | fisbeforeshare | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 13 | fhead_paydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 14 | fmonthrulestartdate | 开始月份 | timestamp | 0 |  |  | null | 开始月份 |
| 15 | fisonaccount | 挂账 | bpchar | 1 |  | √ | '0' | 挂账 |
| 16 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 17 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 19 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 20 | fapplierpositionstr | fapplierpositionstr | varchar | 100 |  | √ | ' ' |  |
| 21 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 22 | fisonway | 支持在途 | bpchar | 1 |  | √ | '0' | 支持在途 |
| 23 | fisover | 超费用标准（提交后有值） | bpchar | 1 |  | √ | '0' | 超费用标准（提交后有值） |
| 24 | fneeduploadinvoice | 有待上传的纸票/附件 | bpchar | 1 |  | √ | '0' | 有待上传的纸票/附件 |
| 25 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 26 | foffsetinvoiceno | 可抵扣发票号码 | varchar | 255 |  | √ | ' ' | 可抵扣发票号码 |
| 27 | fstdbilltype | fstdbilltype | varchar | 30 |  | √ | ' ' |  |
| 28 | fsourcebilltype | 源单类型(已废弃) | varchar | 30 |  | √ | ' ' | 源单类型(已废弃) |
| 29 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 30 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 31 | fmonthsettleamount | 月结金额 | numeric | 23 | 10 | √ | 0 | 月结金额 |
| 32 | finvoiceoffsetamount | 抵扣税额合计（发票） | numeric | 23 | 10 | √ | 0 | 抵扣税额合计（发票） |
| 33 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 34 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 35 | fautomapinvoice | 智能发票报销 | bpchar | 1 |  | √ | '1' | 智能发票报销 |
| 36 | fmigsrc | 来源系统 | int4 | 32 |  | √ | 0 | 来源系统 |
| 37 | foffsetamount | 抵扣税额合计（费用） | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额合计（费用） |
| 38 | fimagenumber | 影像编号 | varchar | 255 |  | √ | ' ' | 影像编号 |
| 39 | fsharerule | 分摊规则 | varchar | 30 |  | √ | ' ' | 分摊规则,枚举: orgrule :按部门分摊 monthrule :按月分摊 yearrule :按年分摊 expenseitemrule :按费用项目分摊 |
| 40 | fassettype | 资产类型 | varchar | 20 |  | √ | ' ' | 资产类型,枚举: newasset :新增资产 existasset :已有资产 |
| 41 | frameworkcontract | 框架合同 | bpchar | 1 |  | √ | '0' | 框架合同 |
| 42 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 43 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 44 | fpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 45 | fnextauditor | 下一步审核人 | varchar | 100 |  | √ | ' ' | 下一步审核人 |
| 46 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 47 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | ' ' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 48 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 49 | fisoverbudget | 超预算 | bpchar | 1 |  | √ | '0' | 超预算 |
| 50 | fcontractsconn | 关联合同 | varchar | 1000 |  | √ | ' ' | 关联合同 |
| 51 | ftel | 联系方式 | varchar | 100 |  | √ | ' ' | 联系方式 |
| 52 | fisshared | 已分摊 | bpchar | 1 |  | √ | '0' | 已分摊 |
| 53 | fbillpayerid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 54 | fredoffsetdes | 红冲说明 | varchar | 1000 |  | √ | ' ' | 红冲说明 |
| 55 | fpayamount | 付现 | numeric | 23 | 10 | √ | 0.0000000000 | 付现 |
| 56 | fprojectsharecount | 下游项目成本分摊单数 | int8 | 64 |  | √ | 0 | 下游项目成本分摊单数 |
| 57 | fabovequota | 超额度 | bpchar | 1 |  | √ | '0' | 超额度,枚举: 1 :超额度 2 :未超额度 0 :- |
| 58 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 59 | fneedsuppleinvoice | 发票后补 | bpchar | 1 |  | √ | '0' | 发票后补 |
| 60 | fsharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额 |
| 61 | funrepaymentamount | 申请人未还款 | numeric | 23 | 10 | √ | 0 | 申请人未还款 |
| 62 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 63 | fispush | 合同下推生成 | varchar | 255 |  | √ | ' ' | 合同下推生成 |
| 64 | fstdreimbursetype | 关联业务 | varchar | 30 |  | √ | ' ' | 关联业务,枚举: biztype_project :立项 biztype_contract :合同 biztype_other :其他 |
| 65 | fpaycurrency | 付现金额币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 66 | fisredoffset | 红冲 | bpchar | 1 |  | √ | '0' | 红冲 |
| 67 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_loanbill :出差借款单 er_tripreimbursebill :差旅费报销单 er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_dailyreimbursebill :费用报销单 er_repaymentbill :还款单 er_publicreimbursebill :对公报销单 |
| 68 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 69 | fis_all_einvoice | 发票状态 | bpchar | 1 |  | √ | '0' | 发票状态,枚举: 0 :无发票 1 :全电票 2 :含纸票 3 :其它 |
| 70 | fonaccountamount | 挂账金额 | numeric | 23 | 10 | √ | 0 | 挂账金额 |
| 71 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 72 | fproxytax | 代扣代缴 | bpchar | 1 |  | √ | '0' | 代扣代缴 |
| 73 | fiscurrency | 多币种 | bpchar | 1 |  | √ | '0' | 多币种 |
| 74 | freimbursetype | 报账类型 | varchar | 30 |  | √ | ' ' | 报账类型,枚举: asset :资产报账 expense :费用报账 entertainment :招待费 meetting :会议费 otherexpenses :其他 |
| 75 | fisinvoicemodified | 发票修改 | bpchar | 1 |  | √ | '0' | 发票修改 |
| 76 | fauditopinion | 审核意见 | varchar | 100 |  | √ | ' ' | 审核意见 |
| 77 | fmonthruleenddate | 结束月份 | timestamp | 0 |  |  | null | 结束月份 |
| 78 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 79 | fispaybyhead | 按单头付款 | bpchar | 1 |  | √ | '0' | 按单头付款 |
| 80 | fsharemethod | 分摊方法 | varchar | 30 |  | √ | ' ' | 分摊方法,枚举: rate :比例分摊 avg :金额平均 amount :金额分摊 |
| 81 | freimrelatedcontractamoun | 关联合同是否扣减代扣代缴 | varchar | 10 |  | √ | '1' | 关联合同是否扣减代扣代缴 |
| 82 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 83 | ftotalaccloanamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 84 | ftarbillstatus | 目标单据 | varchar | 30 |  | √ | ' ' | 目标单据,枚举: A1 :采购转固单(保存) A2 :采购转固单(已审) B1 :项目成本分摊单 C1 :工程转固单 |
| 85 | freimbursecurrency | 报销金额币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 86 | fiscrepayablebill | 生成应付单 | bpchar | 1 |  | √ | '0' | 生成应付单,枚举: 0 :否 1 :是 |
| 87 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | [业务分类 er_projecttype](../em_files/er_projecttype.md) |
| 88 | fcurrencyid | 本位币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 89 | fisneedinstall | 需安装 | bpchar | 1 |  | √ | '0' | 需安装 |
| 90 | fbillpayeramount | 往来单位预付余额 | numeric | 23 | 10 | √ | 0 | 往来单位预付余额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_pubreim_fbillno |  | fbillno |
| 2 | idx_er_pubreim_fcompanyid |  | fcompanyid |
| 3 | idx_er_pubreim_fcostcompanyid |  | fcostcompanyid |
| 4 | idx_er_pubreim_fapplierid |  | fapplierid |
| 5 | idx_er_pubreim_fbizdate_bno |  | fbizdate,fbillno |
| 6 | t_er_pubreimbill_pkey |  | fid |
| 7 | idx_er_pubreim_fbillstatus |  | fbillstatus |
| 8 | idx_er_pubreim_fcreatorid |  | fcreatorid |

---

## 关联子实体-子表 t_er_pubreimexpdet_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_pubreimexpdet_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_pubreimexpdet_lk |  | fpkid |
| 2 | idx_er_pubreimexpdet_lk_fid |  | fentryid |

---

## 关联子实体-子表 t_er_pubreimcontract_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_pubreimcontract_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_pubreimcontract_lk |  | fpkid |
| 2 | idx_er_pubreimcontract_lk |  | fsbillid |

---

## 费用明细-分表 t_er_pubreimexpdet_a

- **表名称：** 费用明细-分表
- **表名：** t_er_pubreimexpdet_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwithholdingtaxrate | 预扣税率 | numeric | 23 | 10 | √ | 0 | 预扣税率 |
| 3 | ftreatway | 招待方式 | varchar | 10 |  | √ | ' ' | 招待方式,枚举: 1 :餐费 2 :酒店住宿 3 :酒水 4 :纪念品 |
| 4 | fgoodsnum | 酒水瓶数 | int4 | 32 |  | √ | 0 | 酒水瓶数 |
| 5 | fotherstandarddesc | 酒水标准 | varchar | 255 |  | √ | ' ' | 酒水标准 |
| 6 | fwineway | 酒水来源 | varchar | 10 |  | √ | ' ' | 酒水来源,枚举: 1 :内部领用 2 :自行购买 3 :无酒水 |
| 7 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 8 | ffeequotetype | 换算方式(标准) | bpchar | 1 |  | √ | '0' | 换算方式(标准),枚举: 0 :直接汇率 1 :间接汇率 |
| 9 | fotherfeeamount | 酒水金额 | numeric | 23 | 10 | √ | 0 | 酒水金额 |
| 10 | fredml | 红酒（毫升） | int4 | 32 |  | √ | 0 | 红酒（毫升） |
| 11 | fcurwithholdingtaxamount | 预扣税额（本位币） | numeric | 23 | 10 | √ | 0 | 预扣税额（本位币） |
| 12 | fmeetlevel | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 13 | fcityarea | 城市类别 | int8 | 64 |  | √ | 0 | [出差地域 er_triparea](../em_files/er_triparea.md) |
| 14 | fwhiteml | 白酒（毫升） | int4 | 32 |  | √ | 0 | 白酒（毫升） |
| 15 | fothercontrolamt | 酒水可报金额 | numeric | 23 | 10 | √ | 0 | 酒水可报金额 |
| 16 | fisover | 超费用标准 | bpchar | 1 |  | √ | '0' | 超费用标准 |
| 17 | fcurotherfeeamount | 酒水金额 | numeric | 23 | 10 | √ | 0 | 酒水金额 |
| 18 | fotherstandamount | 酒水标准金额(页面不可见) | numeric | 23 | 10 | √ | 0 | 酒水标准金额(页面不可见) |
| 19 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 20 | ftripbookamount | 商旅预定金额 | numeric | 23 | 10 | √ | 0 | 商旅预定金额 |
| 21 | fescortnum | 陪同人数 | int4 | 32 |  | √ | 0 | 陪同人数 |
| 22 | ffeecurrency | 币种(标准) | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 23 | foverdesc | 超标说明(暂未支持) | varchar | 255 |  | √ | ' ' | 超标说明(暂未支持) |
| 24 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | [报销级别 er_reimburselevel](../em_files/er_reimburselevel.md) |
| 25 | ffeeexchangerate | 汇率(标准) | numeric | 23 | 10 | √ | 0 | 汇率(标准) |
| 26 | fisexistmonthly | 关联商旅订单 | bpchar | 1 |  | √ | '0' | 关联商旅订单 |
| 27 | ftripbookcuramount | 商旅预定金额（本位币） | numeric | 23 | 10 | √ | 0 | 商旅预定金额（本位币） |
| 28 | fdaysnum | 住宿天数 | int4 | 32 |  | √ | 0 | 住宿天数 |
| 29 | fmeetitem | 会议事项 | varchar | 10 |  | √ | ' ' | 会议事项,枚举: 1 :伙食费 2 :酒店住宿 3 :交通费 4 :其他 |
| 30 | ftreatnum | 招待人数 | int4 | 32 |  | √ | 0 | 招待人数 |
| 31 | fcontrolamt | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 32 | fcurothercontrolamt | 酒水可报金额 | numeric | 23 | 10 | √ | 0 | 酒水可报金额 |
| 33 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 34 | fisovercheck | 校验超额度报销 | bpchar | 1 |  | √ | '0' | 校验超额度报销 |
| 35 | ffeestandid | 费用标准基础资料 | int8 | 64 |  | √ | 0 | [费用标准 er_standard](../em_files/er_standard.md) |
| 36 | fexpisredoffset | 红冲(明细) | bpchar | 1 |  | √ | '0' | 红冲(明细) |
| 37 | fwithholdingtaxamount | 预扣税额 | numeric | 23 | 10 | √ | 0 | 预扣税额 |
| 38 | fcurcontrolamt | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 39 | ffeestandardamt | 费用标准金额(页面不可见) | numeric | 23 | 10 | √ | 0 | 费用标准金额(页面不可见) |
| 40 | ffeestandarddesc | 费用标准 | varchar | 255 |  | √ | ' ' | 费用标准 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_pubreim_expdet_a_fid |  | fid |
| 2 | pk_t_er_pubreimexpdet_a |  | fdetailid |

---

## 冲借款-子表 t_er_pubreimwrioffdet

- **表名称：** 冲借款-子表
- **表名：** t_er_pubreimwrioffdet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floanperson | 借款人 | varchar | 200 |  | √ | ' ' | 借款人 |
| 3 | fentrywlunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 4 | floanbill | floanbill | int8 | 64 |  | √ | 0 |  |
| 5 | floanbillnov1 | 单据编号 | varchar | 100 |  | √ | '0' | 单据编号 |
| 6 | fcurbalancewhtaxamount | 预扣税余额（本位币） | numeric | 23 | 10 | √ | 0 | 预扣税余额（本位币） |
| 7 | fsourceentryid | 借款明细分录ID | int8 | 64 |  | √ | 0 | 借款明细分录ID |
| 8 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcurrloanamount | 借款余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额（本位币） |
| 10 | floanprojectno | 立项号 | varchar | 200 |  | √ | ' ' | 立项号 |
| 11 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 12 | fsrcofsrcentryid | 冲借款源分录id | int8 | 64 |  | √ | 0 | 冲借款源分录id |
| 13 | floanapplydatev1 | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 14 | fsourcesign | 关联申请 | bpchar | 1 |  | √ | '0' | 关联申请 |
| 15 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 17 | faccwhtaxamount | 冲销预扣税 | numeric | 23 | 10 | √ | 0 | 冲销预扣税 |
| 18 | faccloanamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 19 | fcurraccloanamount | 冲销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额(本位币) |
| 20 | floanamount | 借款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额 |
| 21 | floanexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 22 | fbalancewhtaxamount | 预扣税余额 | numeric | 23 | 10 | √ | 0 | 预扣税余额 |
| 23 | floancurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 24 | fsourcebillid | 源单id | varchar | 100 |  | √ | ' ' | 源单id |
| 25 | fsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型,枚举: er_dailyloanbill :借款单 er_tripreqbill :出差借款单 er_prepaybill :预付单 |
| 26 | floandescriptionv1 | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 27 | fcuraccwhtaxamount | 冲销预扣税（本位币） | numeric | 23 | 10 | √ | 0 | 冲销预扣税（本位币） |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fquotetype | 换算方式（冲借款） | bpchar | 1 |  | √ | '0' | 换算方式（冲借款）,枚举: 0 :直接汇率 1 :间接汇率 |
| 30 | fsourceexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 31 | fentrywltype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 32 | floancontractno | 合同号 | varchar | 500 |  | √ | ' ' | 合同号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_pubreimwrioffdet_pkey |  | fentryid |
| 2 | idx_er_pubreimwrioffdet_fid |  | fid |

---

## 发票明细-子表 t_er_pubreiminvoiceitem

- **表名称：** 发票明细-子表
- **表名：** t_er_pubreiminvoiceitem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexcludeamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 3 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 4 | finvoiceitemoffset | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 5 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | finvoiceitemisunbind | 解绑 | bpchar | 1 |  | √ | '0' | 解绑 |
| 8 | finvoicetaxamount | 单头税额 | numeric | 23 | 10 | √ | 0 | 单头税额 |
| 9 | finvoicecurrency | 发票币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 10 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 11 | funitprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 12 | fspecmodel | 规格型号 | varchar | 600 |  | √ | ' ' | 规格型号 |
| 13 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 14 | finvoicecloudoffset | 发票抵扣 | bpchar | 1 |  | √ | '1' | 发票抵扣 |
| 15 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 16 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 17 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |
| 18 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 19 | fitementryid | 费用项目分录id | int8 | 64 |  | √ | 0 | 费用项目分录id |
| 20 | finvoiceitemserialno | 发票序列号 | varchar | 255 |  | √ | ' ' | 发票序列号 |
| 21 | finvoiceheadentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 22 | fgoodscode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 23 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 24 | finvoicetaxrate | 单头税率 | varchar | 255 |  | √ | ' ' | 单头税率 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_pubreiminvoiceitem_pkey |  | fentryid |
| 2 | idx_er_pubreim_ivcite |  | fitementryid |
| 3 | idx_er_pubreiminvoiceitem_fid |  | fid |
| 4 | idx_er_pubreim_ivcite_invhead |  | finvoiceheadentryid |

---

## 冲预提-子表 t_er_publicwithholding

- **表名称：** 冲预提-子表
- **表名：** t_er_publicwithholding

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fwhdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 3 | fwhquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 4 | fwhentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fwhbillpayertype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 7 | forgiwhbalanceamount | 冲销余额 | numeric | 23 | 10 | √ | 0 | 冲销余额 |
| 8 | fwhcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 9 | fwhbalanceamount | 冲销余额(本位币) | numeric | 23 | 10 | √ | 0 | 冲销余额(本位币) |
| 10 | fwithholdingbillno | 预提单号 | varchar | 100 |  | √ | '0' | 预提单号 |
| 11 | fwhpayername | 申请人 | varchar | 200 |  | √ | ' ' | 申请人 |
| 12 | fwhsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型 |
| 13 | fwhbillpayerid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fwhentrycostcompanyid | 分录费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fwhcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | fwhbursedcurramount | 冲销金额(本位币) | numeric | 23 | 10 | √ | 0 | 冲销金额(本位币) |
| 17 | fwhbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 18 | fwithholdingtype | 预提类型 | int8 | 64 |  | √ | 0 | [预提类型 er_withholdingtype](../em_files/er_withholdingtype.md) |
| 19 | fwhsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 20 | fwhentrycostdeptid | 分录费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fwhsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 22 | fwhbursedamount | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fwhexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 25 | fsourcewhitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_publicwithholding |  | fentryid |
| 2 | idx_er_pubreim_withholding_fid |  | fid,fseq |

---

## 资产信息-子表 t_er_assetentry

- **表名称：** 资产信息-子表
- **表名：** t_er_assetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassetsrcbillno | 源单编号 | varchar | 200 |  | √ | ' ' | 源单编号 |
| 3 | fhappendate | 资产发生日期 | timestamp | 0 |  |  | null | 资产发生日期 |
| 4 | fentrycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fmobiledeldoneflag | 移动端删除完成标志 | int4 | 32 |  | √ | 0 | 移动端删除完成标志 |
| 6 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 7 | fassetstoreplace | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fassetcat | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 10 | fcurrexpenseamount | 含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 含税金额(本位币) |
| 11 | fassetmodel | 规格型号 | varchar | 200 |  | √ | ' ' | 规格型号 |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 1 | 汇率 |
| 13 | fsubjectmatter | 标的物 | varchar | 150 |  | √ | ' ' | 标的物 |
| 14 | fexpquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 15 | fassetbillno | 资产编号 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fassetcostdeptid | 使用部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fassetsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 19 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 20 | forientryamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 21 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | fassetname | 资产名称 | varchar | 200 |  | √ | ' ' | 资产名称 |
| 23 | fassetquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 24 | fpricewithouttax | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 25 | fassetentryid | 分录id | int8 | 64 |  | √ | 0 | 分录id |
| 26 | fassetuserid | 使用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fexpenseamount | 含税金额 | numeric | 23 | 10 | √ | 0 | 含税金额 |
| 28 | fis_special_invoice | 专票 | bpchar | 1 |  | √ | '0' | 专票 |
| 29 | fassetunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | fcurentryamount | 金额（本位币） | numeric | 23 | 10 | √ | 0 | 金额（本位币） |
| 31 | fassetnumber | 卡片编号 | varchar | 100 |  | √ | ' ' | 卡片编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_assetentry |  | fdetailid |
| 2 | idx_er_pubreim_asset_fseq |  | fid,fseq |

---

## 对公报销单-分表 t_er_pubreimbill_a

- **表名称：** 对公报销单-分表
- **表名：** t_er_pubreimbill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxshareway | 税额分摊方式 | bpchar | 1 |  | √ | '1' | 税额分摊方式,枚举: 1 :按分摊金额与税率计算 2 :按分摊金额比例计算 |
| 3 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 4 | fmeetlevel | fmeetlevel | varchar | 10 |  | √ | ' ' |  |
| 5 | fcityarea | 城市类别 | int8 | 64 |  | √ | 0 | [出差地域 er_triparea](../em_files/er_triparea.md) |
| 6 | ftotalcurwhtaxamount | 预扣税合计（费用） | numeric | 23 | 10 | √ | 0 | 预扣税合计（费用） |
| 7 | ftotalwhtaxamount | 预扣税原币合计（费用） | numeric | 23 | 10 | √ | 0 | 预扣税原币合计（费用） |
| 8 | ftotalcurinvwhtaxamount | 预扣税合计（发票） | numeric | 23 | 10 | √ | 0 | 预扣税合计（发票） |
| 9 | ftotalinvwhtaxamount | 预扣税原币合计（发票） | numeric | 23 | 10 | √ | 0 | 预扣税原币合计（发票） |
| 10 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 11 | fescortnum | 陪同人数 | int4 | 32 |  | √ | 0 | 陪同人数 |
| 12 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | [报销级别 er_reimburselevel](../em_files/er_reimburselevel.md) |
| 13 | fchangeinvoicedes | 换票说明 | varchar | 1000 |  | √ | ' ' | 换票说明 |
| 14 | fdaysnum | 住宿天数 | int4 | 32 |  | √ | 0 | 住宿天数 |
| 15 | fismultireimburser | 多报销人 | bpchar | 1 |  | √ | '0' | 多报销人 |
| 16 | fwhtaxbear | 往来方承担预扣税 | bpchar | 1 |  | √ | '1' | 往来方承担预扣税 |
| 17 | ftrdbillno | 第三方业务编码 | varchar | 80 |  | √ | ' ' | 第三方业务编码 |
| 18 | fisstopreim | 止付 | bpchar | 1 |  | √ | '0' | 止付 |
| 19 | ftreatnum | 招待人数 | int4 | 32 |  | √ | 0 | 招待人数 |
| 20 | fischangeinvoice | 换发票 | bpchar | 1 |  | √ | '0' | 换发票 |
| 21 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 22 | fissmallreim | 大票小报 | bpchar | 1 |  | √ | '0' | 大票小报 |
| 23 | fmeetgrade | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 24 | fbizitem | 业务事项 | int8 | 64 |  | √ | 0 | [业务事项 er_standard_type](../em_files/er_standard_type.md) |
| 25 | fstopdescription | 止付说明 | varchar | 1000 |  | √ | ' ' | 止付说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_pubreim_a_bizitem |  | fbizitem |
| 2 | pk_t_er_pubreimbill_a |  | fid |

---

## 摊销明细-子表 t_er_publicresharedetail

- **表名称：** 摊销明细-子表
- **表名：** t_er_publicresharedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 3 | fentrycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 4 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 5 | fsdentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | [商机登记F7 mpm_bizopregf7](../mpm_files/mpm_bizopregf7.md) |
| 6 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 7 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 10 | foffset | 可抵扣 | bpchar | 1 |  | √ | '1' | 可抵扣 |
| 11 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 12 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 13 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 15 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
| 16 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | '1' | 专票 |
| 17 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 18 | fcurprice | 核定不含税金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额本位币 |
| 19 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | '0' | 发票类型,枚举: 0 :空 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车销售发票 13 :二手车销售发票 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 26 :数电发票（普通发票） 27 :数电发票（增值税专用发票） 28 :数电票（航空运输电子客票行程单） 29 :数电票（铁路电子客票） 30 :形式发票 |
| 20 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 21 | ftaxclasscodeid | 税收分类编号基础资料 | int8 | 64 |  | √ | 0 | [税收分类编码 er_taxclasscode](../basedata_files/er_taxclasscode.md) |
| 22 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 23 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |
| 24 | fitemfrom | 来源 | varchar | 2 |  | √ | '0' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 4 :分录导入 |
| 25 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 26 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 27 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 28 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 29 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 30 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 31 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 32 | finvoicetypeiditem | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 33 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 34 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 35 | fairportconstructionfee | 民航发展基金及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 民航发展基金及其他 |
| 36 | flkwaitentryid | 待摊明细id | varchar | 200 |  | √ | ' ' | 待摊明细id |
| 37 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 38 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 39 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 40 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 41 | fsdentrympmtaskid | 任务号 | int8 | 64 |  |  | null | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_publicsharedetail_fseq |  | fid,fseq |
| 2 | pk_t_er_publicresharedetail |  | fdetailid |

---

## 对公报销单-多语言表 t_er_pubreimbill_l

- **表名称：** 对公报销单-多语言表
- **表名：** t_er_pubreimbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapplierpositionstr | 职位文本 | varchar | 100 |  | √ | ' ' | 职位文本 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_pubreimbill_l_pkey |  | fpkid |
| 2 | idx_pubreim_l_id |  | fid,flocaleid |

---

## 税务明细-子表 t_er_whtaxdetail

- **表名称：** 税务明细-子表
- **表名：** t_er_whtaxdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fwhtaxcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 2 | fwhoffsetlogo | 抵销标识 | bpchar | 1 |  | √ | '0' | 抵销标识 |
| 3 | fwhdetailid | fwhdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fwhtaxratepercent | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fwhtaxratebase | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 7 | fwhtaxdesc | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 9 | fwhtaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 10 | fwhtaxcode | 税码 | int8 | 64 |  | √ | 0 | [税码 bastax_taxcode](../bastax_files/bastax_taxcode.md) |
| 11 | fwhtaxcategory | 税种 | int8 | 64 |  | √ | 0 | [税种 bd_taxcategory](../basedata_files/bd_taxcategory.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fwhdetailid | fwhdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_whtaxdetail |  | fwhdetailid |

---

## 关联子实体-子表 t_er_publicwithholding_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_publicwithholding_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_publicwithholding_lk |  | fpkid |
| 2 | idx_er_publicwithholding_lk_fk |  | fentryid |

---

## 关联子实体-子表 t_er_pubreimaccinfo_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_pubreimaccinfo_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_pubreimaccinfo_lk |  | fpkid |
| 2 | idx_er_pubreimaccinfo_lk_fk |  | fentryid |

---

## 对公报销单-反写记录表 t_er_pubreimbill_wb

- **表名称：** 对公报销单-反写记录表
- **表名：** t_er_pubreimbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_pubreim_wb_fid |  | fid |
| 2 | pk_t_er_pubreimbill_wb |  | fentryid |

---

## 对公报销单-关联追踪表 t_er_pubreimbill_tc

- **表名称：** 对公报销单-关联追踪表
- **表名：** t_er_pubreimbill_tc

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
| 1 | pk_t_er_pubreimbill_tc |  | fid |
| 2 | idx_er_pubreimbill_tc_ftbillid |  | ftbillid |
| 3 | idx_er_pubreimbill_tc_tid |  | ftid |
| 4 | idx_er_pubreimbill_tc_tbill |  | ftbillid |

---

## 费用明细-子表 t_er_pubreimexpdet

- **表名称：** 费用明细-子表
- **表名：** t_er_pubreimexpdet

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | [商机登记F7 mpm_bizopregf7](../mpm_files/mpm_bizopregf7.md) |
| 3 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 4 | fentrycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 5 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 6 | fwbcurrency | 核销币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 8 | fwbamount | 核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核销金额 |
| 9 | fiscreateprojectcostshare | 生成项目分摊单 | int8 | 64 |  | √ | 0 | 生成项目分摊单 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fiscreateappaycount | 生成应付次数 | int4 | 32 |  | √ | 0 | 生成应付次数 |
| 12 | foffset | 可抵扣 | bpchar | 1 |  | √ | '1' | 可抵扣 |
| 13 | ffentrympmtaskid | 任务号 | int8 | 64 |  |  | null | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 14 | fproxyamt | 代扣代缴个税 | numeric | 23 | 10 | √ | 0.0000000000 | 代扣代缴个税 |
| 15 | fentrycontractname | 合同名称 | varchar | 500 |  |  | ' ' | 合同名称 |
| 16 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 17 | fitemnodeductionreason | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: 1 :用于非应税项目 2 :用于免税项目 3 :用于集体福利或个人消费 4 :遭受非正常损失 5 :其他 |
| 18 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 19 | fwbsrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: contract :合同单 project :立项单 estimate :费用暂估单 er_vehiclecheckingbill :用车结算单 pur_receipt :商城验收单 er_mealcheckingbill :用餐结算单 |
| 20 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
| 21 | fsubjectmatter | 标的物 | varchar | 150 |  | √ | ' ' | 标的物 |
| 22 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | '1' | 专票 |
| 23 | fcurprice | 核定金额不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额不含税金额（本位币） |
| 24 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | '0' | 发票类型,枚举: 0 :空 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车销售发票 13 :二手车销售发票 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 26 :数电发票（普通发票） 27 :数电发票（增值税专用发票） 28 :数电票（航空运输电子客票行程单） 29 :数电票（铁路电子客票） 30 :形式发票 |
| 25 | finvoicefromparent | 发票来源父节点 | bpchar | 1 |  | √ | '0' | 发票来源父节点 |
| 26 | fwbsrcentryid | （核销）分录id | int8 | 64 |  | √ | 0 | （核销）分录id |
| 27 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 28 | ftaxclasscodeid | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | [税收分类编码 er_taxclasscode](../basedata_files/er_taxclasscode.md) |
| 29 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 30 | fexpnonpayamount | 在途金额 | numeric | 23 | 10 | √ | 0 | 在途金额 |
| 31 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 32 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 33 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 34 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 35 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 36 | fwbexchangrate | 核销汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 核销汇率 |
| 37 | fassetquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 38 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 39 | fentryproducttype | 产品类别 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 40 | freimburser | 报销人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fentrysubprojectno | fentrysubprojectno | varchar | 200 |  | √ | ' ' |  |
| 42 | fwbsrcbillno | 源单编号 | varchar | 200 |  | √ | ' ' | 源单编号 |
| 43 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 44 | fairportconstructionfee | 民航发展基金及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 民航发展基金及其他 |
| 45 | fcurproxyamt | 代扣代缴个税(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 代扣代缴个税(本位币) |
| 46 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 47 | fentryprojectno | 立项号 | varchar | 200 |  | √ | ' ' | 立项号 |
| 48 | fassetnumber | 资产编号 | varchar | 100 |  | √ | ' ' | 资产编号 |
| 49 | fwbsrcbillid | （核销）源单id | int8 | 64 |  | √ | 0 | （核销）源单id |
| 50 | fsplitparent | 拆分父分录 | varchar | 32 |  | √ | ' ' | 拆分父分录 |
| 51 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 52 | fassetstoreplace | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 53 | fassetcat | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 54 | fexpentrystatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: F :等待付款 G :已付款 I :关闭 E :审核通过 |
| 55 | fassetmodel | 规格型号 | varchar | 200 |  | √ | ' ' | 规格型号 |
| 56 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 57 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 58 | fwbcuramount | 核销金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 核销金额本位币 |
| 59 | fissettle | 结算状态 | bpchar | 30 |  | √ | ' ' | 结算状态,枚举: unsettle :未结算 partsettle :部分结算 settled :全部结算 |
| 60 | fsharedamount | 已分摊金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额（本位币） |
| 61 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 62 | fpricewithtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 63 | fexpwithholdingamount | 已预提金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额本位币 |
| 64 | fassetbillno | 卡片编号 | int8 | 64 |  | √ | 0 | [资产卡片基础资料 fa_card_real_base](../fa_files/fa_card_real_base.md) |
| 65 | fcontractitemid | 合同付款条目id | int8 | 64 |  | √ | 0 | 合同付款条目id |
| 66 | fentrycontractno | 合同号 | varchar | 500 |  | √ | ' ' | 合同号 |
| 67 | fitemfrom | 来源 | bpchar | 1 |  | √ | '0' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 4 :分录导入 5 :采购商城 |
| 68 | fremark | 备注 | varchar | 2000 |  | √ | ' ' | 备注 |
| 69 | fiscrepayableentry | 生成应付单 | bpchar | 1 |  | √ | '0' | 生成应付单,枚举: 0 :否 1 :是 |
| 70 | fassetname | 资产名称 | varchar | 200 |  | √ | ' ' | 资产名称 |
| 71 | fitemreasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 72 | finvoicetypeiditem | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 73 | fexpebalanceamount | fexpebalanceamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 74 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 75 | fwbpaytype | 付款类型 | varchar | 80 |  | √ | ' ' | 付款类型,枚举: PREPAYMENT :预付款 PROGRESSPAYMENT :进度款 SETTLEPAYMENT :结算款 BOND :保证金 REWORDORPUNISH :奖惩 OTHERS :其它 |
| 76 | freimctldeptid | 额度控制部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 77 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 78 | fassetunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 79 | fexpischangeinvoice | 已解绑 | bpchar | 1 |  | √ | '0' | 已解绑 |
| 80 | forisharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额 |
| 81 | fwbquotetype | 核销换算方式 | bpchar | 1 |  | √ | '0' | 核销换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 82 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 83 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 84 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_preim_edet_feccompanyid |  | fentrycostcompanyid |
| 2 | idx_er_pubreim_expdet_fseq |  | fid,fseq |
| 3 | idx_er_preim_edet_fwbsrcbillid |  | fwbsrcbillid |
| 4 | idx_er_preim_edet_fassetbillno |  | fassetbillno |
| 5 | t_er_pubreimexpdet_pkey |  | fdetailid |

---

## 付款信息-子表 t_er_publicreimpayentry

- **表名称：** 付款信息-子表
- **表名：** t_er_publicreimpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetpayorg | 付款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftargetbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | ftargetbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 5 | fdpcurrency | 付款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ffee | 手续费 | numeric | 23 | 10 | √ | 0.0000000000 | 手续费 |
| 8 | ftargetentrustorg | 委托付款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fdpexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 付款汇率 |
| 10 | flossamt | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 11 | fdpamt | 付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额 |
| 12 | fagreedrate | 兑换汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 兑换汇率 |
| 13 | ftargetlocalamount | 收款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额(本位币) |
| 14 | ftargetpayacctid | 付款账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 15 | ftargetexchange | 收款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 收款汇率 |
| 16 | ftargetpaybank | 付款银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 17 | ffeecurrency | 手续费币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fdplocalamt | 付款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额(本位币) |
| 19 | ftargetpayamt | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 20 | ftargetpayacct | 付款账号（文本） | varchar | 50 |  | √ | ' ' | 付款账号（文本） |
| 21 | ftargetopenorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | ftargetbillid | 目标单据id | int8 | 64 |  | √ | 0 | 目标单据id |
| 23 | ftargetpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
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
| 1 | t_er_publicreimpayentry_pkey |  | fentryid |
| 2 | idx_er_prpe_feq |  | fid,fseq |
| 3 | idx_er_prpe_targetbillid_no |  | ftargetbillid,ftargetbillno |

---

## 关联子实体-子表 t_er_pubreimwrioffapply_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_pubreimwrioffapply_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_pubreimwroff_lk_fid |  | fentryid |
| 2 | pk_t_er_pubreimwrioffapply_lk |  | fpkid |

---

## 项目干系人-多选基础资料表 t_er_publicreimburseower

- **表名称：** 项目干系人-多选基础资料表
- **表名：** t_er_publicreimburseower

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
| 1 | idx_er_publicreimburseower_fid |  | fid |
| 2 | pk_t_er_publicreimburseower |  | fpkid |

---

## 分摊明细-子表 t_er_publicresharerule

- **表名称：** 分摊明细-子表
- **表名：** t_er_publicresharerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | [商机登记F7 mpm_bizopregf7](../mpm_files/mpm_bizopregf7.md) |
| 3 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | fsharecurrency | 分摊币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 8 | fsharewaitseq | 待摊行号 | int4 | 32 |  | √ | 0 | 待摊行号 |
| 9 | fshareamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |
| 10 | fentrympmtaskid | 任务号 | int8 | 64 |  |  | null | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 11 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fshareappamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 13 | fentryexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 14 | fsharewaitid | 待摊明细id | int8 | 64 |  | √ | 0 | 待摊明细id |
| 15 | fshareremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_publicresharerule_fseq |  | fid,fseq |
| 2 | pk_t_er_publicresharerule |  | fdetailid |

---

## 冲申请-子表 t_er_pubreimwrioffapply

- **表名称：** 冲申请-子表
- **表名：** t_er_pubreimwrioffapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapplyproject | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 3 | fexpenseitemfield | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 4 | forgfield | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsourceapplybilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: er_dailyapplybill :费用申请单 ocmem_marketcost_apply :营销费用申请单 |
| 6 | forgiexpebalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fapplycostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fapplybilldate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 10 | fsourcesign | 来源标识 | bpchar | 1 |  | √ | '0' | 来源标识 |
| 11 | fsourceapplybillid | 源单ID | varchar | 100 |  | √ | ' ' | 源单ID |
| 12 | fapplybillno | 申请单号 | varchar | 100 |  | √ | '0' | 申请单号 |
| 13 | fapplydescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 14 | fapplyexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 15 | fapplycostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 16 | freimbursedamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 17 | fstd_applycostcenter | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 18 | fapplyperson | 申请人 | varchar | 200 |  | √ | ' ' | 申请人 |
| 19 | fdatefield | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 20 | fexpebalanceamount | 可报销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额（本位币） |
| 21 | fapplycurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 22 | fsourceapplyentryid | 申请明细分录ID | int8 | 64 |  | √ | 0 | 申请明细分录ID |
| 23 | freimbursedcurramount | 冲销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额（本位币） |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fquotetype | 换算方式（冲申请） | bpchar | 1 |  | √ | '0' | 换算方式（冲申请）,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_pubreim_wrioffapp_fid |  | fid |
| 2 | t_er_pubreimwrioffapply_pkey |  | fentryid |

---

## 发票税务明细-子表 t_er_whinvtaxdetail

- **表名称：** 发票税务明细-子表
- **表名：** t_er_whinvtaxdetail

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
| 1 | pk_er_whinvtaxdetail |  | fwhinvdetailid |

---

## 收款信息-子表 t_er_pubreimaccinfo

- **表名称：** 收款信息-子表
- **表名：** t_er_pubreimaccinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccountcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fbuildedamount | 已出单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已出单金额 |
| 4 | fispaynow | 立即支付 | bpchar | 1 |  | √ | '0' | 立即支付 |
| 5 | foriamount | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 6 | fothercontactunit | 其他往来单位 | int8 | 64 |  | √ | 0 | [其他往来单位 cas_othercontactunit](../cas_files/cas_othercontactunit.md) |
| 7 | fpayeraccount01 | 银行账号4位 | varchar | 100 |  | √ | ' ' | 银行账号4位 |
| 8 | fpayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 cas_othercontactunit :其他往来单位 |
| 9 | fentrystatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: F :等待付款 G :已付款 I :关闭 E :审核通过 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | famount | 收款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额（本位币） |
| 12 | foriaccnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 13 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 14 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 15 | fsupplier | 收款人（供应商） | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 16 | fentryrepaydate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |
| 17 | fpayeraccountname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 18 | fpayerid | 收款人（个人） | int8 | 64 |  | √ | 0 | [收款信息 er_payeer](../em_files/er_payeer.md) |
| 19 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额（本位币） |
| 20 | fcustomer | 收款人（客户） | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 21 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 22 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 23 | foriaccpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 24 | foriaccbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额 |
| 25 | faccpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额（本位币） |
| 26 | fcasorg | 收款人（内部公司） | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | faccnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额(本位币) |
| 28 | frecsrcbillid | （核销）源单id | int8 | 64 |  | √ | 0 | （核销）源单id |
| 29 | frecsrcbillno | 源单编号 | varchar | 200 |  | √ | ' ' | 源单编号 |
| 30 | fbanklogo | 银行卡logo图标 | varchar | 50 |  | √ | ' ' | 银行卡logo图标 |
| 31 | fpayeraccount02 | 银行账号(显示_old) | varchar | 100 |  | √ | ' ' | 银行账号(显示_old) |
| 32 | fpayeraccount | 银行账号 | varchar | 100 |  | √ | ' ' | 银行账号 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 35 | frecsrcentryid | （核销）分录id | int8 | 64 |  | √ | 0 | （核销）分录id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_pubreim_accinfo_fseq |  | fid,fseq |
| 2 | t_er_pubreimaccinfo_pkey |  | fentryid |
