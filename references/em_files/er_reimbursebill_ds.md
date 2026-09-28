# 费用明细查询表-er_reimbursebill_ds

## 费用明细查询表-主表 t_er_reimbursebillds

- **表名称：** 费用明细查询表-主表
- **表名：** t_er_reimbursebillds

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funauditmsg | 反审核意见 | varchar | 1000 |  |  | null | 反审核意见 |
| 3 | fpaycompanyid | 支付公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fassetorgid | 资产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fnoinvoice | 无票 | bpchar | 1 |  | √ | '0' | 无票 |
| 6 | forgid | 部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbillpayertype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 |
| 9 | fhasvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 10 | fhead_paydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 11 | fisonaccount | 是否挂账 | bpchar | 1 |  | √ | '0' | 是否挂账 |
| 12 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0 | 报销金额 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 15 | fapplierpositionstr | fapplierpositionstr | varchar | 100 |  | √ | ' ' |  |
| 16 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | fbilltypefield | fbilltypefield | int8 | 64 |  | √ | 0 |  |
| 19 | foffsetinvoiceno | foffsetinvoiceno | varchar | 255 |  | √ | ' ' |  |
| 20 | fstdbilltype | fstdbilltype | int8 | 64 |  | √ | 0 |  |
| 21 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 22 | fwithholdingamount | 已预提金额 | numeric | 23 | 10 | √ | 0 | 已预提金额 |
| 23 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 H :废弃 I :关闭 |
| 24 | finvoiceoffsetamount | 抵扣税额汇总（发票信息） | numeric | 23 | 10 | √ | 0 | 抵扣税额汇总（发票信息） |
| 25 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 26 | fdescription | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 27 | fautomapinvoice | 智能发票报销 | bpchar | 1 |  | √ | '1' | 智能发票报销 |
| 28 | foffsetamount | foffsetamount | numeric | 23 | 10 | √ | 0 |  |
| 29 | fimagenumber | 影像编号 | varchar | 255 |  | √ | ' ' | 影像编号 |
| 30 | fattachmentacount | fattachmentacount | int8 | 64 |  | √ | 0 |  |
| 31 | fassettype | 资产类型 | varchar | 20 |  | √ | ' ' | 资产类型,枚举: newasset :新增资产 existasset :已有资产 |
| 32 | fbillid | 单据id | int8 | 64 |  | √ | 0 | 单据id |
| 33 | fapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 34 | fnotpayamount | 未付金额 | numeric | 23 | 10 | √ | 0 | 未付金额 |
| 35 | fpayedamount | 已付金额 | numeric | 23 | 10 | √ | 0 | 已付金额 |
| 36 | fnextauditor | 下一步审核人 | varchar | 100 |  | √ | ' ' | 下一步审核人 |
| 37 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fcompanyid | 公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fbalanceamount | fbalanceamount | numeric | 23 | 10 | √ | 0 |  |
| 40 | fisoverbudget | 是否超预算 | bpchar | 1 |  | √ | '0' | 是否超预算 |
| 41 | ftel | 联系方式 | varchar | 100 |  | √ | ' ' | 联系方式 |
| 42 | fisshared | 是否已分摊 | bpchar | 1 |  | √ | '0' | 是否已分摊 |
| 43 | fbillpayerid | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 44 | fpayamount | 付现 | numeric | 23 | 10 | √ | 0 | 付现 |
| 45 | fprojectsharecount | fprojectsharecount | int4 | 32 |  | √ | 0 |  |
| 46 | fcashier | fcashier | int8 | 64 |  | √ | 0 |  |
| 47 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 48 | fneedsuppleinvoice | 发票后补 | bpchar | 1 |  | √ | '0' | 发票后补 |
| 49 | fspecialbill | fspecialbill | bpchar | 1 |  | √ | ' ' |  |
| 50 | fsharedamount | 已分摊金额 | numeric | 23 | 10 | √ | 0 | 已分摊金额 |
| 51 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 52 | fstdreimbursetype | 关联业务 | varchar | 30 |  | √ | ' ' | 关联业务,枚举: biztype_project :立项 biztype_contract :合同 biztype_estimate :无合同暂估 biztype_contractestimate :有合同暂估 biztype_other :无 |
| 53 | fpaycurrency | 付现金额币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 54 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 er_publicreimbursebill_asset :资产报账单 |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 56 | fis_all_einvoice | fis_all_einvoice | bpchar | 1 |  | √ | '0' |  |
| 57 | freimbursecontrolcomany | freimbursecontrolcomany | int8 | 64 |  | √ | 0 |  |
| 58 | ftriptypeid | 出差类型 | int8 | 64 |  | √ | 0 | 出差类型 er_triptype |
| 59 | fonaccountamount | 挂账金额 | numeric | 23 | 10 | √ | 0 | 挂账金额 |
| 60 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 61 | fismultireimburser | 多报销人 | bpchar | 1 |  | √ | ' ' | 多报销人 |
| 62 | fproxytax | 代扣代缴 | bpchar | 1 |  | √ | '0' | 代扣代缴 |
| 63 | fisstdover | 是否超标 | bpchar | 1 |  | √ | '0' | 是否超标 |
| 64 | fiscurrency | 多币别 | bpchar | 1 |  | √ | '0' | 多币别 |
| 65 | freimbursetype | 报账类型 | varchar | 30 |  | √ | ' ' | 报账类型,枚举: asset :资产报账 expense :费用报账 |
| 66 | fauditopinion | 审核意见 | varchar | 100 |  | √ | ' ' | 审核意见 |
| 67 | fbizitem | 业务事项 | int8 | 64 |  | √ | 0 | 业务事项 er_standard_type |
| 68 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 69 | fispaybyhead | 按单头付款 | bpchar | 1 |  | √ | '0' | 按单头付款 |
| 70 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 71 | ftotalaccloanamount | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 72 | ftarbillstatus | ftarbillstatus | varchar | 30 |  | √ | ' ' |  |
| 73 | freimbursecurrency | 报销金额币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 74 | fprojecttype | 业务分类 | int8 | 64 |  | √ | 0 | 业务分类 er_projecttype |
| 75 | fcurrencyid | 本位币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_reimbursebillds |  | fid |
| 2 | idx_er_reimds_fcompanyid |  | fcompanyid |
| 3 | idx_er_reimds_fbillstatus |  | fbillstatus |
| 4 | idx_er_reimds_fapplierid |  | fapplierid |
| 5 | idx_er_reimds_fbizdate_fbillno |  | fbizdate,fbillno |
| 6 | idx_er_reimds_fcreatorid |  | fcreatorid |
| 7 | idx_er_reimds_fbillno |  | fbillno |

