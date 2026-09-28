# 维修计划工卡历史快照-mpdm_maintenanceplan_h

## 维修计划工卡历史快照-使用范围表 t_mpdm_maintenanceplan_h_u

- **表名称：** 维修计划工卡历史快照-使用范围表
- **表名：** t_mpdm_maintenanceplan_h_u

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
| 1 | pk_t_mpdm_maintenanceplan_h_u |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_maintenanceplan_h_u_uo |  | fuseorgid |

---

## 维修计划工卡历史快照-多语言表 t_mpdm_maintenanceplan_h_l

- **表名称：** 维修计划工卡历史快照-多语言表
- **表名：** t_mpdm_maintenanceplan_h_l

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
| 1 | pk_mpdm_maintenanceplan_h_l |  | fpkid |
| 2 | idx_mpdm_maintplan_h_l_0 |  | fid,flocaleid |

---

## 单据体-子表 t_mpdm_mpentry_h

- **表名称：** 单据体-子表
- **表名：** t_mpdm_mpentry_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 3 | fqty | 数量 | numeric | 23 | 10 | √ | 0 | 数量 |
| 4 | fprojectadapt | 适用性 | varchar | 50 |  | √ | ' ' | 适用性 |
| 5 | fcheckrel | 维修计划相关工卡涉及的大件拆装 | bpchar | 1 |  | √ | '0' | 维修计划相关工卡涉及的大件拆装 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fcardentryid | 维修计划工卡分录ID | int8 | 64 |  | √ | 0 | 维修计划工卡分录ID |
| 8 | fsinglehours | 单个拆装工时（小时） | numeric | 23 | 10 | √ | 0 | 单个拆装工时（小时） |
| 9 | fprojectdesc | 拆装项目描述 | varchar | 255 |  | √ | ' ' | 拆装项目描述 |
| 10 | fchecklayout | 航空公司客舱布局核实 | bpchar | 1 |  | √ | '0' | 航空公司客舱布局核实 |
| 11 | fprojectdesc_tag | 拆装项目描述_详情 | text | 0 |  |  | null | 拆装项目描述_详情 |
| 12 | farea | 区域 | varchar | 50 |  | √ | ' ' | 区域 |
| 13 | fsumhours | 总拆装工时（小时） | numeric | 23 | 10 | √ | 0 | 总拆装工时（小时） |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fholdrel | 客货舱相关拆装 | varchar | 50 |  | √ | ' ' | 客货舱相关拆装 |
| 16 | funit | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_mpentry_h_fk |  | fid |
| 2 | pk_mpdm_mpentry_h |  | fentryid |

---

## 维修计划工卡历史快照-主表 t_mpdm_maintenanceplan_h

- **表名称：** 维修计划工卡历史快照-主表
- **表名：** t_mpdm_maintenanceplan_h

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpreparehours | 维修计划准备工时（小时） | numeric | 23 | 10 | √ | 0 | 维修计划准备工时（小时） |
| 3 | fcorehours | 核心工时（小时） | numeric | 23 | 10 | √ | 0 | 核心工时（小时） |
| 4 | fpredicthours | 维修计划预估工时（小时） | numeric | 23 | 10 | √ | 0 | 维修计划预估工时（小时） |
| 5 | fammno | 维修手册编码 | varchar | 50 |  | √ | ' ' | 维修手册编码 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdismountremark | 大件拆装备注 | varchar | 255 |  | √ | ' ' | 大件拆装备注 |
| 8 | fphotoversion | 快照版本 | varchar | 50 |  | √ | ' ' | 快照版本 |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | ftaskhours | 维修计划任务工时（小时） | numeric | 23 | 10 | √ | 0 | 维修计划任务工时（小时） |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fdisabletime | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 13 | fhoursunit | 小时 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 14 | fneedcheck | 需要核查 | varchar | 50 |  | √ | ' ' | 需要核查 |
| 15 | fauditor | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 17 | fdisabler | 禁用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 19 | ftotalhours | 维修计划总工时（小时） | numeric | 23 | 10 | √ | 0 | 维修计划总工时（小时） |
| 20 | faddaccesspanel | 增加接近面板 | varchar | 50 |  | √ | ' ' | 增加接近面板 |
| 21 | fcardid | 维修计划工卡ID | int8 | 64 |  | √ | 0 | 维修计划工卡ID |
| 22 | fenabletime | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 23 | fdismounthours | 大件拆装工时（小时） | numeric | 23 | 10 | √ | 0 | 大件拆装工时（小时） |
| 24 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 26 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 27 | fmpdno | 型号L1-MPD | varchar | 50 |  | √ | ' ' | 型号L1-MPD |
| 28 | fadaptengine | 适用发动机 | varchar | 50 |  | √ | ' ' | 适用发动机 |
| 29 | fzone | 功能位置 | int8 | 64 |  | √ | 0 | 功能位置 mpdm_functionlocation |
| 30 | ftasktype | 工卡任务类型 | varchar | 50 |  | √ | ' ' | 工卡任务类型 |
| 31 | finitialinterval | 初始间隔 | varchar | 50 |  | √ | ' ' | 初始间隔 |
| 32 | faudittime | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 33 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 34 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 35 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 36 | fmoddate | 修订日期 | timestamp | 0 |  |  | null | 修订日期 |
| 37 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 38 | fcleanhours | 清洁工时（小时） | numeric | 23 | 10 | √ | 0 | 清洁工时（小时） |
| 39 | fworkdesc | 工卡描述 | varchar | 255 |  | √ | ' ' | 工卡描述 |
| 40 | fcoreremark | 核心工作备注 | varchar | 255 |  | √ | ' ' | 核心工作备注 |
| 41 | faccesspanel | 接近面板 | varchar | 50 |  | √ | ' ' | 接近面板 |
| 42 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 43 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 45 | fadapt | 适用性 | varchar | 50 |  | √ | ' ' | 适用性 |
| 46 | fpreparework | 准备工作 | varchar | 50 |  | √ | ' ' | 准备工作 |
| 47 | frepeatinterval | 重复间隔 | varchar | 50 |  | √ | ' ' | 重复间隔 |
| 48 | fenabler | 启用人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 49 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 50 | freferenceno | 参考号 | varchar | 50 |  | √ | ' ' | 参考号 |
| 51 | fchangepartrel | 涉及更换的部件 | varchar | 50 |  | √ | ' ' | 涉及更换的部件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_maintplanh_master |  | fmasterid |
| 2 | idx_mpdm_maintplanh_fcardid |  | fcardid |
| 3 | pk_mpdm_maintenanceplan_h |  | fid |
| 4 | idx_mpdm_maintplanh_corg |  | fcreateorgid |
| 5 | idx_t_mpdm_maintenanceplan_h_createorg |  | fcreateorgid |
| 6 | idx_t_mpdm_maintenanceplan_h_master |  | fmasterid |
