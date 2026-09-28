# 信用证开证初始化-lc_lettercredit_init

## 到单分录-子表 t_lc_credit_initentry

- **表名称：** 到单分录-子表
- **表名：** t_lc_credit_initentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | farrivalno | 到单编号 | varchar | 50 |  | √ | ' ' | 到单编号 |
| 3 | fendacceptdate | 最迟承兑/付款日期 | timestamp | 0 |  |  | null | 最迟承兑/付款日期 |
| 4 | farrivalamount | 到单金额 | numeric | 19 | 6 | √ | 0 | 到单金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | farrivalway | 到单处理方式 | varchar | 50 |  | √ | ' ' | 到单处理方式,枚举: protest :拒付 accept :承兑 payment :付款 |
| 7 | fdoneamount | 已付金额 | numeric | 19 | 6 | √ | 0 | 已付金额 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | farrivaldate | 到单日期 | timestamp | 0 |  |  | null | 到单日期 |
| 10 | fendpaydate | 最迟付款日期 | timestamp | 0 |  |  | null | 最迟付款日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_credit_initentry |  | fentryid |
| 2 | idx_lc_credit_initentry |  | fid |

---

## 信用证开证初始化-多语言表 t_lc_lettercredit_init_l

- **表名称：** 信用证开证初始化-多语言表
- **表名：** t_lc_lettercredit_init_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | ftransportway | 运输方式 | varchar | 255 |  | √ | ' ' | 运输方式 |
| 4 | fvalidaddress | 有效期限地点 | varchar | 255 |  | √ | ' ' | 有效期限地点 |
| 5 | fdestination | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 6 | fcargodesc | 货物描述 | varchar | 255 |  | √ | ' ' | 货物描述 |
| 7 | fbenefitaddress | 受益人地址 | varchar | 255 |  | √ | ' ' | 受益人地址 |
| 8 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 9 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 10 | fstartplace | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 11 | fapplyaddress | 开证人地址 | varchar | 255 |  | √ | ' ' | 开证人地址 |
| 12 | fbankaddress | 通知行地址 | varchar | 255 |  | √ | ' ' | 通知行地址 |
| 13 | funloadplace | 卸货地 | varchar | 255 |  | √ | ' ' | 卸货地 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_lettercredit_init_l |  | fid,flocaleid |
| 2 | pk_t_lc_lettercredit_init_l |  | fpkid |

---

## 保证金分录-子表 t_lc_credit_suretyentry

- **表名称：** 保证金分录-子表
- **表名：** t_lc_credit_suretyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsuretycurrency | 保证金币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fsuretyexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 4 | fsuretyfinorg | 存款机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 5 | fsuretyamount | 保证金金额 | numeric | 23 | 10 | √ | 0 | 保证金金额 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsuretyaccount | 保证金账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 8 | fsuretybill | 单据编号 | int8 | 64 |  | √ | 0 | [保证金存入处理F7 fbd_suretybill_f7](../fbd_files/fbd_suretybill_f7.md) |
| 9 | fsuretyinvestorgtype | 存款机构类型 | varchar | 50 |  | √ | ' ' | 存款机构类型,枚举: bd_finorginfo :合作金融机构 bd_customer :客户 bd_supplier :供应商 fbd_other :其他 |
| 10 | fsuretysurplusamount | 剩余金额 | numeric | 23 | 10 | √ | 0 | 剩余金额 |
| 11 | fsuretyintdate | 保证金起息日 | timestamp | 0 |  |  | null | 保证金起息日 |
| 12 | fsuretyterm | 期限（ymd） | varchar | 50 |  | √ | ' ' | 期限（ymd） |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fsuretyfinorgother | 存款机构 | varchar | 255 |  | √ | ' ' | 存款机构 |
| 15 | fsuretysource | 单据来源 | varchar | 50 |  | √ | ' ' | 单据来源,枚举: hand :债务生成 linkgen :保证金生成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_credit_suretyentry |  | fentryid |
| 2 | idx_lc_credit_suretyentry |  | fid |

---

## 信用证开证初始化-主表 t_lc_lettercredit_init

