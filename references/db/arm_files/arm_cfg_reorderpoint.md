# 线边仓再订货点设置-arm_cfg_reorderpoint

## 子单据体-子表 t_arm_reorderptsubentry

- **表名称：** 子单据体-子表
- **表名：** t_arm_reorderptsubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmaterialversions | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 2 | fboms | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 3 | fmaterielnos | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 4 | fauxptys | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fproductionlines | 生产线编码 | int8 | 64 |  | √ | 0 | 生产线 arm_linecapacity |
| 8 | fmasters | 主物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
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

## BOM关联关系-子表 t_arm_reorderptrelation

- **表名称：** BOM关联关系-子表
- **表名：** t_arm_reorderptrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmatversionid | 子项物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 3 | fbomid | BOM | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 4 | fmaterialid | 子项主物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
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

## 物料明细-子表 t_arm_reorderptcmpentry

- **表名称：** 物料明细-子表
- **表名：** t_arm_reorderptcmpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcompmasterid | 主物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 3 | fcompunitid | 库存单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fisfrombom | 来自BOM | bpchar | 1 |  | √ | ' ' | 来自BOM |
| 6 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcompversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 8 | fstatus | BOM关联 | bpchar | 1 |  | √ | ' ' | BOM关联,枚举: 0 :否 1 :是 |
| 9 | fcomponentid | 物料编码 | int8 | 64 |  | √ | 0 | 物料库存信息 bd_materialinventoryinfo |
| 10 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | freordernum | 订货数量 | numeric | 23 | 10 | √ | 0 | 订货数量 |
| 12 | foutorgid | 默认调出组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 13 | foutwarehouseid | 默认调出仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 14 | freorderpoint | 再订货点 | numeric | 23 | 10 | √ | 0 | 再订货点 |
| 15 | fcompauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 16 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | foutlocationid | 默认调出仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |

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

## 线边仓再订货点设置-主表 t_arm_reorderpt

- **表名称：** 线边仓再订货点设置-主表
- **表名：** t_arm_reorderpt

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fwarehouseid | 线边仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | flocationid | 线边仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 11 | freordernum | 默认订货数量 | numeric | 23 | 10 | √ | 0 | 默认订货数量 |
| 12 | freorderpoint | 默认再订货点 | numeric | 23 | 10 | √ | 0 | 默认再订货点 |
| 13 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arm_reorderpt |  | fid |
| 2 | idx_t_arm_reorderpt |  | fbillno |

---

## 生产线使用记录-子表 t_arm_reorderptprdentry

- **表名称：** 生产线使用记录-子表
- **表名：** t_arm_reorderptprdentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifierfield1 | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fproductionline | 生产线 | int8 | 64 |  | √ | 0 | 生产线 arm_linecapacity |
| 4 | fbomid | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 5 | fmasterid | 主物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | fmaterielno | 产品编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 7 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 8 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
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
