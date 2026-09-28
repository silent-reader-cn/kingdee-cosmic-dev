# 开户申请-am_accopenbill

## 币别-多选基础资料表 t_am_acctopenbill_cur

- **表名称：** 币别-多选基础资料表
- **表名：** t_am_acctopenbill_cur

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_am_acctopenbill_cur |  | fpkid |

---

## 开户申请-关联追踪表 t_am_accopenbill_tc

- **表名称：** 开户申请-关联追踪表
- **表名：** t_am_accopenbill_tc

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
| 1 | idx_am_accopenbill_tc_tbill |  | ftbillid |
| 2 | idx_am_accopenbill_tc_tid |  | ftid |
| 3 | t_am_accopenbill_tc_pkey |  | fid |

---

## 关联子实体-子表 t_am_accopenbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_am_accopenbill_lk

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
| 1 | idx_t_am_accopenbill_lk_fid |  | fid |
| 2 | t_am_accopenbill_lk_pkey |  | fpkid |

---

## 开户申请-主表 t_am_accopenbill

- **表名称：** 开户申请-主表
- **表名：** t_am_accopenbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | forgid | 组织（不用） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fauthorizeinfo | fauthorizeinfo | varchar | 255 |  | √ | ' ' |  |
| 5 | fapplytime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 汇率 |
| 8 | facctstyle | 账户类型 | varchar | 80 |  | √ | ' ' | 账户类型,枚举: basic :基本存款账户 normal :一般存款账户 temp :临时存款账户 spcl :专用存款账户 fgn_curr :经常项目外汇账户 fng_fin :资本项目外汇账户 |
| 9 | fbankinterface | 银企接口 | varchar | 80 |  | √ | ' ' | 银企接口,枚举: |
| 10 | fisdefaultpay | 默认付款户 | bpchar | 1 |  | √ | ' ' | 默认付款户 |
| 11 | ffinancialchapter | 财务专用章名称 | varchar | 80 |  | √ | ' ' | 财务专用章名称 |
| 12 | fbankfunc | 网上银行功能 | varchar | 80 |  | √ | ' ' | 网上银行功能,枚举: query :查询 trans :转账 invest :投资理财 ecd :电票 |
| 13 | fclosedatef | 预计销户日期 | timestamp | 0 |  |  | null | 预计销户日期 |
| 14 | faccttype | 账户性质 | varchar | 80 |  | √ | ' ' | 账户性质,枚举: in_out :收支户 in :收入户 out :支出户 |
| 15 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 16 | facctname | facctname | varchar | 80 |  | √ | ' ' |  |
| 17 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 18 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :开户审批中 C :完成 H :开户处理中 R :开户复核中 I :审核中 G :已生成 E :退单 |
| 19 | fbacktime | fbacktime | timestamp | 0 |  |  | null |  |
| 20 | ffcommonseal | 公章名称 | varchar | 80 |  | √ | ' ' | 公章名称 |
| 21 | fnoopenlinereason | fnoopenlinereason | varchar | 500 |  | √ | ' ' |  |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | facctpropertyid | 账户用途 | int8 | 64 |  | √ | 0 | 账户用途 bd_acctpurpose |
| 24 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 25 | freason | freason | varchar | 255 |  | √ | ' ' |  |
| 26 | facctstatus | 账户状态 | varchar | 80 |  | √ | ' ' | 账户状态,枚举: normal :正常 closing :销户中 closed :已销户 |
| 27 | flegalperson | 账户法定代表人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fbankid | 开户行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | flocamt | 金额折本位币 | numeric | 19 | 6 | √ | 0.000000 | 金额折本位币 |
| 31 | fcompanyid | 申请公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | fismulcurrency | fismulcurrency | bpchar | 1 |  | √ | ' ' |  |
| 33 | fdefaultcurrencyid | 默认币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 34 | famount | 金额 | numeric | 19 | 6 | √ | 0.000000 | 金额 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 36 | fmanagecurrencyid | 账户管理费 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 37 | facctmanageamt | 账户管理费 | numeric | 19 | 6 | √ | 0.000000 | 账户管理费 |
| 38 | fbebankfunc | 银企功能 | varchar | 80 |  | √ | ' ' | 银企功能,枚举: query :查询 pay :支付 receipt :电子回单 ecd :电票 |
| 39 | fbanktype | 银行类别 | int8 | 64 |  | √ | 0 | 银行类别 bd_bankcgsetting |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fmanagerid | 账户管理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fenglishname | 账户简称（英文） | varchar | 80 |  | √ | ' ' | 账户简称（英文） |
| 43 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fstrategyid | 账户管理策略 | int8 | 64 |  | √ | 0 | 账户管理策略 am_strategy |
| 46 | fnoopenbeireason | fnoopenbeireason | varchar | 500 |  | √ | ' ' |  |
| 47 | fissetbankinterface | 开通银企接口 | bpchar | 1 |  | √ | ' ' | 开通银企接口 |
| 48 | fshortnumber | 助记码 | varchar | 80 |  | √ | ' ' | 助记码 |
| 49 | fbankaccountnumber | 银行账号 | varchar | 80 |  | √ | ' ' | 银行账号 |
| 50 | fopendate | 开户日期 | timestamp | 0 |  |  | null | 开户日期 |
| 51 | ffinorgtype | 金融机构类别 | varchar | 80 |  | √ | ' ' | 金融机构类别,枚举: 0 :银行 1 :结算中心 3 :财务公司 4 :第三方支付机构 2 :非银行金融机构 |
| 52 | fbackreason | 退单意见 | varchar | 500 |  | √ | ' ' | 退单意见 |
| 53 | fapplierid | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 54 | fbasecurrencyid | fbasecurrencyid | int8 | 64 |  | √ | 0 |  |
| 55 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 56 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 57 | fisopenbank | 开通网上银行 | bpchar | 1 |  | √ | ' ' | 开通网上银行 |
| 58 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 59 | fisdefaultrec | 默认收款户 | bpchar | 1 |  | √ | ' ' | 默认收款户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_am_openbill_num |  | fbillno |
| 2 | t_am_accopenbill_pkey |  | fid |

---

## 开户申请-反写记录表 t_am_accopenbill_wb

- **表名称：** 开户申请-反写记录表
- **表名：** t_am_accopenbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
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
| 1 | t_am_accopenbill_wb_pkey |  | fentryid |
| 2 | idx_t_am_accopenbill_wb_fid |  | fid |

---

## 开户申请-多语言表 t_am_accopenbill_l

- **表名称：** 开户申请-多语言表
- **表名：** t_am_accopenbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctname | 账户简称 | varchar | 80 |  | √ | ' ' | 账户简称 |
| 3 | fname | 账户名称 | varchar | 80 |  | √ | ' ' | 账户名称 |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fnoopenbeireason | 不开通银企原因 | varchar | 500 |  | √ | ' ' | 不开通银企原因 |
| 6 | fnoopenlinereason | 不开通网银原因 | varchar | 500 |  | √ | ' ' | 不开通网银原因 |
| 7 | fauthorizeinfo | 印鉴授权信息 | varchar | 255 |  | √ | ' ' | 印鉴授权信息 |
| 8 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | freason | 开户原因及其它要求 | varchar | 255 |  | √ | ' ' | 开户原因及其它要求 |
| 11 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_am_accopenbill_l_pkey |  | fpkid |
| 2 | idx_am_accopenbill_l_fid |  | fid,flocaleid |
