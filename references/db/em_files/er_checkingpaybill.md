# 商旅付款申请单-er_checkingpaybill

## 发票明细-子表 t_er_invoiceitemcp

- **表名称：** 发票明细-子表
- **表名：** t_er_invoiceitemcp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 3 | fexcludeamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 4 | ftaxrate | 税率 | numeric | 23 | 10 | √ | 0.0000000000 | 税率 |
| 5 | finvoiceitemoffset | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 6 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | finvoiceitemisunbind | 解绑 | bpchar | 1 |  | √ | '0' | 解绑 |
| 9 | fitementryid | 费用项目分录id | int8 | 64 |  | √ | 0 | 费用项目分录id |
| 10 | finvoiceitemserialno | 发票序列号 | varchar | 255 |  | √ | ' ' | 发票序列号 |
| 11 | finvoicecurrency | 发票币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 12 | fnum | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 13 | finvoiceheadentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 14 | funitprice | 不含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税单价 |
| 15 | fgoodscode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 16 | finvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 17 | fspecmodel | 规格型号 | varchar | 600 |  | √ | ' ' | 规格型号 |
| 18 | fgoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |
| 19 | finvoicecloudoffset | 发票抵扣 | bpchar | 1 |  | √ | '1' | 发票抵扣 |
| 20 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 23 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 24 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoiceitemcp_itementry |  | fitementryid |
| 2 | idx_er_invoiceitemcp_invhead |  | finvoiceheadentryid |
| 3 | t_er_invoiceitemcp_pkey |  | fentryid |
| 4 | idx_er_invoiceitemcp_fid |  | fid |

---

## 发票云附件-子表 t_er_invoiceattachinfo

- **表名称：** 发票云附件-子表
- **表名：** t_er_invoiceattachinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fattstarttime | fattstarttime | timestamp | 0 |  |  | null |  |
| 3 | fattlargetxt | fattlargetxt | varchar | 255 |  |  | null |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fattachserialno | 发票序列号 | varchar | 255 |  | √ | ' ' | 发票序列号 |
| 6 | fattsource | fattsource | varchar | 30 |  | √ | ' ' |  |
| 7 | fattachno | 附件序列号 | varchar | 80 |  | √ | ' ' | 附件序列号 |
| 8 | frotationangle | 旋转角度 | varchar | 30 |  |  | null | 旋转角度 |
| 9 | fattaffairdiscription | fattaffairdiscription | varchar | 1024 |  |  | null |  |
| 10 | fattheadcount | fattheadcount | int8 | 64 |  | √ | 0 |  |
| 11 | fattcity | fattcity | varchar | 255 |  |  | null |  |
| 12 | fattachurl | 附件 url | varchar | 512 |  |  | null | 附件 url |
| 13 | fattenddate | fattenddate | timestamp | 0 |  |  | null |  |
| 14 | fattinvoiceentyid | fattinvoiceentyid | int8 | 64 |  | √ | 0 |  |
| 15 | fattfrom | fattfrom | varchar | 255 |  |  | null |  |
| 16 | fattlargetxt_tag | fattlargetxt_tag | text | 0 |  |  | null |  |
| 17 | fattachname | 附件名称 | varchar | 255 |  |  | null | 附件名称 |
| 18 | fattachremark | 备注 | varchar | 1024 |  |  | null | 备注 |
| 19 | foriginalname | 源文件名称 | varchar | 255 |  |  | null | 源文件名称 |
| 20 | fattto | fattto | varchar | 255 |  |  | null |  |
| 21 | fgathertime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 22 | fattendtime | fattendtime | timestamp | 0 |  |  | null |  |
| 23 | fattapplydate | fattapplydate | timestamp | 0 |  |  | null |  |
| 24 | fattstartdate | fattstartdate | timestamp | 0 |  |  | null |  |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fatttotalamount | fatttotalamount | numeric | 23 | 10 | √ | 0 |  |
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

## 商旅付款申请单-主表 t_er_checkingpay