---

## 座位等级-多选基础资料表 t_er_reimdsseatgrade

- **表名称：** 座位等级-多选基础资料表
- **表名：** t_er_reimdsseatgrade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 座位等级 er_seatgradestd |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_reimdsseatgrade |  | fpkid |
| 2 | idx_er_reimdsseatgrade |  | fentryid,fbasedataid |

---

## 出差人-多选基础资料表 t_er_reimbursedspartner

- **表名称：** 出差人-多选基础资料表
- **表名：** t_er_reimbursedspartner

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_reimbursedspartner |  | fpkid |
| 2 | idx_er_reimdspartner_fentryid |  | fentryid |

---

## 发票信息-子表 t_er_invoiceentry

- **表名称：** 发票信息-子表
- **表名：** t_er_invoiceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmapexpenseinfo | fmapexpenseinfo | varchar | 255 |  |  | ' ' |  |
| 3 | ftaxrate | 平均税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 平均税率（%） |
| 4 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 7 | fpassengername | 旅客 | varchar | 255 |  |  | null | 旅客 |
| 8 | fissupplement | 后补发票 | varchar | 30 |  | √ | ' ' | 后补发票,枚举: 0 :否 1 :是 |
| 9 | fordertype | fordertype | bpchar | 1 |  | √ | ' ' |  |
| 10 | finvoicecode | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 11 | fbuyername | 收票公司 | varchar | 250 |  | √ | ' ' | 收票公司 |
| 12 | fpassverifybuyername | 发票抬头一致 | varchar | 30 |  | √ | ' ' | 发票抬头一致,枚举: 1 :是 0 :否 |
| 13 | fpassverifybuyertaxno | 发票税号一致 | varchar | 30 |  | √ | ' ' | 发票税号一致,枚举: 1 :是 0 :否 |
| 14 | finvoiceno | 发票号码 | varchar | 129 |  | √ | ' ' | 发票号码 |
| 15 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 16 | freasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 17 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 18 | fseatgrade | 座位等级 | varchar | 50 |  | √ | ' ' | 座位等级,枚举: |
| 19 | foffsetamount | 抵扣税额 | numeric | 23 | 10 | √ | 0 | 抵扣税额 |
| 20 | fistartcity | 出发城市 | varchar | 50 |  | √ | ' ' | 出发城市 |
| 21 | finvoicecurrencyid | finvoicecurrencyid | int8 | 64 |  | √ | 0 |  |
| 22 | fbuyerorgid | 收票公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 |
| 24 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0 | 机场建设费及其他 |
| 25 | ftocity | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 26 | fcustomeridnumber | 身份证 | varchar | 50 |  | √ | ' ' | 身份证 |
| 27 | ftransportnote | 运输票据 | varchar | 30 |  | √ | ' ' | 运输票据,枚举: 1 :是 0 :否 |
| 28 | fsequencenum | 是否连号 | varchar | 30 |  | √ | ' ' | 是否连号,枚举: 1 :是 2 :否 |
| 29 | ffrominvoicecloud | 发票云导入 | bpchar | 1 |  | √ | '0' | 发票云导入 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 31 | finoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 32 | fidestcity | 目的城市 | varchar | 50 |  | √ | ' ' | 目的城市 |
| 33 | fticketchanges | 机票状态 | varchar | 30 |  | √ | ' ' | 机票状态,枚举: 1 :正常 2 :改签 |
| 34 | finvoicesrcbillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 35 | finvoiceischange | 是否修改 | varchar | 30 |  | √ | ' ' | 是否修改,枚举: 1 :否 2 :是 |
| 36 | falltaxrate | 税率(%) | varchar | 100 |  | √ | ' ' | 税率(%) |
| 37 | fievalidatest | 查验状态 | bpchar | 1 |  | √ | '3' | 查验状态,枚举: 1 :通过 2 :不通过 3 :- |
| 38 | fidestprovince | 目的省份 | varchar | 50 |  | √ | ' ' | 目的省份 |
| 39 | fothertotaltaxamount | 其他税费 | numeric | 23 | 10 | √ | 0 | 其他税费 |
| 40 | finvoicesrcentryid | 源分录id | int8 | 64 |  | √ | 0 | 源分录id |
| 41 | finsurancepremium | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 42 | fvalidatemessage | 发票校验结果 | varchar | 255 |  | √ | ' ' | 发票校验结果 |
| 43 | fairconstfee | 机场建设费 | numeric | 23 | 10 | √ | 0 | 机场建设费 |
| 44 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 45 | finvoicealltaxcode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 46 | fcount | 发票张数 | int4 | 32 |  | √ | 0 | 发票张数 |
| 47 | finvoicenotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 48 | finvoicefrom | 发票来源 | varchar | 30 |  | √ | '1' | 发票来源,枚举: 1 :发票云 2 :OCR识别 3 :商旅月结 |
| 49 | fbillcreatetime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 50 | ffromcity | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 51 | fbuyertaxno | 收票方税号 | varchar | 50 |  | √ | ' ' | 收票方税号 |
| 52 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 53 | fmakeoutcompname | 开票公司 | varchar | 250 |  | √ | ' ' | 开票公司 |
| 54 | fflighttrainnums | 航班号/车次 | varchar | 30 |  | √ | ' ' | 航班号/车次 |
| 55 | fistartprovince | 出发省份 | varchar | 50 |  | √ | ' ' | 出发省份 |
| 56 | fismapexpense | 关联费用明细 | bpchar | 1 |  | √ | '1' | 关联费用明细,枚举: 1 :是 0 :否 |
| 57 | finvoicesrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: er_expense_recordbill :费用记录 er_trip_recordbill :差旅记录 |
| 58 | fpersonalinvoice | 个人发票 | varchar | 30 |  | √ | ' ' | 个人发票,枚举: 1 :是 0 :否 |
| 59 | finvoicegoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoentry_fseq |  | fid,fseq |
| 2 | idx_er_invoentry_serialno |  | fserialno |
| 3 | pk_t_er_invoiceentry |  | fentryid |
| 4 | idx_er_invoentry_query |  | finvoicetype,finvoicedate |

