# 担保申请-gm_guaranteeapply

## 反担保保证单据体-子表 t_gm_guaapply_ceentry

- **表名称：** 反担保保证单据体-子表
- **表名：** t_gm_guaapply_ceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 保证人类型 | varchar | 80 |  | √ | ' ' | 保证人类型,枚举: tmc_org :内部组织 bd_bizpartner :客商 other :其他 |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fensurerate | 保证比例（%） | numeric | 23 | 10 | √ | 0 | 保证比例（%） |
| 6 | famount | 保证金额 | numeric | 23 | 10 | √ | 0 | 保证金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fensure | 保证人ID | int8 | 64 |  | √ | 0 | 保证人ID |
| 9 | fensuretext | 保证人 | varchar | 80 |  | √ | ' ' | 保证人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaapply_ceentry_fd |  | fid |
| 2 | pk_t_gm_guaapply_ceentry |  | fentryid |

---

## 抵押单据体-子表 t_gm_guaapply_mentry

- **表名称：** 抵押单据体-子表
- **表名：** t_gm_guaapply_mentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplegid | 抵质押物 | int8 | 64 |  | √ | 0 | [抵质押物f7 gm_pledgebill_f7](../gm_files/gm_pledgebill_f7.md) |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | famount | 本次抵押价值 | numeric | 19 | 4 | √ | 0 | 本次抵押价值 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaapply_mentry_fid |  | fid |
| 2 | pk_t_gm_guaapply_mentry |  | fentryid |

---

## 保证金单据体-子表 t_gm_guaapply_aentry

- **表名称：** 保证金单据体-子表
- **表名：** t_gm_guaapply_aentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 保证人类型 | varchar | 80 |  | √ | ' ' | 保证人类型,枚举: tmc_org :内部组织 tmc_bank :银行 tmc_otherbank :非银行金融机构 bd_bizpartner :客商 |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fensurerate | 保证比例（%） | numeric | 23 | 10 | √ | 0 | 保证比例（%） |
| 6 | famount | 保证金额 | numeric | 19 | 5 | √ | 0 | 保证金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fensure | 保证人ID | int8 | 64 |  | √ | 0 | 保证人ID |
| 9 | fensuretext | 保证人 | varchar | 80 |  | √ | ' ' | 保证人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gm_guaapply_aentry |  | fentryid |
| 2 | idx_gm_guaapply_aentry_fid |  | fid |

---

## 反担保质押单据体-子表 t_gm_guaapply_cpentry

- **表名称：** 反担保质押单据体-子表
- **表名：** t_gm_guaapply_cpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplegid | 抵质押物 | int8 | 64 |  | √ | 0 | [抵质押物f7 gm_pledgebill_f7](../gm_files/gm_pledgebill_f7.md) |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | famount | 本次抵押价值 | numeric | 23 | 10 | √ | 0 | 本次抵押价值 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaapply_cpentry_fd |  | fid |
| 2 | pk_t_gm_guaapply_cpentry |  | fentryid |

