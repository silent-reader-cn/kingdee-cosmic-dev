# 生产线-arm_linecapacity

## 物料明细-子表 t_arm_materialentry

- **表名称：** 物料明细-子表
- **表名：** t_arm_materialentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaterialprdinfo | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 3 | felapsedate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | fproductunit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 5 | fpriority | 生产优先级 | numeric | 23 | 10 | √ | 9999 | 生产优先级 |
| 6 | flocation | 完工入库仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fmaterialversion | 物料版本 | int8 | 64 |  | √ | 0 | 物料版本 bd_bomversion_new |
| 9 | fprimaryline | 主生产线 | bpchar | 1 |  | √ | '0' | 主生产线 |
| 10 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 11 | fmaterialmaster | 物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 12 | fwarehouse | 完工入库仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 13 | fauxproperty | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 14 | fbomcode | BOM编码 | int8 | 64 |  | √ | 0 | BOM维护 pdm_mftbom |
| 15 | fworkhour | 准备工时 | numeric | 23 | 10 | √ | 0 | 准备工时 |
| 16 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 17 | fquantity | 产量 | numeric | 23 | 10 | √ | 0 | 产量 |
| 18 | fmatcycletime | 生产周期 | numeric | 23 | 10 | √ | 0 | 生产周期 |

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
| 6 | fadjustworkhour | 调整工时 | numeric | 23 | 10 | √ | 0 | 调整工时 |

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
| 4 | fuseorg | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | flinestore | 线边仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fcycletime | 标准生产周期 | numeric | 23 | 10 | √ | 0 | 标准生产周期 |
| 10 | fstartdatecalculate | 提前期计算方式 | varchar | 50 |  | √ | ' ' | 提前期计算方式,枚举: 1 :按生产周期 2 :按物料提前期 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fstdworkhour | 标准准备工时 | numeric | 23 | 10 | √ | 0 | 标准准备工时 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fplangroup | 计划分组 | varchar | 50 |  | √ | ' ' | 计划分组 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fcreateorgid | 生产组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fname | 生产线名称 | varchar | 50 |  | √ | ' ' | 生产线名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fschedulemode | 排产方式 | varchar | 50 |  | √ | ' ' | 排产方式,枚举: 1 :产量 2 :生产周期 |
| 23 | fproductdept | 车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 24 | finwarorg | 库存组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 25 | flinebin | 线边仓位 | int8 | 64 |  | √ | 0 | 仓位 bd_location |
| 26 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 27 | flinenum | 产线数量 | int8 | 64 |  | √ | 0 | 产线数量 |
| 28 | fprdunit | 产量单位 | varchar | 50 |  | √ | ' ' | 产量单位,枚举: h :单位/小时 d :单位/日 |
| 29 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 30 | fnumber | 生产线编码 | varchar | 30 |  | √ | ' ' | 生产线编码 |
| 31 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 32 | fstdproduction | 标准产量 | numeric | 23 | 10 | √ | 0 | 标准产量 |

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
