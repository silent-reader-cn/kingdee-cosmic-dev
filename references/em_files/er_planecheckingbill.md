# 机票结算单-er_planecheckingbill

## 机票结算单-主表 t_er_planecheckingbill

- **表名称：** 机票结算单-主表
- **表名：** t_er_planecheckingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalamount | 结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额 |
| 3 | forgid | 申请人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | forderid | forderid | int8 | 64 |  | √ | 0 |  |
| 5 | fordernum | 结算单号 | varchar | 80 |  | √ | ' ' | 结算单号 |
| 6 | ftravelername | 乘机人 | varchar | 100 |  | √ | ' ' | 乘机人 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fservicedeductrate | 服务费税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税率(%) |
| 9 | forderstatus | 订单状态 | varchar | 30 |  | √ | ' ' | 订单状态,枚举: 20000 :已预订 40000 :已出票 31000 :取消中 30000 :已取消 50201 :退票中 50202 :已退票 50301 :改签中 50302 :已改签 USED :已乘机 9999 :未知 |
| 10 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 11 | fticketstatus | 使用状态 | varchar | 100 |  | √ | ' ' | 使用状态,枚举: UNUSED :未使用 USED :已使用 REFOUND :已退票 CHANGED :已改签 |
| 12 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 13 | fpushcount | 下推计数 | int8 | 64 |  | √ | 0 | 下推计数 |
| 14 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 15 | fdiscount | 折扣（%） | numeric | 23 | 10 | √ | 0.0000000000 | 折扣（%） |
| 16 | forderserver | forderserver | varchar | 30 |  | √ | ' ' |  |
| 17 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | 'A' | 报销状态,枚举: A :未报销 B :报销中 C :已付款 |
| 18 | fkddownloadlink | 内部下载地址 | varchar | 500 |  | √ | ' ' | 内部下载地址 |
| 19 | fperiod | 期间 | varchar | 30 |  | √ | ' ' | 期间 |
| 20 | fhappenddate | 结算发生时间 | timestamp | 0 |  |  | null | 结算发生时间 |
| 21 | fassuranceamount | 保险费 | numeric | 23 | 10 | √ | 0.0000000000 | 保险费 |
| 22 | fisvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | faccountid | 主账户ID | varchar | 30 |  | √ | ' ' | 主账户ID |
| 25 | fbillperiod | 差旅壹号账期 | timestamp | 0 |  |  | null | 差旅壹号账期 |
| 26 | fendorsementamount | 改签费 | numeric | 23 | 10 | √ | 0.0000000000 | 改签费 |
| 27 | flandingtime | 到达时间 | timestamp | 0 |  |  | null | 到达时间 |
| 28 | frefundamount | 退票费 | numeric | 23 | 10 | √ | 0.0000000000 | 退票费 |
| 29 | fitinerarydate | 填开日期 | timestamp | 0 |  |  | null | 填开日期 |
| 30 | ftakeofftime | 出发时间 | timestamp | 0 |  |  | null | 出发时间 |
| 31 | fpaybillnum | 付款/付款申请单号 | varchar | 80 |  | √ | ' ' | 付款/付款申请单号 |
| 32 | forderdeductrate | 票价税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 票价税率(%) |
| 33 | fairlinename | 航空公司名称 | varchar | 100 |  | √ | ' ' | 航空公司名称 |
| 34 | fordertotalamount | fordertotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 35 | fticketnum | 电子客票号 | varchar | 80 |  | √ | ' ' | 电子客票号 |
| 36 | fisreconciliation | 是否对账 | bpchar | 1 |  | √ | ' ' | 是否对账 |
| 37 | finvoiceidentityflag | 是否发票识别成功 | varchar | 1 |  | √ | 0 | 是否发票识别成功 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | ffuelprice | 燃油费 | numeric | 23 | 10 | √ | 0.0000000000 | 燃油费 |
| 40 | kddownloadlink | kddownloadlink | varchar | 2000 |  | √ | ' ' |  |
| 41 | fpromotion | 促销 | numeric | 23 | 10 | √ | 0.0000000000 | 促销 |
| 42 | fotheramount | 其他费用 | numeric | 23 | 10 | √ | 0 | 其他费用 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fcabinclass | 舱位等级 | varchar | 100 |  | √ | ' ' | 舱位等级 |
| 46 | fserviceamounttax | 服务费税额 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税额 |
| 47 | fbookedname | 预订人姓名 | varchar | 100 |  | √ | ' ' | 预订人姓名 |
| 48 | fproducttype | 结算类型 | bpchar | 1 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 |
| 49 | fisbusiness | 订单性质 | bpchar | 1 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 50 | fallorderbaseid | 订单总表数据 | int8 | 64 |  | √ | 0 | 全部订单 er_allorderbill |
| 51 | fsettledept | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 52 | fbalanceremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 53 | forderamounttax | 票价税额 | numeric | 23 | 10 | √ | 0.0000000000 | 票价税额 |
| 54 | fcheckingbillnum | 账单编码 | varchar | 100 |  | √ | ' ' | 账单编码 |
| 55 | forderordernum | forderordernum | varchar | 80 |  | √ | ' ' |  |
| 56 | frebate | 返点 | numeric | 23 | 10 | √ | 0.0000000000 | 返点 |
| 57 | fisbalance | 是否对平 | bpchar | 1 |  | √ | '2' | 是否对平,枚举: 1 :平 2 :不平 3 :废弃 |
| 58 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 59 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 60 | fpaybillstatus | 付款状态 | varchar | 100 |  | √ | ' ' | 付款状态,枚举: 0 :等待付款 1 :已付款 |
| 61 | fsettlemainname | fsettlemainname | varchar | 100 |  | √ | ' ' |  |
| 62 | foperationtype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 |
| 63 | fserver | 服务商 | varchar | 100 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 |
| 64 | forderformid | forderformid | varchar | 30 |  | √ | ' ' |  |
| 65 | fitinerarynum | 行程单号 | varchar | 100 |  | √ | ' ' | 行程单号 |
| 66 | fparentordernum | 父订单号 | varchar | 100 |  | √ | ' ' | 父订单号 |
| 67 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0 | 个人支付金额 |
| 68 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :未审核 C :已审核 |
| 69 | fbatchno | 结算批次号 | varchar | 100 |  | √ | ' ' | 结算批次号 |
| 70 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 71 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 72 | fserialno | 发票流水号 | varchar | 255 |  | √ | ' ' | 发票流水号 |
| 73 | ffromcityname | 出发城市名称 | varchar | 100 |  | √ | ' ' | 出发城市名称 |
| 74 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 75 | fflightno | 航班号 | varchar | 80 |  | √ | ' ' | 航班号 |
| 76 | fdownloadlink | 下载地址 | varchar | 255 |  | √ | ' ' | 下载地址 |
| 77 | ftocityname | 到达城市名称 | varchar | 100 |  | √ | ' ' | 到达城市名称 |
| 78 | fsourcebookedid | 预订人工号 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 79 | fairportprice | 机场基建费 | numeric | 23 | 10 | √ | 0.0000000000 | 机场基建费 |
| 80 | ftax | 税费 | numeric | 23 | 10 | √ | 0.0000000000 | 税费 |
| 81 | fidentityerrormsg | 发票识别异常信息 | varchar | 500 |  | √ | ' ' | 发票识别异常信息 |
| 82 | fproductsontype | 产品子类型 | varchar | 100 |  | √ | ' ' | 产品子类型,枚举: 1 :两方协议产品 2 :三方协议产品 3 :官网 4 :B2G 5 :B2T 6 :代理渠道 7 :公务员 8 :飞行达人 9 :单体协议酒店托管 10 :集团协议酒店托管 11 :会员酒店 |
| 83 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国外 |
| 84 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 85 | fsettlementamount | 结算金额（核算） | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额（核算） |
| 86 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 87 | fsourcetravelerid | 乘机人工号 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 88 | ftotaltax | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 89 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 90 | fticketprice | 机票价格 | numeric | 19 |  | √ | 0 | 机票价格 |
| 91 | fhasinvoice | 是否已开票 | bpchar | 1 |  | √ | '0' | 是否已开票,枚举: 1 :是 0 :否 2 :开票中 |
| 92 | fformid | 表单ID | varchar | 100 |  | √ | ' ' | 表单ID |
| 93 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 94 | fpaybillid | 付款/付款申请单id | int8 | 64 |  | √ | 0 | 付款/付款申请单id |
| 95 | fcabin | 舱位 | varchar | 100 |  | √ | ' ' | 舱位 |
| 96 | fsettlemain | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 97 | fsubbatchno | 结算子批次号 | varchar | 100 |  | √ | ' ' | 结算子批次号 |
| 98 | fbillstatusname | 结算确认状态 | varchar | 5 |  | √ | ' ' | 结算确认状态,枚举: 1 :待确认 2 :已确认 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_planecheck_paybillid |  | fpaybillid |
| 2 | idx_er_pcbill_org |  | fsettlemain,fcompanyid |
| 3 | t_er_planecheckingbill_pkey |  | fid |
| 4 | idx_er_planecheckbill_fbillno |  | fbillno |

---

## 机票结算单-多语言表 t_er_planecheckingbill_l

- **表名称：** 机票结算单-多语言表
- **表名：** t_er_planecheckingbill_l

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
| 1 | t_er_planecheckingbill_l_pkey |  | fpkid |
| 2 | idx_er_plckbill_l_fid_lcid |  | fid,flocaleid |

---

## 机票结算单-分表 t_er_planecheckingbill_a

- **表名称：** 机票结算单-分表
- **表名：** t_er_planecheckingbill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 3 | fislowestpirce | 是否最低价 | bpchar | 1 |  | √ | ' ' | 是否最低价 |
| 4 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 5 | flowestpirce | 最低价格 | numeric | 23 | 10 | √ | 0.0000000000 | 最低价格 |
| 6 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_planecheckingbill_a |  | fid |
| 2 | idx_er_planecb_a_flowe |  | fislowestpirce |
