# 委外接收单-sfc_outreceive

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
| 5 | fsbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 6 | fbasereceiveqty | 接收基本数量 | numeric | 23 | 10 | √ | 0 | 接收基本数量 |
| 7 | fworkrowid | 工单分录id | int8 | 64 |  | √ | 0 | 生产工单分录F7 sfc_mftorder_f7 |
| 8 | fquaqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 9 | fcorebilltypeid | 核心单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 10 | fworkwastbaseqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 11 | fcorebillrow | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 12 | fbaseunitid | 产品基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fstockwastqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 14 | fbasequaqtyreport | 已汇报合格基本数量 | numeric | 23 | 10 | √ | 0 | 已汇报合格基本数量 |
| 15 | fsecquabaseqty | 联副产品合格基本数量(废弃) | numeric | 23 | 10 | √ | 0 | 联副产品合格基本数量(废弃) |
| 16 | fbaseworkwastqtyreport | 已汇报工废基本数量 | numeric | 23 | 10 | √ | 0 | 已汇报工废基本数量 |
| 17 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 18 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 19 | fyieldreceiveqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 20 | fcorebillnumber | 核心单据编号 | varchar | 100 |  | √ | ' ' | 核心单据编号 |
| 21 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 22 | freworkqty | 退回返工数量 | numeric | 23 | 10 | √ | 0 | 退回返工数量 |
| 23 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 24 | fcorebillrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 25 | fproplanid | 工序计划 | int8 | 64 |  | √ | 0 | 工序计划F7 sfc_processplan_f7 |
| 26 | freceiveqty | 接收数量 | numeric | 23 | 10 | √ | 0 | 接收数量 |
| 27 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 28 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 29 | fworkwastqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 30 | fsecworkwastbaseqty | 联副产品工废基本数量 | numeric | 23 | 10 | √ | 0 | 联副产品工废基本数量 |
| 31 | fworkid | 生产工单 | int8 | 64 |  | √ | 0 | 生产工单 pom_mftorder |
| 32 | fbaseyieldrecqtyreport | 已汇报让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 已汇报让步接收基本数量 |
| 33 | fsbillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 34 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 35 | fworkwastqtyreport | 已汇报工废数量 | numeric | 23 | 10 | √ | 0 | 已汇报工废数量 |
| 36 | fbaseyieldreceiveqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 37 | fbasereworkqty | 退回返工基本数量 | numeric | 23 | 10 | √ | 0 | 退回返工基本数量 |
| 38 | fquaqtyreport | 已汇报合格数量 | numeric | 23 | 10 | √ | 0 | 已汇报合格数量 |
| 39 | fyieldrecqtyreport | 已汇报让步接收数量 | numeric | 23 | 10 | √ | 0 | 已汇报让步接收数量 |
| 40 | fstockwastqtyreport | 已汇报料废数量 | numeric | 23 | 10 | √ | 0 | 已汇报料废数量 |
| 41 | fsecstockwastbaseqty | 联副产品料废基本数量 | numeric | 23 | 10 | √ | 0 | 联副产品料废基本数量 |
| 42 | fproducttype | 产品类型 | bpchar | 1 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 43 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | 工序计划分录F7 sfc_processplanentry_f7 |
| 44 | fsourcebillnumber | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 45 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 46 | freceiveqtyback | 接收数量（后台） | numeric | 23 | 10 | √ | 0 | 接收数量（后台） |
| 47 | fproplanbillid | 工序计划号 | int8 | 64 |  | √ | 0 | 工序计划 sfc_processplanbill |
| 48 | fbasestockwastqtyreport | 已汇报料废基本数量 | numeric | 23 | 10 | √ | 0 | 已汇报料废基本数量 |
| 49 | fplanendtime | 计划接收日期(废弃) | timestamp | 0 |  |  | null | 计划接收日期(废弃) |
| 50 | fprocessunitid | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

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

## 接收明细-分表 t_sfc_outreceiveentry_b

