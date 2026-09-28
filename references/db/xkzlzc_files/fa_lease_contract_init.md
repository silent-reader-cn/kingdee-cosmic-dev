# 初始化租赁合同-fa_lease_contract_init

## 付款计划-子表 t_fa_lease_pay_plan

- **表名称：** 付款计划-子表
- **表名：** t_fa_lease_pay_plan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscountdays | 折现天数 | int4 | 32 |  | √ | 0 | 折现天数 |
| 3 | frealpayamount | 实际付款金额 | numeric | 19 | 4 | √ | 0 | 实际付款金额 |
| 4 | ftaxrate | 税率(%) | numeric | 19 | 4 | √ | 0.0000 | 税率(%) |
| 5 | fdiscountdays2 | 折现天数 | int4 | 32 |  | √ | 0 | 折现天数 |
| 6 | fpresentvalue2 | 现值 | numeric | 19 | 4 | √ | 0.0000 | 现值 |
| 7 | fplanunpay | 计划未付金额 | numeric | 19 | 4 | √ | 0 | 计划未付金额 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fpushedamount | 已下推金额 | numeric | 19 | 4 | √ | 0 | 已下推金额 |
| 10 | fenddate | 受益期结束日 | timestamp | 0 |  |  | null | 受益期结束日 |
| 11 | fdiscountfactor2 | 折现系数 | numeric | 19 | 4 | √ | 0.0000 | 折现系数 |
| 12 | frealunpay | 实际未付金额 | numeric | 19 | 4 | √ | 0 | 实际未付金额 |
| 13 | fentrysrcid | 源ID | int8 | 64 |  | √ | 0 | 源ID |
| 14 | fpresentvalue | 现值 | numeric | 19 | 4 | √ | 0.0000 | 现值 |
| 15 | fdiscountfactor | 折现系数 | numeric | 19 | 6 | √ | 0.000000 | 折现系数 |
| 16 | fownerorgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 17 | fpayitemid | 付款项目 | int8 | 64 |  | √ | 0 | [付款项目 fa_payment_item](../xkzlzc_files/fa_payment_item.md) |
| 18 | frentwithtax | 计划付款金额 | numeric | 19 | 4 | √ | 0.0000 | 计划付款金额 |
| 19 | fcontractsrcid | 源合同 | int8 | 64 |  | √ | 0 | [租赁合同 fa_lease_contract](../xkzlzc_files/fa_lease_contract.md) |
| 20 | fplanstatus | 单据状态 | bpchar | 1 |  | √ | 'C' | 单据状态,枚举: A :创建 B :审核中 C :已审核 |
| 21 | fplannumber | 编码 | varchar | 50 |  |  | ' ' | 编码 |
| 22 | finvoicetype | 发票类型 | bpchar | 1 |  | √ | ' ' | 发票类型,枚举: A :专用发票 B :普通发票 |
| 23 | ftax | 税额 | numeric | 19 | 4 | √ | 0.0000 | 税额 |
| 24 | fstartdate | 受益期开始日 | timestamp | 0 |  |  | null | 受益期开始日 |
| 25 | fdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 28 | fplanpaydate | 计划付款日 | timestamp | 0 |  |  | LOCALTIMESTAMP | 计划付款日 |
| 29 | frentnotax | 不含税金额 | numeric | 19 | 4 | √ | 0.0000 | 不含税金额 |
| 30 | funpaidrent | 租金 | numeric | 19 | 4 | √ | 0.0000 | 租金 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_pay_plan_fk |  | fid |
| 2 | t_fa_lease_pay_plan_pkey |  | fentryid |

---

## 初始化租赁合同-多语言表 t_fa_lease_contract_new_l

- **表名称：** 初始化租赁合同-多语言表
- **表名：** t_fa_lease_contract_new_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 3 | fassetname | 资产名称 | varchar | 300 |  | √ | ' ' | 资产名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | '0' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_lease_contract_new_l |  | fpkid |
| 2 | idx_fa_lease_contract_new_l |  | fid,flocaleid |

---

## 关联子实体-子表 t_fa_lease_contract_new_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fa_lease_contract_new_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_contract_new_lk_fid |  | fid |
| 2 | pk_t_fa_lease_contract_new_lk |  | fpkid |

---

## 初始化租赁合同-主表 t_fa_lease_contract_new

