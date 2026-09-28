# 火车结算单-er_traincheckingbill

## 火车结算单-分表 t_er_traincheckingbill_a

- **表名称：** 火车结算单-分表
- **表名：** t_er_traincheckingbill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsettlementamount | 结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额 |
| 3 | fdepartaddress | 出发车站 | varchar | 255 |  | √ | ' ' | 出发车站 |
| 4 | farrivetime | 到达时间 | timestamp | 0 |  |  | null | 到达时间 |
| 5 | frefundamount | 退票费 | numeric | 23 | 10 | √ | 0.0000000000 | 退票费 |
| 6 | forderdeductrate | 票价税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 票价税率(%) |
| 7 | fpaybillstatus | 付款状态 | varchar | 100 |  | √ | ' ' | 付款状态,枚举: 0 :等待付款 1 :已付款 |
| 8 | fservicedeductrate | 服务费税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税率(%) |
| 9 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 10 | ftotaltax | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 11 | farrivecity | 到达城市 | varchar | 255 |  | √ | ' ' | 到达城市 |
| 12 | fticketprice | 火车票价 | numeric | 23 | 10 | √ | 0.0000000000 | 火车票价 |
| 13 | fdeparttime | 出发时间 | timestamp | 0 |  |  | null | 出发时间 |
| 14 | farriveaddress | 到达车站 | varchar | 255 |  | √ | ' ' | 到达车站 |
| 15 | fhasinvoice | 是否已开票 | bpchar | 1 |  | √ | '0' | 是否已开票,枚举: 1 :是 0 :否 2 :开票中 |
| 16 | fparentordernum | 父订单号 | varchar | 100 |  | √ | ' ' | 父订单号 |
| 17 | ftrainseat | 席位 | varchar | 30 |  | √ | ' ' | 席位,枚举: 1 :硬卧 2 :软卧 3 :无座 4 :硬座 5 :动卧 6 :高级软卧 7 :一等卧 8 :二等卧 9 :软座 A :特等座 B :商务座 C :一等座 D :二等座 E :其他 |
| 18 | fbatchno | 结算批次号 | varchar | 100 |  | √ | ' ' | 结算批次号 |
| 19 | fserviceamounttax | 服务费税额 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税额 |
| 20 | fdepartcity | 出发城市 | varchar | 255 |  | √ | ' ' | 出发城市 |
| 21 | fallorderbaseid | 订单总表数据 | int8 | 64 |  | √ | 0 | 全部订单 er_allorderbill |
| 22 | fvendorname | 车次 | varchar | 30 |  | √ | ' ' | 车次 |
| 23 | fperiod | 期间 | varchar | 30 |  | √ | ' ' | 期间 |
| 24 | fassuranceamount | 保险费 | numeric | 23 | 10 | √ | 0.0000000000 | 保险费 |
| 25 | forderamounttax | 票价税额 | numeric | 23 | 10 | √ | 0.0000000000 | 票价税额 |
| 26 | fbillperiod | 差旅壹号账期 | timestamp | 0 |  |  | null | 差旅壹号账期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_traincheckingbill_a_pkey |  | fid |
| 2 | idx_er_train_a_alordid |  | fallorderbaseid |

---

## 火车结算单-多语言表 t_er_traincheckingbill_l

- **表名称：** 火车结算单-多语言表
- **表名：** t_er_traincheckingbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 3 | fbalanceremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_trainbill_l_id |  | fid,flocaleid |
| 2 | t_er_traincheckingbill_l_pkey |  | fpkid |

---

## 火车结算单-主表 t_er_traincheckingbill

- **表名称：** 火车结算单-主表
- **表名：** t_er_traincheckingbill

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
| 11 | fserver | 服务商 | varchar | 30 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 |
| 12 | forderstatus | 订单状态 | varchar | 30 |  | √ | ' ' | 订单状态,枚举: 1 :已出票 2 :已改签 3 :已退票 4 :出票失败 5 :出票失败退款 6 :改签中 7 :退票中 9999 :未知 |
| 13 | fpassegerid | 乘客 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 15 | forderformid | forderformid | varchar | 80 |  | √ | ' ' |  |
| 16 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 17 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 个人支付金额 |
| 18 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :未审核 C :已审核 |
| 19 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 20 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 21 | fserialno | 发票流水号 | varchar | 255 |  | √ | ' ' | 发票流水号 |
| 22 | fpushcount | 下推计数 | int8 | 64 |  | √ | 0 | 下推计数 |
| 23 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | forderserver | forderserver | varchar | 30 |  | √ | ' ' |  |
| 26 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 27 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | 'A' | 报销状态,枚举: A :未报销 B :报销中 C :已付款 |
| 28 | fdownloadlink | 下载地址 | varchar | 500 |  | √ | ' ' | 下载地址 |
| 29 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | fkddownloadlink | 内部下载地址 | varchar | 500 |  | √ | ' ' | 内部下载地址 |
| 31 | fidentityerrormsg | 发票识别异常信息 | varchar | 500 |  | √ | ' ' | 发票识别异常信息 |
| 32 | fhappenddate | 结算发生时间 | timestamp | 0 |  |  | null | 结算发生时间 |
| 33 | fisvoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 34 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国际 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | faccountid | 主账户ID | varchar | 30 |  | √ | ' ' | 主账户ID |
| 37 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 39 | fpaybillnum | 付款/付款申请单号 | varchar | 80 |  | √ | ' ' | 付款/付款申请单号 |
| 40 | fpassegername | 乘客姓名 | varchar | 100 |  | √ | ' ' | 乘客姓名 |
| 41 | fordertotalamount | fordertotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 |
| 43 | ftotaltax | ftotaltax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 44 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 45 | fisreconciliation | 是否对账 | bpchar | 1 |  | √ | ' ' | 是否对账 |
| 46 | finvoiceidentityflag | 是否发票识别成功 | varchar | 1 |  | √ | 0 | 是否发票识别成功 |
| 47 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 48 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 51 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 52 | fpaybillid | 付款/付款申请单id | int8 | 64 |  | √ | 0 | 付款/付款申请单id |
| 53 | ftrainticketnum | 火车票车票号 | varchar | 255 |  | √ | ' ' | 火车票车票号 |
| 54 | fproducttype | 结算类型 | bpchar | 1 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 |
| 55 | fbookedname | 预订人姓名 | varchar | 100 |  | √ | ' ' | 预订人姓名 |
| 56 | fsettlemain | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 57 | fisbusiness | 订单性质 | bpchar | 1 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 58 | fsubbatchno | 结算子批次号 | varchar | 100 |  | √ | ' ' | 结算子批次号 |
| 59 | fsettledept | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 60 | fbalanceremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 61 | fbillstatusname | 结算确认状态 | varchar | 30 |  | √ | ' ' | 结算确认状态,枚举: 1 :待确认 2 :已确认 |
| 62 | fcheckingbillnum | 账单编码 | varchar | 80 |  | √ | ' ' | 账单编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_tcbill_org |  | fcompanyid,fsettlemain |
| 2 | idx_er_train_billno |  | fordernum,fserver |
| 3 | t_er_traincheckingbill_pkey |  | fid |
| 4 | idx_er_traincheck_paybillid |  | fpaybillid |
