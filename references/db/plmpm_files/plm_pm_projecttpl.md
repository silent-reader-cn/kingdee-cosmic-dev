# 项目模板-plm_pm_projecttpl

## 项目模板-主表 t_plm_pm_projecttpl

- **表名称：** 项目模板-主表
- **表名：** t_plm_pm_projecttpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fconstructionperiod | 计划工期(天) | numeric | 23 | 1 | √ | 0 | 计划工期(天) |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fproductlib | 产品库 | int8 | 64 |  | √ | 0 | [产品库 plm_pdm_repo_product](../plmpdm_files/plm_pdm_repo_product.md) |
| 4 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [项目分组 plm_pm_projectgroup](../plmpm_files/plm_pm_projectgroup.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | factendtime | 实际周期.结束 | timestamp | 0 |  |  | null | 实际周期.结束 |
| 7 | fprojectkind | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 plm_pm_projectkind](../plmpm_files/plm_pm_projectkind.md) |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 9 | fisproffield | 启用专业领域计划 | bpchar | 1 |  | √ | '0' | 启用专业领域计划 |
| 10 | fcontrolmode | 管控模式 | varchar | 50 |  | √ | ' ' | 管控模式,枚举: 101 :自上而下 102 :自下而上 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | factbegintime | 实际周期.开始 | timestamp | 0 |  |  | null | 实际周期.开始 |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fworkinghours | 计划工时(h) | numeric | 23 | 1 | √ | 0 | 计划工时(h) |
| 19 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 22 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 23 | fstarttime | 计划周期.开始 | timestamp | 0 |  |  | null | 计划周期.开始 |
| 24 | fctrlstrategy | 控制策略 | varchar | 50 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 25 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fcalendarexampleid | 日历实例 | int8 | 64 |  | √ | 0 | [配置-项目日历 plm_ipd_projectcal](../plmpm_files/plm_ipd_projectcal.md) |
| 27 | fendtime | 计划周期.结束 | timestamp | 0 |  |  | null | 计划周期.结束 |
| 28 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 29 | fprojectcalendarid | 项目日历 | int8 | 64 |  | √ | 0 | [日历模板 plm_ipd_calendar](../plmpm_files/plm_ipd_calendar.md) |
| 30 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_pm_projecttpl_createorg |  | fcreateorgid |
| 2 | pk_plm_pm_projecttpl |  | fid |
| 3 | idx_t_plm_pm_projecttpl_master |  | fmasterid |
| 4 | idx_plm_pm_projecttpl_m0 |  | fnumber |

---

## 项目模板-使用范围表 t_plm_pm_projecttpl_u

- **表名称：** 项目模板-使用范围表
- **表名：** t_plm_pm_projecttpl_u

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
| 1 | idx_t_plm_pm_projecttpl_u_uo |  | fuseorgid |
| 2 | pk_t_plm_pm_projecttpl_u |  | fdataid,fuseorgid |

---

## 项目模板-多语言表 t_plm_pm_projecttpl_l

- **表名称：** 项目模板-多语言表
- **表名：** t_plm_pm_projecttpl_l

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
| 1 | idx_plm_pm_projecttpl_l_0 |  | fid,flocaleid |
| 2 | pk_plm_pm_projecttpl_l |  | fpkid |
