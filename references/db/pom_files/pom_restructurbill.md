# 改制申请单-pom_restructurbill

## 改制申请单-关联追踪表 t_pom_restructurbill_tc

- **表名称：** 改制申请单-关联追踪表
- **表名：** t_pom_restructurbill_tc

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
| 1 | idx_pom_restructurbill_tc_tid |  | ftid |
| 2 | idx_pom_restructurbill_tc_tbill |  | ftbillid |
| 3 | pk_pom_restructurbill_tc |  | fid |

---

## 组件领料明细-子表 t_pom_mrqrestructstocks

- **表名称：** 组件领料明细-子表
- **表名：** t_pom_mrqrestructstocks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmrqbomid | BOM表头ID | varchar | 255 |  | √ | ' ' | BOM表头ID |
| 3 | fmrqqty | 本次领用基本数量 | numeric | 23 | 10 | √ | 0 | 本次领用基本数量 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fmrqmaterial | 组件编码(隐藏) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fmrqprocessseqname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |
| 7 | fmrqmftmaterial | 组件编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 8 | fmrqbomentryid | 组件清单分录ID | varchar | 50 |  | √ | ' ' | 组件清单分录ID |
| 9 | fmrqqtynumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 10 | fmrqauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | fmrqbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fmrqoproperation | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 13 | fmrqsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 14 | fmrqconfiguredcode | 组件配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 15 | fmrqsourcetype | 领料来源类型 | varchar | 50 |  | √ | ' ' | 领料来源类型,枚举: A :手工新增 B :BOM引入 C :组件清单引入 D :库存改制前物料引入 E :更新引入 |
| 16 | fmrqqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :变动 |
| 17 | fmrqissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 18 | fmrquseratio | 使用比例（%） | numeric | 23 | 2 | √ | 0 | 使用比例（%） |
| 19 | fmrqoprdescription | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 20 | fmrqfixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 21 | fmrqoprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 22 | fmrqsupplyorgid | 供货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 23 | fmrqoprparent | 工序序列 | varchar | 50 |  | √ | ' ' | 工序序列 |
| 24 | fmrqwarehouseid | 供货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 25 | fmrqdemandqty | 基本需求数量 | numeric | 23 | 10 | √ | 0 | 基本需求数量 |
| 26 | fmrqscraprate | 变动损耗率% | numeric | 23 | 4 | √ | 0 | 变动损耗率% |
| 27 | fmrqprocessseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 28 | fmrqsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 29 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 30 | fmrqprocessseqtype | 序列类型 | varchar | 50 |  | √ | ' ' | 序列类型,枚举: A :主序列 B :并行序列 C :替代序列 |
| 31 | fmrqqtydenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_mrqrestructstocks |  | fid |
| 2 | pk_pom_mrqrestructstocks |  | fentryid |

---

## 关联子实体-子表 t_pom_restructurbill_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_restructurbill_lk

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
| 1 | idx_pom_restructurbill_lk_fk |  | fid |
| 2 | pk_pom_restructurbill_lk |  | fpkid |

---

## 改制前工序-子表 t_pom_srcrestructopentry

- **表名称：** 改制前工序-子表
- **表名：** t_pom_srcrestructopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsrcoprstatus | 工序状态 | varchar | 50 |  | √ | ' ' | 工序状态,枚举: A :创建 B :计划 C :计划确认 D :下达 E :开工 F :完工 G :关闭 |
| 3 | fsrcprocessseqtype | 序列类型 | varchar | 50 |  | √ | ' ' | 序列类型,枚举: A :主序列 B :并行序列 C :替代序列 |
| 4 | fsrcmftechnicsid | 工序计划表头ID | varchar | 50 |  | √ | ' ' | 工序计划表头ID |
| 5 | fsrcoprdescription | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 6 | fsrcsourcetype | 改制前来源类型 | varchar | 50 |  | √ | ' ' | 改制前来源类型,枚举: A :手工新增 B :更新引入 |
| 7 | fsrcoprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 8 | fsrcorderentryid | 工单分录ID | varchar | 50 |  | √ | ' ' | 工单分录ID |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fsrcchangetype | 调整类型 | varchar | 50 |  | √ | ' ' | 调整类型,枚举: A :作废 B :减少数量 |
| 11 | fsrcoprunitid | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fsrcchangeqty | 拆分改制数量 | numeric | 23 | 10 | √ | 0 | 拆分改制数量 |
| 13 | foprtotalreportqty | 已普通汇报数量 | numeric | 23 | 10 | √ | 0 | 已普通汇报数量 |
| 14 | fsrcoprqty | 工序数量 | numeric | 23 | 10 | √ | 0 | 工序数量 |
| 15 | fsrcoprparent | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 16 | fsrcmftechnicsentryid | 工序计划分录ID | varchar | 50 |  | √ | ' ' | 工序计划分录ID |
| 17 | fsrcorderid | 工单表头ID | varchar | 50 |  | √ | ' ' | 工单表头ID |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fsrcoproperationid | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 20 | fsrcprocessseqname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_srcrestructopentry |  | fentryid |
| 2 | idx_pom_srcrestructopentry |  | fid |

