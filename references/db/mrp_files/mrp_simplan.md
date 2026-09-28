# 计划模拟-mrp_simplan

## 预留明细-子表 t_mrp_simreserveentry

- **表名称：** 预留明细-子表
- **表名：** t_mrp_simreserveentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbillobjid | 单据名称 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 3 | fmaterialid | 物料主档内码 | int8 | 64 |  | √ | 0 | 物料主档内码 |
| 4 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 |
| 5 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | 辅助属性 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fbillentryseq | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 8 | flongestpath | 最长路径 | bpchar | 1 |  | √ | '0' | 最长路径 |
| 9 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务组织 |
| 10 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | 跟踪号 |
| 11 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 基本单位 |
| 13 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 14 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 15 | fpromisedate | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 16 | fsimplandetailid | 模拟详情分录内码 | int8 | 64 |  | √ | 0 | 模拟详情分录内码 |
| 17 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | 项目编码 |
| 18 | fbegindate | 开工日期 | timestamp | 0 |  |  | null | 开工日期 |
| 19 | fdatediffsum | 差值提前期累计 | int4 | 32 |  | √ | 0 | 差值提前期累计 |
| 20 | freserveqty | 基本单位预留数量 | numeric | 23 | 10 | √ | 0 | 基本单位预留数量 |
| 21 | frootbillentryid | 根需求单据分录内码 | int8 | 64 |  | √ | 0 | 根需求单据分录内码 |
| 22 | fdeliverydate | 最早交货日期 | timestamp | 0 |  |  | null | 最早交货日期 |
| 23 | ffinishdate | 完工日期 | timestamp | 0 |  |  | null | 完工日期 |
| 24 | flevel | 层级 | int8 | 64 |  | √ | 0 | 层级 |
| 25 | fbillentryid | 需求单据分录内码 | int8 | 64 |  | √ | 0 | 需求单据分录内码 |
| 26 | fbillid | 需求单据内码 | int8 | 64 |  | √ | 0 | 需求单据内码 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fdatediff | 差值提前期 | int4 | 32 |  | √ | 0 | 差值提前期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_simreserveentry |  | fentryid |
| 2 | idx_mrp_simreserveentry_fid |  | fid |

---

## 模拟详情-子表 t_mrp_simplandetail

- **表名称：** 模拟详情-子表
- **表名：** t_mrp_simplandetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequireqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 4 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fbillentryseq | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 7 | flongestpath | 最长路径 | bpchar | 1 |  | √ | '0' | 最长路径 |
| 8 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务组织 |
| 9 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 10 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 11 | fpurapplyqty | 采购申请 | numeric | 23 | 10 | √ | 0 | 采购申请 |
| 12 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 13 | fsimplorderqty | 模拟计划订单 | numeric | 23 | 10 | √ | 0 | 模拟计划订单 |
| 14 | fsimroqty | 模拟组织间需求单 | numeric | 23 | 10 | √ | 0 | 模拟组织间需求单 |
| 15 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 16 | fpromisedate | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 17 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 18 | fmaterialarr | 物料属性 | varchar | 30 |  | √ | ' ' | 物料属性,枚举: 10020 :虚拟 10030 :自制 10040 :外购 10050 :委外 |
| 19 | fbegindate | 建议采购/生产日期 | timestamp | 0 |  |  | null | 建议采购/生产日期 |
| 20 | finvqty | 库存 | numeric | 23 | 10 | √ | 0 | 库存 |
| 21 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fpomqty | 生产工单 | numeric | 23 | 10 | √ | 0 | 生产工单 |
| 23 | fsupplyqty | 供应数量 | numeric | 23 | 10 | √ | 0 | 供应数量 |
| 24 | ffinishdate | 建议到货/完工日期 | timestamp | 0 |  |  | null | 建议到货/完工日期 |
| 25 | fomqty | 委外工单 | numeric | 23 | 10 | √ | 0 | 委外工单 |
| 26 | flevel | 层级 | int8 | 64 |  | √ | 0 | 层级 |
| 27 | fbillentryid | 单据分录内码 | int8 | 64 |  | √ | 0 | 单据分录内码 |
| 28 | fbillid | 单据内码 | int8 | 64 |  | √ | 0 | 单据内码 |
| 29 | fotherqty | 其他 | numeric | 23 | 10 | √ | 0 | 其他 |
| 30 | fplorderqty | 计划订单 | numeric | 23 | 10 | √ | 0 | 计划订单 |
| 31 | froqty | 组织间需求单 | numeric | 23 | 10 | √ | 0 | 组织间需求单 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 33 | fpurorderqty | 采购订单 | numeric | 23 | 10 | √ | 0 | 采购订单 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_simplandetail_fid |  | fid |
| 2 | pk_mrp_simplandetail |  | fentryid |

