# 内协接收单-sfc_insideaccept

## 内协接收单-主表 t_sfc_insideaccept

- **表名称：** 内协接收单-主表
- **表名：** t_sfc_insideaccept

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fdepartid | 生产车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fprocessorgid | 加工组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 12 | fprocessdepartid | 加工车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
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
| 2 | fproplanid | 工序计划 | int8 | 64 |  | √ | 0 | [工序计划F7 sfc_processplan_f7](../sfc_files/sfc_processplan_f7.md) |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 4 | fsbillentity | 来源单据实体 | varchar | 50 |  | √ | ' ' | 来源单据实体 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 7 | fsampledestoryproqty | 样本破坏生产数量 | numeric | 23 | 10 | √ | 0 | 样本破坏生产数量 |
| 8 | fsbilltypeid | 来源单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 9 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 10 | fworkid | 生产工单号 | int8 | 64 |  | √ | 0 | 生产工单 pom_mftorder |
| 11 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 12 | fworkrowid | 工单分录id | int8 | 64 |  | √ | 0 | [生产工单分录F7 sfc_mftorder_f7](../sfc_files/sfc_mftorder_f7.md) |
| 13 | fcorebilltypeid | 核心单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 14 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 15 | fsbillrow | 来源单据行号 | int4 | 32 |  | √ | 0 | 来源单据行号 |
| 16 | fsourcebillrowid | 来源单据行id | int8 | 64 |  | √ | 0 | 来源单据行id |
| 17 | fcorebillrow | 核心单据行号 | int4 | 32 |  | √ | 0 | 核心单据行号 |
| 18 | fbaseunitid | 产品基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fcreatesend | 已生成连续内协发出单 | bpchar | 1 |  | √ | '0' | 已生成连续内协发出单 |
| 20 | finsendid | 连续内协关联发出单id | varchar | 50 |  | √ | ' ' | 连续内协关联发出单id |
| 21 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 22 | fcorebillid | 核心单据id | int8 | 64 |  | √ | 0 | 核心单据id |
| 23 | fbackflishflag | 倒冲标识 | varchar | 10 |  | √ | ' ' | 倒冲标识,枚举: not :未倒冲 sucess :倒冲成功 part :部分倒冲 |
| 24 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 25 | flicensenoid | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 26 | fcorebillnumber | 核心单据编号 | varchar | 100 |  | √ | ' ' | 核心单据编号 |
| 27 | fsampledestoryqty | 样本破坏数量 | numeric | 23 | 10 | √ | 0 | 样本破坏数量 |
| 28 | fcorebillentity | 核心单据实体 | varchar | 50 |  | √ | ' ' | 核心单据实体 |
| 29 | fproducttype | 产品类型 | bpchar | 1 |  | √ | ' ' | 产品类型,枚举: C :主产品 A :联产品 B :副产品 |
| 30 | fproplanentryid | 工序计划分录 | int8 | 64 |  | √ | 0 | [工序计划分录F7 sfc_processplanentry_f7](../sfc_files/sfc_processplanentry_f7.md) |
| 31 | fisdevproduce | 研发试制 | bpchar | 1 |  | √ | '0' | 研发试制 |
| 32 | fsampledestorybaseqty | 样本破坏基本数量 | numeric | 23 | 10 | √ | 0 | 样本破坏基本数量 |
| 33 | fisgenprocessreview | 已生成工序汇报单 | bpchar | 1 |  | √ | '0' | 已生成工序汇报单 |
| 34 | fsourcebillnumber | 来源单据编号 | varchar | 100 |  | √ | ' ' | 来源单据编号 |
| 35 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 36 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 37 | fproplanbillid | 工序计划号 | int8 | 64 |  | √ | 0 | 工序计划 sfc_processplanbill |
| 38 | fentryremark | 备注 | varchar | 1000 |  | √ | ' ' | 备注 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fcorebillrowid | 核心单据行id | int8 | 64 |  | √ | 0 | 核心单据行id |
| 41 | fprocessunitid | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

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
| 8 | finspectschemeid | 检验方案编码 | int8 | 64 |  | √ | 0 | [检验方案 qcbd_inspectpro](../qcbd_files/qcbd_inspectpro.md) |
| 9 | finsettlepushqty | 关联内协结算数量 | numeric | 23 | 10 | √ | 0 | 关联内协结算数量 |
| 10 | finsettlebaseqty | 内协结算基本数量 | numeric | 23 | 10 | √ | 0 | 内协结算基本数量 |
| 11 | finspectcompletedate | 期望检验完成日期 | timestamp | 0 |  |  | null | 期望检验完成日期 |
| 12 | finsettleprodqty | 内协结算生产数量 | numeric | 23 | 10 | √ | 0 | 内协结算生产数量 |
| 13 | flinkinspectqty | 关联检验数量 | numeric | 23 | 10 | √ | 0 | 关联检验数量 |
| 14 | finspectuserid | 质检员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | finspectplanrowid | 检验方案分录id | int8 | 64 |  | √ | 0 | 检验方案分录id |
| 16 | flinkinbaseqty | 基本关联检验数量 | numeric | 23 | 10 | √ | 0 | 基本关联检验数量 |
| 17 | finsettlepushprodqty | 关联内协结算生产数量 | numeric | 23 | 10 | √ | 0 | 关联内协结算生产数量 |
| 18 | finspectdepid | 质检部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fisurgent | 加急 | bpchar | 1 |  | √ | '0' | 加急 |
| 20 | finspectorg | 质检组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 22 | finsettleqty | 内协结算数量 | numeric | 23 | 10 | √ | 0 | 内协结算数量 |

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