- **表名称：** 商旅付款申请单-主表
- **表名：** t_er_checkingpay

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvokeinvoicecloud | 与发票云交互 | bpchar | 1 |  | √ | '0' | 与发票云交互 |
| 3 | fplanetotalamount |  | numeric | 23 | 10 | √ | 0 |  |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftotalamount | 应付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 应付金额 |
| 6 | fcompany | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fhasvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 8 | finvamount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fenddate | 结束期间 | varchar | 50 |  | √ | ' ' | 结束期间 |
| 11 | fhoteltotalamount |  | numeric | 23 | 10 | √ | 0 |  |
| 12 | foperationtype | 服务类型 | bpchar | 1 |  | √ | ' ' | 服务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 7 :用餐预订 |
| 13 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 14 | fserver | 服务商 | varchar | 100 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 MEITUAN :美团 GAODE :高德 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 |
| 15 | finvffsettaxamount | 发票可抵扣税额 | numeric | 23 | 10 | √ | 0 | 发票可抵扣税额 |
| 16 | fannexnum | 附件数 | int8 | 64 |  | √ | 0 | 附件数 |
| 17 | fmealtotalamount |  | numeric | 23 | 10 | √ | 0 |  |
| 18 | forderformid | 订单表单ID | varchar | 30 |  | √ | ' ' | 订单表单ID |
| 19 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fpaymodeid | 支付方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :审核中 D :审核未通过 E :审核通过 F :等待付款 G :已付款 |
| 23 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 24 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 25 | fautomapinvoice | 智能发票报销 | bpchar | 1 |  | √ | '0' | 智能发票报销 |
| 26 | fbankname | 银行名称(废弃) | varchar | 100 |  | √ | ' ' | 银行名称(废弃) |
| 27 | fimagenumber | 影像编码 | varchar | 50 |  | √ | ' ' | 影像编码 |
| 28 | frplanetotalamount |  | numeric | 23 | 10 | √ | 0 |  |
| 29 | frtraintotalamount |  | numeric | 23 | 10 | √ | 0 |  |
| 30 | fperiod | 期间 | varchar | 50 |  | √ | ' ' | 期间 |
| 31 | fhappenddate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 32 | ftraintotalamount |  | numeric | 23 | 10 | √ | 0 |  |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fappliercompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fpayertype | 收款人类型 | varchar | 30 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :内部公司 cas_othercontactunit :其他往来单位 |
| 36 | fservicetotalamount |  | numeric | 23 | 10 | √ | 0 |  |
| 37 | fbankaccount | 银行账号(废弃) | varchar | 80 |  | √ | ' ' | 银行账号(废弃) |
| 38 | fpayamount | 实付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实付金额 |
| 39 | fpaybillnum | 付款单号 | varchar | 100 |  | √ | ' ' | 付款单号 |
| 40 | fplaneairportprice |  | numeric | 23 | 10 | √ | 0 |  |
| 41 | fdifferenttax | 专票税额差异 | numeric | 23 | 10 | √ | 0 | 专票税额差异 |
| 42 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fapplyexplain | 申请说明 | varchar | 600 |  | √ | ' ' | 申请说明 |
| 44 | fapplierdeptid | 申请人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fpayeraccountname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 46 | fpayerid | 收款人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 47 | fsettleamount | 结算金额 | numeric | 23 | 10 | √ | 0 | 结算金额 |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | fpayerbankid | 收款银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 50 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 51 | fcurrency | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 52 | fvehicletotalamount |  | numeric | 23 | 10 | √ | 0 |  |
| 53 | fpaybillid | 付款单id | int8 | 64 |  | √ | 0 | 付款单id |
| 54 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 55 | fdifferentffsettax | 税额差异 | numeric | 23 | 10 | √ | 0 | 税额差异 |
| 56 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 57 | ftotalaccloanamount | 核销金额 | numeric | 23 | 10 | √ | 0 | 核销金额 |
| 58 | fsettaxamount | 结算可抵扣税额 | numeric | 23 | 10 | √ | 0 | 结算可抵扣税额 |
| 59 | fpayeraccount | 银行账号 | varchar | 80 |  | √ | ' ' | 银行账号 |
| 60 | fpaybillwriteback | 付款单反写金额 | numeric | 23 | 10 | √ | 0.0000000000 | 付款单反写金额 |
| 61 | fpaycompany | 支付公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 62 | fpaydate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_checkingpay_fcompany |  | fcompany |
| 2 | idx_er_checkingpay_fbillno |  | fbillno |
| 3 | t_er_checkingpay_pkey |  | fid |
| 4 | idx_er_checkingpay_fbillstatus |  | fbillstatus |

