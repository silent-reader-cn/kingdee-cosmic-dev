# 酒店结算单-er_hotelcheckingbill

## 酒店结算单-多语言表 t_er_hotelcheckingbill_l

- **表名称：** 酒店结算单-多语言表
- **表名：** t_er_hotelcheckingbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbalanceremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_htckgbill_l_id_lcid |  | fid,flocaleid |
| 2 | t_er_hotelcheckingbill_l_pkey |  | fpkid |

---

## 酒店结算单-主表 t_er_hotelcheckingbill

- **表名称：** 酒店结算单-主表
- **表名：** t_er_hotelcheckingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forderordernum | forderordernum | varchar | 80 |  | √ | ' ' |  |
| 3 | frefunddeductrate | 退票费税率(%) | numeric | 23 | 10 | √ | 0 | 退票费税率(%) |
| 4 | ftotalamount | 结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额 |
| 5 | forgid | 申请人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | forderid | forderid | int8 | 64 |  | √ | 0 |  |
| 7 | fordernum | 结算单号 | varchar | 80 |  | √ | ' ' | 结算单号 |
| 8 | frebate | 返点 | numeric | 23 | 10 | √ | 0.0000000000 | 返点 |
| 9 | fisbalance | 已对平 | bpchar | 1 |  | √ | '2' | 已对平,枚举: 1 :平 2 :不平 3 :废弃 |
| 10 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 11 | ftravelername | 入住人 | varchar | 100 |  | √ | ' ' | 入住人 |
| 12 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 13 | fpaybillstatus | 付款状态 | varchar | 100 |  | √ | ' ' | 付款状态,枚举: 0 :等待付款 1 :已付款 |
| 14 | frefundamounttax | 退票费税额 | numeric | 23 | 10 | √ | 0 | 退票费税额 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fservicedeductrate | 服务费税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税率(%) |
| 17 | fsettlemainname | fsettlemainname | varchar | 100 |  | √ | ' ' |  |
| 18 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 19 | foperationtype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 |
| 20 | fserver | 服务商 | varchar | 100 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 |
| 21 | forderstatus | 订单状态 | varchar | 100 |  | √ | ' ' | 订单状态,枚举: 1 :待审批 2 :待支付 3 :待确认 5 :已确认 6 :满房 7 :已离店 8 :待退订 10 :已退订 14 :已取消 9999 :未知 |
| 22 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 23 | forderformid | forderformid | varchar | 30 |  | √ | ' ' |  |
| 24 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 25 | fparentordernum | 父订单号 | varchar | 100 |  | √ | ' ' | 父订单号 |
| 26 | fhotelname | 酒店名称 | varchar | 100 |  | √ | ' ' | 酒店名称 |
| 27 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 28 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 个人支付金额 |
| 29 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 30 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :未审核 C :已审核 |
| 31 | fbatchno | 结算批次号 | varchar | 100 |  | √ | ' ' | 结算批次号 |
| 32 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 33 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 34 | fpushcount | 下推计数 | int8 | 64 |  | √ | 0 | 下推计数 |
| 35 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 36 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 37 | forderserver | forderserver | varchar | 30 |  | √ | ' ' |  |
| 38 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 39 | fcheckoutdate | 离店日期 | timestamp | 0 |  |  | null | 离店日期 |
| 40 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | 'A' | 报销状态,枚举: A :未报销 B :报销中 C :已付款/已完成 |
| 41 | fsourcebookedid | 预订人工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | froomcount | 订房间数 | int8 | 64 |  | √ | 0 | 订房间数 |
| 43 | fproductsontype | 产品子类型 | varchar | 100 |  | √ | ' ' | 产品子类型,枚举: 1 :两方协议产品 2 :三方协议产品 3 :官网 4 :B2G 5 :B2T 6 :代理渠道 7 :公务员 8 :飞行达人 9 :单体协议酒店托管 10 :集团协议酒店托管 11 :会员酒店 |
| 44 | funbookfee | 退订费 | numeric | 23 | 10 | √ | 0.0000000000 | 退订费 |
| 45 | fperiod | 期间 | varchar | 30 |  | √ | ' ' | 期间 |
| 46 | fhappenddate | 结算发生日期 | timestamp | 0 |  |  | null | 结算发生日期 |
| 47 | froomamount | 房价 | numeric | 23 | 10 | √ | 0.0000000000 | 房价 |
| 48 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 49 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国际 |
| 50 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 51 | faccountid | 主账户ID | varchar | 30 |  | √ | ' ' | 主账户ID |
| 52 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | fbillperiod | 差旅壹号账期 | timestamp | 0 |  |  | null | 差旅壹号账期 |
| 54 | foutaccountid | 商旅方系统拆账id | varchar | 255 |  | √ | ' ' | 商旅方系统拆账id |
| 55 | fsettlementamount | 结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额 |
| 56 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 57 | froomstylename | 房型 | varchar | 255 |  | √ | ' ' | 房型 |
| 58 | fcityname | 城市 | varchar | 100 |  | √ | ' ' | 城市 |
| 59 | fsourcetravelerid | 入住人工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 60 | fpaybillnum | 付款/付款申请单号 | varchar | 80 |  | √ | ' ' | 付款/付款申请单号 |
| 61 | forderdeductrate | 票价税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 票价税率(%) |
| 62 | fordertotalamount | fordertotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 63 | fpricebillingtype | 票价开票类型 | varchar | 10 |  | √ | ' ' | 票价开票类型,枚举: 2 :增值税专用发票 1 :增值税普通发票 9999 :未知 |
| 64 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 |
| 65 | ftotaltax | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 66 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 67 | fisreconciliation | 已对账 | bpchar | 1 |  | √ | '0' | 已对账 |
| 68 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 69 | fhasinvoice | 已开票 | bpchar | 1 |  | √ | '0' | 已开票,枚举: 1 :是 0 :否 2 :开票中 |
| 70 | fpromotion | 促销 | numeric | 23 | 10 | √ | 0.0000000000 | 促销 |
| 71 | fformid | 表单ID | varchar | 100 |  | √ | ' ' | 表单ID |
| 72 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 73 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 74 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 75 | fserviceamounttax | 服务费税额 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税额 |
| 76 | fpaybillid | 付款/付款申请单id | int8 | 64 |  | √ | 0 | 付款/付款申请单id |
| 77 | fbookedname | 预订人姓名 | varchar | 100 |  | √ | ' ' | 预订人姓名 |
| 78 | fproducttype | 结算类型 | bpchar | 1 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 |
| 79 | fsettlemain | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 80 | fisbusiness | 订单性质 | bpchar | 1 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 81 | fsubbatchno | 结算子批次号 | varchar | 100 |  | √ | ' ' | 结算子批次号 |
| 82 | fcheckindate | 入住日期 | timestamp | 0 |  |  | null | 入住日期 |
| 83 | fallorderbaseid | 订单总表数据 | int8 | 64 |  | √ | 0 | [全部订单 er_allorderbill](../em_files/er_allorderbill.md) |
| 84 | fsettledept | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 85 | fbalanceremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 86 | forderamounttax | 票价税额 | numeric | 23 | 10 | √ | 0.0000000000 | 票价税额 |
| 87 | foutsettlementnum | 外部系统结算单号 | varchar | 255 |  | √ | ' ' | 外部系统结算单号 |
| 88 | fcheckingbillnum | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_hotelcheckingbill_pkey |  | fid |
| 2 | idx_er_hcbill_org |  | fsettlemain,fcompanyid |
| 3 | idx_er_hotelchbill_no |  | fbillno |
| 4 | idx_er_hotelcheck_paybillid |  | fpaybillid |
