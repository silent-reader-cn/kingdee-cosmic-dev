# 委外接收单-sfc_outreceive

## 委外接收单-多语言表 t_sfc_outreceive_l

- **表名称：** 委外接收单-多语言表
- **表名：** t_sfc_outreceive_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_outreceive_l_id |  | fid,flocaleid |
| 2 | pk_sfc_outreceive_l |  | fpkid |

---

## 委外接收单-关联追踪表 t_sfc_outreceive_tc

- **表名称：** 委外接收单-关联追踪表
- **表名：** t_sfc_outreceive_tc

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
| 1 | pk_sfc_outreceive_tc |  | fid |
| 2 | idx_sfc_outreceive_tc_tbill |  | ftbillid |
| 3 | idx_sfc_outreceive_tc_tid |  | ftid |

---

## 接收明细-子表 t_sfc_outreceiveentry

- **表名称：** 接收明细-子表
- **表名：** t_sfc_outreceiveentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fquabaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 3 | fstockwastbaseqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 6 | fbasereceiveqty | 接收基本数量 | numeric | 23 | 10 | √ | 0 | 接收基本数量 |
| 7 | fworkrowid | 工单分录id | int8 | 64 |  | √ | 0 | [生产工单分录F7 sfc_mftorder_f7](../sfc_files/sfc_mftorder_f7.md) |
| 8 | fquaqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 9 | fcorebilltypeid | 核心单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 10 | fworkwastbaseqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 11 | fcorebillrow | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 12 | fbaseunitid | 产品基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 13 | fstockwastqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 14 | fbasequaqtyreport | 已汇报合格基本数量 | numeric | 23 | 10 | √ | 0 | 已汇报合格基本数量 |
| 15 | fsecquabaseqty | 联副产品合格基本数量(废弃) | numeric | 23 | 10 | √ | 0 | 联副产品合格基本数量(废弃) |
| 16 | fbaseworkwastqtyreport | 已汇报工废基本数量 | numeric | 23 | 10 | √ | 0 | 已汇报工废基本数量 |
| 17 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 18 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fyieldreceiveqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 20 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 21 | fcorebillnumber | 核心单据编号 | varchar | 100 |  | √ | ' ' | 核心单据编号 |
| 22 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 23 | fsampledestorybaseqty | 样本破坏基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏基本数量 |
| 24 | freworkqty | 退回返工数量 | numeric | 23 | 10 | √ | 0 | 退回返工数量 |
| 25 | fentryremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fcorebillrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 28 | fproplanid | 工序计划 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 29 | freceiveqty | 接收数量 | numeric | 23 | 10 | √ | 0 | 接收数量 |
| 30 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 31 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 32 | fworkwastqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 33 | fsampledestoryproqty | 样本破坏生产数量 | numeric | 23 | 10 | √ | 0 | 样本破坏生产数量 |
| 34 | fsecworkwastbaseqty | 联副产品工废基本数量 | numeric | 23 | 10 | √ | 0 | 联副产品工废基本数量 |
| 35 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 36 | fworkid | 生产工单号 | int8 | 64 |  | √ | 0 | 生产工单 pom_mftorder |
| 37 | fbaseyieldrecqtyreport | 已汇报让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 已汇报让步接收基本数量 |
| 38 | fsbillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 39 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 40 | fworkwastqtyreport | 已汇报工废数量 | numeric | 23 | 10 | √ | 0 | 已汇报工废数量 |
| 41 | fbaseyieldreceiveqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 42 | fbasereworkqty | 退回返工基本数量 | numeric | 23 | 10 | √ | 0 | 退回返工基本数量 |
| 43 | fquaqtyreport | 已汇报合格数量 | numeric | 23 | 10 | √ | 0 | 已汇报合格数量 |
| 44 | fbackflishflag | 倒冲标识 | varchar | 10 |  | √ | ' ' | 倒冲标识,枚举: not :未倒冲 sucess :倒冲成功 part :部分倒冲 |
| 45 | fyieldrecqtyreport | 已汇报让步接收数量 | numeric | 23 | 10 | √ | 0 | 已汇报让步接收数量 |
| 46 | fstockwastqtyreport | 已汇报料废数量 | numeric | 23 | 10 | √ | 0 | 已汇报料废数量 |
| 47 | fsampledestoryqty | 样本破坏数量 | numeric | 23 | 10 | √ | 0 | 样本破坏数量 |
| 48 | fsecstockwastbaseqty | 联副产品料废基本数量 | numeric | 23 | 10 | √ | 0 | 联副产品料废基本数量 |
| 49 | fproducttype | 产品类型 | bpchar | 1 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 50 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 51 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 52 | fsourcebillnumber | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 53 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 54 | freceiveqtyback | 接收数量（后台） | numeric | 23 | 10 | √ | 0 | 接收数量（后台） |
| 55 | fproplanbillid | 工序计划号 | int8 | 64 |  | √ | 0 | 工序计划 sfc_processplanbill |
| 56 | fbasestockwastqtyreport | 已汇报料废基本数量 | numeric | 23 | 10 | √ | 0 | 已汇报料废基本数量 |
| 57 | fplanendtime | 计划接收日期(废弃) | timestamp | 0 |  |  | null | 计划接收日期(废弃) |
| 58 | fprocessunitid | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_outreceiveentry_fid |  | fid |
| 2 | pk_sfc_outreceiveentry |  | fentryid |

