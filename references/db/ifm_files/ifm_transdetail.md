# 内部交易明细查询-ifm_transdetail

## 内部交易明细查询-主表 t_bei_transdetail

- **表名称：** 内部交易明细查询-主表
- **表名：** t_bei_transdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbankcheckflag | 对账标识码 | varchar | 255 |  | √ | ' ' | 对账标识码 |
| 3 | foppunit | 对方户名 | varchar | 255 |  | √ | ' ' | 对方户名 |
| 4 | ftranpackageid | ftranpackageid | varchar | 100 |  | √ | ' ' |  |
| 5 | fnote | fnote | varchar | 255 |  | √ | ' ' |  |
| 6 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 7 | fsortno | 排序号 | int8 | 64 |  | √ | 0 | 排序号 |
| 8 | fiskdretflag | fiskdretflag | bpchar | 1 |  | √ | '0' |  |
| 9 | fisbankwithholding | fisbankwithholding | bpchar | 1 |  | √ | '0' |  |
| 10 | fbankinterface | fbankinterface | varchar | 80 |  | √ | ' ' |  |
| 11 | foppbanknumber | 对方账号 | varchar | 255 |  | √ | ' ' | 对方账号 |
| 12 | fdetailid | 交易流水号 | varchar | 100 |  | √ | ' ' | 交易流水号 |
| 13 | fpostscript | fpostscript | varchar | 255 |  | √ | ' ' |  |
| 14 | fbillno | 交易明细编号 | varchar | 100 |  | √ | ' ' | 交易明细编号 |
| 15 | freceiptno | 电子回单关联标记 | varchar | 100 |  | √ | ' ' | 电子回单关联标记 |
| 16 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fisfakedetail | fisfakedetail | bpchar | 1 |  | √ | '0' |  |
| 18 | fcreditamount | 收款金额 | numeric | 19 | 6 |  | null | 收款金额 |
| 19 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 20 | fdebitamount | 付款金额 | numeric | 19 | 6 |  | null | 付款金额 |
| 21 | ftransbalance | 余额 | numeric | 19 | 6 |  | null | 余额 |
| 22 | fisdownbankjournal | fisdownbankjournal | bpchar | 1 |  | √ | '0' |  |
| 23 | fisdowntobankstate | 是否已经下载到银行对账单 | bpchar | 1 |  | √ | '0' | 是否已经下载到银行对账单 |
| 24 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: frombank :银企接口 import :模板引入 modify :系统修复 fromifm :结算中心 |
| 25 | fsrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型,枚举: ifm_transhandlebill :付款结算单 ifm_rectransbill :收款交易处理 ifm_transrecvbill :收款结算单 fca_transupbill :资金上划单 fca_transdownbill :资金下拨单 ifm_currentintbill :内部利息结息单 ifm_inneraccountinit :内部账户期初 ifm_linkpaybill :联动支付单 |
| 26 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 27 | frulename | frulename | varchar | 100 |  | √ | ' ' |  |
| 28 | faccountbankid | 本方账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 29 | fcompanyid | 成员单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fbankdetailno | fbankdetailno | varchar | 128 |  | √ | ' ' |  |
| 31 | frecedbilltype | 接收单据类型 | varchar | 30 |  | √ | ' ' | 接收单据类型,枚举: 6E41E17C :结算单 cas_paybill :付款单 recbill :收款单 5E920865 :下拨单 D125C4DE :上划单 other :其它单据 |
| 32 | fisreced | fisreced | bpchar | 1 |  | √ | '0' |  |
| 33 | foppbank | 对方开户行 | varchar | 255 |  | √ | ' ' | 对方开户行 |
| 34 | fisdebit | fisdebit | bpchar | 1 |  | √ | '0' |  |
| 35 | frecedbillnumber | 接收单据编号 | varchar | 200 |  | √ | ' ' | 接收单据编号 |
| 36 | fbizrefno | 业务参考号 | varchar | 255 |  | √ | ' ' | 业务参考号 |
| 37 | fisdataimport | fisdataimport | bpchar | 1 |  | √ | '0' |  |
| 38 | fbiztime | 交易时间 | timestamp | 0 |  |  | null | 交易时间 |
| 39 | freceredtype | 入账状态 | varchar | 5 |  | √ | '0' | 入账状态,枚举: 3 :已入账 0 :待入账 |
| 40 | fuse | fuse | varchar | 255 |  | √ | ' ' |  |
| 41 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 1 :普通 2 :上划 3 :下拨 |
| 42 | fistransup | fistransup | bpchar | 1 |  | √ | '0' |  |
| 43 | frawtranstime | frawtranstime | timestamp | 0 |  |  | null |  |
| 44 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fisnoreceipt | fisnoreceipt | bpchar | 1 |  | √ | '0' |  |
| 46 | fisrefund | fisrefund | bpchar | 1 |  | √ | '0' |  |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 49 | funiqueseq | funiqueseq | varchar | 500 |  | √ | ' ' |  |
| 50 | foriginalbankcheckflag | 对账标识码（银行返回） | varchar | 255 |  | √ | ' ' | 对账标识码（银行返回） |
| 51 | ffinancialtypeid | ffinancialtypeid | int8 | 64 |  | √ | 0 |  |
| 52 | fistransdown | fistransdown | bpchar | 1 |  | √ | '0' |  |
| 53 | fismatchereceipt | 跟电子回单匹配 | bpchar | 1 |  | √ | '0' | 跟电子回单匹配 |
| 54 | fbizdate | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 55 | fupdatetime | fupdatetime | timestamp | 0 |  |  | null |  |
| 56 | fsourcebillid | 源单据id | int8 | 64 |  | √ | 0 | 源单据id |
| 57 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bei_transdetailid |  | fdetailid |
| 2 | idx_bei_company_date |  | fcompanyid,fbizdate |
| 3 | idx_bei_transdetail1 |  | fbillno |
| 4 | idx_bei_transdetail |  | faccountbankid,fbiztype |
| 5 | t_bei_transdetail_pkey |  | fid |
| 6 | idx_bei_transrecbillnumber |  | frecedbillnumber |
| 7 | idx_bei_transdetail2 |  | fbizdate |

