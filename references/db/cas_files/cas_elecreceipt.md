# 电子回单-cas_elecreceipt

## 电子回单-主表 t_cas_elecreceipt

- **表名称：** 电子回单-主表
- **表名：** t_cas_elecreceipt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftcpurl | tcpurl | varchar | 255 |  |  | null | tcpurl |
| 3 | fcreditdebitflag | 借贷标记 | varchar | 30 |  | √ | ' ' | 借贷标记,枚举: 1 :出账 2 :入账 |
| 4 | fbankcheckflag | 对账标识码 | varchar | 30 |  | √ | ' ' | 对账标识码 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | foppunit | 对方单位 | varchar | 255 |  | √ | ' ' | 对方单位 |
| 7 | ffileserverurl | 文件服务url | varchar | 255 |  |  | null | 文件服务url |
| 8 | ftransnetcode | 记账网点 | varchar | 100 |  | √ | ' ' | 记账网点 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fpayeracntname | 付款方账户名 | varchar | 100 |  | √ | ' ' | 付款方账户名 |
| 11 | fpayeeacntno | 收款方账号 | varchar | 30 |  | √ | ' ' | 收款方账号 |
| 12 | fpayeracntno | 付款方账号 | varchar | 30 |  | √ | ' ' | 付款方账号 |
| 13 | fbiznumber | 业务参考号 | varchar | 30 |  | √ | ' ' | 业务参考号 |
| 14 | fuploadfilename | 上传文件名称 | varchar | 255 |  |  | null | 上传文件名称 |
| 15 | fbustype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: NORMAL :NORMAL |
| 16 | foppbanknumber | 对方银行账号 | varchar | 255 |  | √ | ' ' | 对方银行账号 |
| 17 | freprintnum | 补打次数 | int8 | 64 |  | √ | 0 | 补打次数 |
| 18 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 19 | freceiptno | 电子回单号(用于和交易明细关联) | varchar | 30 |  | √ | ' ' | 电子回单号(用于和交易明细关联) |
| 20 | fismatch | 匹配交易明细 | bpchar | 1 |  | √ | '0' | 匹配交易明细 |
| 21 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fcurrentdate | 当前日期 | timestamp | 0 |  |  | null | 当前日期 |
| 23 | fserialno | 交易流水号 | varchar | 100 |  | √ | ' ' | 交易流水号 |
| 24 | fpayeebankname | 收款银行 | varchar | 100 |  | √ | ' ' | 收款银行 |
| 25 | fcreditamount | 贷方金额 | numeric | 19 | 6 | √ | 0.000000 | 贷方金额 |
| 26 | fdescription | 摘要 | varchar | 255 |  |  | null | 摘要 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fdebitamount | 借方金额 | numeric | 19 | 6 | √ | 0.000000 | 借方金额 |
| 29 | fpayeeacntname | 收款方账户名 | varchar | 100 |  | √ | ' ' | 收款方账户名 |
| 30 | ftransdate | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 31 | ffileflag | 是否文件 | bpchar | 1 |  | √ | '0' | 是否文件 |
| 32 | fbankid | 金融机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 33 | ftransdetailid | 银行交易明细id | int8 | 64 |  | √ | 0 | 银行交易明细id |
| 34 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 35 | fpayerbankname | 付款方开户银行 | varchar | 100 |  | √ | ' ' | 付款方开户银行 |
| 36 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | foppbank | 对方银行 | varchar | 255 |  | √ | ' ' | 对方银行 |
| 38 | fcompleteflag | 是否完成标识 | bpchar | 1 |  | √ | '0' | 是否完成标识 |
| 39 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 40 | fpassword | 服务器认证密码 | varchar | 30 |  | √ | ' ' | 服务器认证密码 |
| 41 | fuse | 用途 | varchar | 255 |  |  | null | 用途 |
| 42 | fusername | 服务器认证用户名 | varchar | 30 |  | √ | ' ' | 服务器认证用户名 |
| 43 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 45 | ftranstellno | 记账柜员号 | varchar | 30 |  | √ | ' ' | 记账柜员号 |
| 46 | fvalidcode | 验证码 | varchar | 30 |  | √ | ' ' | 验证码 |
| 47 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 49 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 50 | fprintcount | 打印次数 | int8 | 64 |  | √ | 0 | 打印次数 |
| 51 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 52 | fdetaildatetime | 明细交易时间 | timestamp | 0 |  |  | null | 明细交易时间 |
| 53 | ffilepath | 文件路径 | varchar | 100 |  | √ | ' ' | 文件路径 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_er_acct |  | faccountbankid,freceiptno |
| 2 | idx_cas_er_flag |  | fbankcheckflag |
| 3 | idx_cas_er_clu |  | freceiptno |
| 4 | idx_cas_er_date |  | ftransdate,faccountbankid,fcurrencyid |
| 5 | t_cas_elecreceipt_pkey |  | fid |

---

## 单据体-子表 t_cas_elecreceiptentry

- **表名称：** 单据体-子表
- **表名：** t_cas_elecreceiptentry

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
| 1 | idx_cas_ere_fid |  | fid |
| 2 | t_cas_elecreceiptentry_pkey |  | fentryid |