- **表名称：** 接收明细-分表
- **表名：** t_sfc_outreceiveentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutsettleqty | 委外结算数量 | numeric | 23 | 10 | √ | 0 | 委外结算数量 |
| 3 | foutsendid | 连续委外关联发出单id | varchar | 50 |  | √ | ' ' | 连续委外关联发出单id |
| 4 | foutsettlepushqty | 关联委外结算数量 | numeric | 23 | 10 | √ | 0 | 关联委外结算数量 |
| 5 | foutsettlebaseqty | 委外结算基本数量 | numeric | 23 | 10 | √ | 0 | 委外结算基本数量 |
| 6 | fcreatesend | 已生成连续委外发出单 | bpchar | 1 |  | √ | '0' | 已生成连续委外发出单 |
| 7 | foutsettlepushbaseqty | 关联委外结算基本数量 | numeric | 23 | 10 | √ | 0 | 关联委外结算基本数量 |
| 8 | foutsourcepriceandtax | 含税单价 | numeric | 23 | 10 | √ | 0 | 含税单价 |
| 9 | fworkwasteprice | 工废单价 | numeric | 23 | 10 | √ | 0 | 工废单价 |
| 10 | fchargeunitid | 计价单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 11 | fscrapwasteprice | 料废单价 | numeric | 23 | 10 | √ | 0 | 料废单价 |
| 12 | fworkwastepriceandtax | 工废含税单价 | numeric | 23 | 10 | √ | 0 | 工废含税单价 |
| 13 | ftaxrateid | 税率 | int8 | 64 |  | √ | 0 | 税率 bd_taxrate |
| 14 | fscrapwastepriceandtax | 料废含税单价 | numeric | 23 | 10 | √ | 0 | 料废含税单价 |
| 15 | foutsourceprice | 单价 | numeric | 23 | 10 | √ | 0 | 单价 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 17 | fcurrencyid | 币别 | int8 | 64 |  | √ | 0 | 币种 bd_currency |

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
| 6 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 7 | flinksettleswproqty | 关联结算料废生产数量 | numeric | 23 | 10 | √ | 0 | 关联结算料废生产数量 |
| 8 | fsettleswbaseqty | 结算料废基本数量 | numeric | 23 | 10 | √ | 0 | 结算料废基本数量 |
| 9 | fsettleswqty | 结算料废数量 | numeric | 23 | 10 | √ | 0 | 结算料废数量 |
| 10 | flinkinspectqty | 关联检验数量 | numeric | 23 | 10 | √ | 0 | 关联检验数量 |
| 11 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | finspectplan | 检验方案(废弃) | int8 | 64 |  | √ | 0 | 工作中心 sfc_workcenter |
| 13 | flinkinbaseqty | 基本关联检验数量 | numeric | 23 | 10 | √ | 0 | 基本关联检验数量 |
| 14 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 15 | fsettlequabaseqty | 结算合格基本数量 | numeric | 23 | 10 | √ | 0 | 结算合格基本数量 |
| 16 | flinksettlequaqty | 关联结算合格数量 | numeric | 23 | 10 | √ | 0 | 关联结算合格数量 |
| 17 | fsettlewwproqty | 结算工废生产数量 | numeric | 23 | 10 | √ | 0 | 结算工废生产数量 |
| 18 | fsettleswproqty | 结算料废生产数量 | numeric | 23 | 10 | √ | 0 | 结算料废生产数量 |
| 19 | fsettlequaproqty | 结算合格生产数量 | numeric | 23 | 10 | √ | 0 | 结算合格生产数量 |
| 20 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 21 | fproinspect | 工序检验 | bpchar | 1 |  | √ | '0' | 工序检验 |
| 22 | finspectbaseqty | 基本检验数量 | numeric | 23 | 10 | √ | 0 | 基本检验数量 |
| 23 | flinksettlewwbaseqty | 关联结算工废基本数量 | numeric | 23 | 10 | √ | 0 | 关联结算工废基本数量 |
| 24 | flinksettlebasequaqty | 关联结算合格基本数量 | numeric | 23 | 10 | √ | 0 | 关联结算合格基本数量 |
| 25 | fisgenprocessreview | 已生成工序汇报单 | bpchar | 1 |  | √ | '0' | 已生成工序汇报单 |
| 26 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 27 | flinksettleproquaqty | 关联结算合格生产数量 | numeric | 23 | 10 | √ | 0 | 关联结算合格生产数量 |
| 28 | flinksettleswbaseqty | 关联结算料废基本数量 | numeric | 23 | 10 | √ | 0 | 关联结算料废基本数量 |
| 29 | finspectuserid | 质检员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 30 | flinksettlewwqty | 关联结算工废数量 | numeric | 23 | 10 | √ | 0 | 关联结算工废数量 |
| 31 | finspectdepid | 质检部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 32 | finspectorg | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 33 | flinksettleswqty | 关联结算料废数量 | numeric | 23 | 10 | √ | 0 | 关联结算料废数量 |
| 34 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 35 | fsettlewwbaseqty | 结算工废基本数量 | numeric | 23 | 10 | √ | 0 | 结算工废基本数量 |

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
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpurorgid | 采购组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdepartid | 加工车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fdate | 接收日期 | timestamp | 0 |  |  | null | 接收日期 |
| 13 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sfc_outreceive_billno |  | fbillno |
| 2 | pk_sfc_outreceive |  | fid |
