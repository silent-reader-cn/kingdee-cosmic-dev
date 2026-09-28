# 银行收付处理-bei_transdetail_cas

## 银行收付处理-分表 t_bei_transdetail_e

- **表名称：** 银行收付处理-分表
- **表名：** t_bei_transdetail_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fiscreatedtransdown | fiscreatedtransdown | bpchar | 1 |  | √ | '0' |  |
| 3 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 4 | fagentaccname | 被代理户名 | varchar | 255 |  | √ | ' ' | 被代理户名 |
| 5 | fhandlebill | fhandlebill | varchar | 64 |  | √ | ' ' |  |
| 6 | ftransfercharge | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 7 | frecbilltype | frecbilltype | int8 | 64 |  | √ | 0 |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | frequestserialno | 银企请求流水号 | varchar | 255 |  | √ | ' ' | 银企请求流水号 |
| 10 | fbasepayee | fbasepayee | int8 | 64 |  | √ | 0 |  |
| 11 | fbustype | busType | varchar | 255 |  | √ | ' ' | busType |
| 12 | fsettlecenteraccname | fsettlecenteraccname | varchar | 100 |  | √ | ' ' |  |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 14 | fbasepayer | fbasepayer | int8 | 64 |  | √ | 0 |  |
| 15 | freceiptno | freceiptno | varchar | 100 |  | √ | ' ' |  |
| 16 | fbatchno | 银企付款提交的批次号 | varchar | 255 |  | √ | ' ' | 银企付款提交的批次号 |
| 17 | fpayeebasetype | fpayeebasetype | varchar | 64 |  | √ | ' ' |  |
| 18 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 19 | fkdretflag | KD标识 | varchar | 255 |  | √ | ' ' | KD标识 |
| 20 | fautorecorpay | 自动收付款 | bpchar | 1 |  | √ | '0' | 自动收付款 |
| 21 | ftransdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 22 | freservefield | 预留字段 | varchar | 512 |  | √ | ' ' | 预留字段 |
| 23 | fresponseserailno | 银行响应流水号 | varchar | 255 |  | √ | ' ' | 银行响应流水号 |
| 24 | fecommercelasttime | 电商流水入账最后执行时间 | timestamp | 0 |  |  | null | 电商流水入账最后执行时间 |
| 25 | fisdowntobankstate | fisdowntobankstate | bpchar | 1 |  | √ | '0' |  |
| 26 | fagentaccno | 被代理账号 | varchar | 80 |  | √ | ' ' | 被代理账号 |
| 27 | fsmartmatch | 智能匹配 | varchar | 10 |  | √ | ' ' | 智能匹配,枚举: 1 :已匹配 0 :未匹配 |
| 28 | fagentaccbkname | fagentaccbkname | varchar | 100 |  | √ | ' ' |  |
| 29 | fnumber | fnumber | varchar | 100 |  | √ | ' ' |  |
| 30 | fdesc | fdesc | varchar | 255 |  | √ | ' ' |  |
| 31 | freceredway | 入账方式 | varchar | 30 |  | √ | ' ' | 入账方式,枚举: rule :按规则入账 hand :手工入账 claim :认领入账 automatch :自动匹配 handmatch :手工匹配 confirm :确认已入账 handmerge :手工合并入账 beipay :对账标识码匹配 |
| 32 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 33 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 34 | fagentaccbankname | 被代理账号开户行 | varchar | 255 |  | √ | ' ' | 被代理账号开户行 |
| 35 | fextdata | extData | varchar | 255 |  | √ | ' ' | extData |
| 36 | fclaimnoticebillno | 收款认领通知 | varchar | 30 |  | √ | ' ' | 收款认领通知 |
| 37 | fpayee | fpayee | varchar | 256 |  | √ | ' ' |  |
| 38 | flastmodifierid | flastmodifierid | int8 | 64 |  | √ | 0 |  |
| 39 | fpayerbasetype | fpayerbasetype | varchar | 64 |  | √ | ' ' |  |
| 40 | frecedbillentryid | frecedbillentryid | int8 | 64 |  | √ | 0 |  |
| 41 | ffeecode | 手续费匹配码 | varchar | 255 |  | √ | ' ' | 手续费匹配码 |
| 42 | fpayer | fpayer | varchar | 256 |  | √ | ' ' |  |
| 43 | fisdataimport | fisdataimport | bpchar | 1 |  | √ | '0' |  |
| 44 | fbankrst | fbankrst | varchar | 255 |  | √ | ' ' |  |
| 45 | fflowserialno | 流程序列号 | varchar | 255 |  | √ | ' ' | 流程序列号 |
| 46 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 47 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 48 | fpaybilltype | fpaybilltype | int8 | 64 |  | √ | 0 |  |
| 49 | fsortid | 排序ID | varchar | 255 |  | √ | ' ' | 排序ID |
| 50 | fecommercebiztype | 电商流水业务分类 | varchar | 512 |  | √ | ' ' | 电商流水业务分类 |
| 51 | flastmodifytime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 52 | fisnoreceipt | fisnoreceipt | bpchar | 1 |  | √ | '0' |  |
| 53 | fecommercefaildreason | 电商流水入账失败原因 | varchar | 2000 |  | √ | ' ' | 电商流水入账失败原因 |
| 54 | fbillnobillno | 票号 | varchar | 255 |  | √ | ' ' | 票号 |
| 55 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 56 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 57 | fsettletype | fsettletype | int8 | 64 |  | √ | 0 |  |
| 58 | fishandlink | 是否手工关联 | bpchar | 1 |  | √ | '0' | 是否手工关联 |
| 59 | fdatasources | fdatasources | bpchar | 1 |  | √ | '0' |  |
| 60 | fscorgid | fscorgid | int8 | 64 |  | √ | 0 |  |
| 61 | fbusinessbillnum | 票据号 | varchar | 100 |  | √ | ' ' | 票据号 |
| 62 | fiscreatedtransup | fiscreatedtransup | bpchar | 1 |  | √ | '0' |  |
| 63 | fsettlecenteraccno | fsettlecenteraccno | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_transdetail_e |  | fnumber |
| 2 | t_bei_transdetail_e_pkey |  | fid |

