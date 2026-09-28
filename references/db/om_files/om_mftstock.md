# 委外用料清单-om_mftstock

## 委外用料清单-多语言表 t_om_mftorderentry_s_l

- **表名称：** 委外用料清单-多语言表
- **表名：** t_om_mftorderentry_s_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_om_mftorderentry_s_l |  | fpkid |
| 2 | idx_om_moes_l_0 |  | fentryid,flocaleid |

---

## 关联子实体-子表 t_om_mftstock_lk

- **表名称：** 关联子实体-子表
- **表名：** t_om_mftstock_lk

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
| 1 | pk_om_mftstock_lk |  | fpkid |
| 2 | idx_om_mftstock_lk_fk |  | fentryid |

---

## 委外用料清单-反写记录表 t_om_mftstock_wb

- **表名称：** 委外用料清单-反写记录表
- **表名：** t_om_mftstock_wb

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
| 1 | idx_om_mftstock_wb_fk |  | fid |
| 2 | pk_om_mftstock_wb |  | fentryid |

---

## 物料明细-子表 t_om_mftstockentry

- **表名称：** 物料明细-子表
- **表名：** t_om_mftstockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | funissueqty | 未领基本数量 | numeric | 23 | 10 | √ | 0 | 未领基本数量 |
| 2 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 3 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 4 | fwastagerateformula | 损耗计算公式 | varchar | 50 |  | √ | ' ' | 损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 5 | fstandqty | 标准基本数量 | numeric | 23 | 10 | √ | 0 | 标准基本数量 |
| 6 | fissuemode | 领送料方式 | varchar | 50 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 7 | fbackflushtime | 倒冲时机 | varchar | 50 |  | √ | ' ' | 倒冲时机,枚举: A :入库倒冲 B :收货倒冲 |
| 8 | fiscannegative | 退料 | bpchar | 1 |  | √ | '0' | 退料 |
| 9 | flocation | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 10 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 11 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 12 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0 | 变动损耗率% |
| 13 | ffeedingqty | 补料基本数量 | numeric | 23 | 10 | √ | 0 | 补料基本数量 |
| 14 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 15 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 16 | foperatemrp | MRP计算 | bpchar | 1 |  | √ | '0' | MRP计算 |
| 17 | fsupplier | 委外供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 18 | fworkplanid | 工序计划分录ID | int8 | 64 |  | √ | 0 | 工序计划分录ID |
| 19 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 20 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 21 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 22 | fissinlowlimit | 领料下限允差(%) | numeric | 23 | 10 | √ | 0 | 领料下限允差(%) |
| 23 | frework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 24 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 25 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0 | 使用比例(%) |
| 26 | fscrapqty | 报废基本数量 | numeric | 23 | 10 | √ | 0 | 报废基本数量 |
| 27 | fprojectid | 需求项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 28 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 29 | fqtydenominator | 基本单位分母 | numeric | 23 | 10 | √ | 0 | 基本单位分母 |
| 30 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 31 | fchildbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 32 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 33 | frejectedqty | 退料基本数量 | numeric | 23 | 10 | √ | 0 | 退料基本数量 |
| 34 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 35 | fiskeypart | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 36 | fworkstation | 工位 | int8 | 64 |  | √ | 0 | [工位 mpdm_workstation](../mpdm_files/mpdm_workstation.md) |
| 37 | fisstep | 是否阶梯用量 | bpchar | 1 |  | √ | '0' | 是否阶梯用量 |
| 38 | foprworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 39 | fsupplymode | 货主类型 | varchar | 50 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :委外加工商 |
| 40 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 41 | foperationdesc | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 42 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 43 | fwipqty | 在制基本数量 | numeric | 23 | 10 | √ | 0 | 在制基本数量 |
| 44 | fchildbomversion | 子项BOM版本 | varchar | 50 |  | √ | ' ' | 子项BOM版本 |
| 45 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 46 | fextraratioqty | 领料上限基本数量 | numeric | 23 | 10 | √ | 0 | 领料上限基本数量 |
| 47 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 48 | fentrychangetype | 变更方式 | varchar | 50 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 C :取消 |
| 49 | fprocessseq | 序列号 | varchar | 50 |  | √ | ' ' | 序列号 |
| 50 | foutqty | 关联领料基本数量 | numeric | 23 | 10 | √ | 0 | 关联领料基本数量 |
| 51 | fallotqty | 基本单位.已调拨数量 | numeric | 23 | 10 | √ | 0 | 基本单位.已调拨数量 |
| 52 | freservebaseqty | 库存预留基本数量 | numeric | 23 | 10 | √ | 0 | 库存预留基本数量 |
| 53 | fsupplytype | 供应类型 | varchar | 30 |  | √ | ' ' | 供应类型,枚举: 10040 :外购 10030 :自制 10050 :委外 |
| 54 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 55 | fpriority | 替代优先级 | int8 | 64 |  | √ | 0 | 替代优先级 |
| 56 | fconfiguredcodeid | fconfiguredcodeid | int8 | 64 |  | √ | 0 |  |
| 57 | fentryconfiguredcodeid | 组件配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 58 | fpromaterentryid | 工序物料分配分录ID | int8 | 64 |  | √ | 0 | 工序物料分配分录ID |
| 59 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 60 | freplaceplan | 物料替代方案 | int8 | 64 |  | √ | 0 | [物料替代方案 mpdm_replaceplan](../basedata_files/mpdm_replaceplan.md) |
| 61 | fmachiningtype | 加工类型 | varchar | 50 |  | √ | ' ' | 加工类型,枚举: 1001 :厂内加工 1002 :委外加工 1003 :内协加工 1004 :不限制 |
| 62 | foprno | 工序号 | varchar | 50 |  | √ | ' ' | 工序号 |
| 63 | fisbomextend | 来源于BOM展开 | bpchar | 1 |  | √ | '0' | 来源于BOM展开 |
| 64 | fuseqty | 已消耗基本数量 | numeric | 23 | 10 | √ | 0 | 已消耗基本数量 |
| 65 | fworkprocedureid | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 66 | factissueqty | 已领基本数量 | numeric | 23 | 10 | √ | 0 | 已领基本数量 |
| 67 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 68 | foutorgunitid | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 69 | fleadtime | 提前期偏置(天) | numeric | 23 | 10 | √ | 0 | 提前期偏置(天) |
| 70 | foverissuecontrl | 超发控制 | varchar | 50 |  | √ | ' ' | 超发控制,枚举: A :可超发 B :不可超发 C :最小包装量 |
| 71 | fissinhighlimit | 领料上限允差(%) | numeric | 23 | 10 | √ | 0 | 领料上限允差(%) |
| 72 | favbbaseqty | 库存可用基本数量 | numeric | 23 | 10 | √ | 0 | 库存可用基本数量 |
| 73 | fqtytype | 用量类型 | varchar | 50 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 74 | fqtynumerator | 基本单位分子 | numeric | 23 | 10 | √ | 0 | 基本单位分子 |
| 75 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 76 | fisbackflush | 倒冲 | varchar | 50 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 77 | flackraitioqty | 领料下限基本数量 | numeric | 23 | 10 | √ | 0 | 领料下限基本数量 |
| 78 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 79 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0 | 固定损耗 |
| 80 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 81 | fisbulkmaterial | 散装物料 | bpchar | 1 |  | √ | '0' | 散装物料 |
| 82 | fdemandqty | 应发基本数量 | numeric | 23 | 10 | √ | 0 | 应发基本数量 |
| 83 | fcansendqty | 可领基本数量 | numeric | 23 | 10 | √ | 0 | 可领基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_mesen_fmaterielmasterid |  | fmaterielmasterid |
| 2 | idx_om_mftstockentry_fk |  | fentryid |
| 3 | pk_om_mftstockentry |  | fdetailid |

