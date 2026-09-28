# 移动质检任务单-qcmp_taskinfo

## 关联子实体-子表 t_qcmp_task_lk

- **表名称：** 关联子实体-子表
- **表名：** t_qcmp_task_lk

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
| 1 | pk_qcmp_task_lk |  | fpkid |
| 2 | idx_qcmp_task_lk_fk |  | fid |

---

## 移动质检任务单-使用范围表 t_qcmp_task_u

- **表名称：** 移动质检任务单-使用范围表
- **表名：** t_qcmp_task_u

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
| 1 | pk_t_qcmp_task_u |  | fdataid,fuseorgid |
| 2 | idx_t_qcmp_task_u_uo |  | fuseorgid |

---

## 移动质检任务单-多语言表 t_qcmp_task_l

- **表名称：** 移动质检任务单-多语言表
- **表名：** t_qcmp_task_l

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
| 1 | pk_t_qcmp_task_l |  | fpkid |
| 2 | idx_qcmp_taskl_idlocale |  | fid,flocaleid |

---

## 移动质检任务单-主表 t_qcmp_task

- **表名称：** 移动质检任务单-主表
- **表名：** t_qcmp_task

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmaterialcfgid | 物料编码 | int8 | 64 |  | √ | 0 | 物料质检信息 bd_inspect_cfg |
| 3 | fsrcentryid | 来源分录id | int8 | 64 |  | √ | 0 | 来源分录id |
| 4 | ftasktype | 任务类型 | varchar | 1 |  | √ | '1' | 任务类型,枚举: 1 :已认领 2 :已委托 3 :已指派 4 :已接受 |
| 5 | fmaterialid | 物料主数据 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | ftaskexecutor | 执行人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmanager | 质检主管 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fbiztype | 业务类型 | int8 | 64 |  | √ | 0 | 业务类型 bd_biztype |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fmaterialqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 18 | ftaskstatus | 任务状态 | varchar | 1 |  | √ | '0' | 任务状态,枚举: 0 :检验中 1 :已提交 2 :未开始 3 :已关闭 4 :已修改 |
| 19 | fxkallocationtype | 分配类型 | bpchar | 1 |  | √ | ' ' | 分配类型,枚举: 1 :个性化 2 :共享型 |
| 20 | facceptstatus | 委托人接受状态 | varchar | 1 |  | √ | '0' | 委托人接受状态,枚举: 0 :未接受 1 :已接受 |
| 21 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 22 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 23 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 24 | fsrcbillid | 来源单据id | int8 | 64 |  | √ | 0 | 来源单据id |
| 25 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 26 | funitid | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 27 | fexpectdate | 期望完成日期 | timestamp | 0 |  |  | null | 期望完成日期 |
| 28 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 29 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 30 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '5' | 控制策略,枚举: 5 :全局共享 |
| 31 | fsrcnumber | 来源单编码 | varchar | 30 |  | √ | ' ' | 来源单编码 |
| 32 | fenable | 使用状态 | varchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 33 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 34 | fendtime | 完成时间 | timestamp | 0 |  |  | null | 完成时间 |
| 35 | fisurgent | 任务加急 | bpchar | 1 |  | √ | '0' | 任务加急 |
| 36 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 37 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 38 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 39 | ftaskclaimant | 认领人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 40 | ftaskclient | 委托人 | int8 | 64 |  | √ | 0 | 人员 bos_user |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_qcmp_task_master |  | fmasterid |
| 2 | uidx_qcmp_task_fsrcentryid |  | fsrcentryid |
| 3 | idx_t_qcmp_task_createorg |  | fcreateorgid |
| 4 | uidx_qcmp_task_fnumber |  | fnumber |
| 5 | idx_qcmp_task_ftaskexecutor |  | ftaskexecutor |
| 6 | idx_qcmp_task_fcreatetime |  | fcreatetime |
| 7 | pk_qcmp_task |  | fid |
| 8 | idx_qcmp_task_fbiztype |  | fbiztype |
