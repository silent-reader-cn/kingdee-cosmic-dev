# 物料可用性分析供需明细-psw_cacsupdem

## 物料可用性分析供需明细-主表 t_psw_cacsupdem

- **表名称：** 物料可用性分析供需明细-主表
- **表名：** t_psw_cacsupdem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fbaseunit | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 8 | fmaterialmaster | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterscheduleid | 计划编制id | int8 | 64 |  | √ | 0 | 计划编制id |
| 12 | fauxpty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_psw_cacsupdem_m0 |  | fbillno |
| 2 | pk_psw_cacsupdem |  | fid |

---

## 供应明细-子表 t_psw_cacsupply

- **表名称：** 供应明细-子表
- **表名：** t_psw_cacsupply

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 2 | fmodifierfield1 | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 4 | fproductionline | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 5 | fsupplytype | 供应类型 | varchar | 50 |  | √ | ' ' | 供应类型,枚举: 0 :重复生产工单 1 :即时库存 |
| 6 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fmodifydatefield1 | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: 0 :重复生产工单 1 :费重复生产工单 2 :上级物料 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_psw_cacsupply |  | fentryid |
| 2 | idx_psw_cacsupply_fk |  | fid |

---

## 需求明细-子表 t_psw_cacdemand

- **表名称：** 需求明细-子表
- **表名：** t_psw_cacdemand

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fproductionline | 生产线 | int8 | 64 |  | √ | 0 | [生产线 arm_linecapacity](../arm_files/arm_linecapacity.md) |
| 4 | fmodifierfield2 | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fmodifydatefield2 | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fsource | 来源 | varchar | 50 |  | √ | ' ' | 来源,枚举: 0 :重复生产工单 1 :费重复生产工单 2 :上级物料 |
| 8 | frootmaterialmaster | 根节点物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 9 | fdemandtype | 需求类型 | varchar | 50 |  | √ | ' ' | 需求类型,枚举: 0 :重复生产工单 1 :即时库存 |
| 10 | fparauxpty | 父节点辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 11 | frootmatversion | 根节点物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 12 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 13 | fparmatversion | 父节点物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 14 | fparmaterialmaster | 父节点物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 15 | frootauxpty | 根节点辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_psw_cacdemand_fk |  | fid |
| 2 | pk_psw_cacdemand |  | fentryid |
