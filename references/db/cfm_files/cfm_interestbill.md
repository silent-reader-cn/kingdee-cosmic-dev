# 付息处理-cfm_interestbill

## 付息处理-主表 t_cfm_interestbill

- **表名称：** 付息处理-主表
- **表名：** t_cfm_interestbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwriteoffdate | 冲销日期 | timestamp | 0 |  |  | null | 冲销日期 |
| 3 | finsttype | 利率类型 | varchar | 80 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 agree :协议利率 |
| 4 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 5 | flender | 贷款人 | varchar | 80 |  | √ | ' ' | 贷款人 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fbitbackinfo | 退单信息 | varchar | 255 |  | √ | ' ' | 退单信息 |
| 8 | finstbankacctid | 付息银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 9 | fafterchargeinstamt | 冲销后应付利息 | numeric | 19 | 6 | √ | 0.000000 | 冲销后应付利息 |
| 10 | fbillno | 付息单编号 | varchar | 80 |  | √ | ' ' | 付息单编号 |
| 11 | fstartinstdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 12 | fclientorgid | 受托机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 13 | flendernature | 贷款人性质 | varchar | 80 |  | √ | ' ' | 贷款人性质,枚举: outgroup :集团外 ingroup :集团内 |
| 14 | ffinproductid | 融资品种 | int8 | 64 |  | √ | 0 | [融资品种 cfm_financingvarieties](../cfm_files/cfm_financingvarieties.md) |
| 15 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fproductfactoryid | fproductfactoryid | int8 | 64 |  | √ | 0 |  |
| 17 | fpredictinstamt | 测算利息 | numeric | 19 | 6 | √ | 0.000000 | 测算利息 |
| 18 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 19 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fafterexpiredate | 展期后到期日期 | timestamp | 0 |  |  | null | 展期后到期日期 |
| 21 | fthischargeinstamt | 本单冲销金额 | numeric | 19 | 6 | √ | 0.000000 | 本单冲销金额 |
| 22 | fcontractbillno | 合同单据编号 | varchar | 80 |  | √ | ' ' | 合同单据编号 |
| 23 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fcompanyid | fcompanyid | int8 | 64 |  | √ | 0 |  |
| 25 | ffinorginfoid | 贷款人 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 26 | fbatchnoid | 冲销批次id | int8 | 64 |  | √ | 0 | 冲销批次id |
| 27 | fpayeebillno | 付款单编号 | varchar | 80 |  | √ | ' ' | 付款单编号 |
| 28 | fwriteoffstatus | 冲销状态 | varchar | 80 |  | √ | ' ' | 冲销状态,枚举: no_writeoff :未冲销 writeoff :已冲销 |
| 29 | fendinstdate | 结息日 | timestamp | 0 |  |  | null | 结息日 |
| 30 | factualinstamt | 应付利息 | numeric | 19 | 6 | √ | 0.000000 | 应付利息 |
| 31 | fisinit | 是否初始化 | bpchar | 1 |  | √ | '0' | 是否初始化 |
| 32 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 34 | frepaymentid | 还款id | int8 | 64 |  | √ | 0 | 还款id |
| 35 | fbechargeinstamt | 冲销前应付利息 | numeric | 19 | 6 | √ | 0.000000 | 冲销前应付利息 |
| 36 | floandate | 放款日期 | timestamp | 0 |  |  | null | 放款日期 |
| 37 | finstbillctg | 付息单类别 | varchar | 80 |  | √ | ' ' | 付息单类别,枚举: payinterst :付息 payprinandinte :还本付息 |
| 38 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 39 | fdrawamt | 提款金额 | numeric | 19 | 6 | √ | 0.000000 | 提款金额 |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | floanbillno | 提款单编号 | varchar | 80 |  | √ | ' ' | 提款单编号 |
| 42 | finstschemeid | 结息方案 | int8 | 64 |  | √ | 0 | [结息计划方案 cfm_inscheme](../cfm_files/cfm_inscheme.md) |
| 43 | fcontractno | 合同号 | varchar | 80 |  | √ | ' ' | 合同号 |
| 44 | floanorgid | 贷款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 45 | fnotrepayamt | 未还本金 | numeric | 19 | 6 | √ | 0.000000 | 未还本金 |
| 46 | floantype | 贷款类型 | varchar | 80 |  | √ | ' ' | 贷款类型,枚举: loan :普通贷款 sl :银团贷款 ec :企业往来 entrust :委托贷款 bond :债券发行 |
| 47 | fbizdate | 付息日 | timestamp | 0 |  |  | null | 付息日 |
| 48 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 49 | fcurrencyid | 借款币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_interestbill_pkey |  | fid |
| 2 | idx_cfm_interestbill_bnd |  | fbillno,fbizdate |

