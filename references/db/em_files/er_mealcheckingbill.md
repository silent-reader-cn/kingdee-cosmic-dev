# 用餐结算单-er_mealcheckingbill

## 用餐结算单-多语言表 t_er_mealcheckingbill_l

- **表名称：** 用餐结算单-多语言表
- **表名：** t_er_mealcheckingbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbalanceremark | 置平备注 | varchar | 1000 |  | √ | ' ' | 置平备注 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_mealcheckingbill_l |  | fid,flocaleid |
| 2 | pk_t_er_mealcheckingbill_l |  | fpkid |

---

## 用餐结算单-主表 t_er_mealcheckingbill

- **表名称：** 用餐结算单-主表
- **表名：** t_er_mealcheckingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 预订人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftotalamount | 结算金额 | numeric | 23 | 10 | √ | 0 | 结算金额 |
| 4 | fordernum | 结算单号 | varchar | 80 |  | √ | ' ' | 结算单号 |
| 5 | fisbalance | 是否对平 | bpchar | 1 |  | √ | '0' | 是否对平,枚举: 1 :平 2 :不平 3 :废弃 |
| 6 | fmealcityname | 用餐城市 | varchar | 255 |  | √ | ' ' | 用餐城市 |
| 7 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 8 | fpaybillstatus | 付款状态 | bpchar | 1 |  | √ | ' ' | 付款状态,枚举: 0 :等待付款 1 :已付款 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fservicedeductrate | 服务费税率(%) | numeric | 23 | 10 | √ | 0 | 服务费税率(%) |
| 11 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 12 | foperationtype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 8 :用餐 |
| 13 | fserver | 服务商 | varchar | 50 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 MEITUAN :美团商企通 |
| 14 | freimbursenum | freimbursenum | varchar | 80 |  | √ | ' ' |  |
| 15 | forderstatus | 订单状态 | varchar | 50 |  | √ | ' ' | 订单状态,枚举: PAY :已支付 PART_REFUND :部分退款 ALL_REFUND :全额退款 9999 :未知 |
| 16 | ftotaltaxrate | 可抵扣税率 | numeric | 23 | 10 | √ | 0 | 可抵扣税率 |
| 17 | fordertype | 订单类型 | varchar | 50 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 18 | fparentordernum | 父订单号 | varchar | 50 |  | √ | ' ' | 父订单号 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0 | 个人支付金额 |
| 21 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :未审核 C :已审核 |
| 22 | fbatchno | 结算批次号 | varchar | 80 |  | √ | ' ' | 结算批次号 |
| 23 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 24 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 25 | fpushcount | 下推计数 | int4 | 32 |  | √ | 0 | 下推计数 |
| 26 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 29 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | ' ' | 报销状态,枚举: A :未报销 B :报销中 C :已付款 |
| 30 | fsourcebookedid | 预订人工号 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | fperiod | 期间 | varchar | 50 |  | √ | ' ' | 期间 |
| 32 | fhappenddate | 结算发生时间 | timestamp | 0 |  |  | null | 结算发生时间 |
| 33 | fshopaddress | 店铺地址 | varchar | 255 |  | √ | ' ' | 店铺地址 |
| 34 | fisvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 35 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国际 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | faccountid | 主账户ID | varchar | 50 |  | √ | ' ' | 主账户ID |
| 38 | fcompanyid | 预订人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | fbillperiod | 差旅壹号账期 | timestamp | 0 |  |  | null | 差旅壹号账期 |
| 40 | fsettlementamount | 结算金额 | numeric | 23 | 10 | √ | 0 | 结算金额 |
| 41 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0 | 服务费 |
| 42 | forderdeductrate | 票价税率(%) | numeric | 23 | 10 | √ | 0 | 票价税率(%) |
| 43 | fpaybillnum | 付款/付款申请单号 | varchar | 80 |  | √ | ' ' | 付款/付款申请单号 |
| 44 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 er_mealapplication_bill :用餐申请单 |
| 45 | ftotaltax | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |
| 46 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 47 | fisreconciliation | 是否对账 | bpchar | 1 |  | √ | '0' | 是否对账 |
| 48 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 49 | fhasinvoice | 是否已开票 | bpchar | 1 |  | √ | '0' | 是否已开票,枚举: 1 :是 0 :否 2 :开票中 |
| 50 | fshopname | 店铺名称 | varchar | 255 |  | √ | ' ' | 店铺名称 |
| 51 | fmealtime | 用餐日期 | timestamp | 0 |  |  | null | 用餐日期 |
| 52 | fformid | 表单ID | varchar | 50 |  | √ | ' ' | 表单ID |
| 53 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 54 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 55 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 56 | fserviceamounttax | 服务费税额 | numeric | 23 | 10 | √ | 0 | 服务费税额 |
| 57 | fpaybillid | 付款/付款申请单id | int8 | 64 |  | √ | 0 | 付款/付款申请单id |
| 58 | fproducttype | 结算类型 | varchar | 50 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 59 | fbookedname | 预订人 | varchar | 50 |  | √ | ' ' | 预订人 |
| 60 | fsettlemain | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 61 | fisbusiness | 订单性质 | varchar | 50 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 62 | fallorderbaseid | 订单总表数据 | int8 | 64 |  | √ | 0 | 全部订单 er_allorderbill |
| 63 | fdinnerscene | 用餐场景 | varchar | 50 |  | √ | ' ' | 用餐场景,枚举: 1 :商务宴请 3 :差旅用餐 5 :团建用餐 4 :工作用餐 6 :招待用餐 7 :会议用餐 9 :福利用餐 |
| 64 | fsettledept | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 65 | fbalanceremark | 置平备注 | varchar | 500 |  | √ | ' ' | 置平备注 |
| 66 | forderamounttax | 票价税额 | numeric | 23 | 10 | √ | 0 | 票价税额 |
| 67 | forderisinvoicerep | 是否需要开票 | bpchar | 1 |  | √ | '0' | 是否需要开票 |
| 68 | fcheckingbillnum | 账单编码 | varchar | 80 |  | √ | ' ' | 账单编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_mealcheckingbill_billno |  | fordernum,fserver |
| 2 | pk_t_er_mealcheckingbill |  | fid |
| 3 | idx_er_mealcheckingbill_org |  | fcompanyid,fsettlemain |
