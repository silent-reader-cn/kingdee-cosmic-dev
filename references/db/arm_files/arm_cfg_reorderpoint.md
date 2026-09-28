# 线边仓补料设置-arm_cfg_reorderpoint

## BOM关联关系-子表 t_arm_reorderptrelation

- **表名称：** BOM关联关系-子表
- **表名：** t_arm_reorderptrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatversionid | 子项物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 3 | fbomid | BOM | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 4 | fmaterialid | 子项主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fauxptyid | 子项辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arm_reorderptrelation |  | fentryid |
| 2 | idx_t_arm_reorderptrelation |  | fid |

---

## 生产线使用记录-子表 t_arm_reorderptprdentry

- **表名称：** 生产线使用记录-子表
- **表名：** t_arm_reorderptprdentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierfield1 | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fproductionline | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 4 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 5 | fmasterid | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fmaterielno | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fmodifydatefield1 | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_reorderptprdentry |  | fid |
| 2 | pk_t_arm_reorderptprdentry |  | fentryid |

---

## 子单据体-子表 t_arm_reorderptsubentry

- **表名称：** 子单据体-子表
- **表名：** t_arm_reorderptsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialversions | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 2 | fboms | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 3 | fmaterielnos | 产品编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 4 | fauxptys | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fproductionlines | 生产线编码 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 8 | fmasters | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_reorderptsubentry |  | fentryid |
| 2 | pk_t_arm_reorderptsubentry |  | fdetailid |

---

## 物料明细-子表 t_arm_reorderptcmpentry

- **表名称：** 物料明细-子表
- **表名：** t_arm_reorderptcmpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompmasterid | 主物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 3 | fprepamatermode | 调拨类型 | bpchar | 1 |  | √ | ' ' | 调拨类型,枚举: 0 :组织内调拨 1 :跨组织调拨 2 :仓位移动单 3 :VMI组织内调拨 4 :VMI跨组织调拨 |
| 4 | fcompunitid | 库存单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fisfrombom | 来自BOM | bpchar | 1 |  | √ | ' ' | 来自BOM |
| 7 | fstrategy | 补料策略 | bpchar | 1 |  | √ | 'A' | 补料策略,枚举: A :按再订货点补料 B :按需求补料（截至今日） C :按需求补料（截至明日） |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fcompversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 10 | fstatus | BOM关联 | bpchar | 1 |  | √ | ' ' | BOM关联,枚举: 0 :否 1 :是 |
| 11 | fcomponentid | 物料编码 | int8 | 64 |  | √ | 0 | [物料库存信息 bd_materialinventoryinfo](../sbd_files/bd_materialinventoryinfo.md) |
| 12 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | freordernum | 订货数量 | numeric | 23 | 10 | √ | 0 | 订货数量 |
| 14 | foutorgid | 默认调出组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | foutwarehouseid | 默认调出仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 16 | freorderpoint | 再订货点 | numeric | 23 | 10 | √ | 0 | 再订货点 |
| 17 | fisauxptyaffect | fisauxptyaffect | int8 | 64 |  |  | null |  |
| 18 | fownertype | 货主类型 | varchar | 50 |  |  | 'bos_org' | 货主类型,枚举: bos_org :业务组织 bd_supplier :供应商 |
| 19 | fcompauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 20 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 22 | foutlocationid | 默认调出仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_reorderptcmpentry |  | fid |
| 2 | pk_t_arm_reorderptcmpentry |  | fentryid |

---

## 线边仓补料设置-主表 t_arm_reorderpt

- **表名称：** 线边仓补料设置-主表
- **表名：** t_arm_reorderpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fdefaultstrategy | 默认补料策略 | bpchar | 1 |  | √ | 'A' | 默认补料策略,枚举: A :按再订货点补料 B :按需求补料（截至今日） C :按需求补料（截至明日） |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fwarehouseid | 线边仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | flocationid | 线边仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 12 | freordernum | 默认订货数量 | numeric | 23 | 10 | √ | 0 | 默认订货数量 |
| 13 | freorderpoint | 默认再订货点 | numeric | 23 | 10 | √ | 0 | 默认再订货点 |
| 14 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arm_reorderpt |  | fid |
| 2 | idx_t_arm_reorderpt |  | fbillno |
