# 付款交易明细-cas_paytransdetail

## 付款交易明细-反写记录表 t_be_transdetail_wb

- **表名称：** 付款交易明细-反写记录表
- **表名：** t_be_transdetail_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_be_transdetail_wb_pkey |  | fentryid |

---

## 付款交易明细-主表 t_be_transdetail

- **表名称：** 付款交易明细-主表
- **表名：** t_be_transdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fiscreatedtransdown | fiscreatedtransdown | bpchar | 1 |  | √ | ' ' |  |
| 3 | fbankcheckflag | 对账标识码 | varchar | 255 |  |  | null | 对账标识码 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | foppunit | 对方单位 | varchar | 255 |  | √ | ' ' | 对方单位 |
| 6 | ftranpackageid | ftranpackageid | varchar | 100 |  | √ | ' ' |  |
| 7 | fagentaccname | fagentaccname | varchar | 100 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fiskdretflag | 是否银企付款 | bpchar | 1 |  | √ | ' ' | 是否银企付款 |
| 10 | fisbankwithholding | 银行代扣 | bpchar | 1 |  | √ | ' ' | 银行代扣 |
| 11 | fbankinterface | fbankinterface | varchar | 100 |  | √ | ' ' |  |
| 12 | flineno | flineno | int8 | 64 |  | √ | 0 |  |
| 13 | foppbanknumber | 对方银行账户 | varchar | 255 |  | √ | ' ' | 对方银行账户 |
| 14 | fdetailid | detailId | int8 | 64 |  | √ | 0 | detailId |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fname | 票据号 | varchar | 80 |  | √ | ' ' | 票据号 |
| 17 | frecdate | frecdate | timestamp | 0 |  |  | null |  |
| 18 | freceiptno | 电子回单关联标记 | varchar | 100 |  | √ | ' ' | 电子回单关联标记 |
| 19 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 20 | fbankinterfacetype | 银行接口类型 | varchar | 30 |  | √ | ' ' | 银行接口类型,枚举: |
| 21 | fisfakedetail | fisfakedetail | bpchar | 1 |  | √ | ' ' |  |
| 22 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 23 | fcreditamount | 收款金额 | numeric | 19 | 6 | √ | 0.000000 | 收款金额 |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fdebitamount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 26 | ftransbalance | 余额 | numeric | 19 | 6 | √ | 0.000000 | 余额 |
| 27 | fbankinterfaceid | fbankinterfaceid | int8 | 64 |  | √ | 0 |  |
| 28 | fisdowntobankstate | 是否已经下载到银行对账单 | bpchar | 1 |  | √ | ' ' | 是否已经下载到银行对账单 |
| 29 | fagentaccno | fagentaccno | varchar | 80 |  | √ | ' ' |  |
| 30 | fagentaccbkname | fagentaccbkname | varchar | 100 |  | √ | ' ' |  |
| 31 | fsrcbilltype | fsrcbilltype | int8 | 64 |  | √ | 0 |  |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 33 | frecedbilltype | 接收单据类型 | varchar | 30 |  | √ | ' ' | 接收单据类型,枚举: 6E41E17C :结算单 cas_paybill :付款单 recbill :收款单 5E920865 :下拨单 D125C4DE :上划单 other :其它单据 |
| 34 | fbanklog | fbanklog | int8 | 64 |  | √ | 0 |  |
| 35 | fisreced | 是否被接收 | bpchar | 1 |  | √ | ' ' | 是否被接收 |
| 36 | foppbank | 对方银行 | varchar | 255 |  | √ | ' ' | 对方银行 |
| 37 | fisdebit | 是否付款 | bpchar | 1 |  | √ | ' ' | 是否付款 |
| 38 | fhasrefundpay | fhasrefundpay | bpchar | 1 |  | √ | ' ' |  |
| 39 | fbankaccount | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 40 | frecedbillnumber | 接收单据编号 | varchar | 80 |  | √ | ' ' | 接收单据编号 |
| 41 | fisdataimport | 是否导入 | bpchar | 1 |  | √ | ' ' | 是否导入 |
| 42 | fbizrefno | 银行流水号 | varchar | 255 |  |  | null | 银行流水号 |
| 43 | fbiztime | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 44 | freceredtype | 入账状态 | varchar | 5 |  | √ | ' ' | 入账状态,枚举: 1 :确认入账 2 :无需入账 3 :已入账 0 :待入账 |
| 45 | fbankrst | fbankrst | varchar | 255 |  |  | null |  |
| 46 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 1 :普通 2 :上划 3 :下拨 |
| 47 | fistransup | 银行上划 | bpchar | 1 |  | √ | ' ' | 银行上划 |
| 48 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 49 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 50 | frawtranstime | frawtranstime | timestamp | 0 |  |  | null |  |
| 51 | fisnoreceipt | 是否确认无回单 | bpchar | 1 |  | √ | ' ' | 是否确认无回单 |
| 52 | foppcompanyid | foppcompanyid | int8 | 64 |  | √ | 0 |  |
| 53 | fisrefund | 是否退票 | bpchar | 1 |  | √ | ' ' | 是否退票 |
| 54 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 55 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 56 | foriginalbankcheckflag | 对账标识码（银行返回） | varchar | 255 |  |  | null | 对账标识码（银行返回） |
| 57 | fcurrency | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 58 | fistransdown | 银行下拨 | bpchar | 1 |  | √ | ' ' | 银行下拨 |
| 59 | fismatchereceipt | 是否跟电子回单匹配 | bpchar | 1 |  | √ | ' ' | 是否跟电子回单匹配 |
| 60 | fstate | fstate | int8 | 64 |  | √ | 0 |  |
| 61 | fiscreatedtransup | fiscreatedtransup | bpchar | 1 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_be_transdetail_pkey |  | fid |
| 2 | idx_be_td_forgid |  | forgid,fbankaccount,fbiztype |

---

## 关联子实体-子表 t_be_transdetail_lk

- **表名称：** 关联子实体-子表
- **表名：** t_be_transdetail_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_be_transdetail_lk_pkey |  | fpkid |

---

## 付款交易明细-关联追踪表 t_be_transdetail_tc

- **表名称：** 付款交易明细-关联追踪表
- **表名：** t_be_transdetail_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_be_transdetail_tc_tid |  | ftid |
| 2 | idx_be_transdetail_tc_tbill |  | ftbillid |
| 3 | t_be_transdetail_tc_pkey |  | fid |
