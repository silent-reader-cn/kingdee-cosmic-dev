# 工序结算单-sfc_processsettlebill

## 工序结算单-反写记录表 t_sfc_processsettle_wb

- **表名称：** 工序结算单-反写记录表
- **表名：** t_sfc_processsettle_wb

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
| 1 | idx_sfc_processsettle_wb_fk |  | fid |
| 2 | pk_sfc_processsettle_wb |  | fentryid |

---

## 工序结算单-主表 t_sfc_processsettle

- **表名称：** 工序结算单-主表
- **表名：** t_sfc_processsettle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdeliversupplierid | 供货供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 3 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fexchangerate | 汇率 | numeric | 23 | 10 | √ | 0 | 汇率 |
| 6 | fquotation | 换算方式 | bpchar | 1 |  | √ | ' ' | 换算方式,枚举: 0 :直接汇率 1 :间接汇率 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fsumamount | 金额合计 | numeric | 23 | 10 | √ | 0 | 金额合计 |
| 9 | finvoicesupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 10 | fexratetableid | 汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 11 | freceivingsupplierid | 收款供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 12 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsettlertype | 结算方类型 | bpchar | 1 |  | √ | ' ' | 结算方类型,枚举: A :供应商 B :内协组织 |
| 16 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fpayconditionid | 付款条件 | int8 | 64 |  | √ | 0 | [付款条件 bd_paycondition](../sbd_files/bd_paycondition.md) |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | fsumtotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 21 | fpurchaseorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 23 | fsettletypeid | 结算方式 | int8 | 64 |  | √ | 0 | [结算方式 bd_settlementtype](../basedata_files/bd_settlementtype.md) |
| 24 | fbasecurrencyid | 本位币 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 25 | fprocessorgid | 加工组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fsettletime | 结算日期 | timestamp | 0 |  |  | null | 结算日期 |
| 27 | fsumtaxamount | 税额合计 | numeric | 23 | 10 | √ | 0 | 税额合计 |
| 28 | fsettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fexrateeffectdate | 汇率日期 | timestamp | 0 |  |  | null | 汇率日期 |
| 30 | fcurrencyid | 结算币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 31 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_procstl_createtime |  | fcreatetime |
| 2 | idx_sfc_procstl_billno |  | fbillno |
| 3 | idx_sfc_procstl_stlorg |  | fsettleorgid |
| 4 | idx_sfc_procstl_prodorg |  | forgid |
| 5 | idx_sfc_procstl_stltime |  | fsettletime |
| 6 | pk_sfc_processsettle |  | fid |

---

## 工序结算单-关联追踪表 t_sfc_processsettle_tc

- **表名称：** 工序结算单-关联追踪表
- **表名：** t_sfc_processsettle_tc

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
| 1 | idx_sfc_processsettle_tc_tbill |  | ftbillid |
| 2 | pk_sfc_processsettle_tc |  | fid |
| 3 | idx_sfc_processsettle_tc_tid |  | ftid |

---

## 加工结算信息-分表 t_sfc_processstlentry_t

