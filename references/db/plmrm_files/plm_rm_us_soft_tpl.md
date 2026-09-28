# US用户故事模板（软件产品）-plm_rm_us_soft_tpl

## US用户故事模板（软件产品）-主表 t_plm_rm_us_soft_temp

- **表名称：** US用户故事模板（软件产品）-主表
- **表名：** t_plm_rm_us_soft_temp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分类 | int8 | 64 |  | √ | 0 | [需求分类 plm_rm_group](../plmrm_files/plm_rm_group.md) |
| 3 | fstatus_dpd_date | 状态转换日期 | timestamp | 0 |  |  | null | 状态转换日期 |
| 4 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fpriority | 优先级 | varchar | 50 |  | √ | ' ' | 优先级,枚举: high :高 higher :较高 middle :中 lower :较低 low :低 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fdevcharger | 开发负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fsource | 来源 | int8 | 64 |  | √ | 0 | [辅助资料 bos_assistantdata_detail](../base_files/bos_assistantdata_detail.md) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fdesignwork | 设计工作量 | numeric | 23 | 10 | √ | 0 | 设计工作量 |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fend | 计划实现周期.结束 | timestamp | 0 |  |  | null | 计划实现周期.结束 |
| 18 | fstayday | 当前状态停留时长（废弃） | int8 | 64 |  | √ | 0 | 当前状态停留时长（废弃） |
| 19 | findustry | 所属行业 | varchar | 50 |  | √ | ' ' | 所属行业,枚举: elec :机电行业 soft :软件行业 |
| 20 | fexceptedrealiztime1 | 期望实现时间 | timestamp | 0 |  |  | null | 期望实现时间 |
| 21 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fname | [US]标题 | varchar | 50 |  | √ | ' ' | [US]标题 |
| 24 | fstart | 计划实现周期.开始 | timestamp | 0 |  |  | null | 计划实现周期.开始 |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | fsourceinstructions | 来源说明 | varchar | 50 |  | √ | ' ' | 来源说明 |
| 27 | fbsa1 | BSA | varchar | 50 |  | √ | ' ' | BSA,枚举: Basic :Basic Satisfy :Satisfy Attractive :Attractive |
| 28 | fstatus_keep_days | 当前状态停留时长（天） | int8 | 64 |  | √ | 0 | 当前状态停留时长（天） |
| 29 | fitemstatusid | 状态 | int8 | 64 |  | √ | 0 | [状态 plm_ipd_lc_status](../plmipdsm_files/plm_ipd_lc_status.md) |
| 30 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | ftestwork | 测试工作量 | numeric | 23 | 10 | √ | 0 | 测试工作量 |
| 32 | ftestcharger | 测试负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fproductdescharger | 产品设计负责人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 34 | funiversalgrade1 | 通用等级 | varchar | 50 |  | √ | ' ' | 通用等级,枚举: must :必须 should :应有 could :可有 reprieve :暂缓 never :不必 |
| 35 | ftextareafield | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 36 | fdevwork | 开发工作量 | numeric | 23 | 10 | √ | 0 | 开发工作量 |
| 37 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 38 | fnumber | 模板编码 | varchar | 30 |  | √ | ' ' | 模板编码 |
| 39 | ftimedimension | 时间维度 | varchar | 50 |  | √ | ' ' | 时间维度,枚举: A :通用需求 B :长期需求 C :中期需求 D :短期需求 E :定制需求 F :紧急需求 G :已上市产品需求 |
| 40 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 41 | festimatetimedelivery | 预计交付时间 | timestamp | 0 |  |  | null | 预计交付时间 |
| 42 | fworkload | 工作量（人天） | numeric | 23 | 1 | √ | 0 | 工作量（人天） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_rm_us_soft_temp |  | fid |
| 2 | idx_t_plm_rm_us_soft_temp_master |  | fmasterid |
| 3 | idx_t_plm_rm_us_soft_temp_createorg |  | fcreateorgid |
| 4 | idx_plm_rm_us_soft_temp_m0 |  | fmasterid |

---

## 负责人-多选基础资料表 t_plm_rm_tmp_chargeperson

- **表名称：** 负责人-多选基础资料表
- **表名：** t_plm_rm_tmp_chargeperson

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
| 1 | pk_plm_rm_tmp_chargeperson |  | fpkid |
| 2 | idx_plm_rm_tmp_chargeperson_fk |  | fid |

---

## US用户故事模板（软件产品）-多语言表 t_plm_rm_us_soft_temp_l

- **表名称：** US用户故事模板（软件产品）-多语言表
- **表名：** t_plm_rm_us_soft_temp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | [US]标题 | varchar | 80 |  | √ | ' ' | [US]标题 |
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
| 1 | idx_plm_rm_us_soft_temp_l_0 |  | fid,flocaleid |
| 2 | pk_plm_rm_us_soft_temp_l |  | fpkid |

---

## US用户故事模板（软件产品）-使用范围表 t_plm_rm_us_soft_temp_u

- **表名称：** US用户故事模板（软件产品）-使用范围表
- **表名：** t_plm_rm_us_soft_temp_u

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
| 1 | idx_t_plm_rm_us_soft_temp_u_uo |  | fuseorgid |
| 2 | pk_t_plm_rm_us_soft_temp_u |  | fdataid,fuseorgid |
