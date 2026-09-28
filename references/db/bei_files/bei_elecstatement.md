# 电子对账单查询-bei_elecstatement

## 文件路径信息-子表 t_bei_elecstatement_url

- **表名称：** 文件路径信息-子表
- **表名：** t_bei_elecstatement_url

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffileservicepath | 文件服务路径 | varchar | 255 |  | √ | ' ' | 文件服务路径 |
| 3 | ffilesuffix | 文件格式 | varchar | 50 |  | √ | ' ' | 文件格式 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_elecstatement_url |  | fid |
| 2 | pk_bei_elecstatement_url |  | fentryid |

---

## 单据体-子表 t_bei_elecstatement_entry

- **表名称：** 单据体-子表
- **表名：** t_bei_elecstatement_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftransdetailno | 交易明细编号 | varchar | 50 |  | √ | ' ' | 交易明细编号 |
| 3 | ftransactioncode | 交易代码 | varchar | 50 |  | √ | ' ' | 交易代码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizproduct | 业务产品种类 | varchar | 50 |  | √ | ' ' | 业务产品种类 |
| 6 | fotherbookinfo | 其他记账信息 | varchar | 50 |  | √ | ' ' | 其他记账信息 |
| 7 | fbookjournal | 记账流水 | varchar | 50 |  | √ | ' ' | 记账流水 |
| 8 | fbooktime | 记账时间 | timestamp | 0 |  |  | null | 记账时间 |
| 9 | foppositebank | 对方开户行 | varchar | 50 |  | √ | ' ' | 对方开户行 |
| 10 | facctamount | 账户余额 | numeric | 19 | 6 |  | null | 账户余额 |
| 11 | fbookkeeper | 记账柜员 | varchar | 50 |  | √ | ' ' | 记账柜员 |
| 12 | fremark | 摘要 | varchar | 50 |  | √ | ' ' | 摘要 |
| 13 | fismatchdetail | 匹配交易明细 | bpchar | 1 |  | √ | '0' | 匹配交易明细 |
| 14 | fcreditamount | 贷方金额 | numeric | 19 | 6 |  | null | 贷方金额 |
| 15 | fcreditmark | 借贷标志 | varchar | 30 |  | √ | ' ' | 借贷标志,枚举: 0 :借方 1 :贷方 |
| 16 | fdebitamount | 借方金额 | numeric | 19 | 6 |  | null | 借方金额 |
| 17 | foppositeacctname | 对方户名 | varchar | 50 |  | √ | ' ' | 对方户名 |
| 18 | fbusinessserialnumber | 业务流水号 | varchar | 50 |  | √ | ' ' | 业务流水号 |
| 19 | fsourcedocument | 原始凭证种类 | varchar | 50 |  | √ | ' ' | 原始凭证种类 |
| 20 | fsourcedocumentno | 原始凭证号码 | varchar | 50 |  | √ | ' ' | 原始凭证号码 |
| 21 | fbalancedirection | 余额方向 | varchar | 30 |  | √ | ' ' | 余额方向,枚举: 0 :借方 1 :贷方 |
| 22 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 23 | foppositeacct | 对方账号 | varchar | 50 |  | √ | ' ' | 对方账号 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fcurrencyid | 分录币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 26 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 27 | felecreceiptno | 电子回单号 | varchar | 50 |  | √ | ' ' | 电子回单号 |
| 28 | fischeck | 已勾对标志 | bpchar | 1 |  | √ | '0' | 已勾对标志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_elecstatement_entry |  | fentryid |
| 2 | idx_bei_elecstatement_entry |  | fid |

---

## 电子对账单查询-主表 t_bei_elecstatement

- **表名称：** 电子对账单查询-主表
- **表名：** t_bei_elecstatement

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjoindate | 接入日期 | timestamp | 0 |  |  | null | 接入日期 |
| 3 | fendoverdraftamount | 期末透支余额 | numeric | 19 | 6 |  | null | 期末透支余额 |
| 4 | ffileservicepath | 文件服务路径（废弃） | varchar | 255 |  | √ | ' ' | 文件服务路径（废弃） |
| 5 | faccountbankname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 6 | fendfreezeamount | 期末冻结余额 | numeric | 19 | 6 |  | null | 期末冻结余额 |
| 7 | fbankcustomercode | 银行客户编码 | varchar | 80 |  | √ | ' ' | 银行客户编码 |
| 8 | fendacctamount | 期末账户余额 | numeric | 19 | 6 |  | null | 期末账户余额 |
| 9 | fiscompleted | 是否完成 | bpchar | 1 |  | √ | '0' | 是否完成 |
| 10 | famount | 金额 | numeric | 19 | 6 |  | null | 金额 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbankbranchnumber | 营业网点编号 | varchar | 80 |  | √ | ' ' | 营业网点编号 |
| 13 | fexchangerate | 汇率 | numeric | 19 | 6 | √ | 0 | 汇率 |
| 14 | fisextracted | 是否已抽取 | bpchar | 1 |  | √ | '0' | 是否已抽取 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | ffilesuffix | 文件格式（废弃） | varchar | 50 |  | √ | ' ' | 文件格式（废弃） |
| 17 | fendavailableamount | 期末可用余额 | numeric | 19 | 6 |  | null | 期末可用余额 |
| 18 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 19 | fidentificationissuer | 签发机构 | varchar | 80 |  | √ | ' ' | 签发机构 |
| 20 | faccountcompanyid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fjointime | 接入时间 | timestamp | 0 |  |  | null | 接入时间 |
| 22 | fprintdate | 打印日期 | timestamp | 0 |  |  | null | 打印日期 |
| 23 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 24 | fisfile | 是否文件 | bpchar | 1 |  | √ | '0' | 是否文件 |
| 25 | fbankstatus | 银行接收状态 | varchar | 50 |  | √ | ' ' | 银行接收状态,枚举: OP :未提交 OS :银企处理中 OJ :银企接收 TS :对账成功 TF :对账失败 OT :其他途径反馈 |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 30 | fendretainamount | 期末保留余额 | numeric | 19 | 6 |  | null | 期末保留余额 |
| 31 | fprintcount | 打印次数 | int8 | 64 |  | √ | 0 | 打印次数 |
| 32 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 33 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 34 | fperiod | 所属期间 | timestamp | 0 |  |  | null | 所属期间 |
| 35 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: frombank :银企接口 fileimport :识别引入 import :模版引入 |
| 36 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 37 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 38 | faccountbankid | 银行账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 39 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fbilltype | 单据类型 | varchar | 50 |  | √ | ' ' | 单据类型,枚举: bei_elecstatement :电子对账单 bei_elecbalancestate :电子余额对账（按协议） bei_elecbalancestate_acc :电子余额对账（按账号） |
| 41 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 42 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0 | 金额折本位币 |
| 43 | farchivecontent | 归档内容 | varchar | 30 |  | √ | ' ' | 归档内容,枚举: file :版式文件 instance :实例文档 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bei_elecstatement |  | fid |
| 2 | idx_bei_elecstatement |  | fcurrencyid,faccountbankid,fperiod |

---

## 电子对账单查询-多语言表 t_bei_elecstatement_l

- **表名称：** 电子对账单查询-多语言表
- **表名：** t_bei_elecstatement_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 100 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_elecstatement_l |  | fid,flocaleid |
| 2 | pk_t_bei_elecstatement_l |  | fpkid |