---

## 冲借款-子表 t_er_checkingpaywrioff

- **表名称：** 冲借款-子表
- **表名：** t_er_checkingpaywrioff

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | floanperson | 借款人 | varchar | 200 |  | √ | ' ' | 借款人 |
| 3 | fentrywlunit | 往来单位 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 4 | floanbillnov1 | 单据编号 | varchar | 100 |  | √ | '0' | 单据编号 |
| 5 | fsourceentryid | 借款明细分录ID | int8 | 64 |  | √ | 0 | 借款明细分录ID |
| 6 | fcostdeptid | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fcurrloanamount | 借款余额（本位币） | numeric | 23 | 10 | √ | 0 | 借款余额（本位币） |
| 8 | floanprojectno | 立项号 | varchar | 200 |  | √ | ' ' | 立项号 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fsrcofsrcentryid | 冲借款源分录id | int8 | 64 |  | √ | 0 | 冲借款源分录id |
| 11 | floanapplydatev1 | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 12 | fsourcesign | 关联申请 | bpchar | 1 |  | √ | '0' | 关联申请 |
| 13 | fcostcompanyid | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 14 | fstdentrycostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 15 | faccloanamount | 冲销金额 | numeric | 23 | 10 | √ | 0 | 冲销金额 |
| 16 | fcurraccloanamount | 冲销金额(本位币) | numeric | 23 | 10 | √ | 0 | 冲销金额(本位币) |
| 17 | floanamount | 借款余额 | numeric | 23 | 10 | √ | 0 | 借款余额 |
| 18 | floanexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 19 | floancurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 20 | fsourcebillid | 源单id | varchar | 100 |  | √ | ' ' | 源单id |
| 21 | fsrcbilltype | 源单类型 | varchar | 200 |  | √ | ' ' | 源单类型,枚举: er_dailyloanbill :借款单 er_prepaybill :预付单 |
| 22 | floandescriptionv1 | 事由 | varchar | 1000 |  | √ | ' ' | 事由 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fquotetype | 换算方式（冲借款） | bpchar | 1 |  | √ | '0' | 换算方式（冲借款）,枚举: 0 :直接汇率 1 :间接汇率 |
| 25 | fsourceexpenseitemid | 费用项目 | int8 | 64 |  | √ | 0 | [费用项目 er_expenseitemedit](../basedata_files/er_expenseitemedit.md) |
| 26 | fentrywltype | 往来类型 | varchar | 50 |  | √ | ' ' | 往来类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_user :职员 cas_othercontactunit :其他往来单位 |
| 27 | floancontractno | 合同号 | varchar | 500 |  | √ | ' ' | 合同号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_checkingpaywrioff_fid |  | fid |
| 2 | pk_t_er_checkingpaywrioff |  | fentryid |

---

## 关联子实体-子表 t_er_checkingpay_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_checkingpay_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | stableid | stableid | int8 | 64 |  | √ | 0 |  |
| 3 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_checkingpay_lk_pkey |  | fpkid |
| 2 | idx_er_checkingpay_lk_fid |  | fid |

---

## 发票与费用明细-子表 t_er_tripinvoiceanditem

- **表名称：** 发票与费用明细-子表
- **表名：** t_er_tripinvoiceanditem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finvoiceexpisunbind | 解绑 | bpchar | 1 |  | √ | '0' | 解绑 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | finvoiceentryid | 发票头分录id | int8 | 64 |  | √ | 0 | 发票头分录id |
| 5 | finvoiceexpserialno | 发票序列号 | varchar | 255 |  | √ | ' ' | 发票序列号 |
| 6 | fexpenseentryid | 费用明细分录id | int8 | 64 |  | √ | 0 | 费用明细分录id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tripinvoiceanditem_id |  | fid |
| 2 | idx_tripcheck_finvoiceentryid |  | finvoiceentryid |
| 3 | pk_t_er_tripinvoiceanditem |  | fentryid |
| 4 | idx_tripcheck_fexpenseentryid |  | fexpenseentryid |

