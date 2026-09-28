# 内部存款受理-ifm_bizdealbill_deposit

## 关联子实体-子表 t_ifm_bizdealbill_deposit_lk

- **表名称：** 关联子实体-子表
- **表名：** t_ifm_bizdealbill_deposit_lk

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
| 1 | idx_ifm_bizdealbill_deposit_lk_fk |  | fid |
| 2 | pk_ifm_bizdealbill_deposit_lk |  | fpkid |

---

## 内部存款受理-分表 t_ifm_bizdealbill_deposit_e

- **表名称：** 内部存款受理-分表
- **表名：** t_ifm_bizdealbill_deposit_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdealdate | 受理时间 | timestamp | 0 |  |  | null | 受理时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ifm_bizdealbill_dpt_e |  | fdealdate |
| 2 | pk_ifm_bizdealbill_deposit_e |  | fid |

---

## 内部存款受理-多语言表 t_ifm_bizdealbill_deposit_l

- **表名称：** 内部存款受理-多语言表
- **表名：** t_ifm_bizdealbill_deposit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fdealopinion | 受理意见 | varchar | 255 |  | √ | ' ' | 受理意见 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_bizdealbill_deposit_l |  | fpkid |
| 2 | idx_bizdealbill_dpt_l_fid |  | fid |

---

## 内部存款受理-反写记录表 t_ifm_bizdealbill_deposit_wb

- **表名称：** 内部存款受理-反写记录表
- **表名：** t_ifm_bizdealbill_deposit_wb

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
| 1 | idx_ifm_bizdealbill_deposit_wb_fk |  | fid |
| 2 | pk_ifm_bizdealbill_deposit_wb |  | fentryid |

---

## 单据体-子表 t_ifm_bizdealbill_entry

- **表名称：** 单据体-子表
- **表名：** t_ifm_bizdealbill_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | festartdate | 收益计算开始日 | timestamp | 0 |  |  | null | 收益计算开始日 |
| 3 | fefinamount | 存款金额 | numeric | 23 |  | √ | 0 | 存款金额 |
| 4 | ferevenueamount | 预计收益金额 | numeric | 23 | 10 | √ | 0 | 预计收益金额 |
| 5 | feplanrevenue | 预计收益率 | numeric | 23 | 10 | √ | 0 | 预计收益率 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fedays | 本次收益天数 | int4 | 32 |  | √ | 0 | 本次收益天数 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | feconvertdays | 收益率转换天数 | int4 | 32 |  | √ | 0 | 收益率转换天数 |
| 10 | feenddate | 收益计算结束日 | timestamp | 0 |  |  | null | 收益计算结束日 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_bizdealbill_entry |  | fentryid |
| 2 | idx_t_ifm_bizdeal_entry_fid |  | fid |

---

## 内部存款受理-关联追踪表 t_ifm_bizdealbill_deposit_tc

- **表名称：** 内部存款受理-关联追踪表
- **表名：** t_ifm_bizdealbill_deposit_tc

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
| 1 | idx_ifm_bizdealbill_deposit_tc_tbill |  | ftbillid |
| 2 | idx_ifm_bizdealbill_deposit_tc_tid |  | ftid |
| 3 | pk_ifm_bizdealbill_deposit_tc |  | fid |

---

## 内部存款受理-主表 t_ifm_bizdealbill_deposit