---

## 接收明细-多语言表 t_sfc_outreceiveentry_l

- **表名称：** 接收明细-多语言表
- **表名：** t_sfc_outreceiveentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentryremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
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
| 1 | pk_sfc_outreceiveentry_l |  | fpkid |
| 2 | idx_sfc_outreceiveentry_l_id |  | fentryid,flocaleid |

---

## 接收明细-分表 t_sfc_outreceiveentry_b

- **表名称：** 接收明细-分表
- **表名：** t_sfc_outreceiveentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutsettleqty | 委外结算数量 | numeric | 23 | 10 | √ | 0 | 委外结算数量 |
| 3 | foutsendid | 连续委外关联发出单id | varchar | 50 |  | √ | ' ' | 连续委外关联发出单id |
| 4 | ftaxratevalue | 税率(%) | numeric | 23 | 10 | √ | 0 | 税率(%) |
| 5 | foutsettlepushqty | 关联委外结算数量 | numeric | 23 | 10 | √ | 0 | 关联委外结算数量 |
| 6 | foutsettlebaseqty | 委外结算基本数量 | numeric | 23 | 10 | √ | 0 | 委外结算基本数量 |
| 7 | fcreatesend | 已生成连续委外发出单 | bpchar | 1 |  | √ | '0' | 已生成连续委外发出单 |
| 8 | foutsettlepushbaseqty | 关联委外结算基本数量 | numeric | 23 | 10 | √ | 0 | 关联委外结算基本数量 |
| 9 | foutsourcepriceandtax | 合格含税单价 | numeric | 23 | 10 | √ | 0 | 合格含税单价 |
| 10 | fworkwasteprice | 工废单价 | numeric | 23 | 10 | √ | 0 | 工废单价 |
| 11 | fchargeunitid | 计价单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fscrapwasteprice | 料废单价 | numeric | 23 | 10 | √ | 0 | 料废单价 |
| 13 | fworkwastepriceandtax | 工废含税单价 | numeric | 23 | 10 | √ | 0 | 工废含税单价 |
| 14 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | [税率 bd_taxrate](../basedata_files/bd_taxrate.md) |
| 15 | fscrapwastepriceandtax | 料废含税单价 | numeric | 23 | 10 | √ | 0 | 料废含税单价 |
| 16 | foutsourceprice | 合格单价 | numeric | 23 | 10 | √ | 0 | 合格单价 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_outreceiveentry_b_id |  | fid |
| 2 | pk_sfc_outreceiveentry_b |  | fentryid |

---

## 接收明细-分表 t_sfc_outreceiveentry_c

