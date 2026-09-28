# 生产用料清单变更单-pom_xmftstock

## 关联子实体-子表 t_pom_manustockentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_manustockentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdetailid | fdetailid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pom_manustockentry_lk_pkey |  | fpkid |
| 2 | idx_pom_manustockentry_lk_fk |  | fdetailid |

---

## 生产用料清单变更单-反写记录表 t_pom_mftorderentry_s_wb

- **表名称：** 生产用料清单变更单-反写记录表
- **表名：** t_pom_mftorderentry_s_wb

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
| 1 | t_pom_mftorderentry_s_wb_pkey |  | fentryid |
| 2 | idx_pom_mftorderentry_s_wb_fk |  | fid |

---

## 生产用料清单变更单-主表 t_pom_xmftorderentry_s

- **表名称：** 生产用料清单变更单-主表
- **表名：** t_pom_xmftorderentry_s

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 生产工单主id | int8 | 64 |  | √ | 0 | 生产工单主id |
| 2 | fbillauxqty | 辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 辅助数量 |
| 3 | fk_bj73_basedatafield | 工单单据类型 | int8 | 64 |  | √ | 0 | [单据类型 bos_billtype](../cts_files/bos_billtype.md) |
| 4 | fmaterialid | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 5 | fauxpropertynew | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | forderid | 生产工单ID | varchar | 50 |  | √ | ' ' | 生产工单ID |
| 8 | fk_bj73_qtyfield | fk_bj73_qtyfield | numeric | 23 | 10 |  | null |  |
| 9 | fremarks | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 10 | fconfiguredcodeid | 产品配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 11 | forderentryid | 生产工单行号 | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 12 | fbiztime | 变更单日期 | timestamp | 0 |  |  | null | 变更单日期 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fomversion | BOM版本 | varchar | 50 |  | √ | ' ' | BOM版本 |
| 15 | fauxproperty | fauxproperty | varchar | 50 |  | √ | ' ' |  |
| 16 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 17 | freplaceno | 替代号 | varchar | 50 |  | √ | ' ' | 替代号 |
| 18 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 20 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 21 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 23 | ftransactiontypeid | ftransactiontypeid | int8 | 64 |  | √ | 0 |  |
| 24 | fqty | 数量 | numeric | 23 | 10 | √ | 0.0000000000 | 数量 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fischanged | fischanged | bpchar | 1 |  | √ | '0' |  |
| 27 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 D :作废 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | funitid | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 30 | fproductmasterid | 产品(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 31 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 32 | fmftdeptorgid | 单据头生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 33 | freason | 变更原因 | varchar | 255 |  | √ | ' ' | 变更原因 |
| 34 | freasonid | 变更原因 | int8 | 64 |  | √ | 0 | [变更原因 pdm_ecnreason](../pdm_files/pdm_ecnreason.md) |
| 35 | forderno | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 36 | fprocessroute | 工艺路线 | int8 | 64 |  | √ | 0 | [工艺路线 mpdm_sfcprocessroute](../sbd_files/mpdm_sfcprocessroute.md) |
| 37 | fmftinqty | 最新完工入库数量 | numeric | 23 | 10 | √ | 0.0000000000 | 最新完工入库数量 |
| 38 | fsourcebillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 39 | fbaseqty | 基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本数量 |
| 40 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 41 | fbillauxunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 42 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 43 | fbilltype | 单据类型 | int8 | 64 |  | √ | 0 | 单据类型 bos_billtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_xmoes_fbillno |  | fbillno |
| 2 | idx_pom_xmoes_fsourcebillid |  | fsourcebillid |
| 3 | idx_pom_xmoes_fcreatetime |  | fcreatetime |
| 4 | t_pom_xmftorderentry_s_pkey |  | fentryid |

---

## 生产用料清单变更单-关联追踪表 t_pom_mftorderentry_s_tc

- **表名称：** 生产用料清单变更单-关联追踪表
- **表名：** t_pom_mftorderentry_s_tc

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
| 1 | idx_pom_mftorderentry_s_tc_tbill |  | ftbillid |
| 2 | t_pom_mftorderentry_s_tc_pkey |  | fid |
| 3 | idx_pom_mftorderentry_s_tc_tid |  | ftid |

---

## 生产用料清单变更单-多语言表 t_pom_xmftorderentry_s_l

- **表名称：** 生产用料清单变更单-多语言表
- **表名：** t_pom_xmftorderentry_s_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pom_xmftorderentry_s_l_pkey |  | fpkid |
| 2 | idx_pom_xmoesl_fentryid |  | fentryid,flocaleid |

---

## 关联子实体-子表 t_pom_mftorderentry_s_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pom_mftorderentry_s_lk

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
| 1 | pk_pom_mftorderentry_s_lk |  | fpkid |
| 2 | idx_pom_mftorderentry_s_lk_fk |  | fentryid |

---

## 物料明细-子表 t_pom_xmanustockentry

- **表名称：** 物料明细-子表
- **表名：** t_pom_xmanustockentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | funissueqty | 未领基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 未领基本数量 |
| 2 | fbomreversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 3 | fmaterielinv | 物料库存信息 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 4 | fwastagerateformula | 损耗计算公式 | varchar | 30 |  | √ | ' ' | 损耗计算公式,枚举: A :标准用量/（1-损耗率） B :标准用量*（1+损耗率） |
| 5 | fstandqty | 标准基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 标准基本数量 |
| 6 | fissuemode | 领送料方式 | varchar | 30 |  | √ | ' ' | 领送料方式,枚举: A :生产领料 B :直送 C :不领料 |
| 7 | fiscannegative | 退料 | bpchar | 1 |  | √ | '0' | 退料 |
| 8 | flocation | 发料仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | foutlocation | 调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 11 | fscraprate | 变动损耗率% | numeric | 23 | 10 | √ | 0.0000000000 | 变动损耗率% |
| 12 | fchildauxpropertyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | foperatemrp | MRP计算 | bpchar | 1 |  | √ | '0' | MRP计算 |
| 14 | fisreturninspect | 生产退料检验 | bpchar | 1 |  | √ | 0 | 生产退料检验 |
| 15 | fworkplanid | 工序计划分录ID | int8 | 64 |  | √ | 0 | 工序计划分录ID |
| 16 | fownertype | 产品货主类型（废弃） | varchar | 30 |  | √ | ' ' | 产品货主类型（废弃）,枚举: bd_customer :客户 bd_supplier :供应商 bos_org :业务单元 |
| 17 | fisstockallot | 备料调拨 | bpchar | 1 |  | √ | '0' | 备料调拨 |
| 18 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 19 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 20 | frework | 返工 | bpchar | 1 |  | √ | '0' | 返工 |
| 21 | fecostcenterid | 成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 22 | fuseratio | 使用比例(%) | numeric | 23 | 10 | √ | 0.0000000000 | 使用比例(%) |
| 23 | fprojectid | 需求项目号 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 24 | fqtydenominator | 基本单位分母 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位分母 |
| 25 | fbatchno | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 26 | fsrcbillid | 来源单据ID | int8 | 64 |  | √ | 0 | 来源单据ID |
| 27 | fchildbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 28 | fwarehouseid | 发料仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 29 | fsupplierid | 货主 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 30 | fworkstation | 工位 | int8 | 64 |  | √ | 0 | [工位 mpdm_workstation](../mpdm_files/mpdm_workstation.md) |
| 31 | fisstep | 是否阶梯用量 | bpchar | 1 |  | √ | '0' | 是否阶梯用量 |
| 32 | fk_bj73_ylbillid | 用料清单ID | varchar | 50 |  | √ | ' ' | 用料清单ID |
| 33 | fsupplymode | 货主类型 | varchar | 30 |  | √ | ' ' | 货主类型,枚举: bos_org :业务单元 bd_customer :客户 bd_supplier :供应商 |
| 34 | fownerid | 产品货主（废弃） | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 35 | flotid | 批号主档 | int8 | 64 |  | √ | 0 | [批号主档 bd_lot](../sbd_files/bd_lot.md) |
| 36 | fmaterialunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 37 | fchildbomversion | 子项BOM版本 | varchar | 50 |  | √ | ' ' | 子项BOM版本 |
| 38 | fsupplyorgid | 发料组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 39 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 40 | foutsqty | foutsqty | numeric | 23 | 10 | √ | 0.0000000000 |  |
| 41 | foutqty | 关联领料基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 关联领料基本数量 |
| 42 | fsupplytype | 供应类型 | varchar | 30 |  | √ | ' ' | 供应类型,枚举: 10040 :外购 10030 :自制 10050 :委外 |
| 43 | freservebaseqty | 库存预留基本数量 | numeric | 23 | 10 | √ | 0 | 库存预留基本数量 |
| 44 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 45 | fk_bj73_qtyfield | 涨发率 | numeric | 23 | 10 |  | null | 涨发率 |
| 46 | fconfiguredcodeid | 产品配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 47 | fentryconfiguredcodeid | 子项配置号(废弃) | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 48 | fk_bj73_zfl | fk_bj73_zfl | numeric | 23 | 10 |  | null |  |
| 49 | fmaterielmasterid | 物料(主数据) | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 50 | fuseqty | 已消耗基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已消耗基本数量 |
| 51 | factissueqty | 已领基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 已领基本数量 |
| 52 | ftracknumberid | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 53 | foutorgunitid | 调出库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 54 | favbbaseqty | 库存可用基本数量 | numeric | 23 | 10 | √ | 0 | 库存可用基本数量 |
| 55 | fqtytype | 用量类型 | varchar | 30 |  | √ | ' ' | 用量类型,枚举: A :变动 B :固定 C :阶梯 |
| 56 | fqtynumerator | 基本单位分子 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位分子 |
| 57 | fsrcbillentryid | 来源单据分录ID | int8 | 64 |  | √ | 0 | 来源单据分录ID |
| 58 | ffixscrap | 固定损耗 | numeric | 23 | 10 | √ | 0.0000000000 | 固定损耗 |
| 59 | foutwarehouseid | 调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 60 | fprovideorgid | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 61 | fdemandqty | 应发基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 应发基本数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_xmse_fseq |  | fseq |
| 2 | idx_xstentry_fconfiguredcode |  | fconfiguredcodeid |
| 3 | idx_xstentry_ftracknumber |  | ftracknumberid |
| 4 | idx_xstentry_feconfiguredcode |  | fentryconfiguredcodeid |
| 5 | t_pom_xmanustockentry_pkey |  | fdetailid |
| 6 | idx_xstentry_fsrcbillentryid |  | fsrcbillentryid |
| 7 | idx_pom_xmse_fentryid |  | fentryid |

---

## 物料明细-多语言表 t_pom_xmanustockentry_l

- **表名称：** 物料明细-多语言表
- **表名：** t_pom_xmanustockentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fchildremarks | 备注 | varchar | 250 |  | √ | ' ' | 备注 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fsetuplocation | 安装位置 | varchar | 100 |  | √ | ' ' | 安装位置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_xmsel_fdetailid |  | fdetailid,flocaleid |
| 2 | t_pom_xmanustockentry_l_pkey |  | fpkid |

---

## 物料明细-分表 t_pom_xmanustockentry_b

- **表名称：** 物料明细-分表
- **表名：** t_pom_xmanustockentry_b

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbusdenominator | 分母 | numeric | 23 | 10 | √ | 1 | 分母 |
| 2 | fislead | 是否引入 | bpchar | 1 |  | √ | '0' | 是否引入 |
| 3 | fstockentryseq | 生产用料清单行号 | varchar | 50 |  | √ | ' ' | 生产用料清单行号 |
| 4 | fneedqty | 需求数量 | numeric | 23 | 10 | √ | 0 | 需求数量 |
| 5 | fentryorderno | 生产工单编号 | varchar | 50 |  | √ | ' ' | 生产工单编号 |
| 6 | fgoodrejectedqty | 良品退料基本数量 | numeric | 23 | 10 | √ | 0 | 良品退料基本数量 |
| 7 | fisentryexpand | 来源于展开行 | varchar | 5 |  | √ | '0' | 来源于展开行 |
| 8 | fbusactissueqty | 已领数量 | numeric | 23 | 10 | √ | 0 | 已领数量 |
| 9 | factreceivebaseqty | 实领基本数量 | numeric | 23 | 10 | √ | 0 | 实领基本数量 |
| 10 | fparentmaterialid | 父项物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 11 | factreceiveqty | 实领数量 | numeric | 23 | 10 | √ | 0 | 实领数量 |
| 12 | ftopmaterialid | 顶层物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 13 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 14 | fbusstandqty | 标准数量 | numeric | 23 | 10 | √ | 0 | 标准数量 |
| 15 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 16 | fisjumplevel | 跳层 | bpchar | 1 |  | √ | '0' | 跳层 |
| 17 | favbinvqty | 可用库存数量 | numeric | 23 | 10 | √ | 0 | 可用库存数量 |
| 18 | fisentryexpandone | 已展开行 | varchar | 5 |  | √ | '0' | 已展开行 |
| 19 | fprodeptorgid | 生产部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fbusunissueqty | 未领数量 | numeric | 23 | 10 | √ | 0 | 未领数量 |
| 21 | fentryidf | 组件清单分录f7 | int8 | 64 |  | √ | 0 | [生产用料清单分录f7 pom_mftstockentryf7](../pom_files/pom_mftstockentryf7.md) |
| 22 | fentryorderentryid | 生产工单行id | int8 | 64 |  | √ | 0 | [生产工单分录f7 pom_mftorder_f7](../pom_files/pom_mftorder_f7.md) |
| 23 | fsrctype | 子项来源类型 | bpchar | 1 |  | √ | 'A' | 子项来源类型,枚举: A :普通 B :补料单反写 C :退料单反写 |
| 24 | fstockentryid | 生产组件清单分录ID | varchar | 50 |  | √ | ' ' | 生产组件清单分录ID |
| 25 | fbusnumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 26 | fproductbaseqty | 产品基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 产品基本数量 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 28 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |
| 29 | fbusbadincomerejectedqty | 来料不良退料数量 | numeric | 23 | 10 | √ | 0 | 来料不良退料数量 |
| 30 | fretoverdrawnbaseqty | 多领退回基本数量 | numeric | 23 | 10 | √ | 0 | 多领退回基本数量 |
| 31 | fretoverdrawnqty | 多领退回数量 | numeric | 23 | 10 | √ | 0 | 多领退回数量 |
| 32 | fbusgoodrejectedqty | 良品退料数量 | numeric | 23 | 10 | √ | 0 | 良品退料数量 |
| 33 | fproducttransid | fproducttransid | int8 | 64 |  | √ | 0 |  |
| 34 | fbadtaskrejectedqty | 作业不良退料基本数量 | numeric | 23 | 10 | √ | 0 | 作业不良退料基本数量 |
| 35 | finvmatunitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 36 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 37 | fstockno | 生产用料清单编号 | varchar | 50 |  | √ | ' ' | 生产用料清单编号 |
| 38 | fstockentrypid | 用料清单分录父ID | int8 | 64 |  | √ | 0 | 用料清单分录父ID |
| 39 | fbadincomerejectedqty | 来料不良退料基本数量 | numeric | 23 | 10 | √ | 0 | 来料不良退料基本数量 |
| 40 | fbusbadtaskrejectedqty | 作业不良退料数量 | numeric | 23 | 10 | √ | 0 | 作业不良退料数量 |
| 41 | fproductno | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 42 | fbusoutqty | 关联领料数量 | numeric | 23 | 10 | √ | 0 | 关联领料数量 |
| 43 | fbususeqty | 已消耗数量 | numeric | 23 | 10 | √ | 0 | 已消耗数量 |
| 44 | fneedbaseqty | 需求基本数量 | numeric | 23 | 10 | √ | 0 | 需求基本数量 |
| 45 | fbusdemandqty | 应发数量 | numeric | 23 | 10 | √ | 0 | 应发数量 |
| 46 | fproductbaseunit | 产品基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 47 | fstockid | 生产组件清单ID | varchar | 50 |  | √ | ' ' | 生产组件清单ID |
| 48 | fchildmatunitid | 子项单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 49 | favbinvbaseqty | 可用库存基本数量 | numeric | 23 | 10 | √ | 0 | 可用库存基本数量 |
| 50 | fmpmtaskno | 项目任务号 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_xmseb_fentryid |  | fentryid |
| 2 | t_pom_xmanustockentry_b_pkey |  | fdetailid |

---

## 物料明细-分表 t_pom_xmanustockentry_a

- **表名称：** 物料明细-分表
- **表名：** t_pom_xmanustockentry_a

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbackflushtime | 倒冲时机 | varchar | 30 |  | √ | ' ' | 倒冲时机,枚举: A :入库倒冲 B :汇报倒冲 |
| 2 | ffeedingqty | 补料基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 补料基本数量 |
| 3 | fdemanddate | 需求时间 | timestamp | 0 |  |  | null | 需求时间 |
| 4 | fqcppbaseqty | 退料请检基本数量 | numeric | 23 | 10 | √ | 0 | 退料请检基本数量 |
| 5 | freplacegroup | 替代组号 | int8 | 64 |  | √ | 0 | 替代组号 |
| 6 | fsupplier | 委外供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 7 | fqcppbasejoinqty | 退料请检关联基本数量 | numeric | 23 | 10 | √ | 0 | 退料请检关联基本数量 |
| 8 | fprocessplan | 工序计划 | varchar | 50 |  | √ | ' ' | 工序计划 |
| 9 | fbasetransapplyqty | 基本单位.调拨申请数量 | numeric | 23 | 10 | √ | 0 | 基本单位.调拨申请数量 |
| 10 | fqcppqty | 退料请检数量 | numeric | 23 | 10 | √ | 0 | 退料请检数量 |
| 11 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 |  |
| 12 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 13 | fqcppjoinqty | 退料请检关联数量 | numeric | 23 | 10 | √ | 0 | 退料请检关联数量 |
| 14 | fprocessnumber | 工序号 | int4 | 32 |  | √ | 0 | 工序号 |
| 15 | fissinlowlimit | 领料下限允差(%) | numeric | 23 | 10 | √ | 0.0000000000 | 领料下限允差(%) |
| 16 | fscrapqty | 报废基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 报废基本数量 |
| 17 | ftagnum | 位号 | varchar | 255 |  | √ | ' ' | 位号 |
| 18 | ftransapplyqty | 子项单位.调拨申请数量 | numeric | 23 | 10 | √ | 0 | 子项单位.调拨申请数量 |
| 19 | fbuswipqty | 在制数量 | numeric | 23 | 10 | √ | 0 | 在制数量 |
| 20 | frejectedqty | 退料基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 退料基本数量 |
| 21 | finvtransdictqty | 库存单位.已调拨数量 | numeric | 23 | 10 | √ | 0 | 库存单位.已调拨数量 |
| 22 | fiskeypart | 关键件 | bpchar | 1 |  | √ | '0' | 关键件 |
| 23 | foprworkcenter | 工作中心 | int8 | 64 |  | √ | 0 | [工作中心定义(废弃) mpdm_workcentre](../mpdm_files/mpdm_workcentre.md) |
| 24 | fbasetransapplyrelqty | 基本单位.调拨申请关联数量 | numeric | 23 | 10 | √ | 0 | 基本单位.调拨申请关联数量 |
| 25 | ftransdictnonqty | 子项单位.未调拨数量 | numeric | 23 | 10 | √ | 0 | 子项单位.未调拨数量 |
| 26 | foperationdesc | 工序说明 | varchar | 50 |  | √ | ' ' | 工序说明 |
| 27 | fbuscansendqty | 可领数量 | numeric | 23 | 10 | √ | 0 | 可领数量 |
| 28 | fwipqty | 在制基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 在制基本数量 |
| 29 | freplacestrategy | 替代策略 | varchar | 5 |  | √ | ' ' | 替代策略,枚举: 1001 :整批替代 1002 :混用替代 1003 :整批+混用 1004 :手工替代 |
| 30 | fbusallotqty | 调拨数量 | numeric | 23 | 10 | √ | 0 | 调拨数量 |
| 31 | fextraratioqty | 领料上限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 领料上限基本数量 |
| 32 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 33 | fentrychangetype | 变更方式 | varchar | 30 |  | √ | ' ' | 变更方式,枚举: A :新增 B :修改 |
| 34 | fleadtimeunit | fleadtimeunit | varchar | 30 |  | √ | ' ' |  |
| 35 | fprocessseq | 工序序列（废弃） | varchar | 50 |  | √ | ' ' | 工序序列（废弃） |
| 36 | fprocesssequence | 工序序列 | int4 | 32 |  | √ | 0 | 工序序列 |
| 37 | fallotqty | 基本单位.已调拨数量 | numeric | 23 | 10 | √ | 0.0000000000 | 基本单位.已调拨数量 |
| 38 | fisoutmachining | 是否委外加工 | bpchar | 1 |  | √ | '0' | 是否委外加工 |
| 39 | ftagnum_tag | 位号_详情 | text | 0 |  |  | null | 位号_详情 |
| 40 | fpriority | 替代优先级 | int8 | 64 |  | √ | 0 | 替代优先级 |
| 41 | freplacemode | 替代方式 | varchar | 5 |  | √ | ' ' | 替代方式,枚举: A :替代 B :取代 C :按比例 |
| 42 | fpromaterentryid | 工序物料分配分录ID | int8 | 64 |  | √ | 0 | 工序物料分配分录ID |
| 43 | ftransdictrelqty | 子项单位.调拨关联数量 | numeric | 23 | 10 | √ | 0 | 子项单位.调拨关联数量 |
| 44 | ftransdictqty | 子项单位.已调拨数量 | numeric | 23 | 10 | √ | 0 | 子项单位.已调拨数量 |
| 45 | fmachiningtype | 加工类型 | varchar | 30 |  | √ | ' ' | 加工类型,枚举: 1 :厂内加工 2 :内协加工 3 :委外加工 |
| 46 | freplaceplan | 物料替代方案 | int8 | 64 |  | √ | 0 | [物料替代方案 mpdm_replaceplan](../basedata_files/mpdm_replaceplan.md) |
| 47 | foprno | 工序号（废弃） | varchar | 50 |  | √ | ' ' | 工序号（废弃） |
| 48 | fisbomextend | 来源于BOM展开 | bpchar | 1 |  | √ | '0' | 来源于BOM展开 |
| 49 | fworkprocedureid | 工序编码 | int8 | 64 |  | √ | 0 | [标准工序定义(废弃) mpdm_workprocedure](../mpdm_files/mpdm_workprocedure.md) |
| 50 | fbomentryid | BOM分录ID | int8 | 64 |  | √ | 0 | BOM分录ID |
| 51 | fleadtime | 提前期偏置(天) | numeric | 23 | 10 | √ | 0.0000000000 | 提前期偏置(天) |
| 52 | foverissuecontrl | 超发控制 | varchar | 30 |  | √ | ' ' | 超发控制,枚举: A :可超发 B :不可超发 C :最小包装量 |
| 53 | ftransapplyrelqty | 子项单位.调拨申请关联数量 | numeric | 23 | 10 | √ | 0 | 子项单位.调拨申请关联数量 |
| 54 | fissinhighlimit | 领料上限允差(%) | numeric | 23 | 10 | √ | 0.0000000000 | 领料上限允差(%) |
| 55 | fparentid | 父ID | int8 | 64 |  | √ | 0 | 父ID |
| 56 | fbusrejectedqty | 退料数量 | numeric | 23 | 10 | √ | 0 | 退料数量 |
| 57 | fismainreplace | 替代主料 | bpchar | 1 |  | √ | '0' | 替代主料 |
| 58 | fisbackflush | fisbackflush | bpchar | 1 |  | √ | '0' |  |
| 59 | fbusfeedingqty | 补料数量 | numeric | 23 | 10 | √ | 0 | 补料数量 |
| 60 | flackraitioqty | 领料下限基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 领料下限基本数量 |
| 61 | ftotalleadtime | 总提前期偏置(天) | numeric | 23 | 10 | √ | 0 | 总提前期偏置(天) |
| 62 | fbasetransdictrelqty | 基本单位.调拨关联数量 | numeric | 23 | 10 | √ | 0 | 基本单位.调拨关联数量 |
| 63 | fisbulkmaterial | 散装物料 | bpchar | 1 |  | √ | '0' | 散装物料 |
| 64 | fbusscrapqty | 报废数量 | numeric | 23 | 10 | √ | 0 | 报废数量 |
| 65 | fbasetransdictnonqty | 基本单位.未调拨数量 | numeric | 23 | 10 | √ | 0 | 基本单位.未调拨数量 |
| 66 | finvtransdictnonqty | 库存单位.未调拨数量 | numeric | 23 | 10 | √ | 0 | 库存单位.未调拨数量 |
| 67 | fcansendqty | 可领基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 可领基本数量 |
| 68 | fisbackflushnew | 倒冲 | varchar | 30 |  | √ | ' ' | 倒冲,枚举: A :不倒冲 B :始终倒冲 C :工作中心决定是否倒冲 |
| 69 | finvtransdictrelqty | 库存单位.调拨关联数量 | numeric | 23 | 10 | √ | 0 | 库存单位.调拨关联数量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pom_xmsea_fentryid |  | fentryid |
| 2 | t_pom_xmanustockentry_a_pkey |  | fdetailid |