---

## 内部交易明细查询-多语言表 t_bei_transdetail_l

- **表名称：** 内部交易明细查询-多语言表
- **表名：** t_bei_transdetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 3 | flocaleid | flocaleid | varchar | 100 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bei_transdetail_l_pkey |  | fpkid |
| 2 | idx_bei_transdetail_l |  | fid,flocaleid,fdescription |

---

## 内部交易明细查询-分表 t_bei_transdetail_e

- **表名称：** 内部交易明细查询-分表
- **表名：** t_bei_transdetail_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fiscreatedtransdown | fiscreatedtransdown | bpchar | 1 |  | √ | '0' |  |
| 3 | fsourcemigratedata | fsourcemigratedata | varchar | 80 |  | √ | ' ' |  |
| 4 | fagentaccname | fagentaccname | varchar | 255 |  | √ | ' ' |  |
| 5 | fhandlebill | fhandlebill | varchar | 64 |  | √ | ' ' |  |
| 6 | ftransfercharge | ftransfercharge | numeric | 19 | 6 | √ | 0.000000 |  |
| 7 | frecbilltype | frecbilltype | int8 | 64 |  | √ | 0 |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | frequestserialno | frequestserialno | varchar | 255 |  | √ | ' ' |  |
| 10 | fbasepayee | fbasepayee | int8 | 64 |  | √ | 0 |  |
| 11 | fbustype | fbustype | varchar | 255 |  | √ | ' ' |  |
| 12 | fsettlecenteraccname | 结算中心银行账户名称 | varchar | 100 |  | √ | ' ' | 结算中心银行账户名称 |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 14 | fbasepayer | fbasepayer | int8 | 64 |  | √ | 0 |  |
| 15 | freceiptno | freceiptno | varchar | 100 |  | √ | ' ' |  |
| 16 | fbatchno | fbatchno | varchar | 255 |  | √ | ' ' |  |
| 17 | fpayeebasetype | fpayeebasetype | varchar | 64 |  | √ | ' ' |  |
| 18 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 19 | fkdretflag | fkdretflag | varchar | 255 |  | √ | ' ' |  |
| 20 | fautorecorpay | 自动收付款 | bpchar | 1 |  | √ | '0' | 自动收付款 |
| 21 | ftransdate | ftransdate | timestamp | 0 |  |  | null |  |
| 22 | freservefield | freservefield | varchar | 512 |  | √ | ' ' |  |
| 23 | fresponseserailno | fresponseserailno | varchar | 255 |  | √ | ' ' |  |
| 24 | fecommercelasttime | fecommercelasttime | timestamp | 0 |  |  | null |  |
| 25 | fisdowntobankstate | fisdowntobankstate | bpchar | 1 |  | √ | '0' |  |
| 26 | fagentaccno | fagentaccno | varchar | 80 |  | √ | ' ' |  |
| 27 | fsmartmatch | fsmartmatch | varchar | 10 |  | √ | ' ' |  |
| 28 | fagentaccbkname | fagentaccbkname | varchar | 100 |  | √ | ' ' |  |
| 29 | fnumber | fnumber | varchar | 100 |  | √ | ' ' |  |
| 30 | fdesc | fdesc | varchar | 255 |  | √ | ' ' |  |
| 31 | freceredway | freceredway | varchar | 30 |  | √ | ' ' |  |
| 32 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 33 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 34 | fagentaccbankname | fagentaccbankname | varchar | 255 |  | √ | ' ' |  |
| 35 | fextdata | fextdata | varchar | 255 |  | √ | ' ' |  |
| 36 | fclaimnoticebillno | fclaimnoticebillno | varchar | 30 |  | √ | ' ' |  |
| 37 | fpayee | fpayee | varchar | 256 |  | √ | ' ' |  |
| 38 | flastmodifierid | flastmodifierid | int8 | 64 |  | √ | 0 |  |
| 39 | fpayerbasetype | fpayerbasetype | varchar | 64 |  | √ | ' ' |  |
| 40 | frecedbillentryid | frecedbillentryid | int8 | 64 |  | √ | 0 |  |
| 41 | ffeecode | ffeecode | varchar | 255 |  | √ | ' ' |  |
| 42 | fpayer | fpayer | varchar | 256 |  | √ | ' ' |  |
| 43 | fisdataimport | fisdataimport | bpchar | 1 |  | √ | '0' |  |
| 44 | fbankrst | fbankrst | varchar | 255 |  | √ | ' ' |  |
| 45 | fflowserialno | fflowserialno | varchar | 255 |  | √ | ' ' |  |
| 46 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 47 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 48 | fpaybilltype | fpaybilltype | int8 | 64 |  | √ | 0 |  |
| 49 | fsortid | fsortid | varchar | 255 |  | √ | ' ' |  |
| 50 | fecommercebiztype | fecommercebiztype | varchar | 512 |  | √ | ' ' |  |
| 51 | flastmodifytime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 52 | fisnoreceipt | fisnoreceipt | bpchar | 1 |  | √ | '0' |  |
| 53 | fecommercefaildreason | fecommercefaildreason | varchar | 2000 |  | √ | ' ' |  |
| 54 | fbillnobillno | fbillnobillno | varchar | 255 |  | √ | ' ' |  |
| 55 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 56 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 57 | fsettletype | fsettletype | int8 | 64 |  | √ | 0 |  |
| 58 | fishandlink | fishandlink | bpchar | 1 |  | √ | '0' |  |
| 59 | fdatasources | fdatasources | bpchar | 1 |  | √ | '0' |  |
| 60 | fscorgid | 结算中心组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 61 | fbusinessbillnum | fbusinessbillnum | varchar | 100 |  | √ | ' ' |  |
| 62 | fiscreatedtransup | fiscreatedtransup | bpchar | 1 |  | √ | '0' |  |
| 63 | fsettlecenteraccno | 结算中心银行账号 | varchar | 100 |  | √ | ' ' | 结算中心银行账号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_transdetail_e |  | fnumber |
| 2 | t_bei_transdetail_e_pkey |  | fid |
