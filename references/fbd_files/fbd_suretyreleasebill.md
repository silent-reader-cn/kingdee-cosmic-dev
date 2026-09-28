# 保证金存出处理-fbd_suretyreleasebill

## 关联子实体-子表 t_fbd_suretyreleasebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fbd_suretyreleasebill_lk

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
| 1 | pk_fbd_suretyreleasebill_lk |  | fpkid |
| 2 | idx_fbd_suretyrelease_lk_fk |  | fid |

---

## 保证金存出处理-关联追踪表 t_fbd_suretyreleasebill_tc

- **表名称：** 保证金存出处理-关联追踪表
- **表名：** t_fbd_suretyreleasebill_tc

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
| 1 | idx_fbd_suretyreleasebill_tc_tbill |  | ftbillid |
| 2 | pk_fbd_suretyreleasebill_tc |  | fid |
| 3 | idx_fbd_suretyreleasebill_tc_tid |  | ftid |
| 4 | idx_fbd_suretyrelease_tc_tbill |  | ftbillid |
| 5 | idx_fbd_suretyrelease_tc_tid |  | ftid |

---

## 保证金存出处理-多语言表 t_fbd_suretyreleasebill_l

- **表名称：** 保证金存出处理-多语言表
- **表名：** t_fbd_suretyreleasebill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fbd_suretyreleasebill_l |  | fpkid |
| 2 | idx_fbd_suretyrelease_l_0 |  | fid,flocaleid |

---

## 债务信息分录-子表 t_fbd_suretybill_e

- **表名称：** 债务信息分录-子表
- **表名：** t_fbd_suretybill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreditcurrencyid | fcreditcurrencyid | int8 | 64 |  | √ | 0 |  |
| 3 | fpaybillid | 付款单编号 | int8 | 64 |  | √ | 0 | 付款单 cas_paybill_f7 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | frepaydebt | 偿还债务 | bpchar | 1 |  | √ | ' ' | 偿还债务 |
| 6 | fbizno | fbizno | varchar | 100 |  | √ | ' ' |  |
| 7 | frepaydebtamt | 偿还金额 | numeric | 23 | 10 | √ | 0 | 偿还金额 |
| 8 | fdebtbillno | 来源编号 | varchar | 50 |  | √ | ' ' | 来源编号 |
| 9 | fcounterpartyid | 交易对手 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |
| 10 | fcreditamount | fcreditamount | numeric | 23 | 10 | √ | 0 |  |
| 11 | fdebttype | 债务单据类型 | varchar | 50 |  | √ | ' ' | 债务单据类型,枚举: lc_lettercredit :开信用证 cdm_payablebill :应付票据 gm_letterofguarantee :开函登记 |
| 12 | fenddate | 债务结束日 | timestamp | 0 |  |  | null | 债务结束日 |
| 13 | fsuretystatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: guaranting :保证中 settled :已结清 |
| 14 | fcreditid | fcreditid | int8 | 64 |  | √ | 0 |  |
| 15 | fdebtbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 16 | fdebtamt | 债务金额 | numeric | 23 | 10 | √ | 0 | 债务金额 |
| 17 | fstartdate | 债务开始日 | timestamp | 0 |  |  | null | 债务开始日 |
| 18 | fdebtcurrencyid | 债务币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 20 | fsuretysource | fsuretysource | varchar | 50 |  | √ | ' ' |  |
| 21 | freleasecreditamt | freleasecreditamt | numeric | 23 | 10 | √ | 0 |  |

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

## 保证金存出处理-反写记录表 t_fbd_suretyreleasebill_wb

- **表名称：** 保证金存出处理-反写记录表
- **表名：** t_fbd_suretyreleasebill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foperate | foperate | varchar | 50 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0 |  |
| 8 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_suretyrelease_wb_fk |  | fid |
| 2 | pk_fbd_suretyreleasebill_wb |  | fentryid |

---

## 保证金存出处理-主表 t_fbd_suretyreleasebill

- **表名称：** 保证金存出处理-主表
- **表名：** t_fbd_suretyreleasebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | finteresttype | 利率类型 | varchar | 50 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 |
| 3 | forgid | 存款组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fisrevenue | 获取收益 | bpchar | 1 |  | √ | ' ' | 获取收益 |
| 5 | fdemandrate | 活期利率（%） | numeric | 23 | 10 | √ | 0 | 活期利率（%） |
| 6 | ftotalamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 7 | freleasedate | 存出日期 | timestamp | 0 |  |  | null | 存出日期 |
| 8 | famount | 存出金额 | numeric | 23 | 10 | √ | 0 | 存出金额 |
| 9 | frealrevenue | 实际收益 | numeric | 23 | 10 | √ | 0 | 实际收益 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | finvestvarietiesid | 保证金品种 | int8 | 64 |  | √ | 0 | 保证金品种 fbd_investvariety_surety |
| 12 | fsurplusamount | 可存出金额 | numeric | 23 | 10 | √ | 0 | 可存出金额 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fapplyid | 解活申请 | int8 | 64 |  | √ | 0 | 存款申请F7 cim_deposit_apply_f7 |
| 15 | freleasetype | 存出类型 | varchar | 50 |  | √ | ' ' | 存出类型,枚举: expire :到期存出 inadvance :提前存出 current :活期存出 |
| 16 | fsourcebillno | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |
| 17 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 18 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | frecbillno | 收款单编号 | varchar | 50 |  | √ | ' ' | 收款单编号 |
| 21 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: fbd_suretybill :保证金存入处理 |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fpaybillid | 付款单 | int8 | 64 |  | √ | 0 | 付款单 cas_paybill_f7 |
| 25 | fpredictinstamt | 收益测算 | numeric | 23 | 10 | √ | 0 | 收益测算 |
| 26 | fsuretybillid | 保证金编号 | int8 | 64 |  | √ | 0 | 保证金存入处理F7 fbd_suretybill_f7 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | flastreleasedate | 上次存出日期 | timestamp | 0 |  |  | null | 上次存出日期 |
| 29 | ffinaccountid | 收款账户 | int8 | 64 |  | √ | 0 | 银行账户 bd_accountbanks |
| 30 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 31 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 32 | finterestrate | 定期利率（%） | numeric | 23 | 10 | √ | 0 | 定期利率（%） |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | ffinorginfoid | 存款机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_suretyrelease_bn |  | fbillno |
| 2 | pk_fbd_suretyreleasebill |  | fid |
