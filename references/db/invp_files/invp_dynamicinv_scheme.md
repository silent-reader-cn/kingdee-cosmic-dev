# 动态安全库存计算方案-invp_dynamicinv_scheme

## 数据来源-子表 t_invp_dss_scheme_entry

- **表名称：** 数据来源-子表
- **表名：** t_invp_dss_scheme_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fbillentity | 单据名称 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_dss_scheme_entry |  | fentryid |
| 2 | idx_invp_dss_scheme_entry_fk |  | fid |

---

## 动态安全库存计算方案-使用范围表 t_invp_dynamicinv_scheme_u

- **表名称：** 动态安全库存计算方案-使用范围表
- **表名：** t_invp_dynamicinv_scheme_u

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
| 1 | pk_t_invp_dynamicinv_scheme_u |  | fdataid,fuseorgid |
| 2 | idx_t_invp_dynamicinv_scheme_u_uo |  | fuseorgid |

---

## 动态安全库存计算方案-主表 t_invp_dynamicinv_scheme

- **表名称：** 动态安全库存计算方案-主表
- **表名：** t_invp_dynamicinv_scheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialcostsource | 物料成本来源 | varchar | 50 |  | √ | ' ' | 物料成本来源,枚举: materialCost :物料参考成本 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fwritebackmsg | 反写信息 | varchar | 50 |  | √ | ' ' | 反写信息,枚举: invMaterial :物料库存信息 invPlan :库存计划信息 invWarn :库存预警信息 |
| 5 | fcalcycleunit | 计算周期单位 | varchar | 50 |  | √ | ' ' | 计算周期单位,枚举: day :日 month :月 year :年 |
| 6 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 7 | fmateialrange | 物料范围 | varchar | 50 |  | √ | ' ' | 物料范围,枚举: material :指定物料 |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 10 | fcalaccording | 计算依据 | varchar | 50 |  | √ | ' ' | 计算依据,枚举: history :依据历史数据 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | finvdimension | 库存水位维度 | int8 | 64 |  | √ | 0 | [库存水位维度 invp_leveldimension](../invp_files/invp_leveldimension.md) |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fservicedefault | 服务水平缺省值（%） | int8 | 64 |  | √ | 0 | 服务水平缺省值（%） |
| 17 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | factualservice | 实际服务水平（销售） | varchar | 50 |  | √ | ' ' | 实际服务水平（销售）,枚举: otd :订单交付及时率 |
| 20 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 21 | fleadtime | 提前期来源 | varchar | 50 |  | √ | ' ' | 提前期来源,枚举: purStable :采购固定提前期 |
| 22 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fleadtimedefault | 提前期缺省值（天） | int8 | 64 |  | √ | 0 | 提前期缺省值（天） |
| 24 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 25 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fstatisticsunit | 统计周期 | int8 | 64 |  | √ | 0 | 统计周期 |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fname | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 31 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 32 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fnumber | 方案编号 | varchar | 30 |  | √ | ' ' | 方案编号 |
| 34 | fcalalgorithm | 计算算法 | varchar | 50 |  | √ | ' ' | 计算算法,枚举: simple :简单算法 normalDisribution :正态分布 |
| 35 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_invp_dynamicinv_scheme_createorg |  | fcreateorgid |
| 2 | idx_t_invp_dynamicinv_scheme_master |  | fmasterid |
| 3 | pk_invp_dynamicinv_scheme |  | fid |

---

## 动态安全库存计算方案-多语言表 t_invp_dynamicinv_scheme_l

- **表名称：** 动态安全库存计算方案-多语言表
- **表名：** t_invp_dynamicinv_scheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 80 |  | √ | ' ' | 备注 |
| 3 | fname | 方案名称 | varchar | 80 |  | √ | ' ' | 方案名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_invp_dynamicinv_scheme_l |  | fpkid |
| 2 | idx_invp_dynamicinv_scheme_l_0 |  | fid,flocaleid |
