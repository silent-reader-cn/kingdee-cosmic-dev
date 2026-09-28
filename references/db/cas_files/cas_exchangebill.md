# 外币兑换单-cas_exchangebill

## 外币兑换单-关联追踪表 t_cas_exchangebill_tc

- **表名称：** 外币兑换单-关联追踪表
- **表名：** t_cas_exchangebill_tc

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
| 1 | idx_cas_exchangebill_tc_tbill |  | ftbillid |
| 2 | idx_cas_exchangebill_tc_tid |  | ftid |
| 3 | t_cas_exchangebill_tc_pkey |  | fid |

---

## 外币兑换单-主表 t_cas_exchangebill

- **表名称：** 外币兑换单-主表
- **表名：** t_cas_exchangebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fbuybankcheckflag | 买入对账标识码 | varchar | 255 |  | √ | ' ' | 买入对账标识码 |
| 4 | facttradedate | 实际交易日期 | timestamp | 0 |  |  | null | 实际交易日期 |
| 5 | fsourcemigratedata | 迁移数据来源 | varchar | 80 |  | √ | ' ' | 迁移数据来源,枚举: XKQYB :星空企业版 |
| 6 | fcommissioncurrencyid | 手续费币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 7 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fcommissionlocalamount | 手续费金额本位币 | numeric | 19 | 6 | √ | 0.000000 | 手续费金额本位币 |
| 9 | fcommissionamount | 手续费金额 | numeric | 19 | 6 | √ | 0.000000 | 手续费金额 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsalequotation | 卖出换算方式 | varchar | 30 |  | √ | '0' | 卖出换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 12 | fbuyingexchangerate | 买入本币汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 买入本币汇率 |
| 13 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 15 | fsellingexchangerate | 卖出本币汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 卖出本币汇率 |
| 16 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 F :已兑换 |
| 17 | fbuyingcurrencyid | 买入币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 18 | fvouchernum | 凭证号 | varchar | 255 |  | √ | ' ' | 凭证号 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fimagenumber | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 21 | faccounttype | 结算方式 | varchar | 30 |  | √ | ' ' | 结算方式,枚举: bd_accountbanks :银行账户 cas_accountcash :现金账户 |
| 22 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 23 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 25 | fexchangedate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 26 | fpaycommissionaccountid | 付款账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 27 | fexuserid | fexuserid | int8 | 64 |  | √ | 0 |  |
| 28 | ffeebankcheckflag | 手续费对账标识码 | varchar | 255 |  | √ | ' ' | 手续费对账标识码 |
| 29 | fbiztype | 单据类型 | varchar | 255 |  | √ | ' ' | 单据类型,枚举: exchangesettlementbill :结汇单 exchangpayebill :购汇单 exchangebill :外币兑换单 |
| 30 | fsellingcurrencyid | 卖出币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fquotation | 买入换算方式 | varchar | 30 |  | √ | '0' | 买入换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 32 | fbuyamount | 买入金额 | numeric | 19 | 6 | √ | 0.000000 | 买入金额 |
| 33 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 35 | fsellinglocalamount | 卖出金额本位币 | numeric | 19 | 6 | √ | 0.000000 | 卖出金额本位币 |
| 36 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 37 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fotherquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 39 | fexchangegainandloss | 汇兑损益 | numeric | 19 | 6 | √ | 0.000000 | 汇兑损益 |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | fsellamount | 卖出金额 | numeric | 19 | 6 | √ | 0.000000 | 卖出金额 |
| 42 | fsellingbankcheckflag | 卖出对账标识码 | varchar | 255 |  | √ | ' ' | 卖出对账标识码 |
| 43 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 44 | fcommissionexchangerate | 手续费本币汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 手续费本币汇率 |
| 45 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 46 | fbuyingaccountid | 买入账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 47 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 48 | fsellingaccountid | 卖出账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 49 | fbuyinglocalamount | 买入金额本位币 | numeric | 19 | 6 | √ | 0.000000 | 买入金额本位币 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_exb_orgdate |  | forgid,fbizdate |
| 2 | t_cas_exchangebill_pkey |  | fid |

---

## 外币兑换单-反写记录表 t_cas_exchangebill_wb

- **表名称：** 外币兑换单-反写记录表
- **表名：** t_cas_exchangebill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  |  | null |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  |  | null |  |
| 5 | fstableid | fstableid | int8 | 64 |  |  | null |  |
| 6 | fsid | fsid | int8 | 64 |  |  | null |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 |  | null |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cas_exchangebill_wb_fk |  | fid |
| 2 | t_cas_exchangebill_wb_pkey |  | fentryid |

---

## 关联子实体-子表 t_cas_exchangebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cas_exchangebill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_exchangebill_lk_pkey |  | fpkid |
| 2 | idx_cas_exchangebill_lk_fk |  | fid |