---

## 费用明细查询表-多语言表 t_er_reimbursebillds_l

- **表名称：** 费用明细查询表-多语言表
- **表名：** t_er_reimbursebillds_l

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
| 1 | idx_reimds_reimburseds_l_id |  | fid,flocaleid |
| 2 | pk_t_er_reimbursebillds_l |  | fpkid |

---

## 费用明细查询表-分表 t_er_reimbursebillds_a

- **表名称：** 费用明细查询表-分表
- **表名：** t_er_reimbursebillds_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fabovequota | 是否超额 | varchar | 30 |  | √ | ' ' | 是否超额,枚举: 1 :超额 2 :未超额 0 :- |
| 3 | fsharerule | 分摊规则 | varchar | 30 |  | √ | ' ' | 分摊规则,枚举: orgrule :按部门分摊 monthrule :按月分摊 yearrule :按年分摊 |
| 4 | fattachmentcount | 附件数 | int4 | 32 |  | √ | 0 | 附件数 |
| 5 | fsharemethod | 分摊方法 | varchar | 30 |  | √ | ' ' | 分摊方法,枚举: rate :比例分摊 avg :金额平均 amount :金额分摊 |
| 6 | fisbeforeshare | 费用分摊 | bpchar | 1 |  | √ | '0' | 费用分摊 |
| 7 | fmonthrulestartdate | 开始月份 | timestamp | 0 |  |  | null | 开始月份 |
| 8 | fmonthruleenddate | 结束月份 | timestamp | 0 |  |  | null | 结束月份 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_reimbursebillds_a |  | fid |

