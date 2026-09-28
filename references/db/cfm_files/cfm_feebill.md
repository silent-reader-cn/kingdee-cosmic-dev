# 费用明细-cfm_feebill

## 费用明细-反写记录表 t_fbd_feebill_wb

- **表名称：** 费用明细-反写记录表
- **表名：** t_fbd_feebill_wb

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
| 1 | pk_fbd_feebill_wb |  | fentryid |
| 2 | idx_fbd_feebill_wb_fk |  | fid |

---

## 关联子实体-子表 t_fbd_feebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_fbd_feebill_lk

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
| 1 | pk_fbd_feebill_lk |  | fpkid |
| 2 | idx_fbd_feebill_lk_fk |  | fid |

---

## 费用明细-关联追踪表 t_fbd_feebill_tc

- **表名称：** 费用明细-关联追踪表
- **表名：** t_fbd_feebill_tc

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
| 1 | pk_fbd_feebill_tc |  | fid |
| 2 | idx_fbd_feebill_tc_tid |  | ftid |
| 3 | idx_fbd_feebill_tc_tbill |  | ftbillid |

---

## 费用信息分录-子表 t_cfm_feebill_e

- **表名称：** 费用信息分录-子表
- **表名：** t_cfm_feebill_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | ffeedetailamt | 费用明细金额 | numeric | 19 | 6 | √ | 0 | 费用明细金额 |
| 4 | fsrcbillno | 来源单据号 | varchar | 50 |  | √ | ' ' | 来源单据号 |
| 5 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 6 | farrisubno | 到单/交单编号 | varchar | 80 |  | √ | ' ' | 到单/交单编号 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fcreditno | 信用证号 | varchar | 80 |  | √ | ' ' | 信用证号 |
| 9 | fsrcstatus | 来源单据状态 | varchar | 80 |  | √ | ' ' | 来源单据状态,枚举: audit :已审核 noaudit :未审核 |
| 10 | fexcrate | 折债务币种汇率 | numeric | 23 | 10 | √ | 0 | 折债务币种汇率 |
| 11 | ffeeratio | 承担比例（%） | numeric | 19 | 6 | √ | 0 | 承担比例（%） |
| 12 | fproducttypeid | 产品类型 | int8 | 64 |  | √ | 0 | [产品类型 tbd_tradetype](../fbd_files/tbd_tradetype.md) |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cfm_feebill_e |  | fentryid |
| 2 | idx_cfm_feebill_e |  | fid,fsrcbillno |

---

## 费用明细-主表 t_cfm_feebill

- **表名称：** 费用明细-主表
- **表名：** t_cfm_feebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | foppacctbank | 对方银行账号 | varchar | 100 |  | √ | ' ' | 对方银行账号 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | ffeeacctbankid | 费用账号 | int8 | 64 |  | √ | 0 | [银行账户 bd_accountbanks](../basedata_files/bd_accountbanks.md) |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fissettle | 已结算 | bpchar | 1 |  | √ | '0' | 已结算 |
| 8 | fenpayamt | 可用费用金额 | numeric | 19 | 6 | √ | 0 | 可用费用金额 |
| 9 | foppunittext | 对方单位 | varchar | 100 |  | √ | ' ' | 对方单位 |
| 10 | fsettlementtypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 11 | fbillno | 单据编码 | varchar | 30 |  | √ | ' ' | 单据编码 |
| 12 | famountrate | 费率（%） | numeric | 23 | 10 | √ | 0 | 费率（%） |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ffeeaccountid | 费用科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 15 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fbatchno | 批量录入批次号 | varchar | 255 |  | √ | ' ' | 批量录入批次号 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | foppunittype | 对方单位类型 | varchar | 50 |  | √ | ' ' | 对方单位类型,枚举: bos_org :内部单位 bd_finorginfo :金融机构 bd_supplier :供应商 bd_customer :客户 fbd_other :其他 cas_othercontactunit :其他往来单位 |
| 19 | fpaybillid | 付款单编号 | int8 | 64 |  | √ | 0 | [付款单 cas_paybill_f7](../cas_files/cas_paybill_f7.md) |
| 20 | fappsource | 数据应用来源 | varchar | 50 |  | √ | ' ' | 数据应用来源,枚举: cfm :融资 lc :信用证 tm :交易 bdim :发债 gm :担保 cdm :票据 am :实物管理 scf :供应链融资 |
| 21 | ffeeschemeid | 费用方案 | int8 | 64 |  | √ | 0 | [费用方案 fbd_feescheme](../fbd_files/fbd_feescheme.md) |
| 22 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 23 | fcounterpartyid | 交易对手 | int8 | 64 |  | √ | 0 | [交易对手 tbd_counterparty](../fbd_files/tbd_counterparty.md) |
| 24 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 25 | fpayamt | 费用金额 | numeric | 19 | 6 | √ | 0 | 费用金额 |
| 26 | feassrcid | feassrcid | varchar | 50 |  | √ | ' ' |  |
| 27 | foppbebankid | 对方开户银行 | int8 | 64 |  | √ | 0 | [行名行号 bd_bebank](../basedata_files/bd_bebank.md) |
| 28 | ffeetypeid | 费用类型 | int8 | 64 |  | √ | 0 | [费用类型 fbd_feetype](../fbd_files/fbd_feetype.md) |
| 29 | fsharetype | 摊销方式 | bpchar | 1 |  | √ | '0' | 摊销方式,枚举: 0 :不摊销 1 :实际利率法 |
| 30 | ffeesource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: hand :手工新增 linkgen :费用关联生成 batchinput :批量录入 bizpatch :业务补录 |
| 31 | fisvoucher | fisvoucher | bpchar | 1 |  | √ | '0' |  |
| 32 | foppunitid | 对方单位 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fpaydate | 费用日期 | timestamp | 0 |  |  | null | 费用日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cfm_feebill |  | fid |
| 2 | idx_cfm_feebill |  | fbillno |
