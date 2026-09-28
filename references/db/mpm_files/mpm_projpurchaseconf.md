# 项目采购服务确认单-mpm_projpurchaseconf

## 项目采购服务确认单-分表 t_mpm_purchaseconf_p

- **表名称：** 项目采购服务确认单-分表
- **表名：** t_mpm_purchaseconf_p

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpurchaseuserid | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 3 | fsrcentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 4 | fsrcbillno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 5 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 6 | fpurchasegroupid | 采购组 | int8 | 64 |  | √ | 0 | [供应链业务组 bd_operatorgroup](../sbd_files/bd_operatorgroup.md) |
| 7 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fpurchasedeptid | 采购部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fprovidersupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 10 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fsrcentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 12 | freceivesupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 13 | fmainentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 14 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 15 | fmainbillno | 核心单据编号 | varchar | 50 |  | √ | ' ' | 核心单据编号 |
| 16 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 17 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 18 | fmainentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpmc_p_src_id_entryid |  | fsrcbillid,fsrcentryid |
| 2 | pk_t_mpm_purchaseconf_p |  | fid |

---

## 项目采购服务确认单-多语言表 t_mpm_purchaseconf_l

- **表名称：** 项目采购服务确认单-多语言表
- **表名：** t_mpm_purchaseconf_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_purchaseconf_l |  | fpkid |
| 2 | idx_purconf_l_id_localeid |  | fid,flocaleid |

---

## 项目采购服务确认单-关联追踪表 t_mpm_purchaseconf_tc

- **表名称：** 项目采购服务确认单-关联追踪表
- **表名：** t_mpm_purchaseconf_tc

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
| 1 | pk_mpm_purchaseconf_tc |  | fid |
| 2 | idx_mpm_purchaseconf_tc_tid |  | ftid |
| 3 | idx_mpm_purchaseconf_tc_tbill |  | ftbillid |

---

## 交付确认信息单据体-分表 t_mpm_purconfentry_a

- **表名称：** 交付确认信息单据体-分表
- **表名：** t_mpm_purconfentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjoinpayablepriceamount | 关联应付金额 | numeric | 23 | 10 | √ | 0 | 关联应付金额 |
| 3 | fpayableamount | 应付金额 | numeric | 23 | 10 | √ | 0 | 应付金额 |
| 4 | fhasgenapbusbill | 已生成暂估应付单 | bpchar | 1 |  | √ | '0' | 已生成暂估应付单 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpmc_p_id |  | fid |
| 2 | pk_t_mpm_purconfentry_a |  | fentryid |

---

## 项目采购服务确认单-主表 t_mpm_purchaseconf

- **表名称：** 项目采购服务确认单-主表
- **表名：** t_mpm_purchaseconf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | foperatorid | 经办人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcurtaxsettlamt | 含税结算额(本位币) | numeric | 23 | 10 | √ | 0 | 含税结算额(本位币) |
| 4 | forgid | 立项组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fiswrittenoff | 冲销单据 | bpchar | 1 |  | √ | '0' | 冲销单据 |
| 6 | fsettleamt | 结算额 | numeric | 23 | 10 | √ | 0 | 结算额 |
| 7 | fmilestone | 里程碑 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 10 | fistax | 含税 | bpchar | 1 |  | √ | '0' | 含税 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | foperatordeptid | 经办部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 14 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fsumsettleamt | 累计结算额 | numeric | 23 | 10 | √ | 0 | 累计结算额 |
| 17 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 18 | fremark | 备注 | varchar | 1024 |  | √ | ' ' | 备注 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | fhadwrittenoff | 已被冲销 | bpchar | 1 |  | √ | '0' | 已被冲销 |
| 22 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 23 | fisprojectbegin | 项目期初 | bpchar | 1 |  | √ | '0' | 项目期初 |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 26 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 27 | fexpconway | 支出确认方式 | varchar | 50 |  | √ | ' ' | 支出确认方式,枚举: D :按交付物 M :按里程碑 P :按项目进度 |
| 28 | fexpconrate | 支出确认比例(%) | numeric | 23 | 10 | √ | 0 | 支出确认比例(%) |
| 29 | fcursettamt | 结算额(本位币) | numeric | 23 | 10 | √ | 0 | 结算额(本位币) |
| 30 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 31 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 32 | fcursumsettamt | 累计结算额(本位币) | numeric | 23 | 10 | √ | 0 | 累计结算额(本位币) |
| 33 | fpaymode | 付款方式 | varchar | 50 |  | √ | ' ' | 付款方式,枚举: CREDIT :赊购 CASH :现购 |
| 34 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 35 | fbizdate | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 36 | fexratedate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 37 | fexchangetype | 换算方式 | varchar | 50 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 38 | ftaxsettleamt | 含税结算额 | numeric | 23 | 10 | √ | 0 | 含税结算额 |
| 39 | ftaskid | ftaskid | int8 | 64 |  | √ | 0 |  |
| 40 | fcurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 41 | fsettlecurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpmc_project |  | fprojectid |
| 2 | pk_t_mpm_purchaseconf |  | fid |