---

## 改制后工序-子表 t_pom_torestructopentry

- **表名称：** 改制后工序-子表
- **表名：** t_pom_torestructopentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftooprworkshopid | 生产车间 | int8 | 64 |  | √ | 0 | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 3 | ftooprunit | 工序单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 4 | ftooproperation | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | ftooprworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 7 | ftoprocessseqname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |
| 8 | ftomachiningtype | 加工类型 | varchar | 50 |  | √ | ' ' | 加工类型,枚举: 1001 :厂内加工 1002 :委外加工 1003 :内协加工 1004 :不限制 |
| 9 | ftostoragepoint | 入库点 | bpchar | 1 |  | √ | '0' | 入库点 |
| 10 | ftoinspectiontype | 检验方式 | varchar | 50 |  | √ | ' ' | 检验方式,枚举: 1011 :免检 1012 :车间检验 1013 :质量检验 |
| 11 | ftochangetype | 调整类型 | varchar | 50 |  | √ | ' ' | 调整类型,枚举: A :作废 B :手工新增 |
| 12 | ftooprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 13 | ftooprdescription | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 14 | ftooprparent | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 15 | ftosourcetype | 改制后来源类型 | varchar | 50 |  | √ | ' ' | 改制后来源类型,枚举: A :手工新增 B :更新引入 |
| 16 | ftooprctrlstrategy | 工序控制策略 | int8 | 64 |  | √ | 0 | [工序控制策略(废弃) mpdm_proctrlstrategy](../mpdm_files/mpdm_proctrlstrategy.md) |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | ftooprorg | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | ftoprocessseqtype | 序列类型 | varchar | 50 |  | √ | ' ' | 序列类型,枚举: A :主序列 B :并行序列 C :替代序列 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_torestructopentry |  | fentryid |
| 2 | idx_pom_torestructopentry |  | fid |

---

## 组件退料明细-子表 t_pom_retrestructstocks

- **表名称：** 组件退料明细-子表
- **表名：** t_pom_retrestructstocks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fretmaterialid | 组件编码(隐藏) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fretissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 4 | fretthisreturnqty | 本次退料数量 | numeric | 23 | 10 | √ | 0 | 本次退料数量 |
| 5 | fretstockentryid | 组件清单分录ID | varchar | 50 |  | √ | ' ' | 组件清单分录ID |
| 6 | fretoproperation | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fretorderentryid | 工单分录ID | varchar | 50 |  | √ | ' ' | 工单分录ID |
| 9 | fretcanreturnqty | 可退料数量 | numeric | 23 | 10 | √ | 0 | 可退料数量 |
| 10 | fretreceivedbaseqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 11 | fretsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fretauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fretstockid | 组件清单表头ID | varchar | 50 |  | √ | ' ' | 组件清单表头ID |
| 14 | fretqtynumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 15 | fretsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 16 | fretmftmaterialid | 组件编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 17 | fretunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fretqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :变动 |
| 19 | fretplanreturnbaseqty | 计划退料基本数量 | numeric | 23 | 10 | √ | 0 | 计划退料基本数量 |
| 20 | fretconfiguredcodeid | 组件配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 21 | fretsupplyorgid | 供货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fretlocation | 供货仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 23 | fretdemandqty | 基本需求数量 | numeric | 23 | 10 | √ | 0 | 基本需求数量 |
| 24 | fmaterialmodel | fmaterialmodel | varchar | 50 |  | √ | ' ' |  |
| 25 | fretorderid | 工单表头ID | varchar | 50 |  | √ | ' ' | 工单表头ID |
| 26 | fretmftechnicsentryid | 工序计划分录ID | varchar | 50 |  | √ | ' ' | 工序计划分录ID |
| 27 | fretqtydenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 28 | fretoprdescription | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 29 | fretbomid | BOM表头ID | varchar | 50 |  | √ | ' ' | BOM表头ID |
| 30 | fretmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fretsourcetype | 退料来源类型 | varchar | 50 |  | √ | ' ' | 退料来源类型,枚举: A :手工新增 B :BOM引入 C :组件清单引入 |
| 32 | fretprocessseqtype | 序列类型 | varchar | 50 |  | √ | ' ' | 序列类型,枚举: A :主序列 B :并行序列 C :替代序列 |
| 33 | fretwarehouseid | 供货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 34 | fretprocessseqname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |
| 35 | fretbomentryid | BOM分录ID | varchar | 50 |  | √ | ' ' | BOM分录ID |
| 36 | fretoprparent | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 37 | fretmftechnicsid | 工序计划表头ID | varchar | 50 |  | √ | ' ' | 工序计划表头ID |
| 38 | fretoprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fmaterialname | fmaterialname | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_retrestructstocks |  | fid |
| 2 | pk_pom_retrestructstocks |  | fentryid |

