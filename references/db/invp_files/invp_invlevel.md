# 库存计划信息-invp_invlevel

## 库存计划信息-主表 t_invp_invlevel

- **表名称：** 库存计划信息-主表
- **表名：** t_invp_invlevel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fbosorg | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fmax | 最大库存 | numeric | 23 | 10 | √ | 0 | 最大库存 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fecobatch | 经济批量 | numeric | 23 | 10 | √ | 0 | 经济批量 |
| 9 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 10 | fmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 11 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fbaseunitid | 基本单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 13 | fmin | 最小库存 | numeric | 23 | 10 | √ | 0 | 最小库存 |
| 14 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 15 | fmaterialgroupstandard | 物料分类标准 | int8 | 64 |  | √ | 0 | 物料分类标准 bd_materialgroupstandard |
| 16 | fpreprocessingtime | 前处理时间(天) | numeric | 23 | 10 | √ | 0 | 前处理时间(天) |
| 17 | fwarehouse | 仓库 | int8 | 64 |  | √ | 0 | 仓库 bd_warehouse |
| 18 | fsafeinvdays | 安全库存天数 | numeric | 23 | 10 | √ | 0 | 安全库存天数 |
| 19 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 21 | freorder | 再订货点 | numeric | 23 | 10 | √ | 0 | 再订货点 |
| 22 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 23 | fdimension | 库存水位维度 | int8 | 64 |  | √ | 0 | 库存水位维度 invp_leveldimension |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 25 | fmaterialgroup | 物料分类 | int8 | 64 |  | √ | 0 | 物料分类 bd_materialgroup |
| 26 | fsupplytype | 订货类型 | bpchar | 1 |  | √ | 'A' | 订货类型,枚举: A :周 B :月 |
| 27 | forderperiod | 订货周期(天) | numeric | 23 | 10 | √ | 0 | 订货周期(天) |
| 28 | freplenishmentpolicy | 补货策略 | varchar | 50 |  | √ | ' ' | 补货策略,枚举: PURCHASE :采购 TRANS :调拨 |
| 29 | fdailyconsume | 平均消耗量 | numeric | 23 | 10 | √ | 0 | 平均消耗量 |
| 30 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 31 | fdeliverytime | 供应商交期(天) | numeric | 23 | 10 | √ | 0 | 供应商交期(天) |
| 32 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 33 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 34 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 35 | fplangroup | 计划组 | int8 | 64 |  | √ | 0 | 供应链业务组 bd_operatorgroup |
| 36 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 37 | fleadtime | 累计提前期(天) | numeric | 23 | 10 | √ | 0 | 累计提前期(天) |
| 38 | furgentinvdays | 紧急补货天数 | numeric | 23 | 10 | √ | 0 | 紧急补货天数 |
| 39 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 41 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 42 | ftgtinvdays | 目标库存天数 | numeric | 23 | 10 | √ | 0 | 目标库存天数 |
| 43 | fsafeinv | 安全库存 | numeric | 23 | 10 | √ | 0 | 安全库存 |
| 44 | ffixbatch | 固定批量 | numeric | 23 | 10 | √ | 0 | 固定批量 |
| 45 | fpostprocessingtime | 后处理时间(天) | numeric | 23 | 10 | √ | 0 | 后处理时间(天) |
| 46 | fplanner | 计划员 | int8 | 64 |  | √ | 0 | 供应链业务员 bd_operator |
| 47 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 48 | fbatchpolicy | 批量政策 | varchar | 50 |  | √ | ' ' | 批量政策,枚举: DIRECT :直接批量 ECO :经济批量 FIX :固定批量 |
| 49 | fmainplantype | 计划类型 | bpchar | 1 |  | √ | 'A' | 计划类型,枚举: A :再订货点 B :最大最小 D :固定期间 E :安全库存 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_invlv_fmaterial |  | fmaterial |
| 2 | idx_invp_invlv_fnumber |  | fnumber |
| 3 | idx_t_invp_invlevel_master |  | fmasterid |
| 4 | pk_t_invp_invlevel |  | fid |
| 5 | idx_t_invp_invlevel_createorg |  | fcreateorgid |

---

## 订货日期-多选基础资料表 t_invp_levelsupplyday

- **表名称：** 订货日期-多选基础资料表
- **表名：** t_invp_levelsupplyday

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 补货日期 invp_supplyday |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_lvsup_day_fid |  | fid |
| 2 | pk_t_invp_levelsupplyday |  | fpkid |

---

## 库存计划信息-使用范围表 t_invp_invlevel_u

- **表名称：** 库存计划信息-使用范围表
- **表名：** t_invp_invlevel_u

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
| 1 | pk_t_invp_invlevel_u |  | fdataid,fuseorgid |
| 2 | idx_t_invp_invlevel_u_uo |  | fuseorgid |

---

## 库存计划信息-多语言表 t_invp_invlevel_l

- **表名称：** 库存计划信息-多语言表
- **表名：** t_invp_invlevel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_invp_lv_l_fid_floc |  | fid,flocaleid |
| 2 | pk_t_invp_invlevel_l |  | fpkid |
