# AR分配需求_维护-plm_rm_ar_elec_upd

## 关联项目-多选基础资料表 t_plm_rm_relateprojects

- **表名称：** 关联项目-多选基础资料表
- **表名：** t_plm_rm_relateprojects

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [项目 plm_ipd_project](../plmpm_files/plm_ipd_project.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rm_relateprojects |  | fpkid |
| 2 | idx_plm_rm_relateprojects_fk |  | fid |

---

## 负责人-多选基础资料表 t_plm_rm_chargeperson

- **表名称：** 负责人-多选基础资料表
- **表名：** t_plm_rm_chargeperson

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
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

## 关联PRD-多选基础资料表 t_plm_rm_relateprd

- **表名称：** 关联PRD-多选基础资料表
- **表名：** t_plm_rm_relateprd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [PRD产品包需求 plm_rm_prd](../plmrm_files/plm_rm_prd.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_relateprd_fk |  | fid |
| 2 | pk_plm_rm_relateprd |  | fpkid |

---

## 关联任务-多选基础资料表 t_plm_rm_relatetask

- **表名称：** 关联任务-多选基础资料表
- **表名：** t_plm_rm_relatetask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [任务 plm_ipd_task](../plmpm_files/plm_ipd_task.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_relatetask_fk |  | fid |
| 2 | pk_plm_rm_relatetask |  | fpkid |

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

---

## 关联MRD-多选基础资料表 t_plm_rm_relatemrd

- **表名称：** 关联MRD-多选基础资料表
- **表名：** t_plm_rm_relatemrd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [MRD市场包需求 plm_rm_mrd](../plmrm_files/plm_rm_mrd.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_relatemrd_fk |  | fid |
| 2 | pk_plm_rm_relatemrd |  | fpkid |

---

## AR分配需求_维护-使用范围表 t_plm_rm_ar_elec_u

- **表名称：** AR分配需求_维护-使用范围表
- **表名：** t_plm_rm_ar_elec_u

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
| 1 | pk_t_plm_rm_ar_elec_u |  | fdataid,fuseorgid |
| 2 | idx_t_plm_rm_ar_elec_u_uo |  | fuseorgid |

---

## AR分配需求_维护-多语言表 t_plm_rm_ar_elec_l

- **表名称：** AR分配需求_维护-多语言表
- **表名：** t_plm_rm_ar_elec_l

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
| 1 | idx_plm_rm_ar_elec_l_0 |  | fid,flocaleid |
| 2 | pk_plm_rm_ar_elec_l |  | fpkid |

---

## AR分配需求_维护-主表 t_plm_rm_ar_elec

- **表名称：** AR分配需求_维护-主表
- **表名：** t_plm_rm_ar_elec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | [需求分类 plm_rm_group](../plmrm_files/plm_rm_group.md) |
| 3 | frelatermchangebillnum | 关联变更单 | varchar | 255 |  | √ | ' ' | 关联变更单 |
| 4 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fstatus_dpd_date | 状态转换日期 | timestamp | 0 |  |  | null | 状态转换日期 |
| 6 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: high :高 higher :较高 middle :中 lower :较低 low :低 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fupversiondes | 修订描述 | varchar | 500 |  | √ | ' ' | 修订描述 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fsource | 来源 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 11 | frmchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: nochange : changing :变更中 |
| 12 | ftextfield | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 13 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | fflowsign | 流程标识 | bpchar | 1 |  | √ | '0' | 流程标识 |
| 20 | frelatermchangebill | 关联变更单id | int8 | 64 |  | √ | 0 | 关联变更单id |
| 21 | fstayday | 当前状态停留时长（废弃） | int8 | 64 |  | √ | 0 | 当前状态停留时长（废弃） |
| 22 | fcurversionid | 当前版本ID | int8 | 64 |  | √ | 0 | 当前版本ID |
| 23 | findustry | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业,枚举: elec :机电行业 soft :软件行业 |
| 24 | fexceptedrealiztime1 | 期望实现时间 | timestamp | 0 |  |  | null | 期望实现时间 |
| 25 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 26 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 27 | fname | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | frmtpl | 需求模板 | int8 | 64 |  | √ | 0 | [RR原始需求模板 plm_rm_rr_common_tpl](../plmrm_files/plm_rm_rr_common_tpl.md) |
| 30 | fsourceinstructions | 来源说明 | varchar | 50 |  | √ | ' ' | 来源说明 |
| 31 | fistempversion | 是否临时版本 | bpchar | 1 |  | √ | '0' | 是否临时版本 |
| 32 | fbsa1 | BSA | varchar | 50 |  | √ | ' ' | BSA,枚举: Basic :Basic Satisfy :Satisfy Attractive :Attractive |
| 33 | fstatus_keep_days | 当前状态停留时长（天） | int8 | 64 |  | √ | 0 | 当前状态停留时长（天） |
| 34 | fitemstatusid | 状态 | int8 | 64 |  | √ | 0 | [状态 plm_ipd_lc_status](../plmipdsm_files/plm_ipd_lc_status.md) |
| 35 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 36 | funiversalgrade1 | 通用等级 | varchar | 50 |  | √ | ' ' | 通用等级,枚举: must :必须 should :应有 could :可有 reprieve :暂缓 never :不必 |
| 37 | ftextareafield | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 38 | fbasedatafield | 工作项图标 | int8 | 64 |  | √ | 0 | [工作项图标 plm_ipditempic](../plmipdsm_files/plm_ipditempic.md) |
| 39 | fcurversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 40 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 41 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 42 | frelateproject | 关联项目 | int8 | 64 |  | √ | 0 | [项目 plm_ipd_project](../plmpm_files/plm_ipd_project.md) |
| 43 | ftimedimension | 时间维度 | varchar | 50 |  | √ | ' ' | 时间维度,枚举: A :通用需求 B :长期需求 C :中期需求 D :短期需求 E :定制需求 F :紧急需求 G :已上市产品需求 |
| 44 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 45 | flatestver | 是否最新版本 | bpchar | 1 |  | √ | '1' | 是否最新版本 |
| 46 | festimatetimedelivery | 预计交付时间 | timestamp | 0 |  |  | null | 预计交付时间 |
| 47 | fworkload | 工作量（人天） | numeric | 23 | 1 | √ | 0 | 工作量（人天） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_rm_ar_elec_m0 |  | fmasterid |
| 2 | pk_plm_rm_ar_elec |  | fid |
| 3 | idx_t_plm_rm_ar_elec_createorg |  | fcreateorgid |
| 4 | idx_t_plm_rm_ar_elec_master |  | fmasterid |