---

## 银行收付处理-主表 t_bei_transdetail

- **表名称：** 银行收付处理-主表
- **表名：** t_bei_transdetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbankcheckflag | 对账标识码 | varchar | 255 |  | √ | ' ' | 对账标识码 |
| 3 | foppunit | 对方户名 | varchar | 255 |  | √ | ' ' | 对方户名 |
| 4 | ftranpackageid | ftranpackageid | varchar | 100 |  | √ | ' ' |  |
| 5 | fnote | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 6 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 7 | fsortno | 排序号 | int8 | 64 |  | √ | 0 | 排序号 |
| 8 | fiskdretflag | 是否银企付款 | bpchar | 1 |  | √ | '0' | 是否银企付款 |
| 9 | fisbankwithholding | 银行代扣 | bpchar | 1 |  | √ | '0' | 银行代扣 |
| 10 | fbankinterface | 银行接口 | varchar | 80 |  | √ | ' ' | 银行接口 |
| 11 | foppbanknumber | 对方账号 | varchar | 255 |  | √ | ' ' | 对方账号 |
| 12 | fdetailid | 明细流水号 | varchar | 100 |  | √ | ' ' | 明细流水号 |
| 13 | fpostscript | 附言 | varchar | 255 |  | √ | ' ' | 附言 |
| 14 | fbillno | 交易明细编号 | varchar | 100 |  | √ | ' ' | 交易明细编号 |
| 15 | freceiptno | 电子回单关联标记 | varchar | 100 |  | √ | ' ' | 电子回单关联标记 |
| 16 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fisfakedetail | fisfakedetail | bpchar | 1 |  | √ | '0' |  |
| 18 | fcreditamount | 收款金额 | numeric | 19 | 6 |  | null | 收款金额 |
| 19 | fdescription | 摘要 | varchar | 255 |  | √ | ' ' | 摘要 |
| 20 | fdebitamount | 付款金额 | numeric | 19 | 6 |  | null | 付款金额 |
| 21 | ftransbalance | 余额 | numeric | 19 | 6 |  | null | 余额 |
| 22 | fisdownbankjournal | 已下载银行日记账 | bpchar | 1 |  | √ | '0' | 已下载银行日记账 |
| 23 | fisdowntobankstate | 已经下载到银行对账单 | bpchar | 1 |  | √ | '0' | 已经下载到银行对账单 |
| 24 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: frombank :银企接口 import :模板引入 modify :系统修复 receiptgen :电子回单生成 fromifm :结算中心 cbs :招行CBS nb :宁波银行财资大管家 |
| 25 | fsrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型 |
| 26 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 27 | frulename | 适配规则 | varchar | 100 |  | √ | ' ' | 适配规则 |
| 28 | faccountbankid | 银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 29 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fbankdetailno | 银行流水号 | varchar | 128 |  | √ | ' ' | 银行流水号 |
| 31 | frecedbilltype | 接收单据类型 | varchar | 30 |  | √ | ' ' | 接收单据类型,枚举: cas_paybill :付款单 cas_paybill_synonym :同名转账 recbill :收款单 fca_transdownbill :下拨单 fca_transupbill :上划单 cas_agentreturnbill :代发退款单 cas_agentpaybill :代发处理单 cas_exchangebill :外币兑换单 cas_paybill_cash :现金存取 |
| 32 | fisreced | 是否接收 | bpchar | 1 |  | √ | '0' | 是否接收 |
| 33 | foppbank | 对方开户行 | varchar | 255 |  | √ | ' ' | 对方开户行 |
| 34 | fisdebit | fisdebit | bpchar | 1 |  | √ | '0' |  |
| 35 | frecedbillnumber | 接收单据编号 | varchar | 200 |  | √ | ' ' | 接收单据编号 |
| 36 | fbizrefno | 业务参考号 | varchar | 255 |  | √ | ' ' | 业务参考号 |
| 37 | fisdataimport | 是否导入 | bpchar | 1 |  | √ | '0' | 是否导入 |
| 38 | fbiztime | 交易时间 | timestamp | 0 |  |  | null | 交易时间 |
| 39 | freceredtype | 处理状态 | varchar | 5 |  | √ | '0' | 处理状态,枚举: 3 :已入账 0 :待入账 |
| 40 | fuse | 用途 | varchar | 255 |  | √ | ' ' | 用途 |
| 41 | fbiztype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: 1 :普通 2 :上划 3 :下拨 |
| 42 | fistransup | 银行上划 | bpchar | 1 |  | √ | '0' | 银行上划 |
| 43 | frawtranstime | frawtranstime | timestamp | 0 |  |  | null |  |
| 44 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fisnoreceipt | 确认无回单 | bpchar | 1 |  | √ | '0' | 确认无回单 |
| 46 | fisrefund | 是否退票 | bpchar | 1 |  | √ | '0' | 是否退票 |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 48 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 49 | funiqueseq | 银行主键 | varchar | 500 |  | √ | ' ' | 银行主键 |
| 50 | foriginalbankcheckflag | 对账标识码(银行返回) | varchar | 255 |  | √ | ' ' | 对账标识码(银行返回) |
| 51 | ffinancialtypeid | ffinancialtypeid | int8 | 64 |  | √ | 0 |  |
| 52 | fistransdown | 银行下拨 | bpchar | 1 |  | √ | '0' | 银行下拨 |
| 53 | fismatchereceipt | 跟电子回单匹配 | bpchar | 1 |  | √ | '0' | 跟电子回单匹配 |
| 54 | fbizdate | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 55 | fupdatetime | fupdatetime | timestamp | 0 |  |  | null |  |
| 56 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 57 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

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
