# 对公报销单(共享审批)-er_publicreimburse_ssc

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
| 2 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 3 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 6 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 7 | frotationangle | 旋转角度 | varchar | 30 |  |  | null | 旋转角度 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 10 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 11 | fsnapshoturl | 快照 url | varchar | 512 |  |  | null | 快照 url |
| 12 | fattachtype | 文件类型 | varchar | 30 |  |  | null | 文件类型,枚举: |

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
| 2 | ftaxrate | 平均税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 平均税率（%） |
| 3 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 4 | fuploadseq | 采集顺序 | int8 | 64 |  | √ | 0 | 采集顺序 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 7 | fisred | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票,枚举: 0 :否 1 :是 |
| 8 | fbuyeraddressphone | 地址电话 | varchar | 255 |  | √ | ' ' | 地址电话 |
| 9 | fpassengername | 旅客 | varchar | 255 |  |  | null | 旅客 |
| 10 | fenddate | 通行日期止 | timestamp | 0 |  |  | null | 通行日期止 |
| 11 | fissupplement | 后补发票 | bpchar | 1 |  | √ | '0' | 后补发票,枚举: 0 :否 1 :是 |
| 12 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 13 | ffuelsurcharge | 燃油附加费 | numeric | 23 | 10 | √ | 0 | 燃油附加费 |
| 14 | finvoicecode | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 15 | fcity | 发票所在地 | varchar | 50 |  | √ | ' ' | 发票所在地 |
| 16 | fbuyername | 收票公司 | varchar | 250 |  | √ | ' ' | 收票公司 |
| 17 | fpassverifybuyername | 发票抬头一致 | varchar | 30 |  | √ | ' ' | 发票抬头一致,枚举: 1 :是 0 :否 |
| 18 | fpassverifybuyertaxno | 发票税号一致 | varchar | 30 |  | √ | ' ' | 发票税号一致,枚举: 1 :是 0 :否 |
| 19 | finvoiceno | 发票号码 | varchar | 129 |  | √ | ' ' | 发票号码 |
| 20 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |
| 21 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 22 | freasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 23 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 24 | fseatgrade | 座位等级 | varchar | 50 |  | √ | ' ' | 座位等级,枚举: |
| 25 | foffsetamount | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 26 | fistartcity | 出发城市 | varchar | 50 |  | √ | ' ' | 出发城市 |
| 27 | finvoicecurrencyid | 发票币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 28 | fbuyerorgid | 收票公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 29 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :酒店账单 23 :通用机打电子发票 |
| 30 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 31 | ftocity | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 32 | fcustomeridnumber | 身份证 | varchar | 50 |  | √ | ' ' | 身份证 |
| 33 | fstartdate | 通行日期起 | timestamp | 0 |  |  | null | 通行日期起 |
| 34 | ffairtime | 飞机乘机时间 | varchar | 20 |  | √ | ' ' | 飞机乘机时间 |
| 35 | ftransportnote | 运输票据 | varchar | 30 |  | √ | ' ' | 运输票据,枚举: 1 :是 0 :否 |
| 36 | fsequencenum | 是否连号 | varchar | 30 |  | √ | ' ' | 是否连号,枚举: 1 :是 2 :否 |
| 37 | ffrominvoicecloud | 发票云导入 | bpchar | 1 |  | √ | '0' | 发票云导入 |
| 38 | finvaddr | 发票下载地址 | varchar | 512 |  | √ | ' ' | 发票下载地址 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | finoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 41 | fidestcity | 目的城市 | varchar | 50 |  | √ | ' ' | 目的城市 |
| 42 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 43 | fsequencenuminfo | 连号信息 | varchar | 255 |  | √ | ' ' | 连号信息 |
| 44 | fticketchanges | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :正常 2 :改签 3 :售票 4 :退票 |
| 45 | fisxbrl | 是否xbrl | bpchar | 1 |  | √ | '0' | 是否xbrl |
| 46 | finvoiceischange | 是否修改 | varchar | 30 |  | √ | ' ' | 是否修改,枚举: 1 :否 2 :是 |
| 47 | falltaxrate | 税率(%) | varchar | 100 |  | √ | ' ' | 税率(%) |
| 48 | fievalidatest | 查验状态 | bpchar | 1 |  | √ | '3' | 查验状态,枚举: 1 :通过 2 :不通过 3 :- |
| 49 | fidestprovince | 目的省份 | varchar | 50 |  | √ | ' ' | 目的省份 |
| 50 | fothertotaltaxamount | 其他税费 | numeric | 23 | 10 | √ | 0 | 其他税费 |
| 51 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 52 | finsurancepremium | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 53 | fspecmodel | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 54 | fvalidatemessage | 发票校验结果 | varchar | 255 |  | √ | ' ' | 发票校验结果 |
| 55 | fairconstfee | 机场建设费 | numeric | 23 | 10 | √ | 0 | 机场建设费 |
| 56 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 57 | finvoicealltaxcode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 58 | fislinkagedetail | 是否费用联动 | bpchar | 1 |  | √ | '0' | 是否费用联动 |
| 59 | fregion | 地域 | bpchar | 1 |  |  | null | 地域,枚举: 1 :国内 2 :国际 |
| 60 | fcount | 发票张数 | int8 | 64 |  | √ | 0 | 发票张数 |
| 61 | finvoicenotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 62 | finvoicefrom | 发票来源 | bpchar | 1 |  | √ | '1' | 发票来源,枚举: 1 :发票云 2 :OCR识别 3 :商旅月结 5 :采购商城 |
| 63 | fbillcreatetime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 64 | ffromcity | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 65 | fbuyertaxno | 收票方税号 | varchar | 50 |  | √ | ' ' | 收票方税号 |
| 66 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 67 | fmakeoutcompname | 开票公司 | varchar | 250 |  | √ | ' ' | 开票公司 |
| 68 | fflighttrainnums | 航班号/车次 | varchar | 30 |  | √ | ' ' | 航班号/车次 |
| 69 | fistartprovince | 出发省份 | varchar | 50 |  | √ | ' ' | 出发省份 |
| 70 | fismapexpense | 关联费用明细 | bpchar | 1 |  | √ | '1' | 关联费用明细,枚举: 1 :是 0 :否 |
| 71 | fpersonalinvoice | 个人发票 | varchar | 30 |  | √ | ' ' | 个人发票,枚举: 1 :是 0 :否 |
| 72 | fendorsement | 签注 | varchar | 255 |  | √ | ' ' | 签注 |
| 73 | finvoicegoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_pubreiminvoiceinfo_pkey |  | fentryid |
| 2 | idx_er_pubreim_ivcif_fseq |  | fid,fseq |
| 3 | idx_er_invoice_pub_query |  | finvoicetype,finvoicedate |
| 4 | idx_er_invoice_pub_serialno |  | fserialno |

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
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | finvoiceentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 5 | fexpenseentryid | 费用明细分录id | int8 | 64 |  | √ | 0 | 费用明细分录id |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
| 11 | fbegintime | 出发时间 | timestamp | 0 |  |  | null | 出发时间 |
| 12 | foabillnum | 申请单号 | varchar | 255 |  | √ | ' ' | 申请单号 |
| 13 | foperationtype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 7 :服务费 8 :用餐 |
| 14 | fticketprice | 票价 | numeric | 23 | 10 | √ | 0 | 票价 |
| 15 | fserver | 服务商 | varchar | 50 |  | √ | ' ' | 服务商,枚举: CHAILVYIHAO :差旅壹号 DIDI :滴滴 MEITUAN :美团 XIECHENG :携程 ZHAOSHANG :招商银行 |
| 16 | ftoplace | 目的地 | varchar | 2000 |  | √ | ' ' | 目的地 |
| 17 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 18 | forderformid | 订单表单ID | varchar | 255 |  | √ | ' ' | 订单表单ID |
| 19 | fparentordernum | 父订单号 | varchar | 255 |  | √ | ' ' | 父订单号 |
| 20 | ffuelprice | 燃油费 | numeric | 23 | 10 | √ | 0 | 燃油费 |
| 21 | fticketstatus | 订单使用状态（机票） | varchar | 50 |  | √ | ' ' | 订单使用状态（机票）,枚举: USED :已使用 UNUSED :未使用 REFOUND :已退票 CHANGED :已改签 |
| 22 | fordercostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | forderbookeddept | 申请人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 25 | fordercompany | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | fticketpricedeductibletax | 票价可抵扣税额 | numeric | 23 | 10 | √ | 0 | 票价可抵扣税额 |
| 27 | fordernumber | 订单号 | varchar | 255 |  | √ | ' ' | 订单号 |
| 28 | fordexpenseentryid | 关联费用明细id | int8 | 64 |  | √ | 0 | 关联费用明细id |
| 29 | fordercurrency | 订单币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 30 | fservicefeedeductibletax | 服务费可抵扣税额 | numeric | 23 | 10 | √ | 0 | 服务费可抵扣税额 |
| 31 | fordercostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fairportprice | 机场建设费及其他/税费 | numeric | 23 | 10 | √ | 0 | 机场建设费及其他/税费 |
| 34 | fassuranceamount | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 35 | fendtime | 到达时间 | timestamp | 0 |  |  | null | 到达时间 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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
| 3 | fcontractapplier | 经办人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | foricontractnonpayamount | 在途金额(原币) | numeric | 23 | 10 | √ | 0 | 在途金额(原币) |
| 5 | fcontractcurrreimamount | 付款金额（本位币） | numeric | 23 | 10 | √ | 0 | 付款金额（本位币） |
| 6 | fsourceentryid | fsourceentryid | int8 | 64 |  | √ | 0 |  |
| 7 | foricontractnotpayamount | 未付金额（原币） | numeric | 23 | 10 | √ | 0 | 未付金额（原币） |
| 8 | fsigndate | 签订日期 | timestamp | 0 |  |  | null | 签订日期 |
| 9 | fcontractproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fcontractexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 12 | fcontractpartatypenew | 甲方类型 | varchar | 50 |  | √ | ' ' | 甲方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司(行政组织) bos_org :公司 |
| 13 | fcontractdescription | 合同说明 | varchar | 1000 |  | √ | ' ' | 合同说明 |
| 14 | fcontractexpquotetype | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 15 | fcontractcanamount | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 16 | fcontractsrcentryid | 关联合同分录id | int8 | 64 |  | √ | 0 | 关联合同分录id |
| 17 | fcontractpaytypeid | 付款类型 | int8 | 64 |  | √ | 0 | 付款用途 cas_paymentbilltype |
| 18 | fcontractpartbtype | 乙方类型 | varchar | 50 |  | √ | ' ' | 乙方类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_adminorg :公司(行政组织) bos_org :公司 |
| 19 | fentryprepayedamount | 已预付金额 | numeric | 23 | 10 | √ | 0 | 已预付金额 |
| 20 | fcontractsid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 21 | fcontractpartanew | 甲方 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 22 | fentryinvoiceamount | 到票金额 | numeric | 23 | 10 | √ | 0 | 到票金额 |
| 23 | fentrycurrprepayedamount | 已预付金额（本位币） | numeric | 23 | 10 | √ | 0 | 已预付金额（本位币） |
| 24 | fcontractentrycurrency | 关联合同币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | fcontractnotpayamount | 未付金额（本位币） | numeric | 23 | 10 | √ | 0 | 未付金额（本位币） |
| 26 | fcontractcostorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 27 | fcontractname | 合同名称 | varchar | 500 |  | √ | ' ' | 合同名称 |
| 28 | fcontracthappendate | 预计付款日期 | timestamp | 0 |  |  | null | 预计付款日期 |
| 29 | fcontractwriteoff | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 30 | fcontractpartb | 乙方 | varchar | 100 |  | √ | ' ' | 供应商 bd_supplier |
| 31 | fcontractnonpayamount | 在途金额 | numeric | 23 | 10 | √ | 0 | 在途金额 |
| 32 | fcontractparta | 甲方(old) | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 34 | fcontractentrychangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 35 | fcontractcurrcanamount | 可报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 可报销金额(本位币) |
| 36 | fcontractcurrwriteoff | 冲销金额（本位币） | numeric | 23 | 10 | √ | 0 | 冲销金额（本位币） |
| 37 | fcontractreimamount | 付款金额 | numeric | 23 | 10 | √ | 0 | 付款金额 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

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

