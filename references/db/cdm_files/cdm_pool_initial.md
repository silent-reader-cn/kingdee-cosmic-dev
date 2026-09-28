# 银行票据池初始化-cdm_pool_initial

## 银行票据池初始化-主表 t_cdm_poolinitial

- **表名称：** 银行票据池初始化-主表
- **表名：** t_cdm_poolinitial

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 签约组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fpoolamount | 票据池金额 | numeric | 23 | 10 | √ | 0 | 票据池金额 |
| 9 | fpledgeamount | 质押期初金额 | numeric | 23 | 10 | √ | 0 | 质押期初金额 |
| 10 | fpoolprotocolid | 票据池 | int8 | 64 |  | √ | 0 | [银行票据池协议 cdm_pool_protocol](../cdm_files/cdm_pool_protocol.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | favailableamount | 可用金额 | numeric | 23 | 10 | √ | 0 | 可用金额 |
| 13 | fbizdate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 14 | fuseamount | 已用金额 | numeric | 23 | 10 | √ | 0 | 已用金额 |
| 15 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 16 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 17 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fdepositamount | 保证金期初金额 | numeric | 23 | 10 | √ | 0 | 保证金期初金额 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_poolinitial |  | fid |

---

## 单据体-子表 t_cdm_poolinitial_entry

- **表名称：** 单据体-子表
- **表名：** t_cdm_poolinitial_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fitempledgeamount | 质押金额 | numeric | 23 | 10 | √ | 0 | 质押金额 |
| 3 | fmodifydatefield | 修改时间 | varchar | 50 |  | √ | ' ' | 修改时间 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fbilldate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbilltype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: pledge :质押 payable :开票 |
| 9 | fsourcebill | 业务单据 | int8 | 64 |  | √ | 0 | [票据登记 cdm_draftbillf7](../cdm_files/cdm_draftbillf7.md) |
| 10 | fitemuseamount | 已用金额 | numeric | 23 | 10 | √ | 0 | 已用金额 |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cdm_poolinitial_entry |  | fentryid |
| 2 | idx_cdm_poolinitial_entry_fid |  | fid |
