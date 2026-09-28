# 银行账户-bd_accountbanks

## 限定结算方式-多选基础资料表 t_bd_accountbanks_st

- **表名称：** 限定结算方式-多选基础资料表
- **表名：** t_bd_accountbanks_st

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_accountbanks_st_fk |  | fid,fbasedataid |
| 2 | t_bd_accountbanks_st_pkey |  | fpkid |

---

## 银行账户-主表 t_bd_accountbanks

- **表名称：** 银行账户-主表
- **表名：** t_bd_accountbanks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | 开户组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fparentbankacctid | fparentbankacctid | int8 | 64 |  | √ | 0 |  |
| 5 | fclosedate | 销户日期 | timestamp | 0 |  |  | null | 销户日期 |
| 6 | fcommonseal | 公章名称 | varchar | 80 |  | √ | ' ' | 公章名称 |
| 7 | fauthorizeinfo | fauthorizeinfo | varchar | 512 |  | √ | ' ' |  |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | finneracctid | 内部账户 | int8 | 64 |  | √ | 0 | [内部账户管理 ifm_inneracct](../ifm_files/ifm_inneracct.md) |
| 10 | fmodifytime | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |
| 11 | facctstyle | 账户类型 | varchar | 80 |  | √ | ' ' | 账户类型,枚举: basic :基本存款账户 normal :一般存款账户 temp :临时存款账户 spcl :专用存款账户 fgn_curr :经常项目外汇账户 fng_fin :资本项目外汇账户 |
| 12 | fbankinterface | 银企云接口 | varchar | 80 |  | √ | ' ' | 银企云接口,枚举: |
| 13 | fisdefaultpay | 默认付款户 | bpchar | 1 |  | √ | ' ' | 默认付款户 |
| 14 | ffinancialchapter | 财务专用章名称 | varchar | 80 |  | √ | ' ' | 财务专用章名称 |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fbankfunc | 网上银行功能 | varchar | 80 |  | √ | ' ' | 网上银行功能,枚举: query :查询 trans :转账 invest :投资理财 ecd :电票 |
| 17 | fclosedatef | 预计销户日期 | timestamp | 0 |  |  | null | 预计销户日期 |
| 18 | faccttype | 账户性质 | varchar | 80 |  | √ | ' ' | 账户性质,枚举: in_out :收支户 in :收入户 out :支出户 |
| 19 | fauthquerpt | 授权查询银行回单 | bpchar | 1 |  | √ | '0' | 授权查询银行回单 |
| 20 | fcurrencyname | 多币别名称 | varchar | 80 |  | √ | ' ' | 多币别名称 |
| 21 | fnoopenlinereason | fnoopenlinereason | varchar | 512 |  | √ | ' ' |  |
| 22 | facctpropertyid | 账户用途 | int8 | 64 |  | √ | 0 | [账户用途 bd_acctpurpose](../basedata_files/bd_acctpurpose.md) |
| 23 | facctstatus | 账户状态 | varchar | 80 |  | √ | ' ' | 账户状态,枚举: normal :正常 closing :销户中 changing :变更中 closed :已销户 freeze :冻结 |
| 24 | flegalperson | 账户法定代表人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fenable | 使用状态 | varchar | 80 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 27 | fbankid | 开户行 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 28 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 29 | fcompanyid | 申请组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fismulcurrency | 是否多币别 | bpchar | 1 |  | √ | ' ' | 是否多币别 |
| 31 | fdefaultcurrencyid | 默认币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 32 | fk_bj73_textfield1 | 回款户名 | varchar | 50 |  | √ | ' ' | 回款户名 |
| 33 | fstatus | 数据状态 | varchar | 80 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 36 | fmanagecurrencyid | 账户管理费 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 37 | finneraccountid | finneraccountid | int8 | 64 |  | √ | 0 |  |
| 38 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 39 | facctmanageamt | 账户管理费 | numeric | 19 | 6 | √ | 0.000000 | 账户管理费 |
| 40 | facctclassify | 账户分类 | varchar | 30 |  | √ | ' ' | 账户分类,枚举: I :内部账户 B :银行账户 |
| 41 | fbebankfunc | 银企云功能 | varchar | 80 |  | √ | ' ' | 银企云功能,枚举: query :查询 pay :支付 receipt :电子回单 ecd :电票 proxyinquiry :代理查询 |
| 42 | fbanktype | 银行类别 | int8 | 64 |  | √ | 0 | [银行类别 bd_bankcgsetting](../basedata_files/bd_bankcgsetting.md) |
| 43 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fmodifierid | 最后更新人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fmanagerid | 账户管理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 46 | fenglishname | 账户名称（英文） | varchar | 255 |  | √ | ' ' | 账户名称（英文） |
| 47 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 48 | fstrategyid | 账户管理策略 | int8 | 64 |  | √ | 0 | [账户管理策略 am_strategy](../am_files/am_strategy.md) |
| 49 | fnoopenbeireason | fnoopenbeireason | varchar | 512 |  | √ | ' ' |  |
| 50 | fissetbankinterface | 开通银企接口 | bpchar | 1 |  | √ | ' ' | 开通银企接口 |
| 51 | fbankaccountnumber | 银行账号 | varchar | 80 |  | √ | ' ' | 银行账号 |
| 52 | fshortnumber | 助记码 | varchar | 80 |  | √ | ' ' | 助记码 |
| 53 | fopendate | 开户日期 | timestamp | 0 |  |  | null | 开户日期 |
| 54 | ffinorgtype | 金融机构类别 | varchar | 80 |  | √ | ' ' | 金融机构类别,枚举: 0 :银行 1 :结算中心 3 :财务公司 4 :第三方支付机构 2 :非银行金融机构 |
| 55 | fscorgid | 结算中心业务单元 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 56 | fctrlstrategy | 控制策略 | varchar | 80 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 57 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 58 | fk_bj73_textfield | 识别规则 | varchar | 2000 |  | √ | ' ' | 识别规则 |
| 59 | fisopenbank | 开通企业网上银行 | bpchar | 1 |  | √ | ' ' | 开通企业网上银行 |
| 60 | fuseorgid | fuseorgid | int8 | 64 |  | √ | 0 |  |
| 61 | fisdefaultrec | 默认收款户 | bpchar | 1 |  | √ | ' ' | 默认收款户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_accountbanks_fcompanyid |  | fcompanyid,fbankid |
| 2 | idx_t_bd_acctbanks_num |  | fnumber |
| 3 | t_bd_accountbanks_pkey |  | fid |
| 4 | idx_t_bd_accountbanks_master |  | fmasterid |
| 5 | idx_t_bd_accountbanks_createorg |  | fcreateorgid |