## 对公报销单(共享审批)-主表 t_er_pubreimbill

- **表名称：** 对公报销单(共享审批)-主表
- **表名：** t_er_pubreimbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fautogenshare | 自动生成分摊单 | bpchar | 1 |  | √ | '0' | 自动生成分摊单 |
| 4 | fpaycompanyid | 支付公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | finvokeinvoicecloud | 是否与发票云交互 | bpchar | 1 |  | √ | '0' | 是否与发票云交互 |
| 6 | fassetorgid | 资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fnoinvoice | 无票 | bpchar | 1 |  | √ | '0' | 无票 |
| 8 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fbillpayertype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 11 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 12 | fisbeforeshare | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 13 | fhead_paydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 14 | fmonthrulestartdate | 开始月份 | timestamp | 0 |  |  | null | 开始月份 |
| 15 | fisonaccount | 是否挂账 | bpchar | 1 |  | √ | '0' | 是否挂账 |
| 16 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 17 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 18 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 19 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 20 | fapplierpositionstr | fapplierpositionstr | varchar | 100 |  | √ | ' ' |  |
| 21 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 22 | fisonway | 是否支持在途 | bpchar | 1 |  | √ | '0' | 是否支持在途 |
| 23 | fisover | 是否超标（提交后有值） | bpchar | 1 |  | √ | '0' | 是否超标（提交后有值） |
| 24 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 25 | foffsetinvoiceno | 可抵扣发票号码 | varchar | 255 |  | √ | ' ' | 可抵扣发票号码 |
| 26 | fstdbilltype | fstdbilltype | varchar | 30 |  | √ | ' ' |  |
| 27 | fsourcebilltype | 源单类型(已废弃) | varchar | 30 |  | √ | ' ' | 源单类型(已废弃) |
| 28 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 29 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 30 | fmonthsettleamount | 月结金额 | numeric | 23 | 10 | √ | 0 | 月结金额 |
| 31 | finvoiceoffsetamount | 抵扣税额（发票信息） | numeric | 23 | 10 | √ | 0 | 抵扣税额（发票信息） |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 34 | fautomapinvoice | 智能发票报销 | bpchar | 1 |  | √ | '1' | 智能发票报销 |
| 35 | foffsetamount | foffsetamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 36 | fimagenumber | 影像编号 | varchar | 255 |  | √ | ' ' | 影像编号 |
| 37 | fsharerule | 分摊规则 | varchar | 30 |  | √ | ' ' | 分摊规则,枚举: orgrule :按部门分摊 monthrule :按月分摊 yearrule :按年分摊 expenseitemrule :按费用项目分摊 |
| 38 | fassettype | 资产类型 | varchar | 20 |  | √ | ' ' | 资产类型,枚举: newasset :新增资产 existasset :已有资产 |
| 39 | frameworkcontract | 框架合同 | bpchar | 1 |  | √ | '0' | 框架合同 |
| 40 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 41 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 42 | fpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 43 | fnextauditor | 下一步审核人 | varchar | 100 |  | √ | ' ' | 下一步审核人 |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fneedimagescan | 需要影像扫描 | bpchar | 1 |  | √ | ' ' | 需要影像扫描,枚举: 1 :是 2 :否 |
| 46 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 47 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 48 | fcontractsconn | 关联合同 | varchar | 1000 |  | √ | ' ' | 关联合同 |
| 49 | ftel | 联系方式 | varchar | 100 |  | √ | ' ' | 联系方式 |
| 50 | fisshared | 是否已分摊 | bpchar | 1 |  | √ | '0' | 是否已分摊 |
| 51 | fbillpayerid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 52 | fredoffsetdes | 红冲说明 | varchar | 1000 |  | √ | ' ' | 红冲说明 |
| 53 | fpayamount | 付现 | numeric | 23 | 10 | √ | 0.0000000000 | 付现 |
| 54 | fprojectsharecount | 下游项目成本分摊单数 | int8 | 64 |  | √ | 0 | 下游项目成本分摊单数 |
| 55 | fabovequota | 是否超额 | bpchar | 1 |  | √ | '0' | 是否超额,枚举: 1 :超额 2 :未超额 0 :- |
| 56 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 57 | fneedsuppleinvoice | 发票后补 | bpchar | 1 |  | √ | '0' | 发票后补 |
| 58 | fsharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额 |
| 59 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 60 | fispush | 是否合同下推生成 | varchar | 255 |  | √ | ' ' | 是否合同下推生成 |
| 61 | fstdreimbursetype | 关联业务 | varchar | 30 |  | √ | ' ' | 关联业务,枚举: biztype_contract :合同 biztype_other :其他 |
| 62 | fpaycurrency | 付现金额币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 63 | fisredoffset | 红冲 | bpchar | 1 |  | √ | '0' | 红冲 |
| 64 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_tripreqbill :出差申请单 er_loanbill :出差借款单 er_tripreimbursebill :差旅费报销单 er_dailyapplybill :费用申请单 er_dailyloanbill :借款单 er_dailyreimbursebill :费用报销单 er_repaymentbill :还款单 er_publicreimbursebill :对公报销单 |
| 65 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 66 | fis_all_einvoice | 发票状态 | bpchar | 1 |  | √ | '0' | 发票状态,枚举: 0 :无发票 1 :全电票 2 :含纸票 3 :其它 |
| 67 | fonaccountamount | 挂账金额 | numeric | 23 | 10 | √ | 0 | 挂账金额 |
| 68 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 69 | fproxytax | 代扣代缴 | bpchar | 1 |  | √ | '0' | 代扣代缴 |
| 70 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 71 | freimbursetype | 报账类型 | varchar | 30 |  | √ | ' ' | 报账类型,枚举: asset :资产报账 expense :费用报账 entertainment :招待费 meetting :会议费 otherexpenses :其他 |
| 72 | fisinvoicemodified | 发票修改 | bpchar | 1 |  | √ | '0' | 发票修改 |
| 73 | fauditopinion | 审核意见 | varchar | 100 |  | √ | ' ' | 审核意见 |
| 74 | fmonthruleenddate | 结束月份 | timestamp | 0 |  |  | null | 结束月份 |
| 75 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 76 | fispaybyhead | 按单头付款 | bpchar | 1 |  | √ | '0' | 按单头付款 |
| 77 | fsharemethod | 分摊方法 | varchar | 30 |  | √ | ' ' | 分摊方法,枚举: rate :比例分摊 avg :金额平均 amount :金额分摊 |
| 78 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 79 | ftotalaccloanamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 80 | ftarbillstatus | 目标单据 | varchar | 30 |  | √ | ' ' | 目标单据,枚举: A1 :采购转固单(保存) A2 :采购转固单(已审) B1 :项目成本分摊单 C1 :工程转固单 |
| 81 | freimbursecurrency | 报销金额币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 82 | fiscrepayablebill | 生成应付单 | bpchar | 1 |  | √ | '0' | 生成应付单,枚举: 0 :否 1 :是 |
| 83 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | 业务分类 er_projecttype |
| 84 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 85 | fisneedinstall | 需安装 | bpchar | 1 |  | √ | '0' | 需安装 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_pubreim_fapplierid |  | fapplierid |
| 2 | idx_er_pubreim_fbizdate_bno |  | fbizdate,fbillno |
| 3 | t_er_pubreimbill_pkey |  | fid |
| 4 | idx_er_pubreim_fbillstatus |  | fbillstatus |
| 5 | idx_er_pubreim_fcompanyid |  | fcompanyid |
| 6 | idx_er_pubreim_fcreatorid |  | fcreatorid |

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
| 1 | idx_er_pubreimexpdet_lk_fid |  | fentryid |
| 2 | pk_t_er_pubreimexpdet_lk |  | fpkid |

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
| 2 | ftreatway | 招待方式 | varchar | 10 |  | √ | ' ' | 招待方式,枚举: 1 :餐费 2 :酒店住宿 3 :酒水 4 :纪念品 |
| 3 | fgoodsnum | 酒水瓶数 | int4 | 32 |  | √ | 0 | 酒水瓶数 |
| 4 | fotherstandarddesc | 酒水标准 | varchar | 255 |  | √ | ' ' | 酒水标准 |
| 5 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 6 | fotherfeeamount | 酒水金额 | numeric | 23 | 10 | √ | 0 | 酒水金额 |
| 7 | fmeetlevel | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |
| 8 | fcityarea | 城市类别 | int8 | 64 |  | √ | 0 | 出差地域 er_triparea |
| 9 | fisover | 超费用标准 | bpchar | 1 |  | √ | '0' | 超费用标准 |
| 10 | fotherstandamount | 酒水标准金额(页面不可见) | numeric | 23 | 10 | √ | 0 | 酒水标准金额(页面不可见) |
| 11 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 12 | ftripbookamount | 商旅预定金额 | numeric | 23 | 10 | √ | 0 | 商旅预定金额 |
| 13 | fescortnum | 陪同人数 | int4 | 32 |  | √ | 0 | 陪同人数 |
| 14 | foverdesc | 超标说明(暂未支持) | varchar | 255 |  | √ | ' ' | 超标说明(暂未支持) |
| 15 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | 报销级别 er_reimburselevel |
| 16 | fisexistmonthly | 是否关联商旅订单 | bpchar | 1 |  | √ | '0' | 是否关联商旅订单 |
| 17 | ftripbookcuramount | 商旅预定金额（本位币） | numeric | 23 | 10 | √ | 0 | 商旅预定金额（本位币） |
| 18 | fdaysnum | 住宿天数 | int4 | 32 |  | √ | 0 | 住宿天数 |
| 19 | fmeetitem | 会议事项 | varchar | 10 |  | √ | ' ' | 会议事项,枚举: 1 :伙食费 2 :酒店住宿 3 :交通费 4 :其他 |
| 20 | ftreatnum | 招待人数 | int4 | 32 |  | √ | 0 | 招待人数 |
| 21 | fcontrolamt | 可报销金额 | numeric | 23 | 10 | √ | 0 | 可报销金额 |
| 22 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 23 | ffeestandid | 费用标准基础资料 | int8 | 64 |  | √ | 0 | 费用标准 er_standard |
| 24 | fexpisredoffset | 红冲(明细) | bpchar | 1 |  | √ | '0' | 红冲(明细) |
| 25 | ffeestandardamt | 费用标准金额(页面不可见) | numeric | 23 | 10 | √ | 0 | 费用标准金额(页面不可见) |
| 26 | ffeestandarddesc | 费用标准 | varchar | 255 |  | √ | ' ' | 费用标准 |

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
| 5 | floanbillnov1 | 单据编码 | varchar | 100 |  | √ | '0' | 单据编码 |
| 6 | fsourceentryid | 借款明细分录ID | int8 | 64 |  | √ | 0 | 借款明细分录ID |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcurrloanamount | 借款余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额（本位币） |
| 9 | floanprojectno | 立项号 | varchar | 200 |  | √ | ' ' | 立项号 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fsrcofsrcentryid | 冲借款源分录id | int8 | 64 |  | √ | 0 | 冲借款源分录id |
| 12 | floanapplydatev1 | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 13 | fsourcesign | 是否关联申请 | bpchar | 1 |  | √ | '0' | 是否关联申请 |
| 14 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 16 | faccloanamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 17 | fcurraccloanamount | 冲销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额(本位币) |
| 18 | floanamount | 借款余额 | numeric | 23 | 10 | √ | 0.0000000000 | 借款余额 |
| 19 | floanexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 20 | floancurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 21 | fsourcebillid | 源单id | varchar | 100 |  | √ | ' ' | 源单id |
| 22 | fsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型,枚举: er_dailyloanbill :借款单 er_tripreqbill :出差借款单 er_prepaybill :预付单 |
| 23 | floandescriptionv1 | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fquotetype | 换算方式（冲借款） | bpchar | 1 |  | √ | '0' | 换算方式（冲借款）,枚举: 0 :直接汇率 1 :间接汇率 |
| 26 | fsourceexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 27 | fentrywltype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 28 | floancontractno | 合同号 | varchar | 500 |  | √ | ' ' | 合同号 |

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
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | fexcludeamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | finvoiceitemoffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fitementryid | 费用项目分录id | int8 | 64 |  | √ | 0 | 费用项目分录id |
| 8 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 9 | finvoiceheadentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 10 | funitprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 11 | fgoodscode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 12 | fspecmodel | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 13 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 14 | finvoicecloudoffset | 发票抵扣 | bpchar | 1 |  | √ | '1' | 发票抵扣 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 16 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 17 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |

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
| 4 | fwhentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fwhbillpayertype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 7 | forgiwhbalanceamount | 冲销余额 | numeric | 23 | 10 | √ | 0 | 冲销余额 |
| 8 | fwhcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 9 | fwhbalanceamount | 冲销余额(本位币) | numeric | 23 | 10 | √ | 0 | 冲销余额(本位币) |
| 10 | fwithholdingbillno | 预提单号 | varchar | 100 |  | √ | '0' | 预提单号 |
| 11 | fwhpayername | 申请人 | varchar | 200 |  | √ | ' ' | 申请人 |
| 12 | fwhsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型 |
| 13 | fwhbillpayerid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 14 | fwhentrycostcompanyid | 分录费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fwhcostcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fwhbursedcurramount | 冲销金额(本位币) | numeric | 23 | 10 | √ | 0 | 冲销金额(本位币) |
| 17 | fwhbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 18 | fwithholdingtype | 预提类型 | int8 | 64 |  | √ | 0 | 预提类型 er_withholdingtype |
| 19 | fwhsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 20 | fwhentrycostdeptid | 分录费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fwhsourceentryid | 源单分录ID | int8 | 64 |  | √ | 0 | 源单分录ID |
| 22 | fwhbursedamount | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fwhexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 25 | fsourcewhitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |

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
| 2 | fassetsrcbillno | 源单编码 | varchar | 200 |  | √ | ' ' | 源单编码 |
| 3 | fhappendate | 资产发生日期 | timestamp | 0 |  |  | null | 资产发生日期 |
| 4 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fmobiledeldoneflag | 移动端删除完成标志 | int4 | 32 |  | √ | 0 | 移动端删除完成标志 |
| 6 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0 | 税率（%） |
| 7 | fassetstoreplace | 存放地点 | int8 | 64 |  | √ | 0 | 存放地点 fa_storeplace |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fassetcat | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 10 | fcurrexpenseamount | 含税金额(本位币) | numeric | 23 | 10 | √ | 0 | 含税金额(本位币) |
| 11 | fassetmodel | 规格型号 | varchar | 200 |  | √ | ' ' | 规格型号 |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 1 | 汇率 |
| 13 | fsubjectmatter | 标的物 | varchar | 150 |  | √ | ' ' | 标的物 |
| 14 | fexpquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 15 | fassetbillno | 资产编码 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fassetcostdeptid | 使用部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 18 | fassetsrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 19 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 20 | forientryamount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 21 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 22 | fassetname | 资产名称 | varchar | 200 |  | √ | ' ' | 资产名称 |
| 23 | fassetquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 24 | fpricewithouttax | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 25 | fassetentryid | 分录id | int8 | 64 |  | √ | 0 | 分录id |
| 26 | fassetuserid | 使用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fexpenseamount | 含税金额 | numeric | 23 | 10 | √ | 0 | 含税金额 |
| 28 | fis_special_invoice | 专票 | bpchar | 1 |  | √ | '0' | 专票 |
| 29 | fassetunit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
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

