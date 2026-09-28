# 生产事务类型-mpdm_transactproduct

## 生产事务类型-分表 t_mpdm_traproduct_d

- **表名称：** 生产事务类型-分表
- **表名：** t_mpdm_traproduct_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foutconversionruleid | 转换规则 | varchar | 36 |  | √ | ' ' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 3 | fxkinvsource | 入库来源 | varchar | 50 |  | √ | 'MO' | 入库来源,枚举: MO :生产工单 MORPT :生产汇报 |
| 4 | fgenfollowpurbill | 生成后续采购单据 | varchar | 30 |  | √ | ' ' | 生成后续采购单据,枚举: T :是 F :否 |
| 5 | fisautocreat | 自动生成 | bpchar | 1 |  | √ | '0' | 自动生成 |
| 6 | fisreleasetechnis | 工单下达自动下达工序计划 | bpchar | 1 |  | √ | '0' | 工单下达自动下达工序计划 |
| 7 | fbackflusherr | 倒冲失败中止审核 | bpchar | 1 |  | √ | '0' | 倒冲失败中止审核 |
| 8 | fmaterialsource | 用料清单库存发料信息来源 | varchar | 30 |  | √ | ' ' | 用料清单库存发料信息来源,枚举: A :BOM B :物料生产信息 |
| 9 | ftransapplytype | 调拨方式 | varchar | 2 |  | √ | 'RE' | 调拨方式,枚举: RE :调拨申请 DI :直接调拨 |
| 10 | fconversionrule | 转换规则 | varchar | 36 |  | √ | ' ' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 11 | fpickstatus | 手工关闭时领料状态控制 | varchar | 50 |  | √ | 'C' | 手工关闭时领料状态控制,枚举: A :未领料 B :部分领料 C :全部领料 D :超额领料 |
| 12 | ftaskstatus | 手工关闭时任务状态控制 | varchar | 50 |  | √ | 'C' | 手工关闭时任务状态控制,枚举: A :未开工 B :开工 C :完工 D :部分完工 |
| 13 | freturnbackflush | 退库倒冲 | bpchar | 1 |  | √ | ' ' | 退库倒冲 |
| 14 | foprstatus | 工序状态 | varchar | 50 |  | √ | 'F' | 工序状态,枚举: A :创建 B :计划 C :计划确认 D :下达 E :开工 F :完工 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_traproduct_d_pkey |  | fid |
| 2 | idx_mpdm_trans_d_frule |  | fconversionrule |

---

## BOM类型-多选基础资料表 t_mpdm_trabomtypes