---

## 费用明细-子表 t_er_reimbilldsexp

- **表名称：** 费用明细-子表
- **表名：** t_er_reimbilldsexp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexporiusedamount | fexporiusedamount | numeric | 23 | 10 | √ | 0 |  |
| 3 | fhappendate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 4 | fserialno_entry | 发票序列号 | varchar | 200 |  |  | ' ' | 发票序列号 |
| 5 | fentrycurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 6 | fdeductibletax | 抵扣税额 | numeric | 23 | 10 | √ | 0 | 抵扣税额 |
| 7 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0 | 税率 |
| 8 | finvoiceno_entry | 发票号码 | varchar | 255 |  |  | ' ' | 发票号码 |
| 9 | forgiexpebalanceamount | forgiexpebalanceamount | numeric | 23 | 10 | √ | 0 |  |
| 10 | fsourceentryid | fsourceentryid | int8 | 64 |  | √ | 0 |  |
| 11 | fordernum | 关联订单号 | varchar | 500 |  |  | ' ' | 关联订单号 |
| 12 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 13 | foffset | 是否抵扣 | bpchar | 1 |  | √ | '0' | 是否抵扣 |
| 14 | fentrycontractname | 合同名称 | varchar | 200 |  |  | ' ' | 合同名称 |
| 15 | freimburseamount | 报销金额 | numeric | 23 | 10 | √ | 0 | 报销金额 |
| 16 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 17 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 18 | fcurrreimburseamount | 报销金额(本位币) | numeric | 23 | 10 | √ | 0 | 报销金额(本位币) |
| 19 | ftoplaceid | 目的地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 20 | fisover | 是否超标 | bpchar | 1 |  | √ | '0' | 是否超标,枚举: 1 :是 0 :否 |
| 21 | fcurprice | 核定不含税金额（本位币） | numeric | 23 | 10 | √ | 0 | 核定不含税金额（本位币） |
| 22 | fsettlementtype | 结算方式 | bpchar | 1 |  | √ | '1' | 结算方式,枚举: 1 :现付 2 :月结 |
| 23 | fvehicle | 交通工具 | varchar | 50 |  | √ | ' ' | 交通工具,枚举: 1 :飞机 2 :火车 3 :汽车 4 :轮船 5 :其他交通工具 |
| 24 | foverdesc | 超标说明 | varchar | 500 |  |  | ' ' | 超标说明 |
| 25 | fexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | 费用项目 er_expenseitemedit |
| 26 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 27 | fexpehasreimamount | fexpehasreimamount | numeric | 23 | 10 | √ | 0 |  |
| 28 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 29 | fapprovetax | 核定税额 | numeric | 23 | 10 | √ | 0 | 核定税额 |
| 30 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 31 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 32 | fexpeorirepayamount | fexpeorirepayamount | numeric | 23 | 10 | √ | 0 |  |
| 33 | freimburser | 报销人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | ftripexpenseitemid | 差旅项目 | int8 | 64 |  | √ | 0 | 差旅项目 er_tripexpenseitem |
| 35 | fexpeapprovecurramount | 核定金额（本位币） | numeric | 23 | 10 | √ | 0 | 核定金额（本位币） |
| 36 | fexperepayamount | fexperepayamount | numeric | 23 | 10 | √ | 0 |  |
| 37 | fairportconstructionfee | 机场建设费及其他 | numeric | 23 | 10 | √ | 0 | 机场建设费及其他 |
| 38 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 39 | ftaxclasscode | 税收分类编码基础资料 | int8 | 64 |  | √ | 0 | 税收分类编码 er_taxclasscode |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fexpusedamount | fexpusedamount | numeric | 23 | 10 | √ | 0 |  |
| 42 | fentryprojectno | 立项号 | varchar | 30 |  | √ | ' ' | 立项号 |
| 43 | ftripday | 行程天数 | int4 | 32 |  | √ | 0 | 行程天数 |
| 44 | foriamount | 不含税金额 | numeric | 23 | 10 | √ | 0 | 不含税金额 |
| 45 | fhighseasondaycount | 旺季天数 | numeric | 23 | 10 | √ | 0 | 旺季天数 |
| 46 | fprice | 核定不含税金额 | numeric | 23 | 10 | √ | 0 | 核定不含税金额 |
| 47 | fentrycostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 48 | fentrycontractno | 合同号 | varchar | 30 |  | √ | ' ' | 合同号 |
| 49 | fstd_entrycostcenter | fstd_entrycostcenter | int8 | 64 |  | √ | 0 |  |
| 50 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 51 | ffromplaceid | 出发地 | int8 | 64 |  | √ | 0 | 行政区划 bd_admindivision |
| 52 | fitemreasonfortransferout | 转出原因 | varchar | 200 |  |  | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 53 | fexpensegoodsname | 商品名称 | varchar | 255 |  |  | ' ' | 商品名称 |
| 54 | ftripentryarea | 出差地域 | int8 | 64 |  | √ | 0 | 出差地域 er_triparea |
| 55 | fexpebalanceamount | fexpebalanceamount | numeric | 23 | 10 | √ | 0 |  |
| 56 | finvoicelink | 发票代码 | varchar | 200 |  |  | ' ' | 发票代码 |
| 57 | fwbpaytype | 付款类型 | varchar | 50 |  | √ | ' ' | 付款类型,枚举: PREPAYMENT :预付款 PROGRESSPAYMENT :进度款 SETTLEPAYMENT :结算款 BOND :保证金 REWORDORPUNISH :奖惩 OTHERS :其它 |
| 58 | fis_special_invoice | 专票 | bpchar | 1 |  | √ | '0' | 专票 |
| 59 | fexpeorihasreimamount | fexpeorihasreimamount | numeric | 23 | 10 | √ | 0 |  |
| 60 | freimctldeptid | 额度控制部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 61 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 62 | fiteminoutamount | 转出金额 | numeric | 23 | 10 | √ | 0 | 转出金额 |
| 63 | fexpeapproveamount | 核定金额 | numeric | 23 | 10 | √ | 0 | 核定金额 |
| 64 | fentrycostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 65 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_reimbilldsexp_id |  | fid |
| 2 | pk_er_reimbilldsexp |  | fentryid |

