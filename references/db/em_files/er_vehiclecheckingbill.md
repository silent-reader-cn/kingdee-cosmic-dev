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
| 12 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 13 | ftravelways | 出行方式 | varchar | 100 |  | √ | ' ' | 出行方式 |
| 14 | ftotaltax | ftotaltax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 15 | fallorderbaseid | 订单总表数据 | int8 | 64 |  | √ | 0 | [全部订单 er_allorderbill](../em_files/er_allorderbill.md) |
| 16 | fvendorname | 供应商名称 | varchar | 30 |  | √ | ' ' | 供应商名称 |
| 17 | fperiod | 期间 | varchar | 30 |  | √ | ' ' | 期间 |
| 18 | fhasinvoice | 已开票 | bpchar | 1 |  | √ | '0' | 已开票,枚举: 1 :是 0 :否 2 :开票中 |
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
| 13 | fserver | 服务商 | varchar | 30 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 GAODE :高德 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 |
| 14 | fservicebegintime | 服务开始时间 | timestamp | 0 |  |  | null | 服务开始时间 |
| 15 | forderstatus | 订单状态 | varchar | 30 |  | √ | ' ' | 订单状态,枚举: WaitReply :等待应答 WaitService :等待接驾 InService :正在服务 EndService :行程结束 Canceling :取消中 Canceled :已取消 WaitPay :待支付 Successful :已成交 Refunded :已退款 PartialRefund :部分退款 9999 :未知 |
| 16 | fpassegerid | 乘客 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | farriveaddress | 下车地址 | varchar | 255 |  | √ | ' ' | 下车地址 |
| 18 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 19 | forderformid | forderformid | varchar | 80 |  | √ | ' ' |  |
| 20 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 21 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 22 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :未审核 C :已审核 |
| 23 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 24 | fpushcount | 下推计数 | int8 | 64 |  | √ | 0 | 下推计数 |
| 25 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | forderserver | forderserver | varchar | 30 |  | √ | ' ' |  |
| 28 | fdistance | 公里数 | varchar | 50 |  | √ | ' ' | 公里数 |
| 29 | fvehicletype | 用车类型 | varchar | 50 |  | √ | ' ' | 用车类型,枚举: 1 :差旅用车 2 :公务出行用车 3 :工作日加班用车 4 :周末/节假日加班用车 6 :招待用车 7 :会议用车 |
| 30 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 31 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | 'A' | 报销状态,枚举: A :未报销 B :报销中 C :已付款/已完成 |
| 32 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fhappenddate | 结算发生时间 | timestamp | 0 |  |  | null | 结算发生时间 |
| 34 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | faccountid | 主账户ID | varchar | 30 |  | √ | ' ' | 主账户ID |
| 37 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | foutaccountid | 商旅方系统拆账id | varchar | 255 |  | √ | ' ' | 商旅方系统拆账id |
| 39 | fdepartaddress | 上车地址 | varchar | 255 |  | √ | ' ' | 上车地址 |
| 40 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 41 | fcityname | 城市名称 | varchar | 100 |  | √ | ' ' | 城市名称 |
| 42 | fpaybillnum | 付款/付款申请单号 | varchar | 80 |  | √ | ' ' | 付款/付款申请单号 |
| 43 | fserviceendtime | 服务结束时间 | timestamp | 0 |  |  | null | 服务结束时间 |
| 44 | fpassegername | 乘客姓名 | varchar | 30 |  | √ | ' ' | 乘客姓名 |
| 45 | fordertotalamount | fordertotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 46 | fpricebillingtype | 票价开票类型 | varchar | 10 |  | √ | ' ' | 票价开票类型,枚举: 2 :增值税专用发票 1 :增值税普通发票 9999 :未知 |
| 47 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 er_dailyvehiclebill :用车申请单 |
| 48 | ftotaltax | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 49 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 50 | fisreconciliation | 已对账 | bpchar | 1 |  | √ | ' ' | 已对账 |
| 51 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 52 | fdealamount | 实付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实付金额 |
| 53 | fusetime | 用车时间 | timestamp | 0 |  |  | null | 用车时间 |
| 54 | fformid | 表单ID | varchar | 30 |  | √ | ' ' | 表单ID |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 56 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 57 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 58 | fpaybillid | 付款/付款申请单id | int8 | 64 |  | √ | 0 | 付款/付款申请单id |
| 59 | fpushcheckingexplist | 生成部门清单 | bpchar | 1 |  | √ | '0' | 生成部门清单 |
| 60 | fproducttype | 结算类型 | bpchar | 1 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 |
| 61 | fbookedname | 预订人姓名 | varchar | 100 |  | √ | ' ' | 预订人姓名 |
| 62 | fsettlemain | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 63 | fisbusiness | 订单性质 | bpchar | 1 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 64 | fsubbatchno | 结算子批次号 | varchar | 100 |  | √ | ' ' | 结算子批次号 |
| 65 | fsettledept | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 66 | fbalanceremark | 置平备注 | varchar | 1000 |  | √ | ' ' | 置平备注 |
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
| 1 | idx_er_vcb_billno |  | fordernum,fserver |
| 2 | idx_er_vehiclecheck_paybillid |  | fpaybillid |
| 3 | t_er_vehiclecheckingbill_pkey |  | fid |
| 4 | idx_er_vcbill_org |  | fcompanyid,fsettlemain |