- **表名称：** 信用证开证初始化-主表
- **表名：** t_lc_lettercredit_init

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransportway | 运输方式 | varchar | 255 |  | √ | ' ' | 运输方式 |
| 3 | fcredittypeid | 信用证类型 | int8 | 64 |  | √ | 0 | [信用证类型 lc_billtype](../lc_files/lc_billtype.md) |
| 4 | fvalidaddress | 有效期限地点 | varchar | 255 |  | √ | ' ' | 有效期限地点 |
| 5 | fcargodesc | 货物描述 | varchar | 255 |  | √ | ' ' | 货物描述 |
| 6 | famount | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 7 | fcreditno | 信用证号 | varchar | 50 |  | √ | ' ' | 信用证号 |
| 8 | fiscancel | 可撤销 | bpchar | 1 |  | √ | '0' | 可撤销 |
| 9 | fstartplace | 起运地 | varchar | 255 |  | √ | ' ' | 起运地 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fbankaddress | 通知行地址 | varchar | 255 |  | √ | ' ' | 通知行地址 |
| 13 | flowstr | 金额下限 | varchar | 50 |  | √ | ' ' | 金额下限 |
| 14 | fisnationalcard | 国际证 | bpchar | 1 |  | √ | '0' | 国际证 |
| 15 | funloadplace | 卸货地 | varchar | 255 |  | √ | ' ' | 卸货地 |
| 16 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 17 | famountscaleupper | 溢短装金额浮动比例上限（%） | numeric | 19 | 6 | √ | 0 | 溢短装金额浮动比例上限（%） |
| 18 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fismakeover | 可转让 | bpchar | 1 |  | √ | '0' | 可转让 |
| 21 | fcreditstatus | 信用证状态 | varchar | 50 |  | √ | ' ' | 信用证状态,枚举: done_register :已登记 done_close :已闭卷 done_repeal :已撤证 change_ing :改证中 repeal_ing :撤证中 close_ing :闭卷中 |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fapplydate | 登记日期 | timestamp | 0 |  |  | null | 登记日期 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fdestination | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 26 | fguarantee | 担保方式 | varchar | 50 |  | √ | ' ' | 担保方式,枚举: 2 :保证 3 :保证金 4 :抵押 5 :质押 6 :其他 7 :信用/无担保 |
| 27 | fbizcontactorid | 业务联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fisforward | 远期 | bpchar | 1 |  | √ | '0' | 远期 |
| 29 | fbenefitaddress | 受益人地址 | varchar | 255 |  | √ | ' ' | 受益人地址 |
| 30 | fforwarddays | 远期天数 | int8 | 64 |  | √ | 0 | 远期天数 |
| 31 | fbizcontactinfo | 业务联系方式 | varchar | 50 |  | √ | ' ' | 业务联系方式 |
| 32 | fapplyaddress | 开证人地址 | varchar | 255 |  | √ | ' ' | 开证人地址 |
| 33 | fbizdate | 开证日期 | timestamp | 0 |  |  | null | 开证日期 |
| 34 | fbankid | 开证行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 35 | famountscalelow | 溢短装金额浮动比例下限（%） | numeric | 19 | 6 | √ | 0 | 溢短装金额浮动比例下限（%） |
| 36 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 37 | fupperstr | 金额上限 | varchar | 50 |  | √ | ' ' | 金额上限 |
| 38 | fcreditlimitid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_lc_lettercredit_init |  | fid |
| 2 | idx_lc_lettercredit_init |  | fbillno |

---

## 担保信息分录-子表 t_lc_credit_gmentry

- **表名称：** 担保信息分录-子表
- **表名：** t_lc_credit_gmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fgcontract | 担保单据编号 | int8 | 64 |  | √ | 0 | [担保合同 gm_guaranteecontract_f7](../gm_files/gm_guaranteecontract_f7.md) |
| 3 | fgexchrate | 折算汇率 | numeric | 23 | 10 | √ | 0 | 折算汇率 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fgratio | 担保比例(%) | numeric | 23 | 10 | √ | 0 | 担保比例(%) |
| 6 | fgcontractcurrency | 担保合同币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fgamount | 担保金额 | numeric | 23 | 10 | √ | 0 | 担保金额 |
| 9 | fgcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_credit_gmentry |  | fid |
| 2 | pk_t_lc_credit_gmentry |  | fentryid |

---

## 信用证开证初始化-分表 t_lc_lettercredit_init_e

- **表名称：** 信用证开证初始化-分表
- **表名：** t_lc_lettercredit_init_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freimbursingbank | 偿付行 | varchar | 255 |  | √ | ' ' | 偿付行 |
| 3 | forgid | 开证人 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fnoticebank | 通知行 | varchar | 255 |  | √ | ' ' | 通知行 |
| 5 | fnegotiatingbank | 议付行 | varchar | 255 |  | √ | ' ' | 议付行 |
| 6 | fpromisrate | 保证金比例(%) | numeric | 23 | 2 | √ | 0 | 保证金比例(%) |
| 7 | fbenefiterother | 受益人 | varchar | 255 |  | √ | ' ' | 受益人 |
| 8 | ftotalsuretymoney | 保证金累计金额 | numeric | 23 | 10 | √ | 0 | 保证金累计金额 |
| 9 | fvaliddate | 有效期 | timestamp | 0 |  |  | null | 有效期 |
| 10 | fnegotiatingdate | 议付日期 | timestamp | 0 |  |  | null | 议付日期 |
| 11 | fisbatch | 分批 | bpchar | 1 |  | √ | '0' | 分批 |
| 12 | fdealbilltermstart | 交单期限.开始 | timestamp | 0 |  |  | null | 交单期限.开始 |
| 13 | fbankcountryid | 通知行国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 14 | flastdate | 最迟装期 | timestamp | 0 |  |  | null | 最迟装期 |
| 15 | fsuretycur | 保证金币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 16 | fsuretymoney | 保证金初始金额 | numeric | 23 | 10 | √ | 0 | 保证金初始金额 |
| 17 | fcreditamount | 实际占用授信金额 | numeric | 23 | 10 | √ | 0 | 实际占用授信金额 |
| 18 | fdealbilltermend | 交单期限.结束 | timestamp | 0 |  |  | null | 交单期限.结束 |
| 19 | fistransfer | 转运 | bpchar | 1 |  | √ | '0' | 转运 |
| 20 | fnoticebankid | 通知行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 21 | fconfirmingbank | 保兑行 | varchar | 255 |  | √ | ' ' | 保兑行 |
| 22 | fbenefitcountryid | 受益人国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 23 | fisnegotiating | 议付 | bpchar | 1 |  | √ | '0' | 议付 |
| 24 | fcargocountryid | 货物国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 25 | fapplycountryid | 开证人国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 26 | fbenefitertype | 受益人类型 | varchar | 50 |  | √ | ' ' | 受益人类型,枚举: bd_supplier :供应商 bd_customer :客户 bos_org :公司 fbd_other :其他 |
| 27 | fbenefiterid | 受益人 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lc_lettercredit_init_e |  | forgid |
| 2 | pk_t_lc_lettercredit_init_e |  | fid |
