# 内部通知存款-ifm_notice_deposit

## 内部通知存款-多语言表 t_cim_deposit_l

- **表名称：** 内部通知存款-多语言表
- **表名：** t_cim_deposit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |
| 5 | fexplain | 说明 | varchar | 255 |  | √ | ' ' | 说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cimdepositl_fid |  | fid |
| 2 | pk_t_cim_deposit_l |  | fpkid |

---

## 内部通知存款-分表 t_cim_deposit_e

- **表名称：** 内部通知存款-分表
- **表名：** t_cim_deposit_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbankcheckflag | 对账标识码 | varchar | 80 |  | √ | ' ' | 对账标识码 |
| 3 | fproductid | 存款产品 | int8 | 64 |  | √ | 0 | 存贷款产品维护 ifm_ldproduct |
| 4 | fdeadline | 期限 | varchar | 50 |  | √ | ' ' | 期限,枚举: 1 :一个月 3 :三个月 6 :六个月 12 :一年 24 :两年 36 :三年 60 :五年 |
| 5 | fnotifyid | 银企通知编号 | varchar | 80 |  | √ | ' ' | 银企通知编号 |
| 6 | fdealbillno | 受理单编号 | varchar | 80 |  | √ | ' ' | 受理单编号 |
| 7 | freqnbr | 银企流程实例号 | varchar | 80 |  | √ | ' ' | 银企流程实例号 |
| 8 | fplanamount | 测算未来收益 | numeric | 23 | 10 | √ | 0 | 测算未来收益 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cim_deposit_e |  | fdeadline |
| 2 | pk_t_cim_deposit_e |  | fid |

---

## 日历-多选基础资料表 t_cim_finsubscribe_wd

- **表名称：** 日历-多选基础资料表
- **表名：** t_cim_finsubscribe_wd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 工作日历 tbd_workcalendar |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cim_finsubscribe_wd |  | fid |
| 2 | pk_t_cim_finsubscribe_wd |  | fpkid |

---

## 关联子实体-子表 t_cim_deposit_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cim_deposit_lk

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
| 1 | pk_cim_deposit_lk |  | fpkid |
| 2 | idx_cim_deposit_lk_fk |  | fid |

---

## 内部通知存款-主表 t_cim_deposit

