# VMI结算记录-pm_vmisettlerecord

## 关联子实体-子表 t_pm_vmisrecordentry_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_vmisrecordentry_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 2 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 3 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | null |  |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_vmisrecordentry_lk_pkey |  | fpkid |
| 2 | idx_pm_vmisrecordentry_lk_fk |  | fentryid |

---

## VMI结算记录-主表 t_pm_vmisrecord

- **表名称：** VMI结算记录-主表
- **表名：** t_pm_vmisrecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fsettletype | 结算方式 | varchar | 5 |  | √ | ' ' | 结算方式,枚举: A :手工结算 B :实时结算 C :周期结算 |
| 4 | fbillstatus | 单据状态 | varchar | 5 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fsettlelotno | 结算批号 | varchar | 80 |  | √ | ' ' | 结算批号 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fsettlementmanid | 结算人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | frecorgid | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fbillno | 结算记录号 | varchar | 80 |  | √ | ' ' | 结算记录号 |
| 14 | fsettledate | 结算日期 | timestamp | 0 |  |  | null | 结算日期 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_vmisrecord_fbillno |  | fbillno |
| 2 | t_pm_vmisrecord_pkey |  | fid |

---

## 关联子实体-子表 t_pm_vmisrecord_lk

- **表名称：** 关联子实体-子表
- **表名：** t_pm_vmisrecord_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  | √ | 0 | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  | √ | 0 | 源单主实体内码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_vmisrecord_lk_fk |  | fid |
| 2 | t_pm_vmisrecord_lk_pkey |  | fpkid |

---

## VMI结算记录-关联追踪表 t_pm_vmisrecord_tc

- **表名称：** VMI结算记录-关联追踪表
- **表名：** t_pm_vmisrecord_tc

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
| 1 | t_pm_vmisrecord_tc_pkey |  | fid |
| 2 | idx_pm_vmisrecord_tc_tbill |  | ftbillid |
| 3 | idx_pm_vmisrecord_tc_tid |  | ftid |

---

## VMI结算记录-反写记录表 t_pm_vmisrecord_wb

- **表名称：** VMI结算记录-反写记录表
- **表名：** t_pm_vmisrecord_wb

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
| 1 | t_pm_vmisrecord_wb_pkey |  | fentryid |
| 2 | idx_pm_vmisrecord_wb_fk |  | fid |

---

## 物料明细-子表 t_pm_vmisrecordentry

- **表名称：** 物料明细-子表
- **表名：** t_pm_vmisrecordentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fpurinbillnumber | 采购入库单编号 | varchar | 80 |  | √ | ' ' | 采购入库单编号 |
| 3 | finvbillentryid | 库存单据行ID | int8 | 64 |  | √ | 0 | 库存单据行ID |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 5 | finvbillid | 库存单据ID | int8 | 64 |  | √ | 0 | 库存单据ID |
| 6 | fauxptyid | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fsrcbillentryseq | 物权转移单分录序号 | int8 | 64 |  | √ | 0 | 物权转移单分录序号 |
| 9 | fauxunitid | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 10 | finvbillentryseq | 库存单据分录序号 | int8 | 64 |  | √ | 0 | 库存单据分录序号 |
| 11 | fpurinbillentryid | 采购入库单行ID | int8 | 64 |  | √ | 0 | 采购入库单行ID |
| 12 | fpurinbillentity | 采购入库单实体 | varchar | 36 |  | √ | ' ' | 采购入库单实体 |
| 13 | finvbillnumber | 库存单据编号 | varchar | 80 |  | √ | ' ' | 库存单据编号 |
| 14 | fmaterialversionid | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 15 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 16 | fsrcbillentity | 物权转移单实体 | varchar | 36 |  | √ | ' ' | 物权转移单实体 |
| 17 | fqty | 本次结算数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次结算数量 |
| 18 | fsrcbillnumber | 物权转移单编号 | varchar | 80 |  | √ | ' ' | 物权转移单编号 |
| 19 | fsrcbillid | 物权转移单ID | int8 | 64 |  | √ | 0 | 物权转移单ID |
| 20 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fsupplierid | 结算供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 22 | fsrcbillentryid | 物权转移单行ID | int8 | 64 |  | √ | 0 | 物权转移单行ID |
| 23 | fpurinbillid | 采购入库单ID | int8 | 64 |  | √ | 0 | 采购入库单ID |
| 24 | fauxqty | 本次结算辅助数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次结算辅助数量 |
| 25 | fpurinbillentryseq | 采购入库单分录序号 | int8 | 64 |  | √ | 0 | 采购入库单分录序号 |
| 26 | fsrcbillform | 源单实体 | varchar | 36 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 27 | fbaseqty | 本次结算基本数量 | numeric | 23 | 10 | √ | 0.0000000000 | 本次结算基本数量 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | finvbillentity | 库存单据实体 | varchar | 36 |  | √ | ' ' | 库存单据实体 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_vmisrecordentry_pkey |  | fentryid |
| 2 | idx_pm_vmisrecordentry_fid |  | fid |
