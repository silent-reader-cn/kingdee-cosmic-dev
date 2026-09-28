# 开票申请-er_invoiceorderbill

## 开票申请-主表 t_er_invoiceorderbill

- **表名称：** 开票申请-主表
- **表名：** t_er_invoiceorderbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fserviceitem | 服务项目 | varchar | 30 |  | √ | ' ' | 服务项目 |
| 3 | fvatcominvoicenum | 增值税普票号码 | varchar | 100 |  | √ | ' ' | 增值税普票号码 |
| 4 | finvoicestatus | 开票状态 | bpchar | 1 |  | √ | ' ' | 开票状态,枚举: 1 :未推送 2 :开票中 3 :已开票 5 :开票失败 6 :可开票余额不足 7 :开票数据异常 |
| 5 | ftrdinvoiceid | 商旅系统开票单号 | varchar | 100 |  | √ | ' ' | 商旅系统开票单号 |
| 6 | ftotalamount | 总金额 | numeric | 23 | 10 | √ | 0.0000000000 | 总金额 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fvatcominvoicecode | 增值税普票代码 | varchar | 100 |  | √ | ' ' | 增值税普票代码 |
| 9 | finvoicenum | 发票号码 | varchar | 30 |  | √ | ' ' | 发票号码 |
| 10 | finvoicestatustime | 开票单状态时间 | timestamp | 0 |  |  | null | 开票单状态时间 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fserviceamount | 服务费 | numeric | 23 | 10 | √ | 0.0000000000 | 服务费 |
| 13 | finvoicetax | 可抵扣税额 | numeric | 23 | 10 | √ | 0.0000000000 | 可抵扣税额 |
| 14 | fdiffamountwithtax | 差异金额（含税） | numeric | 23 | 10 | √ | 0.0000000000 | 差异金额（含税） |
| 15 | fvatdednvoicecode | 增值税专票代码 | varchar | 100 |  | √ | ' ' | 增值税专票代码 |
| 16 | fsettleamounttax | 结算合计税额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算合计税额 |
| 17 | foperationtype | 服务类型 | bpchar | 1 |  | √ | '0' | 服务类型,枚举: 1 :国内酒店 2 :国内机票 3 :国内用车 4 :国际机票 5 :国际酒店 6 :国内火车 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fsettleamountwithtax | 结算合计金额（含税） | numeric | 23 | 10 | √ | 0.0000000000 | 结算合计金额（含税） |
| 20 | fserver | 服务商 | varchar | 100 |  |  | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 GAODE :高德 MEITUAN :美团 QICHENG :企橙 MEIYA :美亚 |
| 21 | finvoicedate | 开票申请日期 | timestamp | 0 |  |  | null | 开票申请日期 |
| 22 | finvoicecode | 发票代码 | varchar | 30 |  | √ | ' ' | 发票代码 |
| 23 | fbillno | 开票申请单号 | varchar | 30 |  | √ | ' ' | 开票申请单号 |
| 24 | ftaxamount | 抵扣税额(商旅) | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额(商旅) |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :未审核 C :已审核 |
| 27 | fbatchno | 批次号 | varchar | 100 |  | √ | ' ' | 批次号 |
| 28 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 29 | fsystemtaxrate | 系统税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 系统税率（%） |
| 30 | fvouchernum | 凭证号码 | varchar | 80 |  | √ | ' ' | 凭证号码 |
| 31 | finvoiceheadnametype | 发票摘要 | varchar | 10 |  | √ | ' ' | 发票摘要,枚举: 0 :机票住宿费 1 :机票费 2 :退票费 3 :代理服务费 4 :机票签证费 5 :机票用车费 6 :商旅服务费 9 :代订住宿费 10 :保险费 11 :*运输服务*客运服务费 16 :代订用车费 7 :火车票 12 :经济代理*代订餐费 13 :经济代理*服务费 |
| 32 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 33 | fhassend | 推送 | bpchar | 1 |  | √ | ' ' | 推送 |
| 34 | fvatdednvoicenum | 增值税专票号码 | varchar | 100 |  | √ | ' ' | 增值税专票号码 |
| 35 | fsystaxamount | 抵扣税额(系统) | numeric | 23 | 10 | √ | 0.0000000000 | 抵扣税额(系统) |
| 36 | finvoicetype | 开票类型 | varchar | 50 |  | √ | ' ' | 开票类型,枚举: 0 :增值税普通发票（纸质） 1 :增值税专用发票（纸质） 2 :增值税普通发票（电子） 3 :机票行程单 4 :火车票 5 :定额发票 6 :增值税专用发票（电子） |
| 37 | finvoiceamount | 发票金额（含税） | numeric | 23 | 10 | √ | 0.0000000000 | 发票金额（含税） |
| 38 | finvoicetaxrate | 发票税率（%） | numeric | 23 | 10 | √ | 0.0000000000 | 发票税率（%） |
| 39 | forderamount | 订单金额 | numeric | 23 | 10 | √ | 0.0000000000 | 订单金额 |
| 40 | fexpcommitcomnum | 开票公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 41 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fdifftaxamount | 差异税额 | numeric | 23 | 10 | √ | 0.0000000000 | 差异税额 |
| 44 | faccountid | 主账户id | varchar | 30 |  | √ | ' ' | 主账户id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_iob_finvoicedate |  | finvoicedate |
| 2 | t_er_invoiceorderbill_pkey |  | fid |
