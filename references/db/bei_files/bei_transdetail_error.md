# 异常交易明细处理-bei_transdetail_error

## 异常交易明细处理-主表 t_bei_transdetail

- **表名称：** 异常交易明细处理-主表
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
| 24 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: frombank :银企接口 import :模板引入 modify :系统修复 receiptgen :电子回单生成 fromifm :结算中心 cbs :招行CBS |
| 25 | fsrcbilltype | 源单类型 | varchar | 30 |  | √ | ' ' | 源单类型 |
| 26 | fbankid | 开户银行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 27 | frulename | 适配入账规则 | varchar | 100 |  | √ | ' ' | 适配入账规则 |
| 28 | faccountbankid | 银行账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 29 | fcompanyid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fbankdetailno | 银行流水号 | varchar | 128 |  | √ | ' ' | 银行流水号 |
| 31 | frecedbilltype | 接收单据类型 | varchar | 30 |  | √ | ' ' | 接收单据类型,枚举: 6E41E17C :结算单 cas_paybill :付款单 recbill :收款单 5E920865 :下拨单 D125C4DE :上划单 other :其它单据 |
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
| 44 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fisnoreceipt | 确认无回单 | bpchar | 1 |  | √ | '0' | 确认无回单 |
| 46 | fisrefund | 是否退票 | bpchar | 1 |  | √ | '0' | 是否退票 |
| 47 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 48 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 49 | funiqueseq | 银行主键 | varchar | 500 |  | √ | ' ' | 银行主键 |
| 50 | foriginalbankcheckflag | 对账标识码（银行返回） | varchar | 255 |  | √ | ' ' | 对账标识码（银行返回） |
| 51 | ffinancialtypeid | ffinancialtypeid | int8 | 64 |  | √ | 0 |  |
| 52 | fistransdown | 银行下拨 | bpchar | 1 |  | √ | '0' | 银行下拨 |
| 53 | fismatchereceipt | 跟电子回单匹配 | bpchar | 1 |  | √ | '0' | 跟电子回单匹配 |
| 54 | fbizdate | 交易日期 | timestamp | 0 |  |  | null | 交易日期 |
| 55 | fupdatetime | fupdatetime | timestamp | 0 |  |  | null |  |
| 56 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 57 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

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

## 异常交易明细处理-分表 t_bei_transdetail_e

