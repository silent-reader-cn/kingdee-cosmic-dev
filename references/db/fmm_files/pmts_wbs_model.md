# 计划模板-pmts_wbs_model

## 计划模板-使用范围位图表 t_pmts_plan_model_m

- **表名称：** 计划模板-使用范围位图表
- **表名：** t_pmts_plan_model_m

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
| 1 | pk_t_pmts_plan_model_m |  | forgid |

---

## 计划模板-多语言表 t_pmts_plan_model_l

- **表名称：** 计划模板-多语言表
- **表名：** t_pmts_plan_model_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 计划模板名称 | varchar | 50 |  | √ | ' ' | 计划模板名称 |
| 3 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 255 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmts_planl_fname |  | fname |
| 2 | pk_pmts_plan_model_l |  | fpkid |
| 3 | idx_pmts_planl_fid |  | fid,flocaleid |

---

## 计划模板-使用范围表 t_pmts_plan_model_u

- **表名称：** 计划模板-使用范围表
- **表名：** t_pmts_plan_model_u

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
| 1 | pk_t_pmts_plan_model_u |  | fdataid,fuseorgid |
| 2 | idx_t_pmts_plan_model_u_uo |  | fuseorgid |

---

## 计划模板-主表 t_pmts_plan_model

- **表名称：** 计划模板-主表
- **表名：** t_pmts_plan_model

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftemplateset | 模板设置 | varchar | 5 |  | √ | ' ' | 模板设置,枚举: 1 :仅WBS模板 2 :仅任务模板 3 :WBS和任务模板 |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '0' | 是否叶子 |
| 4 | festimateddays | 预计工期 | numeric | 23 | 10 | √ | 0 | 预计工期 |
| 5 | fpreparationtime | 编制时间 | timestamp | 0 |  |  | null | 编制时间 |
| 6 | fmodelnumber | 计划模板编码 | varchar | 50 |  | √ | ' ' | 计划模板编码 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcostobj | 成本对象 | bpchar | 1 |  | √ | '0' | 成本对象 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fresponsorgid | 责任单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fmodeltypeid | 计划模板类型 | int8 | 64 |  | √ | 0 | [计划模板类型 pmts_wbs_modeltype](../fmm_files/pmts_wbs_modeltype.md) |
| 17 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 18 | fcreateorgid | 项目组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fremark | 备注 | varchar | 58 |  | √ | ' ' | 备注 |
| 20 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fprojectstageid | 项目阶段 | int8 | 64 |  | √ | 0 | [项目阶段 pmbd_projectstage](../fmm_files/pmbd_projectstage.md) |
| 23 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [计划模板 pmts_wbs_model](../fmm_files/pmts_wbs_model.md) |
| 24 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 25 | fresponspersonid | 责任人 | int8 | 64 |  | √ | 0 | [企业人力资源池 pmbd_enterprise_hm_res_po](../fmm_files/pmbd_enterprise_hm_res_po.md) |
| 26 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 27 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 28 | fwbsname | WBS名称 | varchar | 50 |  | √ | ' ' | WBS名称 |
| 29 | fwtimeunit | 工期单位 | varchar | 5 |  | √ | ' ' | 工期单位,枚举: 1 :天 2 :周 |
| 30 | fctrlstrategy | 控制策略 | varchar | 5 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 31 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 32 | fwbstypeid | WBS类型 | int8 | 64 |  | √ | 0 | [项目WBS类型 pmbd_projectwbstype](../fmm_files/pmbd_projectwbstype.md) |
| 33 | fmodelstatus | 数据状态 | varchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 34 | fmodelname | 计划模板名称 | varchar | 50 |  | √ | ' ' | 计划模板名称 |
| 35 | fenable | 使用状态 | varchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 36 | fnumber | 计划模板编码 | varchar | 30 |  | √ | ' ' | 计划模板编码 |
| 37 | fuseorgid | 项目组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 38 | fpreparedby | 编制人 | int8 | 64 |  | √ | 0 | [企业人力资源池 pmbd_enterprise_hm_res_po](../fmm_files/pmbd_enterprise_hm_res_po.md) |
| 39 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 40 | fistemplate | 是否模板 | bpchar | 1 |  | √ | '0' | 是否模板 |
| 41 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmts_plan_fnumber |  | fnumber |
| 2 | idx_t_pmts_plan_model_master |  | fmasterid |
| 3 | pk_pmts_plan_model |  | fid |
| 4 | idx_pmts_plan_fcreatetime |  | fcreatetime |
| 5 | idx_t_pmts_plan_model_createorg |  | fcreateorgid |

---

## 任务模板-子表 t_pmts_tasktpentryentitys

- **表名称：** 任务模板-子表
- **表名：** t_pmts_tasktpentryentitys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaskrelation | 任务关系 | varchar | 5 |  | √ | ' ' | 任务关系,枚举: 1 :FS 2 :FF 3 :SS 4 :SF |
| 3 | fplanenddate | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 4 | ftresponsorg | 责任单位 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | ftaskrelationtwo | 任务关系 | varchar | 5 |  | √ | ' ' | 任务关系,枚举: 1 :FS 2 :FF 3 :SS 4 :SF |
| 6 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 pmbd_jobtype](../fmm_files/pmbd_jobtype.md) |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ftaskname | 任务名称 | varchar | 50 |  | √ | ' ' | 任务名称 |
| 9 | fplantime | 计划工期 | numeric | 23 | 10 | √ | 0 | 计划工期 |
| 10 | fworkloadunit | 工作量计量单位 | varchar | 5 |  | √ | ' ' | 工作量计量单位,枚举: 1 :H |
| 11 | fplanhours | 计划工时 | numeric | 23 | 10 | √ | 0 | 计划工时 |
| 12 | fplanstartdate | 计划开始时间 | timestamp | 0 |  |  | null | 计划开始时间 |
| 13 | ftimeunit | 工期单位 | varchar | 5 |  | √ | ' ' | 工期单位,枚举: 1 :天 2 :周 |
| 14 | fpercenttype | 完成百分比类型 | varchar | 5 |  | √ | ' ' | 完成百分比类型,枚举: 1 :实际百分比 2 :工期百分比 3 :数量百分比 |
| 15 | fposttask | 后置任务 | varchar | 50 |  | √ | ' ' | 后置任务 |
| 16 | fwbstname | WBS名称 | varchar | 50 |  | √ | ' ' | WBS名称 |
| 17 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 18 | ftresponsperson | 责任人 | int8 | 64 |  | √ | 0 | [企业人力资源池 pmbd_enterprise_hm_res_po](../fmm_files/pmbd_enterprise_hm_res_po.md) |
| 19 | fpretask | 前置任务 | varchar | 50 |  | √ | ' ' | 前置任务 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pmts_taskys_fid |  | fid |
| 2 | pk_pmts_tasktpentryentitys |  | fentryid |
| 3 | idx_pmts_taskys_fseq |  | fseq |
