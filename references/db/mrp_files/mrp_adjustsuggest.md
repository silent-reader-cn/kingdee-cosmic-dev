# 调整建议-mrp_adjustsuggest

## 调整建议-分表 t_mrp_adjustsuggest_e

- **表名称：** 调整建议-分表
- **表名：** t_mrp_adjustsuggest_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fadjuststrategy | 调整策略 | varchar | 50 |  | √ | ' ' | 调整策略,枚举: C :不调整 A :整单调整 B :部分调整 |
| 3 | flineid | 单据行号ID | varchar | 50 |  | √ | ' ' | 单据行号ID |
| 4 | fconfiguredcode | 配置号 | int8 | 64 |  | √ | 0 | [配置号（废弃） bd_configuredcode](../sbd_files/bd_configuredcode.md) |
| 5 | fbillid | 单据ID | varchar | 50 |  | √ | ' ' | 单据ID |
| 6 | fauxprop | 辅助属性 | int8 | 64 |  | √ | 0 | null 001 |
| 7 | ftracknumber | 跟踪号 | int8 | 64 |  | √ | 0 | [跟踪号 bd_tracknumber](../sbd_files/bd_tracknumber.md) |
| 8 | fbonded | 保税 | bpchar | 1 |  | √ | '0' | 保税 |
| 9 | fadjustdatetype | 调整日期类型 | varchar | 50 |  | √ | ' ' | 调整日期类型 |
| 10 | flicenseno | 许可证编号 | int8 | 64 |  | √ | 0 | [许可证 bd_licence](../sbd_files/bd_licence.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_adjustsuggest_e |  | fid |

---

## 调整建议-主表 t_mrp_adjustsuggest

- **表名称：** 调整建议-主表
- **表名：** t_mrp_adjustsuggest

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsupplyorg | 供应组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fadjustcause | 调整原因 | varchar | 500 |  | √ | ' ' | 调整原因 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fbaseunit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fadjustsuggest | 调整类型 | varchar | 30 |  | √ | ' ' | 调整类型,枚举: 0 :建议取消 1 :建议延后 2 :建议提前 |
| 9 | fplannum | 计划运算号 | int8 | 64 |  | √ | 0 | [运算日志 mrp_caculate_log](../msplan_files/mrp_caculate_log.md) |
| 10 | fadjustdate | 调整可用日期 | timestamp | 0 |  |  | null | 调整可用日期 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fpurchaser | 采购员 | int8 | 64 |  | √ | 0 | [供应链业务员 bd_operator](../sbd_files/bd_operator.md) |
| 13 | fschduler | 计划员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsupplier | 供应商 | int8 | 64 |  | √ | 0 | 供应商 bd_supplier |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fsuggestdate | 建议可用日期 | timestamp | 0 |  |  | null | 建议可用日期 |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | flineno | 单据行号 | int4 | 32 |  | √ | 0 | 单据行号 |
| 21 | fmateriel | 物料 | int8 | 64 |  | √ | 0 | [物料 bd_material](../basedata_files/bd_material.md) |
| 22 | fmaterialattr | 物料属性 | varchar | 30 |  | √ | ' ' | 物料属性,枚举: 10030 :自制件 10040 :外购件 10050 :外协件 10020 :虚拟件 10060 :内协件 |
| 23 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 24 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 25 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 28 | fdealer | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | freleasestatus | 释放状态 | bpchar | 1 |  | √ | '0' | 释放状态 |
| 31 | fentryseq | 行号 | varchar | 50 |  | √ | ' ' | 行号 |
| 32 | forigindate | 原可用日期 | timestamp | 0 |  |  | null | 原可用日期 |
| 33 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 34 | fdealdate | 处理时间 | timestamp | 0 |  |  | null | 处理时间 |
| 35 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 37 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 38 | fbilltypeid | 供应单据实体 | varchar | 30 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_material |  | fmateriel |
| 2 | idx_mrp_adjustsuggest |  | fplannum |
| 3 | idx_mrp_adjustsuggest_entryseq |  | fentryseq |
| 4 | idx_t_mrp_adjustsuggest_createorg |  | fcreateorgid |
| 5 | idx_t_mrp_adjustsuggest_master |  | fmasterid |
| 6 | pk_t_mrp_adjustsuggest |  | fid |

---

## 调整建议-使用范围表 t_mrp_adjustsuggest_u

- **表名称：** 调整建议-使用范围表
- **表名：** t_mrp_adjustsuggest_u

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
| 1 | pk_t_mrp_adjustsuggest_u |  | fdataid,fuseorgid |
| 2 | idx_t_mrp_adjustsuggest_u_uo |  | fuseorgid |

---

## 调整建议-使用范围位图表 t_mrp_adjustsuggest_m

- **表名称：** 调整建议-使用范围位图表
- **表名：** t_mrp_adjustsuggest_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mrp_adjustsuggest_m |  | forgid |

---

## 调整建议-多语言表 t_mrp_adjustsuggest_l

- **表名称：** 调整建议-多语言表
- **表名：** t_mrp_adjustsuggest_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mrp_adjustsuggest_l |  | fid,flocaleid |
| 2 | pk_t_mrp_adjustsuggest_l |  | fpkid |
