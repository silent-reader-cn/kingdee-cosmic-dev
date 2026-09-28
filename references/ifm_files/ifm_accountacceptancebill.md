# 内部账户受理-ifm_accountacceptancebill

## 关联子实体-子表 t_ifm_accountaccept_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_accountaccept_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_accountaccept_lk_fk |  | fid |
| 2 | pk_ifm_accountaccept_lk |  | fpkid |

---

## 内部账户受理-关联追踪表 t_ifm_accountacceptance_tc

- **表名称：** 内部账户受理-关联追踪表
- **表名：** t_ifm_accountacceptance_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  |  | null |  |
| 3 | fttableid | fttableid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | ftid | ftid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_accountacceptance_tc |  | fid |
| 2 | idx_ifm_accountacceptance_tc_tid |  | ftid |
| 3 | idx_ifm_accountacceptance_tc_tbill |  | ftbillid |

---

## 内部账户受理-主表 t_ifm_accountaccept

- **表名称：** 内部账户受理-主表
- **表名：** t_ifm_accountaccept

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fdefaultcurrencyid | 默认币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 4 | fopenreason | fopenreason | varchar | 255 |  | √ | ' ' |  |
| 5 | fagreement | 协定 | bpchar | 1 |  | √ | '0' | 协定 |
| 6 | fclosedate | 销户日期 | timestamp | 0 |  |  | null | 销户日期 |
| 7 | fbusinesstype | 业务类型 | varchar | 30 |  | √ | ' ' | 业务类型,枚举: A :开户 B :销户 C :变更 |
| 8 | fapplytime | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | facctstyle | 账户类型 | varchar | 80 |  | √ | ' ' | 账户类型,枚举: basic :基本存款账户 normal :一般存款账户 temp :临时存款账户 spcl :专用存款账户 fgn_curr :经常项目外汇账户 fng_fin :资本项目外汇账户 |
| 12 | finterest | 计息 | bpchar | 1 |  | √ | '0' | 计息 |
| 13 | fmanagecurrencyid | 账户管理费 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 14 | fapplier | 申请人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbankinterface | fbankinterface | varchar | 80 |  | √ | ' ' |  |
| 16 | fpaymodel | 支付模式 | varchar | 30 |  | √ | ' ' | 支付模式,枚举: 1 :普通支付 2 :联动支付 3 :先拨后支 |
| 17 | fisdefaultpay | 默认付款户 | bpchar | 1 |  | √ | '0' | 默认付款户 |
| 18 | fsettlementtype | 限定结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 19 | facctmanageamt | 账户管理费 | numeric | 19 | 6 | √ | 0.000000 | 账户管理费 |
| 20 | fbusinessstatus | 业务状态 | varchar | 30 |  | √ | ' ' | 业务状态,枚举: A :待受理 B :已受理 C :已退单 |
| 21 | faccttype | 账户性质 | varchar | 80 |  | √ | ' ' | 账户性质,枚举: in_out :收支户 in :收入户 out :支出户 |
| 22 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | facctname | facctname | varchar | 100 |  | √ | ' ' |  |
| 25 | fsourcebilltype | fsourcebilltype | varchar | 30 |  | √ | ' ' |  |
| 26 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 27 | fmanagerid | 账户管理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fenglishname | 账户名称（英文） | varchar | 80 |  | √ | ' ' | 账户名称（英文） |
| 29 | fcomment | fcomment | varchar | 255 |  | √ | ' ' |  |
| 30 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 31 | fstrategyid | 账户管理策略 | int8 | 64 |  | √ | 0 | 账户管理策略 am_strategy |
| 32 | fshortnumber | 助记码 | varchar | 80 |  | √ | ' ' | 助记码 |
| 33 | fissetbankinterface | 开通银企接口 | bpchar | 1 |  | √ | '0' | 开通银企接口 |
| 34 | fbankaccountnumber | 账号 | varchar | 80 |  | √ | ' ' | 账号 |
| 35 | fopendate | 开户日期 | timestamp | 0 |  |  | null | 开户日期 |
| 36 | ffinorgtype | 金融机构类别 | varchar | 80 |  | √ | ' ' | 金融机构类别,枚举: 0 :银行 1 :结算中心 3 :财务公司 4 :第三方支付机构 |
| 37 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 38 | facctpropertyid | 账户用途 | int8 | 64 |  | √ | 0 | 账户用途 bd_acctpurpose |
| 39 | fscorgid | 结算中心组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fbackreason | 退单意见 | varchar | 500 |  | √ | ' ' | 退单意见 |
| 41 | fclosereason | fclosereason | varchar | 255 |  | √ | ' ' |  |
| 42 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 43 | fisopenbank | 开通网上银行 | bpchar | 1 |  | √ | '0' | 开通网上银行 |
| 44 | fbankid | 开户行 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 45 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fisdefaultrec | 默认收款户 | bpchar | 1 |  | √ | '0' | 默认收款户 |
| 47 | faccountbankid | 账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 48 | fcompanyid | 申请公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_accountaccept |  | fid |
| 2 | idx_ifm_accacc_fscorgid |  | fscorgid |

