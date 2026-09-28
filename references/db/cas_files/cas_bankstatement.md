# 银行对账单-cas_bankstatement

## 单据体-子表 t_cas_bankstatemententry

- **表名称：** 单据体-子表
- **表名：** t_cas_bankstatemententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_bankstatemententry_pkey |  | fentryid |
| 2 | idx_cas_bse_fpid |  | fid |

---

## 银行对账单-主表 t_cas_bankstatement

- **表名称：** 银行对账单-主表
- **表名：** t_cas_bankstatement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbankvoucherno | 明细流水号 | varchar | 255 |  | √ | ' ' | 明细流水号 |
| 3 | foppaccountnumber | 对方账号 | varchar | 255 |  | √ | ' ' | 对方账号 |
| 4 | fbankcheckflag | 对账标识码 | varchar | 1024 |  | √ | ' ' | 对账标识码 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | foppunit | 对方账号名称 | varchar | 255 |  | √ | ' ' | 对方账号名称 |
| 7 | foppbank | 对方开户行 | varchar | 255 |  | √ | ' ' | 对方开户行 |
| 8 | ftranstime | 交易时间 | timestamp | 0 |  |  | null | 交易时间 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: 1 :银行交易下载 2 :内部金融机构下载 3 :手工引入 4 :手工新增 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fcashier | 柜员 | varchar | 50 |  | √ | ' ' | 柜员 |
| 13 | fuse | 用途 | varchar | 255 |  | √ | ' ' | 用途 |
| 14 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 1 :普通 2 :上划 3 :下拨 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 17 | fsettlementnumber | 结算号 | varchar | 2000 |  | √ | ' ' | 结算号 |
| 18 | fimageno | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 19 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 20 | fpostscript | 附言 | varchar | 255 |  | √ | ' ' | 附言 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbalanceamtfrombank | 余额（源于银行） | numeric | 23 | 10 | √ | 0 | 余额（源于银行） |
| 24 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 25 | fsequencenumber | 排序号 | varchar | 50 |  | √ | ' ' | 排序号 |
| 26 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fbatchno | 源文件编码 | varchar | 50 |  | √ | ' ' | 源文件编码 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fratesdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 30 | fisbank | 是否对账 | bpchar | 1 |  | √ | '1' | 是否对账 |
| 31 | ftradenumber | 业务参考号 | varchar | 50 |  | √ | ' ' | 业务参考号 |
| 32 | fvouchernumber | 银行凭证号 | varchar | 1024 |  | √ | ' ' | 银行凭证号 |
| 33 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 34 | fcreditamount | 贷方金额（收入） | numeric | 19 | 6 | √ | 0.000000 | 贷方金额（收入） |
| 35 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 36 | fdebitamount | 借方金额（支出） | numeric | 19 | 6 | √ | 0.000000 | 借方金额（支出） |
| 37 | forderno | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 38 | fbalanceamt | 余额 | numeric | 19 | 6 | √ | 0.000000 | 余额 |
| 39 | fbizdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 40 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 41 | fdirection | 方向 | varchar | 30 |  | √ | ' ' | 方向,枚举: 1 :借 2 :贷 |
| 42 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 43 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fverifystatus | fverifystatus | varchar | 30 |  | √ | ' ' |  |
| 46 | fischeck | 是否勾对 | bpchar | 1 |  | √ | '0' | 是否勾对 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_bs_clu |  | fbizdate,fbankcheckflag,fsettlementnumber,fdebitamount,fcreditamount |
| 2 | idx_cas_bs_sourceid |  | fsourcebillid |
| 3 | t_cas_bankstatement_pkey |  | fid |
| 4 | idx_cas_bs_oacb |  | forgid,faccountbankid,fcurrencyid,fbizdate |
| 5 | idx_cas_bs_accountbankiddate |  | faccountbankid,fbizdate |
