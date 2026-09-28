# 参数设置-plm_pm_parasettings

## 参数设置-主表 t_plm_pm_parasettings

- **表名称：** 参数设置-主表
- **表名：** t_plm_pm_parasettings

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fuseorg | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fsuppleweek | 工作汇报中可以补录周数 | int8 | 64 |  | √ | 0 | 工作汇报中可以补录周数 |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fprojectld | 所属实例 | int8 | 64 |  | √ | 0 | 项目 plm_ipd_project |
| 6 | fprogress | 进度 | bpchar | 1 |  | √ | '0' | 进度 |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | fcontrolmode | 项目管控模式 | varchar | 50 |  | √ | ' ' | 项目管控模式,枚举: 101 :自上而下 102 :自下而上 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fquality | 质量 | bpchar | 1 |  | √ | '0' | 质量 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | ftypesource | 所属类型 | varchar | 50 |  | √ | ' ' | 所属类型,枚举: plm_ipd_project :项目 plm_pm_projectbaseline :项目基线 plm_pm_projectcopy :项目副本 plm_pm_projecttpl :项目模版 |
| 15 | fdayload | 日负荷基准 | int8 | 64 |  | √ | 0 | 日负荷基准 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int8 | 64 |  | √ | 0 | 位图 |
| 18 | fcheckbox4 | 前置任务完成时的输出、默认同步到后置任务的输入 | bpchar | 1 |  | √ | '0' | 前置任务完成时的输出、默认同步到后置任务的输入 |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fcheckbox3 | 任务组启动，自动启动第一个下层任务组或任务 | bpchar | 1 |  | √ | '0' | 任务组启动，自动启动第一个下层任务组或任务 |
| 21 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 23 | fcheckbox2 | 项目启动，自动启动第一个任务组或任务 | bpchar | 1 |  | √ | '0' | 项目启动，自动启动第一个任务组或任务 |
| 24 | fcheckbox1 | 项目启动后修改项目里程碑计划，团队，一级计划需要走变更 | bpchar | 1 |  | √ | '0' | 项目启动后修改项目里程碑计划，团队，一级计划需要走变更 |
| 25 | fcheckbox8 | 前置任务完成，驱动后置任务启动 | bpchar | 1 |  | √ | '0' | 前置任务完成，驱动后置任务启动 |
| 26 | fsourceobjid | 原业务对象 | int8 | 64 |  | √ | 0 | [参数设置 plm_pm_parasettings](../plmpm_files/plm_pm_parasettings.md) |
| 27 | fcheckbox7 | 项目及任务完成时记录交付物当前版本 | bpchar | 1 |  | √ | '0' | 项目及任务完成时记录交付物当前版本 |
| 28 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 29 | fcheckbox6 | 任务组由下层任务驱动完成 | bpchar | 1 |  | √ | '0' | 任务组由下层任务驱动完成 |
| 30 | feffncy | 效率 | bpchar | 1 |  | √ | '0' | 效率 |
| 31 | fcheckbox5 | 任务完成需要汇报确认 | bpchar | 1 |  | √ | '0' | 任务完成需要汇报确认 |
| 32 | fworkconsum | 工时消耗 | bpchar | 1 |  | √ | '0' | 工时消耗 |
| 33 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 34 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 35 | fapprovalworking | 启动工时审批 | bpchar | 1 |  | √ | '0' | 启动工时审批 |
| 36 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 37 | fcheckbox9 | 项目/任务启动自动根据文档模板创建实例 | bpchar | 1 |  | √ | '0' | 项目/任务启动自动根据文档模板创建实例 |
| 38 | fsourcebitindex | 原资料位图 | int8 | 64 |  | √ | 0 | 原资料位图 |
| 39 | fscope | 范围 | bpchar | 1 |  | √ | '0' | 范围 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_parasettings_m0 |  | fmasterid |
| 2 | pk_plm_pm_parasettings |  | fid |
| 3 | idx_t_plm_pm_parasettings_master |  | fmasterid |
| 4 | idx_t_plm_pm_parasettings_createorg |  | fcreateorgid |

