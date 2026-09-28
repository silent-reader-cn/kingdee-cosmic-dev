# PRD产品包需求_维护-plm_rm_prd_upd

## 负责人-多选基础资料表 t_plm_rm_chargeperson

- **表名称：** 负责人-多选基础资料表
- **表名：** t_plm_rm_chargeperson

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rm_chargeperson |  | fpkid |
| 2 | idx_plm_rm_chargeperson_fk |  | fid |

---

## PRD产品包需求_维护-主表 t_plm_rm_prd

- **表名称：** PRD产品包需求_维护-主表
- **表名：** t_plm_rm_prd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | 需求分类 plm_rm_group |
| 3 | fmrdbasedatafield | 关联MRD | int8 | 64 |  | √ | 0 | MRD市场包需求 plm_rm_mrd |
| 4 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fstatus_dpd_date | 状态转换日期 | timestamp | 0 |  |  | null | 状态转换日期 |
| 6 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: high :高 higher :较高 middle :中 lower :较低 low :低 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fsource | 来源 | int8 | 64 |  | √ | 0 | 辅助资料 bos_assistantdata_detail |
| 10 | ftextfield | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fstayday | 当前状态停留时长（废弃） | int8 | 64 |  | √ | 0 | 当前状态停留时长（废弃） |
| 18 | findustry | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业,枚举: elec :机电行业 soft :软件行业 |
| 19 | fexceptedrealiztime1 | 期望实现时间 | timestamp | 0 |  |  | null | 期望实现时间 |
| 20 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 22 | fname | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 25 | fsourceinstructions | 来源说明 | varchar | 50 |  | √ | ' ' | 来源说明 |
| 26 | fbsa1 | BSA | varchar | 50 |  | √ | ' ' | BSA,枚举: Basic :Basic Satisfy :Satisfy Attractive :Attractive |
| 27 | fstatus_keep_days | 当前状态停留时长（天） | int8 | 64 |  | √ | 0 | 当前状态停留时长（天） |
| 28 | fitemstatusid | 状态 | int8 | 64 |  | √ | 0 | 状态 plm_ipd_lc_status |
| 29 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 30 | funiversalgrade1 | 通用等级 | varchar | 50 |  | √ | ' ' | 通用等级,枚举: must :必须 should :应有 could :可有 reprieve :暂缓 never :不必 |
| 31 | ftextareafield | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 32 | fbasedatafield | 工作项图标 | int8 | 64 |  | √ | 0 | 工作项图标 plm_ipditempic |
| 33 | fcurversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 34 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 36 | frelateproject | 关联项目 | int8 | 64 |  | √ | 0 | 项目 plm_ipd_project |
| 37 | ftimedimension | 时间维度 | varchar | 50 |  | √ | ' ' | 时间维度,枚举: A :通用需求 B :长期需求 C :中期需求 D :短期需求 E :定制需求 F :紧急需求 G :已上市产品需求 |
| 38 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 39 | festimatetimedelivery | 预计交付时间 | timestamp | 0 |  |  | null | 预计交付时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_rm_prd_master |  | fmasterid |
| 2 | idx_plm_rm_prd_m0 |  | fmasterid |
| 3 | idx_t_plm_rm_prd_createorg |  | fcreateorgid |
| 4 | pk_plm_rm_prd |  | fid |

---

## PRD产品包需求_维护-多语言表 t_plm_rm_prd_l

- **表名称：** PRD产品包需求_维护-多语言表
- **表名：** t_plm_rm_prd_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 标题 | varchar | 80 |  | √ | ' ' | 标题 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fsourceinstructions | 来源说明 | varchar | 80 |  | √ | ' ' | 来源说明 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_prd_l_0 |  | fid,flocaleid |
| 2 | pk_plm_rm_prd_l |  | fpkid |

---

## PRD产品包需求_维护-使用范围表 t_plm_rm_prd_u

- **表名称：** PRD产品包需求_维护-使用范围表
- **表名：** t_plm_rm_prd_u

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
| 1 | pk_t_plm_rm_prd_u |  | fdataid,fuseorgid |
| 2 | idx_t_plm_rm_prd_u_uo |  | fuseorgid |

---

## 关联子实体-子表 t_plm_ipditembaseinfo_lk

- **表名称：** 关联子实体-子表
- **表名：** t_plm_ipditembaseinfo_lk

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fsbillid | 源单内码 | int8 | 64 |  |  | null | 源单内码 |
| 3 | fstableid | 源单主实体编码 | int8 | 64 |  |  | null | 源单主实体编码 |
| 4 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fpkid | fpkid | int8 | 64 |  | √ | null | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipditembaseinfo_lk |  | fpkid |
| 2 | idx_plm_ipditembaseinfo_lk_fk |  | fid |