- **表名称：** 内部通知存款-主表
- **表名：** t_cim_deposit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterm | 期限（ymd） | varchar | 50 |  | √ | ' ' | 期限（ymd） |
| 3 | forgid | 存款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | ftotalamount | 总收益金额 | numeric | 23 | 10 | √ | 0 | 总收益金额 |
| 5 | fredeemamount | 已解活金额 | numeric | 23 | 10 | √ | 0 | 已解活金额 |
| 6 | fprenoticeday | 提前通知天数 | varchar | 50 |  | √ | ' ' | 提前通知天数,枚举: 01 :一天 07 :七天 00 :其他 |
| 7 | finvestvarietiesid | 存款产品 | int8 | 64 |  | √ | 0 | 投资品种 cim_investvarieties |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fapplyid | 存款申请 | int8 | 64 |  | √ | 0 | 存款申请F7 cim_deposit_apply_f7 |
| 10 | fratefloatpoint | 利率浮动基点 | numeric | 23 | 10 | √ | 0 | 利率浮动基点 |
| 11 | fintdate | 起息日期 | timestamp | 0 |  |  | null | 起息日期 |
| 12 | fisredepositgenerate | 续存生成 | bpchar | 1 |  | √ | '0' | 续存生成 |
| 13 | fsrcdepositno | 源定期存款单 | varchar | 50 |  | √ | ' ' | 源定期存款单 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | ffinaccount | 存款账户 | varchar | 50 |  | √ | ' ' | 存款账户 |
| 16 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: cim_deposit_apply :存款业务申请 |
| 17 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fproductfactoryid | 存款模型 | int8 | 64 |  | √ | 0 | 投资模型 cim_investmodel |
| 19 | fsubmittime | 提交日期 | timestamp | 0 |  |  | null | 提交日期 |
| 20 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 21 | freturnmsg | 银行返回信息 | varchar | 255 |  | √ | ' ' | 银行返回信息 |
| 22 | frateadjuststyle | 利率重置方式 | varchar | 50 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期调整 cycle :周期性调整 hand :手工调整 noadjust :不调整 |
| 23 | ffinaccountid | 定期账户F7 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 24 | fbasis | 计息基准 | varchar | 50 |  | √ | ' ' | 计息基准,枚举: Actual_actual :Actual/actual SIA_30_360 :30/360(SIA) Actual_360 :Actual/360 Actual_365 :Acutal/365 BMA_30_360 :30/360(BMA) ISDA_30_360 :30/360(ISDA) European_30_360 :30/360(European) Japanese_Actual_365 :Acutal/365(Japanese) ICMA_Actual_actual :Actual/actual(ICMA) ICMA_Actual_360 :Actual/360(ICMA) ICMA_Actual_365 :Acutal/365(ICMA) ICMA_30_360 :30/360E(ICMA) ISDA_Actual_365 :Actual/365(ISDA) BUS_252 :BUS/252 |
| 25 | fendpreinstdate | 上次预提结束日 | timestamp | 0 |  |  | null | 上次预提结束日 |
| 26 | fexpireredeposit | 到期续存 | varchar | 50 |  | √ | ' ' | 到期续存,枚举: noredeposit :不续存 principalredeposit :自动本金续存 principalintredeposit :自动本息续存 |
| 27 | fidentification | fidentification | varchar | 50 |  | √ | ' ' |  |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 29 | ffinorginfoid | 存款机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 30 | finteresttype | 利率类型 | varchar | 50 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 |
| 31 | fdemandrate | 活期利率（%） | numeric | 23 | 10 | √ | 0 | 活期利率（%） |
| 32 | fsrcdepositid | 源存款单ID | int8 | 64 |  | √ | 0 | 源存款单ID |
| 33 | fbizstatus | 存款业务状态 | varchar | 50 |  | √ | ' ' | 存款业务状态,枚举: subscribe_ing :存款中 subscribe_done :已存款 subscribe_part :部分解活 subscribe_end :已解活 |
| 34 | famount | 存款金额 | numeric | 23 | 10 | √ | 0 | 存款金额 |
| 35 | fsurplusamount | 剩余金额 | numeric | 23 | 10 | √ | 0 | 剩余金额 |
| 36 | fbebankstatus | 直联提交状态 | varchar | 50 |  | √ | ' ' | 直联提交状态,枚举: OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 38 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 39 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 40 | freferencerate | 参考利率 | int8 | 64 |  | √ | 0 | 参考利率 tbd_referrate |
| 41 | flastredeemdate | 上次解活时间 | timestamp | 0 |  |  | null | 上次解活时间 |
| 42 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fsettleaccountid | 活期账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 46 | fisresubmit | 是否失败重提 | bpchar | 1 |  | √ | ' ' | 是否失败重提 |
| 47 | fisredeposit | fisredeposit | bpchar | 1 |  | √ | ' ' |  |
| 48 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 49 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 50 | ftradechannel | 交易渠道 | varchar | 50 |  | √ | ' ' | 交易渠道,枚举: offline :线下处理 online :银企直联 |
| 51 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 52 | finterestrate | 存款利率（%） | numeric | 23 | 10 | √ | 0 | 存款利率（%） |
| 53 | fratesign | 利率浮动基点（BP） | varchar | 50 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 54 | fexplain | 说明 | varchar | 255 |  | √ | ' ' | 说明 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cimdeposit_fbillno |  | fbillno |
| 2 | pk_t_cim_deposit |  | fid |

---

## 内部通知存款-反写记录表 t_cim_deposit_wb

- **表名称：** 内部通知存款-反写记录表
- **表名：** t_cim_deposit_wb

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
| 1 | idx_cim_deposit_wb_fk |  | fid |
| 2 | pk_cim_deposit_wb |  | fentryid |

---

## 内部通知存款-关联追踪表 t_cim_deposit_tc

- **表名称：** 内部通知存款-关联追踪表
- **表名：** t_cim_deposit_tc

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
| 1 | pk_cim_deposit_tc |  | fid |
| 2 | idx_cim_deposit_tc_tbill |  | ftbillid |
| 3 | idx_cim_deposit_tc_tid |  | ftid |
