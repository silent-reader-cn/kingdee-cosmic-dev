# 维修计划工具需求-mpdm_repairplantool

## 维修计划工具需求-主表 t_mpdm_repairplantool

- **表名称：** 维修计划工具需求-主表
- **表名：** t_mpdm_repairplantool

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 8 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 14 | fisneedtool | 需要工具 | bpchar | 1 |  | √ | '0' | 需要工具 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | frepairplancard | 维修计划工卡编码 | int8 | 64 |  | √ | 0 | 维修计划工卡 mpdm_maintenanceplan |
| 20 | fmaterialtype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |
| 21 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 23 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_repairplantool |  | fid |
| 2 | idx_t_mpdm_repairplantool_createorg |  | fcreateorgid |
| 3 | idx_t_mpdm_repairplantool_master |  | fmasterid |
| 4 | t_mpdm_rpt_frpcard_idx |  | frepairplancard |
| 5 | t_mpdm_rpt_fcreateorgid_idx |  | fcreateorgid |

---

## 工具清单-子表 t_mpdm_repairptentry

- **表名称：** 工具清单-子表
- **表名：** t_mpdm_repairptentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentrybaseunit | 基本单位(封存) | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 3 | ftoolusability | 工具适用性 | varchar | 255 |  | √ | ' ' | 工具适用性 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | ftoolsubgroup | ftoolsubgroup | int8 | 64 |  | √ | 0 |  |
| 6 | fsupplyduty | 供货责任 | varchar | 50 |  | √ | ' ' | 供货责任,枚举: A :业务组织 B :客户 |
| 7 | fentryunit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 8 | fentrybaseqty | 基本数量 | numeric | 23 | 10 | √ | 0 | 基本数量 |
| 9 | fentryqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 10 | frefertocustcode | 参考的客户手册代码 | varchar | 255 |  | √ | ' ' | 参考的客户手册代码 |
| 11 | fmaterial | 工具件号 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 12 | frefermanualversion | 参考手册的版本号 | varchar | 255 |  | √ | ' ' | 参考手册的版本号 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fbasedatapropfield | fbasedatapropfield | varchar | 50 |  | √ | ' ' |  |
| 15 | ftooluselevel | 工具使用级别 | varchar | 50 |  | √ | ' ' | 工具使用级别,枚举: A :必录 B :可选 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_repairptentry_fk |  | fid |
| 2 | pk_mpdm_repairptentry |  | fentryid |

---

## 维修计划工具需求-使用范围位图表 t_mpdm_repairplantool_m

- **表名称：** 维修计划工具需求-使用范围位图表
- **表名：** t_mpdm_repairplantool_m

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
| 1 | pk_t_mpdm_repairplantool_m |  | forgid |

---

## 维修计划工具需求-多语言表 t_mpdm_repairplantool_l

- **表名称：** 维修计划工具需求-多语言表
- **表名：** t_mpdm_repairplantool_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_repairplantool_l |  | fpkid |
| 2 | idx_mpdm_repairplantool_l_0 |  | fid,flocaleid |

---

## 维修计划工具需求-使用范围表 t_mpdm_repairplantool_u

- **表名称：** 维修计划工具需求-使用范围表
- **表名：** t_mpdm_repairplantool_u

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
| 1 | idx_t_mpdm_repairplantool_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_repairplantool_u |  | fdataid,fuseorgid |
