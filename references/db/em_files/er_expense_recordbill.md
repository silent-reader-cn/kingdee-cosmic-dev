# 记费用-er_expense_recordbill

## 发票信息-子表 t_er_invoicepoolinfo

- **表名称：** 发票信息-子表
- **表名：** t_er_invoicepoolinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmapexpenseinfo | fmapexpenseinfo | varchar | 255 |  |  | ' ' |  |
| 3 | ftaxrate | 平均税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 平均税率（%） |
| 4 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 5 | fuploadseq | 采集顺序 | int8 | 64 |  | √ | 0 | 采集顺序 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 8 | fisred | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票,枚举: 0 :否 1 :是 |
| 9 | fpassengername | 旅客 | varchar | 255 |  |  | null | 旅客 |
| 10 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 11 | finvoicecode | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 12 | fbuyername | 收票公司 | varchar | 250 |  | √ | ' ' | 收票公司 |
| 13 | fpassverifybuyername | 发票抬头一致 | varchar | 30 |  | √ | ' ' | 发票抬头一致,枚举: 1 :是 0 :否 |
| 14 | fpassverifybuyertaxno | 发票税号一致 | varchar | 30 |  | √ | ' ' | 发票税号一致,枚举: 1 :是 0 :否 |
| 15 | finvoiceno | 发票号码 | varchar | 129 |  | √ | ' ' | 发票号码 |
| 16 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |
| 17 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 18 | freasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 19 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 20 | fseatgrade | 座位等级 | varchar | 50 |  | √ | ' ' | 座位等级,枚举: |
| 21 | foffsetamount | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 22 | fistartcity | 出发城市 | varchar | 50 |  | √ | ' ' | 出发城市 |
| 23 | finvoicecurrencyid | 发票币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 24 | fbuyerorgid | 收票公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :酒店账单 23 :通用机打电子发票 |
| 26 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 27 | ftocity | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 28 | fcustomeridnumber | 身份证 | varchar | 50 |  | √ | ' ' | 身份证 |
| 29 | ftransportnote | 运输票据 | varchar | 30 |  | √ | ' ' | 运输票据,枚举: 1 :是 0 :否 |
| 30 | fsequencenum | 是否连号 | varchar | 30 |  | √ | ' ' | 是否连号,枚举: 1 :是 2 :否 |
| 31 | ffrominvoicecloud | 发票云导入 | bpchar | 1 |  | √ | '0' | 发票云导入 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | finoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 34 | fidestcity | 目的城市 | varchar | 50 |  | √ | ' ' | 目的城市 |
| 35 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 36 | fsequencenuminfo | 连号信息 | varchar | 255 |  | √ | ' ' | 连号信息 |
| 37 | fticketchanges | 机票状态 | varchar | 30 |  | √ | ' ' | 机票状态,枚举: 1 :正常 2 :改签 |
| 38 | finvoiceischange | 是否修改 | varchar | 30 |  | √ | ' ' | 是否修改,枚举: 1 :否 2 :是 |
| 39 | falltaxrate | 税率(%) | varchar | 100 |  | √ | ' ' | 税率(%) |
| 40 | fievalidatest | 查验状态 | bpchar | 1 |  | √ | '3' | 查验状态,枚举: 1 :通过 2 :不通过 3 :- |
| 41 | fidestprovince | 目的省份 | varchar | 50 |  | √ | ' ' | 目的省份 |
| 42 | fothertotaltaxamount | 其他税费 | numeric | 23 | 10 | √ | 0 | 其他税费 |
| 43 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 44 | finsurancepremium | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 45 | fspecmodel | 规格型号 | varchar | 50 |  | √ | ' ' | 规格型号 |
| 46 | fvalidatemessage | 发票校验结果 | varchar | 255 |  | √ | ' ' | 发票校验结果 |
| 47 | fairconstfee | 机场建设费 | numeric | 23 | 10 | √ | 0 | 机场建设费 |
| 48 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 49 | finvoicealltaxcode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 50 | fregion | 地域 | bpchar | 1 |  |  | null | 地域,枚举: 1 :国内 2 :国际 |
| 51 | fcount | 发票张数 | int4 | 32 |  | √ | 0 | 发票张数 |
| 52 | finvoicenotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 53 | finvoicefrom | 发票来源 | varchar | 30 |  | √ | '1' | 发票来源,枚举: 1 :发票云 2 :OCR识别 3 :商旅月结 |
| 54 | fbillcreatetime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 55 | ffromcity | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 56 | fbuyertaxno | 收票方税号 | varchar | 50 |  | √ | ' ' | 收票方税号 |
| 57 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 58 | fmakeoutcompname | 开票公司 | varchar | 250 |  | √ | ' ' | 开票公司 |
| 59 | fflighttrainnums | 航班号/车次 | varchar | 30 |  | √ | ' ' | 航班号/车次 |
| 60 | fistartprovince | 出发省份 | varchar | 50 |  | √ | ' ' | 出发省份 |
| 61 | fismapexpense | 关联费用明细 | bpchar | 1 |  | √ | '1' | 关联费用明细,枚举: 1 :是 0 :否 |
| 62 | fpersonalinvoice | 个人发票 | varchar | 30 |  | √ | ' ' | 个人发票,枚举: 1 :是 0 :否 |
| 63 | finvoicegoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoicepool_query |  | finvoicetype,finvoicedate |
| 2 | pk_t_er_invoicepoolinfo |  | fentryid |
| 3 | idx_er_invoicepoolinfo_fseq |  | fid,fseq |