---

## 改制申请单-主表 t_pom_restructurbill

- **表名称：** 改制申请单-主表
- **表名：** t_pom_restructurbill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fmodel1 | fmodel1 | varchar | 50 |  | √ | ' ' |  |
| 4 | fbomversion2 | fbomversion2 | varchar | 50 |  | √ | ' ' |  |
| 5 | fpbauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fpabiztypeid | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fpaconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 9 | fpamanuversion | 生产版本 | int8 | 64 |  | √ | 0 | [生产版本 pdm_manuversion](../fmm_files/pdm_manuversion.md) |
| 10 | fbillno | 申请单号 | varchar | 30 |  | √ | ' ' | 申请单号 |
| 11 | fpbmftmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 12 | fpamftmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 13 | fpbrestructurqty | 本次改制数量 | numeric | 23 | 10 | √ | 0 | 本次改制数量 |
| 14 | fpaproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fpadealresult | 处理结果 | varchar | 255 |  | √ | ' ' | 处理结果 |
| 17 | fpbunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 18 | fparestructurqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 19 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 20 | freason | 改制原因 | varchar | 255 |  | √ | ' ' | 改制原因 |
| 21 | fpbconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 22 | fordernumber1 | fordernumber1 | varchar | 50 |  | √ | ' ' |  |
| 23 | frequesterid | 申请人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fpbproducedept | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fmaterialname1 | fmaterialname1 | varchar | 50 |  | √ | ' ' |  |
| 26 | fpbcanrestructurqty | 可改制数量 | numeric | 23 | 10 | √ | 0 | 可改制数量 |
| 27 | fpbqty | 生产工单数量 | numeric | 23 | 10 | √ | 0 | 生产工单数量 |
| 28 | fpamaterialid | 产品编码（物料） | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 29 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 30 | fmaterialname | fmaterialname | varchar | 50 |  | √ | ' ' |  |
| 31 | fpbordernumber | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 32 | fmodel | fmodel | varchar | 50 |  | √ | ' ' |  |
| 33 | fpborderentryid | 工单分录ID | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 34 | fpaplanpreparetime | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 35 | fpbxorderid | 工单变更单表头ID | int8 | 64 |  | √ | 0 | 工单变更单表头ID |
| 36 | fpbbomid | BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 37 | fpaorderentryid | 工单分录(改制生成)ID | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 38 | fbilldate | 申请日期 | timestamp | 0 |  |  | null | 申请日期 |
| 39 | fisrestructured | 已改制 | bpchar | 1 |  | √ | '0' | 已改制 |
| 40 | fpaplanbegintime | 计划开工时间 | timestamp | 0 |  |  | null | 计划开工时间 |
| 41 | fpaworkcenterid | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 42 | fpbmaterialid | 产品编码（物料） | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 43 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | frestructurtype | 改制类型 | varchar | 50 |  | √ | ' ' | 改制类型,枚举: A :库存改制 B :在产改制 |
| 45 | fpaplanendtime | 计划完工时间 | timestamp | 0 |  |  | null | 计划完工时间 |
| 46 | fpaunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 47 | fpbtransactiontype | 生产事务类型 | int8 | 64 |  | √ | 0 | [生产事务类型 mpdm_transactproduct](../mpdm_files/mpdm_transactproduct.md) |
| 48 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 49 | fpbtracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 50 | fpborderid | 工单表头ID | varchar | 50 |  | √ | ' ' | 工单表头ID |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fpbprocessroute | 工艺路线号 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 53 | fpaprocessroute | 工艺路线号 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 54 | fpbmanuversion | 生产版本 | int8 | 64 |  | √ | 0 | [生产版本 pdm_manuversion](../fmm_files/pdm_manuversion.md) |
| 55 | fpatransactiontype | 生产事务类型 | int8 | 64 |  | √ | 0 | [生产事务类型 mpdm_transactproduct](../mpdm_files/mpdm_transactproduct.md) |
| 56 | fproducttype | 生产类型 | varchar | 50 |  | √ | ' ' | 生产类型,枚举: A :生产 B :委外 |
| 57 | fisscrapped | 已报废 | bpchar | 1 |  | √ | '0' | 已报废 |
| 58 | fisreturned | 已退料 | bpchar | 1 |  | √ | '0' | 已退料 |
| 59 | fpadealstatus | 处理状态 | varchar | 50 |  | √ | ' ' | 处理状态,枚举: A :未处理 B :处理中 C :已完成 D :异常 |
| 60 | fpatracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 61 | fpabomid | BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 62 | fpaauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 63 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pom_restructurbill |  | fid |
| 2 | idx_pom_restructurbill_fno |  | fbillno |