---

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
| 7 | fgratio | 担保比例(%) | numeric | 23 | 10 | √ | 0 | 担保比例(%) |
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
| 2 | fishascontract | 已登记担保合同 | bpchar | 1 |  | √ | '0' | 已登记担保合同 |
| 3 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | famount | 担保申请金额 | numeric | 19 | 6 | √ | 0 | 担保申请金额 |
| 5 | frepledgename | frepledgename | varchar | 80 |  | √ | ' ' |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fenddate | 预计担保结束日期 | timestamp | 0 |  |  | null | 预计担保结束日期 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fcreditorid | 债权人ID | int8 | 64 |  | √ | 0 | 债权人ID |
| 10 | fguaranteeorgtext | 担保人 | varchar | 80 |  | √ | ' ' | 担保人 |
| 11 | fdescription_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 12 | fguaranteetype | 担保人类型 | varchar | 30 |  | √ | ' ' | 担保人类型,枚举: bos_org :本组织 tmc_org :内部组织 tmc_bank :银行 tmc_otherbank :非银行金融机构 bd_bizpartner :客商 |
| 13 | fguaranteeamount | 担保费 | numeric | 19 | 6 | √ | 0 | 担保费 |
| 14 | frepledgeamount | frepledgeamount | numeric | 19 | 6 | √ | 0 |  |
| 15 | fguacontractid | 担保合同 | int8 | 64 |  | √ | 0 | [担保合同 gm_guaranteecontract_f7](../gm_files/gm_guaranteecontract_f7.md) |
| 16 | fcountorguaway | 反担保方式 | varchar | 80 |  | √ | ' ' | 反担保方式,枚举: ensure :保证 mortgage :抵押 pledge :质押 |
| 17 | frepledgebillid | frepledgebillid | int8 | 64 |  | √ | 0 |  |
| 18 | fapplytype | 申请类型 | varchar | 30 |  | √ | ' ' | 申请类型,枚举: add :新增担保 change :变更担保 |
| 19 | fguaranteedorgtext | 被担保人 | varchar | 80 |  | √ | ' ' | 被担保人 |
| 20 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 21 | fguaranteelimit | 担保范围 | varchar | 80 |  | √ | ' ' | 担保范围,枚举: creditorright :主债权 interest :利息 liquidated :违约金 damages :损害赔偿金 expenses :相关费用 |
| 22 | fguaranteevarietiesid | 担保品种 | int8 | 64 |  | √ | 0 | [担保品种 gm_guaranteevarieties](../gm_files/gm_guaranteevarieties.md) |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fguaranteedorgid | 被担保人ID | int8 | 64 |  | √ | 0 | 被担保人ID |
| 25 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 26 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 27 | fguaranteequotaid | fguaranteequotaid | int8 | 64 |  | √ | 0 |  |
| 28 | fcreditortext | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 29 | fbegindate | 预计担保开始日期 | timestamp | 0 |  |  | null | 预计担保开始日期 |
| 30 | fguaranteeorgid | 担保人ID | int8 | 64 |  | √ | 0 | 担保人ID |
| 31 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 32 | fdescription | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 33 | fguaranteekindid | fguaranteekindid | int8 | 64 |  | √ | 0 |  |
| 34 | fiscrossguarantee | 交叉互保 | bpchar | 1 |  | √ | '0' | 交叉互保 |
| 35 | fisneedreg | 提供反担保 | bpchar | 1 |  | √ | '0' | 提供反担保 |
| 36 | fisexceedstock | 超股比 | bpchar | 1 |  | √ | '0' | 超股比 |
| 37 | freguaranteetype | 被担保人类型 | varchar | 30 |  | √ | ' ' | 被担保人类型,枚举: bos_org :本组织 tmc_org :内部组织 bd_bizpartner :客商 other :其他 |
| 38 | fcreditortype | 债权人类型 | varchar | 30 |  | √ | ' ' | 债权人类型,枚举: tmc_org :内部组织 tmc_bank :银行 tmc_otherbank :非银行金融机构 bd_bizpartner :客商 |
| 39 | fbizdate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 40 | fguaranteeway | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: ensure :保证 mortgage :抵押 pledge :质押 |
| 41 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fdutyamount | 担保责任金额 | numeric | 19 | 6 | √ | 0 | 担保责任金额 |

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

## 反担保抵押单据体-子表 t_gm_guaapply_cmentry

- **表名称：** 反担保抵押单据体-子表
- **表名：** t_gm_guaapply_cmentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplegid | 抵质押物 | int8 | 64 |  | √ | 0 | [抵质押物f7 gm_pledgebill_f7](../gm_files/gm_pledgebill_f7.md) |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | famount | 本次抵押价值 | numeric | 23 | 10 | √ | 0 | 本次抵押价值 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaapply_cmentry_fd |  | fid |
| 2 | pk_t_gm_guaapply_cmentry |  | fentryid |

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

## 质押单据体-子表 t_gm_guaapply_pentry

- **表名称：** 质押单据体-子表
- **表名：** t_gm_guaapply_pentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplegid | 抵质押物 | int8 | 64 |  | √ | 0 | [抵质押物f7 gm_pledgebill_f7](../gm_files/gm_pledgebill_f7.md) |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | famount | 本次抵押价值 | numeric | 19 | 4 | √ | 0 | 本次抵押价值 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gm_guaapply_pentry |  | fentryid |
| 2 | t_gm_guaapply_pentry_fid |  | fid |

---

## 保证单据体-子表 t_gm_guaapply_eentry

- **表名称：** 保证单据体-子表
- **表名：** t_gm_guaapply_eentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 保证人类型 | varchar | 80 |  | √ | ' ' | 保证人类型,枚举: tmc_org :内部组织 tmc_bank :银行 tmc_otherbank :非银行金融机构 bd_bizpartner :客商 |
| 3 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fensurerate | 保证比例（%） | numeric | 23 | 10 | √ | 0 | 保证比例（%） |
| 6 | famount | 保证金额 | numeric | 19 | 4 | √ | 0 | 保证金额 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fensure | 保证人ID | int8 | 64 |  | √ | 0 | 保证人ID |
| 9 | fensuretext | 保证人 | varchar | 80 |  | √ | ' ' | 保证人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gm_guaapply_eentry |  | fentryid |
| 2 | idx_gm_guaapply_eentry_fid |  | fid |
