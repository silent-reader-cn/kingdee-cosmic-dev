# 担保申请-gm_guaranteeapply_f7

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

## 担保申请-主表 t_gm_guaranteeapply

- **表名称：** 担保申请-主表
- **表名：** t_gm_guaranteeapply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fishascontract | fishascontract | bpchar | 1 |  | √ | '0' |  |
| 3 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | famount | 担保申请金额 | numeric | 19 | 6 | √ | 0 | 担保申请金额 |
| 5 | frepledgename | frepledgename | varchar | 80 |  | √ | ' ' |  |
| 6 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 7 | fenddate | 预计担保结束日期 | timestamp | 0 |  |  | null | 预计担保结束日期 |
| 8 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 9 | fcreditorid | fcreditorid | int8 | 64 |  | √ | 0 |  |
| 10 | fguaranteeorgtext | 担保人 | varchar | 80 |  | √ | ' ' | 担保人 |
| 11 | fdescription_tag | fdescription_tag | text | 0 |  |  | null |  |
| 12 | fguaranteetype | 担保人类型 | varchar | 30 |  | √ | ' ' | 担保人类型,枚举: bos_org :本组织 tmc_org :内部组织 tmc_bank :银行 tmc_otherbank :非银行金融机构 bd_bizpartner :客商 |
| 13 | fguaranteeamount | 担保费 | numeric | 19 | 6 | √ | 0 | 担保费 |
| 14 | frepledgeamount | frepledgeamount | numeric | 19 | 6 | √ | 0 |  |
| 15 | fguacontractid | fguacontractid | int8 | 64 |  | √ | 0 |  |
| 16 | fcountorguaway | fcountorguaway | varchar | 80 |  | √ | ' ' |  |
| 17 | frepledgebillid | frepledgebillid | int8 | 64 |  | √ | 0 |  |
| 18 | fapplytype | fapplytype | varchar | 30 |  | √ | ' ' |  |
| 19 | fguaranteedorgtext | 被担保人 | varchar | 80 |  | √ | ' ' | 被担保人 |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fguaranteelimit | 担保范围 | varchar | 80 |  | √ | ' ' | 担保范围,枚举: creditorright :主债权 interest :利息 liquidated :违约金 damages :损害赔偿金 expenses :相关费用 |
| 22 | fguaranteevarietiesid | 担保品种 | int8 | 64 |  | √ | 0 | [担保品种 gm_guaranteevarieties](../gm_files/gm_guaranteevarieties.md) |
| 23 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 24 | fguaranteedorgid | fguaranteedorgid | int8 | 64 |  | √ | 0 |  |
| 25 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 27 | fguaranteequotaid | fguaranteequotaid | int8 | 64 |  | √ | 0 |  |
| 28 | fcreditortext | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 29 | fbegindate | 预计担保开始日期 | timestamp | 0 |  |  | null | 预计担保开始日期 |
| 30 | fguaranteeorgid | fguaranteeorgid | int8 | 64 |  | √ | 0 |  |
| 31 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 32 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 33 | fguaranteekindid | fguaranteekindid | int8 | 64 |  | √ | 0 |  |
| 34 | fiscrossguarantee | 交叉互保 | bpchar | 1 |  | √ | '0' | 交叉互保 |
| 35 | fisneedreg | 提供反担保 | bpchar | 1 |  | √ | '0' | 提供反担保 |
| 36 | fisexceedstock | fisexceedstock | bpchar | 1 |  | √ | '0' |  |
| 37 | freguaranteetype | 被担保人类型 | varchar | 30 |  | √ | ' ' | 被担保人类型,枚举: bos_org :本组织 tmc_org :内部组织 bd_bizpartner :客商 |
| 38 | fcreditortype | 债权人类型 | varchar | 30 |  | √ | ' ' | 债权人类型,枚举: |
| 39 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 40 | fguaranteeway | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: ensure :保证 ensuamt :保证金 mortgage :抵押 pledge :质押 |
| 41 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |
| 43 | fdutyamount | fdutyamount | numeric | 19 | 6 | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gm_guaranteeapply |  | fid |
| 2 | idx_t_gm_gapply_billno |  | fbillno |
| 3 | idx_t_gm_gapply_org |  | forgid |

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