- **表名称：** 加工结算信息-分表
- **表名：** t_sfc_processstlentry_t

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcbillno | 来源单据 | varchar | 100 |  | √ | ' ' | 来源单据 |
| 3 | fapprodqty | 应付生产单位数量 | numeric | 23 | 10 | √ | 0 | 应付生产单位数量 |
| 4 | funverifybaseqty | 未勾稽基本数量（分录） | numeric | 23 | 10 | √ | 0 | 未勾稽基本数量（分录） |
| 5 | fapbusbillbaseqty | 暂估应付基本数量（分录） | numeric | 23 | 10 | √ | 0 | 暂估应付基本数量（分录） |
| 6 | fcorebillno | 核心单据编号 | varchar | 100 |  | √ | ' ' | 核心单据编号 |
| 7 | frestapqty | 剩余应付数量（分录） | numeric | 23 | 10 | √ | 0 | 剩余应付数量（分录） |
| 8 | fverifyprodqty | 已勾稽生产单位数量 | numeric | 23 | 10 | √ | 0 | 已勾稽生产单位数量 |
| 9 | fcrosscorp | 跨法人 | bpchar | 1 |  | √ | ' ' | 跨法人,枚举: 0 :否 1 :是 |
| 10 | frestapbaseqty | 剩余应付基本数量（分录） | numeric | 23 | 10 | √ | 0 | 剩余应付基本数量（分录） |
| 11 | fapqty | 应付数量（分录） | numeric | 23 | 10 | √ | 0 | 应付数量（分录） |
| 12 | fverifyqty | 已勾稽数量（分录） | numeric | 23 | 10 | √ | 0 | 已勾稽数量（分录） |
| 13 | fcrossorg | 跨组织业务 | bpchar | 1 |  | √ | ' ' | 跨组织业务 |
| 14 | fsrcbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 15 | fcorebillrow | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 16 | fcorebilltype | 核心单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 17 | funverifyprodqty | 未勾稽生产单位数量 | numeric | 23 | 10 | √ | 0 | 未勾稽生产单位数量 |
| 18 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 19 | fsrcbillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 20 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 21 | frestapprodqty | 剩余应付生产单位数量 | numeric | 23 | 10 | √ | 0 | 剩余应付生产单位数量 |
| 22 | fverifybaseqty | 已勾稽基本数量（分录） | numeric | 23 | 10 | √ | 0 | 已勾稽基本数量（分录） |
| 23 | fsrcbillrow | 来源单据行 | int4 | 32 |  | √ | 0 | 来源单据行 |
| 24 | fjoinbusunwoffbaseqty | 暂估应付未冲回基本数量（分录） | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回基本数量（分录） |
| 25 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 26 | fjoinbusunwoffprodqty | 暂估应付未冲回生产单位数量 | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回生产单位数量 |
| 27 | fjoinbusunwoffqty | 暂估应付未冲回数量（分录） | numeric | 23 | 10 | √ | 0 | 暂估应付未冲回数量（分录） |
| 28 | fapbaseqty | 应付基本数量（分录） | numeric | 23 | 10 | √ | 0 | 应付基本数量（分录） |
| 29 | fapbusbillprodqty | 暂估应付生产单位数量 | numeric | 23 | 10 | √ | 0 | 暂估应付生产单位数量 |
| 30 | fapbusbillqty | 暂估应付数量（分录） | numeric | 23 | 10 | √ | 0 | 暂估应付数量（分录） |
| 31 | funverifyqty | 未勾稽数量（分录） | numeric | 23 | 10 | √ | 0 | 未勾稽数量（分录） |
| 32 | fsrcbilltype | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 33 | fgenapbusbill | 已生成暂估应付单 | bpchar | 1 |  | √ | ' ' | 已生成暂估应付单 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fcorebillrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_procstlentryt_src |  | fsrcbillentity,fsrcbilltype,fsrcbillid,fsrcbillrowid |
| 2 | idx_sfc_procstlentryt_core |  | fcorebillentity,fcorebilltype,fcorebillid,fcorebillrowid |
| 3 | pk_sfc_processstlentry_t |  | fentryid |
| 4 | idx_sfc_procstlentryt_id |  | fid |

---

## 加工结算信息-多语言表 t_sfc_processstlentry_l

- **表名称：** 加工结算信息-多语言表
- **表名：** t_sfc_processstlentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_processstlentry_l |  | fentryid,flocaleid |
| 2 | pk_sfc_processstlentry_l |  | fpkid |

---

## 加工结算信息-子表 t_sfc_processstlentry

