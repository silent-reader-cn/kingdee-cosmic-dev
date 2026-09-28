# 进项转出登记-tcvat_input_rollout

## 进项转出登记-分表 t_tdm_invoice_input_a

- **表名称：** 进项转出登记-分表
- **表名：** t_tdm_invoice_input_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisgeneratevoucher | fisgeneratevoucher | varchar | 50 |  | √ | ' ' |  |
| 3 | finvoicearriveder | finvoicearriveder | varchar | 50 |  | √ | ' ' |  |
| 4 | ftaxperioddate | ftaxperioddate | timestamp | 0 |  |  | null |  |
| 5 | freceiptdate | freceiptdate | timestamp | 0 |  |  | null |  |
| 6 | foriginalinvoiceno | foriginalinvoiceno | varchar | 100 |  | √ | ' ' |  |
| 7 | fsourcesys | fsourcesys | varchar | 50 |  | √ | ' ' |  |
| 8 | finvoicearrivedstatus | finvoicearrivedstatus | varchar | 50 |  | √ | ' ' |  |
| 9 | feffectivetaxamount | feffectivetaxamount | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 10 | freceipter | freceipter | varchar | 50 |  | √ | ' ' |  |
| 11 | fcertstatus | fcertstatus | varchar | 50 |  | √ | ' ' |  |
| 12 | fselectresult | fselectresult | varchar | 50 |  | √ | ' ' |  |
| 13 | fopentype | fopentype | varchar | 30 |  | √ | ' ' |  |
| 14 | foriginalinvoicecode | foriginalinvoicecode | varchar | 100 |  | √ | ' ' |  |
| 15 | fauthdate | fauthdate | timestamp | 0 |  |  | null |  |
| 16 | fbaseinvoicetype | 发票类型 | int8 | 64 |  | √ | 0 | 发票类型 bd_invoicetype |
| 17 | fsignstatus | fsignstatus | varchar | 50 |  | √ | ' ' |  |
| 18 | fselectstatus | fselectstatus | varchar | 50 |  | √ | ' ' |  |
| 19 | fdatasource | fdatasource | varchar | 50 |  | √ | ' ' |  |
| 20 | fsenddate | fsenddate | timestamp | 0 |  |  | null |  |
| 21 | finvoicearriveddate | finvoicearriveddate | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tdm_invoice_input_a_pkey |  | fid |
| 2 | idx_tdm_invoice_input_a |  | foriginalinvoicecode,foriginalinvoiceno |
| 3 | idx_tdm_invoice_input_a2 |  | fbaseinvoicetype |

---

## 进项转出登记-主表 t_tdm_invoice_input

