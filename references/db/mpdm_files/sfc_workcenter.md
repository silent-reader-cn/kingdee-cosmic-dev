# 工作中心-sfc_workcenter

## 单据体-子表 t_sfc_wcactivity

- **表名称：** 单据体-子表
- **表名：** t_sfc_wcactivity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | factunitid | 活动单位 | int8 | 64 |  |  | null | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 3 | factivity | 活动名称 | bpchar | 1 |  | √ | ' ' | 活动名称,枚举: A :准备活动 B :加工活动 C :其他活动一 D :其他活动二 |
| 4 | fresourceid | 资源 | int8 | 64 |  | √ | 0 | [资源 mpdm_resourceinfo](../mpdm_files/mpdm_resourceinfo.md) |
| 5 | factivityreport | 汇报活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 6 | fpformulaid | 计划活动量公式 | int8 | 64 |  | √ | 0 | [活动公式 mpdm_activityformula](../mpdm_files/mpdm_activityformula.md) |
| 7 | factivitytype | 活动类型 | bpchar | 1 |  | √ | ' ' | 活动类型,枚举: 0 :机器 1 :人工 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fdefaultqty | 基本数量 | numeric | 23 | 10 |  | null | 基本数量 |
| 10 | factivityexpress | 活动汇报量公式 | bpchar | 1 |  | √ | ' ' | 活动汇报量公式,枚举: A :准备活动 B :加工活动*CEIL(工序汇报.合格数量/工序计划.基本批量) |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_wcactivity |  | fentryid |

---

## 工作中心-主表 t_sfc_workcenter

- **表名称：** 工作中心-主表
- **表名：** t_sfc_workcenter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjobtype | 作业类型 | bpchar | 1 |  | √ | ' ' | 作业类型,枚举: B :个人作业 A :团队作业 |
| 3 | fgroupid | 分组 | int8 | 64 |  |  | null | [工作中心分组 sfc_workcentergroup](../mpdm_files/sfc_workcentergroup.md) |
| 4 | forgid | 组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdepartid | 所属车间 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fworkshopid | 车间 | int8 | 64 |  |  | null | [车间设置 mpdm_workshopsetup](../mpdm_files/mpdm_workshopsetup.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 14 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fsourcedataid | 原资料id | int8 | 64 |  |  | null | 原资料id |
| 16 | fbitindex | 位图 | int8 | 64 |  |  | null | 位图 |
| 17 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 19 | fname | 工作中心名称 | varchar | 255 |  |  | null | 工作中心名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 23 | fenabler | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 24 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fprocesscodeid | 工序控制码 | int8 | 64 |  |  | null | [工序控制码 mpdm_processcontrolcode](../mpdm_files/mpdm_processcontrolcode.md) |
| 28 | fnumber | 工作中心编码 | varchar | 80 |  | √ | ' ' | 工作中心编码 |
| 29 | fuseorgid | 业务组织 | int8 | 64 |  |  | null | [业务单元 bos_org](../base_files/bos_org.md) |
| 30 | fsourcebitindex | 原资料位图 | int8 | 64 |  |  | null | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_sfc_workcenter |  | fid |
| 2 | idx_t_sfc_workcenter_master |  | fmasterid |
| 3 | idx_t_sfc_workcenter_createorg |  | fcreateorgid |

---

## 工作中心-使用范围表 t_sfc_workcenter_u

- **表名称：** 工作中心-使用范围表
- **表名：** t_sfc_workcenter_u

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
| 1 | pk_t_sfc_workcenter_u |  | fdataid,fuseorgid |
| 2 | idx_t_sfc_workcenter_u_uo |  | fuseorgid |

---

## 工作中心-多语言表 t_sfc_workcenter_l

- **表名称：** 工作中心-多语言表
- **表名：** t_sfc_workcenter_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工作中心名称 | varchar | 255 |  |  | null | 工作中心名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  |  | null | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sfc_workcenter_l |  | fpkid |
