# 简单委外事务类型-mpdm_transactout

## 简单委外事务类型-多语言表 t_mpdm_transactout_l

- **表名称：** 简单委外事务类型-多语言表
- **表名：** t_mpdm_transactout_l

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
| 1 | idx_mpdm_transactoutl_fid |  | fid,flocaleid |
| 2 | t_mpdm_transactout_l_pkey |  | fpkid |

---

## 简单委外事务类型-使用范围位图表 t_mpdm_transactout_m

- **表名称：** 简单委外事务类型-使用范围位图表
- **表名：** t_mpdm_transactout_m

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
| 1 | pk_t_mpdm_transactout_m |  | forgid |

---

## 简单委外事务类型-使用范围表 t_mpdm_transactout_u

- **表名称：** 简单委外事务类型-使用范围表
- **表名：** t_mpdm_transactout_u

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
| 1 | t_mpdm_transactout_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_transactout_u_uo |  | fuseorgid |

---

## 简单委外事务类型-主表 t_mpdm_transactout

- **表名称：** 简单委外事务类型-主表
- **表名：** t_mpdm_transactout

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fbackflushtime | 倒冲时机 | varchar | 30 |  | √ | ' ' | 倒冲时机,枚举: A :入库倒冲 |
| 4 | ftransactiontype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 5 | fisstockchange | 启用委外组件清单变更 | bpchar | 1 |  | √ | '0' | 启用委外组件清单变更 |
| 6 | fbackflusherr | 倒冲失败中止审核 | bpchar | 1 |  | √ | '0' | 倒冲失败中止审核 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbackflushmore | 倒冲数量允许大于需求数量 | bpchar | 1 |  | √ | '0' | 倒冲数量允许大于需求数量 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fwarehousrang | 控制范围 | varchar | 30 |  | √ | ' ' | 控制范围,枚举: A :非倒冲物料 B :关键物料 C :全部物料 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fisreturn | 已消耗不允许退料 | bpchar | 1 |  | √ | '0' | 已消耗不允许退料 |
| 17 | ffeedtype | 投料方式 | varchar | 30 |  | √ | ' ' | 投料方式,枚举: A :展BOM B :手工录入 C :不投料 D :已投料 E :仅委外件 |
| 18 | fisvolcal | 自动计算领料 | bpchar | 1 |  | √ | '0' | 自动计算领料 |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fisauditstock | 自动审核组件清单 | bpchar | 1 |  | √ | '0' | 自动审核组件清单 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fisconsiderloss | 委外组件清单考虑损耗 | bpchar | 1 |  | √ | '1' | 委外组件清单考虑损耗 |
| 24 | fisbackflush | 自动倒冲 | bpchar | 1 |  | √ | '0' | 自动倒冲 |
| 25 | fiswarehousingpick | 入库完全领料 | bpchar | 1 |  | √ | '0' | 入库完全领料 |
| 26 | fmaterialsource | 组件清单库存发料信息来源 | varchar | 50 |  | √ | ' ' | 组件清单库存发料信息来源,枚举: A :BOM B :物料生产信息 |
| 27 | fdeduction | 在制材料扣减 | varchar | 50 |  | √ | ' ' | 在制材料扣减,枚举: A :入库扣减 |
| 28 | fwarehouscontrol | 控制强度 | varchar | 30 |  | √ | ' ' | 控制强度,枚举: A :警告 B :严格控制 |
| 29 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 30 | fbomtype | BOM类型(废弃) | int8 | 64 |  | √ | 0 | BOM类型 mpdm_bomtype |
| 31 | freturncontrol | 控制强度 | varchar | 30 |  | √ | 'A' | 控制强度,枚举: A :警告 B :严格控制 |
| 32 | fcontrolscope | 计算领料控制范围 | varchar | 30 |  | √ | ' ' | 计算领料控制范围,枚举: A :非倒冲物料 B :关键物料 C :全部物料 |
| 33 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 34 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 35 | fisfault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 36 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_transactout_pkey |  | fid |
| 2 | idx_t_mpdm_transactout_master |  | fmasterid |
| 3 | idx_mpdm_transactout_fnumber |  | fnumber |
| 4 | idx_t_mpdm_transactout_createorg |  | fcreateorgid |

---

## BOM类型-多选基础资料表 t_mpdm_transoutbomtypes

- **表名称：** BOM类型-多选基础资料表
- **表名：** t_mpdm_transoutbomtypes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | BOM类型 mpdm_bomtype |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpdm_transoutbomtypes |  | fpkid |
| 2 | idx_mpdm_transoutbomtypes |  | fid |
