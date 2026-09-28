# 用车结算单-er_vehiclecheckingbill

## 用车结算单-多语言表 t_er_vehiclecheckingbill_l

- **表名称：** 用车结算单-多语言表
- **表名：** t_er_vehiclecheckingbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbalanceremark | 置平备注 | varchar | 1000 |  | √ | ' ' | 置平备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_vehiclecheckingbill_l_pkey |  | fpkid |
| 2 | idx_er_vcb_l_fid |  | fid,flocaleid |

---

## 用车结算单-分表 t_er_vehiclecheckingbill_a

- **表名称：** 用车结算单-分表
- **表名：** t_er_vehiclecheckingbill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 个人支付金额 |
| 4 | fsettlementamount | 结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额 |
| 5 | fbatchno | 结算批次号 | varchar | 100 |  | √ | ' ' | 结算批次号 |
| 6 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 7 | fserviceamounttax | 服务费税额 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税额 |
| 8 | forderdeductrate | 票价税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 票价税率(%) |
| 9 | fpaybillstatus | 付款状态 | varchar | 100 |  | √ | ' ' | 付款状态,枚举: 0 :等待付款 1 :已付款 |
| 10 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 11 | fservicedeductrate | 服务费税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税率(%) |
| 12 | ftravelways | 出行方式 | varchar | 30 |  | √ | ' ' | 出行方式 |
| 13 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 14 | ftotaltax | ftotaltax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fallorderbaseid | 订单总表数据 | int8 | 64 |  | √ | 0 | 全部订单 er_allorderbill |
| 16 | fvendorname | 供应商名称 | varchar | 30 |  | √ | ' ' | 供应商名称 |
| 17 | fperiod | 期间 | varchar | 30 |  | √ | ' ' | 期间 |
| 18 | fhasinvoice | 是否已开票 | bpchar | 1 |  | √ | '0' | 是否已开票,枚举: 1 :是 0 :否 2 :开票中 |
| 19 | forderamounttax | 票价税额 | numeric | 23 | 10 | √ | 0.0000000000 | 票价税额 |
| 20 | fparentordernum | 父订单号 | varchar | 100 |  | √ | ' ' | 父订单号 |
| 21 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国际 |
| 22 | fbillperiod | 差旅壹号账期 | timestamp | 0 |  |  | null | 差旅壹号账期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_vehckb_a_alordid |  | fallorderbaseid |
| 2 | t_er_vehiclecheckingbill_a_pkey |  | fid |

---

## 用车结算单-主表 t_er_vehiclecheckingbill

- **表名称：** 用车结算单-主表
- **表名：** t_er_vehiclecheckingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forderordernum | forderordernum | varchar | 80 |  | √ | ' ' |  |
| 3 | forgid | 申请人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftotalamount | 结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额 |
| 5 | forderid | forderid | int8 | 64 |  | √ | 0 |  |
| 6 | fordernum | 结算单号 | varchar | 80 |  | √ | ' ' | 结算单号 |
| 7 | fisbalance | 是否对平 | bpchar | 1 |  | √ | '2' | 是否对平,枚举: 1 :平 2 :不平 3 :废弃 |
| 8 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | foperationtype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 |
| 11 | fserver | 服务商 | varchar | 30 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 GAODE :高德 |
| 12 | fservicebegintime | 服务开始时间 | timestamp | 0 |  |  | null | 服务开始时间 |
| 13 | forderstatus | 订单状态 | varchar | 30 |  | √ | ' ' | 订单状态,枚举: WaitReply :等待应答 WaitService :等待接驾 InService :正在服务 EndService :行程结束 Canceling :取消中 Canceled :已取消 WaitPay :待支付 Successful :已成交 Refunded :已退款 PartialRefund :部分退款 9999 :未知 |
| 14 | fpassegerid | 乘客 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | farriveaddress | 下车地址 | varchar | 255 |  | √ | ' ' | 下车地址 |
| 16 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 17 | forderformid | forderformid | varchar | 80 |  | √ | ' ' |  |
| 18 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 19 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :未审核 C :已审核 |
| 20 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 21 | fpushcount | 下推计数 | int8 | 64 |  | √ | 0 | 下推计数 |
| 22 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | forderserver | forderserver | varchar | 30 |  | √ | ' ' |  |
| 25 | fdistance | 公里数 | varchar | 50 |  | √ | ' ' | 公里数 |
| 26 | fvehicletype | 用车类型 | varchar | 50 |  | √ | ' ' | 用车类型,枚举: 1 :差旅用车 2 :公务出行用车 3 :工作日加班用车 4 :周末/节假日加班用车 6 :招待用车 7 :会议用车 |
| 27 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 28 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | 'A' | 报销状态,枚举: A :未报销 B :报销中 C :已付款 |
| 29 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fhappenddate | 结算发生日期 | timestamp | 0 |  |  | null | 结算发生日期 |
| 31 | fisvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | faccountid | 主账户ID | varchar | 30 |  | √ | ' ' | 主账户ID |
| 34 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fdepartaddress | 上车地址 | varchar | 255 |  | √ | ' ' | 上车地址 |
| 36 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 37 | fcityname | 城市名称 | varchar | 100 |  | √ | ' ' | 城市名称 |
| 38 | fpaybillnum | 付款/付款申请单号 | varchar | 80 |  | √ | ' ' | 付款/付款申请单号 |
| 39 | fserviceendtime | 服务结束时间 | timestamp | 0 |  |  | null | 服务结束时间 |
| 40 | fpassegername | 乘客姓名 | varchar | 30 |  | √ | ' ' | 乘客姓名 |
| 41 | fordertotalamount | fordertotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fpricebillingtype | 票价开票类型 | varchar | 10 |  | √ | ' ' | 票价开票类型,枚举: 2 :增值税专用发票 1 :增值税普通发票 9999 :未知 |
| 43 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 er_dailyvehiclebill :用车申请单 |
| 44 | ftotaltax | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 45 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 46 | fisreconciliation | 是否对账 | bpchar | 1 |  | √ | ' ' | 是否对账 |
| 47 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 48 | fdealamount | 实付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实付金额 |
| 49 | fusetime | 用车时间 | timestamp | 0 |  |  | null | 用车时间 |
| 50 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID |
| 51 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 52 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 53 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 54 | fpaybillid | 付款/付款申请单id | int8 | 64 |  | √ | 0 | 付款/付款申请单id |
| 55 | fpushcheckingexplist | 是否生成部门清单 | bpchar | 1 |  | √ | '0' | 是否生成部门清单 |
| 56 | fproducttype | 结算类型 | bpchar | 1 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 |
| 57 | fbookedname | 预订人姓名 | varchar | 100 |  | √ | ' ' | 预订人姓名 |
| 58 | fsettlemain | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 59 | fisbusiness | 订单性质 | bpchar | 1 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 60 | fsubbatchno | 结算子批次号 | varchar | 100 |  | √ | ' ' | 结算子批次号 |
| 61 | fsettledept | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 62 | fbalanceremark | 置平备注 | varchar | 1000 |  | √ | ' ' | 置平备注 |
| 63 | fbillstatusname | 结算确认状态 | varchar | 30 |  | √ | ' ' | 结算确认状态,枚举: 1 :待确认 2 :已确认 |
| 64 | fcheckingbillnum | 账单编码 | varchar | 80 |  | √ | ' ' | 账单编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_vcb_billno |  | fordernum,fserver |
| 2 | idx_er_vehiclecheck_paybillid |  | fpaybillid |
| 3 | t_er_vehiclecheckingbill_pkey |  | fid |
| 4 | idx_er_vcbill_org |  | fcompanyid,fsettlemain |