- **表名称：** 加工结算信息-子表
- **表名：** t_sfc_processstlentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fworkwastebaseqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 3 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 4 | ftotalamount | 价税合计 | numeric | 23 | 10 | √ | 0 | 价税合计 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fworkrowid | 工单行id | int8 | 64 |  | √ | 0 | [生产工单分录F7 sfc_mftorder_f7](../sfc_files/sfc_mftorder_f7.md) |
| 7 | fqualifypriceandtax | 合格含税单价 | numeric | 23 | 10 | √ | 0 | 合格含税单价 |
| 8 | fworkwastepriceandtax | 工废含税单价 | numeric | 23 | 10 | √ | 0 | 工废含税单价 |
| 9 | fprocessdepartid | 加工车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fworkn | 生产工单号 | varchar | 50 |  | √ | ' ' | 生产工单号 |
| 11 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fprocessunitfactor | 工序单位换算系数 | int4 | 32 |  | √ | 0 | 工序单位换算系数 |
| 14 | ftaxamount | 税额 | numeric | 23 | 10 | √ | 0 | 税额 |
| 15 | fprocessplanid | 工序计划 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 16 | fprocessplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 17 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 18 | fqualifyprodqty | 合格生产单位数量 | numeric | 23 | 10 | √ | 0 | 合格生产单位数量 |
| 19 | funitid | 计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fworkwasteqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 21 | fworkrown | 工单行号 | int4 | 32 |  | √ | 0 | 工单行号 |
| 22 | fprodunitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | fprodunitfactor | 表头单位换算系数 | int4 | 32 |  | √ | 0 | 表头单位换算系数 |
| 24 | fscrapwasteprice | 料废单价 | numeric | 23 | 10 | √ | 0 | 料废单价 |
| 25 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 26 | fscrapwastebaseqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |
| 27 | fqualifybaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 28 | foperatorid | 业务员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 29 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 30 | fscrapwasteqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 31 | fqualifyprice | 合格单价 | numeric | 23 | 10 | √ | 0 | 合格单价 |
| 32 | famount | 金额 | numeric | 23 | 10 | √ | 0 | 金额 |
| 33 | fconfiguredcodeid | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 34 | fsource | 来源 | bpchar | 1 |  | √ | ' ' | 来源,枚举: A :内协接收单 B :委外接收单 C :手工 |
| 35 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 36 | fworkid | 生产工单id | int8 | 64 |  | √ | 0 | [生产工单 sfc_bd_mftorer](../sfc_files/sfc_bd_mftorer.md) |
| 37 | fsettleprodqty | 结算生产单位数量 | numeric | 23 | 10 | √ | 0 | 结算生产单位数量 |
| 38 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 39 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 40 | fscrapwasteprodqty | 料废生产单位数量 | numeric | 23 | 10 | √ | 0 | 料废生产单位数量 |
| 41 | fsettleprice | 结算单价 | numeric | 23 | 10 | √ | 0 | 结算单价 |
| 42 | fscrapwastepriceandtax | 料废含税单价 | numeric | 23 | 10 | √ | 0 | 料废含税单价 |
| 43 | fsettleqty | 结算数量 | numeric | 23 | 10 | √ | 0 | 结算数量 |
| 44 | fworkwasteprodqty | 工废生产单位数量 | numeric | 23 | 10 | √ | 0 | 工废生产单位数量 |
| 45 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 46 | fqualifyqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 47 | fsettlepriceandtax | 结算含税单价 | numeric | 23 | 10 | √ | 0 | 结算含税单价 |
| 48 | fworkwasteprice | 工废单价 | numeric | 23 | 10 | √ | 0 | 工废单价 |
| 49 | fsettlebaseqty | 结算基本数量 | numeric | 23 | 10 | √ | 0 | 结算基本数量 |
| 50 | fauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 51 | fprocessunitid | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_procstlentry_id |  | fid |
| 2 | idx_sfc_procstlentry_deptid |  | fdepartid,fprocessdepartid |
| 3 | pk_sfc_processstlentry |  | fentryid |
| 4 | idx_sfc_procstlentry_mat |  | fmaterialid |
| 5 | idx_sfc_procstlentry_planeid |  | fprocessplanid,fprocessplanentryid |

---

## 关联子实体-子表 t_sfc_processsettle_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_processsettle_lk

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
| 1 | pk_sfc_processsettle_lk |  | fpkid |
| 2 | idx_sfc_processsettle_lk_fk |  | fid |

---

## 关联子实体-子表 t_sfc_processstlentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_processstlentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_processstlentry_lk_fk |  | fentryid |
| 2 | pk_sfc_processstlentry_lk |  | fpkid |
