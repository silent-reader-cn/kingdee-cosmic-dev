# 计划模板-pmpd_milestonetpl

## 计划模板-多语言表 t_fmm_milestonetpl_l

- **表名称：** 计划模板-多语言表
- **表名：** t_fmm_milestonetpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模板名称 | varchar | 50 |  | √ | ' ' | 模板名称 |
| 3 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_milestonetpl_l |  | fpkid |
| 2 | idx_fmm_milestonetpl_l |  | fid,flocaleid |

---

## 计划模板-使用范围位图表 t_fmm_milestonetpl_m

- **表名称：** 计划模板-使用范围位图表
- **表名：** t_fmm_milestonetpl_m

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
| 1 | pk_t_fmm_milestonetpl_m |  | forgid |

---

## 计划模板-使用范围表 t_fmm_milestonetpl_u

- **表名称：** 计划模板-使用范围表
- **表名：** t_fmm_milestonetpl_u

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
| 1 | pk_t_fmm_milestonetpl_u |  | fdataid,fuseorgid |
| 2 | idx_t_fmm_milestonetpl_u_uo |  | fuseorgid |

---

## 模板明细-子表 t_fmm_mstentry

- **表名称：** 模板明细-子表
- **表名：** t_fmm_mstentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fplanbegin | 计划开始 | int4 | 32 |  | √ | 0 | 计划开始 |
| 3 | fposttaskid | 后置任务ID | int8 | 64 |  | √ | 0 | 后置任务ID |
| 4 | ftasktype | 任务类型 | int8 | 64 |  | √ | 0 | 任务类型 pmbd_jobtype |
| 5 | fpostrelation | 后置任务关系 | varchar | 5 |  | √ | ' ' | 后置任务关系,枚举: 1 :FS 2 :FF 3 :SS 4 :SF |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fplanfinish | 计划完成 | int4 | 32 |  | √ | 0 | 计划完成 |
| 8 | fbiztype | 业务类型 | varchar | 5 |  | √ | ' ' | 业务类型,枚举: A :里程碑 B :WBS C :任务 |
| 9 | fplanperiod | 计划工期 | numeric | 23 | 10 | √ | 0 | 计划工期 |
| 10 | fpercenttype | 完成百分比类型 | varchar | 5 |  | √ | ' ' | 完成百分比类型,枚举: A :实际百分比 B :工期百分比 C :数量百分比 |
| 11 | fpostdelay | 后置延时设置 | numeric | 23 | 10 |  | null | 后置延时设置 |
| 12 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 13 | fmilestonename | 里程碑名称 | varchar | 255 |  | √ | ' ' | 里程碑名称 |
| 14 | fwbstype | WBS类型 | int8 | 64 |  | √ | 0 | 项目WBS类型 pmbd_projectwbstype |
| 15 | fpercent | 进度比（%） | numeric | 23 | 10 | √ | 0 | 进度比（%） |
| 16 | ffrontrelation | 前置任务关系 | varchar | 5 |  | √ | ' ' | 前置任务关系,枚举: 1 :FS 2 :FF 3 :SS 4 :SF |
| 17 | ffronttask | 前置任务 | varchar | 50 |  | √ | ' ' | 前置任务 |
| 18 | ftaskname | 任务名称 | varchar | 255 |  | √ | ' ' | 任务名称 |
| 19 | fwbsname | WBS名称 | varchar | 255 |  | √ | ' ' | WBS名称 |
| 20 | ffrontdelay | 前置延时设置 | numeric | 23 | 10 |  | null | 前置延时设置 |
| 21 | fstandardmile | 标准里程碑 | int8 | 64 |  | √ | 0 | 标准任务清单 fmm_standardtask |
| 22 | fparent | 上级 | varchar | 50 |  | √ | ' ' | 上级 |
| 23 | ftimeunit | 工期单位 | int8 | 64 |  | √ | 0 | 工期单位 pmpd_timeunit |
| 24 | fstandardtask | 标准任务 | int8 | 64 |  | √ | 0 | 标准任务清单 fmm_standardtask |
| 25 | ffronttaskid | 前置任务ID | int8 | 64 |  | √ | 0 | 前置任务ID |
| 26 | fposttask | 后置任务 | varchar | 50 |  | √ | ' ' | 后置任务 |
| 27 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_mstentry |  | fentryid |
| 2 | idx_fmm_mstentry_fid |  | fid |

---

## 计划模板-主表 t_fmm_milestonetpl

- **表名称：** 计划模板-主表
- **表名：** t_fmm_milestonetpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 计划模板类型 | int8 | 64 |  | √ | 0 | 计划模板类型 pmts_wbs_modeltype |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fchecktype | 检修级别 | int8 | 64 |  | √ | 0 | 检修级别 mpdm_checktype |
| 8 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | ffixweek | 维修周期 | numeric | 23 | 10 | √ | 0 | 维修周期 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fname | 模板名称 | varchar | 50 |  | √ | ' ' | 模板名称 |
| 19 | fcustomer | 客户 | int8 | 64 |  | √ | 0 | 客户 bd_customer |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fstructure | 模板结构 | varchar | 50 |  | √ | ' ' | 模板结构,枚举: A :里程碑模板 B :WBS模板 C :任务模板 D :全量模板 |
| 22 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 23 | ftype | 行业分类 | varchar | 50 |  | √ | ' ' | 行业分类,枚举: A :标准行业 B :检修行业 |
| 24 | ftimeunit | ftimeunit | int8 | 64 |  | √ | 0 |  |
| 25 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 模板编码 | varchar | 30 |  | √ | ' ' | 模板编码 |
| 27 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 28 | fmrtype | 检修设备类型 | int8 | 64 |  | √ | 0 | 检修设备类型 mpdm_mrtype |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fmm_milestonetpl_createorg |  | fcreateorgid |
| 2 | idx_fmm_milestonetpl_fnumber |  | fnumber |
| 3 | pk_fmm_milestonetpl |  | fid |
| 4 | idx_t_fmm_milestonetpl_master |  | fmasterid |
