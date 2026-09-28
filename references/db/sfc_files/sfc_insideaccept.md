# 内协接收单-sfc_insideaccept

## 内协接收单-主表 t_sfc_insideaccept

- **表名称：** 内协接收单-主表
- **表名：** t_sfc_insideaccept

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fprocessorgid | 加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fprocessdepartid | 加工车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | fdate | 接收日期 | timestamp | 0 |  |  | null | 接收日期 |
| 14 | fbillno | 单据编号 | varchar | 80 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_insideaccept |  | fid |
| 2 | idx_sfc_insideaccept_billno |  | fbillno |

---

## 接收明细-子表 t_sfc_insideacceptentry

- **表名称：** 接收明细-子表
- **表名：** t_sfc_insideacceptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fproplanid | 工序计划 | int8 | 64 |  | √ | 0 | 工序计划F7 sfc_processplan_f7 |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 4 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 7 | fsbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 8 | fworkid | 生产工单号 | int8 | 64 |  | √ | 0 | 生产工单 pom_mftorder |
| 9 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 10 | fworkrowid | 工单分录id | int8 | 64 |  | √ | 0 | 生产工单分录F7 sfc_mftorder_f7 |
| 11 | fcorebilltypeid | 核心单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |
| 12 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 bd_tracknumber |
| 13 | fsbillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 14 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 15 | fcorebillrow | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 16 | fbaseunitid | 产品基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fcreatesend | 已生成连续内协发出单 | bpchar | 1 |  | √ | '0' | 已生成连续内协发出单 |
| 18 | finsendid | 连续内协关联发出单id | varchar | 50 |  | √ | ' ' | 连续内协关联发出单id |
| 19 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 20 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 21 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 22 | fcorebillnumber | 核心单据编号 | varchar | 100 |  | √ | ' ' | 核心单据编号 |
| 23 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 24 | fproducttype | 产品类型 | bpchar | 1 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 25 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | 工序计划分录F7 sfc_processplanentry_f7 |
| 26 | fisgenprocessreview | 已生成工序汇报单 | bpchar | 1 |  | √ | '0' | 已生成工序汇报单 |
| 27 | fsourcebillnumber | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 28 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | 批号主档 bd_lot |
| 29 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 30 | fproplanbillid | 工序计划号 | int8 | 64 |  | √ | 0 | 工序计划 sfc_processplanbill |
| 31 | fentryremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fcorebillrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 34 | fprocessunitid | 工序单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_insideacceptentry |  | fentryid |
| 2 | idx_sfc_insideacceptentry_fid |  | fid |

---

## 接收明细-分表 t_sfc_insideacceptentry_b

