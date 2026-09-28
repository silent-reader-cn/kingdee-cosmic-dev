# 物权转移单-pm_transferbill

## 物权转移单-多语言表 t_pm_transferbill_l

- **表名称：** 物权转移单-多语言表
- **表名：** t_pm_transferbill_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_transferbill_l |  | fid,flocaleid |
| 2 | t_pm_transferbill_l_pkey |  | fpkid |

---

## 关联子实体-子表 t_pm_transferbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_transferbill_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_transferbill_lk_fk |  | fid |
| 2 | t_pm_transferbill_lk_pkey |  | fpkid |

---

## 物权转移单-关联追踪表 t_pm_transferbill_tc

- **表名称：** 物权转移单-关联追踪表
- **表名：** t_pm_transferbill_tc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 3 | fttableid | fttableid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | ftid | ftid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_transferbill_tc_pkey |  | fid |
| 2 | idx_pm_transferbill_tc_tid |  | ftid |
| 3 | idx_pm_transferbill_tc_tbill |  | ftbillid |

---

## 物权转移单-反写记录表 t_pm_transferbill_wb

- **表名称：** 物权转移单-反写记录表
- **表名：** t_pm_transferbill_wb

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | foperate | foperate | varchar | 30 |  | √ | ' ' |  |
| 3 | fruleverid | fruleverid | int8 | 64 |  | √ | 0 |  |
| 4 | fsbillid | fsbillid | int8 | 64 |  | √ | 0 |  |
| 5 | fstableid | fstableid | int8 | 64 |  | √ | 0 |  |
| 6 | fsid | fsid | int8 | 64 |  | √ | 0 |  |
| 7 | fwritevalue | fwritevalue | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 8 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 10 | fruleitemid | fruleitemid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_transferbill_wb_fk |  | fid |
| 2 | t_pm_transferbill_wb_pkey |  | fentryid |

---

## 物权转移单-主表 t_pm_transferbill

- **表名称：** 物权转移单-主表
- **表名：** t_pm_transferbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | funitsrctype | 计量单位来源 | varchar | 30 |  | √ | ' ' | 计量单位来源,枚举: MAINBILLUNIT :核心单据计量单位 BIZUNIT :默认业务单位 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fisintertransaction | 内部交易 | bpchar | 1 |  | √ | '0' | 内部交易 |
| 6 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcomment | fcomment | varchar | 512 |  |  | null |  |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 12 | fbiztime | 业务日期 | timestamp | 0 |  |  | null | 业务日期 |
| 13 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fsrcbillform | 源单实体 | varchar | 36 |  | √ | ' ' | 业务对象 bos_objecttype |
| 17 | fbiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 18 | fbookdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 19 | fsrcbilltype | 源单类型(废弃) | varchar | 5 |  | √ | ' ' | 源单类型(废弃),枚举: A :领料出库单 |
| 20 | fsettlecurrencyid | 结算币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 21 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 22 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_transferbill_fbillno |  | fbillno |
| 2 | t_pm_transferbill_pkey |  | fid |

---

## 关联子实体-子表 t_pm_transferentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_transferentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_transferentry_lk_pkey |  | fpkid |
| 2 | idx_pm_transferentry_lk_fk |  | fentryid |

---

## 物料明细-子表 t_pm_transferentry

- **表名称：** 物料明细-子表
- **表名：** t_pm_transferentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | flotnumber | 批号 | varchar | 80 |  | √ | ' ' | 批号 |
| 4 | ftaxrate | 税率(%) | numeric | 23 | 10 | √ | 0.0000000000 | 税率(%) |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fsettlestatus | 结算状态 | varchar | 5 |  | √ | ' ' | 结算状态,枚举: A :待结算 B :结算中 C :已结算 |
| 9 | fprice | 单价 | numeric | 23 | 10 | √ | 0.0000000000 | 单价 |
| 10 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fsrcbillentryseq | 来源单据分录行号 | int8 | 64 |  | √ | 0 | 来源单据分录行号 |
| 12 | fistax | 含税 | bpchar | 1 |  | √ | '1' | 含税 |
| 13 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fentrysettleorgid | 结算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 15 | fjoinqty | 已结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已结算数量 |
| 16 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 18 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 20 | fsrcbillentity | 来源单据实体 | varchar | 36 |  | √ | ' ' | 来源单据实体 |
| 21 | fpriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0.0000000000 | 含税单价 |
| 22 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 23 | fsrcbillnumber | 来源单据编号 | varchar | 80 |  | √ | ' ' | 来源单据编号 |
| 24 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 25 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 26 | fjoinbaseqty | 已结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已结算基本数量 |
| 27 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 28 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 29 | fauxunitid2 | 辅助单位(2) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 30 | famountandtax | 价税合计 | numeric | 23 | 10 | √ | 0.0000000000 | 价税合计 |
| 31 | fjoinauxqty2 | 已结算辅助数量(2) | numeric | 23 | 10 | √ | 0 | 已结算辅助数量(2) |
| 32 | fispresent | 赠品 | bpchar | 1 |  | √ | '0' | 赠品 |
| 33 | fwarehouseid | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 34 | fsupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 35 | fjoinauxqty | 已结算辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已结算辅助数量 |
| 36 | fsrcbillentryid | 来源单据行ID | int8 | 64 |  | √ | 0 | 来源单据行ID |
| 37 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 38 | fauxqty2 | 辅助数量(2) | numeric | 23 | 10 | √ | 0 | 辅助数量(2) |
| 39 | fauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 40 | flocationid | 仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 41 | fentrycomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 42 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 43 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 44 | flinetypeid | 行类型 | int8 | 64 |  | √ | 0 | 行类型 bd_linetype |
| 45 | fentryreqorgid | 需求组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_transferentry_fid |  | fid |
| 2 | t_pm_transferentry_pkey |  | fentryid |
