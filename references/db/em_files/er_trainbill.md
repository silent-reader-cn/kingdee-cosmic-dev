# 火车订单-er_trainbill

## 火车订单-主表 t_er_trainbill

- **表名称：** 火车订单-主表
- **表名：** t_er_trainbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | ftotalamount | 订单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 订单金额 |
| 4 | fordernum | 订单号 | varchar | 80 |  | √ | ' ' | 订单号 |
| 5 | fbookedcompany | 预订人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 7 | fisapprove | 审核通过 | bpchar | 1 |  | √ | ' ' | 审核通过 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fneedbilling | 需要开票 | bpchar | 1 |  | √ | ' ' | 需要开票 |
| 10 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 11 | fpaymentstatus | 支付状态 | varchar | 30 |  | √ | ' ' | 支付状态,枚举: WP :待支付 PP :支付中 PF :支付失败 PS :支付成功 |
| 12 | foperationtype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 |
| 13 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 14 | fserver | 服务商 | varchar | 30 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 |
| 15 | freimbursenum | 报销单号 | varchar | 100 |  | √ | ' ' | 报销单号 |
| 16 | fpassegerid | 乘客 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | forderstatus | 订单状态 | varchar | 30 |  | √ | ' ' | 订单状态,枚举: 1 :已出票 2 :已改签 3 :已退票 4 :出票失败 5 :出票失败退款 6 :改签中 7 :退票中 9999 :未知 |
| 18 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 19 | ftrdbizno | 第三方业务编号 | varchar | 160 |  | √ | ' ' | 第三方业务编号 |
| 20 | fparentordernum | 父订单号 | varchar | 80 |  | √ | ' ' | 父订单号 |
| 21 | fisconfirm | 已确认 | bpchar | 1 |  | √ | ' ' | 已确认 |
| 22 | fpassegerdept | 乘客部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 24 | foverdesc | 超标理由 | varchar | 255 |  | √ | ' ' | 超标理由 |
| 25 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 个人支付金额 |
| 26 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 27 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 29 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 30 | fserialno | 发票流水号 | varchar | 255 |  | √ | ' ' | 发票流水号 |
| 31 | fisreimburse | 已报销 | bpchar | 1 |  | √ | ' ' | 已报销 |
| 32 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 33 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 34 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | 'A' | 报销状态,枚举: A :未报销 B :报销中 C :已付款/已完成 |
| 35 | ffeedback | 错误反馈 | varchar | 255 |  | √ | '0' | 错误反馈 |
| 36 | fdownloadlink | 下载地址 | varchar | 500 |  | √ | ' ' | 下载地址 |
| 37 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fkddownloadlink | 内部下载地址 | varchar | 500 |  | √ | ' ' | 内部下载地址 |
| 39 | fidentityerrormsg | 发票识别异常信息 | varchar | 2000 |  | √ | ' ' | 发票识别异常信息 |
| 40 | foutordernum | 外部系统订单号 | varchar | 255 |  | √ | ' ' | 外部系统订单号 |
| 41 | fhappenddate | 费用发生时间 | timestamp | 0 |  |  | null | 费用发生时间 |
| 42 | fbookeddept | 预订人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 43 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国际 |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | foutaccountid | 商旅方系统拆账id | varchar | 255 |  | √ | ' ' | 商旅方系统拆账id |
| 47 | ftripid | 出差行程ID | varchar | 30 |  | √ | ' ' | 出差行程ID |
| 48 | fisverified | 已核销 | bpchar | 1 |  | √ | ' ' | 已核销 |
| 49 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 50 | fendorsementamount | 改签费 | numeric | 23 | 10 | √ | 0 | 改签费 |
| 51 | fisaddintegral | 加入低碳积分榜 | bpchar | 1 |  | √ | ' ' | 加入低碳积分榜 |
| 52 | fpaybillnum | 付款单号 | varchar | 80 |  | √ | ' ' | 付款单号 |
| 53 | fpassegername | 乘客姓名 | varchar | 100 |  | √ | ' ' | 乘客姓名 |
| 54 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 |
| 55 | fpricebillingtype | 票价开票类型 | varchar | 255 |  | √ | ' ' | 票价开票类型,枚举: 2 :增值税专用发票 1 :增值税普通发票 9999 :未知 3 :机票行程单 4 :火车票 28 :数电票（航空运输电子客票） 29 :数电票（铁路电子客票） |
| 56 | fexpcommitdepnum | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 57 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 58 | fisreconciliation | 已对账 | bpchar | 1 |  | √ | ' ' | 已对账 |
| 59 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 60 | fdealamount | 保险费 | numeric | 23 | 10 | √ | 0.0000000000 | 保险费 |
| 61 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 62 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 63 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 64 | ftrainticketnum | 火车票车票号 | varchar | 255 |  | √ | ' ' | 火车票车票号 |
| 65 | fproducttype | 结算类型 | bpchar | 1 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 66 | fbookedname | 预订人姓名 | varchar | 100 |  | √ | ' ' | 预订人姓名 |
| 67 | fnoticetimes | 通知次数 | int4 | 32 |  | √ | 0 | 通知次数 |
| 68 | fisbusiness | 订单性质 | bpchar | 1 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 69 | foriordernum | 原单订单号 | varchar | 80 |  | √ | ' ' | 原单订单号 |
| 70 | fexpcommitcomnum | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_trainbill_fordernum |  | foabillnum,fordernum |
| 2 | idx_er_tr_fsourcebookedid |  | fsourcebookedid |
| 3 | idx_er_tbill_org |  | fexpcommitcomnum,fcompanyid |
| 4 | t_er_trainbill_pkey |  | fid |
| 5 | idx_er_tfpassegerid |  | fpassegerid |

---

## 火车订单-分表 t_er_trainbill_a

- **表名称：** 火车订单-分表
- **表名：** t_er_trainbill_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | farrivecity | 到达城市 | varchar | 255 |  | √ | ' ' | 到达城市 |
| 3 | fticketprice | 火车票价 | numeric | 23 | 10 | √ | 0.0000000000 | 火车票价 |
| 4 | fdepartaddress | 出发车站 | varchar | 255 |  | √ | ' ' | 出发车站 |
| 5 | fvendorname | 车次 | varchar | 100 |  | √ | ' ' | 车次 |
| 6 | fdeparttime | 出发时间 | timestamp | 0 |  |  | null | 出发时间 |
| 7 | farriveaddress | 到达车站 | varchar | 255 |  | √ | ' ' | 到达车站 |
| 8 | farrivetime | 到达时间 | timestamp | 0 |  |  | null | 到达时间 |
| 9 | frefundamount | 退票费 | numeric | 23 | 10 | √ | 0.0000000000 | 退票费 |
| 10 | fdepartcity | 出发城市 | varchar | 255 |  | √ | ' ' | 出发城市 |
| 11 | ftrainseat | 席位 | bpchar | 1 |  | √ | ' ' | 席位,枚举: 1 :硬卧 2 :软卧 3 :无座 4 :硬座 5 :动卧 6 :高级软卧 7 :一等卧 8 :二等卧 9 :软座 A :特等座 B :商务座 C :一等座 D :二等座 E :其他 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_trainbill_a_index |  | fdeparttime |
| 2 | t_er_trainbill_a_pkey |  | fid |
| 3 | idx_er_trainbill_a_complex |  | fvendorname,fdepartaddress,farriveaddress,fdeparttime |