## 对公报销单(共享审批)-分表 t_er_pubreimbill_a

- **表名称：** 对公报销单(共享审批)-分表
- **表名：** t_er_pubreimbill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizitem | 业务事项 | int8 | 64 |  | √ | 0 | 业务事项 er_standard_type |
| 3 | freimburselevel | 报销级别 | int8 | 64 |  | √ | 0 | 报销级别 er_reimburselevel |
| 4 | fmeetlevel | fmeetlevel | varchar | 10 |  | √ | ' ' |  |
| 5 | fcityarea | 城市类别 | int8 | 64 |  | √ | 0 | 出差地域 er_triparea |
| 6 | fdaysnum | 住宿天数 | int4 | 32 |  | √ | 0 | 住宿天数 |
| 7 | fmeettype | 会议类别 | varchar | 10 |  | √ | ' ' | 会议类别,枚举: 1 :国内会议 2 :国际会议 3 :其他会议 |
| 8 | ftreatnum | 招待人数 | int4 | 32 |  | √ | 0 | 招待人数 |
| 9 | fescortnum | 陪同人数 | int4 | 32 |  | √ | 0 | 陪同人数 |
| 10 | ftreattype | 招待类型 | varchar | 10 |  | √ | ' ' | 招待类型,枚举: 1 :商务招待 2 :公务招待 3 :外事招待 |
| 11 | fmeetgrade | 会议级别 | varchar | 10 |  | √ | ' ' | 会议级别,枚举: 1 :普通 2 :重要 |

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
| 3 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 5 | fsdentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 6 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 7 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 10 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '1' | 是否抵扣 |
| 11 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 12 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 13 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 15 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
| 16 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | '1' | 专票 |
| 17 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 18 | fcurprice | 核定不含税金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额本位币 |
| 19 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | '0' | 发票类型,枚举: 0 :空 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 |
| 20 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 21 | ftaxclasscodeid | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 22 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 23 | fsharerate | 分摊比例（%） | numeric | 23 | 10 | √ | 0.0000000000 | 分摊比例（%） |
| 24 | fitemfrom | 来源 | varchar | 2 |  | √ | '0' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 4 :分录导入 |
| 25 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 26 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 27 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 28 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 29 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 30 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 31 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 32 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 33 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 34 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 35 | flkwaitentryid | 待摊明细id | varchar | 200 |  | √ | ' ' | 待摊明细id |
| 36 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 37 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 38 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 40 | fsdentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |

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

