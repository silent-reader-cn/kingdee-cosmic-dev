# 任务状态规则基础资料-mpm_taskstatusrule

## 任务状态规则基础资料-多语言表 t_mpm_tskstatrule_l

- **表名称：** 任务状态规则基础资料-多语言表
- **表名：** t_mpm_tskstatrule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 3 | fname | 操作步骤 | varchar | 255 |  | √ | ' ' | 操作步骤 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpm_tskstatrule_l |  | fpkid |
| 2 | idx_mpm_tskstatrule_fidflid |  | fid,flocaleid |

---

## 任务状态规则基础资料-使用范围表 t_mpm_tskstatrule_u

- **表名称：** 任务状态规则基础资料-使用范围表
- **表名：** t_mpm_tskstatrule_u

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
| 1 | pk_t_mpm_tskstatrule_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpm_tskstatrule_u_uo |  | fuseorgid |

---

## 分单条件分录-子表 t_mpm_tskstatruleentry

- **表名称：** 分单条件分录-子表
- **表名：** t_mpm_tskstatruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldtype | 字段类型 | bpchar | 1 |  | √ | ' ' | 字段类型,枚举: A :基础资料 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fsplitbillfield | 分单字段 | varchar | 30 |  | √ | ' ' | 分单字段,枚举: createorg :任务创建组织 taskcntrcode :任务业务类型 org :任务负责部门 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpm_tskstatruleentry_fid |  | fid |
| 2 | pk_mpm_tskstatruleentry |  | fentryid |

---

## 任务状态规则基础资料-主表 t_mpm_tskstatrule

- **表名称：** 任务状态规则基础资料-主表
- **表名：** t_mpm_tskstatrule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 业务对象分组 | varchar | 255 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | fisnotification | 状态变更通知 | bpchar | 1 |  | √ | '0' | 状态变更通知 |
| 4 | ftargetstatusid | 目标状态 | int8 | 64 |  | √ | 0 | [任务状态 mpm_taskstatus](../mpm_files/mpm_taskstatus.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbotpruleid | 指定转换规则 | varchar | 36 |  | √ | ' ' | [转换规则 botp_crlist](../botp_files/botp_crlist.md) |
| 10 | fbeginstatusid | 开始状态 | int8 | 64 |  | √ | 0 | [任务状态 mpm_taskstatus](../mpm_files/mpm_taskstatus.md) |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 16 | fisinitialstatus | 开始状态为初始状态 | bpchar | 1 |  | √ | '0' | 开始状态为初始状态 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fremark | 备注 | varchar | 512 |  | √ | ' ' | 备注 |
| 19 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 23 | fprocesstype | 流程使用方式 | bpchar | 1 |  | √ | ' ' | 流程使用方式,枚举: A :按流程启动条件自动匹配 B :指定流程 |
| 24 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fprocessdefineid | 指定流程 | int8 | 64 |  | √ | 0 | [流程管理 wf_processdefinition](../wf_files/wf_processdefinition.md) |
| 26 | fprojectkindid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 27 | fbotptype | 转换规则使用方式 | bpchar | 1 |  | √ | ' ' | 转换规则使用方式,枚举: A :自动匹配规则 B :指定规则 |
| 28 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fuseorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 31 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 32 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | fuseprocess | 启用工作流 | bpchar | 1 |  | √ | ' ' | 启用工作流 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpm_tskstatrule_createorg |  | fcreateorgid |
| 2 | idx_t_mpm_tskstatrule_master |  | fmasterid |
| 3 | pk_mpm_tskstatrule |  | fid |
| 4 | idx_mpm_tskstatrule_number |  | fnumber |