---

## 关联子实体-子表 t_om_mftstockentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_om_mftstockentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_mftstockentry_lk |  | fpkid |
| 2 | idx_om_mftstockentry_lk_fk |  | fdetailid |

---

## 物料明细-多语言表 t_om_mftstockentry_l

- **表名称：** 物料明细-多语言表
- **表名：** t_om_mftstockentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fchildremarks | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fsetuplocation | 安装位置 | varchar | 100 |  | √ | ' ' | 安装位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_mftstockentry_l |  | fpkid |
| 2 | idx_om_mftstockentry_l_0 |  | fdetailid,flocaleid |

---

## 物料明细-分表 t_om_mftstockentry_b

- **表名称：** 物料明细-分表
- **表名：** t_om_mftstockentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbusdenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 2 | fbusbadincomerejectedqty | 来料不良退料数量 | numeric | 23 | 10 | √ | 0 | 来料不良退料数量 |
| 3 | fretoverdrawnbaseqty | 多领退回基本数量 | numeric | 23 | 10 | √ | 0 | 多领退回基本数量 |
| 4 | fretoverdrawnqty | 多领退回数量 | numeric | 23 | 10 | √ | 0 | 多领退回数量 |
| 5 | fbusgoodrejectedqty | 良品退料数量 | numeric | 23 | 10 | √ | 0 | 良品退料数量 |
| 6 | fneedqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 7 | fbadtaskrejectedqty | 作业不良退料基本数量 | numeric | 23 | 10 | √ | 0 | 作业不良退料基本数量 |
| 8 | fgoodrejectedqty | 良品退料基本数量 | numeric | 23 | 10 | √ | 0 | 良品退料基本数量 |
| 9 | fisentryexpand | 来源于展开行 | varchar | 5 |  | √ | '0' | 来源于展开行 |
| 10 | finvmatunitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fbusactissueqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 12 | factreceivebaseqty | 实领基本数量 | numeric | 23 | 10 | √ | 0 | 实领基本数量 |
| 13 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 14 | fparentmaterialid | 父项物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 15 | factreceiveqty | 实领数量 | numeric | 23 | 10 | √ | 0 | 实领数量 |
| 16 | ftopmaterialid | 顶层物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 17 | fbadincomerejectedqty | 来料不良退料基本数量 | numeric | 23 | 10 | √ | 0 | 来料不良退料基本数量 |
| 18 | fownertype | 产品货主类型（废弃） | varchar | 30 |  | √ | ' ' | 产品货主类型（废弃）,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 19 | fbusbadtaskrejectedqty | 作业不良退料数量 | numeric | 23 | 10 | √ | 0 | 作业不良退料数量 |
| 20 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 21 | fbusstandqty | 标准数量 | numeric | 23 | 10 | √ | 0 | 标准数量 |
| 22 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 23 | fisjumplevel | 跳层 | bpchar | 1 |  | √ | '0' | 跳层 |
| 24 | favbinvqty | 可用库存数量 | numeric | 23 | 10 | √ | 0 | 可用库存数量 |
| 25 | fisentryexpandone | 已展开行 | varchar | 5 |  | √ | '0' | 已展开行 |
| 26 | fbusoutqty | 关联领料数量 | numeric | 23 | 10 | √ | 0 | 关联领料数量 |
| 27 | fbususeqty | 已消耗数量 | numeric | 23 | 10 | √ | 0 | 已消耗数量 |
| 28 | fbusunissueqty | 未领数量 | numeric | 23 | 10 | √ | 0 | 未领数量 |
| 29 | fneedbaseqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 30 | fbusdemandqty | 应发数量 | numeric | 23 | 10 | √ | 0 | 应发数量 |
| 31 | fchildmatunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 32 | favbinvbaseqty | 可用库存基本数量 | numeric | 23 | 10 | √ | 0 | 可用库存基本数量 |
| 33 | fsrctype | 子项来源类型 | bpchar | 1 |  | √ | 'A' | 子项来源类型,枚举: A :普通 B :补料单反写 C :退料单反写 |
| 34 | fbusnumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 35 | fownerid | 产品货主（废弃） | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 36 | fpushdownmatqty | 下推领料数量 | numeric | 23 | 10 | √ | 0 | 下推领料数量 |
| 37 | fchildmatunitqty | 子项单位数量 | numeric | 23 | 10 | √ | 0 | 子项单位数量 |
| 38 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 40 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_mftstockentry_b |  | fdetailid |
| 2 | idx_om_mftstockentry_b |  | fentryid |

