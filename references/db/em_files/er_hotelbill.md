# 酒店订单-er_hotelbill

## 酒店订单-主表 t_er_hotelbill

- **表名称：** 酒店订单-主表
- **表名：** t_er_hotelbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftotalamount | 订单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 订单金额 |
| 3 | fordernum | 订单号 | varchar | 100 |  | √ | ' ' | 订单号 |
| 4 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 5 | fisapprove | 审核通过 | bpchar | 1 |  | √ | '0' | 审核通过 |
| 6 | ftravelername | 入住人 | varchar | 100 |  | √ | ' ' | 入住人 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fneedbilling | 需要开票 | bpchar | 1 |  | √ | '1' | 需要开票 |
| 9 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 10 | fvatdednvoicecode | fvatdednvoicecode | varchar | 100 |  | √ | ' ' |  |
| 11 | foperationtype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 |
| 12 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 13 | fserver | 服务商 | varchar | 100 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 |
| 14 | freimbursenum | 报销单号 | varchar | 100 |  | √ | ' ' | 报销单号 |
| 15 | forderstatus | 订单状态 | varchar | 100 |  | √ | ' ' | 订单状态,枚举: 1 :待审批 2 :待支付 3 :待确认 5 :已确认 6 :满房 7 :已离店 8 :待退订 10 :已退订 14 :已取消 9999 :未知 |
| 16 | fordertype | 订单类型 | varchar | 100 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 17 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 18 | fparentordernum | 父订单号 | varchar | 100 |  | √ | ' ' | 父订单号 |
| 19 | fisconfirm | 已确认 | bpchar | 1 |  | √ | '0' | 已确认 |
| 20 | fhotelname | 酒店名称 | varchar | 100 |  | √ | ' ' | 酒店名称 |
| 21 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 22 | foverdesc | 超标理由 | varchar | 100 |  | √ | ' ' | 超标理由 |
| 23 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 个人支付金额 |
| 24 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 25 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 27 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 28 | fisreimburse | 已报销 | bpchar | 1 |  | √ | '0' | 已报销 |
| 29 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 30 | fvatdednvoicenum | fvatdednvoicenum | varchar | 100 |  | √ | ' ' |  |
| 31 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 32 | fcheckoutdate | 离店日期 | timestamp | 0 |  |  | null | 离店日期 |
| 33 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | 'A' | 报销状态,枚举: A :未报销 B :报销中 C :已付款/已完成 |
| 34 | ffeedback | 错误反馈 | varchar | 255 |  | √ | '0' | 错误反馈 |
| 35 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | froomcount | 订房间数 | numeric | 23 | 10 | √ | 0.0000000000 | 订房间数 |
| 37 | foutordernum | 外部系统订单号 | varchar | 255 |  | √ | ' ' | 外部系统订单号 |
| 38 | funbookfee | 退订费 | numeric | 23 | 10 | √ | 0.0000000000 | 退订费 |
| 39 | fhappenddate | 费用发生时间 | timestamp | 0 |  |  | null | 费用发生时间 |
| 40 | froomamount | 房价 | numeric | 23 | 10 | √ | 0.0000000000 | 房价 |
| 41 | fbookeddept | 预订人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国际 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fhoteladdress | 酒店地址 | varchar | 255 |  | √ | ' ' | 酒店地址 |
| 46 | foutaccountid | 商旅方系统拆账id | varchar | 255 |  | √ | ' ' | 商旅方系统拆账id |
| 47 | ftravelerdept | 入住人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 48 | ftripid | 出差行程ID | varchar | 100 |  | √ | ' ' | 出差行程ID |
| 49 | fvatcominvoicenum | fvatcominvoicenum | varchar | 100 |  | √ | ' ' |  |
| 50 | fisverified | 已核销 | bpchar | 1 |  | √ | '0' | 已核销 |
| 51 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 52 | fvatcominvoicecode | fvatcominvoicecode | varchar | 100 |  | √ | ' ' |  |
| 53 | fcityname | 城市 | varchar | 100 |  | √ | ' ' | 城市 |
| 54 | froomstylename | 房型 | varchar | 255 |  | √ | ' ' | 房型 |
| 55 | fisaddintegral | 加入低碳积分榜 | bpchar | 1 |  | √ | '0' | 加入低碳积分榜 |
| 56 | fsourcetravelerid | 入住人工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 57 | fpaybillnum | 付款单号 | varchar | 100 |  | √ | ' ' | 付款单号 |
| 58 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 |
| 59 | fpricebillingtype | 票价开票类型 | varchar | 10 |  | √ | ' ' | 票价开票类型,枚举: 2 :增值税专用发票 1 :增值税普通发票 9999 :未知 |
| 60 | forderstatusname | 订单状态名称 | varchar | 100 |  | √ | ' ' | 订单状态名称 |
| 61 | fexpcommitdepnum | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 62 | foabillnum | 申请单号 | varchar | 100 |  | √ | ' ' | 申请单号 |
| 63 | fisreconciliation | 已对账 | bpchar | 1 |  | √ | '0' | 已对账 |
| 64 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 65 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 66 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 67 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 68 | fproducttype | 结算类型 | varchar | 100 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 69 | fbookedname | 预订人姓名 | varchar | 100 |  | √ | ' ' | 预订人姓名 |
| 70 | fnoticetimes | 通知次数 | int4 | 32 |  | √ | 0 | 通知次数 |
| 71 | fisbusiness | 订单性质 | varchar | 100 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 72 | foriordernum | 原单订单号 | varchar | 100 |  | √ | ' ' | 原单订单号 |
| 73 | fcheckindate | 入住日期 | timestamp | 0 |  |  | null | 入住日期 |
| 74 | fexpcommitcomnum | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_hbfsourcebookedid |  | fsourcebookedid |
| 2 | idx_er_hbill_org |  | fexpcommitcomnum,fcompanyid |
| 3 | idx_er_hbbillno |  | foabillnum |
| 4 | t_er_hotelbill_pkey |  | fid |
| 5 | idx_er_hotel_org_time |  | fcheckindate,fexpcommitcomnum,fexpcommitdepnum |
| 6 | idx_er_hfsourcetravelerid |  | fsourcetravelerid |
