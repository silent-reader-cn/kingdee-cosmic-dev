# 火车订单-er_trainbill

## 火车订单-主表 t_er_trainbill

- **表名称：** 火车订单-主表
- **表名：** t_er_trainbill

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
| 11 | fpaymentstatus | 支付状态 | varchar | 30 |  | √ | ' ' | 支付状态,枚举: WP :待支付 PP :支付中 PF :支付失败 PS :支付成功 |
| 12 | foperationtype | 业务类型 | bpchar | 1 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 |
| 13 | fbookeddate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 14 | fserver | 服务商 | varchar | 30 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 |
| 15 | freimbursenum | 报销单号 | varchar | 100 |  | √ | ' ' | 报销单号 |
| 16 | fpassegerid | 乘客 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | forderstatus | 订单状态 | varchar | 30 |  | √ | ' ' | 订单状态,枚举: 1 :已出票 2 :已改签 3 :已退票 4 :出票失败 5 :出票失败退款 6 :改签中 7 :退票中 9999 :未知 |
| 18 | fordertype | 订单类型 | bpchar | 1 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 19 | fparentordernum | 父订单号 | varchar | 80 |  | √ | ' ' | 父订单号 |
| 20 | fisconfirm | 是否确认 | bpchar | 1 |  | √ | ' ' | 是否确认 |
| 21 | fpassegerdept | 乘客部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fbillno | 单据编号 | varchar | 100 |  | √ | ' ' | 单据编号 |
| 23 | foverdesc | 超标理由 | varchar | 255 |  | √ | ' ' | 超标理由 |
| 24 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0.0000000000 | 个人支付金额 |
| 25 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 27 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 28 | fserialno | 发票流水号 | varchar | 255 |  | √ | ' ' | 发票流水号 |
| 29 | fisreimburse | 是否报销 | bpchar | 1 |  | √ | ' ' | 是否报销 |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 32 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | 'A' | 报销状态,枚举: A :未报销 B :报销中 C :已付款 |
| 33 | ffeedback | 错误反馈 | varchar | 255 |  | √ | '0' | 错误反馈 |
| 34 | fdownloadlink | 下载地址 | varchar | 500 |  | √ | ' ' | 下载地址 |
| 35 | fsourcebookedid | 预订人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fkddownloadlink | 内部下载地址 | varchar | 500 |  | √ | ' ' | 内部下载地址 |
| 37 | fidentityerrormsg | 发票识别异常信息 | varchar | 2000 |  | √ | ' ' | 发票识别异常信息 |
| 38 | fhappenddate | 费用发生时间 | timestamp | 0 |  |  | null | 费用发生时间 |
| 39 | fbookeddept | 预订人部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国际 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fcompanyid | 申请人公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 43 | ftripid | 出差行程ID | varchar | 30 |  | √ | ' ' | 出差行程ID |
| 44 | fisverified | 是否核销 | bpchar | 1 |  | √ | ' ' | 是否核销 |
| 45 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 46 | fisaddintegral | 是否加入低碳积分榜 | bpchar | 1 |  | √ | ' ' | 是否加入低碳积分榜 |
| 47 | fpaybillnum | 付款单号 | varchar | 80 |  | √ | ' ' | 付款单号 |
| 48 | fpassegername | 乘客姓名 | varchar | 100 |  | √ | ' ' | 乘客姓名 |
| 49 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 |
| 50 | fexpcommitdepnum | 费用承担部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 51 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 52 | fisreconciliation | 是否对账 | bpchar | 1 |  | √ | ' ' | 是否对账 |
| 53 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 54 | fdealamount | 保险费 | numeric | 23 | 10 | √ | 0.0000000000 | 保险费 |
| 55 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 56 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 57 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 58 | ftrainticketnum | 火车票车票号 | varchar | 255 |  | √ | ' ' | 火车票车票号 |
| 59 | fproducttype | 结算类型 | bpchar | 1 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 60 | fbookedname | 预订人姓名 | varchar | 100 |  | √ | ' ' | 预订人姓名 |
| 61 | fnoticetimes | 通知次数 | int4 | 32 |  | √ | 0 | 通知次数 |
| 62 | fisbusiness | 订单性质 | bpchar | 1 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 63 | foriordernum | 原单订单号 | varchar | 80 |  | √ | ' ' | 原单订单号 |
| 64 | fexpcommitcomnum | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_trainbill_fordernum |  | foabillnum,fordernum |
| 2 | idx_er_tr_fsourcebookedid |  | fsourcebookedid |
| 3 | t_er_trainbill_pkey |  | fid |
| 4 | idx_er_tbill_org |  | fexpcommitcomnum,fcompanyid |

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
