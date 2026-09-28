# 全部结算单-er_allcheckingbill

## 全部结算单-主表 t_er_allcheckingbill

- **表名称：** 全部结算单-主表
- **表名：** t_er_allcheckingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fapplyorg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftotalamount | 订单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 订单金额 |
| 4 | forgid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fordernum | 订单号 | varchar | 100 |  | √ | ' ' | 订单号 |
| 6 | fisbalance | 已对平 | bpchar | 1 |  | √ | '1' | 已对平,枚举: 1 :平 2 :不平 3 :废弃 |
| 7 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 8 | fpayamount | 实付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 实付金额 |
| 9 | forderdeductrate | 票价税率 | numeric | 23 | 10 | √ | 0.0000000000 | 票价税率 |
| 10 | fpaybillnum | 付款单号 | varchar | 100 |  | √ | ' ' | 付款单号 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fservicedeductrate | 服务费税率 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税率 |
| 13 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 er_mealapplication_bill :用餐申请单 er_dailyvehiclebill :用车申请单 |
| 14 | ftotaltax | 可参考抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可参考抵扣税额 |
| 15 | foabillnum | 出差申请单号 | varchar | 100 |  | √ | ' ' | 出差申请单号 |
| 16 | fisreconciliation | 已对账 | bpchar | 1 |  | √ | '0' | 已对账 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | foperationtype | 业务类型 | varchar | 20 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :火车预订 8 :用餐 |
| 19 | fserver | 服务商 | varchar | 50 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 GAODE :高德 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 |
| 20 | fcheckingpayid | 月结付款表ID | int8 | 64 |  | √ | 0 | 月结付款表ID |
| 21 | forderformid | forderformid | varchar | 30 |  | √ | ' ' |  |
| 22 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 23 | fcheckingid | 对账单ID | varchar | 50 |  | √ | ' ' | 对账单ID |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :未审核 C :已审核 |
| 26 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 27 | fcheckingformid | 对账单表单ID | varchar | 30 |  | √ | ' ' | 对账单表单ID |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | funiqueid | 商旅侧结算单唯一标识 | varchar | 255 |  | √ | ' ' | 商旅侧结算单唯一标识 |
| 30 | fserviceamounttax | 服务费税额 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费税额 |
| 31 | fvouchernum | 凭证编号 | varchar | 80 |  | √ | ' ' | 凭证编号 |
| 32 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 33 | fbookedname | fbookedname | varchar | 30 |  | √ | ' ' |  |
| 34 | fproducttype | 结算类型 | bpchar | 1 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 |
| 35 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 36 | fisbusiness | 订单性质 | bpchar | 10 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 37 | fallorderbaseid | 订单总表数据 | int8 | 64 |  | √ | 0 | [全部订单 er_allorderbill](../em_files/er_allorderbill.md) |
| 38 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | finvoiceid | finvoiceid | varchar | 100 |  | √ | ' ' |  |
| 40 | fhappenddate | 费用发生日期 | timestamp | 0 |  |  | null | 费用发生日期 |
| 41 | forderamounttax | forderamounttax | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 42 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 43 | fcheckingbillnum | 账单编号 | varchar | 80 |  | √ | ' ' | 账单编号 |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | faccountid | 主账户ID | varchar | 30 |  | √ | ' ' | 主账户ID |
| 46 | fbillperiod | 差旅壹号账期 | timestamp | 0 |  |  | null | 差旅壹号账期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_allcheckingbill_pkey |  | fid |
| 2 | idx_er_allcheck_checkingnum |  | fcheckingbillnum |
