# US用户故事_维护-plm_rm_us_soft_upd

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

## US用户故事_维护-主表 t_plm_rm_us_soft

- **表名称：** US用户故事_维护-主表
- **表名：** t_plm_rm_us_soft

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | [需求分类 plm_rm_group](../plmrm_files/plm_rm_group.md) |
| 3 | frelatermchangebillnum | 关联变更单 | varchar | 255 |  | √ | ' ' | 关联变更单 |
| 4 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fupversiondes | 修订描述 | varchar | 500 |  | √ | ' ' | 修订描述 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | ftextfield | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 11 | fflowsign | 流程标识 | bpchar | 1 |  | √ | '0' | 流程标识 |
| 12 | fend | 计划实现周期.结束 | timestamp | 0 |  |  | null | 计划实现周期.结束 |
| 13 | findustry | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业,枚举: elec :机电行业 soft :软件行业 |
| 14 | fexceptedrealiztime1 | 期望实现时间 | timestamp | 0 |  |  | null | 期望实现时间 |
| 15 | fname | 标题 | varchar | 50 |  | √ | ' ' | 标题 |
| 16 | fstart | 计划实现周期.开始 | timestamp | 0 |  |  | null | 计划实现周期.开始 |
| 17 | frmtpl | 需求模板 | int8 | 64 |  | √ | 0 | [RR原始需求模板 plm_rm_rr_common_tpl](../plmrm_files/plm_rm_rr_common_tpl.md) |
| 18 | fsourceinstructions | 来源说明 | varchar | 50 |  | √ | ' ' | 来源说明 |
| 19 | fbsa1 | BSA | varchar | 50 |  | √ | ' ' | BSA,枚举: Basic :Basic Satisfy :Satisfy Attractive :Attractive |
| 20 | fstatus_keep_days | 当前状态停留时长（天） | int8 | 64 |  | √ | 0 | 当前状态停留时长（天） |
| 21 | fproductdescharger | 产品设计负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | funiversalgrade1 | 通用等级 | varchar | 50 |  | √ | ' ' | 通用等级,枚举: must :必须 should :应有 could :可有 reprieve :暂缓 never :不必 |
| 23 | fdevwork | 开发工作量 | numeric | 23 | 10 | √ | 0 | 开发工作量 |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | ftimedimension | 时间维度 | varchar | 50 |  | √ | ' ' | 时间维度,枚举: A :通用需求 B :长期需求 C :中期需求 D :短期需求 E :定制需求 F :紧急需求 G :已上市产品需求 |
| 27 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 28 | flatestver | 是否最新版本 | bpchar | 1 |  | √ | '1' | 是否最新版本 |
| 29 | fworkload | 工作量（人天） | numeric | 23 | 1 | √ | 0 | 工作量（人天） |
| 30 | fstatus_dpd_date | 状态转换日期 | timestamp | 0 |  |  | null | 状态转换日期 |
| 31 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: high :高 higher :较高 middle :中 lower :较低 low :低 |
| 32 | fdevcharger | 开发负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fsource | 来源 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 34 | frmchangestatus | 变更状态 | varchar | 50 |  | √ | ' ' | 变更状态,枚举: nochange : changing :变更中 |
| 35 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 36 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 37 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 38 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 39 | fdesignwork | 设计工作量 | numeric | 23 | 10 | √ | 0 | 设计工作量 |
| 40 | frelatermchangebill | 关联变更单id | int8 | 64 |  | √ | 0 | 关联变更单id |
| 41 | fstayday | 当前状态停留时长（废弃） | int8 | 64 |  | √ | 0 | 当前状态停留时长（废弃） |
| 42 | fcurversionid | 当前版本ID | int8 | 64 |  | √ | 0 | 当前版本ID |
| 43 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 44 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 45 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 46 | fistempversion | 是否临时版本 | bpchar | 1 |  | √ | '0' | 是否临时版本 |
| 47 | fitemstatusid | 状态 | int8 | 64 |  | √ | 0 | [状态 plm_ipd_lc_status](../plmipdsm_files/plm_ipd_lc_status.md) |
| 48 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 49 | ftestwork | 测试工作量 | numeric | 23 | 10 | √ | 0 | 测试工作量 |
| 50 | ftestcharger | 测试负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 51 | ftextareafield | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 52 | fbasedatafield | 工作项图标 | int8 | 64 |  | √ | 0 | [工作项图标 plm_ipditempic](../plmipdsm_files/plm_ipditempic.md) |
| 53 | fcurversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 54 | frelateproject | 关联项目 | int8 | 64 |  | √ | 0 | [项目 plm_ipd_project](../plmpm_files/plm_ipd_project.md) |
| 55 | festimatetimedelivery | 预计交付时间 | timestamp | 0 |  |  | null | 预计交付时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_rm_us_soft_master |  | fmasterid |
| 2 | idx_t_plm_rm_us_soft_createorg |  | fcreateorgid |
| 3 | pk_plm_rm_us_soft |  | fid |
| 4 | idx_plm_rm_us_soft_m0 |  | fmasterid |

---

## US用户故事_维护-使用范围表 t_plm_rm_us_soft_u

- **表名称：** US用户故事_维护-使用范围表
- **表名：** t_plm_rm_us_soft_u

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
| 1 | pk_t_plm_rm_us_soft_u |  | fdataid,fuseorgid |
| 2 | idx_t_plm_rm_us_soft_u_uo |  | fuseorgid |

---

## US用户故事_维护-多语言表 t_plm_rm_us_soft_l

- **表名称：** US用户故事_维护-多语言表
- **表名：** t_plm_rm_us_soft_l

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
| 1 | idx_plm_rm_us_soft_l_0 |  | fid,flocaleid |
| 2 | pk_plm_rm_us_soft_l |  | fpkid |