---

## 物料明细-分表 t_om_mftstockentry_a

- **表名称：** 物料明细-分表
- **表名：** t_om_mftstockentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ftagnum_tag | 位号_详情 | text | 0 |  |  | null | 位号_详情 |
| 2 | freplacemode | 替代方式 | varchar | 5 |  | √ | ' ' | 替代方式,枚举: A :替代 B :取代 C :按比例 |
| 3 | ftransdictrelqty | 子项单位.调拨关联数量 | numeric | 23 | 10 | √ | 0 | 子项单位.调拨关联数量 |
| 4 | ftransdictqty | 子项单位.已调拨数量 | numeric | 23 | 10 | √ | 0 | 子项单位.已调拨数量 |
| 5 | fqcppbaseqty | 退料请检完成基本数量 | numeric | 23 | 10 | √ | 0 | 退料请检完成基本数量 |
| 6 | freplacegroup | 替代组号 | int8 | 64 |  | √ | 0 | 替代组号 |
| 7 | fisreturninspect | 委外退料检验 | bpchar | 1 |  | √ | 0 | 委外退料检验 |
| 8 | fqcppbasejoinqty | 退料请检关联基本数量 | numeric | 23 | 10 | √ | 0 | 退料请检关联基本数量 |
| 9 | fbasetransapplyqty | 基本单位.调拨申请数量 | numeric | 23 | 10 | √ | 0 | 基本单位.调拨申请数量 |
| 10 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 11 | fqcppqty | 退料请检完成数量 | numeric | 23 | 10 | √ | 0 | 退料请检完成数量 |
| 12 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 13 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 14 | fqcppjoinqty | 退料请检关联数量 | numeric | 23 | 10 | √ | 0 | 退料请检关联数量 |
| 15 | ftransapplyrelqty | 子项单位.调拨申请关联数量 | numeric | 23 | 10 | √ | 0 | 子项单位.调拨申请关联数量 |
| 16 | fisreplace | 替代件 | bpchar | 1 |  | √ | '0' | 替代件 |
| 17 | fbusrejectedqty | 退料数量 | numeric | 23 | 10 | √ | 0 | 退料数量 |
| 18 | fparentid | 父ID | int8 | 64 |  | √ | 0 | 父ID |
| 19 | ftagnum | 位号 | varchar | 255 |  | √ | ' ' | 位号 |
| 20 | ftransapplyqty | 子项单位.调拨申请数量 | numeric | 23 | 10 | √ | 0 | 子项单位.调拨申请数量 |
| 21 | fbuswipqty | 在制数量 | numeric | 23 | 10 | √ | 0 | 在制数量 |
| 22 | fbusfeedingqty | 补料数量 | numeric | 23 | 10 | √ | 0 | 补料数量 |
| 23 | finvtransdictqty | 库存单位.已调拨数量 | numeric | 23 | 10 | √ | 0 | 库存单位.已调拨数量 |
| 24 | ftotalleadtime | 总提前期偏置(天) | numeric | 23 | 10 | √ | 0 | 总提前期偏置(天) |
| 25 | fbasetransapplyrelqty | 基本单位.调拨申请关联数量 | numeric | 23 | 10 | √ | 0 | 基本单位.调拨申请关联数量 |
| 26 | ftransdictnonqty | 子项单位.未调拨数量 | numeric | 23 | 10 | √ | 0 | 子项单位.未调拨数量 |
| 27 | fbasetransdictrelqty | 基本单位.调拨关联数量 | numeric | 23 | 10 | √ | 0 | 基本单位.调拨关联数量 |
| 28 | fbuscansendqty | 可领数量 | numeric | 23 | 10 | √ | 0 | 可领数量 |
| 29 | freplacestrategy | 替代策略 | varchar | 5 |  | √ | ' ' | 替代策略,枚举: 1001 :整批替代 1002 :混用替代 1003 :整批+混用 1004 :手工替代 |
| 30 | fbusallotqty | 调拨数量 | numeric | 23 | 10 | √ | 0 | 调拨数量 |
| 31 | fbusscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 32 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | fbasetransdictnonqty | 基本单位.未调拨数量 | numeric | 23 | 10 | √ | 0 | 基本单位.未调拨数量 |
| 34 | finvtransdictnonqty | 库存单位.未调拨数量 | numeric | 23 | 10 | √ | 0 | 库存单位.未调拨数量 |
| 35 | finvtransdictrelqty | 库存单位.调拨关联数量 | numeric | 23 | 10 | √ | 0 | 库存单位.调拨关联数量 |
| 36 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 37 | fbomexpandpath | BOM展开路径 | varchar | 500 |  | √ | ' ' | BOM展开路径 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_om_mftstockentry_a |  | fdetailid |
| 2 | idx_om_mftstockentry_a |  | fentryid |