---

## 收款信息-子表 t_er_reimdsaccinfo

- **表名称：** 收款信息-子表
- **表名：** t_er_reimdsaccinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccountcurrency | 币种 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fbuildedamount | 已出单金额 | numeric | 19 | 6 | √ | 0 | 已出单金额 |
| 4 | foriamount | 收款金额 | numeric | 19 | 6 | √ | 0 | 收款金额 |
| 5 | fpayeraccount01 | 银行账号4位 | varchar | 100 |  | √ | ' ' | 银行账号4位 |
| 6 | fpayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 er_payeer :个人 other :其他 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | famount | 收款金额（本位币） | numeric | 19 | 6 | √ | 0 | 收款金额（本位币） |
| 9 | foriaccnotpayamount | 未付金额 | numeric | 19 | 6 | √ | 0 | 未付金额 |
| 10 | fexchangerate | 汇率 | numeric | 19 | 6 | √ | 0 | 汇率 |
| 11 | fpayername | 收款人 | varchar | 100 |  | √ | ' ' | 收款人 |
| 12 | fsupplier | 收款人（供应商） | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 13 | fentryrepaydate | 还款日期 | timestamp | 0 |  |  | null | 还款日期 |
| 14 | fpayerid | 收款人 | int8 | 64 |  | √ | 0 | 收款信息 er_payeer |
| 15 | faccbalanceamount | 可用余额（本位币） | numeric | 19 | 6 | √ | 0 | 可用余额（本位币） |
| 16 | fcustomer | 收款人（客户） | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 17 | fpayerbankid | 开户银行 | int8 | 64 |  | √ | 0 | 行名行号 bd_bebank |
| 18 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 19 | foriaccpayedamount | 已付金额 | numeric | 19 | 6 | √ | 0 | 已付金额 |
| 20 | foriaccbalanceamount | 可用余额 | numeric | 19 | 6 | √ | 0 | 可用余额 |
| 21 | faccpayedamount | 已付金额（本位币） | numeric | 19 | 6 | √ | 0 | 已付金额（本位币） |
| 22 | fcasorg | 收款人（内部公司） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | faccnotpayamount | 未付金额(本位币) | numeric | 19 | 6 | √ | 0 | 未付金额(本位币) |
| 24 | fpayeraccount02 | 银行账号(显示_old) | varchar | 100 |  | √ | ' ' | 银行账号(显示_old) |
| 25 | fpayeraccount | 银行帐号 | varchar | 100 |  | √ | ' ' | 银行帐号 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_reimdsaccinfo |  | fentryid |
| 2 | idx_er_reimdsaccinfo_fseq |  | fid,fseq |