---

## 单据体-子表 t_am_bankfunclist

- **表名称：** 单据体-子表
- **表名：** t_am_bankfunclist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factualopendate | 实际开通日期 | timestamp | 0 |  |  | null | 实际开通日期 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fenable | 是否启用 | bpchar | 1 |  | √ | '0' | 是否启用 |
| 5 | fpredictopendate | 预计开通日期 | timestamp | 0 |  |  | null | 预计开通日期 |
| 6 | fbankfunction | 银企功能 | varchar | 50 |  | √ | ' ' | 银企功能,枚举: query :查询 pay :支付 receipt :电子回单 ecd :电票 proxyinquiry :代理查询 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fbillinfo | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_am_bankfunclist_fid |  | fid |
| 2 | pk_t_am_bankfunclist |  | fentryid |

---

## 网银子账户-多选基础资料表 t_bd_accountbanks_nb

- **表名称：** 网银子账户-多选基础资料表
- **表名：** t_bd_accountbanks_nb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [网银子账户 bd_netbankacct](../basedata_files/bd_netbankacct.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_accountbanks_nb_fk |  | fid |
| 2 | t_bd_accountbanks_nb_pkey |  | fpkid |

---

## 银行账户-分表 t_bd_accountbanks_a

- **表名称：** 银行账户-分表
- **表名：** t_bd_accountbanks_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffundaccflag | 集中资金账户标识 | varchar | 80 |  |  | ' ' | 集中资金账户标识,枚举: 00 :非监控 01 :可监控 02 :可归集 |
| 3 | fisvirtual | 虚拟账户 | bpchar | 1 |  | √ | '0' | 虚拟账户 |
| 4 | fisagent | 签约银行代发服务 | bpchar | 1 |  | √ | '0' | 签约银行代发服务 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_accountbanks_a |  | fid |

---

## 银行账户-多语言表 t_bd_accountbanks_l

- **表名称：** 银行账户-多语言表
- **表名：** t_bd_accountbanks_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctname | 账户名称 | varchar | 255 |  | √ | ' ' | 账户名称 |
| 3 | fname | 账户简称 | varchar | 255 |  | √ | ' ' | 账户简称 |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fclosereason | 销户原因 | varchar | 255 |  | √ | ' ' | 销户原因 |
| 6 | fnoopenbeireason | 不开通银企原因 | varchar | 512 |  | √ | ' ' | 不开通银企原因 |
| 7 | fnoopenlinereason | 不开通网银原因 | varchar | 512 |  | √ | ' ' | 不开通网银原因 |
| 8 | fauthorizeinfo | 印鉴授权信息 | varchar | 512 |  | √ | ' ' | 印鉴授权信息 |
| 9 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 10 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accountbanks_l_pkey |  | fpkid |
| 2 | idx_t_bd_accountbanks_l_fid |  | flocaleid,fid |

---

## 银行账户-使用范围位图表 t_bd_accountbanks_m

- **表名称：** 银行账户-使用范围位图表
- **表名：** t_bd_accountbanks_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_accountbanks_m |  | forgid |

---

## 银行账户-使用范围表 t_bd_accountbanks_u

- **表名称：** 银行账户-使用范围表
- **表名：** t_bd_accountbanks_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accountbanks_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_bd_accountbanks_u_uo |  | fuseorgid |

---

## 关联子实体-子表 t_bd_accountbanks_lk

- **表名称：** 关联子实体-子表
- **表名：** t_bd_accountbanks_lk

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
| 1 | t_bd_accountbanks_lk_pkey |  | fpkid |
| 2 | idx_t_bd_acctbanks_lk_fid |  | fid |

---

## 币别范围-多选基础资料表 t_bd_accountbanks_cur

- **表名称：** 币别范围-多选基础资料表
- **表名：** t_bd_accountbanks_cur

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_accountbanks_cur |  | fpkid |
| 2 | idx_t_bd_accountbanks_cur_fid |  | fid |
