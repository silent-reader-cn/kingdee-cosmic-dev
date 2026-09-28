# 单据对账-sim_reconciliation_sum

## 单据对账-主表 t_sim_reconciliation_sum

- **表名称：** 单据对账-主表
- **表名：** t_sim_reconciliation_sum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foriginalid | 开票申请单id | int8 | 64 |  | √ | 0 | 开票申请单id |
| 3 | ftotaltaxdiffer | 税额差值 | numeric | 23 | 10 | √ | 0 | 税额差值 |
| 4 | ftotalamount | 发票价税汇总 | numeric | 23 | 10 | √ | 0 | 发票价税汇总 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fbilldate | 单据日期 | timestamp | 0 |  |  | null | 单据日期 |
| 7 | forigtotalamount | 申请价税汇总 | numeric | 23 | 10 | √ | 0 | 申请价税汇总 |
| 8 | ftotaltax | 发票税额汇总 | numeric | 23 | 10 | √ | 0 | 发票税额汇总 |
| 9 | finvoicetype | finvoicetype | varchar | 10 |  | √ | ' ' |  |
| 10 | finvoiceamount | 发票金额汇总 | numeric | 23 | 10 | √ | 0 | 发票金额汇总 |
| 11 | ftotalamountdiffer | 价税合计差值 | numeric | 23 | 10 | √ | 0 | 价税合计差值 |
| 12 | forigtotaltax | 申请税额汇总 | numeric | 23 | 10 | √ | 0 | 申请税额汇总 |
| 13 | fbuyername | 购方名称 | varchar | 150 |  | √ | ' ' | 购方名称 |
| 14 | finvoiceamountdiffer | 金额差值 | numeric | 23 | 10 | √ | 0 | 金额差值 |
| 15 | fbillno | 申请单编号 | varchar | 50 |  | √ | ' ' | 申请单编号 |
| 16 | foriginvoiceamount | 申请金额汇总 | numeric | 23 | 10 | √ | 0 | 申请金额汇总 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_reconciliation_sum |  | fid |
| 2 | idx_sim_reconciliation_sum |  | forgid |

---

## 发票信息-子表 t_sim_reconciliation_item

- **表名称：** 发票信息-子表
- **表名：** t_sim_reconciliation_item

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 3 | finvoicetype | 发票种类 | varchar | 10 |  | √ | ' ' | 发票种类,枚举: 026 :电子普通发票 028 :电子专用发票 007 :纸质普通发票 004 :纸质专用发票 005 :机动车发票 006 :二手车发票 08xdp :全电发票（增值税专用发票） 10xdp :全电发票（普通发票） |
| 4 | fissuetime | 开票日期 | timestamp | 0 |  |  | null | 开票日期 |
| 5 | finvoicestatus | 发票状态 | varchar | 10 |  | √ | ' ' | 发票状态,枚举: 0 :正常 3 :红冲 6 :作废 |
| 6 | finvoiceid | 发票id | int8 | 64 |  | √ | 0 | 发票id |
| 7 | finvoicecode | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | finvoiceno | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sim_reconciliation_item |  | fentryid |
| 2 | idx_sim_reconciliation_item |  | fid |
