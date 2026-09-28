# 担保合同-gm_guaranteecontract_f7

## 担保人信息分录-子表 t_gm_guarantee_entry

- **表名称：** 担保人信息分录-子表
- **表名：** t_gm_guarantee_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fguaranteequotaid | 担保额度 | int8 | 64 |  | √ | 0 | [担保额度 gm_guaranteequota](../gm_files/gm_guaranteequota.md) |
| 3 | fguaranteeorgtext | 担保人 | varchar | 80 |  | √ | ' ' | 担保人 |
| 4 | fguaranteetype | 担保人类型 | varchar | 80 |  | √ | ' ' | 担保人类型,枚举: bos_org :本组织 tmc_org :内部组织 tmc_bank :银行 tmc_otherbank :非银行金融机构 bd_bizpartner :客商 |
| 5 | fguaranteeorgid | 担保人ID | int8 | 64 |  | √ | 0 | 担保人ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fgratio | 担保比例 | numeric | 23 | 10 | √ | 0 | 担保比例 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fgamount | 担保金额 | numeric | 23 | 10 | √ | 0 | 担保金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gm_guarantee_entry |  | fentryid |
| 2 | idx_gm_guarantee_entry |  | fid |

---

## 被担保人信息分录-子表 t_gm_guaranteed_entry

- **表名称：** 被担保人信息分录-子表
- **表名：** t_gm_guaranteed_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fguaranteedorgid | 被担保人ID | int8 | 64 |  | √ | 0 | 被担保人ID |
| 3 | freguaranteetype | 被担保人类型 | varchar | 80 |  | √ | ' ' | 被担保人类型,枚举: bos_org :本组织 tmc_org :内部组织 bd_bizpartner :客商 other :其他 |
| 4 | fguaranteequotaid | 担保额度 | int8 | 64 |  | √ | 0 | [担保额度 gm_guaranteequota](../gm_files/gm_guaranteequota.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fgratio | 被担保比例(%) | numeric | 23 | 10 | √ | 0 | 被担保比例(%) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fguaranteedorgtext | 被担保人 | varchar | 80 |  | √ | ' ' | 被担保人 |
| 9 | fgamount | 被担保金额 | numeric | 23 | 10 | √ | 0 | 被担保金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaranteed_entry |  | fid |
| 2 | pk_t_gm_guaranteed_entry |  | fentryid |

---

## 担保合同-主表 t_gm_guarcontract

- **表名称：** 担保合同-主表
- **表名：** t_gm_guarcontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 4 | fclosetime | fclosetime | timestamp | 0 |  |  | null |  |
| 5 | fenddate | 担保结束日期 | timestamp | 0 |  |  | null | 担保结束日期 |
| 6 | fcreditorid | 债权人id | int8 | 64 |  | √ | 0 | 债权人id |
| 7 | fguaranteeorgtext | 担保人 | varchar | 80 |  | √ | ' ' | 担保人 |
| 8 | fguaranteeamount | fguaranteeamount | numeric | 19 | 4 | √ | 0 |  |
| 9 | frepledgeamount | frepledgeamount | numeric | 19 | 4 | √ | 0 |  |
| 10 | frepledgebillid | frepledgebillid | int8 | 64 |  | √ | 0 |  |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | foldbizstatus | foldbizstatus | varchar | 80 |  | √ | ' ' |  |
| 13 | fguaranteevarietiesid | 担保品种 | int8 | 64 |  | √ | 0 | [担保品种 gm_guaranteevarieties](../gm_files/gm_guaranteevarieties.md) |
| 14 | fguaranteedorgid | 被担保人ID | int8 | 64 |  | √ | 0 | 被担保人ID |
| 15 | fischange | fischange | bpchar | 1 |  | √ | '0' |  |
| 16 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fguaranteequotaid | fguaranteequotaid | int8 | 64 |  | √ | 0 |  |
| 18 | fcreditortext | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 19 | fguaranteeorgid | 担保人Id | int8 | 64 |  | √ | 0 | 担保人Id |
| 20 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 21 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 22 | fapplybillid | fapplybillid | int8 | 64 |  | √ | 0 |  |
| 23 | fisneedreg | fisneedreg | bpchar | 1 |  | √ | '0' |  |
| 24 | fisexceedstock | fisexceedstock | bpchar | 1 |  | √ | '0' |  |
| 25 | fcreditortype | 债权人类型 | varchar | 80 |  | √ | ' ' | 债权人类型,枚举: tmc_org :内部组织 tmc_bank :银行 tmc_otherbank :非银行金融机构 bd_bizpartner :客商 other :其他 |
| 26 | fguaranteeno | 担保合同号 | varchar | 80 |  | √ | ' ' | 担保合同号 |
| 27 | fguaranteeway | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: ensure :保证 ensuamt :保证金 mortgage :抵押 pledge :质押 |
| 28 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 29 | fdutyamount | fdutyamount | numeric | 19 | 4 | √ | 0 |  |
| 30 | fbizstatus | 业务状态 | varchar | 80 |  | √ | ' ' | 业务状态,枚举: registing :登记中 registed :已登记 doing :执行中 closed :已关闭 changing :变更中 |
| 31 | famount | 担保合约金额 | numeric | 19 | 4 | √ | 0 | 担保合约金额 |
| 32 | frepledgename | frepledgename | varchar | 255 |  | √ | ' ' |  |
| 33 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 34 | fdescription_tag | fdescription_tag | text | 0 |  |  | null |  |
| 35 | fguaranteetype | 担保人类型 | varchar | 80 |  | √ | ' ' | 担保人类型,枚举: bos_org :本组织 tmc_org :内部组织 tmc_bank :银行 tmc_otherbank :非银行金融机构 bd_bizpartner :客商 |
| 36 | fcountorguaway | fcountorguaway | varchar | 80 |  | √ | ' ' |  |
| 37 | fguaranteedorgtext | 被担保人 | varchar | 80 |  | √ | ' ' | 被担保人 |
| 38 | fguaranteelimit | 担保范围 | varchar | 80 |  | √ | ' ' | 担保范围,枚举: creditorright :主债权 interest :利息 liquidated :违约金 damages :损害赔偿金 expenses :相关费用 |
| 39 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 40 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 41 | fbegindate | 担保开始日期 | timestamp | 0 |  |  | null | 担保开始日期 |
| 42 | fguaranteekindid | fguaranteekindid | int8 | 64 |  | √ | 0 |  |
| 43 | fiscrossguarantee | 交叉互保 | bpchar | 1 |  | √ | '0' | 交叉互保 |
| 44 | fcloseuserid | fcloseuserid | int8 | 64 |  | √ | 0 |  |
| 45 | feassrcid | feassrcid | varchar | 50 |  | √ | ' ' |  |
| 46 | freguaranteetype | 被担保人类型 | varchar | 80 |  | √ | ' ' | 被担保人类型,枚举: bos_org :本组织 tmc_org :内部组织 bd_bizpartner :客商 other :其他 |
| 47 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 48 | fsourcebillid | fsourcebillid | int8 | 64 |  | √ | 0 |  |
| 49 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gm_guarcontract |  | fid |
| 2 | idx_gm_guarcontract_feassrcid |  | feassrcid |
| 3 | idx_gm_guarcontract |  | fbillno,fid |
