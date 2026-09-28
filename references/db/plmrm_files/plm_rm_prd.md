# PRD产品包需求-plm_rm_prd

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

## PRD产品包需求-主表 t_plm_rm_prd

- **表名称：** PRD产品包需求-主表
- **表名：** t_plm_rm_prd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | [需求分类 plm_rm_group](../plmrm_files/plm_rm_group.md) |
| 3 | fmrdbasedatafield | 关联MRD | int8 | 64 |  | √ | 0 | [MRD市场包需求 plm_rm_mrd](../plmrm_files/plm_rm_mrd.md) |
| 4 | frelatermchangebillnum | 关联变更单 | varchar | 255 |  | √ | ' ' | 关联变更单 |
| 5 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fstatus_dpd_date | 状态转换日期 | timestamp | 0 |  |  | null | 状态转换日期 |
| 7 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: high :高 higher :较高 middle :中 lower :较低 low :低 |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fupversiondes | 修订描述 | varchar | 500 |  | √ | ' ' | 修订描述 |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fsource | 来源 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 12 | frmchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: nochange : changing :变更中 |
| 13 | ftextfield | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 20 | fflowsign | 流程标识 | bpchar | 1 |  | √ | '0' | 流程标识 |
| 21 | frelatermchangebill | 关联变更单id | int8 | 64 |  | √ | 0 | 关联变更单id |
| 22 | fstayday | 当前状态停留时长（废弃） | int8 | 64 |  | √ | 0 | 当前状态停留时长（废弃） |
| 23 | fcurversionid | 当前版本ID | int8 | 64 |  | √ | 0 | 当前版本ID |
| 24 | findustry | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业,枚举: elec :机电行业 soft :软件行业 |
| 25 | fexceptedrealiztime1 | 期望实现时间 | timestamp | 0 |  |  | null | 期望实现时间 |
| 26 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 27 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fname | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 30 | frmtpl | 需求模板 | int8 | 64 |  | √ | 0 | [RR原始需求模板 plm_rm_rr_common_tpl](../plmrm_files/plm_rm_rr_common_tpl.md) |
| 31 | fdescription | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 32 | fsourceinstructions | 来源说明 | varchar | 50 |  | √ | ' ' | 来源说明 |
| 33 | fistempversion | 是否临时版本 | bpchar | 1 |  | √ | '0' | 是否临时版本 |
| 34 | fbsa1 | BSA | varchar | 50 |  | √ | ' ' | BSA,枚举: Basic :Basic Satisfy :Satisfy Attractive :Attractive |
| 35 | fstatus_keep_days | 当前状态停留时长（天） | int8 | 64 |  | √ | 0 | 当前状态停留时长（天） |
| 36 | fitemstatusid | 状态 | int8 | 64 |  | √ | 0 | [状态 plm_ipd_lc_status](../plmipdsm_files/plm_ipd_lc_status.md) |
| 37 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 38 | funiversalgrade1 | 通用等级 | varchar | 50 |  | √ | ' ' | 通用等级,枚举: must :必须 should :应有 could :可有 reprieve :暂缓 never :不必 |
| 39 | ftextareafield | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 40 | fbasedatafield | 工作项图标 | int8 | 64 |  | √ | 0 | [工作项图标 plm_ipditempic](../plmipdsm_files/plm_ipditempic.md) |
| 41 | fcurversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 42 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 43 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 44 | frelateproject | 关联项目 | int8 | 64 |  | √ | 0 | [项目 plm_ipd_project](../plmpm_files/plm_ipd_project.md) |
| 45 | ftimedimension | 时间维度 | varchar | 50 |  | √ | ' ' | 时间维度,枚举: A :通用需求 B :长期需求 C :中期需求 D :短期需求 E :定制需求 F :紧急需求 G :已上市产品需求 |
| 46 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 47 | flatestver | 是否最新版本 | bpchar | 1 |  | √ | '1' | 是否最新版本 |
| 48 | festimatetimedelivery | 预计交付时间 | timestamp | 0 |  |  | null | 预计交付时间 |

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

## PRD产品包需求-多语言表 t_plm_rm_prd_l

- **表名称：** PRD产品包需求-多语言表
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

## PRD产品包需求-使用范围表 t_plm_rm_prd_u

- **表名称：** PRD产品包需求-使用范围表
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