---

## 委外用料清单-关联追踪表 t_om_mftstock_tc

- **表名称：** 委外用料清单-关联追踪表
- **表名：** t_om_mftstock_tc

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
| 1 | idx_om_mftstock_tc_tid |  | ftid |
| 2 | pk_om_mftstock_tc |  | fid |
| 3 | idx_om_mftstock_tc_tbill |  | ftbillid |

---

## 委外用料清单-主表 t_om_mftorderentry_s

- **表名称：** 委外用料清单-主表
- **表名：** t_om_mftorderentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 生产工单主id | int8 | 64 |  | √ | 0 | 生产工单主id |
| 2 | fbillauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0 | 辅助数量 |
| 3 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 4 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forderid | 生产工单ID | varchar | 50 |  | √ | ' ' | 生产工单ID |
| 6 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 7 | finterprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 8 | fmftorderid | 委外工单单据头F7 | int8 | 64 |  | √ | 0 | [委外工单单据头F7 om_mftorder_headf7](../om_files/om_mftorder_headf7.md) |
| 9 | fconfiguredcodeid | 产品配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 10 | forderentryid | 委外工单行号 | int8 | 64 |  | √ | 0 | [委外工单分录F7 om_mftorder_f7](../om_files/om_mftorder_f7.md) |
| 11 | fisinit | 初始化单据 | bpchar | 1 |  | √ | '0' | 初始化单据 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fomversion | BOM版本 | varchar | 50 |  | √ | ' ' | BOM版本 |
| 14 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 15 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 16 | freplaceno | 替代号 | varchar | 50 |  | √ | ' ' | 替代号 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 19 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 20 | fentrustorg | 受托组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 21 | fbaseunitid | 产品基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fplanpreparetime | 计划准备时间 | timestamp | 0 |  |  | null | 计划准备时间 |
| 23 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 24 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fischanged | 是否存在未审核变更单 | bpchar | 1 |  | √ | '0' | 是否存在未审核变更单 |
| 28 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 31 | fproductmasterid | 产品(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 32 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 33 | fmftdeptorgid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 34 | forderno | 委外工单编号 | varchar | 50 |  | √ | ' ' | 委外工单编号 |
| 35 | fprocessroute | 工艺路线 | int8 | 64 |  | √ | 0 | 工艺路线维护（废弃） pdm_route |
| 36 | fmftinqty | 最新完工入库数量 | numeric | 23 | 10 | √ | 0 | 最新完工入库数量 |
| 37 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 38 | fbaseqty | 产品基本数量 | numeric | 23 | 10 | √ | 0 | 产品基本数量 |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 40 | fbillauxunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 42 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_om_moes_fcreatetime |  | fcreatetime |
| 2 | idx_om_moes_forderid |  | forderid |
| 3 | pk_om_mftorderentry_s |  | fentryid |
| 4 | idx_om_moes_forgideid |  | forgid,fentryid |
| 5 | idx_om_mes_fproductmasterid |  | fproductmasterid |
| 6 | idx_om_mes_orderno |  | fbillno,forderno |
| 7 | idx_om_moes_forderentryid |  | forderentryid |
