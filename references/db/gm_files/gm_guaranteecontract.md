# 担保合同-gm_guaranteecontract

## 保证金单据体-子表 t_gm_guarcontract_aentry

- **表名称：** 保证金单据体-子表
- **表名：** t_gm_guarcontract_aentry

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
| 9 | fensuretext | 保证人 | varchar | 255 |  | √ | ' ' | 保证人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guarcontract_aentry_fid |  | fid |
| 2 | pk_t_gm_guarcontract_aentry |  | fentryid |

---

## 抵押单据体-子表 t_gm_guarcontract_mentry

- **表名称：** 抵押单据体-子表
- **表名：** t_gm_guarcontract_mentry

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
| 1 | pk_t_gm_guarcontract_mentry |  | fentryid |
| 2 | idx_gm_guarcontract_mentry_fid |  | fid |

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

## 反担保保证单据体-子表 t_gm_guarcontract_ceentry

- **表名称：** 反担保保证单据体-子表
- **表名：** t_gm_guarcontract_ceentry

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
| 1 | idx_gm_guarcontract_ceentry_fd |  | fid |
| 2 | pk_t_gm_guarcontract_ceentry |  | fentryid |

---

## 担保合同-反写记录表 t_gm_guaranteecontract_wb

- **表名称：** 担保合同-反写记录表
- **表名：** t_gm_guaranteecontract_wb

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
| 1 | idx_gm_guaranteecontract_wb_fk |  | fid |
| 2 | pk_gm_guaranteecontract_wb |  | fentryid |

---

## 质押单据体-子表 t_gm_guarcontract_pentry

- **表名称：** 质押单据体-子表
- **表名：** t_gm_guarcontract_pentry

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
| 1 | pk_t_gm_guarcontract_pentry |  | fentryid |
| 2 | idx_gm_guarcontract_pentry_fid |  | fid |

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

## 保证单据体-子表 t_gm_guarcontract_eentry

- **表名称：** 保证单据体-子表
- **表名：** t_gm_guarcontract_eentry

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
| 9 | fensuretext | 保证人 | varchar | 255 |  | √ | ' ' | 保证人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guarcontract_eentry_fid |  | fid |
| 2 | pk_t_gm_guarcontract_eentry |  | fentryid |

---

## 反担保质押单据体-子表 t_gm_guarcontract_cpentry

- **表名称：** 反担保质押单据体-子表
- **表名：** t_gm_guarcontract_cpentry

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
| 1 | idx_gm_guarcontract_cpentry_fd |  | fid |
| 2 | pk_t_gm_guarcontract_cpentry |  | fentryid |

---

## 担保合同-关联追踪表 t_gm_guaranteecontract_tc

- **表名称：** 担保合同-关联追踪表
- **表名：** t_gm_guaranteecontract_tc

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
| 1 | idx_gm_guaranteecontract_tc_tbill |  | ftbillid |
| 2 | idx_gm_guaranteecontract_tc_tid |  | ftid |
| 3 | pk_gm_guaranteecontract_tc |  | fid |

---

## 担保合同-主表 t_gm_guarcontract

