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
| 3 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 4 | fbalanceamtfromsys | 余额（系统计算） | numeric | 23 | 10 | √ | 0 | 余额（系统计算） |
| 5 | foppaccountnumber | 对方账号 | varchar | 255 |  | √ | ' ' | 对方账号 |
| 6 | fbankcheckflag | 对账标识码 | varchar | 1024 |  | √ | ' ' | 对账标识码 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | foppunit | 对方账号名称 | varchar | 255 |  | √ | ' ' | 对方账号名称 |
| 9 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsettlementnumber | 结算号 | varchar | 2000 |  | √ | ' ' | 结算号 |
| 12 | fimageno | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 13 | fpostscript | 附言 | varchar | 255 |  | √ | ' ' | 附言 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fbalanceamtfrombank | 余额（源于银行） | numeric | 23 | 10 | √ | 0 | 余额（源于银行） |
| 16 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 17 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fbatchno | 源文件编码 | varchar | 50 |  | √ | ' ' | 源文件编码 |
| 19 | fratesdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 20 | fisbank | 是否对账 | bpchar | 1 |  | √ | '1' | 是否对账 |
| 21 | ftradenumber | 业务参考号 | varchar | 50 |  | √ | ' ' | 业务参考号 |
| 22 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 23 | fcreditamount | 贷方金额（收入） | numeric | 19 | 6 | √ | 0.000000 | 贷方金额（收入） |
| 24 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 25 | fdebitamount | 借方金额（支出） | numeric | 19 | 6 | √ | 0.000000 | 借方金额（支出） |
| 26 | forderno | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 27 | fdirection | 方向 | varchar | 30 |  | √ | ' ' | 方向,枚举: 1 :借 2 :贷 |
| 28 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | foppbank | 对方开户行 | varchar | 255 |  | √ | ' ' | 对方开户行 |
| 31 | ftranstime | 交易时间 | timestamp | 0 |  |  | null | 交易时间 |
| 32 | fsource | 来源 | varchar | 30 |  | √ | ' ' | 来源,枚举: 1 :银行交易下载 2 :内部金融机构下载 3 :手工引入 4 :手工新增 |
| 33 | fcashier | 柜员 | varchar | 50 |  | √ | ' ' | 柜员 |
| 34 | fuse | 用途 | varchar | 255 |  | √ | ' ' | 用途 |
| 35 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 1 :普通 2 :上划 3 :下拨 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 37 | fcheckresult | 检查结果 | varchar | 10 |  | √ | ' ' | 检查结果,枚举: 1 :通过 2 :不通过 3 :未知 |
| 38 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 39 | fdiffamt | 差额 | numeric | 23 | 10 | √ | 0 | 差额 |
| 40 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fsequencenumber | 排序号 | varchar | 50 |  | √ | ' ' | 排序号 |
| 43 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 44 | fvouchernumber | 银行凭证号 | varchar | 1024 |  | √ | ' ' | 银行凭证号 |
| 45 | fbalanceamt | 余额 | numeric | 19 | 6 | √ | 0.000000 | 余额 |
| 46 | fbizdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 47 | fsourcebillid | 源单ID | int8 | 64 |  | √ | 0 | 源单ID |
| 48 | fcheckerrormsg | 检查结果说明 | varchar | 255 |  | √ | ' ' | 检查结果说明 |
| 49 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 50 | fverifystatus | fverifystatus | varchar | 30 |  | √ | ' ' |  |
| 51 | fischeck | 是否勾对 | bpchar | 1 |  | √ | '0' | 是否勾对 |

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