---

## 模拟概要-子表 t_mrp_simplanentry

- **表名称：** 模拟概要-子表
- **表名：** t_mrp_simplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | frequiredate | 需求日期 | timestamp | 0 |  |  | null | 需求日期 |
| 3 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料销售信息 bd_materialsalinfo](../sbd_files/bd_materialsalinfo.md) |
| 4 | fbaseinvqty | 基本单位库存可交数量 | numeric | 23 | 10 | √ | 0 | 基本单位库存可交数量 |
| 5 | fmatverid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdemandbillentryid | 需求单据分录内码 | int8 | 64 |  | √ | 0 | 需求单据分录内码 |
| 9 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 10 | fsourcetype | 来源 | bpchar | 1 |  | √ | 'B' | 来源,枚举: A :选单 B :手工 |
| 11 | fdemandbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 12 | fwayqty | 可交数量 | numeric | 23 | 10 | √ | 0 | 可交数量 |
| 13 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 14 | fdemandbillentryseq | 行号 | int4 | 32 |  | √ | 0 | 行号 |
| 15 | frequiretypeid | 需求类型 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fbasewayqty | 基本单位可交数量 | numeric | 23 | 10 | √ | 0 | 基本单位可交数量 |
| 17 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 19 | fpromisedate | 承诺日期 | timestamp | 0 |  |  | null | 承诺日期 |
| 20 | fprojectid | 项目编码 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 21 | finvqty | 库存可交数量 | numeric | 23 | 10 | √ | 0 | 库存可交数量 |
| 22 | funitid | 单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 23 | frequireorgid | 需求组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 24 | fdeliverydate | 最早交货日期 | timestamp | 0 |  |  | null | 最早交货日期 |
| 25 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 26 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 28 | fstockorgid | 发货组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 29 | fcustomerid | 客户 | int8 | 64 |  | √ | 0 | [客户 bd_customer](../basedata_files/bd_customer.md) |
| 30 | fbilltypeid | 单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 31 | fdemandbillid | 需求单据内码 | int8 | 64 |  | √ | 0 | 需求单据内码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_simplanentry_fid |  | fid |
| 2 | pk_mrp_simplanentry |  | fentryid |

---

## 计划模拟-主表 t_mrp_simplan

- **表名称：** 计划模拟-主表
- **表名：** t_mrp_simplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fplanschemeid | 模拟方案 | int8 | 64 |  | √ | 0 | [计划方案 mrp_planscheme](../msplan_files/mrp_planscheme.md) |
| 4 | fretentiondays | 保留天数 | int4 | 32 |  | √ | 0 | 保留天数 |
| 5 | fsimulationuserid | 模拟人员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | frunlogid | 运算编号 | int8 | 64 |  | √ | 0 | [计划模拟运算日志 mrp_simcaculate_log](../msplan_files/mrp_simcaculate_log.md) |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | forgid | 计划组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 11 | fclosedate | 关闭时间 | timestamp | 0 |  |  | null | 关闭时间 |
| 12 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 13 | fsimulationstatus | 模拟状态 | bpchar | 1 |  | √ | 'A' | 模拟状态,枚举: A :未模拟 B :已模拟 C :已转正 D :已过期 |
| 14 | fsimstartdate | 模拟启动时间 | timestamp | 0 |  |  | null | 模拟启动时间 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fclosestatus | 关闭状态 | bpchar | 1 |  | √ | 'B' | 关闭状态,枚举: A :正常 B :关闭 |
| 17 | fcloseuserid | 关闭人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fsimenddate | 模拟截止日期 | timestamp | 0 |  |  | null | 模拟截止日期 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fbillno | 模拟编号 | varchar | 30 |  | √ | ' ' | 模拟编号 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mrp_simplan |  | fid |
| 2 | idx_mrp_simplan_fbillno |  | fbillno |
