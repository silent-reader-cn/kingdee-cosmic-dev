# 内部账户管理-ifm_inneracct

## 内部账户管理-分表 t_ifm_inneracct_e

- **表名称：** 内部账户管理-分表
- **表名：** t_ifm_inneracct_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | feasid | 集成来源标识 | varchar | 100 |  | √ | ' ' | 集成来源标识 |
| 3 | fchangedate | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 4 | fchangeuser | 变更人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_inneracct_e |  | fid |

---

## 内部账户管理-多语言表 t_ifm_inneracct_l

- **表名称：** 内部账户管理-多语言表
- **表名：** t_ifm_inneracct_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 3 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fclosereason | 销户原因 | varchar | 255 |  | √ | ' ' | 销户原因 |
| 5 | fopenreason | 开户原因 | varchar | 255 |  | √ | ' ' | 开户原因 |
| 6 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 7 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ifm_inneracct_l_fid |  | fid,flocaleid |
| 2 | t_ifm_inneracct_l_pkey |  | fpkid |

---

## 内部账户管理-主表 t_ifm_inneracct

- **表名称：** 内部账户管理-主表
- **表名：** t_ifm_inneracct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | 开户组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fcenteracctdlftid | 默认中心账号 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 4 | fopenreason | 开户原因 | varchar | 255 |  | √ | ' ' | 开户原因 |
| 5 | forgid | 结算中心组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fagreement | 协定 | bpchar | 1 |  | √ | '0' | 协定 |
| 7 | fclosedate | 销户日期 | timestamp | 0 |  |  | null | 销户日期 |
| 8 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 9 | fcurrencymgrfee | 账户管理费币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fbeifunc | 银企功能 | varchar | 80 |  | √ | ' ' | 银企功能,枚举: query :查询 pay :支付 receipt :电子回单 ecd :电票 |
| 12 | fisdefaultpay | 默认付款户 | bpchar | 1 |  | √ | '0' | 默认付款户 |
| 13 | fsettlementtype | 限定结算方式 | int8 | 64 |  | √ | 0 | 结算方式 bd_settlementtype |
| 14 | fenablerid | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | faccttype | 账户类型 | varchar | 30 |  | √ | ' ' | 账户类型,枚举: basic :基本存款账户 normal :一般存款账户 temp :临时存款账户 spcl :专用存款账户 fgn_curr :经常项目外汇账户 fng_fin :资本项目外汇账户 |
| 16 | fauthquerpt | 授权查询银行回单 | bpchar | 1 |  | √ | '1' | 授权查询银行回单 |
| 17 | fcurrencydfltid | 默认币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fname | 账户名称 | varchar | 100 |  | √ | ' ' | 账户名称 |
| 19 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fmgrstratgid | 账户管理策略 | int8 | 64 |  | √ | 0 | 账户管理策略 am_strategy |
| 21 | facctstatus | 账户状态 | varchar | 30 |  | √ | ' ' | 账户状态,枚举: normal :正常 changing :变更中 closing :销户中 closed :已销户 frozen :冻结 |
| 22 | fclosereason | 销户原因 | varchar | 255 |  | √ | ' ' | 销户原因 |
| 23 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | facctuseageid | 账户用途 | int8 | 64 |  | √ | 0 | 账户用途 bd_acctpurpose |
| 25 | feasycode | 助记码 | varchar | 30 |  | √ | ' ' | 助记码 |
| 26 | finterestdate | 结息日 | timestamp | 0 |  |  | null | 结息日 |
| 27 | fendpreinstdate | 上次预提结束日 | timestamp | 0 |  |  | null | 上次预提结束日 |
| 28 | fnumber | 账号 | varchar | 80 |  | √ | ' ' | 账号 |
| 29 | fcompanyid | 成员单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fbeiinterf | 开通银企接口 | bpchar | 1 |  | √ | '0' | 开通银企接口 |
| 31 | fmgrfee | 账户管理费 | numeric | 19 | 6 | √ | 0.000000 | 账户管理费 |
| 32 | ffinorgid | 结算中心 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 33 | fonlinebank | 开通网上银行 | bpchar | 1 |  | √ | '0' | 开通网上银行 |
| 34 | fonlinebankfunc | 网上银行功能 | varchar | 80 |  | √ | ' ' | 网上银行功能,枚举: query :查询 trans :转账 invest :投资理财 ecd :电票 |
| 35 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 36 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 37 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 38 | finterest | 是否计息 | bpchar | 1 |  | √ | '0' | 是否计息 |
| 39 | fpaymodel | 支付模式 | varchar | 30 |  | √ | ' ' | 支付模式,枚举: 1 :普通支付 2 :联动支付 3 :先拨后支 |
| 40 | fisdrawobject | 已关联计息对象 | bpchar | 1 |  | √ | '0' | 已关联计息对象 |
| 41 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 42 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 43 | fenglishname | 账户名称（英文） | varchar | 80 |  | √ | ' ' | 账户名称（英文） |
| 44 | fmanagerid | 账户管理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 47 | fopendate | 开户日期 | timestamp | 0 |  |  | null | 开户日期 |
| 48 | ffinorgtype | 金融机构类别 | varchar | 30 |  | √ | ' ' | 金融机构类别,枚举: 0 :银行 1 :结算中心 3 :财务公司 4 :第三方支付机构 |
| 49 | fintereststartdate | 计息开始日期 | timestamp | 0 |  |  | null | 计息开始日期 |
| 50 | facctprop | 账户性质 | varchar | 30 |  | √ | ' ' | 账户性质,枚举: in_out :收支户 in :收入户 out :支出户 |
| 51 | fisdefaultrec | 默认收款户 | bpchar | 1 |  | √ | '0' | 默认收款户 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_ifm_inneracct_num |  | fnumber |
| 2 | t_ifm_inneracct_pkey |  | fid |

---

## 币别-多选基础资料表 t_ifm_inneracct_cr

- **表名称：** 币别-多选基础资料表
- **表名：** t_ifm_inneracct_cr

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
| 1 | t_ifm_inneracct_cr_pkey |  | fpkid |
| 2 | idx_t_ifm_inneracct_cr_fid |  | fid |

---

## 关联账户-多选基础资料表 t_ifm_inneracct_acc

- **表名称：** 关联账户-多选基础资料表
- **表名：** t_ifm_inneracct_acc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ifm_inneracct_acc |  | fpkid |
| 2 | idx_ifm_inneracct_acc_fid |  | fid |

---

## 关联子实体-子表 t_ifm_inneracct_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_inneracct_lk

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
| 1 | idx_t_ifm_inneracct_lk_fid |  | fid |
| 2 | t_ifm_inneracct_lk_pkey |  | fpkid |