---

## 关联子实体-子表 t_er_checkingpayentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_checkingpayentry_lk

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
| 1 | t_er_checkingpayentry_lk_pkey |  | fpkid |
| 2 | idx_er_checkingpayentry_lk_fk |  | fentryid |

---

## 商旅付款申请单-关联追踪表 t_er_checkingpay_tc

- **表名称：** 商旅付款申请单-关联追踪表
- **表名：** t_er_checkingpay_tc

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
| 1 | t_er_checkingpay_tc_pkey |  | fid |
| 2 | idx_er_checkingpay_tc_sbillid |  | fsbillid |
| 3 | idx_er_checkingpay_tc_tbillid |  | ftbillid |
| 4 | idx_er_checkingpay_tc_tbill |  | ftbillid |
| 5 | idx_er_checkingpay_tc_tid |  | ftid |

---

## 商旅付款申请单-反写记录表 t_er_checkingpay_wb

- **表名称：** 商旅付款申请单-反写记录表
- **表名：** t_er_checkingpay_wb

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
| 1 | idx_er_checkingpay_wb_fid |  | fid |
| 2 | t_er_checkingpay_wb_pkey |  | fentryid |

---

## 发票信息-子表 t_er_invoiceinfocp

- **表名称：** 发票信息-子表
- **表名：** t_er_invoiceinfocp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxrate | 平均税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 平均税率（%） |
| 3 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 4 | fuploadseq | 采集顺序 | int8 | 64 |  | √ | 0 | 采集顺序 |
| 5 | fordernum | 匹配结算单号 | varchar | 255 |  |  | null | 匹配结算单号 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcarrierdate | 乘车/机日期 | timestamp | 0 |  |  | null | 乘车/机日期 |
| 8 | foffset | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 9 | fisred | 红字发票 | bpchar | 1 |  | √ | '0' | 红字发票,枚举: 0 :否 1 :是 |
| 10 | finvoiceitemequal | 对平 | bpchar | 1 |  | √ | '1' | 对平 |
| 11 | fbuyeraddressphone | 地址电话 | varchar | 255 |  | √ | ' ' | 地址电话 |
| 12 | fpassengername | 旅客 | varchar | 255 |  |  | null | 旅客 |
| 13 | fenddate | 通行日期止 | timestamp | 0 |  |  | null | 通行日期止 |
| 14 | funitprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 15 | ffuelsurcharge | 燃油附加费 | numeric | 23 | 10 | √ | 0 | 燃油附加费 |
| 16 | finvoicecode | 发票代码 | varchar | 129 |  | √ | ' ' | 发票代码 |
| 17 | fcity | 发票所在地 | varchar | 50 |  | √ | ' ' | 发票所在地 |
| 18 | fbuyername | 收票公司 | varchar | 250 |  | √ | ' ' | 收票公司 |
| 19 | fpassverifybuyername | 发票抬头一致 | varchar | 30 |  | √ | ' ' | 发票抬头一致,枚举: 1 :是 0 :否 |
| 20 | fpassverifybuyertaxno | 发票税号一致 | varchar | 30 |  | √ | ' ' | 发票税号一致,枚举: 1 :是 0 :否 |
| 21 | finvoiceno | 发票号码 | varchar | 129 |  | √ | ' ' | 发票号码 |
| 22 | fsalertaxno | 开票方税号 | varchar | 50 |  | √ | ' ' | 开票方税号 |
| 23 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 24 | fisemployee | 职员 | bpchar | 1 |  | √ | '0' | 职员 |
| 25 | freasonfortransferout | 转出原因 | varchar | 30 |  | √ | ' ' | 转出原因,枚举: a :免税项目用 b :集体福利、个人消费 c :非正常损失 d :简易计税方法征税项目用 e :免抵退税办法不得抵扣的进项税额 f :纳税检查调减进项税额 g :红字专用发票信息表注明的进项税额 h :上期留抵税额抵减欠税 i :上期留抵税额退税 j :其他应作进项税额转出的情形 |
| 26 | fserialno | 发票序列号 | varchar | 80 |  | √ | ' ' | 发票序列号 |
| 27 | foffsetamount | 抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额 |
| 28 | finvoicecurrencyid | 发票币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fbuyerorgid | 收票公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 1 :普通电子发票 2 :电子发票专票 3 :普通纸质发票 4 :专用纸质发票 5 :普通纸质卷票 7 :通用机打 8 :的士票 9 :火车票 10 :飞机票 11 :其他 12 :机动车 13 :二手车 14 :定额发票 15 :通行费 16 :客运票 17 :过路过桥费 18 :车船税发票（专票） 19 :完税证明 20 :轮船票 21 :海关缴款书 23 :通用机打电子发票 24 :火车退票 25 :财政电子票据 26 :数电发票（普通发票） 27 :数电发票（增值税专用发票） 28 :数电票（航空运输电子客票行程单） 29 :数电票（铁路电子客票） 30 :形式发票 |
| 31 | fairportconstructionfee | 民航发展基金及其他 | numeric | 23 | 10 | √ | 0.0000000000 | 民航发展基金及其他 |
| 32 | ftocity | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 33 | fcustomeridnumber | 身份证 | varchar | 50 |  | √ | ' ' | 身份证 |
| 34 | fstartdate | 通行日期起 | timestamp | 0 |  |  | null | 通行日期起 |
| 35 | ffairtime | 飞机乘机时间 | varchar | 20 |  | √ | ' ' | 飞机乘机时间 |
| 36 | ftransportnote | 运输票据 | varchar | 30 |  | √ | ' ' | 运输票据,枚举: 1 :是 0 :否 |
| 37 | fsequencenum | 连号 | varchar | 30 |  | √ | ' ' | 连号,枚举: 1 :是 2 :否 |
| 38 | ffrominvoicecloud | 发票云导入 | bpchar | 1 |  | √ | '0' | 发票云导入 |
| 39 | fblockchain | 区块链 | bpchar | 1 |  | √ | '0' | 区块链 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | finoutamount | 转出金额 | numeric | 23 | 10 | √ | 0.0000000000 | 转出金额 |
| 42 | funit | 单位 | varchar | 50 |  | √ | ' ' | 单位 |
| 43 | fsequencenuminfo | 连号信息 | varchar | 255 |  | √ | ' ' | 连号信息 |
| 44 | fticketchanges | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: 1 :正常 2 :改签 3 :售票 4 :退票 1001 :失控 1002 :作废 1003 :红冲 1004 :异常 1005 :非正常 1006 :红字发票待确认 1007 :部分红冲 1008 :全部红冲 |
| 45 | finvoiceischange | 已修改 | varchar | 30 |  | √ | ' ' | 已修改,枚举: 1 :否 2 :是 |
| 46 | falltaxrate | 税率(%) | varchar | 100 |  | √ | ' ' | 税率(%) |
| 47 | fspecialtypemark | 特定业务类型 | varchar | 4 |  | √ | '0' | 特定业务类型,枚举: 1 :成品油发票 2 :稀土发票 3 :机动车发票 4 :农产品收购发票 5 :石脑油发票 6 :卷烟发票 7 :建筑服务发票 8 :货物运输服务发票 9 :不动产销售服务发票 10 :不动产经营租赁服务 11 :代收车船税发票 12 :旅客运输服务发票 13 :自产农产品销售发票 14 :通行费发票 15 :医疗服务（住院）发票 16 :医疗服务（门诊）发票 17 :拖拉机和联合收割机发票 18 :二手车发票 19 :光伏收购发票 20 :出口发票 21 :农产品发票 22 :稀土矿产品发票 23 :稀土产成品发票 24 :铁路电子客票 25 :航空运输电子客票行程单 26 :电子烟 27 :正常开具 28 :反向开具 |
| 48 | fothertotaltaxamount | 其他税费 | numeric | 23 | 10 | √ | 0 | 其他税费 |
| 49 | fnum | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 50 | finsurancepremium | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 51 | fspecmodel | 规格型号 | varchar | 600 |  | √ | ' ' | 规格型号 |
| 52 | finvoicematch | 匹配 | bpchar | 1 |  | √ | '0' | 匹配 |
| 53 | fvalidatemessage | 发票校验结果 | varchar | 255 |  | √ | ' ' | 发票校验结果 |
| 54 | fairconstfee | 民航发展基金 | numeric | 23 | 10 | √ | 0 | 民航发展基金 |
| 55 | finvoicedate | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 56 | finvoicealltaxcode | 税收分类编码 | varchar | 255 |  | √ | ' ' | 税收分类编码 |
| 57 | fregion | 地域 | bpchar | 1 |  |  | null | 地域,枚举: 1 :国内 2 :国际 |
| 58 | fcount | 发票张数 | int8 | 64 |  | √ | 0 | 发票张数 |
| 59 | finvoicenotaxamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 60 | finvexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 61 | finvoicefrom | 发票来源 | varchar | 30 |  | √ | '1' | 发票来源,枚举: 1 :发票云 2 :OCR识别 3 :商旅月结 |
| 62 | fbillcreatetime | 采集时间 | timestamp | 0 |  |  | null | 采集时间 |
| 63 | ffromcity | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 64 | fbuyertaxno | 收票方税号 | varchar | 50 |  | √ | ' ' | 收票方税号 |
| 65 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 66 | finvexpquotetype | 换算方式 | bpchar | 1 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 67 | finvoicetypeid | 发票类型 | int8 | 64 |  | √ | 0 | [发票类型(发票云) er_invoicetype](../basedata_files/er_invoicetype.md) |
| 68 | fmakeoutcompname | 开票公司 | varchar | 250 |  | √ | ' ' | 开票公司 |
| 69 | fflighttrainnums | 航班号/车次 | varchar | 50 |  | √ | ' ' | 航班号/车次 |
| 70 | fnodeductionreason | 不抵扣原因 | varchar | 2 |  | √ | ' ' | 不抵扣原因,枚举: a :用于非应税项目 b :用于免税项目 c :用于集体福利或个人消费 d :遭受非正常损失 e :其他 |
| 71 | fordernum_tag | 匹配结算单号_详情 | text | 0 |  |  | null | 匹配结算单号_详情 |
| 72 | fismapexpense | 关联费用明细 | bpchar | 1 |  | √ | '1' | 关联费用明细,枚举: 1 :是 0 :否 |
| 73 | fcurrtotalamount | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 74 | fpersonalinvoice | 个人发票 | varchar | 30 |  | √ | ' ' | 个人发票,枚举: 1 :是 0 :否 |
| 75 | fendorsement | 签注 | varchar | 255 |  | √ | ' ' | 签注 |
| 76 | finvoicegoodsname | 商品名称 | varchar | 255 |  | √ | ' ' | 商品名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invoicecp_invq |  | finvoiceno,finvoicecode |
| 2 | idx_er_invoiceinfocp_fseq |  | fid |
| 3 | idx_er_invoicecp_query |  | fserialno |
| 4 | t_er_invoiceinfocp_pkey |  | fentryid |

