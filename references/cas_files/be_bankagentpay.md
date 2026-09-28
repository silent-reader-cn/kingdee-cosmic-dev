# 银行代发单（历史单据）-be_bankagentpay

## 银行代发单（历史单据）-主表 t_be_bankagentpaybill

- **表名称：** 银行代发单（历史单据）-主表
- **表名：** t_be_bankagentpaybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbankcheckflag | 对账标识码 | varchar | 80 |  | √ | ' ' | 对账标识码 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | famount | 总金额 | numeric | 19 | 6 | √ | 0.000000 | 总金额 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fexchangerate | 汇率 | numeric | 19 | 6 | √ | 0.000000 | 汇率 |
| 7 | fcreatorid | 制单人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fexpectdealtime | 期望交易时间 | timestamp | 0 |  |  | null | 期望交易时间 |
| 9 | factamount | 确认金额 | numeric | 19 | 6 | √ | 0.000000 | 确认金额 |
| 10 | factcount | 确认笔数 | int8 | 64 |  | √ | 0 | 确认笔数 |
| 11 | fcount | 总笔数 | int8 | 64 |  | √ | 0 | 总笔数 |
| 12 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 13 | fpayeracctbankid | 付款账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | flocalamount | 折本位币金额 | numeric | 19 | 6 | √ | 0.000000 | 折本位币金额 |
| 16 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 TF :交易失败 NC :交易未确认 OP :准备提交 OF :银企异常 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fagentpaybillno | 代发单号 | varchar | 80 |  | √ | ' ' | 代发单号 |
| 19 | fsubmittime | 提交银企时间 | timestamp | 0 |  |  | null | 提交银企时间 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | fserialnumber | 序列号 | varchar | 80 |  | √ | ' ' | 序列号 |
| 22 | fbasecurrencyid | 组织本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 23 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 24 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 25 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 26 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fisbitback | 打回标识 | bpchar | 1 |  | √ | ' ' | 打回标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_be_bankagentpaybill_pkey |  | fid |
| 2 | idx_be_bap_fbillno |  | fbillno |

---

## 关联子实体-子表 t_be_bankagentpay_lk

- **表名称：** 关联子实体-子表
- **表名：** t_be_bankagentpay_lk

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
| 1 | t_be_bankagentpay_lk_pkey |  | fpkid |

---

## 银行代发单（历史单据）-关联追踪表 t_be_bankagentpay_tc

- **表名称：** 银行代发单（历史单据）-关联追踪表
- **表名：** t_be_bankagentpay_tc

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
| 1 | t_be_bankagentpay_tc_pkey |  | fid |
| 2 | idx_be_bankagentpay_tc_tbill |  | ftbillid |
| 3 | idx_be_bankagentpay_tc_tid |  | ftid |

---

## 分录-子表 t_be_bankagentpayentry

- **表名称：** 分录-子表
- **表名：** t_be_bankagentpayentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 转账附言 | varchar | 200 |  |  | null | 转账附言 |
| 3 | fisagencypersonpay | 是否并笔入账 | bpchar | 1 |  | √ | ' ' | 是否并笔入账 |
| 4 | fbankcheckflag | 对账标识码 | varchar | 80 |  | √ | ' ' | 对账标识码 |
| 5 | fsourceentryid | 源分录ID | int8 | 64 |  | √ | 0 | 源分录ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | frecname | 姓名 | varchar | 50 |  | √ | ' ' | 姓名 |
| 8 | famount | 加密金额 | varchar | 100 |  | √ | ' ' | 加密金额 |
| 9 | facctbanknum | 收款账号 | varchar | 50 |  | √ | ' ' | 收款账号 |
| 10 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: OP :准备提交 TS :交易成功 TF :交易失败 NC :交易未确认 OS :银企处理中 BP :银行处理中 |
| 11 | fcity | 收款市 | varchar | 50 |  | √ | ' ' | 收款市 |
| 12 | fisrefund | 是否退票 | bpchar | 1 |  | √ | ' ' | 是否退票 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | frecbank | 收款银行 | varchar | 50 |  | √ | ' ' | 收款银行 |
| 15 | fprovince | 收款省 | varchar | 50 |  | √ | ' ' | 收款省 |
| 16 | fbankreturnmsg | 银行返回信息 | varchar | 200 |  |  | null | 银行返回信息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_be_bape_fpid |  | fid,fbankcheckflag |
| 2 | t_be_bankagentpayentry_pkey |  | fentryid |

---

## 银行代发单（历史单据）-反写记录表 t_be_bankagentpay_wb

- **表名称：** 银行代发单（历史单据）-反写记录表
- **表名：** t_be_bankagentpay_wb

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
| 1 | t_be_bankagentpay_wb_pkey |  | fentryid |
