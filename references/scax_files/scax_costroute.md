# 成本工艺路线-scax_costroute

## 成本工艺路线-主表 t_scax_costroute

- **表名称：** 成本工艺路线-主表
- **表名：** t_scax_costroute

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fsourceid | 源单id | int8 | 64 |  | √ | 0 | 源单id |
| 4 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fdisableuser | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fdisabletime | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fsynctime | 同步时间 | timestamp | 0 |  |  | null | 同步时间 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 16 | fmaterial | 主产品物料 | int8 | 64 |  | √ | 0 | 物料 bd_material |
| 17 | ferpmaterial | 物料编码 | int8 | 64 |  | √ | 0 | 物料生产信息 bd_materialmftinfo |
| 18 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fname | 工艺路线名称 | varchar | 255 |  | √ | ' ' | 工艺路线名称 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 22 | fprocesstype | 类型 | bpchar | 1 |  | √ | ' ' | 类型,枚举: A :物料 B :物料组 C :通用工艺 |
| 23 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 24 | fenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 25 | fenableuser | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fismain | 默认工艺路线 | bpchar | 1 |  | √ | ' ' | 默认工艺路线 |
| 28 | fnumber | 工艺路线编码 | varchar | 255 |  | √ | ' ' | 工艺路线编码 |
| 29 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 30 | funit | 生产单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_costroute |  | fid |
| 2 | idx_scax_costtoute_number |  | fnumber |
| 3 | idx_t_scax_costroute_createorg |  | fcreateorgid |
| 4 | idx_t_scax_costroute_master |  | fmasterid |

---

## 子单据体-子表 t_scax_costrouteactive

- **表名称：** 子单据体-子表
- **表名：** t_scax_costrouteactive

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbaseunitnum | 基准单位分子 | numeric | 23 | 10 | √ | 0 | 基准单位分子 |
| 2 | factivity | 活动名称 | varchar | 30 |  | √ | ' ' | 活动名称,枚举: A :准备活动 B :加工活动 C :其他活动一 D :其他活动二 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdefaultqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 5 | factivityexpress | factivityexpress | varchar | 30 |  | √ | ' ' |  |
| 6 | factunit | 活动单位 | varchar | 30 |  | √ | ' ' | 活动单位,枚举: 1 :时 2 :分 3 :秒 |
| 7 | factivityreport | factivityreport | int8 | 64 |  | √ | 0 |  |
| 8 | factivitytype | 活动类型 | varchar | 30 |  | √ | ' ' | 活动类型,枚举: 0 :机器 1 :人工 |
| 9 | fbaseunitden | 基准单位分母 | numeric | 23 | 10 | √ | 0 | 基准单位分母 |
| 10 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 11 | fplanformulaid | fplanformulaid | int8 | 64 |  | √ | 0 |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 13 | fbaseactunit | 基准活动单位 | varchar | 30 |  | √ | ' ' | 基准活动单位,枚举: 1 :时 2 :分 3 :秒 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_costrouteactive |  | fdetailid |
| 2 | idx_scax_costrouteactive |  | fentryid |

---

## 成本工艺路线-多语言表 t_scax_costroute_l

- **表名称：** 成本工艺路线-多语言表
- **表名：** t_scax_costroute_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 工艺路线名称 | varchar | 255 |  | √ | ' ' | 工艺路线名称 |
| 3 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_costroute_l |  | fpkid |
| 2 | idx_scax_costroute_l |  | fid,flocaleid |

---

## 成本工艺路线-使用范围表 t_scax_costroute_u

- **表名称：** 成本工艺路线-使用范围表
- **表名：** t_scax_costroute_u

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
| 1 | idx_t_scax_costroute_u_uo |  | fuseorgid |
| 2 | pk_t_scax_costroute_u |  | fdataid,fuseorgid |

---

## 工序-多语言表 t_scax_costrouteentry_l

- **表名称：** 工序-多语言表
- **表名：** t_scax_costrouteentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprocessinstructions | 【工序信息】页签的工序说明 | varchar | 512 |  | √ | ' ' | 【工序信息】页签的工序说明 |
| 2 | flocaleid | flocaleid | varchar | 20 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_costrouteentry_l |  | fpkid |
| 2 | idx_scax_costrouteentry_l |  | fentryid,flocaleid |

---

## 工序-子表 t_scax_costrouteentry

- **表名称：** 工序-子表
- **表名：** t_scax_costrouteentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fprocesssequence | 【工序信息】页签的序列号 | int8 | 64 |  | √ | 0 | 【工序信息】页签的序列号 |
| 3 | frelationid | 工序分录唯一ID，用于与计划信息、活动后台表关联的ID | int8 | 64 |  | √ | 0 | 工序分录唯一ID，用于与计划信息、活动后台表关联的ID |
| 4 | fcostcenterid | 【工序信息】页签的成本中心 | int8 | 64 |  | √ | 0 | 成本中心 bos_costcenter |
| 5 | fislastprocess | 末序 | bpchar | 1 |  | √ | ' ' | 末序 |
| 6 | fprocessdepart | 【工序信息】页签的加工车间 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fprocesscontrolcode | 【工序信息】页签的工序控制码 | int8 | 64 |  | √ | 0 | 工序控制码 mpdm_processcontrolcode |
| 8 | fsequencetype | 【工序信息】序列类型 | varchar | 30 |  | √ | ' ' | 【工序信息】序列类型,枚举: A :并行序列 B :返工序列 C :主干序列 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fprocessinstructions | 【工序信息】页签的工序说明 | varchar | 512 |  | √ | ' ' | 【工序信息】页签的工序说明 |
| 11 | fprocessorg | 【工序信息】页签的加工组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 12 | fisfirstprocess | 首序 | bpchar | 1 |  | √ | ' ' | 首序 |
| 13 | fprocesscode | 工序编码 | int8 | 64 |  | √ | 0 | 标准工序 mpdm_normprocess |
| 14 | fismilestone | 里程碑 | bpchar | 1 |  | √ | ' ' | 里程碑 |
| 15 | fprocessnumber | 【工序信息】页签的工序号 | int8 | 64 |  | √ | 0 | 【工序信息】页签的工序号 |
| 16 | fbaseqty | 【工序信息】页签的基本批量 | numeric | 23 | 10 | √ | 0 | 【工序信息】页签的基本批量 |
| 17 | fismainprocess | 主工序 | bpchar | 1 |  | √ | ' ' | 主工序 |
| 18 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 19 | fprocesscenter | 【工序信息】页签的工作中心 | int8 | 64 |  | √ | 0 | 工作中心 sfc_workcenter |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_scax_costrouteentry |  | fentryid |
| 2 | idx_scax_costrouteentry |  | fid |