---

## 关联子实体-子表 t_mpm_purchaseconf_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpm_purchaseconf_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftaxsettleamt | 含税结算额_确认携带值 | numeric | 23 | 10 |  | null | 含税结算额_确认携带值 |
| 7 | ftaxsettleamt_old | 含税结算额_原始携带值 | numeric | 23 | 10 |  | null | 含税结算额_原始携带值 |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_purchaseconf_lk |  | fpkid |
| 2 | idx_mpm_purchaseconf_lk_fk |  | fid |

---

## 关联子实体-子表 t_mpm_purconfentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_mpm_purconfentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量_确认携带值 | numeric | 23 | 10 |  | null | 数量_确认携带值 |
| 2 | fbaseqty_old | 基本数量_原始携带值 | numeric | 23 | 10 |  | null | 基本数量_原始携带值 |
| 3 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 4 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 5 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 6 | fqty_old | 数量_原始携带值 | numeric | 23 | 10 |  | null | 数量_原始携带值 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fbaseqty | 基本数量_确认携带值 | numeric | 23 | 10 |  | null | 基本数量_确认携带值 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_purconfentry_lk |  | fpkid |
| 2 | idx_mpm_purconfentry_lk_fk |  | fentryid |

---

## 交付确认信息单据体-子表 t_mpm_purconfentry

- **表名称：** 交付确认信息单据体-子表
- **表名：** t_mpm_purconfentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscountrate | 单位折扣(率) | numeric | 23 | 10 | √ | 0 | 单位折扣(率) |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fmainbillentity | 核心单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsrcentryseq | 来源单据分录序号 | int8 | 64 |  | √ | 0 | 来源单据分录序号 |
| 8 | fmainbillid | 核心单据ID | int8 | 64 |  | √ | 0 | 核心单据ID |
| 9 | fcuramount | 金额(本位币) | numeric | 23 | 10 | √ | 0 | 金额(本位币) |
| 10 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 11 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 13 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 14 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 15 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 16 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 17 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 19 | fcontractentryid | 合同行ID | int8 | 64 |  | √ | 0 | 合同行ID |
| 20 | fmaterialmasterid | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 21 | factualtaxprice | 实际含税单价 | numeric | 23 | 10 | √ | 0 | 实际含税单价 |
| 22 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 23 | fcuramountandtax | 价税合计(本位币) | numeric | 23 | 10 | √ | 0 | 价税合计(本位币) |
| 24 | fmainbillno | 核心单据编号 | varchar | 80 |  | √ | ' ' | 核心单据编号 |
| 25 | fcontractnum | 合同编号 | varchar | 80 |  | √ | ' ' | 合同编号 |
| 26 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | [行类型 bd_linetype](../sbd_files/bd_linetype.md) |
| 29 | fsrcentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 30 | settleorg | settleorg | int8 | 64 |  | √ | 0 |  |
| 31 | fsrcbillno | 来源单据编号 | varchar | 50 |  | √ | ' ' | 来源单据编号 |
| 32 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 33 | fcontractentity | 合同实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 34 | fdiscountamount | 折扣额 | numeric | 23 | 10 | √ | 0 | 折扣额 |
| 35 | fcontractid | 合同ID | int8 | 64 |  | √ | 0 | 合同ID |
| 36 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 37 | fprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 38 | fcontractseq | 合同行号 | varchar | 36 |  | √ | ' ' | 合同行号 |
| 39 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 40 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 41 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 42 | fdiscounttype | 折扣方式 | varchar | 50 |  | √ | ' ' | 折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 43 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 44 | fmainentryseq | 核心单据分录序号 | int8 | 64 |  | √ | 0 | 核心单据分录序号 |
| 45 | fcurtaxamount | 税额(本位币) | numeric | 23 | 10 | √ | 0 | 税额(本位币) |
| 46 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 47 | factualprice | 实际单价 | numeric | 23 | 10 | √ | 0 | 实际单价 |
| 48 | ftaskid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 49 | fmainentryid | 核心单据行ID | int8 | 64 |  | √ | 0 | 核心单据行ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_purconfentry |  | fentryid |
| 2 | idx_mpmc_src_id_entryid |  | fsrcbillid,fsrcbillentity |

---

## 项目采购服务确认单-反写记录表 t_mpm_purchaseconf_wb

- **表名称：** 项目采购服务确认单-反写记录表
- **表名：** t_mpm_purchaseconf_wb

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
| 1 | idx_mpm_purchaseconf_wb_fk |  | fid |
| 2 | pk_mpm_purchaseconf_wb |  | fentryid |