---

## 单据体-子表 t_plm_pm_consum_entry

- **表名称：** 单据体-子表
- **表名：** t_plm_pm_consum_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcondition5 | 条件 | varchar | 50 |  | √ | ' ' | 条件 |
| 3 | fsign5 | 运算符 | varchar | 50 |  | √ | ' ' | 运算符,枚举: ge :>= g :> |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | ficonsty5 | 图标样式 | varchar | 50 |  | √ | ' ' | 图标样式,枚举: R :红色图标 Y :黄色图标 G :绿色图标 |
| 6 | flight5 |  | varchar | 50 |  | √ | ' ' | ,枚举: R :红色图标 Y :黄色图标 G :绿色图标 |
| 7 | fvalue5 | 数值 | numeric | 23 | 2 |  | null | 数值 |
| 8 | ftype5 | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: percent :百分比 numeral :数字 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fresultview5 | 结果预览 | varchar | 50 |  | √ | ' ' | 结果预览 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_consum_entry |  | fentryid |
| 2 | idx_plm_pm_consum_entry_fk |  | fid |

---

## 参数设置-多语言表 t_plm_pm_parasettings_l

- **表名称：** 参数设置-多语言表
- **表名：** t_plm_pm_parasettings_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_parasettings_l |  | fpkid |
| 2 | idx_plm_pm_parasettings_l_0 |  | fid,flocaleid |

---

## 参数设置-使用范围表 t_plm_pm_parasettings_u

- **表名称：** 参数设置-使用范围表
- **表名：** t_plm_pm_parasettings_u

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
| 1 | idx_t_plm_pm_parasettings_u_uo |  | fuseorgid |
| 2 | pk_t_plm_pm_parasettings_u |  | fdataid,fuseorgid |

---

## 单据体-子表 t_plm_pm_problem_entry

- **表名称：** 单据体-子表
- **表名：** t_plm_pm_problem_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcondition6 | 条件 | varchar | 50 |  | √ | ' ' | 条件 |
| 3 | fsign6 | 运算符 | varchar | 50 |  | √ | ' ' | 运算符,枚举: ge :>= g :> |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fvalue6 | 数值 | numeric | 23 | 2 |  | null | 数值 |
| 6 | ficonsty6 | 图标样式 | varchar | 50 |  | √ | ' ' | 图标样式,枚举: R :红色图标 Y :黄色图标 G :绿色图标 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftype6 | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: percent :百分比 numeral :数字 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_problem_entry_fk |  | fid |
| 2 | pk_plm_pm_problem_entry |  | fentryid |

---

## 单据体-子表 t_plm_pm_deviat_entry

- **表名称：** 单据体-子表
- **表名：** t_plm_pm_deviat_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue1 | 数值 | numeric | 23 | 2 |  | null | 数值 |
| 3 | ftype1 | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: percent :百分比 numeral :数字 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsign1 | 运算符 | varchar | 50 |  | √ | ' ' | 运算符,枚举: le :<= l :< |
| 6 | fresultview1 | 结果预览 | varchar | 50 |  | √ | ' ' | 结果预览 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ficonsty1 | 图标样式 | varchar | 50 |  | √ | ' ' | 图标样式,枚举: R :红色图标 Y :黄色图标 G :绿色图标 |
| 9 | flight1 |  | varchar | 50 |  | √ | ' ' | ,枚举: R :红色图标 Y :黄色图标 G :绿色图标 |
| 10 | fcondition1 | 条件 | varchar | 50 |  | √ | ' ' | 条件 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plm_pm_deviat_entry_fk |  | fid |
| 2 | pk_plm_pm_deviat_entry |  | fentryid |

---

## 单据体-子表 t_plm_pm_prodeviat_entry

