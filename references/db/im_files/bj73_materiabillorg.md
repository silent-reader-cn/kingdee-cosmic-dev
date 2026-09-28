# 原料清单-bj73_materiabillorg

## 原料清单-主表 tk_bj73_materialbillorg

- **表名称：** 原料清单-主表
- **表名：** tk_bj73_materialbillorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fk_bj73_qty | 数量 | numeric | 23 | 10 |  | null | 数量 |
| 4 | fk_bj73_status | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :未发布 B :已发布 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fk_bj73_productinbillid | 生产入库单ID | varchar | 50 |  | √ | ' ' | 生产入库单ID |
| 9 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fk_bj73_materiel | 产品编码 | int8 | 64 |  |  | null | [物料 bd_material](../basedata_files/bd_material.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fk_bj73_unitfield | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 14 | fk_bj73_hgqty | 合格品入库数量 | numeric | 23 | 10 |  | null | 合格品入库数量 |
| 15 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__bj73_materialbillorg |  | fid |

---

## 单据体-子表 tk_bj73_entryproduct

- **表名称：** 单据体-子表
- **表名：** tk_bj73_entryproduct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_bj73_decimalfield | 分配系数后重量 | numeric | 23 | 4 |  | null | 分配系数后重量 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fk_bj73_zhangfalv | 涨发率 | numeric | 23 | 4 |  | null | 涨发率 |
| 5 | fk_bj73_promateriel | 成品编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 6 | fk_bj73_soumaterial | 原料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 7 | fk_bj73_souqty | 原料重量 | numeric | 23 | 10 |  | null | 原料重量 |
| 8 | fk_bj73_prounit | 成品单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 9 | fk_bj73_fpxs | 分配系数 | numeric | 23 | 10 |  | null | 分配系数 |
| 10 | fk_bj73_invqty | 生产数量 | numeric | 23 | 10 |  | null | 生产数量 |
| 11 | fk_bj73_souunit | 原料单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 12 | fk_bj73_proqty | 入库数量 | numeric | 23 | 10 |  | null | 入库数量 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 14 | fk_bj73_skip | 是否不分摊 | bpchar | 1 |  | √ | '0' | 是否不分摊 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__bj73_entryproduct |  | fentryid |
| 2 | idx__bj73_entryproduct_fk |  | fid |

---

## 单据体1-子表 tk_bj73_materialorgentry

- **表名称：** 单据体1-子表
- **表名：** tk_bj73_materialorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fk_bj73_qty | 数量 | numeric | 23 | 10 |  | null | 数量 |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fk_bj73_materielnum | 物料编码 | int8 | 64 |  |  | null | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 5 | fk_bj73_zjdbentryid | 直接调拨单行id | int8 | 64 |  |  | null | 直接调拨单行id |
| 6 | fk_bj73_warehouse | 仓库 | int8 | 64 |  |  | null | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fk_bj73_batch | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 9 | fk_bj73_unit | 计量单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 11 | fmodifierfield | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx__bj73_materialorgentry_fk |  | fid |
| 2 | pk__bj73_materialorgentry |  | fentryid |

---

## 子单据体-子表 tk_bj73_auxsubenty

- **表名称：** 子单据体-子表
- **表名：** tk_bj73_auxsubenty

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fk_bj73_qty1 | 数量 | numeric | 23 | 10 |  | null | 数量 |
| 2 | fk_bj73_batch1 | 批号 | varchar | 50 |  | √ | ' ' | 批号 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fk_bj73_auxmaterial | 辅料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | fk_bj73_warehouse1 | 仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 6 | fk_bj73_unit1 | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fdetailid | fdetailid | int8 | 64 |  | √ | null | id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk__bj73_auxsubenty |  | fdetailid |
| 2 | idx__bj73_auxsubenty_fk |  | fentryid |