- **表名称：** 初始化租赁合同-主表
- **表名：** t_fa_lease_contract_new

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fleaseassets | 使用权资产原值 | numeric | 19 | 4 | √ | 0.0000 | 使用权资产原值 |
| 3 | fexratetable | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 4 | fdiscountrate | 年折现率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 年折现率(%) |
| 5 | forgid | 货主组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | faccuminterest | 累计利息 | numeric | 19 | 4 | √ | 0 | 累计利息 |
| 7 | fleasetermstartdate | 租赁期开始日 | timestamp | 0 |  |  | null | 租赁期开始日 |
| 8 | fleaseliabori | 租赁负债原值 | numeric | 19 | 4 | √ | 0.0000 | 租赁负债原值 |
| 9 | fsysswitchdate | 系统切换日 | timestamp | 0 |  |  | null | 系统切换日 |
| 10 | fclearbillid | 清理单基础资料 | int8 | 64 |  | √ | 0 | [清理单基础资料 fa_clearbill_base](../fa_files/fa_clearbill_base.md) |
| 11 | finitconfirmdate | 初始确认日 | timestamp | 0 |  |  | null | 初始确认日 |
| 12 | fleasestartdate | 起租日 | timestamp | 0 |  |  | null | 起租日 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstoreplaceid | 存放地点 | int8 | 64 |  | √ | 0 | [存放地点 fa_storeplace](../fa_files/fa_storeplace.md) |
| 15 | fsrccontractid | 关联合同 | int8 | 64 |  | √ | 0 | [租赁合同 fa_lease_contract](../xkzlzc_files/fa_lease_contract.md) |
| 16 | fdailydiscountrate | 日折现率(%) | numeric | 23 | 10 | √ | 0.000000 | 日折现率(%) |
| 17 | fleaseassetsfor | 使用权资产原值（本位币） | numeric | 19 | 6 | √ | 0 | 使用权资产原值（本位币） |
| 18 | faccountapply | 适用准则 | varchar | 50 |  | √ | 'A' | 适用准则,枚举: A :中国会计准则 B :美国会计准则 |
| 19 | fexrate | 汇率 | numeric | 19 | 6 | √ | 1 | 汇率 |
| 20 | fleaseterminationdate | 租赁终止日 | timestamp | 0 |  |  | null | 租赁终止日 |
| 21 | fversion | 版本号 | varchar | 50 |  | √ | '0' | 版本号 |
| 22 | fname | 合同名称 | varchar | 100 |  | √ | ' ' | 合同名称 |
| 23 | fleaseexprule | 租赁费用按照不含税租金计算 | bpchar | 1 |  | √ | '0' | 租赁费用按照不含税租金计算 |
| 24 | fhasdepremonths | 已折旧期间（月） | int4 | 32 |  | √ | 0 | 已折旧期间（月） |
| 25 | fleaseliab | 租赁负债现值 | numeric | 19 | 4 | √ | 0.0000 | 租赁负债现值 |
| 26 | fsettlesharesrcid | 租金结算共享ID | int8 | 64 |  | √ | 0 | 租金结算共享ID |
| 27 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | [资产类别 fa_assetcategory](../fa_files/fa_assetcategory.md) |
| 28 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 29 | fbacktime | 备份时间 | timestamp | 0 |  |  | null | 备份时间 |
| 30 | fassetqty | 数量 | numeric | 19 | 4 | √ | 0.0000 | 数量 |
| 31 | fassetsaccumdepre | 使用权资产累计折旧 | numeric | 19 | 4 | √ | 0.0000 | 使用权资产累计折旧 |
| 32 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 33 | fmigsrc | 是否迁移 | int4 | 32 |  | √ | 0 | 是否迁移 |
| 34 | fleaseliaboribalance | 租赁负债原值结余 | numeric | 19 | 4 | √ | 0.0000 | 租赁负债原值结余 |
| 35 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 37 | fnumber | 合同号 | varchar | 30 |  | √ | ' ' | 合同号 |
| 38 | fdepremonths | 适用租赁期(月) | int4 | 32 |  | √ | 0 | 适用租赁期(月) |
| 39 | fassetqtycreate | 可生成数量 | int4 | 32 |  | √ | 0 | 可生成数量 |
| 40 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fleaseliabbalance | 租赁负债现值结余 | numeric | 19 | 4 | √ | 0.0000 | 租赁负债现值结余 |
| 42 | faccumrent | 累计租金 | numeric | 19 | 4 | √ | 0 | 累计租金 |
| 43 | fbizstatus | 业务状态 | bpchar | 1 |  | √ | 'A' | 业务状态,枚举: A :正常 B :已终止 C :变更 |
| 44 | faddupyearrent | 本年累计租金 | numeric | 19 | 4 | √ | 0 | 本年累计租金 |
| 45 | fisinitdata | 是否原始数据 | bpchar | 1 |  | √ | '1' | 是否原始数据 |
| 46 | fleasemonths | 租赁期(月) | int4 | 32 |  | √ | 0 | 租赁期(月) |
| 47 | fstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 48 | fcuryearleaseexp | 本年租赁费用 | numeric | 19 | 6 | √ | 0 | 本年租赁费用 |
| 49 | fassetunitid | 资产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 50 | fquotation | 换算方式 | varchar | 50 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 51 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 52 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 53 | fsourcetype | 来源类型 | bpchar | 1 |  | √ | 'A' | 来源类型,枚举: A :新增 B :初始化 C :变更备份 |
| 54 | fleaseenddate | 租赁结束日 | timestamp | 0 |  |  | null | 租赁结束日 |
| 55 | fleasetype | 租赁类型 | varchar | 50 |  | √ | 'A' | 租赁类型,枚举: A :融资租赁 B :经营租赁 |
| 56 | ffromcurr | 原币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 57 | fisexempt | 豁免 | bpchar | 1 |  | √ | '0' | 豁免 |
| 58 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 59 | fassetname | 资产名称 | varchar | 300 |  | √ | ' ' | 资产名称 |
| 60 | faddupyearinterest | 本年累计利息 | numeric | 19 | 4 | √ | 0 | 本年累计利息 |
| 61 | ffreeleasestartdate | 免租期开始日 | timestamp | 0 |  |  | null | 免租期开始日 |
| 62 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 63 | ftocurr | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 64 | fcontrsigndate | 合同签订日 | timestamp | 0 |  |  | null | 合同签订日 |
| 65 | ftransitionplan | 过渡方案 | bpchar | 1 |  | √ | ' ' | 过渡方案,枚举: A :简化追溯法1 B :简化追溯法2 C :完全追溯法 |
| 66 | fpreviousbackid | 上一次备份ID | int8 | 64 |  | √ | 0 | 上一次备份ID |
| 67 | faccleaseexp | 累计租赁费用 | numeric | 19 | 6 | √ | 0 | 累计租赁费用 |
| 68 | fisbak | 是否备份 | bpchar | 1 |  | √ | '0' | 是否备份 |
| 69 | funconfirmcharge | 未确认融资费用 | numeric | 19 | 6 | √ | 0 | 未确认融资费用 |
| 70 | fexratedate | 汇率日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 汇率日期 |
| 71 | fleaserid | 出租方 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 72 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 73 | ffreeleasemonths | 免租期(月) | int4 | 32 |  | √ | 0 | 免租期(月) |
| 74 | frenewalcontractid | 续租合同id | int8 | 64 |  | √ | 0 | 续租合同id |
| 75 | fassetsaddupyeardepre | 使用权资产本年累计折旧 | numeric | 19 | 4 | √ | 0 | 使用权资产本年累计折旧 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fa_lease_contract_new |  | fid |
| 2 | idx_fa_contract_new_orgdate |  | forgid,fleasestartdate |
| 3 | idx_fa_contract_version |  | fmasterid,fversion,fisbak |

