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
| 2 | fopenorgid | 开户公司 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbuybankcheckflag | 买入对账标识码 | varchar | 255 |  | √ | ' ' | 买入对账标识码 |
| 4 | facttradedate | 实际交易日期 | timestamp | 0 |  |  | null | 实际交易日期 |
| 5 | fexchangedate | 付款日期 | timestamp | 0 |  |  | null | 付款日期 |
| 6 | fcommissioncurrencyid | 手续费币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 7 | forgid | 收付组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fcommissionlocalamount | 手续费金额本位币 | numeric | 19 | 6 | √ | 0.000000 | 手续费金额本位币 |
| 9 | fcommissionamount | 手续费金额 | numeric | 19 | 6 | √ | 0.000000 | 手续费金额 |
| 10 | fpaycommissionaccountid | 付款账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 11 | fexuserid | fexuserid | int8 | 64 |  | √ | 0 |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | ffeebankcheckflag | 手续费对账标识码 | varchar | 255 |  | √ | ' ' | 手续费对账标识码 |
| 14 | fsalequotation | 卖出换算方式 | varchar | 30 |  | √ | '0' | 卖出换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 15 | fbiztype | 单据类型 | varchar | 255 |  | √ | ' ' | 单据类型,枚举: exchangesettlementbill :结汇单 exchangpayebill :购汇单 exchangebill :外币兑换单 |
| 16 | fbuyingexchangerate | 买入本币汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 买入本币汇率 |
| 17 | fsellingcurrencyid | 卖出币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 18 | fquotation | 买入换算方式 | varchar | 30 |  | √ | '0' | 买入换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 19 | fbuyamount | 买入金额 | numeric | 19 | 6 | √ | 0.000000 | 买入金额 |
| 20 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fisarchive | 是否归档 | bpchar | 1 |  | √ | '0' | 是否归档 |
| 22 | fsellinglocalamount | 卖出金额本位币 | numeric | 19 | 6 | √ | 0.000000 | 卖出金额本位币 |
| 23 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 24 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 25 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 27 | fsellingexchangerate | 卖出本币汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 卖出本币汇率 |
| 28 | fotherquotation | 换算方式 | varchar | 30 |  | √ | '0' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 29 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 F :已兑换 |
| 30 | fexchangegainandloss | 汇兑损益 | numeric | 19 | 6 | √ | 0.000000 | 汇兑损益 |
| 31 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 32 | fbuyingcurrencyid | 买入币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 33 | fsellamount | 卖出金额 | numeric | 19 | 6 | √ | 0.000000 | 卖出金额 |
| 34 | fvouchernum | 凭证号 | varchar | 255 |  | √ | ' ' | 凭证号 |
| 35 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 36 | fsellingbankcheckflag | 卖出对账标识码 | varchar | 255 |  | √ | ' ' | 卖出对账标识码 |
| 37 | fimagenumber | 影像编号 | varchar | 50 |  | √ | ' ' | 影像编号 |
| 38 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 39 | fcommissionexchangerate | 手续费本币汇率 | numeric | 23 | 10 | √ | 0.0000000000 | 手续费本币汇率 |
| 40 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 41 | faccounttype | 结算方式 | varchar | 30 |  | √ | ' ' | 结算方式,枚举: bd_accountbanks :银行账户 cas_accountcash :现金账户 |
| 42 | fbuyingaccountid | 买入账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 43 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 44 | fisvoucher | 已生成凭证 | bpchar | 1 |  | √ | '0' | 已生成凭证 |
| 45 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 46 | fsellingaccountid | 卖出账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 47 | fbuyinglocalamount | 买入金额本位币 | numeric | 19 | 6 | √ | 0.000000 | 买入金额本位币 |
| 48 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

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
