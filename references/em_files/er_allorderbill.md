# 全部订单-er_allorderbill

## 全部订单-主表 t_er_allorderbill

- **表名称：** 全部订单-主表
- **表名：** t_er_allorderbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalamount | 订单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 订单金额 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | forderid | 订单ID | varchar | 50 |  | √ | ' ' | 订单ID |
| 5 | fordernum | 订单号 | varchar | 100 |  | √ | ' ' | 订单号 |
| 6 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 7 | fisapprove | 是否审核通过 | bpchar | 1 |  | √ | '0' | 是否审核通过 |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fneedbilling | 是否需要开票 | bpchar | 1 |  | √ | '1' | 是否需要开票 |
| 10 | foperationtype | 业务类型 | bpchar | 1 |  | √ | '0' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 8 :用餐 |
| 11 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 12 | fserver | 服务商 | varchar | 50 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 MEITUAN :美团商企通 |
| 13 | freimbursenum | 差旅报销单号 | varchar | 100 |  | √ | ' ' | 差旅报销单号 |
| 14 | forderstatus | forderstatus | varchar | 100 |  | √ | ' ' |  |
| 15 | forderformid | 订单表单ID | varchar | 30 |  | √ | ' ' | 订单表单ID |
| 16 | fparentordernum | 父订单号 | varchar | 100 |  | √ | ' ' | 父订单号 |
| 17 | fisconfirm | 是否确认 | bpchar | 1 |  | √ | '0' | 是否确认 |
| 18 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 19 | foverdesc | 超标理由 | varchar | 255 |  | √ | ' ' | 超标理由 |
| 20 | fdeptid | 申请人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 23 | fisreimburse | 是否报销 | bpchar | 1 |  | √ | '0' | 是否报销 |
| 24 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 25 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 26 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fperiod | fperiod | varchar | 100 |  | √ | ' ' |  |
| 28 | fhappenddate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 29 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国外 |
| 30 | fbillauditstatus | 申请单是否审核 | varchar | 10 |  | √ | ' ' | 申请单是否审核 |
| 31 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 32 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fisverified | 是否核销 | bpchar | 1 |  | √ | '0' | 是否核销 |
| 34 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 35 | fpayamount | 实付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实付金额 |
| 36 | fpaybillnum | 付款单号 | varchar | 100 |  | √ | ' ' | 付款单号 |
| 37 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 er_mealapplication_bill :用餐申请单 er_dailyvehiclebill :用车申请单 |
| 38 | fexpcommitdepnum | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 39 | foabillnum | 出差申请单号 | varchar | 100 |  | √ | ' ' | 出差申请单号 |
| 40 | fisreconciliation | 是否对账 | bpchar | 1 |  | √ | '0' | 是否对账 |
| 41 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 42 | fcheckingpayid | 月结付款表ID | int8 | 64 |  | √ | 0 | 月结付款表ID |
| 43 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 44 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 45 | fbookedname | fbookedname | varchar | 30 |  | √ | ' ' |  |
| 46 | fproducttype | 结算类型 | varchar | 100 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 47 | fpaymentbillnum | fpaymentbillnum | varchar | 80 |  | √ | ' ' |  |
| 48 | fdeptconfirm | 部门确认 | varchar | 10 |  | √ | ' ' | 部门确认 |
| 49 | finvoiceid | 开票记录ID | int8 | 64 |  | √ | 0 | 开票记录ID |
| 50 | fexpcommitcomnum | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 51 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_aob_fordernum |  | fordernum |
| 2 | idx_er_aob_fsourcebookedid |  | fsourcebookedid |
| 3 | t_er_allorderbill_pkey |  | fid |
| 4 | idx_fhappenddate |  | fhappenddate |
| 5 | idx_er_aob_fbillno |  | foabillnum |