- **表名称：** 接收明细-分表
- **表名：** t_sfc_insideacceptentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | freceiveqty | 接收数量 | numeric | 23 | 10 | √ | 0 | 接收数量 |
| 3 | fquabaseqty | 合格基本数量 | numeric | 23 | 10 | √ | 0 | 合格基本数量 |
| 4 | fstockwastbaseqty | 料废基本数量 | numeric | 23 | 10 | √ | 0 | 料废基本数量 |
| 5 | fworkwastqty | 工废数量 | numeric | 23 | 10 | √ | 0 | 工废数量 |
| 6 | fworkwastprodqty | 工废生产数量 | numeric | 23 | 10 | √ | 0 | 工废生产数量 |
| 7 | freworkprodqty | 退回返工生产数量 | numeric | 23 | 10 | √ | 0 | 退回返工生产数量 |
| 8 | fsecstockwastprodqty | 联副产品料废生产数量 | numeric | 23 | 10 | √ | 0 | 联副产品料废生产数量 |
| 9 | fsecworkwastbaseqty | 联副产品工废基本数量 | numeric | 23 | 10 | √ | 0 | 联副产品工废基本数量 |
| 10 | fstockwastreportprodqty | 已汇报料废生产数量 | numeric | 23 | 10 | √ | 0 | 已汇报料废生产数量 |
| 11 | fbasereceiveqty | 接收基本数量 | numeric | 23 | 10 | √ | 0 | 接收基本数量 |
| 12 | fquaqty | 合格数量 | numeric | 23 | 10 | √ | 0 | 合格数量 |
| 13 | fquareportprodqty | 已汇报合格生产数量 | numeric | 23 | 10 | √ | 0 | 已汇报合格生产数量 |
| 14 | fworkwastbaseqty | 工废基本数量 | numeric | 23 | 10 | √ | 0 | 工废基本数量 |
| 15 | fbaseyieldrecqtyreport | 已汇报让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 已汇报让步接收基本数量 |
| 16 | fproducereceiveqty | 接收生产数量 | numeric | 23 | 10 | √ | 0 | 接收生产数量 |
| 17 | fworkwastqtyreport | 已汇报工废数量 | numeric | 23 | 10 | √ | 0 | 已汇报工废数量 |
| 18 | fstockwastqty | 料废数量 | numeric | 23 | 10 | √ | 0 | 料废数量 |
| 19 | fbaseyieldreceiveqty | 让步接收基本数量 | numeric | 23 | 10 | √ | 0 | 让步接收基本数量 |
| 20 | fbasereworkqty | 退回返工基本数量 | numeric | 23 | 10 | √ | 0 | 退回返工基本数量 |
| 21 | fbasequaqtyreport | 已汇报合格基本数量 | numeric | 23 | 10 | √ | 0 | 已汇报合格基本数量 |
| 22 | fquaqtyreport | 已汇报合格数量 | numeric | 23 | 10 | √ | 0 | 已汇报合格数量 |
| 23 | fyieldrecreportprodqty | 已汇报让步接收生产数量 | numeric | 23 | 10 | √ | 0 | 已汇报让步接收生产数量 |
| 24 | fbaseworkwastqtyreport | 已汇报工废基本数量 | numeric | 23 | 10 | √ | 0 | 已汇报工废基本数量 |
| 25 | fyieldrecqtyreport | 已汇报让步接收数量 | numeric | 23 | 10 | √ | 0 | 已汇报让步接收数量 |
| 26 | fyieldreceiveqty | 让步接收数量 | numeric | 23 | 10 | √ | 0 | 让步接收数量 |
| 27 | fstockwastqtyreport | 已汇报料废数量 | numeric | 23 | 10 | √ | 0 | 已汇报料废数量 |
| 28 | fsecworkwastprodqty | 联副产品工废生产数量 | numeric | 23 | 10 | √ | 0 | 联副产品工废生产数量 |
| 29 | fstockwastprodqty | 料废生产数量 | numeric | 23 | 10 | √ | 0 | 料废生产数量 |
| 30 | fsecstockwastbaseqty | 联副产品料废基本数量 | numeric | 23 | 10 | √ | 0 | 联副产品料废基本数量 |
| 31 | fyieldreceiveprodqty | 让步接收生产数量 | numeric | 23 | 10 | √ | 0 | 让步接收生产数量 |
| 32 | fquaproduceqty | 合格生产数量 | numeric | 23 | 10 | √ | 0 | 合格生产数量 |
| 33 | freworkqty | 退回返工数量 | numeric | 23 | 10 | √ | 0 | 退回返工数量 |
| 34 | freceiveqtyback | 接收数量（后台） | numeric | 23 | 10 | √ | 0 | 接收数量（后台） |
| 35 | fbasestockwastqtyreport | 已汇报料废基本数量 | numeric | 23 | 10 | √ | 0 | 已汇报料废基本数量 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 37 | fworkwastreportprodqty | 已汇报工废生产数量 | numeric | 23 | 10 | √ | 0 | 已汇报工废生产数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_insideacceptentry_b |  | fentryid |
| 2 | idx_sfc_insideaptentry_b_id |  | fid |

