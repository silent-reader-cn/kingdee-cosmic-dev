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
| 9 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 10 | ftotaltax | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 11 | farrivecity | 到达城市 | varchar | 255 |  | √ | ' ' | 到达城市 |
| 12 | fticketprice | 火车票价 | numeric | 23 | 10 | √ | 0.0000000000 | 火车票价 |
| 13 | fdeparttime | 出发时间 | timestamp | 0 |  |  | null | 出发时间 |
| 14 | farriveaddress | 到达车站 | varchar | 255 |  | √ | ' ' | 到达车站 |
| 15 | fhasinvoice | 已开票 | bpchar | 1 |  | √ | '0' | 已开票,枚举: 1 :是 0 :否 2 :开票中 |
| 16 | fparentordernum | 父订单号 | varchar | 100 |  | √ | ' ' | 父订单号 |
| 17 | ftrainseat | 席位 | varchar | 30 |  | √ | ' ' | 席位,枚举: 1 :硬卧 2 :软卧 3 :无座 4 :硬座 5 :动卧 6 :高级软卧 7 :一等卧 8 :二等卧 9 :软座 A :特等座 B :商务座 C :一等座 D :二等座 E :其他 |
| 18 | fbatchno | 结算批次号 | varchar | 100 |  | √ | ' ' | 结算批次号 |
| 19 | fserviceamounttax | 服务费税额 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税额 |
| 20 | fdepartcity | 出发城市 | varchar | 255 |  | √ | ' ' | 出发城市 |
| 21 | fallorderbaseid | 订单总表数据 | int8 | 64 |  | √ | 0 | [全部订单 er_allorderbill](../em_files/er_allorderbill.md) |
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
| 3 | frefunddeductrate | 退票费税率(%) | numeric | 23 | 10 | √ | 0 | 退票费税率(%) |
| 4 | forgid | 申请人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftotalamount | 结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额 |
| 6 | forderid | forderid | int8 | 64 |  | √ | 0 |  |
| 7 | fordernum | 结算单号 | varchar | 80 |  | √ | ' ' | 结算单号 |
| 8 | fisbalance | 已对平 | bpchar | 1 |  | √ | '2' | 已对平,枚举: 1 :平 2 :不平 3 :废弃 |
| 9 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 10 | frefundamounttax | 退票费税额 | numeric | 23 | 10 | √ | 0 | 退票费税额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | foperationtype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 |
| 13 | fserver | 服务商 | varchar | 30 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 |
| 14 | forderstatus | 订单状态 | varchar | 30 |  | √ | ' ' | 订单状态,枚举: 1 :已出票 2 :已改签 3 :已退票 4 :出票失败 5 :出票失败退款 6 :改签中 7 :退票中 9999 :未知 |
| 15 | fpassegerid | 乘客 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 17 | forderformid | forderformid | varchar | 80 |  | √ | ' ' |  |
| 18 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 19 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 个人支付金额 |
| 20 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :未审核 C :已审核 |
| 22 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 23 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 24 | fserialno | 发票流水号 | varchar | 255 |  | √ | ' ' | 发票流水号 |
| 25 | fpushcount | 下推计数 | int8 | 64 |  | √ | 0 | 下推计数 |
| 26 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 27 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 28 | forderserver | forderserver | varchar | 30 |  | √ | ' ' |  |
| 29 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 30 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | 'A' | 报销状态,枚举: A :未报销 B :报销中 C :已付款/已完成 |
| 31 | fdownloadlink | 下载地址 | varchar | 2000 |  | √ | ' ' | 下载地址 |
| 32 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fkddownloadlink | 内部下载地址 | varchar | 2000 |  | √ | ' ' | 内部下载地址 |
| 34 | fidentityerrormsg | 发票识别异常信息 | varchar | 500 |  | √ | ' ' | 发票识别异常信息 |
| 35 | fhappenddate | 结算发生时间 | timestamp | 0 |  |  | null | 结算发生时间 |
| 36 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 37 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国际 |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | faccountid | 主账户ID | varchar | 30 |  | √ | ' ' | 主账户ID |
| 40 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | foutaccountid | 商旅方系统拆账id | varchar | 255 |  | √ | ' ' | 商旅方系统拆账id |
| 42 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 43 | fendorsementamount | 改签费 | numeric | 23 | 10 | √ | 0 | 改签费 |
| 44 | fpaybillnum | 付款/付款申请单号 | varchar | 80 |  | √ | ' ' | 付款/付款申请单号 |
| 45 | fpassegername | 乘客姓名 | varchar | 100 |  | √ | ' ' | 乘客姓名 |
| 46 | fordertotalamount | fordertotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 47 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 |
| 48 | fpricebillingtype | 票价开票类型 | varchar | 255 |  | √ | ' ' | 票价开票类型,枚举: 2 :增值税专用发票 1 :增值税普通发票 9999 :未知 3 :机票行程单 4 :火车票 28 :数电票（航空运输电子客票） 29 :数电票（铁路电子客票） |
| 49 | ftotaltax | ftotaltax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 50 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 51 | fisreconciliation | 已对账 | bpchar | 1 |  | √ | ' ' | 已对账 |
| 52 | finvoiceidentityflag | 发票识别成功 | varchar | 1 |  | √ | 0 | 发票识别成功 |
| 53 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 57 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 58 | fpaybillid | 付款/付款申请单id | int8 | 64 |  | √ | 0 | 付款/付款申请单id |
| 59 | ftrainticketnum | 火车票车票号 | varchar | 255 |  | √ | ' ' | 火车票车票号 |
| 60 | fproducttype | 结算类型 | bpchar | 1 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 |
| 61 | fbookedname | 预订人姓名 | varchar | 100 |  | √ | ' ' | 预订人姓名 |
| 62 | fsettlemain | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 63 | fisbusiness | 订单性质 | bpchar | 1 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 64 | fsubbatchno | 结算子批次号 | varchar | 100 |  | √ | ' ' | 结算子批次号 |
| 65 | fsettledept | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 66 | fbalanceremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 67 | fbillstatusname | 结算确认状态 | varchar | 30 |  | √ | ' ' | 结算确认状态,枚举: 1 :待确认 2 :已确认 |
| 68 | foutsettlementnum | 外部系统结算单号 | varchar | 255 |  | √ | ' ' | 外部系统结算单号 |
| 69 | fcheckingbillnum | 账单编号 | varchar | 80 |  | √ | ' ' | 账单编号 |

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
