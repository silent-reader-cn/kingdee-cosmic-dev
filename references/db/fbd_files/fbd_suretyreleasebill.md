# 保证金存出处理-fbd_suretyreleasebill

## 授信关联分录-子表 t_fbd_suretyrelease_c

- **表名称：** 授信关联分录-子表
- **表名：** t_fbd_suretyrelease_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreditbillid | 单据编号 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 3 | fcreditsource | 单据来源 | varchar | 50 |  | √ | ' ' | 单据来源,枚举: hand :授信生成 linkgen :保证金生成 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_suretyrelease_c |  | fentryid |
| 2 | idx_fbd_suretyrelease_c_fk |  | fid |
| 3 | idx_fbd_suretyrelease_c_bi |  | fcreditbillid |

---

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

## 关联子实体-子表 t_fbd_suretyrelease_c_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fbd_suretyrelease_c_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fbd_suretyrelease_c_lk |  | fpkid |
| 2 | idx_fbd_suretyrelease_c_lk_fk |  | fentryid |

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
| 3 | fsuretyamount | 债务占用保证金金额 | numeric | 23 | 10 | √ | 0 | 债务占用保证金金额 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizno | 业务编号 | varchar | 100 |  | √ | ' ' | 业务编号 |
| 6 | fdebtbillno | 来源编号 | varchar | 50 |  | √ | ' ' | 来源编号 |
| 7 | fappendamt | fappendamt | numeric | 23 | 10 | √ | 0 |  |
| 8 | fdebttype | 债务单据类型 | varchar | 50 |  | √ | ' ' | 债务单据类型,枚举: lc_lettercredit :开信用证 cdm_payablebill :应付票据 gm_letterofguarantee :开函登记 cdm_payablebill_ap_manual :批量开票申请 cfm_loancontract_bl_l :银行借款合同 fl_leasecontractbill :融资租赁合同 |
| 9 | fenddate | 债务结束日 | timestamp | 0 |  |  | null | 债务结束日 |
| 10 | fsuretystatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: guaranting :保证中 settled :已结清 |
| 11 | fcreditid | fcreditid | int8 | 64 |  | √ | 0 |  |
| 12 | fdebtbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 13 | fdebtcurrencyid | 债务币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | fapplybillno | fapplybillno | varchar | 50 |  | √ | ' ' |  |
| 15 | freleasecreditamt | freleasecreditamt | numeric | 23 | 10 | √ | 0 |  |
| 16 | fpaybillid | 付款单编号 | int8 | 64 |  | √ | 0 | [付款单 cas_paybill_f7](../cas_files/cas_paybill_f7.md) |
| 17 | frepaydebt | 偿还债务 | bpchar | 1 |  | √ | ' ' | 偿还债务 |
| 18 | frepaydebtamt | 偿还金额 | numeric | 23 | 10 | √ | 0 | 偿还金额 |
| 19 | fcounterpartyid | 交易对手 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 20 | fcreditamount | fcreditamount | numeric | 23 | 10 | √ | 0 |  |
| 21 | fapplybillid | fapplybillid | int8 | 64 |  | √ | 0 |  |
| 22 | fdebtamt | 债务金额 | numeric | 23 | 10 | √ | 0 | 债务金额 |
| 23 | fstartdate | 债务开始日 | timestamp | 0 |  |  | null | 债务开始日 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fsuretysource | fsuretysource | varchar | 50 |  | √ | ' ' |  |

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
| 2 | freleasesource | 存出来源 | varchar | 50 |  | √ | ' ' | 存出来源,枚举: surety :保证金存出 repay :本金抵扣存出 interestrepay :本息抵扣存出 |
| 3 | finteresttype | 利率类型 | varchar | 50 |  | √ | ' ' | 利率类型,枚举: fixed :固定利率 float :浮动利率 |
| 4 | forgid | 存款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fisrevenue | 获取收益 | bpchar | 1 |  | √ | ' ' | 获取收益 |
| 6 | fdemandrate | 活期利率（%） | numeric | 23 | 10 | √ | 0 | 活期利率（%） |
| 7 | ftotalamount | 合计金额 | numeric | 23 | 10 | √ | 0 | 合计金额 |
| 8 | freleasedate | 存出日期 | timestamp | 0 |  |  | null | 存出日期 |
| 9 | famount | 存出金额 | numeric | 23 | 10 | √ | 0 | 存出金额 |
| 10 | frealrevenue | 实际收益 | numeric | 23 | 10 | √ | 0 | 实际收益 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | finvestvarietiesid | 保证金品种 | int8 | 64 |  | √ | 0 | [保证金品种 fbd_investvariety_surety](../fbd_files/fbd_investvariety_surety.md) |
| 13 | fsurplusamount | 可存出金额 | numeric | 23 | 10 | √ | 0 | 可存出金额 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fapplyid | 解活申请 | int8 | 64 |  | √ | 0 | 存款申请F7 cim_deposit_apply_f7 |
| 16 | freleasetype | 存出类型 | varchar | 50 |  | √ | ' ' | 存出类型,枚举: expire :到期存出 inadvance :提前存出 current :活期存出 |
| 17 | frepaybillno | 抵扣单编号 | varchar | 30 |  | √ | ' ' | 抵扣单编号 |
| 18 | fsourcebillno | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |
| 19 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 20 | fremark | fremark | varchar | 255 |  | √ | ' ' |  |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | frecbillno | 收款单编号 | varchar | 50 |  | √ | ' ' | 收款单编号 |
| 23 | fsourcebilltype | 源单类型 | varchar | 50 |  | √ | ' ' | 源单类型,枚举: fbd_suretybill :保证金存入处理 |
| 24 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fpaybillid | 付款单 | int8 | 64 |  | √ | 0 | [付款单 cas_paybill_f7](../cas_files/cas_paybill_f7.md) |
| 27 | fpredictinstamt | 收益测算 | numeric | 23 | 10 | √ | 0 | 收益测算 |
| 28 | fsuretybillid | 保证金编号 | int8 | 64 |  | √ | 0 | [保证金存入处理F7 fbd_suretybill_f7](../fbd_files/fbd_suretybill_f7.md) |
| 29 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 30 | flastreleasedate | 上次存出日期 | timestamp | 0 |  |  | null | 上次存出日期 |
| 31 | frepaybilltype | 抵扣单类型 | varchar | 50 |  | √ | ' ' | 抵扣单类型,枚举: fbd_suretybill :保证金存入处理 cdm_payablebill :开票登记 cdm_payablebill_ap_manual :开票申请 cdm_drafttradebill :票据解付 cfm_repaymentbill :还款处理 fl_rentpaybill :租金支付 |
| 32 | ffinaccountid | 收款账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 33 | frepaybillid | 抵扣单id | int8 | 64 |  | √ | 0 | 抵扣单id |
| 34 | flockpayamt | 锁定金额 | numeric | 23 | 10 | √ | 0 | 锁定金额 |
| 35 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 36 | finvestorgtype | 存款机构类型 | varchar | 50 |  | √ | ' ' | 存款机构类型,枚举: bd_finorginfo :金融机构 bd_customer :客户 bd_supplier :供应商 fbd_other :其他 |
| 37 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 38 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 39 | finterestrate | 定期利率（%） | numeric | 23 | 10 | √ | 0 | 定期利率（%） |
| 40 | ffinorgother | 存款机构 | varchar | 255 |  | √ | ' ' | 存款机构 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | ffinorginfoid | 存款机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fbd_suretyrelease_bn |  | fbillno |
| 2 | pk_fbd_suretyreleasebill |  | fid |
| 3 | idx_fbd_suretyrelease_rp |  | frepaybillid,frepaybilltype |