- **表名称：** 接收明细-分表
- **表名：** t_sfc_outreceiveentry_c

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fyieldrecreportprodqty | 已汇报让步接收生产数量 | numeric | 23 | 10 | √ | 0 | 已汇报让步接收生产数量 |
| 3 | finspectprodqty | 检验生产数量 | numeric | 23 | 10 | √ | 0 | 检验生产数量 |
| 4 | flinkinprodqty | 关联检验生产数量 | numeric | 23 | 10 | √ | 0 | 关联检验生产数量 |
| 5 | fsecworkwastprodqty | 联副产品工废生产数量 | numeric | 23 | 10 | √ | 0 | 联副产品工废生产数量 |
| 6 | fstockwastprodqty | 料废生产数量 | numeric | 23 | 10 | √ | 0 | 料废生产数量 |
| 7 | fworkwastprodqty | 工废生产数量 | numeric | 23 | 10 | √ | 0 | 工废生产数量 |
| 8 | freworkprodqty | 退回返工生产数量 | numeric | 23 | 10 | √ | 0 | 退回返工生产数量 |
| 9 | foutsettlepushprodqty | 关联委外结算生产数量 | numeric | 23 | 10 | √ | 0 | 关联委外结算生产数量 |
| 10 | fyieldreceiveprodqty | 让步接收生产数量 | numeric | 23 | 10 | √ | 0 | 让步接收生产数量 |
| 11 | fsecstockwastprodqty | 联副产品料废生产数量 | numeric | 23 | 10 | √ | 0 | 联副产品料废生产数量 |
| 12 | fstockwastreportprodqty | 已汇报料废生产数量 | numeric | 23 | 10 | √ | 0 | 已汇报料废生产数量 |
| 13 | fquaproduceqty | 合格生产数量 | numeric | 23 | 10 | √ | 0 | 合格生产数量 |
| 14 | fquareportprodqty | 已汇报合格生产数量 | numeric | 23 | 10 | √ | 0 | 已汇报合格生产数量 |
| 15 | fproducereceiveqty | 接收生产数量 | numeric | 23 | 10 | √ | 0 | 接收生产数量 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | foutsettleprodqty | 委外结算生产数量 | numeric | 23 | 10 | √ | 0 | 委外结算生产数量 |
| 18 | fworkwastreportprodqty | 已汇报工废生产数量 | numeric | 23 | 10 | √ | 0 | 已汇报工废生产数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_outreceiveentry_c |  | fentryid |
| 2 | idx_sfc_outreceiveentry_c_id |  | fid |

---

## 接收明细-分表 t_sfc_outreceiveentry_a

