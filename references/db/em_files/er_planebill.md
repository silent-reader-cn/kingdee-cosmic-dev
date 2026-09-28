# 机票订单-er_planebill

## 机票订单-分表 t_er_planebill_a

- **表名称：** 机票订单-分表
- **表名：** t_er_planebill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutaccountid | 商旅方系统拆账id | varchar | 255 |  | √ | ' ' | 商旅方系统拆账id |
| 3 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fislowestpirce | 最低价 | bpchar | 1 |  | √ | ' ' | 最低价 |
| 5 | foutordernum | 外部系统订单号 | varchar | 255 |  | √ | ' ' | 外部系统订单号 |
| 6 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 7 | flowestpirce | 最低价格 | numeric | 23 | 10 | √ | 0.0000000000 | 最低价格 |
| 8 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_planebill_a |  | fid |
| 2 | idx_er_planebill_flow |  | fislowestpirce |

---

## 机票订单-主表 t_er_planebill

- **表名称：** 机票订单-主表
- **表名：** t_er_planebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalamount | 订单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 订单金额 |
| 3 | fordernum | 订单号 | varchar | 100 |  | √ | ' ' | 订单号 |
| 4 | fisapprove | 审核通过 | bpchar | 1 |  | √ | '0' | 审核通过 |
| 5 | ftravelername | 乘机人 | varchar | 100 |  | √ | ' ' | 乘机人 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 8 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 9 | forderstatus | 订单状态 | varchar | 100 |  | √ | ' ' | 订单状态,枚举: 40000 :已出票 50301 :改签中 50302 :已改签 50201 :退票中 50202 :已退票 10000 :已提交 20000 :已预订 40100 :出票中 50203 :已部分出票 55555 :改签失败 55554 :改签已取消 30000 :已取消 9999 :未知 |
| 10 | fordertype | 订单类型 | varchar | 100 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 Q :取消单 |
| 11 | fticketstatusupdater | 使用状态修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fticketstatus | 订单使用状态 | varchar | 100 |  | √ | 'UNUSED' | 订单使用状态,枚举: USED :已使用 UNUSED :未使用 REFOUND :已退票 CHANGED :已改签 |
| 13 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 14 | foverdesc | 超标理由 | varchar | 100 |  | √ | ' ' | 超标理由 |
| 15 | fisreimburse | 已报销 | bpchar | 1 |  | √ | '0' | 已报销 |
| 16 | frefundreason | 退票理由 | varchar | 255 |  | √ | ' ' | 退票理由 |
| 17 | fdiscount | 折扣（%） | numeric | 23 | 10 | √ | 0.0000000000 | 折扣（%） |
| 18 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | 'A' | 报销状态,枚举: A :未报销 B :报销中 C :已付款/已完成 |
| 19 | ffeedback | 错误反馈 | varchar | 255 |  | √ | '0' | 错误反馈 |
| 20 | fkddownloadlink | 内部下载地址 | varchar | 500 |  | √ | ' ' | 内部下载地址 |
| 21 | fassuranceamount | 保险费 | numeric | 23 | 10 | √ | 0.0000000000 | 保险费 |
| 22 | fhappenddate | 费用发生时间 | timestamp | 0 |  |  | null | 费用发生时间 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fpnr | PNR | varchar | 100 |  | √ | ' ' | PNR |
| 25 | fendorsementamount | 改签费 | numeric | 23 | 10 | √ | 0.0000000000 | 改签费 |
| 26 | flandingtime | 降落时间 | timestamp | 0 |  |  | null | 降落时间 |
| 27 | frefundamount | 退票费 | numeric | 23 | 10 | √ | 0.0000000000 | 退票费 |
| 28 | fitinerarydate | 填开日期 | timestamp | 0 |  |  | null | 填开日期 |
| 29 | ftakeofftime | 出发时间 | timestamp | 0 |  |  | null | 出发时间 |
| 30 | fpaybillnum | 付款单号 | varchar | 100 |  | √ | ' ' | 付款单号 |
| 31 | fairlinename | 航空公司名称 | varchar | 100 |  | √ | ' ' | 航空公司名称 |
| 32 | fticketnum | 电子客票号 | varchar | 100 |  | √ | ' ' | 电子客票号 |
| 33 | fisreconciliation | 已对账 | bpchar | 1 |  | √ | '0' | 已对账 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fispushinvoicecloud | 影像已推送发票云 | bpchar | 1 |  | √ | '0' | 影像已推送发票云 |
| 36 | ffuelprice | 燃油费 | numeric | 23 | 10 | √ | 0.0000000000 | 燃油费 |
| 37 | fchoosenotminreason | 非最低价说明 | varchar | 100 |  | √ | ' ' | 非最低价说明 |
| 38 | kddownloadlink | kddownloadlink | varchar | 2000 |  | √ | ' ' |  |
| 39 | fotheramount | 其他费用 | numeric | 23 | 10 | √ | 0 | 其他费用 |
| 40 | ffromcity | 出发城市 | varchar | 100 |  | √ | ' ' | 出发城市 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 43 | fcabinclass | 舱位等级 | varchar | 100 |  | √ | ' ' | 舱位等级 |
| 44 | fproducttype | 结算类型 | varchar | 100 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 45 | fbookedname | 预订人 | varchar | 100 |  | √ | ' ' | 预订人 |
| 46 | fnoticetimes | 通知次数 | int4 | 32 |  | √ | 0 | 通知次数 |
| 47 | fisbusiness | 订单性质 | varchar | 100 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 48 | foriordernum | 原单订单号 | varchar | 100 |  | √ | ' ' | 原单订单号 |
| 49 | foverflag | 超标 | varchar | 100 |  | √ | ' ' | 超标 |
| 50 | ftakeoffportname | 出发机场名称 | varchar | 100 |  | √ | ' ' | 出发机场名称 |
| 51 | fstandprice | 标准价格 | numeric | 23 | 10 | √ | 0.0000000000 | 标准价格 |
| 52 | fbilltype | fbilltype | varchar | 100 |  | √ | ' ' |  |
| 53 | ftakeoffport | 出发机场 | varchar | 100 |  | √ | ' ' | 出发机场 |
| 54 | fairline | 航空公司 | varchar | 100 |  | √ | ' ' | 航空公司 |
| 55 | flandingport | 降落机场 | varchar | 100 |  | √ | ' ' | 降落机场 |
| 56 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 57 | fneedbilling | 需要开票 | bpchar | 1 |  | √ | '1' | 需要开票 |
| 58 | fvatdednvoicecode | fvatdednvoicecode | varchar | 100 |  | √ | ' ' |  |
| 59 | foperationtype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 |
| 60 | fserver | 服务商 | varchar | 100 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 |
| 61 | freimbursenum | 报销单号 | varchar | 100 |  | √ | ' ' | 报销单号 |
| 62 | fitinerarynum | 行程单号 | varchar | 100 |  | √ | ' ' | 行程单号 |
| 63 | fparentordernum | 父订单号 | varchar | 100 |  | √ | ' ' | 父订单号 |
| 64 | fisconfirm | 已确认 | bpchar | 1 |  | √ | '0' | 已确认 |
| 65 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0 | 个人支付金额 |
| 66 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 67 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 68 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 69 | fserialno | 发票流水号 | varchar | 255 |  | √ | ' ' | 发票流水号 |
| 70 | ffromcityname | 出发城市名称 | varchar | 100 |  | √ | ' ' | 出发城市名称 |
| 71 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 72 | fvatdednvoicenum | fvatdednvoicenum | varchar | 100 |  | √ | ' ' |  |
| 73 | fflightno | 航班号 | varchar | 100 |  | √ | ' ' | 航班号 |
| 74 | fdownloadlink | 下载地址 | varchar | 500 |  | √ | ' ' | 下载地址 |
| 75 | ftocityname | 到达城市名称 | varchar | 100 |  | √ | ' ' | 到达城市名称 |
| 76 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 77 | ftocity | 到达城市 | varchar | 100 |  | √ | ' ' | 到达城市 |
| 78 | fairportprice | 民航发展基金及其他/税费 | numeric | 23 | 10 | √ | 0.0000000000 | 民航发展基金及其他/税费 |
| 79 | ftax | 税费 | numeric | 23 | 10 | √ | 0.0000000000 | 税费 |
| 80 | fidentityerrormsg | 发票识别异常信息 | varchar | 2000 |  | √ | ' ' | 发票识别异常信息 |
| 81 | flandingportname | 降落机场名称 | varchar | 100 |  | √ | ' ' | 降落机场名称 |
| 82 | fbookeddept | 预订人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 83 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国际 |
| 84 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 85 | ftravelerdept | 乘机人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 86 | ftripid | 出差行程ID | varchar | 100 |  | √ | ' ' | 出差行程ID |
| 87 | fvatcominvoicenum | fvatcominvoicenum | varchar | 100 |  | √ | ' ' |  |
| 88 | fisverified | 已核销 | bpchar | 1 |  | √ | ' ' | 已核销 |
| 89 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 90 | fvatcominvoicecode | fvatcominvoicecode | varchar | 100 |  | √ | ' ' |  |
| 91 | fisaddintegral | 加入低碳积分榜 | bpchar | 1 |  | √ | '0' | 加入低碳积分榜 |
| 92 | fsourcetravelerid | 乘机人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 93 | fchangetype | 退改性质 | varchar | 100 |  | √ | ' ' | 退改性质 |
| 94 | fpricebillingtype | 票价开票类型 | varchar | 255 |  | √ | ' ' | 票价开票类型,枚举: 2 :增值税专用发票 1 :增值税普通发票 9999 :未知 3 :机票行程单 4 :火车票 28 :数电票（航空运输电子客票） 29 :数电票（铁路电子客票） |
| 95 | forderstatusname | 订单状态名称 | varchar | 100 |  | √ | ' ' | 订单状态名称 |
| 96 | fexpcommitdepnum | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 97 | foabillnum | 申请单号 | varchar | 100 |  | √ | ' ' | 申请单号 |
| 98 | fticketprice | 机票价格 | numeric | 23 | 10 | √ | 0.0000000000 | 机票价格 |
| 99 | fchangereason | 改签理由 | varchar | 255 |  | √ | ' ' | 改签理由 |
| 100 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 101 | fcabin | 舱位 | varchar | 100 |  | √ | ' ' | 舱位 |
| 102 | fisattachment | 影像已推送附件 | bpchar | 1 |  | √ | '0' | 影像已推送附件 |
| 103 | fexpcommitcomnum | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_planebill_pkey |  | fid |
| 2 | idx_er_plane_org_time |  | ftakeofftime,fexpcommitcomnum,fexpcommitdepnum |
| 3 | idx_er_pbbillno |  | foabillnum |
| 4 | idx_er_pbill_complex |  | ftravelername,fflightno,ftakeofftime |
| 5 | idx_er_pbill_org |  | fexpcommitcomnum,fcompanyid |
| 6 | idx_er_pbfsourcebookedid |  | fsourcebookedid |
| 7 | idx_er_pfsourcetravelerid |  | fsourcetravelerid |
