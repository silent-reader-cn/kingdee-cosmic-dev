# 生产线-arm_linecapacity

## 班次-子表 t_arm_shiftentry

- **表名称：** 班次-子表
- **表名：** t_arm_shiftentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fshiftid | 班次 | int8 | 64 |  | √ | 0 | [生产线班次 arm_shift](../arm_files/arm_shift.md) |
| 3 | fshiftendtime | 结束时间 | int8 | 64 |  | √ | 0 | 结束时间 |
| 4 | fshiftplanhour | 计划工时 | numeric | 23 | 10 | √ | 0 | 计划工时 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fshiftnumber | 班次编码 | int8 | 64 |  | √ | 0 | 班次编码 |
| 7 | fshiftname | 班次 | varchar | 500 |  |  | null | 班次 |
| 8 | fshiftstarttime | 开始时间 | int8 | 64 |  | √ | 0 | 开始时间 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_shiftentry |  | fid |
| 2 | pk_t_arm_shiftentry |  | fentryid |

---

## 物料明细-子表 t_arm_materialentry

- **表名称：** 物料明细-子表
- **表名：** t_arm_materialentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialprdinfo | 物料编码 | int8 | 64 |  | √ | 0 | [物料生产信息 bd_materialmftinfo](../sbd_files/bd_materialmftinfo.md) |
| 3 | felapsedate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | fpriority | 排程优先级 | numeric | 23 | 10 | √ | 9999 | 排程优先级 |
| 5 | flocation | 完工入库仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | [物料版本 bd_bomversion_new](../basedata_files/bd_bomversion_new.md) |
| 8 | fprimaryline | 主生产线 | bpchar | 1 |  | √ | '0' | 主生产线 |
| 9 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 10 | fassistunit | 辅助单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 11 | fassistquantity | 辅助单位产量 | numeric | 23 | 10 | √ | 0 | 辅助单位产量 |
| 12 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 13 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | ftracknumberid | ftracknumberid | int8 | 64 |  | √ | 0 |  |
| 15 | fassistcycletime | 辅助单位生产周期 | numeric | 23 | 10 | √ | 0 | 辅助单位生产周期 |
| 16 | fstdpackqty | 标准包装数量 | numeric | 23 | 10 | √ | 0 | 标准包装数量 |
| 17 | fsharegroup | 共享组 | varchar | 50 |  | √ | ' ' | 共享组 |
| 18 | fprdcheck | 产品检验 | bpchar | 1 |  | √ | '0' | 产品检验 |
| 19 | fquantity | 产量 | numeric | 23 | 10 | √ | 0 | 产量 |
| 20 | fproductunit | 生产单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 21 | fprojectid | fprojectid | int8 | 64 |  | √ | 0 |  |
| 22 | fmaterialmaster | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 23 | fwarehouse | 完工入库仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 24 | fratedqty | 额定日产量 | numeric | 23 | 10 | √ | 0 | 额定日产量 |
| 25 | fbomcode | BOM编码 | int8 | 64 |  | √ | 0 | [BOM维护 pdm_mftbom](../fmm_files/pdm_mftbom.md) |
| 26 | flinepriority | 分配优先级 | numeric | 23 | 10 | √ | 9999 | 分配优先级 |
| 27 | fworkhour | 准备工时 | numeric | 23 | 10 | √ | 0 | 准备工时 |
| 28 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 29 | fminqty | 最小生产量 | numeric | 23 | 10 | √ | 0 | 最小生产量 |
| 30 | fmatcycletime | 生产周期 | numeric | 23 | 10 | √ | 0 | 生产周期 |
| 31 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arm_materialentry |  | fentryid |
| 2 | idx_t_arm_materialentry |  | fid |

---

## 产能调整-子表 t_arm_capacityentry

- **表名称：** 产能调整-子表
- **表名：** t_arm_capacityentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadjustdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 3 | fremarks | 备注 | varchar | 500 |  |  | null | 备注 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fshiftselect | 班次 | varchar | 50 |  | √ | ' ' | 班次,枚举: |
| 7 | fadjustworkhour | 调整工时 | numeric | 23 | 10 | √ | 0 | 调整工时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_arm_capacityentry |  | fid |
| 2 | pk_t_arm_capacityentry |  | fentryid |