- **表名称：** 进项转出登记-主表
- **表名：** t_tdm_invoice_input

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finvaliddate | finvaliddate | timestamp | 0 |  |  | null |  |
| 3 | fdrawer | fdrawer | varchar | 100 |  | √ | ' ' |  |
| 4 | ftotalamount | 价税合计 | numeric | 23 | 2 | √ | 0.00 | 价税合计 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | finputstatus | finputstatus | varchar | 30 |  | √ | ' ' |  |
| 7 | fbuyeraccount | fbuyeraccount | varchar | 100 |  | √ | ' ' |  |
| 8 | fbuyeraddressphone | fbuyeraddressphone | varchar | 300 |  | √ | ' ' |  |
| 9 | fauthenticateflag | 认证标志 | varchar | 30 |  | √ | ' ' | 认证标志,枚举: 0 :未勾选 1 :勾选 2 :勾选认证 3 :扫描认证 |
| 10 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 11 | fsaleraddressphone | fsaleraddressphone | varchar | 300 |  | √ | ' ' |  |
| 12 | fsaleraccount | fsaleraccount | varchar | 300 |  | √ | ' ' |  |
| 13 | fmachineno | fmachineno | varchar | 100 |  | √ | ' ' |  |
| 14 | fselectauthenticatetime | 勾选认证时间 | timestamp | 0 |  |  | null | 勾选认证时间 |
| 15 | finvoicecode | 发票代码 | varchar | 100 |  | √ | ' ' | 发票代码 |
| 16 | fbuyername | fbuyername | varchar | 100 |  | √ | ' ' |  |
| 17 | finvoiceno | 发票号码 | varchar | 100 |  | √ | ' ' | 发票号码 |
| 18 | fbillno | fbillno | varchar | 60 |  | √ | ' ' |  |
| 19 | fsalertaxno | 销方税号 | varchar | 100 |  | √ | ' ' | 销方税号 |
| 20 | ftaxamount | 合计税额 | numeric | 23 | 2 | √ | 0.00 | 合计税额 |
| 21 | fbillstatus | fbillstatus | varchar | 30 |  | √ | ' ' |  |
| 22 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 23 | fusedjzjtse | 已登记即征即退税额 | numeric | 23 | 2 | √ | 0.00 | 已登记即征即退税额 |
| 24 | flastrolloutuser | 最后转出人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | flastrollouttime | 最后转出时间 | timestamp | 0 |  |  | null | 最后转出时间 |
| 26 | fjzjtamount | 即征即退税额 | numeric | 23 | 2 | √ | 0.00 | 即征即退税额 |
| 27 | fsalername | 销方名称 | varchar | 200 |  | √ | ' ' | 销方名称 |
| 28 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 29 | fcheckcode | fcheckcode | varchar | 100 |  | √ | ' ' |  |
| 30 | fpayee | fpayee | varchar | 100 |  | √ | ' ' |  |
| 31 | finvoicestatus | finvoicestatus | varchar | 30 |  | √ | ' ' |  |
| 32 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 33 | fscanauthenticatetime | fscanauthenticatetime | timestamp | 0 |  |  | null |  |
| 34 | fselecttime | fselecttime | timestamp | 0 |  |  | null |  |
| 35 | freviewer | freviewer | varchar | 100 |  | √ | ' ' |  |
| 36 | finvoicedata | finvoicedata | timestamp | 0 |  |  | null |  |
| 37 | fmaingoodsname | 主要商品名称 | varchar | 200 |  | √ | ' ' | 主要商品名称 |
| 38 | fbuyertaxno | fbuyertaxno | varchar | 100 |  | √ | ' ' |  |
| 39 | fremark | fremark | varchar | 480 |  | √ | ' ' |  |
| 40 | ftaxperiod | 所属税期 | varchar | 100 |  | √ | ' ' | 所属税期 |
| 41 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 42 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 43 | fregisterstatus | 登记状态 | varchar | 30 |  | √ | ' ' | 登记状态,枚举: 0 :全部登记 1 :部分登记 2 :未登记 |
| 44 | fremainamount | 可转出金额 | numeric | 23 | 2 | √ | 0.00 | 可转出金额 |
| 45 | fexportamount | 出口税额 | numeric | 23 | 2 | √ | 0.00 | 出口税额 |
| 46 | ftype | 发票类型 | varchar | 30 |  | √ | ' ' | 发票类型,枚举: 4 :增值税专用发票 15 :通行费发票 |
| 47 | frolloutamount | 已转出金额 | numeric | 23 | 2 | √ | 0.00 | 已转出金额 |
| 48 | finvoiceamount | 合计金额 | numeric | 23 | 2 | √ | 0.00 | 合计金额 |
| 49 | fproxymark | fproxymark | varchar | 30 |  | √ | ' ' |  |
| 50 | fusedckse | 已转出出口税额 | numeric | 23 | 2 | √ | 0.00 | 已转出出口税额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tdm_invoice_input |  | fbillno |
| 2 | t_tdm_invoice_input_pkey |  | fid |
| 3 | idx_t_tdm_invoice_input2 |  | fselectauthenticatetime,ftaxperiod,forgid |
