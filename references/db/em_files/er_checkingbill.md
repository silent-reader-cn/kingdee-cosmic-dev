# 月结账单-er_checkingbill

## 发票信息-子表 t_er_checkinginvoice

- **表名称：** 发票信息-子表
- **表名：** t_er_checkinginvoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 3 | ffromcity | 出发地 | varchar | 500 |  | √ | ' ' | 出发地 |
| 4 | fflightitineraryandtrain | 是否行程单/火车票 | bpchar | 1 |  | √ | '0' | 是否行程单/火车票 |
| 5 | fmakeoutcompname | 开票公司 | varchar | 250 |  | √ | ' ' | 开票公司 |
| 6 | finnerdownloadurl | 内部下载地址 | varchar | 1500 |  | √ | ' ' | 内部下载地址 |
| 7 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 8 | fcheckingbillno | 结算单号 | varchar | 50 |  | √ | ' ' | 结算单号 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fpassengername | 旅客 | varchar | 255 |  | √ | ' ' | 旅客 |
| 11 | fbuyerorgid | 收票公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | finvoicetype | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型,枚举: 0 :增值税普通发票（纸质） 1 :增值税专用发票（纸质） 2 :增值税普通发票（电子） 3 :增值税专用发票（电子） 4 :机票行程单 5 :火车票 6 :定额发票 7 :区块链电子发票 8 :数电发票（增值税专用发票） 9 :数电发票（增值税普通发票） 999 :其他 |
| 13 | ftocity | 目的地 | varchar | 500 |  | √ | ' ' | 目的地 |
| 14 | fdownloadurl | 下载地址 | varchar | 1500 |  | √ | ' ' | 下载地址 |
| 15 | finvoicecode | 发票代码 | varchar | 255 |  | √ | ' ' | 发票代码 |
| 16 | fbuyername | 收票公司 | varchar | 250 |  | √ | ' ' | 收票公司 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | finvoiceno | 发票号码 | varchar | 255 |  | √ | ' ' | 发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_er_checkinginvoice |  | fentryid |
| 2 | idx_invoice_fid |  | fid |
| 3 | idx_invoice_finvoiceno |  | finvoiceno,fcheckingbillno |
| 4 | idx_invoice_fcheckingno |  | fcheckingbillno |
| 5 | idx_invoice_finvoicecode |  | finvoicecode,fcheckingbillno |

---

## 月结账单-主表 t_er_checkingbill

- **表名称：** 月结账单-主表
- **表名：** t_er_checkingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fperiodstartdate | 账单起始日 | timestamp | 0 |  |  | null | 账单起始日 |
| 3 | fsettlementamount | 结算金额 | numeric | 23 | 10 | √ | 0.0000000000 | 结算金额 |
| 4 | paybillid | paybillid | int8 | 64 |  | √ | 0 |  |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fresult | 对账结果 | varchar | 30 |  | √ | ' ' | 对账结果,枚举: 1 :平 2 :不平 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fisreconciliation | 是否对账 | bpchar | 1 |  | √ | '0' | 是否对账 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | foperationtype | 服务类型 | bpchar | 1 |  | √ | ' ' | 服务类型,枚举: 2 :国内机票 4 :国际机票 1 :国内酒店 5 :国际酒店 3 :用车预订 6 :火车预订 8 :用餐预订 |
| 11 | fserver | 服务商 | varchar | 100 |  | √ | ' ' | 服务商,枚举: ZHONGXING :中兴 XIECHENG :携程 CHAILVYIHAO :差旅壹号 DIDI :滴滴 |
| 12 | fbillnum | 账单编码 | varchar | 80 |  | √ | ' ' | 账单编码 |
| 13 | fperiodenddate | 账单截止日 | timestamp | 0 |  |  | null | 账单截止日 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fformid | 表单ID | varchar | 100 |  | √ | ' ' | 表单ID |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fsettlemain | 费用承担公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fiscreatevoucher | 是否生成凭证 | bpchar | 1 |  | √ | '0' | 是否生成凭证 |
| 23 | fbillstatusname | 账单状态 | varchar | 100 |  | √ | ' ' | 账单状态,枚举: 1 :未审核 2 :已审核 3 :已确认 |
| 24 | fpaybillwriteback | fpaybillwriteback | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 25 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fperiodenddate |  | fperiodenddate |
| 2 | idx_er_checkingbill |  | fbillno |
| 3 | t_er_checkingbill_pkey |  | fid |
| 4 | idx_fperiodstartdate |  | fperiodstartdate |
