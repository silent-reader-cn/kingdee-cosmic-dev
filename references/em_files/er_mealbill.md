# 用餐订单-er_mealbill

## 用餐订单-主表 t_er_mealbill

- **表名称：** 用餐订单-主表
- **表名：** t_er_mealbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftotalamount | 订单金额 | numeric | 23 | 10 | √ | 0 | 订单金额 |
| 4 | fordernum | 订单号 | varchar | 50 |  | √ | ' ' | 订单号 |
| 5 | fmealcityname | 用餐城市 | varchar | 255 |  | √ | ' ' | 用餐城市 |
| 6 | fbookedcompany | 预订人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fisapprove | 是否审核通过 | bpchar | 1 |  | √ | '0' | 是否审核通过 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 10 | foperationtype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 7 :服务费 8 :用餐 |
| 11 | fserver | 服务商 | varchar | 50 |  | √ | ' ' | 服务商,枚举: CHAILVYIHAO :差旅壹号 MEITUAN :美团商企通 |
| 12 | freimbursenum | 报销单号 | varchar | 80 |  | √ | ' ' | 报销单号 |
| 13 | forderstatus | 订单状态 | varchar | 50 |  | √ | ' ' | 订单状态,枚举: PAY :已支付 PART_REFUND :部分退款 ALL_REFUND :全额退款 9999 :未知 |
| 14 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 15 | fparentordernum | 父订单号 | varchar | 50 |  | √ | ' ' | 父订单号 |
| 16 | fisconfirm | 是否确认 | bpchar | 1 |  | √ | '0' | 是否确认 |
| 17 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 18 | foverdesc | 超标理由 | varchar | 255 |  | √ | ' ' | 超标理由 |
| 19 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0 | 个人支付金额 |
| 20 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 21 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 22 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 23 | fisreimburse | 是否报销 | bpchar | 1 |  | √ | '0' | 是否报销 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 26 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | ' ' | 报销状态,枚举: A :未报销 B :报销中 C :已付款 |
| 27 | ffeedback | 错误反馈 | varchar | 255 |  | √ | ' ' | 错误反馈 |
| 28 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | fhappenddate | 费用发生时间 | timestamp | 0 |  |  | null | 费用发生时间 |
| 30 | fshopaddress | 店铺地址 | varchar | 255 |  | √ | ' ' | 店铺地址 |
| 31 | fbookeddept | 预订人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 34 | ftripid | 出差行程ID | varchar | 30 |  | √ | ' ' | 出差行程ID |
| 35 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0 | 服务费 |
| 36 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 er_mealapplication_bill :用餐申请单 |
| 37 | fexpcommitdepnum | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 38 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 39 | fisreconciliation | 是否对账 | bpchar | 1 |  | √ | '0' | 是否对账 |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fshopname | 店铺名称 | varchar | 255 |  | √ | ' ' | 店铺名称 |
| 42 | fmealtime | 用餐日期 | timestamp | 0 |  |  | null | 用餐日期 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 46 | fproducttype | 结算类型 | bpchar | 1 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 47 | fbookedname | 预订人姓名 | varchar | 50 |  | √ | ' ' | 预订人姓名 |
| 48 | fnoticetimes | 通知次数 | int4 | 32 |  | √ | 0 | 通知次数 |
| 49 | fisbusiness | 订单性质 | bpchar | 1 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 50 | foriordernum | 原单订单号 | varchar | 100 |  | √ | ' ' | 原单订单号 |
| 51 | fdinnerscene | 用餐场景 | bpchar | 1 |  | √ | ' ' | 用餐场景,枚举: 1 :商务宴请 3 :差旅用餐 5 :团建用餐 4 :工作用餐 6 :招待用餐 7 :会议用餐 9 :福利用餐 |
| 52 | fexpcommitcomnum | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_mealbill |  | fid |
| 2 | idx_er_mbbillno |  | foabillnum |
| 3 | idx_er_mbfsourcebookedid |  | fsourcebookedid |
| 4 | idx_er_mbill_org |  | fexpcommitcomnum,fbookedcompany |
