# 银行付款单（历史单据）-be_bankpaying

## 银行付款单（历史单据）-关联追踪表 t_be_bankpayingbill_tc

- **表名称：** 银行付款单（历史单据）-关联追踪表
- **表名：** t_be_bankpayingbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_be_bp_tc_ftbillid |  | ftbillid |
| 2 | t_be_bankpayingbill_tc_pkey |  | fid |
| 3 | idx_be_bankpayingbill_tc_tbill |  | ftbillid |
| 4 | idx_be_bankpayingbill_tc_tid |  | ftid |

---

## 银行付款单（历史单据）-反写记录表 t_be_bankpayingbill_wb

- **表名称：** 银行付款单（历史单据）-反写记录表
- **表名：** t_be_bankpayingbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  |  | null |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  |  | null |  |
| 9 | fentryid | fentryid | int8 | 64 |  |  | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_be_bp_wb_fsbid_fsid |  | fsid,fsbillid |
| 2 | t_be_bankpayingbill_wb_pkey |  | fid |

---

## 关联子实体-子表 t_be_bankpayingbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_be_bankpayingbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  |  | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  |  | null | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_be_bankpayingbill_lk_pkey |  | fpkid |
| 2 | idx_be_bp_lk_fid |  | fid |

---

## 银行付款单（历史单据）-主表 t_be_bankpayingbill

- **表名称：** 银行付款单（历史单据）-主表
- **表名：** t_be_bankpayingbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbillno | 源单编号 | varchar | 80 |  | √ | ' ' | 源单编号 |
| 3 | fisagencypersonpay | 并笔入账 | bpchar | 1 |  | √ | ' ' | 并笔入账 |
| 4 | forgid | 付款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fpayamount | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 6 | fstatementrefno | 对账标识码 | varchar | 80 |  | √ | ' ' | 对账标识码 |
| 7 | fispersonpay | 对私付款 | bpchar | 1 |  | √ | ' ' | 对私付款 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fusage | 用途 | varchar | 255 |  |  | null | 用途 |
| 10 | fcreatorid | 制单人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fislinkpay | 联动支付 | bpchar | 1 |  | √ | ' ' | 联动支付 |
| 12 | fexpectdealtime | 期望交易时间 | timestamp | 0 |  |  | null | 期望交易时间 |
| 13 | freccountryid | 收款方国家 | int8 | 64 |  | √ | 0 | 国家和地区 bd_country |
| 14 | fisrefund | 是否退票 | bpchar | 1 |  | √ | ' ' | 是否退票 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | fpayeename | 收款人 | varchar | 80 |  | √ | ' ' | 收款人 |
| 17 | fbatchseqid | 提交银企批次流水 | varchar | 80 |  | √ | ' ' | 提交银企批次流水 |
| 18 | fpayeracctbankid | 付款账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fpayeebanknum | 收款账户 | varchar | 80 |  | √ | ' ' | 收款账户 |
| 21 | frecemail | frecemail | varchar | 80 |  | √ | ' ' |  |
| 22 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 TS :交易成功 TF :交易失败 NC :交易未确认 OF :银企异常 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fpayeebankname | 收款银行 | varchar | 80 |  | √ | ' ' | 收款银行 |
| 25 | fsubmittime | 提交银行时间 | timestamp | 0 |  |  | null | 提交银行时间 |
| 26 | fisemergency | fisemergency | bpchar | 1 |  | √ | ' ' |  |
| 27 | fhandlerid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 29 | freccity | 收款方市县 | varchar | 80 |  | √ | ' ' | 收款方市县 |
| 30 | fserialnumber | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 31 | frecprovince | 收款方省 | varchar | 80 |  | √ | ' ' | 收款方省 |
| 32 | frecbanknum | 收款行号 | varchar | 30 |  | √ | ' ' | 收款行号 |
| 33 | fsigntext | 签名 | varchar | 1000 |  |  | null | 签名 |
| 34 | fbitbacktime | 打回日期 | timestamp | 0 |  |  | null | 打回日期 |
| 35 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 36 | fpayapplyorgnm | 申请组织 | varchar | 100 |  | √ | ' ' | 申请组织 |
| 37 | fisaudit | 审核 | bpchar | 1 |  | √ | ' ' | 审核 |
| 38 | fsrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: cas_paybill :付款单 |
| 39 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 40 | fbankreturnmsg | 银行返回信息 | varchar | 255 |  |  | null | 银行返回信息 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fbitbackerid | 打回处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 43 | fisbitback | 打回 | bpchar | 1 |  | √ | ' ' | 打回 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_be_bankpayingbill_pkey |  | fid |
| 2 | idx_be_bp_fbillno |  | fbillno |