---

## 关联子实体-子表 t_er_checkingpaywrioff_lk

- **表名称：** 关联子实体-子表
- **表名：** t_er_checkingpaywrioff_lk

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
| 1 | pk_t_er_checkingpaywrioff_lk |  | fpkid |
| 2 | t_er_checkingpaywrioff_lk_fid |  | fentryid |

---

## 结算单关联信息-子表 t_er_checkingpayentry

- **表名称：** 结算单关联信息-子表
- **表名：** t_er_checkingpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fserviceitem | 服务项目 | varchar | 10 |  | √ | ' ' | 服务项目,枚举: TICKET :票价 SERVICE :服务费 |
| 3 | finvoicetotalamount | 发票金额 | numeric | 23 | 10 | √ | 0 | 发票金额 |
| 4 | ftaxrate | 税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 税率（%） |
| 5 | fendorsementamount | 改签费 | numeric | 23 | 10 | √ | 0 | 改签费 |
| 6 | fcheckingbillno | 月结账单编号 | varchar | 255 |  | √ | ' ' | 月结账单编号 |
| 7 | farrivetime | 到达时间 | timestamp | 0 |  |  | null | 到达时间 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | frefundamount | 退订费 | numeric | 23 | 10 | √ | 0 | 退订费 |
| 10 | fbusinesstype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 8 :用餐预订 |
| 11 | finvoicenum | finvoicenum | varchar | 255 |  | √ | ' ' |  |
| 12 | ftravelbill | 行程单/火车票 | bpchar | 1 |  | √ | '0' | 行程单/火车票 |
| 13 | frefundamounttax | 退票费税额 | numeric | 23 | 10 | √ | 0 | 退票费税额 |
| 14 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 15 | finvoicetax | 发票税额 | numeric | 23 | 10 | √ | 0 | 发票税额 |
| 16 | fticketnum | 电子客票号/火车票 | varchar | 50 |  | √ | ' ' | 电子客票号/火车票 |
| 17 | foabillnum | 申请单号 | varchar | 255 |  | √ | ' ' | 申请单号 |
| 18 | foperationtype | 服务类型 | bpchar | 1 |  | √ | ' ' | 服务类型,枚举: 1 :酒店预订 2 :机票预订 3 :用车预订 4 :火车预订 5 :用餐预订 |
| 19 | fticketprice | 票价 | numeric | 23 | 10 | √ | 0 | 票价 |
| 20 | finvoicedifferent | 发票金额差异 | numeric | 23 | 10 | √ | 0 | 发票金额差异 |
| 21 | freimbursenum | 报销单号 | varchar | 255 |  | √ | ' ' | 报销单号 |
| 22 | fdeparttime | 出发时间 | timestamp | 0 |  |  | null | 出发时间 |
| 23 | fordertype | 订单类型 | varchar | 50 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 Q :取消单 |
| 24 | fparentordernum | 父订单号 | varchar | 255 |  | √ | ' ' | 父订单号 |
| 25 | ffuelprice | 燃油费 | numeric | 23 | 10 | √ | 0 | 燃油费 |
| 26 | fotheramount | 其他费用 | numeric | 23 | 10 | √ | 0 | 其他费用 |
| 27 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0.0000000000 | 税额 |
| 28 | ffromcity | 出发地 | varchar | 50 |  | √ | ' ' | 出发地 |
| 29 | flargeinvoicenum_tag | 发票号码_详情 | text | 0 |  | √ | ' ' | 发票号码_详情 |
| 30 | factentryamount | 结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额 |
| 31 | fmatch | 已匹配 | bpchar | 1 |  | √ | '0' | 已匹配 |
| 32 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 33 | fdept | 部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | fserviceamounttax | 服务费税额 | numeric | 23 | 10 | √ | 0 | 服务费税额 |
| 35 | fuserid | 人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fcheckingbillid | 结算单id | int8 | 64 |  | √ | 0 | 结算单id |
| 37 | fnotaxoriamount | 不含税金额 | numeric | 23 | 10 | √ | 0.0000000000 | 不含税金额 |
| 38 | fisuploadinvoicecloud | 上传发票云 | bpchar | 1 |  | √ | '0' | 上传发票云 |
| 39 | finvoicetaxdifferent | 发票税额差异 | numeric | 23 | 10 | √ | 0 | 发票税额差异 |
| 40 | flargeinvoicenum | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |
| 41 | ftocity | 目的地 | varchar | 50 |  | √ | ' ' | 目的地 |
| 42 | fvendorname | 车次 | varchar | 50 |  | √ | ' ' | 车次 |
| 43 | fairportprice | 民航发展基金 | numeric | 23 | 10 | √ | 0 | 民航发展基金 |
| 44 | fassuranceamount | 保险费 | numeric | 23 | 10 | √ | 0 | 保险费 |
| 45 | forderamounttax | 票价税额 | numeric | 23 | 10 | √ | 0 | 票价税额 |
| 46 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 47 | fcheckingbillnum | 结算单号 | varchar | 100 |  | √ | ' ' | 结算单号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_checkingpayentry_pkey |  | fentryid |
| 2 | idx_er_checkingpayentry_id |  | fid |
