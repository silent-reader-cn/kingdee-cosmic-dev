# 用餐结算单-er_mealcheckingbill

## 用餐结算单-多语言表 t_er_mealcheckingbill_l

- **表名称：** 用餐结算单-多语言表
- **表名：** t_er_mealcheckingbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbalanceremark | 置平备注 | varchar | 1000 |  | √ | ' ' | 置平备注 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 50 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_mealcheckingbill_l |  | fid,flocaleid |
| 2 | pk_t_er_mealcheckingbill_l |  | fpkid |

---

## 用餐结算单-主表 t_er_mealcheckingbill

- **表名称：** 用餐结算单-主表
- **表名：** t_er_mealcheckingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frefunddeductrate | 退票费税率(%) | numeric | 23 | 10 | √ | 0 | 退票费税率(%) |
| 3 | forgid | 预订人部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | ftotalamount | 结算金额 | numeric | 23 | 10 | √ | 0 | 结算金额 |
| 5 | fordernum | 结算单号 | varchar | 80 |  | √ | ' ' | 结算单号 |
| 6 | fisbalance | 已对平 | bpchar | 1 |  | √ | '0' | 已对平,枚举: 1 :平 2 :不平 3 :废弃 |
| 7 | fmealcityname | 用餐城市 | varchar | 255 |  | √ | ' ' | 用餐城市 |
| 8 | fisdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 9 | fpaybillstatus | 付款状态 | bpchar | 1 |  | √ | ' ' | 付款状态,枚举: 0 :等待付款 1 :已付款 |
| 10 | frefundamounttax | 退票费税额 | numeric | 23 | 10 | √ | 0 | 退票费税额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fservicedeductrate | 服务费税率(%) | numeric | 23 | 10 | √ | 0 | 服务费税率(%) |
| 13 | fstdcostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | [成本中心 bos_costcenter](../basedata_files/bos_costcenter.md) |
| 14 | foperationtype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 8 :用餐 |
| 15 | fserver | 服务商 | varchar | 50 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 MEITUAN :美团商企通 TONGCHENG :同程 ALI :阿里商旅 QICHENG :企橙 MEIYA :美亚 MEITUAN_NEW :美团商企通 |
| 16 | freimbursenum | freimbursenum | varchar | 80 |  | √ | ' ' |  |
| 17 | forderstatus | 订单状态 | varchar | 50 |  | √ | ' ' | 订单状态,枚举: PAY :已支付 PART_REFUND :部分退款 ALL_REFUND :全额退款 9999 :未知 |
| 18 | ftotaltaxrate | 可抵扣税率 | numeric | 23 | 10 | √ | 0 | 可抵扣税率 |
| 19 | fordertype | 订单类型 | varchar | 50 |  | √ | ' ' | 订单类型,枚举: O :原始单 G :改签单 T :退票单 C :调整单 |
| 20 | fparentordernum | 父订单号 | varchar | 50 |  | √ | ' ' | 父订单号 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fpersonalfee | 个人支付金额 | numeric | 23 | 10 | √ | 0 | 个人支付金额 |
| 23 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :未审核 C :已审核 |
| 25 | fbatchno | 结算批次号 | varchar | 80 |  | √ | ' ' | 结算批次号 |
| 26 | fservicefeepaytype | 服务费结算类型 | bpchar | 1 |  | √ | ' ' | 服务费结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 27 | forderdate | 订单日期 | timestamp | 0 |  |  | null | 订单日期 |
| 28 | fpushcount | 下推计数 | int4 | 32 |  | √ | 0 | 下推计数 |
| 29 | fvouchernum | 凭证号 | varchar | 80 |  | √ | ' ' | 凭证号 |
| 30 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 31 | freimbillformid | 报销单表单id | varchar | 50 |  | √ | ' ' | 报销单表单id,枚举: er_tripreimbursebill :差旅报销单 er_dailyreimbursebill :费用报销单 er_publicreimbursebill :对公报销单 |
| 32 | freimbursestatus | 报销状态 | bpchar | 1 |  | √ | ' ' | 报销状态,枚举: A :未报销 B :报销中 C :已付款/已完成 |
| 33 | fsourcebookedid | 预订人工号 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fperiod | 期间 | varchar | 50 |  | √ | ' ' | 期间 |
| 35 | fhappenddate | 结算发生日期 | timestamp | 0 |  |  | null | 结算发生日期 |
| 36 | fshopaddress | 店铺地址 | varchar | 255 |  | √ | ' ' | 店铺地址 |
| 37 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 38 | fordersort | 订单分类 | varchar | 30 |  | √ | ' ' | 订单分类,枚举: 1 :国内 2 :国际 |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | faccountid | 主账户ID | varchar | 50 |  | √ | ' ' | 主账户ID |
| 41 | fcompanyid | 预订人公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | fbillperiod | 差旅壹号账期 | timestamp | 0 |  |  | null | 差旅壹号账期 |
| 43 | foutaccountid | 商旅方系统拆账id | varchar | 255 |  | √ | ' ' | 商旅方系统拆账id |
| 44 | fsettlementamount | 结算金额 | numeric | 23 | 10 | √ | 0 | 结算金额 |
| 45 | fservicefee | 服务费 | numeric | 23 | 10 | √ | 0 | 服务费 |
| 46 | forderdeductrate | 票价税率(%) | numeric | 23 | 10 | √ | 0 | 票价税率(%) |
| 47 | fpaybillnum | 付款/付款申请单号 | varchar | 80 |  | √ | ' ' | 付款/付款申请单号 |
| 48 | foabillformid | 申请单表单id | varchar | 50 |  | √ | ' ' | 申请单表单id,枚举: er_tripreqbill :出差申请单 er_dailyapplybill :费用申请单 er_mealapplication_bill :用餐申请单 |
| 49 | ftotaltax | 可抵扣税额 | numeric | 23 | 10 | √ | 0 | 可抵扣税额 |
| 50 | foabillnum | 申请单号 | varchar | 80 |  | √ | ' ' | 申请单号 |
| 51 | fisreconciliation | 已对账 | bpchar | 1 |  | √ | '0' | 已对账 |
| 52 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 53 | fhasinvoice | 已开票 | bpchar | 1 |  | √ | '0' | 已开票,枚举: 1 :是 0 :否 2 :开票中 |
| 54 | fshopname | 店铺名称 | varchar | 255 |  | √ | ' ' | 店铺名称 |
| 55 | fmealtime | 用餐时间 | timestamp | 0 |  |  | null | 用餐时间 |
| 56 | fformid | 表单ID | varchar | 50 |  | √ | ' ' | 表单ID |
| 57 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 58 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 59 | fcurrency | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 60 | fserviceamounttax | 服务费税额 | numeric | 23 | 10 | √ | 0 | 服务费税额 |
| 61 | fpaybillid | 付款/付款申请单id | int8 | 64 |  | √ | 0 | 付款/付款申请单id |
| 62 | fproducttype | 结算类型 | varchar | 50 |  | √ | ' ' | 结算类型,枚举: 1 :公司月结 2 :个人现付 3 :公司预存 |
| 63 | fbookedname | 预订人 | varchar | 50 |  | √ | ' ' | 预订人 |
| 64 | fsettlemain | 费用承担公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 65 | fisbusiness | 订单性质 | varchar | 50 |  | √ | ' ' | 订单性质,枚举: 1 :因公 2 :因私 |
| 66 | fallorderbaseid | 订单总表数据 | int8 | 64 |  | √ | 0 | [全部订单 er_allorderbill](../em_files/er_allorderbill.md) |
| 67 | fdinnerscene | 用餐场景 | varchar | 50 |  | √ | ' ' | 用餐场景,枚举: 1 :商务宴请 3 :差旅用餐 5 :团建用餐 4 :工作用餐 6 :招待用餐 7 :会议用餐 9 :福利用餐 9999 :其他 |
| 68 | fsettledept | 费用承担部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 69 | fbalanceremark | 置平备注 | varchar | 500 |  | √ | ' ' | 置平备注 |
| 70 | forderamounttax | 票价税额 | numeric | 23 | 10 | √ | 0 | 票价税额 |
| 71 | forderisinvoicerep | 需要开票 | bpchar | 1 |  | √ | '0' | 需要开票 |
| 72 | foutsettlementnum | 外部系统结算单号 | varchar | 255 |  | √ | ' ' | 外部系统结算单号 |
| 73 | fcheckingbillnum | 账单编号 | varchar | 80 |  | √ | ' ' | 账单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_mealcheckingbill_billno |  | fordernum,fserver |
| 2 | pk_t_er_mealcheckingbill |  | fid |
| 3 | idx_er_mealcheckingbill_org |  | fcompanyid,fsettlemain |
