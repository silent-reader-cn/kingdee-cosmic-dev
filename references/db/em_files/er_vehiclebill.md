# 用车订单-er_vehiclebill

## 用车订单-分表 t_er_vehiclebill_a

- **表名称：** 用车订单-分表
- **表名：** t_er_vehiclebill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 个人支付金额 |
| 4 | fdepartaddress | 上车地址 | varchar | 255 |  | √ | ' ' | 上车地址 |
| 5 | fbatchno | fbatchno | varchar | 100 |  | √ | ' ' |  |
| 6 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 7 | fcityname | 城市名称 | varchar | 100 |  | √ | ' ' | 城市名称 |
| 8 | fcarcontroltype | 管控指标 | varchar | 30 |  | √ | ' ' | 管控指标,枚举: 2 :费用 4 :车型 8 :用车时间 16 :用车地点 |
| 9 | fvendorname | 供应商名称 | varchar | 100 |  | √ | ' ' | 供应商名称 |
| 10 | fchildtype | 超标类型 | bpchar | 1 |  | √ | ' ' | 超标类型,枚举: E :预估超标RC R :实际费用超标RC |
| 11 | frccodename | RC名称 | varchar | 100 |  | √ | ' ' | RC名称 |
| 12 | farriveaddress | 下车地址 | varchar | 255 |  | √ | ' ' | 下车地址 |
| 13 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国际 |
| 14 | fusetime | 用车时间 | timestamp | 0 |  |  | null | 用车时间 |
| 15 | fvehicleid | 车型 | bpchar | 1 |  | √ | ' ' | 车型,枚举: 1 :经济型 2 :舒适型 3 :豪华型 4 :商务型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_vehib_a_utm |  | fusetime |
| 2 | t_er_vehiclebill_a_pkey |  | fid |

---

## 用车订单-主表 t_er_vehiclebill

- **表名称：** 用车订单-主表
- **表名：** t_er_vehiclebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftotalamount | 订单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 订单金额 |
| 4 | fordernum | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 5 | fbookedcompany | 预订人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 7 | fisapprove | 是否审核通过 | bpchar | 1 |  | √ | ' ' | 是否审核通过 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fneedbilling | 是否需要开票 | bpchar | 1 |  | √ | ' ' | 是否需要开票 |
| 10 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 11 | fvatdednvoicecode | fvatdednvoicecode | varchar | 100 |  | √ | ' ' |  |
| 12 | fpaymentstatus | 支付状态 | varchar | 30 |  | √ | ' ' | 支付状态,枚举: WP :待支付 PP :支付中 PF :支付失败 PS :支付成功 |
| 13 | foperationtype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 |
| 14 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 15 | fserver | 服务商 | varchar | 30 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 |
| 16 | freimbursenum | 报销单号 | varchar | 100 |  | √ | ' ' | 报销单号 |
| 17 | fpassegerid | 乘客 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | forderstatus | 订单状态 | varchar | 30 |  | √ | ' ' | 订单状态,枚举: WaitReply :等待应答 WaitService :等待接驾 InService :正在服务 EndService :行程结束 Canceling :取消中 Canceled :已取消 Successful :已成交 WaitPay :待支付 Refunded :已退款 PartialRefund :部分退款 9999 :未知 |
| 19 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 20 | fparentordernum | 父订单号 | varchar | 80 |  | √ | ' ' | 父订单号 |
| 21 | fisconfirm | 是否确认 | bpchar | 1 |  | √ | ' ' | 是否确认 |
| 22 | fpassegerdept | 乘客部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 23 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 24 | foverdesc | 超标理由 | varchar | 255 |  | √ | ' ' | 超标理由 |
| 25 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 27 | fisreimburse | 是否报销 | bpchar | 1 |  | √ | ' ' | 是否报销 |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | fvatdednvoicenum | fvatdednvoicenum | varchar | 100 |  | √ | ' ' |  |
| 30 | fdistance | 公里数 | varchar | 50 |  | √ | ' ' | 公里数 |
| 31 | fvehicletype | 用车类型 | varchar | 50 |  | √ | ' ' | 用车类型,枚举: 1 :差旅用车 2 :公务出行用车 3 :工作日加班用车 4 :周末/节假日加班用车 6 :招待用车 7 :会议用车 |
| 32 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 33 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | 'A' | 报销状态,枚举: A :未报销 B :报销中 C :已付款 |
| 34 | ffeedback | 错误反馈 | varchar | 255 |  | √ | '0' | 错误反馈 |
| 35 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fhappenddate | 费用发生时间 | timestamp | 0 |  |  | null | 费用发生时间 |
| 37 | fbookeddept | 预订人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | ftripid | 出差行程ID | varchar | 30 |  | √ | ' ' | 出差行程ID |
| 41 | fvatcominvoicenum | fvatcominvoicenum | varchar | 100 |  | √ | ' ' |  |
| 42 | fisverified | 是否核销 | bpchar | 1 |  | √ | ' ' | 是否核销 |
| 43 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 44 | fvatcominvoicecode | fvatcominvoicecode | varchar | 100 |  | √ | ' ' |  |
| 45 | fisaddintegral | 是否加入低碳积分榜 | bpchar | 1 |  | √ | ' ' | 是否加入低碳积分榜 |
| 46 | fpaybillnum | 付款单号 | varchar | 80 |  | √ | ' ' | 付款单号 |
| 47 | fpassegername | 乘客姓名 | varchar | 100 |  | √ | ' ' | 乘客姓名 |
| 48 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 er_dailyvehiclebill :用车申请单 |
| 49 | fpricebillingtype | 票价开票类型 | varchar | 10 |  | √ | ' ' | 票价开票类型,枚举: 2 :增值税专用发票 1 :增值税普通发票 9999 :未知 |
| 50 | fexpcommitdepnum | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 51 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 52 | fisreconciliation | 是否对账 | bpchar | 1 |  | √ | ' ' | 是否对账 |
| 53 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 54 | fdealamount | 实付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实付金额 |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 56 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 57 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 58 | fproducttype | 结算类型 | bpchar | 1 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 59 | fbookedname | 预订人姓名 | varchar | 100 |  | √ | ' ' | 预订人姓名 |
| 60 | fnoticetimes | 通知次数 | int4 | 32 |  | √ | 0 | 通知次数 |
| 61 | fisbusiness | 订单性质 | bpchar | 1 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 62 | foriordernum | 原单订单号 | varchar | 80 |  | √ | ' ' | 原单订单号 |
| 63 | fallorderbaseid | 订单总表数据 | int8 | 64 |  | √ | 0 | 全部订单 er_allorderbill |
| 64 | fexpcommitcomnum | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_vbbill_billnum |  | foabillnum |
| 2 | idx_er_vbfsourcebookedid |  | fsourcebookedid |
| 3 | t_er_vehiclebill_pkey |  | fid |
| 4 | idx_er_vbill_org |  | fexpcommitcomnum,fcompanyid |