---

## 付息处理-分表 t_cfm_interestbill_e

- **表名称：** 付息处理-分表
- **表名：** t_cfm_interestbill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flenddraccountid | 借款方借方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 3 | fbankcheckflag | 对账标识码 | varchar | 80 |  | √ | ' ' | 对账标识码 |
| 4 | forgid | 借款人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fconfirmstatus | 确认状态 | varchar | 30 |  | √ | ' ' | 确认状态,枚举: registrying :登记中 waitconfirm :待确认 yetconfirm :已确认 yetreturn :已回退 |
| 6 | fiscycleloan | fiscycleloan | bpchar | 1 |  | √ | '0' |  |
| 7 | fcompanyer | 借款人(旧) | varchar | 30 |  | √ | ' ' | 借款人(旧) |
| 8 | fpayeebankid | 收款银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 9 | freturnreason | 退回原因 | varchar | 255 |  | √ | ' ' | 退回原因 |
| 10 | fsettlestatus | 提交结算中心状态 | varchar | 80 |  | √ | ' ' | 提交结算中心状态,枚举: addnew :新增 submit :已提交 accept :已受理 bitback :已退回 hide :隐藏 |
| 11 | fregistorgid | 登记组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fcreditorgid | 债权人(组织) | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fpayeeaccttext | 收款账号 | varchar | 80 |  | √ | ' ' | 收款账号 |
| 14 | fconfirmdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 15 | fcreditorid | 债权人id | int8 | 64 |  | √ | 0 | 债权人id |
| 16 | fdebtorid | 借款人id | int8 | 64 |  | √ | 0 | 借款人id |
| 17 | floandraccountid | 贷款方借方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 18 | fauto | 自动付/收息 | bpchar | 1 |  | √ | '0' | 自动付/收息 |
| 19 | ftextdebtor | 借款人(文本) | varchar | 80 |  | √ | ' ' | 借款人(文本) |
| 20 | frecbillno | 收款单编号 | varchar | 80 |  | √ | ' ' | 收款单编号 |
| 21 | fbatchno | fbatchno | varchar | 80 |  | √ | ' ' |  |
| 22 | flendcraccountid | 借款方贷方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 23 | fproductfactoryid | 融资模型 | int8 | 64 |  | √ | 0 | [融资模型 cfm_productfactory](../cfm_files/cfm_productfactory.md) |
| 24 | fpaybillid | 付款单 | int8 | 64 |  | √ | 0 | [付款单 cas_paybill_f7](../cas_files/cas_paybill_f7.md) |
| 25 | fdebtortype | 借款人类型 | varchar | 30 |  | √ | ' ' | 借款人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 custom :客商 other :其它 |
| 26 | fpayeetype | 收款人类型 | varchar | 80 |  | √ | ' ' | 收款人类型,枚举: bd_supplier :供应商 fbd_other :其他 |
| 27 | ftextcreditor | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 28 | fsettlecenterid | fsettlecenterid | int8 | 64 |  | √ | 0 |  |
| 29 | fpayeeid | 收款人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 30 | fpayamt | fpayamt | numeric | 23 | 10 | √ | 0 |  |
| 31 | fbizdealno | fbizdealno | varchar | 80 |  | √ | ' ' |  |
| 32 | floancraccountid | 贷款方贷方科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 33 | fconfirmerid | 确认人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fcreditortype | 债权人类型 | varchar | 30 |  | √ | ' ' | 债权人类型,枚举: innerunit :内部单位 bank :银行 finorg :非银行金融机构 settlecenter :结算中心 custom :客商 other :其他 |
| 35 | fdatasource | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: cfm :融资管理 invest :投资管理 ifm :内部金融管理 bond :债券 |
| 36 | fpayeetext | 收款人 | varchar | 80 |  | √ | ' ' | 收款人 |
| 37 | fconfirmtime | 确认时间 | timestamp | 0 |  |  | null | 确认时间 |
| 38 | floaneracctbankid | 收息银行账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cfm_interstbill_bnd_e |  | fdatasource |
| 2 | pk_t_cfm_interestbill_e |  | fid |