---

## 生产线-多语言表 t_arm_linecapacity_l

- **表名称：** 生产线-多语言表
- **表名：** t_arm_linecapacity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 生产线名称 | varchar | 50 |  | √ | ' ' | 生产线名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arm_linecapacity_l |  | fpkid |
| 2 | idx_t_arm_lcpct_l |  | fid |

---

## 生产线-主表 t_arm_linecapacity

- **表名称：** 生产线-主表
- **表名：** t_arm_linecapacity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flogo |  | varchar | 255 |  | √ | ' ' |  |
| 3 | fplanworkhour | 日计划工时 | numeric | 23 | 10 | √ | 0 | 日计划工时 |
| 4 | fuseorg | 生产组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | flinestore | 线边仓库 | int8 | 64 |  | √ | 0 | [仓库 bd_warehouse](../sbd_files/bd_warehouse.md) |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcycletime | 标准生产周期 | numeric | 23 | 10 | √ | 0 | 标准生产周期 |
| 10 | fstartdatecalculate | 提前期计算方式 | varchar | 50 |  | √ | ' ' | 提前期计算方式,枚举: 1 :按生产周期 2 :按物料提前期 |
| 11 | funitmode | 单位 | bpchar | 1 |  | √ | '1' | 单位,枚举: 1 :生产单位 2 :辅助单位 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fstdworkhour | 标准准备工时 | numeric | 23 | 10 | √ | 0 | 标准准备工时 |
| 14 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fplangroup | 计划分组 | varchar | 50 |  | √ | ' ' | 计划分组 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 20 | fomwarehouse | 委外仓库设置 | int8 | 64 |  | √ | 0 | [委外仓库设置 om_warehouseset](../om_files/om_warehouseset.md) |
| 21 | fpurorg | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fmanufacturetype | 制造类型 | bpchar | 1 |  | √ | 'C' | 制造类型,枚举: A :离散制造 C :重复制造 |
| 23 | fshiftnum | 班次数 | varchar | 50 |  | √ | '0' | 班次数,枚举: 0 :0 1 :1 2 :2 3 :3 4 :4 |
| 24 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fname | 生产线名称 | varchar | 50 |  | √ | ' ' | 生产线名称 |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fschedulemode | 排产方式 | varchar | 50 |  | √ | ' ' | 排产方式,枚举: 1 :产量 2 :生产周期 |
| 29 | fproductdept | 车间 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | finwarorg | 库存组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | flinebin | 线边仓位 | int8 | 64 |  | √ | 0 | [仓位 bd_location](../sbd_files/bd_location.md) |
| 32 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 33 | flinenum | 产线数量 | int8 | 64 |  | √ | 0 | 产线数量 |
| 34 | fprdunit | 产量单位 | varchar | 50 |  | √ | ' ' | 产量单位,枚举: h :单位/小时 d :单位/日 |
| 35 | fcapacityfactor | 产能系数 | numeric | 23 | 10 | √ | 0 | 产能系数 |
| 36 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 37 | fnumber | 生产线编码 | varchar | 30 |  | √ | ' ' | 生产线编码 |
| 38 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 39 | fstdproduction | 标准产量 | numeric | 23 | 10 | √ | 0 | 标准产量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arm_linecapacity |  | fid |
| 2 | idx_t_arm_lcpct_no |  | fnumber |
| 3 | idx_t_arm_linecapacity_createorg |  | fcreateorgid |
| 4 | idx_t_arm_linecapacity_master |  | fmasterid |

---

## 生产线-使用范围表 t_arm_linecapacity_u

- **表名称：** 生产线-使用范围表
- **表名：** t_arm_linecapacity_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_arm_linecapacity_u |  | fdataid,fuseorgid |
| 2 | idx_t_arm_linecapacity_u_uo |  | fuseorgid |

---

## 班次-多语言表 t_arm_shiftentry_l

- **表名称：** 班次-多语言表
- **表名：** t_arm_shiftentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fshiftname | 班次 | varchar | 255 |  | √ | ' ' | 班次 |
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
| 1 | pk_t_arm_shiftentry_l |  | fpkid |
| 2 | idx_arm_shiftentry_l |  | fentryid,flocaleid |