## 对公报销单(共享审批)-多语言表 t_er_pubreimbill_l

- **表名称：** 对公报销单(共享审批)-多语言表
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

## 对公报销单(共享审批)-反写记录表 t_er_pubreimbill_wb

- **表名称：** 对公报销单(共享审批)-反写记录表
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

## 对公报销单(共享审批)-关联追踪表 t_er_pubreimbill_tc

- **表名称：** 对公报销单(共享审批)-关联追踪表
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
| 2 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 3 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 4 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 5 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 6 | fwbcurrency | 核销币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 8 | fwbamount | 核销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核销金额 |
| 9 | fiscreateprojectcostshare | 生成项目分摊单 | int8 | 64 |  | √ | 0 | 生成项目分摊单 |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | fiscreateappaycount | 生成应付次数 | int4 | 32 |  | √ | 0 | 生成应付次数 |
| 12 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '1' | 是否抵扣 |
| 13 | ffentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 14 | fproxyamt | 代扣代缴个税 | numeric | 23 | 10 | √ | 0.0000000000 | 代扣代缴个税 |
| 15 | fentrycontractname | 合同名称 | varchar | 500 |  |  | ' ' | 合同名称 |
| 16 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 17 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 18 | fwbsrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: contract :合同单 project :立项单 estimate :费用暂估单 er_vehiclecheckingbill :用车结算单 pur_receipt :商城验收单 er_mealcheckingbill :用餐结算单 |
| 19 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额(本位币) |
| 20 | fsubjectmatter | 标的物 | varchar | 150 |  | √ | ' ' | 标的物 |
| 21 | fisspecialinvoice | 专票 | bpchar | 1 |  | √ | '1' | 专票 |
| 22 | fcurprice | 核定金额不含税金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额不含税金额（本位币） |
| 23 | finvoicetypeitem | 发票类型 | varchar | 50 |  | √ | '0' | 发票类型,枚举: 0 :空 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :酒店账单 |
| 24 | finvoicefromparent | 发票来源父节点 | bpchar | 1 |  | √ | '0' | 发票来源父节点 |
| 25 | fwbsrcentryid | （核销）分录id | int8 | 64 |  | √ | 0 | （核销）分录id |
| 26 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 27 | ftaxclasscodeid | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 28 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 29 | fexpnonpayamount | 在途金额 | numeric | 23 | 10 | √ | 0 | 在途金额 |
| 30 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 31 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 32 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 33 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 34 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 35 | fwbexchangrate | 核销汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 核销汇率 |
| 36 | fassetquantity | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 37 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 38 | fentryproducttype | 产品类别 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 39 | fentrysubprojectno | fentrysubprojectno | varchar | 200 |  | √ | ' ' |  |
| 40 | fwbsrcbillno | 源单编码 | varchar | 200 |  | √ | ' ' | 源单编码 |
| 41 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额（本位币） |
| 42 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 43 | fcurproxyamt | 代扣代缴个税(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 代扣代缴个税(本位币) |
| 44 | fexporiwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额 |
| 45 | fentryprojectno | 立项号 | varchar | 200 |  | √ | ' ' | 立项号 |
| 46 | fassetnumber | 资产编码 | varchar | 100 |  | √ | ' ' | 资产编码 |
| 47 | fwbsrcbillid | （核销）源单id | int8 | 64 |  | √ | 0 | （核销）源单id |
| 48 | fsplitparent | 拆分父分录 | varchar | 32 |  | √ | ' ' | 拆分父分录 |
| 49 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 50 | fassetstoreplace | 存放地点 | int8 | 64 |  | √ | 0 | 存放地点 fa_storeplace |
| 51 | fassetcat | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 52 | fexpentrystatus | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: F :等待付款 G :已付款 I :关闭 E :审核通过 |
| 53 | fassetmodel | 规格型号 | varchar | 200 |  | √ | ' ' | 规格型号 |
| 54 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定不含税金额 |
| 55 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 56 | fwbcuramount | 核销金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 核销金额本位币 |
| 57 | fissettle | 结算状态 | bpchar | 30 |  | √ | ' ' | 结算状态,枚举: unsettle :未结算 partsettle :部分结算 settled :全部结算 |
| 58 | fsharedamount | 已分摊金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额（本位币） |
| 59 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 60 | fpricewithtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 61 | fexpwithholdingamount | 已预提金额本位币 | numeric | 23 | 10 | √ | 0.0000000000 | 已预提金额本位币 |
| 62 | fassetbillno | 卡片编码 | int8 | 64 |  | √ | 0 | 资产卡片基础资料 fa_card_real_base |
| 63 | fcontractitemid | 合同付款条目id | int8 | 64 |  | √ | 0 | 合同付款条目id |
| 64 | fentrycontractno | 合同号 | varchar | 500 |  | √ | ' ' | 合同号 |
| 65 | fitemfrom | 来源 | bpchar | 1 |  | √ | '0' | 来源,枚举: 0 :手动添加 1 :发票云 2 :OCR识别 3 :商旅 4 :分录导入 5 :采购商城 |
| 66 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 67 | fiscrepayableentry | 生成应付单 | bpchar | 1 |  | √ | '0' | 生成应付单,枚举: 0 :否 1 :是 |
| 68 | fassetname | 资产名称 | varchar | 200 |  | √ | ' ' | 资产名称 |
| 69 | fitemreasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 70 | fexpebalanceamount | fexpebalanceamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 71 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 72 | fwbpaytype | 付款类型 | varchar | 80 |  | √ | ' ' | 付款类型,枚举: PREPAYMENT :预付款 PROGRESSPAYMENT :进度款 SETTLEPAYMENT :结算款 BOND :保证金 REWORDORPUNISH :奖惩 OTHERS :其它 |
| 73 | freimctldeptid | 额度控制部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 74 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 75 | fassetunit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 76 | forisharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已分摊金额 |
| 77 | fwbquotetype | 核销换算方式 | bpchar | 1 |  | √ | '0' | 核销换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 78 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0.0000000000 | 核定金额 |
| 79 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 80 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_pubreim_expdet_fseq |  | fid,fseq |
| 2 | t_er_pubreimexpdet_pkey |  | fdetailid |

---

## 付款信息-子表 t_er_publicreimpayentry

- **表名称：** 付款信息-子表
- **表名：** t_er_publicreimpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftargetpayorg | 付款人 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftargetbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 4 | ftargetbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 5 | fdpcurrency | 付款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | ffee | 手续费 | numeric | 23 | 10 | √ | 0.0000000000 | 手续费 |
| 8 | ftargetentrustorg | 委托付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fdpexchangerate | 付款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 付款汇率 |
| 10 | flossamt | 汇兑损益 | numeric | 23 | 10 | √ | 0.0000000000 | 汇兑损益 |
| 11 | fdpamt | 付款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额 |
| 12 | fagreedrate | 兑换汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 兑换汇率 |
| 13 | ftargetlocalamount | 收款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额(本位币) |
| 14 | ftargetpayacctid | 付款账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 15 | ftargetexchange | 收款汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 收款汇率 |
| 16 | ftargetpaybank | 付款银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 17 | ffeecurrency | 手续费币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fdplocalamt | 付款金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 付款金额(本位币) |
| 19 | ftargetpayamt | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 20 | ftargetpayacct | 付款账号（文本） | varchar | 50 |  | √ | ' ' | 付款账号（文本） |
| 21 | ftargetopenorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | ftargetbillid | 目标单据id | int8 | 64 |  | √ | 0 | 目标单据id |
| 23 | ftargetpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 24 | ftargetcurrency | 收款币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 25 | ftargetsettletype | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_prpe_feq |  | fid,fseq |
| 2 | t_er_publicreimpayentry_pkey |  | fentryid |
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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
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
| 2 | fentrympmbizopregid | 商机号 | int8 | 64 |  |  | null | 商机登记F7 mpm_bizopregf7 |
| 3 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 5 | fsharecurrency | 分摊币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentrymonth | 月份 | timestamp | 0 |  |  | null | 月份 |
| 8 | fsharewaitseq | 待摊行号 | int4 | 32 |  | √ | 0 | 待摊行号 |
| 9 | fshareamount | 分摊金额 | numeric | 23 | 10 | √ | 0 | 分摊金额 |
| 10 | fentrympmtaskid | 任务号 | int8 | 64 |  |  | null | 项目任务F7 mpm_task_f7 |
| 11 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fshareappamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 13 | fentryexpenseitem | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 14 | fsharewaitid | 待摊明细id | int8 | 64 |  | √ | 0 | 待摊明细id |
| 15 | fshareremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 17 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
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
| 2 | fapplyproject | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 3 | fexpenseitemfield | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 4 | forgfield | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fapplycostcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | forgiexpebalanceamount | 可报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额 |
| 7 | freimbursedamount | 冲销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fstd_applycostcenter | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 10 | fapplyperson | 申请人 | varchar | 200 |  | √ | ' ' | 申请人 |
| 11 | fdatefield | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 12 | fapplycostdept | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fexpebalanceamount | 可报销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可报销金额（本位币） |
| 14 | fapplybilldate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 15 | fapplycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 16 | fsourcesign | 来源标识 | bpchar | 1 |  | √ | '0' | 来源标识 |
| 17 | fsourceapplybillid | 源单ID | varchar | 100 |  | √ | ' ' | 源单ID |
| 18 | fapplybillno | 申请单号 | varchar | 100 |  | √ | '0' | 申请单号 |
| 19 | fsourceapplyentryid | 申请明细分录ID | int8 | 64 |  | √ | 0 | 申请明细分录ID |
| 20 | fapplydescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 21 | freimbursedcurramount | 冲销金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 冲销金额（本位币） |
| 22 | fapplyexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fquotetype | 换算方式（冲申请） | bpchar | 1 |  | √ | '0' | 换算方式（冲申请）,枚举: 0 :直接汇率 1 :间接汇率 |

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

## 收款信息-子表 t_er_pubreimaccinfo

- **表名称：** 收款信息-子表
- **表名：** t_er_pubreimaccinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccountcurrency | 币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fbuildedamount | 已出单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已出单金额 |
| 4 | fispaynow | 立即支付 | bpchar | 1 |  | √ | '0' | 立即支付 |
| 5 | foriamount | 收款金额 | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额 |
| 6 | fpayeraccount01 | 银行账号4位 | varchar | 100 |  | √ | ' ' | 银行账号4位 |
| 7 | fpayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 |
| 8 | fentrystatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: F :等待付款 G :已付款 I :关闭 E :审核通过 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | famount | 收款金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 收款金额（本位币） |
| 11 | foriaccnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额 |
| 12 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 13 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 14 | fsupplier | 收款人（供应商） | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 15 | fentryrepaydate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |
| 16 | fpayeraccountname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 17 | fpayerid | 收款人（个人） | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 18 | faccbalanceamount | 可用余额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额（本位币） |
| 19 | fcustomer | 收款人（客户） | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 20 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 21 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 22 | foriaccpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额 |
| 23 | foriaccbalanceamount | 可用余额 | numeric | 23 | 10 | √ | 0.0000000000 | 可用余额 |
| 24 | faccpayedamount | 已付金额（本位币） | numeric | 23 | 10 | √ | 0.0000000000 | 已付金额（本位币） |
| 25 | fcasorg | 收款人（内部公司） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 26 | faccnotpayamount | 未付金额(本位币) | numeric | 23 | 10 | √ | 0.0000000000 | 未付金额(本位币) |
| 27 | frecsrcbillid | （核销）源单id | int8 | 64 |  | √ | 0 | （核销）源单id |
| 28 | frecsrcbillno | 源单编码 | varchar | 200 |  | √ | ' ' | 源单编码 |
| 29 | fbanklogo | 银行卡logo图标 | varchar | 50 |  | √ | ' ' | 银行卡logo图标 |
| 30 | fpayeraccount02 | 银行账号(显示_old) | varchar | 100 |  | √ | ' ' | 银行账号(显示_old) |
| 31 | fpayeraccount | 银行账号 | varchar | 100 |  | √ | ' ' | 银行账号 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 34 | frecsrcentryid | （核销）分录id | int8 | 64 |  | √ | 0 | （核销）分录id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_pubreim_accinfo_fseq |  | fid,fseq |
| 2 | t_er_pubreimaccinfo_pkey |  | fentryid |
