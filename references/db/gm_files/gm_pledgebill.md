# 抵质押物-gm_pledgebill

## 共享组织单据体-子表 t_gm_pledgebill_shareorg

- **表名称：** 共享组织单据体-子表
- **表名：** t_gm_pledgebill_shareorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_gm_pledgebill_shareorg |  | fentryid |
| 2 | ind_gm_pledgebill_shareorg_fd |  | fid |

---

## 抵质押物-主表 t_gm_pledgebill

- **表名称：** 抵质押物-主表
- **表名：** t_gm_pledgebill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpledgename | 抵质押物名称 | varchar | 255 |  | √ | ' ' | 抵质押物名称 |
| 3 | fusablerange | 使用范围 | varchar | 80 |  | √ | ' ' | 使用范围,枚举: org :本组织 share :共享 specifyshare :指定共享 |
| 4 | forgid | 资金组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fstoppledgedate | 注销日期 | timestamp | 0 |  |  | null | 注销日期 |
| 6 | fpledgestatus | 业务状态 | varchar | 80 |  | √ | ' ' | 业务状态,枚举: unpledge :待押 pledging :在押 releasepledge :解押 cacelpledge :注销 |
| 7 | fpledgetextno | 抵质押物编码 | varchar | 255 |  | √ | ' ' | 抵质押物编码 |
| 8 | frealrightpersonid | 物权人ID | int8 | 64 |  | √ | 0 | 物权人ID |
| 9 | frealright | 物权属性 | varchar | 80 |  | √ | ' ' | 物权属性,枚举: bos_org :本组织 tmc_org :内部组织 bd_bizpartner :客商 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fenddate | 抵（质）押结束日 | timestamp | 0 |  |  | null | 抵（质）押结束日 |
| 12 | fpledgerate | 抵质押率（％） | int4 | 32 |  | √ | 0 | 抵质押率（％） |
| 13 | fcreatorid | 制单人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fpledgeno | 抵质押物编码ID | int8 | 64 |  | √ | 0 | 抵质押物编码ID |
| 15 | frealrightpersontext | 物权人 | varchar | 80 |  | √ | ' ' | 物权人 |
| 16 | fbaseedittype | fbaseedittype | varchar | 80 |  | √ | ' ' |  |
| 17 | ftotalpledgevalue | 累计抵押价值 | numeric | 19 | 4 | √ | 0 | 累计抵押价值 |
| 18 | fpledgevalue | 可抵押价值 | numeric | 19 | 4 | √ | 0 | 可抵押价值 |
| 19 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 20 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fbillstatus | 单据状态 | varchar | 80 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fbegindate | 抵（质）押开始日 | timestamp | 0 |  |  | null | 抵（质）押开始日 |
| 25 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 26 | fpledgetypeid | 抵质押物种类 | int8 | 64 |  | √ | 0 | [抵质押物种类 gm_pledgetype](../gm_files/gm_pledgetype.md) |
| 27 | foriginalvalue | 原值 | numeric | 19 | 4 | √ | 0 | 原值 |
| 28 | fcurrentappraisedvalue | 当前评估价值 | numeric | 19 | 4 | √ | 0 | 当前评估价值 |
| 29 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 30 | fbillsource | 单据来源 | varchar | 80 |  | √ | ' ' | 单据来源,枚举: gm_pledgebill :手工新增 gm_guaranteecontract :担保合同 cdm_drafttradebill :票据业务 cim_tradebill :投资理财 |
| 31 | fsourcebillid | 原单ID | int8 | 64 |  | √ | 0 | 原单ID |
| 32 | finitialappraisedvalue | 最初评估价值 | numeric | 19 | 4 | √ | 0 | 最初评估价值 |
| 33 | fattribute | 属性 | varchar | 80 |  | √ | ' ' | 属性,枚举: mortgage :抵押 pledge :质押 |
| 34 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gm_pledgebill_fsource |  | fsourcebillid,fbillsource |
| 2 | pk_t_gm_pledgebill |  | fid |
| 3 | idx_gm_pledgebill_billno |  | fbillno |

---

## 关联子实体-子表 t_gm_pledgebill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_gm_pledgebill_lk

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
| 1 | pk_gm_pledgebill_lk |  | fpkid |
| 2 | idx_gm_pledgebill_lk_fk |  | fid |

---

## 抵质押物-关联追踪表 t_gm_pledgebill_tc

- **表名称：** 抵质押物-关联追踪表
- **表名：** t_gm_pledgebill_tc

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
| 1 | pk_gm_pledgebill_tc |  | fid |
| 2 | idx_gm_pledgebill_tc_tbill |  | ftbillid |
| 3 | idx_gm_pledgebill_tc_tid |  | ftid |

---

## 抵质押物-反写记录表 t_gm_pledgebill_wb

- **表名称：** 抵质押物-反写记录表
- **表名：** t_gm_pledgebill_wb

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
| 1 | idx_gm_pledgebill_wb_fk |  | fid |
| 2 | pk_gm_pledgebill_wb |  | fentryid |
