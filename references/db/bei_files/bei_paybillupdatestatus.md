# 付款状态变更单-bei_paybillupdatestatus

## 付款状态变更单-反写记录表 t_bei_updatepaystat_wb

- **表名称：** 付款状态变更单-反写记录表
- **表名：** t_bei_updatepaystat_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 19 | 6 | √ | 0.000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_updatepaystat_wb |  | fid |
| 2 | t_bei_updatepaystat_wb_pkey |  | fentryid |

---

## 付款状态变更单-多语言表 t_bei_updatepaystat_l

- **表名称：** 付款状态变更单-多语言表
- **表名：** t_bei_updatepaystat_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_updatepaystat_l_pkey |  | fpkid |
| 2 | idx_t_bei_updatepaystat_l |  | fid,flocaleid |

---

## 关联子实体-子表 t_bei_updatepaystat_entry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_bei_updatepaystat_entry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_updatepaystat_entry_lk_pkey |  | fpkid |
| 2 | idx_bei_updatepaystat_et_lk |  | fentryid |

---

## 分录-子表 t_bei_updatepaystat_entry

- **表名称：** 分录-子表
- **表名：** t_bei_updatepaystat_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourceentryid | 源单ID | varchar | 30 |  | √ | ' ' | 源单ID |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | freason | 原因 | varchar | 255 |  | √ | ' ' | 原因 |
| 5 | fencpayacct | 收款账号 | varchar | 30 |  |  | null | 收款账号 |
| 6 | fpayamt | 付款金额 | numeric | 19 | 6 | √ | 0.000000 | 付款金额 |
| 7 | fencpayamt | 付款金额 | varchar | 30 |  |  | null | 付款金额 |
| 8 | fpayacctorgid | 收款账号收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fpaystatus | 付款状态 | varchar | 30 |  | √ | ' ' | 付款状态,枚举: OP :准备提交 TS :交易成功 TF :交易失败 NC :交易未确认 OS :银企处理中 BP :银行处理中 |
| 10 | ferrmsg | 操作失败原因 | varchar | 255 |  | √ | ' ' | 操作失败原因 |
| 11 | frecuser | 收款人 | varchar | 255 |  | √ | ' ' | 收款人 |
| 12 | fstatusnew | 修改后付款状态 | varchar | 30 |  | √ | ' ' | 修改后付款状态,枚举: TS :交易成功 TF :交易失败 |
| 13 | fopstatus | 操作状态 | varchar | 30 |  | √ | ' ' | 操作状态,枚举: success :成功 failed :失败 |
| 14 | fsourceseq | 源分录行号 | varchar | 30 |  | √ | ' ' | 源分录行号 |
| 15 | fpayacct | 收款账号 | varchar | 80 |  | √ | ' ' | 收款账号 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fbankreturnmsg | 银行返回信息 | varchar | 255 |  | √ | ' ' | 银行返回信息 |
| 18 | frecbank | 收款银行 | varchar | 255 |  | √ | ' ' | 收款银行 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_updatepaystat_entry |  | fid |
| 2 | t_bei_updatepaystat_entry_pkey |  | fentryid |

---

## 关联子实体-子表 t_bei_updatepaystat_lk

- **表名称：** 关联子实体-子表
- **表名：** t_bei_updatepaystat_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_updatepaystat_lk_pkey |  | fpkid |
| 2 | idx_t_bei_updatepaystat_lk |  | fid |

---

## 付款状态变更单-关联追踪表 t_bei_updatepaystat_tc

- **表名称：** 付款状态变更单-关联追踪表
- **表名：** t_bei_updatepaystat_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
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
| 1 | idx_bei_updatepaystat_tc_tid |  | ftid |
| 2 | idx_bei_updatepaystat_tc_tbill |  | ftbillid |
| 3 | idx_t_bei_updatepaystat_tc |  | ftbillid |
| 4 | t_bei_updatepaystat_tc_pkey |  | fid |

---

## 付款状态变更单-主表 t_bei_updatepaystat

- **表名称：** 付款状态变更单-主表
- **表名：** t_bei_updatepaystat

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fskipproc | 是否跳过流程 | bpchar | 1 |  | √ | '0' | 是否跳过流程 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 9 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fsourcetype | 单据类型 | varchar | 30 |  | √ | ' ' | 单据类型,枚举: bei_bankpaybill :银行付款单 bei_bankagentpay :银行代发单 bei_banktransupbill :银行上划单 bei_banktransdownbill :银行下拨单 |
| 14 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 15 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 16 | fisencryption | 是否加密 | bpchar | 1 |  | √ | '0' | 是否加密 |
| 17 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 18 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fsourcebillno | 源单编号 | varchar | 100 |  | √ | ' ' | 源单编号 |
| 20 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 23 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 金额折本位币 |
| 24 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_updatepaystat |  | fbillno |
| 2 | t_bei_updatepaystat_pkey |  | fid |