- **表名称：** 内部存款受理-主表
- **表名：** t_ifm_bizdealbill_deposit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterm | 期限（ymd） | varchar | 80 |  | √ | ' ' | 期限（ymd） |
| 3 | fdealopinion | 受理意见 | varchar | 255 |  | √ | ' ' | 受理意见 |
| 4 | forgid | 存款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fisrevenue | 支付收益 | bpchar | 1 |  | √ | '0' | 支付收益 |
| 6 | ftotalamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 7 | ffinbillnoid | 存款单编号 | int8 | 64 |  | √ | 0 | 存款处理F7 cim_deposit_f7 |
| 8 | frealrevenue | 实际收益 | numeric | 23 | 10 | √ | 0 | 实际收益 |
| 9 | fprenoticeday | 提前通知天数 | varchar | 80 |  | √ | ' ' | 提前通知天数,枚举: 01 :一天 07 :七天 00 :其他 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | finvestvarietiesid | 存款产品 | int8 | 64 |  | √ | 0 | 投资品种 cim_investvarieties |
| 12 | fapplyid | 申请单编号 | int8 | 64 |  | √ | 0 | 存款申请F7 cim_deposit_apply_f7 |
| 13 | freleasetype | 解活类型 | varchar | 80 |  | √ | ' ' | 解活类型,枚举: agreeon :约定解活 temporary :非约定解活 expire :到期解活 inadvance :提前解活 |
| 14 | fdealuserid | 受理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fredeemdate | 解活日期 | timestamp | 0 |  |  | null | 解活日期 |
| 16 | fratefloatpoint | 利率浮动基点 | numeric | 23 | 10 | √ | 0 | 利率浮动基点 |
| 17 | fapplytype | 申请类型 | varchar | 80 |  | √ | ' ' | 申请类型,枚举: deposit :存款申请 release :解活申请 renew :续存申请 |
| 18 | fintdate | 起息日期 | timestamp | 0 |  |  | null | 起息日期 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | ffinaccount | 存款账户 | varchar | 80 |  | √ | ' ' | 存款账户 |
| 21 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 22 | fpredictinstamt | 测算收益 | numeric | 23 | 10 | √ | 0 | 测算收益 |
| 23 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 24 | frateadjuststyle | 利率重置方式 | varchar | 80 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期重置 cycle :周期性重置 hand :手工重置 noadjust :不重置 |
| 25 | ffinaccountid | 存款账户F7 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 26 | fdepositamt | 存款金额 | numeric | 23 | 10 | √ | 0 | 存款金额 |
| 27 | fproductid | 存款产品 | int8 | 64 |  | √ | 0 | 存贷款产品维护 ifm_ldproduct |
| 28 | fbasis | 计息基准 | varchar | 80 |  | √ | ' ' | 计息基准,枚举: Actual_actual :Actual/actual SIA_30_360 :30/360(SIA) Actual_360 :Actual/360 Actual_365 :Acutal/365 BMA_30_360 :30/360(BMA) ISDA_30_360 :30/360(ISDA) European_30_360 :30/360(European) Japanese_Actual_365 :Acutal/365(Japanese) ICMA_Actual_actual :Actual/actual(ICMA) ICMA_Actual_360 :Actual/360(ICMA) ICMA_Actual_365 :Acutal/365(ICMA) ICMA_30_360 :30/360E(ICMA) ISDA_Actual_365 :Actual/365(ISDA) BUS_252 :BUS/252 |
| 29 | fexpireredeposit | 到期续存 | varchar | 80 |  | √ | ' ' | 到期续存,枚举: noredeposit :不续存 principalredeposit :本金续存 principalintredeposit :本息续存 |
| 30 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 31 | ffinorginfoid | 存款机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 32 | finteresttype | 利率类型 | varchar | 80 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 |
| 33 | fdemandrate | 活期利率（%） | numeric | 23 | 10 | √ | 0 | 活期利率（%） |
| 34 | fbizstatus | 业务状态 | varchar | 80 |  | √ | ' ' | 业务状态,枚举: A :待受理 B :已受理 D :已退单 |
| 35 | famount | 解活金额 | numeric | 23 | 10 | √ | 0 | 解活金额 |
| 36 | fsurplusamount | 可解活金额 | numeric | 23 | 10 | √ | 0 | 可解活金额 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fapplidate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 39 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 40 | fredepositamount | 存款续存金额 | numeric | 23 | 10 | √ | 0 | 存款续存金额 |
| 41 | freferencerate | 参考利率 | int8 | 64 |  | √ | 0 | 参考利率 tbd_referrate |
| 42 | flastredeemdate | 上次解活日期 | timestamp | 0 |  |  | null | 上次解活日期 |
| 43 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 45 | fapplyorgid | 申请组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 46 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 47 | fsettleaccountid | 活期账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 48 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 49 | finterestrate | 存款利率（%） | numeric | 23 | 10 | √ | 0 | 存款利率（%） |
| 50 | fratesign | 利率浮动基点（BP） | varchar | 80 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ifm_bizdealbill_deposit |  | fid |
| 2 | idx_ifm_bizdealbill_dpt_billno |  | fbillno |