- **表名称：** 单据体-子表
- **表名：** t_plm_pm_prodeviat_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsign3 | 运算符 | varchar | 50 |  | √ | ' ' | 运算符,枚举: le :<= l :< |
| 3 | fresultview3 | 结果预览 | varchar | 50 |  | √ | ' ' | 结果预览 |
| 4 | fvalue3 | 数值 | numeric | 23 | 2 |  | null | 数值 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | ftype3 | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: percent :百分比 numeral :数字 |
| 7 | ficonsty3 | 图标样式 | varchar | 50 |  | √ | ' ' | 图标样式,枚举: R :红色图标 Y :黄色图标 G :绿色图标 |
| 8 | flight3 |  | varchar | 50 |  | √ | ' ' | ,枚举: R :红色图标 Y :黄色图标 G :绿色图标 |
| 9 | fcondition3 | 条件 | varchar | 50 |  | √ | ' ' | 条件 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_prodeviat_entry |  | fentryid |
| 2 | idx_plm_pm_prodeviat_entry_fk |  | fid |

---

## 单据体-子表 t_plm_pm_scope_entry

- **表名称：** 单据体-子表
- **表名：** t_plm_pm_scope_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue2 | 数值 | numeric | 23 | 2 |  | null | 数值 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftype2 | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: percent :百分比 numeral :数字 |
| 5 | fsign2 | 运算符 | varchar | 50 |  | √ | ' ' | 运算符,枚举: ge :>= g :> |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fcondition2 | 条件 | varchar | 50 |  | √ | ' ' | 条件 |
| 8 | ficonsty2 | 图标样式 | varchar | 50 |  | √ | ' ' | 图标样式,枚举: R :红色图标 Y :黄色图标 G :绿色图标 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_scope_entry |  | fentryid |

---

## 单据体-子表 t_plm_pm_delay_entry

- **表名称：** 单据体-子表
- **表名：** t_plm_pm_delay_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsign4 | 运算符 | varchar | 50 |  | √ | ' ' | 运算符,枚举: ge :>= g :> |
| 3 | fvalue4 | 数值 | numeric | 23 | 2 |  | null | 数值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | flight4 |  | varchar | 50 |  | √ | ' ' | ,枚举: R :红色图标 Y :黄色图标 G :绿色图标 |
| 6 | fcondition4 | 条件 | varchar | 50 |  | √ | ' ' | 条件 |
| 7 | ftype4 | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: percent :百分比 numeral :数字 |
| 8 | ficonsty4 | 图标样式 | varchar | 50 |  | √ | ' ' | 图标样式,枚举: R :红色图标 Y :黄色图标 G :绿色图标 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fresultview4 | 结果预览 | varchar | 50 |  | √ | ' ' | 结果预览 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_delay_entry |  | fentryid |
| 2 | idx_plm_pm_delay_entry_fk |  | fid |

---

## 单据体-子表 t_plm_pm_resour_entry

- **表名称：** 单据体-子表
- **表名：** t_plm_pm_resour_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fsign7 | 运算符 | varchar | 50 |  | √ | ' ' | 运算符,枚举: ge :>= lt :< |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fcondition7 | 条件 | varchar | 50 |  | √ | ' ' | 条件 |
| 4 | ficonsty7 | 图标样式 | varchar | 50 |  | √ | ' ' | 图标样式,枚举: R :红色图标 Y :黄色图标 |
| 5 | flight7 |  | varchar | 50 |  | √ | ' ' | ,枚举: R :红色图标 Y :黄色图标 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fresultview7 | 结果预览 | varchar | 50 |  | √ | ' ' | 结果预览 |
| 8 | fvalue7 | 数值 | numeric | 23 | 2 |  | null | 数值 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | ftype7 | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: percent :百分比 numeral :数字 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pm_resour_entry |  | fentryid |
| 2 | idx_plm_pm_resour_entry_fk |  | fid |
