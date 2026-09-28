# 保证金追加处理-fbd_surety_append

## 保证金追加处理-主表 t_fbd_surety_append

- **表名称：** 保证金追加处理-主表
- **表名：** t_fbd_surety_append

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fterm | 期限（ymd） | varchar | 50 |  | √ | ' ' | 期限（ymd） |
| 3 | fsuretybillno | 保证金存入单据 | varchar | 50 |  | √ | ' ' | 保证金存入单据 |
| 4 | forgid | 存款组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fappendamount | 追加金额 | numeric | 23 | 10 | √ | 0 | 追加金额 |
| 6 | fbizstatus | 业务状态 | varchar | 50 |  | √ | ' ' | 业务状态,枚举: 1 :申请中 2 :已办理 3 :已退回 4 :办理中 |
| 7 | famount | 保证金金额 | numeric | 23 | 10 | √ | 0 | 保证金金额 |
| 8 | fappendintdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 9 | fappendflag | 新业务追加 | bpchar | 1 |  | √ | '0' | 新业务追加 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | finvestvarietiesid | 保证金品种 | int8 | 64 |  | √ | 0 | [保证金品种 fbd_investvariety_surety](../fbd_files/fbd_investvariety_surety.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fexpiredate | 到期日期 | timestamp | 0 |  |  | null | 到期日期 |
| 14 | fintdate | 起息日 | timestamp | 0 |  |  | null | 起息日 |
| 15 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 16 | fisfromdebt | 债务列表追加保证金 | bpchar | 1 |  | √ | '0' | 债务列表追加保证金 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fpaybillid | 付款单F7 | int8 | 64 |  | √ | 0 | [付款单 cas_paybill_f7](../cas_files/cas_paybill_f7.md) |
| 21 | fsuretybillid | 保证金存入 | int8 | 64 |  | √ | 0 | [保证金存入处理F7 fbd_suretybill_f7](../fbd_files/fbd_suretybill_f7.md) |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fsettleaccountid | 保证金账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 24 | fappendremark | fappendremark | varchar | 255 |  | √ | ' ' |  |
| 25 | ffinaccountid | 活期账户 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 26 | flockpayamt | 锁定金额 | numeric | 23 | 10 | √ | 0 | 锁定金额 |
| 27 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 28 | fsourcebillid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 29 | finvestorgtype | 存款机构类型 | varchar | 50 |  | √ | ' ' | 存款机构类型,枚举: bd_finorginfo :金融机构 bd_customer :客户 bd_supplier :供应商 fbd_other :其他 |
| 30 | fisvoucher | 生成凭证 | bpchar | 1 |  | √ | '0' | 生成凭证 |
| 31 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 32 | ffinorgother | 存款机构 | varchar | 255 |  | √ | ' ' | 存款机构 |
| 33 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | ffinorginfoid | 存款机构 | int8 | 64 |  | √ | 0 | 金融机构 bd_finorginfo |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_surety_append |  | fid |
| 2 | idx_fbd_surety_apd_bn |  | fbillno |

---

## 保证金追加处理-反写记录表 t_fbd_surety_append_wb

- **表名称：** 保证金追加处理-反写记录表
- **表名：** t_fbd_surety_append_wb

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
| 1 | pk_fbd_surety_append_wb |  | fentryid |
| 2 | idx_fbd_surety_append_wb_fk |  | fid |

---

## 债务信息分录-子表 t_fbd_suretybill_e

- **表名称：** 债务信息分录-子表
- **表名：** t_fbd_suretybill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcreditcurrencyid | 占用币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fsuretyamount | fsuretyamount | numeric | 23 | 10 | √ | 0 |  |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbizno | 业务编号 | varchar | 100 |  | √ | ' ' | 业务编号 |
| 6 | fdebtbillno | 债务来源单据 | varchar | 50 |  | √ | ' ' | 债务来源单据 |
| 7 | fappendamt | 追加金额 | numeric | 23 | 10 | √ | 0 | 追加金额 |
| 8 | fdebttype | 债务单据类型 | varchar | 50 |  | √ | ' ' | 债务单据类型,枚举: lc_lettercredit :开信用证 cdm_payablebill :应付票据 gm_letterofguarantee :开函登记 cfm_loancontract_bl_l :银行借款合同 fl_leasecontractbill :融资租赁合同 cdm_payablebill_ap_manual :批量开票申请 |
| 9 | fenddate | 债务结束日 | timestamp | 0 |  |  | null | 债务结束日 |
| 10 | fsuretystatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: guaranting :保证中 settled :已结清 |
| 11 | fcreditid | 占用授信 | int8 | 64 |  | √ | 0 | [授信合同 cfm_creditlimit](../creditm_files/cfm_creditlimit.md) |
| 12 | fdebtbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 13 | fdebtcurrencyid | 债务币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | fapplybillno | fapplybillno | varchar | 50 |  | √ | ' ' |  |
| 15 | freleasecreditamt | 释放授信 | numeric | 23 | 10 | √ | 0 | 释放授信 |
| 16 | fpaybillid | fpaybillid | int8 | 64 |  | √ | 0 |  |
| 17 | frepaydebt | frepaydebt | bpchar | 1 |  | √ | ' ' |  |
| 18 | frepaydebtamt | frepaydebtamt | numeric | 23 | 10 | √ | 0 |  |
| 19 | fcounterpartyid | 交易对手 | int8 | 64 |  | √ | 0 | [金融机构 bd_finorginfo](../basedata_files/bd_finorginfo.md) |
| 20 | fcreditamount | 占用金额 | numeric | 23 | 10 | √ | 0 | 占用金额 |
| 21 | fapplybillid | fapplybillid | int8 | 64 |  | √ | 0 |  |
| 22 | fdebtamt | 债务金额 | numeric | 23 | 10 | √ | 0 | 债务金额 |
| 23 | fstartdate | 债务开始日 | timestamp | 0 |  |  | null | 债务开始日 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fsuretysource | 单据来源 | varchar | 50 |  | √ | ' ' | 单据来源,枚举: hand :债务生成 linkgen :保证金生成 |

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

## 关联子实体-子表 t_fbd_surety_append_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fbd_surety_append_lk

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
| 1 | pk_fbd_surety_append_lk |  | fpkid |
| 2 | idx_fbd_surety_append_lk_fk |  | fid |

---

## 保证金追加处理-关联追踪表 t_fbd_surety_append_tc

- **表名称：** 保证金追加处理-关联追踪表
- **表名：** t_fbd_surety_append_tc

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
| 1 | pk_fbd_surety_append_tc |  | fid |
| 2 | idx_fbd_surety_append_tc_tid |  | ftid |
| 3 | idx_fbd_surety_append_tc_tbill |  | ftbillid |

---

## 保证金追加处理-多语言表 t_fbd_surety_append_l

- **表名称：** 保证金追加处理-多语言表
- **表名：** t_fbd_surety_append_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fappendremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fbd_surety_append_l |  | fpkid |
| 2 | idx_fbd_surety_append_l_0 |  | fid,flocaleid |

---

## 授信关联分录-子表 t_fbd_suretyappend_c

- **表名称：** 授信关联分录-子表
- **表名：** t_fbd_suretyappend_c

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
| 1 | idx_fbd_suretyappend_c_fk |  | fid |
| 2 | pk_t_fbd_suretyappend_c |  | fentryid |
| 3 | idx_fbd_suretyappend_c_bi |  | fcreditbillid |
