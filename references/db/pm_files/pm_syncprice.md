# 同步价格信息-pm_syncprice

## 同步价格信息-主表 t_pm_syncprice

- **表名称：** 同步价格信息-主表
- **表名：** t_pm_syncprice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fsrcorgid | 源单组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fsynctime | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 11 | fsyncconfigid | 同步配置 | int8 | 64 |  | √ | 0 | [同步下游单据配置 msbd_synctgtbillcfg](../msbd_files/msbd_synctgtbillcfg.md) |
| 12 | fsrcentityid | 源单类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 13 | fsyncstatus | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: A :未同步 B :已同步 C :已自动同步 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fbillno | 源单编号 | varchar | 50 |  | √ | ' ' | 源单编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pm_syncprice |  | fid |
| 2 | idx_pm_syncprice_billno |  | fbillno |

---

## 下游单据列表-子表 t_pm_targetbilllist

- **表名称：** 下游单据列表-子表
- **表名：** t_pm_targetbilllist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdiscountrate | 原单位折扣(率) | numeric | 23 | 10 | √ | 0 | 原单位折扣(率) |
| 3 | ftaxrate | 原税率(%) | numeric | 23 | 10 | √ | 0 | 原税率(%) |
| 4 | ftargetprice | 新单价 | numeric | 23 | 10 | √ | 0 | 新单价 |
| 5 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | febillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 7 | forgid | 主业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fsyncresult_tag | 同步结果_详情 | text | 0 |  |  | null | 同步结果_详情 |
| 9 | fsyncsuccess | 同步成功 | bpchar | 1 |  | √ | '0' | 同步成功 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fprice | 原单价 | numeric | 23 | 10 | √ | 0 | 原单价 |
| 12 | feseq | 单据行号 | int8 | 64 |  | √ | 0 | 单据行号 |
| 13 | ftargetcurrencyid | 新币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 14 | feentryid | 分录内码 | int8 | 64 |  | √ | 0 | 分录内码 |
| 15 | fsyncresult | 同步结果 | varchar | 255 |  | √ | ' ' | 同步结果 |
| 16 | ftargettaxrate | 新税率(%) | numeric | 23 | 10 | √ | 0 | 新税率(%) |
| 17 | ftaxrateid | 原税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 18 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 19 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 20 | fentityid | 单据名称 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 21 | ftargetdiscountrate | 新单位折扣(率) | numeric | 23 | 10 | √ | 0 | 新单位折扣(率) |
| 22 | fpriceandtax | 原含税单价 | numeric | 23 | 10 | √ | 0 | 原含税单价 |
| 23 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 24 | ftargetpresent | 新赠品 | bpchar | 1 |  | √ | '0' | 新赠品 |
| 25 | ftargetpriceandtax | 新含税单价 | numeric | 23 | 10 | √ | 0 | 新含税单价 |
| 26 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 27 | fdiscountype | 原折扣方式 | varchar | 50 |  | √ | ' ' | 原折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 28 | fpresent | 原赠品 | bpchar | 1 |  | √ | '0' | 原赠品 |
| 29 | ftargetdiscountype | 新折扣方式 | varchar | 50 |  | √ | ' ' | 新折扣方式,枚举: A :折扣率(%) B :单位折扣额 NULL :无 |
| 30 | ftargettaxrateid | 新税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 31 | feid | 单据内码 | int8 | 64 |  | √ | 0 | 单据内码 |
| 32 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 33 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 34 | fcurrencyid | 原币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 35 | ftargetunitid | 新单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_targetbilllist_fk |  | fid |
| 2 | pk_pm_targetbilllist |  | fentryid |