- **表名称：** 担保合同-主表
- **表名：** t_gm_guarcontract

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fclosetime | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 5 | fenddate | 担保结束日期 | timestamp | 0 |  |  | null | 担保结束日期 |
| 6 | fcreditorid | 债权人ID | int8 | 64 |  | √ | 0 | 债权人ID |
| 7 | fguaranteeorgtext | 担保人 | varchar | 80 |  | √ | ' ' | 担保人 |
| 8 | fguaranteeamount | 担保费 | numeric | 19 | 4 | √ | 0 | 担保费 |
| 9 | frepledgeamount | frepledgeamount | numeric | 19 | 4 | √ | 0 |  |
| 10 | frepledgebillid | frepledgebillid | int8 | 64 |  | √ | 0 |  |
| 11 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 12 | foldbizstatus | 原业务状态 | varchar | 80 |  | √ | ' ' | 原业务状态,枚举: registing :登记中 registed :已登记 doing :执行中 closed :已关闭 |
| 13 | fguaranteevarietiesid | 担保品种 | int8 | 64 |  | √ | 0 | [担保品种 gm_guaranteevarieties](../gm_files/gm_guaranteevarieties.md) |
| 14 | fguaranteedorgid | 被担保人ID | int8 | 64 |  | √ | 0 | 被担保人ID |
| 15 | fischange | 变更 | bpchar | 1 |  | √ | '0' | 变更 |
| 16 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fguaranteequotaid | fguaranteequotaid | int8 | 64 |  | √ | 0 |  |
| 18 | fcreditortext | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 19 | fguaranteeorgid | 担保人ID | int8 | 64 |  | √ | 0 | 担保人ID |
| 20 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 21 | fdescription | 限制性条款说明 | varchar | 255 |  | √ | ' ' | 限制性条款说明 |
| 22 | fapplybillid | 担保申请单 | int8 | 64 |  | √ | 0 | [担保申请 gm_guaranteeapply_f7](../gm_files/gm_guaranteeapply_f7.md) |
| 23 | fisneedreg | 提供反担保 | bpchar | 1 |  | √ | '0' | 提供反担保 |
| 24 | fisexceedstock | 超股比 | bpchar | 1 |  | √ | '0' | 超股比 |
| 25 | fcreditortype | 债权人类型 | varchar | 80 |  | √ | ' ' | 债权人类型,枚举: tmc_org :内部组织 tmc_bank :银行 tmc_otherbank :非银行金融机构 bd_bizpartner :客商 other :其他 |
| 26 | fguaranteeno | 担保合同号 | varchar | 80 |  | √ | ' ' | 担保合同号 |
| 27 | fguaranteeway | 担保方式 | varchar | 80 |  | √ | ' ' | 担保方式,枚举: ensure :保证 mortgage :抵押 pledge :质押 |
| 28 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fdutyamount | 担保责任金额 | numeric | 19 | 4 | √ | 0 | 担保责任金额 |
| 30 | fbizstatus | 业务状态 | varchar | 80 |  | √ | ' ' | 业务状态,枚举: registing :登记中 registed :已登记 doing :执行中 closed :已关闭 changing :变更中 |
| 31 | famount | 担保合约金额 | numeric | 19 | 4 | √ | 0 | 担保合约金额 |
| 32 | frepledgename | frepledgename | varchar | 255 |  | √ | ' ' |  |
| 33 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | fdescription_tag | 限制性条款说明_详情 | text | 0 |  |  | null | 限制性条款说明_详情 |
| 35 | fguaranteetype | 担保人类型 | varchar | 80 |  | √ | ' ' | 担保人类型,枚举: bos_org :本组织 tmc_org :内部组织 tmc_bank :银行 tmc_otherbank :非银行金融机构 bd_bizpartner :客商 |
| 36 | fcountorguaway | 反担保方式 | varchar | 80 |  | √ | ' ' | 反担保方式,枚举: ensure :保证 mortgage :抵押 pledge :质押 |
| 37 | fguaranteedorgtext | 被担保人 | varchar | 80 |  | √ | ' ' | 被担保人 |
| 38 | fguaranteelimit | 担保范围 | varchar | 80 |  | √ | ' ' | 担保范围,枚举: creditorright :主债权 interest :利息 liquidated :违约金 damages :损害赔偿金 expenses :相关费用 |
| 39 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 41 | fbegindate | 担保开始日期 | timestamp | 0 |  |  | null | 担保开始日期 |
| 42 | fguaranteekindid | fguaranteekindid | int8 | 64 |  | √ | 0 |  |
| 43 | fiscrossguarantee | 交叉互保 | bpchar | 1 |  | √ | '0' | 交叉互保 |
| 44 | fcloseuserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | feassrcid | eas数据id | varchar | 50 |  | √ | ' ' | eas数据id |
| 46 | freguaranteetype | 被担保人类型 | varchar | 80 |  | √ | ' ' | 被担保人类型,枚举: bos_org :本组织 tmc_org :内部组织 bd_bizpartner :客商 other :其他 |
| 47 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 48 | fsourcebillid | 原担保合同 | int8 | 64 |  | √ | 0 | 原担保合同 |
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

---

## 反担保抵押单据体-子表 t_gm_guarcontract_cmentry

- **表名称：** 反担保抵押单据体-子表
- **表名：** t_gm_guarcontract_cmentry

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
| 1 | idx_gm_guarcontract_cmentry_fd |  | fid |
| 2 | pk_t_gm_guarcontract_cmentry |  | fentryid |

---

## 关联子实体-子表 t_gm_guaranteecontract_lk

- **表名称：** 关联子实体-子表
- **表名：** t_gm_guaranteecontract_lk

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
| 1 | idx_gm_guaranteecontract_lk_fk |  | fid |
| 2 | pk_gm_guaranteecontract_lk |  | fpkid |
