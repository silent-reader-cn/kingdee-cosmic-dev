# 维修计划工卡-mpdm_maintenanceplan

## 维修计划工卡-主表 t_mpdm_maintenanceplan

- **表名称：** 维修计划工卡-主表
- **表名：** t_mpdm_maintenanceplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpreparehours | 维修计划准备工时（小时） | numeric | 23 | 10 | √ | 0 | 维修计划准备工时（小时） |
| 3 | fcorehours | 核心工时（小时） | numeric | 23 | 10 | √ | 0 | 核心工时（小时） |
| 4 | fpredicthours | 维修计划预估工时（小时） | numeric | 23 | 10 | √ | 0 | 维修计划预估工时（小时） |
| 5 | fadaptengine | 适用发动机 | varchar | 50 |  | √ | ' ' | 适用发动机 |
| 6 | fammno | 维修手册编码 | varchar | 50 |  | √ | ' ' | 维修手册编码 |
| 7 | fzone | 功能位置 | int8 | 64 |  | √ | 0 | [功能位置 mpdm_functionlocation](../mpdm_files/mpdm_functionlocation.md) |
| 8 | ftasktype | 工卡任务类型 | varchar | 50 |  | √ | ' ' | 工卡任务类型 |
| 9 | finitialinterval | 初始间隔 | varchar | 50 |  | √ | ' ' | 初始间隔 |
| 10 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fdismountremark | 大件拆装备注 | varchar | 255 |  | √ | ' ' | 大件拆装备注 |
| 12 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | ftaskhours | 维修计划任务工时（小时） | numeric | 23 | 10 | √ | 0 | 维修计划任务工时（小时） |
| 14 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 15 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 16 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 17 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 18 | fhoursunit | 小时 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 20 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 21 | fneedcheck | 需要核查 | varchar | 50 |  | √ | ' ' | 需要核查 |
| 22 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 24 | fcleanhours | 清洁工时（小时） | numeric | 23 | 10 | √ | 0 | 清洁工时（小时） |
| 25 | fworkdesc | 工卡描述 | varchar | 255 |  | √ | ' ' | 工卡描述 |
| 26 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 27 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 28 | fcoreremark | 核心工作备注 | varchar | 255 |  | √ | ' ' | 核心工作备注 |
| 29 | faccesspanel | 接近面板 | varchar | 50 |  | √ | ' ' | 接近面板 |
| 30 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 31 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 32 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 33 | ftotalhours | 维修计划总工时（小时） | numeric | 23 | 10 | √ | 0 | 维修计划总工时（小时） |
| 34 | faddaccesspanel | 增加接近面板 | varchar | 50 |  | √ | ' ' | 增加接近面板 |
| 35 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 36 | fadapt | 适用性 | varchar | 50 |  | √ | ' ' | 适用性 |
| 37 | fpreparework | 准备工作 | varchar | 50 |  | √ | ' ' | 准备工作 |
| 38 | frepeatinterval | 重复间隔 | varchar | 50 |  | √ | ' ' | 重复间隔 |
| 39 | fenabler | 启用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 40 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 41 | fenabletime | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 42 | fdismounthours | 大件拆装工时（小时） | numeric | 23 | 10 | √ | 0 | 大件拆装工时（小时） |
| 43 | freferenceno | 参考号 | varchar | 50 |  | √ | ' ' | 参考号 |
| 44 | fchangepartrel | 涉及更换的部件 | varchar | 50 |  | √ | ' ' | 涉及更换的部件 |
| 45 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 46 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 47 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 48 | fmpdno | 型号L1-MPD | varchar | 50 |  | √ | ' ' | 型号L1-MPD |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_maintenanceplan |  | fid |
| 2 | idx_t_mpdm_maintenanceplan_createorg |  | fcreateorgid |
| 3 | idx_t_mpdm_maintenanceplan_master |  | fmasterid |
| 4 | idx_t_mpdm_maintenanceplan |  | fnumber |

---

## 单据体-子表 t_mpdm_mpentry

- **表名称：** 单据体-子表
- **表名：** t_mpdm_mpentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 4 | fprojectadapt | 适用性 | varchar | 50 |  | √ | ' ' | 适用性 |
| 5 | fcheckrel | 维修计划相关工卡涉及的大件拆装 | bpchar | 1 |  | √ | '0' | 维修计划相关工卡涉及的大件拆装 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fsinglehours | 单个拆装工时（小时） | numeric | 23 | 10 | √ | 0 | 单个拆装工时（小时） |
| 8 | fprojectdesc | 拆装项目描述 | varchar | 255 |  | √ | ' ' | 拆装项目描述 |
| 9 | fchecklayout | 航空公司客舱布局核实 | bpchar | 1 |  | √ | '0' | 航空公司客舱布局核实 |
| 10 | fprojectdesc_tag | 拆装项目描述_详情 | text | 0 |  |  | null | 拆装项目描述_详情 |
| 11 | farea | 区域 | varchar | 50 |  | √ | ' ' | 区域 |
| 12 | fsumhours | 总拆装工时（小时） | numeric | 23 | 10 | √ | 0 | 总拆装工时（小时） |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | fholdrel | 客货舱相关拆装 | varchar | 50 |  | √ | ' ' | 客货舱相关拆装 |
| 15 | funit | 计量单位 | int8 | 64 |  | √ | 0 | [计量单位 bd_measureunits](../base_files/bd_measureunits.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_mpentry_fk |  | fid |
| 2 | pk_mpdm_mpentry |  | fentryid |

---

## 维修计划工卡-多语言表 t_mpdm_maintenanceplan_l

- **表名称：** 维修计划工卡-多语言表
- **表名：** t_mpdm_maintenanceplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_mpdm_maintenanceplan_l |  | fpkid |
| 2 | idx_mpdm_maintenanceplan_l |  | fid,flocaleid |

---

## 维修计划工卡-使用范围位图表 t_mpdm_maintenanceplan_m

- **表名称：** 维修计划工卡-使用范围位图表
- **表名：** t_mpdm_maintenanceplan_m

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
| 1 | pk_t_mpdm_maintenanceplan_m |  | forgid |

---

## 维修计划工卡-使用范围表 t_mpdm_maintenanceplan_u

- **表名称：** 维修计划工卡-使用范围表
- **表名：** t_mpdm_maintenanceplan_u

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
| 1 | idx_t_mpdm_maintenanceplan_u_uo |  | fuseorgid |
| 2 | pk_t_mpdm_maintenanceplan_u |  | fdataid,fuseorgid |
