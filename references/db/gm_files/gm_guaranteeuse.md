# 担保占用-gm_guaranteeuse

## 担保占用-主表 t_gm_guaranteeuse

- **表名称：** 担保占用-主表
- **表名：** t_gm_guaranteeuse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgdebtcurrency | 债务币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 3 | fgcparty | 交易对手 | varchar | 255 |  | √ | ' ' | 交易对手 |
| 4 | fgdebtenddate | 债务结束日期 | timestamp | 0 |  |  | null | 债务结束日期 |
| 5 | fgdebtbalance | 剩余债务金额 | numeric | 19 | 6 | √ | 0 | 剩余债务金额 |
| 6 | fgsrcbillid | 来源业务单据Id | int8 | 64 |  | √ | 0 | 来源业务单据Id |
| 7 | fgdebtorgtext | 债务组织 | varchar | 80 |  | √ | ' ' | 债务组织 |
| 8 | fgamount | 担保金额 | numeric | 19 | 6 | √ | 0 | 担保金额 |
| 9 | fgcreditorid | 债权人id | int8 | 64 |  | √ | 0 | 债权人id |
| 10 | fgsrcbilllayout | 来源单据布局 | varchar | 80 |  | √ | ' ' | 来源单据布局 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fgdebtamount | 债务金额 | numeric | 19 | 6 | √ | 0 | 债务金额 |
| 13 | fgdebtorg | 债务组织ID | int8 | 64 |  | √ | 0 | 债务组织ID |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fguaranteecontractid | 担保合同 | int8 | 64 |  | √ | 0 | [担保合同 gm_guaranteecontract_f7](../gm_files/gm_guaranteecontract_f7.md) |
| 16 | fgexchrate | 折算汇率 | numeric | 23 | 10 | √ | 0 | 折算汇率 |
| 17 | fgsrcbillbizamount | 业务金额 | numeric | 19 | 6 | √ | 0 | 业务金额 |
| 18 | fgratio | 担保比例 | numeric | 19 | 6 | √ | 0 | 担保比例 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fgcreditortext | 债权人 | varchar | 80 |  | √ | ' ' | 债权人 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fgdebtstartdate | 债务开始日期 | timestamp | 0 |  |  | null | 债务开始日期 |
| 23 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fgsrcbillno | 来源业务单据编号 | varchar | 80 |  | √ | ' ' | 来源业务单据编号 |
| 26 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 27 | fgsrcbilltype | 来源业务单据类型 | varchar | 80 |  | √ | ' ' | 来源业务单据类型 |
| 28 | fgcurrencyid | 担保币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 29 | fgcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 30 | fgcreditortype | 债权人类型 | varchar | 50 |  | √ | ' ' | 债权人类型 |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaranteeuse_sbillid |  | fgsrcbillid |
| 2 | pk_gm_guaranteeuse |  | fid |
| 3 | idx_gm_guarantee_gcid |  | fguaranteecontractid |

---

## 释放分录-子表 t_gm_guaranteeuse_entry

- **表名称：** 释放分录-子表
- **表名：** t_gm_guaranteeuse_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freturnbilltype | 返还单类型 | varchar | 80 |  | √ | ' ' | 返还单类型 |
| 3 | freturntime | 释放时间 | timestamp | 0 |  |  | null | 释放时间 |
| 4 | freturnamount | 金额 | numeric | 19 | 6 | √ | 0 | 金额 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | freturnbillid | 返还单ID | int8 | 64 |  | √ | 0 | 返还单ID |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_guaranteeuse_eretid |  | freturnbillid |
| 2 | pk_gm_guaranteeuse_entry |  | fentryid |
| 3 | idx_gm_guaranteeuse_efid |  | fid |