- **表名称：** 接收明细-分表
- **表名：** t_sfc_outreceiveentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finspectqty | 检验数量 | numeric | 23 | 10 | √ | 0 | 检验数量 |
| 3 | flinksettlewwproqty | 关联结算工废生产数量 | numeric | 23 | 10 | √ | 0 | 关联结算工废生产数量 |
| 4 | fsettlewwqty | 结算工废数量 | numeric | 23 | 10 | √ | 0 | 结算工废数量 |
| 5 | fsettlequaqty | 结算合格数量 | numeric | 23 | 10 | √ | 0 | 结算合格数量 |
| 6 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 7 | flinksettleswproqty | 关联结算料废生产数量 | numeric | 23 | 10 | √ | 0 | 关联结算料废生产数量 |
| 8 | fsettleswbaseqty | 结算料废基本数量 | numeric | 23 | 10 | √ | 0 | 结算料废基本数量 |
| 9 | fsettleswqty | 结算料废数量 | numeric | 23 | 10 | √ | 0 | 结算料废数量 |
| 10 | flinkinspectqty | 关联检验数量 | numeric | 23 | 10 | √ | 0 | 关联检验数量 |
| 11 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | finspectplan | 检验方案(废弃) | int8 | 64 |  | √ | 0 | [工作中心 sfc_workcenter](../mpdm_files/sfc_workcenter.md) |
| 13 | finspectplanrowid | 检验方案分录id | int8 | 64 |  | √ | 0 | 检验方案分录id |
| 14 | flinkinbaseqty | 基本关联检验数量 | numeric | 23 | 10 | √ | 0 | 基本关联检验数量 |
| 15 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 16 | fsettlequabaseqty | 结算合格基本数量 | numeric | 23 | 10 | √ | 0 | 结算合格基本数量 |
| 17 | flinksettlequaqty | 关联结算合格数量 | numeric | 23 | 10 | √ | 0 | 关联结算合格数量 |
| 18 | fsettlewwproqty | 结算工废生产数量 | numeric | 23 | 10 | √ | 0 | 结算工废生产数量 |
| 19 | fsettleswproqty | 结算料废生产数量 | numeric | 23 | 10 | √ | 0 | 结算料废生产数量 |
| 20 | fsettlequaproqty | 结算合格生产数量 | numeric | 23 | 10 | √ | 0 | 结算合格生产数量 |
| 21 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 22 | fproinspect | 工序检验 | bpchar | 1 |  | √ | '0' | 工序检验 |
| 23 | finspectbaseqty | 基本检验数量 | numeric | 23 | 10 | √ | 0 | 基本检验数量 |
| 24 | finspectschemeid | 检验方案编码 | int8 | 64 |  | √ | 0 | [检验方案 qcbd_inspectpro](../qcbd_files/qcbd_inspectpro.md) |
| 25 | finspectcompletedate | 期望检验完成日期 | timestamp | 0 |  |  | null | 期望检验完成日期 |
| 26 | flinksettlewwbaseqty | 关联结算工废基本数量 | numeric | 23 | 10 | √ | 0 | 关联结算工废基本数量 |
| 27 | flinksettlebasequaqty | 关联结算合格基本数量 | numeric | 23 | 10 | √ | 0 | 关联结算合格基本数量 |
| 28 | fisgenprocessreview | 已生成工序汇报单 | bpchar | 1 |  | √ | '0' | 已生成工序汇报单 |
| 29 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 30 | flinksettleproquaqty | 关联结算合格生产数量 | numeric | 23 | 10 | √ | 0 | 关联结算合格生产数量 |
| 31 | flinksettleswbaseqty | 关联结算料废基本数量 | numeric | 23 | 10 | √ | 0 | 关联结算料废基本数量 |
| 32 | finspectuserid | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | flinksettlewwqty | 关联结算工废数量 | numeric | 23 | 10 | √ | 0 | 关联结算工废数量 |
| 34 | finspectdepid | 质检部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fisurgent | 加急 | bpchar | 1 |  | √ | '0' | 加急 |
| 36 | finspectorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 37 | flinksettleswqty | 关联结算料废数量 | numeric | 23 | 10 | √ | 0 | 关联结算料废数量 |
| 38 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 39 | fsettlewwbaseqty | 结算工废基本数量 | numeric | 23 | 10 | √ | 0 | 结算工废基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_outreceiveentry_a |  | fentryid |
| 2 | idx_sfc_outreceiveentry_a_id |  | fid |

---

## 委外接收单-反写记录表 t_sfc_outreceive_wb

- **表名称：** 委外接收单-反写记录表
- **表名：** t_sfc_outreceive_wb

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
| 1 | idx_sfc_outreceive_wb_fk |  | fid |
| 2 | pk_sfc_outreceive_wb |  | fentryid |

---

## 关联子实体-子表 t_sfc_outreceiveentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_outreceiveentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | freceiveqty | 接收数量_确认携带值 | numeric | 23 | 10 |  | null | 接收数量_确认携带值 |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | freceiveqty_old | 接收数量_原始携带值 | numeric | 23 | 10 |  | null | 接收数量_原始携带值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 8 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_outreceiveentry_lk_fk |  | fentryid |
| 2 | pk_sfc_outreceiveentry_lk |  | fpkid |

---

## 委外接收单-主表 t_sfc_outreceive

- **表名称：** 委外接收单-主表
- **表名：** t_sfc_outreceive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 加工组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdepartid | 加工车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fdate | 接收日期 | timestamp | 0 |  |  | null | 接收日期 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fpostdate | 记账日期 | timestamp | 0 |  |  | null | 记账日期 |
| 17 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_outreceive_billno |  | fbillno |
| 2 | pk_sfc_outreceive |  | fid |