---

## 改制申请单-反写记录表 t_pom_restructurbill_wb

- **表名称：** 改制申请单-反写记录表
- **表名：** t_pom_restructurbill_wb

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
| 1 | pk_pom_restructurbill_wb |  | fentryid |
| 2 | idx_pom_restructurbill_wb_fk |  | fid |

---

## 组件报废明细-子表 t_pom_scraprestructstocks

- **表名称：** 组件报废明细-子表
- **表名：** t_pom_scraprestructstocks

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fscrapthiswasteqty | 本次报废数量 | numeric | 23 | 10 | √ | 0 | 本次报废数量 |
| 3 | fscrapplanreturnbaseqty | 计划报废基本数量 | numeric | 23 | 10 | √ | 0 | 计划报废基本数量 |
| 4 | fscrapstockentryid | 组件清单分录ID | varchar | 50 |  | √ | ' ' | 组件清单分录ID |
| 5 | fscrapqtydenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 6 | fscrapprocessseqname | 序列名称 | varchar | 50 |  | √ | ' ' | 序列名称 |
| 7 | fscrapmaterialunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | fscraporderentryid | 工单分录ID | varchar | 50 |  | √ | ' ' | 工单分录ID |
| 10 | fscrapoproperation | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 11 | fscrapmaterial | 组件编码(隐藏) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 12 | fscrapbomentryid | BOM分录ID | varchar | 50 |  | √ | ' ' | BOM分录ID |
| 13 | fscrapconfiguredcode | 组件配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 14 | fscrapreceivedbaseqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 15 | fscrapmftechnicsid | 工序计划表头ID | varchar | 50 |  | √ | ' ' | 工序计划表头ID |
| 16 | fscrapunitid | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 17 | fscrapissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 18 | fscrapbomid | BOM表头ID | varchar | 50 |  | √ | ' ' | BOM表头ID |
| 19 | fmaterialmodel | fmaterialmodel | varchar | 50 |  | √ | ' ' |  |
| 20 | fscrapoprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 21 | fscrapmftechnicsentryid | 工序计划分录ID | varchar | 50 |  | √ | ' ' | 工序计划分录ID |
| 22 | fscrapstockid | 组件清单表头ID | varchar | 50 |  | √ | ' ' | 组件清单表头ID |
| 23 | fscrapsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 24 | fscrapqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :变动 |
| 25 | fscrapqtynumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 26 | fscrapoprparent | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 27 | fscrapwarehouseid | 供货仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 28 | fscrapoprdescription | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 29 | fscrapprocessseqtype | 序列类型 | varchar | 50 |  | √ | ' ' | 序列类型,枚举: A :主序列 B :并行序列 C :替代序列 |
| 30 | fscrapcanwasteqty | 可报废数量 | numeric | 23 | 10 | √ | 0 | 可报废数量 |
| 31 | fscraporderid | 工单表头ID | varchar | 50 |  | √ | ' ' | 工单表头ID |
| 32 | fscrapdemandqty | 基本需求数量 | numeric | 23 | 10 | √ | 0 | 基本需求数量 |
| 33 | fscrapsourcetype | 报废来源类型 | varchar | 50 |  | √ | ' ' | 报废来源类型,枚举: A :手工新增 B :BOM引入 C :组件清单引入 |
| 34 | fscrapsupplyorgid | 供货库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 35 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 36 | fscrapsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fscrapauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 38 | fscrapmftmaterial | 组件编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 39 | fmaterialname | fmaterialname | varchar | 50 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_scraprestructstocks |  | fid |
| 2 | pk_pom_scraprestructstocks |  | fentryid |