---

## 单据体-子表 t_ifm_acceptmodifyentry

- **表名称：** 单据体-子表
- **表名：** t_ifm_acceptmodifyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fchangefieldname | 变更属性名称 | varchar | 255 |  | √ | ' ' | 变更属性名称 |
| 3 | fbeforechangename | 变更前 | varchar | 255 |  | √ | ' ' | 变更前 |
| 4 | fbasedataid | 多类别基础资料 | varchar | 255 |  | √ | ' ' | 业务单元 bos_org |
| 5 | fafterchangename | 变更后 | varchar | 255 |  | √ | ' ' | 变更后 |
| 6 | fbeforechange | 变更前 | varchar | 255 |  | √ | ' ' | 变更前 |
| 7 | fbasedatatype | 基础资料类型 | varchar | 255 |  | √ | ' ' | 基础资料类型,枚举: bos_org :业务单元 bd_finorginfo :合作金融机构 bd_acctpurpose :账户用途 bos_user :人员 bd_currency :币别 am_strategy :账户管理策略 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | freason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 10 | fchangefield | 变更属性 | varchar | 50 |  | √ | ' ' | 变更属性,枚举: |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | fafterchange | 变更后 | varchar | 255 |  | √ | ' ' | 变更后 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_acceptmodifyentry |  | fentryid |
| 2 | idx_ifmacctacceptmodify_fid |  | fid |

---

## 内部账户受理-多语言表 t_ifm_accountaccept_l

- **表名称：** 内部账户受理-多语言表
- **表名：** t_ifm_accountaccept_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | facctname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 3 | fclosereason | 销户原因及其它销户要求 | varchar | 255 |  | √ | ' ' | 销户原因及其它销户要求 |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fopenreason | 开户原因及其它开户要求 | varchar | 255 |  | √ | ' ' | 开户原因及其它开户要求 |
| 6 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 7 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_accountaccept_l |  | fpkid |
| 2 | idx_ifm_accountaccept_l_fid |  | fid |

---

## 币别-多选基础资料表 t_ifm_acceptmodify_cur

- **表名称：** 币别-多选基础资料表
- **表名：** t_ifm_acceptmodify_cur

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_acctacceptmodcur_fentryid |  | fentryid |
| 2 | pk_t_ifm_acceptmodify_cur |  | fpkid |

---

## 内部账户受理-反写记录表 t_ifm_accountacceptance_wb

- **表名称：** 内部账户受理-反写记录表
- **表名：** t_ifm_accountacceptance_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ifm_accountacceptance_wb_fk |  | fid |
| 2 | pk_ifm_accountacceptance_wb |  | fentryid |

---

## 币别-多选基础资料表 t_ifm_accountaccept_cur

- **表名称：** 币别-多选基础资料表
- **表名：** t_ifm_accountaccept_cur

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
| 1 | idx_ifm_accountaccept_cur_fid |  | fid |
| 2 | pk_ifm_accountaccept_cur |  | fpkid |

---

## 限定结算方式-多选基础资料表 t_ifm_acceptmodify_st

- **表名称：** 限定结算方式-多选基础资料表
- **表名：** t_ifm_acceptmodify_st

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_acceptmodify_st |  | fpkid |
| 2 | idx_acctacceptmodst_fentryid |  | fentryid |
