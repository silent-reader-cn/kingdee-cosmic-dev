# 机票结算单-er_planecheckingbill

## 机票结算单-主表 t_er_planecheckingbill

- **表名称：** 机票结算单-主表
- **表名：** t_er_planecheckingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalamount | 结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额 |
| 3 | forgid | 申请人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forderid | forderid | int8 | 64 |  | √ | 0 |  |
| 5 | fordernum | 结算单号 | varchar | 80 |  | √ | ' ' | 结算单号 |
| 6 | ftravelername | 乘机人 | varchar | 100 |  | √ | ' ' | 乘机人 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fservicedeductrate | 服务费税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税率(%) |
| 9 | forderstatus | 订单状态 | varchar | 30 |  | √ | ' ' | 订单状态,枚举: 20000 :已预订 40000 :已出票 31000 :取消中 30000 :已取消 50201 :退票中 50202 :已退票 50301 :改签中 50302 :已改签 USED :已乘机 9999 :未知 |
| 10 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 Q :取消单 |
| 11 | fticketstatus | 使用状态 | varchar | 100 |  | √ | ' ' | 使用状态,枚举: UNUSED :未使用 USED :已使用 REFOUND :已退票 CHANGED :已改签 |
| 12 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 13 | fpushcount | 下推计数 | int8 | 64 |  | √ | 0 | 下推计数 |
| 14 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 15 | fdiscount | 折扣（%） | numeric | 23 | 10 | √ | 0.0000000000 | 折扣（%） |
| 16 | forderserver | forderserver | varchar | 30 |  | √ | ' ' |  |
| 17 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | 'A' | 报销状态,枚举: A :未报销 B :报销中 C :已付款/已完成 |
| 18 | fkddownloadlink | 内部下载地址 | varchar | 500 |  | √ | ' ' | 内部下载地址 |
| 19 | fperiod | 期间 | varchar | 30 |  | √ | ' ' | 期间 |
| 20 | fhappenddate | 结算发生日期 | timestamp | 0 |  |  | null | 结算发生日期 |
| 21 | fassuranceamount | 保险费 | numeric | 23 | 10 | √ | 0.0000000000 | 保险费 |
| 22 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | faccountid | 主账户ID | varchar | 30 |  | √ | ' ' | 主账户ID |
| 25 | fbillperiod | 差旅壹号账期 | timestamp | 0 |  |  | null | 差旅壹号账期 |
| 26 | fendorsementamount | 改签费 | numeric | 23 | 10 | √ | 0.0000000000 | 改签费 |
| 27 | flandingtime | 到达时间 | timestamp | 0 |  |  | null | 到达时间 |
| 28 | frefundamount | 退票费 | numeric | 23 | 10 | √ | 0.0000000000 | 退票费 |
| 29 | fitinerarydate | 填开日期 | timestamp | 0 |  |  | null | 填开日期 |
| 30 | ftakeofftime | 出发日期 | timestamp | 0 |  |  | null | 出发日期 |
| 31 | fpaybillnum | 付款/付款申请单号 | varchar | 80 |  | √ | ' ' | 付款/付款申请单号 |
| 32 | forderdeductrate | 票价税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 票价税率(%) |
| 33 | fairlinename | 航空公司名称 | varchar | 100 |  | √ | ' ' | 航空公司名称 |
| 34 | fordertotalamount | fordertotalamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 35 | fticketnum | 电子客票号 | varchar | 80 |  | √ | ' ' | 电子客票号 |
| 36 | fisreconciliation | 已对账 | bpchar | 1 |  | √ | ' ' | 已对账 |
| 37 | finvoiceidentityflag | 发票识别成功 | varchar | 1 |  | √ | 0 | 发票识别成功 |
| 38 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | ffuelprice | 燃油费 | numeric | 23 | 10 | √ | 0.0000000000 | 燃油费 |
| 40 | kddownloadlink | kddownloadlink | varchar | 2000 |  | √ | ' ' |  |
| 41 | fpromotion | 促销 | numeric | 23 | 10 | √ | 0.0000000000 | 促销 |
| 42 | fotheramount | 其他费用 | numeric | 23 | 10 | √ | 0 | 其他费用 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fcabinclass | 舱位等级 | varchar | 100 |  | √ | ' ' | 舱位等级 |
| 46 | fserviceamounttax | 服务费税额 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税额 |
| 47 | fbookedname | 预订人姓名 | varchar | 100 |  | √ | ' ' | 预订人姓名 |
| 48 | fproducttype | 结算类型 | bpchar | 1 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 |
| 49 | fisbusiness | 订单性质 | bpchar | 1 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 50 | fallorderbaseid | 订单总表数据 | int8 | 64 |  | √ | 0 | [全部订单 er_allorderbill](../em_files/er_allorderbill.md) |
| 51 | fsettledept | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 52 | fbalanceremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 53 | forderamounttax | 票价税额 | numeric | 23 | 10 | √ | 0.0000000000 | 票价税额 |
| 54 | fcheckingbillnum | 账单编号 | varchar | 100 |  | √ | ' ' | 账单编号 |
| 55 | forderordernum | forderordernum | varchar | 80 |  | √ | ' ' |  |
| 56 | frefunddeductrate | 退票费税率(%) | numeric | 23 | 10 | √ | 0 | 退票费税率(%) |
| 57 | frebate | 返点 | numeric | 23 | 10 | √ | 0.0000000000 | 返点 |
| 58 | fisbalance | 已对平 | bpchar | 1 |  | √ | '2' | 已对平,枚举: 1 :平 2 :不平 3 :废弃 |
| 59 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 60 | forg | forg | int8 | 64 |  | √ | 0 |  |
| 61 | fpaybillstatus | 付款状态 | varchar | 100 |  | √ | ' ' | 付款状态,枚举: 0 :等待付款 1 :已付款 |
| 62 | frefundamounttax | 退票费税额 | numeric | 23 | 10 | √ | 0 | 退票费税额 |
| 63 | fsettlemainname | fsettlemainname | varchar | 100 |  | √ | ' ' |  |
| 64 | foperationtype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 |
| 65 | fserver | 服务商 | varchar | 100 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 |
| 66 | forderformid | forderformid | varchar | 30 |  | √ | ' ' |  |
| 67 | fitinerarynum | 行程单号 | varchar | 100 |  | √ | ' ' | 行程单号 |
| 68 | fparentordernum | 父订单号 | varchar | 100 |  | √ | ' ' | 父订单号 |
| 69 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0 | 个人支付金额 |
| 70 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | 'A' | 单据状态,枚举: A :未审核 C :已审核 |
| 71 | fbatchno | 结算批次号 | varchar | 100 |  | √ | ' ' | 结算批次号 |
| 72 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 73 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 74 | fserialno | 发票流水号 | varchar | 255 |  | √ | ' ' | 发票流水号 |
| 75 | ffromcityname | 出发城市名称 | varchar | 100 |  | √ | ' ' | 出发城市名称 |
| 76 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 77 | fflightno | 航班号 | varchar | 80 |  | √ | ' ' | 航班号 |
| 78 | fdownloadlink | 下载地址 | varchar | 500 |  | √ | ' ' | 下载地址 |
| 79 | ftocityname | 到达城市名称 | varchar | 100 |  | √ | ' ' | 到达城市名称 |
| 80 | fsourcebookedid | 预订人工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 81 | fairportprice | 民航发展基金 | numeric | 23 | 10 | √ | 0.0000000000 | 民航发展基金 |
| 82 | ftax | 税费 | numeric | 23 | 10 | √ | 0.0000000000 | 税费 |
| 83 | fidentityerrormsg | 发票识别异常信息 | varchar | 500 |  | √ | ' ' | 发票识别异常信息 |
| 84 | fproductsontype | 产品子类型 | varchar | 100 |  | √ | ' ' | 产品子类型,枚举: 1 :两方协议产品 2 :三方协议产品 3 :官网 4 :B2G 5 :B2T 6 :代理渠道 7 :公务员 8 :飞行达人 9 :单体协议酒店托管 10 :集团协议酒店托管 11 :会员酒店 |
| 85 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国外 |
| 86 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 87 | fsettlementamount | 结算金额（核算） | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额（核算） |
| 88 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 89 | fsourcetravelerid | 乘机人工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 90 | fpricebillingtype | 票价开票类型 | varchar | 255 |  | √ | ' ' | 票价开票类型,枚举: 2 :增值税专用发票 1 :增值税普通发票 9999 :未知 3 :机票行程单 4 :火车票 28 :数电票（航空运输电子客票） 29 :数电票（铁路电子客票） |
| 91 | ftotaltax | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 92 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 93 | fticketprice | 机票价格 | numeric | 19 |  | √ | 0 | 机票价格 |
| 94 | fhasinvoice | 已开票 | bpchar | 1 |  | √ | '0' | 已开票,枚举: 1 :是 0 :否 2 :开票中 |
| 95 | fformid | 表单ID | varchar | 100 |  | √ | ' ' | 表单ID |
| 96 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 97 | fpaybillid | 付款/付款申请单id | int8 | 64 |  | √ | 0 | 付款/付款申请单id |
| 98 | fcabin | 舱位 | varchar | 100 |  | √ | ' ' | 舱位 |
| 99 | fsettlemain | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 100 | fsubbatchno | 结算子批次号 | varchar | 100 |  | √ | ' ' | 结算子批次号 |
| 101 | fbillstatusname | 结算确认状态 | varchar | 5 |  | √ | ' ' | 结算确认状态,枚举: 1 :待确认 2 :已确认 |

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
| 2 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 3 | foutaccountid | 商旅方系统拆账id | varchar | 255 |  | √ | ' ' | 商旅方系统拆账id |
| 4 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 5 | fislowestpirce | 最低价 | bpchar | 1 |  | √ | ' ' | 最低价 |
| 6 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 7 | foutsettlementnum | 外部系统结算单号 | varchar | 255 |  | √ | ' ' | 外部系统结算单号 |
| 8 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 9 | flowestpirce | 最低价格 | numeric | 23 | 10 | √ | 0.0000000000 | 最低价格 |
| 10 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_planecheckingbill_a |  | fid |
| 2 | idx_er_planecb_a_flowe |  | fislowestpirce |
