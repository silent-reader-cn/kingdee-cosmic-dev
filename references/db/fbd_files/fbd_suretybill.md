# 保证金存入处理-fbd_suretybill

## 保证金存入处理-反写记录表 t_fbd_suretybill_wb

- **表名称：** 保证金存入处理-反写记录表
- **表名：** t_fbd_suretybill_wb

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
| 1 | pk_fbd_suretybill_wb |  | fentryid |
| 2 | idx_fbd_suretybill_wb_fk |  | fid |

---

## 保证金存入处理-主表 t_fbd_suretybill

- **表名称：** 保证金存入处理-主表
- **表名：** t_fbd_suretybill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterm | 期限（ymd） | varchar | 50 |  | √ | ' ' | 期限（ymd） |
| 3 | finteresttype | 利率类型 | varchar | 50 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 |
| 4 | forgid | 存款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | ftotalamount | 总收益金额 | numeric | 23 | 10 | √ | 0 | 总收益金额 |
| 6 | fdemandrate | 活期利率（%） | numeric | 23 | 10 | √ | 0 | 活期利率（%） |
| 7 | fbizstatus | 保证金业务状态 | varchar | 50 |  | √ | ' ' | 保证金业务状态,枚举: surety_ing :存入中 surety_done :已存入 surety_part :已部分存出 surety_end :已存出 |
| 8 | famount | 保证金金额 | numeric | 23 | 10 | √ | 0 | 保证金金额 |
| 9 | fendinstdate | 上次结息日 | timestamp | 0 |  |  | null | 上次结息日 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fsurplusamount | 剩余金额 | numeric | 23 | 10 | √ | 0 | 剩余金额 |
| 12 | finvestvarietiesid | 保证金品种 | int8 | 64 |  | √ | 0 | 保证金品种 fbd_investvariety_surety |
| 13 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fprefutureamt | 预期未来收益 | numeric | 23 | 10 | √ | 0 | 预期未来收益 |
| 16 | fapplyid | 保证金申请(预留) | int8 | 64 |  | √ | 0 | 存款申请F7 cim_deposit_apply_f7 |
| 17 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 18 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 19 | fratefloatpoint | 利率浮动基点 | numeric | 19 | 6 | √ | 0 | 利率浮动基点 |
| 20 | fintdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 21 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 22 | freleaseamount | 已存出金额 | numeric | 23 | 10 | √ | 0 | 已存出金额 |
| 23 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 24 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 26 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: fbd_surety_apply :保证金业务申请 |
| 27 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fproductfactoryid | 保证金模型 | int8 | 64 |  | √ | 0 | 保证金模型 fbd_investmodel_surety |
| 30 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 31 | fsettleaccountid | 保证金账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 32 | flastreleasedate | 上次存出日期 | timestamp | 0 |  |  | null | 上次存出日期 |
| 33 | frevenueplanid | 收益方案 | int8 | 64 |  | √ | 0 | 收益方案 cim_profitscheme |
| 34 | frateadjuststyle | 利率重置方式 | varchar | 50 |  | √ | ' ' | 利率重置方式,枚举: deadline :即期重置 |
| 35 | frevenueway | 收益方式 | varchar | 50 |  | √ | ' ' | 收益方式,枚举: stage :固定频率收益 norevenue :无收益 |
| 36 | ffinaccountid | 活期账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 37 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 38 | freferencerateid | 参考利率 | int8 | 64 |  | √ | 0 | 参考利率 tbd_referrate |
| 39 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 40 | fbasis | 计息基准 | varchar | 50 |  | √ | ' ' | 计息基准,枚举: Actual_actual :Actual/actual SIA_30_360 :30/360(SIA) Actual_360 :Actual/360 Actual_365 :Acutal/365 BMA_30_360 :30/360(BMA) ISDA_30_360 :30/360(ISDA) European_30_360 :30/360(European) Japanese_Actual_365 :Acutal/365(Japanese) ICMA_Actual_actual :Actual/actual(ICMA) ICMA_Actual_360 :Actual/360(ICMA) ICMA_Actual_365 :Acutal/365(ICMA) ICMA_30_360 :30/360E(ICMA) ISDA_Actual_365 :Actual/365(ISDA) BUS_252 :BUS/252 |
| 41 | fenable | 是否可用 | bpchar | 1 |  | √ | ' ' | 是否可用 |
| 42 | fendpreinstdate | 上次预提结束日 | timestamp | 0 |  |  | null | 上次预提结束日 |
| 43 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 44 | finterestrate | 定期利率（%） | numeric | 23 | 10 | √ | 0 | 定期利率（%） |
| 45 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 46 | fratesign | 利率浮动基点（BP） | varchar | 50 |  | √ | ' ' | 利率浮动基点（BP）,枚举: add :加 subtract :减 |
| 47 | ffinorginfoid | 存款机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_suretybill_bn |  | fbillno |
| 2 | pk_fbd_suretybill |  | fid |

---

## 保证金存入处理-关联追踪表 t_fbd_suretybill_tc

- **表名称：** 保证金存入处理-关联追踪表
- **表名：** t_fbd_suretybill_tc

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
| 1 | pk_fbd_suretybill_tc |  | fid |
| 2 | idx_fbd_suretybill_tc_tbill |  | ftbillid |
| 3 | idx_fbd_suretybill_tc_tid |  | ftid |

