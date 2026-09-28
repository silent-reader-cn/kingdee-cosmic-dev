# 标准任务清单-fmm_standardtask

## 工卡信息-子表 t_fmm_standardtaskentry

- **表名称：** 工卡信息-子表
- **表名：** t_fmm_standardtaskentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fcardno | fcardno | varchar | 50 |  | √ | ' ' |  |
| 4 | fprogroup | 工序组 | int8 | 64 |  | √ | 0 | [工序组(废弃) mpdm_progroup](../mpdm_files/mpdm_progroup.md) |
| 5 | fcardid | 检修工艺ID | int8 | 64 |  | √ | 0 | 检修工艺ID |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcardtitle | fcardtitle | varchar | 50 |  | √ | ' ' |  |
| 8 | fcardentryid | 检修工艺分录ID | int8 | 64 |  | √ | 0 | 检修工艺分录ID |
| 9 | fworkcard | 工卡 | varchar | 255 |  | √ | ' ' | 工卡 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fcardnumber | fcardnumber | int8 | 64 |  | √ | 0 |  |
| 12 | fcard | fcard | int8 | 64 |  | √ | 0 |  |
| 13 | fprofession | 行业 | int8 | 64 |  | √ | 0 | [树形基础资料模板 mpdm_professiona](../mpdm_files/mpdm_professiona.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_standardtaskentry |  | fentryid |
| 2 | idx_fmm_standardtaskentry_fsq |  | fid,fseq |

---

## 标准任务清单-主表 t_fmm_standardtask

- **表名称：** 标准任务清单-主表
- **表名：** t_fmm_standardtask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftasktype | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 pmbd_jobtype](../fmm_files/pmbd_jobtype.md) |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fbiztype | 业务类型 | varchar | 50 |  | √ | ' ' | 业务类型,枚举: A :标准任务 B :里程碑 C :WBS |
| 9 | fplanperiod | 计划工期 | numeric | 23 | 10 | √ | 0 | 计划工期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 15 | fisimport | 重要任务 | bpchar | 1 |  | √ | '0' | 重要任务 |
| 16 | fwbstype | WBS类型 | int8 | 64 |  | √ | 0 | [项目WBS类型 pmbd_projectwbstype](../fmm_files/pmbd_projectwbstype.md) |
| 17 | fcreateorgid | 项目组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fsourceproject | 来源项目 | int8 | 64 |  | √ | 0 | [项目 pmpd_project](../fmm_files/pmpd_project.md) |
| 19 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 20 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fplanarea | 计划区域 | int8 | 64 |  | √ | 0 | [计划区域 fmm_planningarea](../fmm_files/fmm_planningarea.md) |
| 25 | ftimeunit | 工期单位 | int8 | 64 |  | √ | 0 | [工期单位 pmpd_timeunit](../fmm_files/pmpd_timeunit.md) |
| 26 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fplantype | fplantype | int8 | 64 |  | √ | 0 |  |
| 28 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 29 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fmm_standardtask_fnm |  | fnumber |
| 2 | idx_t_fmm_standardtask_master |  | fmasterid |
| 3 | pk_fmm_standardtask |  | fid |
| 4 | idx_t_fmm_standardtask_createorg |  | fcreateorgid |

---

## 标准任务清单-多语言表 t_fmm_standardtask_l

- **表名称：** 标准任务清单-多语言表
- **表名：** t_fmm_standardtask_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_standardtask_l |  | fpkid |
| 2 | idx_fmm_standardtask_l |  | fid,flocaleid |

---

## 标准任务清单-使用范围位图表 t_fmm_standardtask_m

- **表名称：** 标准任务清单-使用范围位图表
- **表名：** t_fmm_standardtask_m

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
| 1 | pk_t_fmm_standardtask_m |  | forgid |

---

## 标准任务清单-使用范围表 t_fmm_standardtask_u

- **表名称：** 标准任务清单-使用范围表
- **表名：** t_fmm_standardtask_u

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
| 1 | pk_t_fmm_standardtask_u |  | fdataid,fuseorgid |
| 2 | idx_t_fmm_standardtask_u_uo |  | fuseorgid |

---

## 项目计划类型-多选基础资料表 t_fmm_standardtask_type

- **表名称：** 项目计划类型-多选基础资料表
- **表名：** t_fmm_standardtask_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [项目计划类型 fmm_plantype](../fmm_files/fmm_plantype.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_standardtask_type |  | fpkid |
| 2 | idx_fmm_standardtask_type_fid |  | fid |