---

## 接收明细-分表 t_sfc_insideacceptentry_a

- **表名称：** 接收明细-分表
- **表名：** t_sfc_insideacceptentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | finsettlepushbaseqty | 关联内协结算基本数量 | numeric | 23 | 10 | √ | 0 | 关联内协结算基本数量 |
| 3 | finspectqty | 检验数量 | numeric | 23 | 10 | √ | 0 | 检验数量 |
| 4 | flinkinprodqty | 关联检验生产数量 | numeric | 23 | 10 | √ | 0 | 关联检验生产数量 |
| 5 | finspectprodqty | 检验生产数量 | numeric | 23 | 10 | √ | 0 | 检验生产数量 |
| 6 | fproinspect | 工序检验 | bpchar | 1 |  | √ | '0' | 工序检验 |
| 7 | finspectbaseqty | 基本检验数量 | numeric | 23 | 10 | √ | 0 | 基本检验数量 |
| 8 | finsettlepushqty | 关联内协结算数量 | numeric | 23 | 10 | √ | 0 | 关联内协结算数量 |
| 9 | finsettlebaseqty | 内协结算基本数量 | numeric | 23 | 10 | √ | 0 | 内协结算基本数量 |
| 10 | finsettleprodqty | 内协结算生产数量 | numeric | 23 | 10 | √ | 0 | 内协结算生产数量 |
| 11 | flinkinspectqty | 关联检验数量 | numeric | 23 | 10 | √ | 0 | 关联检验数量 |
| 12 | finspectuserid | 质检员 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | flinkinbaseqty | 基本关联检验数量 | numeric | 23 | 10 | √ | 0 | 基本关联检验数量 |
| 14 | finsettlepushprodqty | 关联内协结算生产数量 | numeric | 23 | 10 | √ | 0 | 关联内协结算生产数量 |
| 15 | finspectdepid | 质检部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | finspectorg | 质检组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 18 | finsettleqty | 内协结算数量 | numeric | 23 | 10 | √ | 0 | 内协结算数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_insideacceptentry_a |  | fentryid |
| 2 | idx_sfc_insideaptentry_a_id |  | fid |

---

## 内协接收单-反写记录表 t_sfc_insideaccept_wb

- **表名称：** 内协接收单-反写记录表
- **表名：** t_sfc_insideaccept_wb

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
| 1 | pk_sfc_insideaccept_wb |  | fentryid |
| 2 | idx_sfc_insideaccept_wb_fk |  | fid |

---

## 接收明细-多语言表 t_sfc_insideacceptentry_l

- **表名称：** 接收明细-多语言表
- **表名：** t_sfc_insideacceptentry_l

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
| 1 | idx_sfc_insideaptentry_l_id |  | fentryid,flocaleid |
| 2 | pk_sfc_insideacceptentry_l |  | fpkid |

---

## 内协接收单-多语言表 t_sfc_insideaccept_l

- **表名称：** 内协接收单-多语言表
- **表名：** t_sfc_insideaccept_l

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
| 1 | pk_sfc_insideaccept_l |  | fpkid |
| 2 | idx_sfc_insideaccept_l_id |  | fid,flocaleid |

---

## 内协接收单-关联追踪表 t_sfc_insideaccept_tc

- **表名称：** 内协接收单-关联追踪表
- **表名：** t_sfc_insideaccept_tc

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
| 1 | idx_sfc_insideaccept_tc_tid |  | ftid |
| 2 | pk_sfc_insideaccept_tc |  | fid |
| 3 | idx_sfc_insideaccept_tc_tbill |  | ftbillid |

---

## 关联子实体-子表 t_sfc_insideacceptentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_sfc_insideacceptentry_lk

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
| 1 | idx_sfc_insideacceptentry_lk_fk |  | fentryid |
| 2 | pk_sfc_insideacceptentry_lk |  | fpkid |