---

## 付款规则-子表 t_fa_lease_pay_rule

- **表名称：** 付款规则-子表
- **表名：** t_fa_lease_pay_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffrequency | 频率 | bpchar | 1 |  | √ | ' ' | 频率,枚举: A :每月 B :每两个月 C :每三个月 D :每六个月 E :每十二个月 F :一次性 |
| 3 | frelativepaydate | 第几天支付 | int4 | 32 |  | √ | 0 | 第几天支付 |
| 4 | fentrysrcid | 源ID | int8 | 64 |  | √ | 0 | 源ID |
| 5 | ftaxrate | 税率(%) | numeric | 19 | 4 | √ | 0.0000 | 税率(%) |
| 6 | fpayitemid | 付款项目 | int8 | 64 |  | √ | 0 | [付款项目 fa_payment_item](../xkzlzc_files/fa_payment_item.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | famount | 含税金额 | numeric | 19 | 4 | √ | 0.0000 | 含税金额 |
| 9 | fenddate | 受益期_止 | timestamp | 0 |  |  | null | 受益期_止 |
| 10 | fpaypoint | 支付起点(功能不全，勿用) | bpchar | 1 |  | √ | 'A' | 支付起点(功能不全，勿用),枚举: A :期初 B :期末 |
| 11 | finvoicetype | 发票类型 | bpchar | 1 |  | √ | ' ' | 发票类型,枚举: A :专用发票 B :普通发票 |
| 12 | fstartdate | 受益期_起 | timestamp | 0 |  |  | null | 受益期_起 |
| 13 | ftax | 税额 | numeric | 19 | 4 | √ | 0.0000 | 税额 |
| 14 | fdeductible | 可抵扣 | bpchar | 1 |  | √ | '0' | 可抵扣 |
| 15 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fa_pay_rule_fk |  | fid |
| 2 | pk_t_fa_lease_pay_rule |  | fentryid |