---

## 关联子实体-子表 t_fbd_suretybill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fbd_suretybill_lk

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
| 1 | pk_fbd_suretybill_lk |  | fpkid |
| 2 | idx_fbd_suretybill_lk_fk |  | fid |

---

## 保证金存入处理-多语言表 t_fbd_suretybill_l

- **表名称：** 保证金存入处理-多语言表
- **表名：** t_fbd_suretybill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fname | fname | varchar | 80 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fbd_suretybill_l |  | fpkid |
| 2 | idx_fbd_suretybill_l_0 |  | fid,flocaleid |

---

## 债务信息分录-子表 t_fbd_suretybill_e

- **表名称：** 债务信息分录-子表
- **表名：** t_fbd_suretybill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreditcurrencyid | 占用币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 3 | fpaybillid | fpaybillid | int8 | 64 |  | √ | 0 |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | frepaydebt | frepaydebt | bpchar | 1 |  | √ | ' ' |  |
| 6 | fbizno | 业务编号 | varchar | 100 |  | √ | ' ' | 业务编号 |
| 7 | frepaydebtamt | frepaydebtamt | numeric | 23 | 10 | √ | 0 |  |
| 8 | fdebtbillno | 债务来源单据 | varchar | 50 |  | √ | ' ' | 债务来源单据 |
| 9 | fcounterpartyid | 交易对手 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 10 | fcreditamount | 占用金额 | numeric | 23 | 10 | √ | 0 | 占用金额 |
| 11 | fdebttype | 债务单据类型 | varchar | 50 |  | √ | ' ' | 债务单据类型,枚举: lc_lettercredit :开信用证 cdm_payablebill :应付票据 gm_letterofguarantee :开函登记 |
| 12 | fenddate | 债务结束日 | timestamp | 0 |  |  | null | 债务结束日 |
| 13 | fsuretystatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: guaranting :保证中 settled :已结清 |
| 14 | fcreditid | 占用授信 | int8 | 64 |  | √ | 0 | 授信额度管理 cfm_creditlimit |
| 15 | fdebtbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 16 | fdebtamt | 债务金额 | numeric | 23 | 10 | √ | 0 | 债务金额 |
| 17 | fstartdate | 债务开始日 | timestamp | 0 |  |  | null | 债务开始日 |
| 18 | fdebtcurrencyid | 债务币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fsuretysource | 单据来源 | varchar | 50 |  | √ | ' ' | 单据来源,枚举: hand :债务生成 linkgen :保证金生成 |
| 21 | freleasecreditamt | 释放授信 | numeric | 23 | 10 | √ | 0 | 释放授信 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fbd_suretybill_e |  | fentryid |
| 2 | idx_fbd_suretybill_e_fk |  | fid |
| 3 | idx_fbd_suretybill_e_bn |  | fbizno |

---

## 收益测算子单据体-子表 t_fbd_surety_sub_re_entry

- **表名称：** 收益测算子单据体-子表
- **表名：** t_fbd_surety_sub_re_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fenddate | 收益计算结束日 | timestamp | 0 |  |  | null | 收益计算结束日 |
| 2 | fdays | 本次收益天数 | int8 | 64 |  | √ | 0 | 本次收益天数 |
| 3 | fstartdate | 收益计算开始日 | timestamp | 0 |  |  | null | 收益计算开始日 |
| 4 | ferevenueamount | 预计收益金额 | numeric | 23 | 10 | √ | 0 | 预计收益金额 |
| 5 | feplanrevenue | 预计收益率 | numeric | 17 | 4 | √ | 0 | 预计收益率 |
| 6 | fconvertdays | 收益率转换天数 | int8 | 64 |  | √ | 0 | 收益率转换天数 |
| 7 | ffinamount | 保证金金额 | numeric | 23 | 10 | √ | 0 | 保证金金额 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fbd_surety_sub_re_entry |  | fdetailid |
| 2 | idx_fbd_surety_sub_re_entry |  | fentryid |

---

## 利率重置分录-子表 t_fbd_rateadjust_entry

- **表名称：** 利率重置分录-子表
- **表名：** t_fbd_rateadjust_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fraeffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 3 | fraremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | frayearrate | 年利率（%） | numeric | 16 | 6 | √ | 0 | 年利率（%） |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | framodifier | 最后更新人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fconfirmdate | 利率确定日 | timestamp | 0 |  |  | null | 利率确定日 |
| 9 | framodifydate | 最后更新时间 | timestamp | 0 |  |  | null | 最后更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fbd_rateadjust_entry |  | fentryid |
| 2 | idx_fbd_rateadjust_entry |  | fid |

---

## 收益测算单据体-子表 t_fbd_surety_re_entry

- **表名称：** 收益测算单据体-子表
- **表名：** t_fbd_surety_re_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frevenueseq | 期数 | varchar | 50 |  | √ | ' ' | 期数 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | frevenuedate | 预计收益日期 | timestamp | 0 |  |  | null | 预计收益日期 |
| 5 | frevenuecalamount | 测算收益 | numeric | 23 | 10 | √ | 0 | 测算收益 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_surety_re_entry |  | fid |
| 2 | pk_fbd_surety_re_entry |  | fentryid |
