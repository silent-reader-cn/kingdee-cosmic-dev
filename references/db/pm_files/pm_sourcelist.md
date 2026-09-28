# 货源清单-pm_sourcelist

## 货源明细-子表 t_pm_sourcelistentry

- **表名称：** 货源明细-子表
- **表名：** t_pm_sourcelistentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmaxbillqty | 最大订货量 | numeric | 23 | 10 | √ | 0.0000000000 | 最大订货量 |
| 3 | fentrymodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fmaterialid | 物料编码 | int8 | 64 |  | √ | 0 | [物料采购信息 bd_materialpurchaseinfo](../sbd_files/bd_materialpurchaseinfo.md) |
| 5 | fmaterialgroupid | 类别编码 | int8 | 64 |  | √ | 0 | [物料分类 bd_materialgroup](../basedata_files/bd_materialgroup.md) |
| 6 | funitid | 采购单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fminbillqty | 最小订货量 | numeric | 23 | 10 | √ | 0.0000000000 | 最小订货量 |
| 8 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 9 | feffectdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 10 | fisvmi | VMI | bpchar | 1 |  | √ | ' ' | VMI |
| 11 | fentrycreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsrctype | 来源类型 | varchar | 5 |  | √ | ' ' | 来源类型,枚举: A :新增 B :协同同步 |
| 13 | fpackagelotbaseqty | 最小包装量基本数量 | numeric | 23 | 10 | √ | 0 | 最小包装量基本数量 |
| 14 | fentrycreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 15 | ftype | 类型 | varchar | 5 |  | √ | ' ' | 类型,枚举: A :物料 B :类别 |
| 16 | fminbillbaseqty | 最小订货基本数量 | numeric | 23 | 10 | √ | 0 | 最小订货基本数量 |
| 17 | fpackagebatchqty | 包装批量(废弃) | int8 | 64 |  | √ | 0 | 包装批量(废弃) |
| 18 | fentrymodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fexpirydate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 20 | fbillcontrol | 单据控制 | varchar | 5 |  | √ | ' ' | 单据控制,枚举: A :采购订单 |
| 21 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 22 | fpackagelotqty | 最小包装量 | numeric | 23 | 10 | √ | 1 | 最小包装量 |
| 23 | fmaxbillbaseqty | 最大订货基本数量 | numeric | 23 | 10 | √ | 0 | 最大订货基本数量 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_pm_sourcelistentry_pkey |  | fentryid |
| 2 | idx_pm_sourcelistentry |  | fid |

---

## 货源清单-多语言表 t_pm_sourcelist_l

- **表名称：** 货源清单-多语言表
- **表名：** t_pm_sourcelist_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_sourcelist_l |  | fid,flocaleid |
| 2 | t_pm_sourcelist_l_pkey |  | fpkid |

---

## 货源清单-主表 t_pm_sourcelist

- **表名称：** 货源清单-主表
- **表名：** t_pm_sourcelist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fcomment | 备注 | varchar | 512 |  |  | null | 备注 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 采购组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | flastupdateuserid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fsupplierid | 供应商 | int8 | 64 |  | √ | 0 | [供应商 bd_supplier](../basedata_files/bd_supplier.md) |
| 13 | flastupdatetime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fctrlstrategy | fctrlstrategy | varchar | 5 |  | √ | ' ' |  |
| 16 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 21 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pm_sourcelist_fnumber |  | fnumber |
| 2 | idx_pm_sourcelist_supplier |  | fsupplierid |
| 3 | t_pm_sourcelist_pkey |  | fid |
