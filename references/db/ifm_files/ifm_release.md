# 内部定期存款解活处理-ifm_release

## 关联子实体-子表 t_cim_release_lk

- **表名称：** 关联子实体-子表
- **表名：** t_cim_release_lk

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
| 1 | idx_cim_release_lk_fk |  | fid |
| 2 | pk_cim_release_lk |  | fpkid |

---

## 内部定期存款解活处理-主表 t_cim_release

- **表名称：** 内部定期存款解活处理-主表
- **表名：** t_cim_release

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbankcheckflag | 对账标识码 | varchar | 80 |  | √ | ' ' | 对账标识码 |
| 3 | forgid | 存款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fisrevenue | 支付收益 | bpchar | 1 |  | √ | ' ' | 支付收益 |
| 5 | fdemandrate | 活期利率（%） | numeric | 23 | 10 | √ | 0 | 活期利率（%） |
| 6 | ftotalamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 7 | fsrcdepositid | 源解活单ID | int8 | 64 |  | √ | 0 | 源解活单ID |
| 8 | ffinbillnoid | 内部定期存款编号 | int8 | 64 |  | √ | 0 | 存款处理F7 cim_deposit_f7 |
| 9 | famount | 解活金额 | numeric | 23 | 10 | √ | 0 | 解活金额 |
| 10 | frealrevenue | 实际收益 | numeric | 23 | 10 | √ | 0 | 实际收益 |
| 11 | finvestvarietiesid | 存款产品 | int8 | 64 |  | √ | 0 | [投资品种 cim_investvarieties](../fbd_files/cim_investvarieties.md) |
| 12 | fsurplusamount | 可解活金额 | numeric | 23 | 10 | √ | 0 | 可解活金额 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fbebankstatus | 直联提交状态 | varchar | 50 |  | √ | ' ' | 直联提交状态,枚举: OS :银企处理中 BP :银行处理中 TS :交易成功 TF :交易失败 NC :交易未确认 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fapplyid | 解活申请 | int8 | 64 |  | √ | 0 | 存款申请F7 cim_deposit_apply_f7 |
| 17 | freleasetype | 解活类型 | varchar | 50 |  | √ | ' ' | 解活类型,枚举: expire :到期解活 inadvance :提前解活 |
| 18 | fredeemdate | 解活日期 | timestamp | 0 |  |  | null | 解活日期 |
| 19 | fredepositamount | 存款续存金额 | numeric | 23 | 10 | √ | 0 | 存款续存金额 |
| 20 | faccountdate | 到账日期 | timestamp | 0 |  |  | null | 到账日期 |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | flastredeemdate | 上次解活时间 | timestamp | 0 |  |  | null | 上次解活时间 |
| 23 | ffinaccount | 收款账户(文本) | varchar | 50 |  | √ | ' ' | 收款账户(文本) |
| 24 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: cim_deposit :定期存款处理 cim_deposit_apply :存款业务申请 ifm_deposit :内部定期存款处理 ifm_notice_deposit :内部通知存款处理 |
| 27 | frecbillno | 收款单编号 | varchar | 50 |  | √ | ' ' | 收款单编号 |
| 28 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fsubmittime | 提交日期 | timestamp | 0 |  |  | null | 提交日期 |
| 31 | fpredictinstamt | 测算收益 | numeric | 23 | 10 | √ | 0 | 测算收益 |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | freturnmsg | 银行返回信息 | varchar | 255 |  | √ | ' ' | 银行返回信息 |
| 34 | fdealbillno | 受理单编号 | varchar | 80 |  | √ | ' ' | 受理单编号 |
| 35 | fisresubmit | 是否失败重提 | bpchar | 1 |  | √ | '0' | 是否失败重提 |
| 36 | ffinaccountid | 收款账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 37 | fproductid | 存款产品 | int8 | 64 |  | √ | 0 | [存贷款产品维护 ifm_ldproduct](../ifm_files/ifm_ldproduct.md) |
| 38 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 39 | ftradechannel | 交易渠道 | varchar | 50 |  | √ | ' ' | 交易渠道,枚举: offline :线下处理 online :银企直联 |
| 40 | fexpireredeposit | 到期续存 | varchar | 50 |  | √ | ' ' | 到期续存,枚举: noredeposit :不续存 principalredeposit :本金续存 principalintredeposit :本息续存 |
| 41 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | finterestrate | 存款利率（%） | numeric | 23 | 10 | √ | 0 | 存款利率（%） |
| 43 | fidentification | fidentification | varchar | 50 |  | √ | ' ' |  |
| 44 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fnoticetype | 通知类型 | varchar | 50 |  | √ | ' ' | 通知类型,枚举: 01 :一天通知 07 :七天通知 00 :其他 |
| 46 | ffinorginfoid | 存款机构 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cimrelease_finbillno |  | ffinbillnoid |
| 2 | pk_t_cim_release |  | fid |

---

## 内部定期存款解活处理-多语言表 t_cim_release_l

- **表名称：** 内部定期存款解活处理-多语言表
- **表名：** t_cim_release_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cim_release_l |  | fpkid |
| 2 | idx_cimreleasel_fid |  | fid |

---

## 内部定期存款解活处理-关联追踪表 t_cim_release_tc

- **表名称：** 内部定期存款解活处理-关联追踪表
- **表名：** t_cim_release_tc

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
| 1 | idx_cim_release_tc_tbill |  | ftbillid |
| 2 | idx_cim_release_tc_tid |  | ftid |
| 3 | pk_cim_release_tc |  | fid |

---

## 单据体-子表 t_cim_releaseentry

- **表名称：** 单据体-子表
- **表名：** t_cim_releaseentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | festartdate | 收益计算开始日 | timestamp | 0 |  |  | null | 收益计算开始日 |
| 3 | fefinamount | 存款金额 | numeric | 19 | 6 | √ | 0 | 存款金额 |
| 4 | ferevenueamount | 预计收益金额 | numeric | 19 | 6 | √ | 0 | 预计收益金额 |
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
| 1 | idx_cimreleaseentry_fid |  | fid |
| 2 | pk_t_cim_releaseentry |  | fentryid |

---

## 内部定期存款解活处理-反写记录表 t_cim_release_wb

- **表名称：** 内部定期存款解活处理-反写记录表
- **表名：** t_cim_release_wb

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
| 1 | pk_cim_release_wb |  | fentryid |
| 2 | idx_cim_release_wb_fk |  | fid |