---

## 付息处理-多语言表 t_cfm_interestbill_l

- **表名称：** 付息处理-多语言表
- **表名：** t_cfm_interestbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbitbackinfo | 退单信息 | varchar | 255 |  | √ | ' ' | 退单信息 |
| 3 | flocaleid | flocaleid | varchar | 80 |  | √ | ' ' | localeid |
| 4 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fpkid | fpkid | varchar | 80 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cfm_interestbill_l_pkey |  | fpkid |
| 2 | idx_cfm_interestbill_l |  | fid,flocaleid |

---

## 关联子实体-子表 t_cfm_interestbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cfm_interestbill_lk

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
| 1 | t_cfm_interestbill_lk_pkey |  | fpkid |
| 2 | idx_cfm_interestbill_lk |  | fid |

---

## 利息预算明细-子表 t_cfm_interestbill_entrys

- **表名称：** 利息预算明细-子表
- **表名：** t_cfm_interestbill_entrys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffloatrate | 加点利率（%） | numeric | 19 | 6 | √ | 0 | 加点利率（%） |
| 3 | flasttotalint | 上期累计基准利息 | numeric | 19 | 6 | √ | 0 | 上期累计基准利息 |
| 4 | fconfirmratedate | 利率确定日 | timestamp | 0 |  |  | null | 利率确定日 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | finstprincipalamt | 计息本金 | numeric | 19 | 6 | √ | 0.000000 | 计息本金 |
| 7 | finstctg | 利息类别 | varchar | 80 |  | √ | ' ' | 利息类别,枚举: normal :正常利息 extend :展期利息 overdue :逾期利息 |
| 8 | ffloatint | 加点利息 | numeric | 19 | 6 | √ | 0 | 加点利息 |
| 9 | ftotalint | 总利息 | numeric | 19 | 6 | √ | 0 | 总利息 |
| 10 | flookdays | 计息天数（利率确定日） | int4 | 32 |  | √ | 0 | 计息天数（利率确定日） |
| 11 | frate | 利率(%) | numeric | 23 | 10 | √ | 0 | 利率(%) |
| 12 | finststartdate | 计息开始日 | timestamp | 0 |  |  | null | 计息开始日 |
| 13 | finstdays | 计息天数 | int8 | 64 |  | √ | 0 | 计息天数 |
| 14 | fratetrandays | 利率转换天数 | int8 | 64 |  | √ | 0 | 利率转换天数 |
| 15 | finstenddate | 计息结束日 | timestamp | 0 |  |  | null | 计息结束日 |
| 16 | finstamt | 利息金额 | numeric | 19 | 6 | √ | 0.000000 | 利息金额 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | fcurtotalint | 当期累计基准利息 | numeric | 19 | 6 | √ | 0 | 当期累计基准利息 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cfm_interestbill_entrys |  | fid |
| 2 | t_cfm_interestbill_entrys_pkey |  | fentryid |

---

## 付息处理-关联追踪表 t_cfm_interestbill_tc

- **表名称：** 付息处理-关联追踪表
- **表名：** t_cfm_interestbill_tc

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
| 1 | idx_cfm_interestbill_tc_tid |  | ftid |
| 2 | idx_cfm_interestbill_tc |  | ftbillid |
| 3 | idx_cfm_interestbill_tc_tbill |  | ftbillid |
| 4 | t_cfm_interestbill_tc_pkey |  | fid |

---

## 关联子实体-子表 t_cfm_interestbill_entrys_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cfm_interestbill_entrys_lk

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
| 1 | t_cfm_interestbill_entrys_lk_pkey |  | fpkid |
| 2 | idx_cfm_ib_entrys_lk |  | fentryid |

---

## 付息处理-反写记录表 t_cfm_interestbill_wb

- **表名称：** 付息处理-反写记录表
- **表名：** t_cfm_interestbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 80 |  | √ | ' ' |  |
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
| 1 | idx_cfm_interestbill_wb |  | fid |
| 2 | t_cfm_interestbill_wb_pkey |  | fentryid |