---

## 记费用-多语言表 t_er_expensepoolbill_l

- **表名称：** 记费用-多语言表
- **表名：** t_er_expensepoolbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fapplierposition | 职位 | varchar | 100 |  | √ | ' ' | 职位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_expensepoolbill_l |  | fpkid |
| 2 | idx_epb_l_id |  | fid,flocaleid |

---

## 座位等级-多选基础资料表 t_er_poolmulseatgrade

- **表名称：** 座位等级-多选基础资料表
- **表名：** t_er_poolmulseatgrade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 座位等级 er_seatgradestd |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_er_pooltripseatgrade |  | fbasedataid |
| 2 | pk_t_er_poolmulseatgrade |  | fpkid |

---

## 途径地-多选基础资料表 t_er_pooltrip2mulwayto

- **表名称：** 途径地-多选基础资料表
- **表名：** t_er_pooltrip2mulwayto

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_pooltripmulwayto |  | fid,fpkid,fbasedataid |
| 2 | pk_t_er_pooltrip2mulwayto |  | fpkid |

---

## 发票明细-子表 t_er_invoicepoolitem

- **表名称：** 发票明细-子表
- **表名：** t_er_invoicepoolitem

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
| 1 | idx_er_invoicepoolitem |  | fitementryid |
| 2 | pk_t_er_invoicepoolitem |  | fentryid |
| 3 | idx_er_invoicepoolitem_fid |  | fid |

---

## 记费用-主表 t_er_expensepoolbill

- **表名称：** 记费用-主表
- **表名：** t_er_expensepoolbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 3 | ftripstartdate | ftripstartdate | timestamp | 0 |  |  | null |  |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 5 | fformgroup | 单据体行合并策略 | int8 | 64 |  | √ | 0 | 单据体行合并策略 |
| 6 | freimbursetime | 报销次数 | int4 | 32 |  | √ | 0 | 报销次数 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | finvoicetotalcount | 发票张数 | int4 | 32 |  | √ | 0 | 发票张数 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 12 | ftrippassenger | 乘客 | varchar | 100 |  | √ | ' ' | 乘客 |
| 13 | ftaxclasscodeid | 税收分类编码 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 14 | finvoiceno | 发票号码 | varchar | 129 |  | √ | ' ' | 发票号码 |
| 15 | fvehicle | 交通工具 | bpchar | 1 |  | √ | '0' | 交通工具,枚举: 0 :空 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他工具 6 :住宿 7 :补助 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | fbilltypefield | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 18 | ftripexpenseitem | ftripexpenseitem | int8 | 64 |  | √ | 0 |  |
| 19 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 20 | fexpenseitemid | 差旅项目 | int8 | 64 |  | √ | 0 | 差旅项目 er_tripexpenseitem |
| 21 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :未报销 B :已报销 |
| 23 | fserialno | 发票序列号 | varchar | 50 |  | √ | ' ' | 发票序列号 |
| 24 | ftripdateareatext | 行程期间 | varchar | 50 |  | √ | ' ' | 行程期间 |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fdescription | 消费事由 | varchar | 1000 |  | √ | ' ' | 消费事由 |
| 27 | ftripcheckindate | 入住时间 | timestamp | 0 |  |  | null | 入住时间 |
| 28 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 机场建设费及其他 |
| 29 | fstartdate | 出发时间 | timestamp | 0 |  |  | null | 出发时间 |
| 30 | fitemalltaxclasscode | fitemalltaxclasscode | varchar | 100 |  | √ | ' ' |  |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 32 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | ftel | 联系方式 | varchar | 100 |  | √ | ' ' | 联系方式 |
| 34 | fexpenseitemedit | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 35 | ftargetbillno | 下游单据编码 | varchar | 50 |  | √ | ' ' | 下游单据编码 |
| 36 | ftripdeparturedate | 离店时间 | timestamp | 0 |  |  | null | 离店时间 |
| 37 | airportconstructionfee | airportconstructionfee | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 38 | ftriparea | 出差地域 | int8 | 64 |  | √ | 0 | 出差地域 er_triparea |
| 39 | fcreatedate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 40 | fbilltypestr | 单据类别 | bpchar | 1 |  | √ | '0' | 单据类别,枚举: 1 :记费用 2 :记差旅 |
| 41 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fgoodsname | 商品名称 | varchar | 50 |  | √ | ' ' | 商品名称 |
| 43 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 44 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_expense_recordbill :记费用 er_trip_recordbill :记差旅 |
| 45 | forientryamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 46 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 47 | ftripto | 目的地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 48 | ftargetbillcurrency | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 51 | ftripfrom | 出发地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 52 | finvoicelink | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 53 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 54 | fexpenseamount | 报销金额 | numeric | 23 | 10 | √ | 0.0000000000 | 报销金额 |
| 55 | ftripcityfield | 城市 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_expensepoolbill |  | fid |
| 2 | idx_er_pool_fcreatorid |  | fcreatorid |
| 3 | idx_er_pool_fbillno |  | fbillno |
| 4 | idx_er_pool_fcompanyid |  | fcompanyid |