- **表名称：** 异常交易明细处理-分表
- **表名：** t_bei_transdetail_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fiscreatedtransdown | fiscreatedtransdown | bpchar | 1 |  | √ | '0' |  |
| 3 | fagentaccname | 被代理户名 | varchar | 255 |  | √ | ' ' | 被代理户名 |
| 4 | fhandlebill | fhandlebill | varchar | 64 |  | √ | ' ' |  |
| 5 | ftransfercharge | 手续费 | numeric | 19 | 6 | √ | 0.000000 | 手续费 |
| 6 | frecbilltype | frecbilltype | int8 | 64 |  | √ | 0 |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | frequestserialno | 银企请求流水号 | varchar | 255 |  | √ | ' ' | 银企请求流水号 |
| 9 | fbasepayee | fbasepayee | int8 | 64 |  | √ | 0 |  |
| 10 | fbustype | busType | varchar | 255 |  | √ | ' ' | busType |
| 11 | fsettlecenteraccname | fsettlecenteraccname | varchar | 100 |  | √ | ' ' |  |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 13 | fbasepayer | fbasepayer | int8 | 64 |  | √ | 0 |  |
| 14 | freceiptno | freceiptno | varchar | 100 |  | √ | ' ' |  |
| 15 | fbatchno | 银企付款提交的批次号 | varchar | 255 |  | √ | ' ' | 银企付款提交的批次号 |
| 16 | fpayeebasetype | fpayeebasetype | varchar | 64 |  | √ | ' ' |  |
| 17 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 18 | fkdretflag | KD标识 | varchar | 255 |  | √ | ' ' | KD标识 |
| 19 | fautorecorpay | 自动收付款 | bpchar | 1 |  | √ | '0' | 自动收付款 |
| 20 | ftransdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 21 | freservefield | 预留字段 | varchar | 512 |  | √ | ' ' | 预留字段 |
| 22 | fresponseserailno | 银行响应流水号 | varchar | 255 |  | √ | ' ' | 银行响应流水号 |
| 23 | fisdowntobankstate | fisdowntobankstate | bpchar | 1 |  | √ | '0' |  |
| 24 | fagentaccno | 被代理账号 | varchar | 80 |  | √ | ' ' | 被代理账号 |
| 25 | fsmartmatch | 智能匹配 | varchar | 10 |  | √ | ' ' | 智能匹配,枚举: 1 :已匹配 0 :未匹配 |
| 26 | fagentaccbkname | fagentaccbkname | varchar | 100 |  | √ | ' ' |  |
| 27 | fnumber | fnumber | varchar | 100 |  | √ | ' ' |  |
| 28 | fdesc | fdesc | varchar | 255 |  | √ | ' ' |  |
| 29 | freceredway | freceredway | varchar | 30 |  | √ | ' ' |  |
| 30 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 31 | fcustomerid | fcustomerid | int8 | 64 |  | √ | 0 |  |
| 32 | fagentaccbankname | 被代理账号开户行 | varchar | 255 |  | √ | ' ' | 被代理账号开户行 |
| 33 | fextdata | extData | varchar | 255 |  | √ | ' ' | extData |
| 34 | fclaimnoticebillno | 收款认领通知 | varchar | 30 |  | √ | ' ' | 收款认领通知 |
| 35 | fpayee | fpayee | varchar | 256 |  | √ | ' ' |  |
| 36 | flastmodifierid | flastmodifierid | int8 | 64 |  | √ | 0 |  |
| 37 | fpayerbasetype | fpayerbasetype | varchar | 64 |  | √ | ' ' |  |
| 38 | frecedbillentryid | frecedbillentryid | int8 | 64 |  | √ | 0 |  |
| 39 | fpayer | fpayer | varchar | 256 |  | √ | ' ' |  |
| 40 | fisdataimport | fisdataimport | bpchar | 1 |  | √ | '0' |  |
| 41 | fbankrst | fbankrst | varchar | 255 |  | √ | ' ' |  |
| 42 | fflowserialno | 流程序列号 | varchar | 255 |  | √ | ' ' | 流程序列号 |
| 43 | fcreatedate | fcreatedate | timestamp | 0 |  |  | null |  |
| 44 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 45 | fpaybilltype | fpaybilltype | int8 | 64 |  | √ | 0 |  |
| 46 | fsortid | 排序ID | varchar | 255 |  | √ | ' ' | 排序ID |
| 47 | flastmodifytime | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 48 | fisnoreceipt | fisnoreceipt | bpchar | 1 |  | √ | '0' |  |
| 49 | fbillnobillno | 票号 | varchar | 255 |  | √ | ' ' | 票号 |
| 50 | fremark | fremark | varchar | 512 |  | √ | ' ' |  |
| 51 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 52 | fsettletype | fsettletype | int8 | 64 |  | √ | 0 |  |
| 53 | fishandlink | fishandlink | bpchar | 1 |  | √ | '0' |  |
| 54 | fdatasources | fdatasources | bpchar | 1 |  | √ | '0' |  |
| 55 | fscorgid | fscorgid | int8 | 64 |  | √ | 0 |  |
| 56 | fbusinessbillnum | 票据号 | varchar | 100 |  | √ | ' ' | 票据号 |
| 57 | fiscreatedtransup | fiscreatedtransup | bpchar | 1 |  | √ | '0' |  |
| 58 | fsettlecenteraccno | fsettlecenteraccno | varchar | 100 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bei_transdetail_e |  | fnumber |
| 2 | t_bei_transdetail_e_pkey |  | fid |