- **表名称：** BOM类型-多选基础资料表
- **表名：** t_mpdm_trabomtypes

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [BOM类型 mpdm_bomtype](../mpdm_files/mpdm_bomtype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_trabomtypes |  | fid |
| 2 | pk_t_mpdm_trabomtypes |  | fpkid |

---

## 生产事务类型-主表 t_mpdm_traproduct

- **表名称：** 生产事务类型-主表
- **表名：** t_mpdm_traproduct

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fshutdowncontrol | 停产控制 | varchar | 30 |  | √ | ' ' | 停产控制,枚举: 1 :不控制 2 :仅支持停产 3 :不支持停产 |
| 3 | fiswarehousquality | 允许入库后质检 | bpchar | 1 |  | √ | '0' | 允许入库后质检 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fbackflushtime | 倒冲时机 | varchar | 30 |  | √ | ' ' | 倒冲时机,枚举: A :入库倒冲 B :汇报倒冲 |
| 6 | ftransactiontype | 业务类型 | int8 | 64 |  | √ | 0 | [业务类型 bd_biztype](../sbd_files/bd_biztype.md) |
| 7 | fisprocedure | 启用工序管理 | bpchar | 1 |  | √ | '0' | 启用工序管理 |
| 8 | freportcontrolrang | 汇报领料控制范围 | varchar | 30 |  | √ | ' ' | 汇报领料控制范围,枚举: A :非倒冲物料 B :关键物料 C :全部物料 |
| 9 | fisstockchange | 启用用料清单变更 | bpchar | 1 |  | √ | '0' | 启用用料清单变更 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fstockmaterials | 用料清单展开方式 | varchar | 30 |  | √ | ' ' | 用料清单展开方式,枚举: A :按BOM展开 B :仅主产品 C :不展开BOM |
| 12 | fbackflushmore | 倒冲数量允许大于需求数量 | bpchar | 1 |  | √ | '0' | 倒冲数量允许大于需求数量 |
| 13 | fallowvaluetype | 允差类型 | varchar | 30 |  | √ | ' ' | 允差类型,枚举: A :数值 B :百分比 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fisprecedingprocess | 里程碑工序完工自动汇报未完工的前工序 | bpchar | 1 |  | √ | '0' | 里程碑工序完工自动汇报未完工的前工序 |
| 16 | fisrework | 返工标识 | bpchar | 1 |  | √ | '0' | 返工标识 |
| 17 | fproctransmaketime | 委外工序发出时机 | varchar | 30 |  | √ | ' ' | 委外工序发出时机,枚举: A :采购申请单审核 B :采购订单审核 |
| 18 | fisautowarehouse | 汇报自动入库 | bpchar | 1 |  | √ | '0' | 汇报自动入库 |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fautoclosebypro | 自动关闭考虑联副产品 | bpchar | 1 |  | √ | '0' | 自动关闭考虑联副产品 |
| 21 | fisreturn | 已消耗不允许退料 | bpchar | 1 |  | √ | '0' | 已消耗不允许退料 |
| 22 | fisreportpick | 汇报完全领料 | bpchar | 1 |  | √ | '0' | 汇报完全领料 |
| 23 | fisvolcal | 自动计算领料 | bpchar | 1 |  | √ | '0' | 自动计算领料 |
| 24 | fautomaketime | 生成时机 | varchar | 30 |  | √ | ' ' | 生成时机,枚举: A :工序计划审核 B :工序计划下达 C :工序转移单审核 |
| 25 | fpomorom | 生产/委外 | varchar | 50 |  | √ | ' ' | 生产/委外,枚举: P :生产 O :委外 |
| 26 | fiswarehousingpick | 入库完全领料 | bpchar | 1 |  | √ | '0' | 入库完全领料 |
| 27 | fisinnerprocess | 内协加工 | bpchar | 1 |  | √ | '0' | 内协加工 |
| 28 | fdeduction | 在制材料扣减 | varchar | 30 |  | √ | ' ' | 在制材料扣减,枚举: A :入库扣减 B :汇报扣减 |
| 29 | fbomtype | BOM类型（废弃） | int8 | 64 |  | √ | 0 | [BOM类型 mpdm_bomtype](../mpdm_files/mpdm_bomtype.md) |
| 30 | fisaudittechnis | 自动审核工序计划 | bpchar | 1 |  | √ | '0' | 自动审核工序计划 |
| 31 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 33 | fisfault | 默认 | bpchar | 1 |  | √ | '0' | 默认 |
| 34 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 35 | fcloseclear | 工单关闭时在制材料清零 | bpchar | 1 |  | √ | '0' | 工单关闭时在制材料清零 |
| 36 | fqtysource | 工序委外订单数量来源 | varchar | 30 |  | √ | ' ' | 工序委外订单数量来源,枚举: A :委外发出数量 B :工序计划数量 |
| 37 | fexecutionmode | 执行模式 | varchar | 30 |  | √ | ' ' | 执行模式,枚举: A :采购模式 B :简单模式 |
| 38 | fbusiprocess | 业务流程 | varchar | 50 |  | √ | ' ' | 业务流程,枚举: 1 :生产工单->完工入库单 2 :生产工单->工单汇报单->完工入库单 3 :生产工单->工序计划->工序汇报单->完工入库单 4 :生产工单->工序计划->工序转移单->完工入库单 |
| 39 | ftransmitbeginwork | 下达即开工 | bpchar | 1 |  | √ | '0' | 下达即开工 |
| 40 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 41 | fallowvalue | 允差判断 | varchar | 30 |  | √ | ' ' | 允差判断,枚举: A :下限 B :上下限 |
| 42 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 43 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 45 | fwarehousrang | 入库领料控制范围 | varchar | 30 |  | √ | ' ' | 入库领料控制范围,枚举: A :非倒冲物料 B :关键物料 C :全部物料 |
| 46 | fisautoclose | 工单自动关闭 | bpchar | 1 |  | √ | '1' | 工单自动关闭 |
| 47 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 48 | fisworkdate | 工时定义 | bpchar | 1 |  | √ | '1' | 工时定义 |
| 49 | fexpandstock | 用料清单展开 | varchar | 30 |  | √ | 'A' | 用料清单展开,枚举: A :工卡 B :手工维护 |
| 50 | fpickbeginwork | 领料即开工 | bpchar | 1 |  | √ | '0' | 领料即开工 |
| 51 | ftechnisrptdim | 汇报维度 | varchar | 30 |  | √ | 'A' | 汇报维度,枚举: A :工时 B :数量 |
| 52 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 53 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 54 | fisauditstock | 自动审核用料清单 | bpchar | 1 |  | √ | '0' | 自动审核用料清单 |
| 55 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 56 | fisautomake | 自动生成 | varchar | 30 |  | √ | ' ' | 自动生成,枚举: T :是 F :否 |
| 57 | fauditrelease | 审核即下达 | bpchar | 1 |  | √ | '0' | 审核即下达 |
| 58 | fmaxallowvalue | 上限允差 | numeric | 23 | 10 | √ | 0.0000000000 | 上限允差 |
| 59 | fisconsiderloss | 用料清单考虑损耗 | bpchar | 1 |  | √ | '0' | 用料清单考虑损耗 |
| 60 | fisbackflush | 自动倒冲 | bpchar | 1 |  | √ | '0' | 自动倒冲 |
| 61 | fproducttype | 生产类型 | varchar | 30 |  |  | ' ' | 生产类型,枚举: A :标准生产 B :返工生产 C :在产改制 D :库存改制 |
| 62 | fwarehouscontrol | 入库领料控制强度 | varchar | 30 |  | √ | ' ' | 入库领料控制强度,枚举: A :警告 B :严格控制 |
| 63 | fissyspre | 初始化 | bpchar | 1 |  | √ | '0' | 初始化 |
| 64 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 65 | freportcontrol | 汇报领料控制强度 | varchar | 30 |  | √ | ' ' | 汇报领料控制强度,枚举: A :警告 B :严格控制 |
| 66 | fpurbillmakemethod | 采购单据生成方式 | varchar | 30 |  | √ | ' ' | 采购单据生成方式,枚举: A :工序转移单生成 B :工序计划生成 |
| 67 | fisforceclose | 允许无条件手工关闭 | bpchar | 1 |  | √ | '0' | 允许无条件手工关闭 |
| 68 | freturncontrol | 已消耗不允许退料控制强度 | varchar | 30 |  | √ | 'A' | 已消耗不允许退料控制强度,枚举: A :警告 B :严格控制 |
| 69 | fcontrolscope | 计算领料控制范围 | varchar | 30 |  | √ | ' ' | 计算领料控制范围,枚举: A :非倒冲物料 B :关键物料 C :全部物料 |
| 70 | fminallowvalue | 下限允差 | numeric | 23 | 10 | √ | 0.0000000000 | 下限允差 |
| 71 | fisproceduremust | 工艺路线必录 | bpchar | 1 |  | √ | '0' | 工艺路线必录 |
| 72 | ftechnissrc | 工序计划来源 | varchar | 30 |  | √ | 'A' | 工序计划来源,枚举: A :工卡 B :手工维护 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_traproduct |  | fnumber,fcreateorgid |
| 2 | idx_t_mpdm_traproduct_master |  | fmasterid |
| 3 | idx_t_mpdm_traproduct_createorg |  | fcreateorgid |
| 4 | t_mpdm_traproduct_pkey |  | fid |

---

## 生产事务类型-使用范围表 t_mpdm_traproduct_u

- **表名称：** 生产事务类型-使用范围表
- **表名：** t_mpdm_traproduct_u

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
| 1 | idx_t_mpdm_traproduct_u_uo |  | fuseorgid |
| 2 | t_mpdm_traproduct_u_pkey |  | fdataid,fuseorgid |

---

## 生产事务类型-多语言表 t_mpdm_traproduct_l

- **表名称：** 生产事务类型-多语言表
- **表名：** t_mpdm_traproduct_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_traproduct_l_pkey |  | fpkid |
| 2 | idx_mpdm_trans_l |  | fid,flocaleid |

---

## 生产事务类型-使用范围位图表 t_mpdm_traproduct_m

- **表名称：** 生产事务类型-使用范围位图表
- **表名：** t_mpdm_traproduct_m

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
| 1 | pk_t_mpdm_traproduct_m |  | forgid |
