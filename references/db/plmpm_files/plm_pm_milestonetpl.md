# 里程碑模板-plm_pm_milestonetpl

## 里程碑模板-多语言表 t_plm_ipd_milestone_l

- **表名称：** 里程碑模板-多语言表
- **表名：** t_plm_ipd_milestone_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_milestone_l |  | fpkid |
| 2 | idx_plm_ipd_milestone_l_0 |  | fid,flocaleid |

---

## 前置任务-多选基础资料表 plm_ipd_milestonepretask

- **表名称：** 前置任务-多选基础资料表
- **表名：** plm_ipd_milestonepretask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [任务模板 plm_pm_tasktpl](../plmpm_files/plm_pm_tasktpl.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ipd_basedataid |  | fbasedataid |
| 2 | pk_plm_ipd_milestonepretask |  | fpkid |

---

## 里程碑模板-主表 t_plm_ipd_milestone

- **表名称：** 里程碑模板-主表
- **表名：** t_plm_ipd_milestone

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | [工作项类型配置 plm_ipditemgroup](../plmipdsm_files/plm_ipditemgroup.md) |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fprophase | 项目阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |
| 5 | fparenttask | 父项任务 | int8 | 64 |  | √ | 0 | [任务模板 plm_pm_tasktpl](../plmpm_files/plm_pm_tasktpl.md) |
| 6 | fmilestonefield | 所属领域 | int8 | 64 |  | √ | 0 | [专业领域 plm_pm_proffield](../plmpm_files/plm_pm_proffield.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fenddate | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fseqnumber | 顺序 | varchar | 100 |  | √ | ' ' | 顺序 |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 14 | fcreatetype | 创建方式 | varchar | 50 |  | √ | ' ' | 创建方式,枚举: 1 :项目任务书下推生成 2 :手动新建 3 :甘特图行新建 |
| 15 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 16 | fposition | 位置 | varchar | 50 |  | √ | ' ' | 位置,枚举: up :上 down :下 |
| 17 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 18 | fwbsnumber | WBS编码 | varchar | 50 |  | √ | ' ' | WBS编码 |
| 19 | fdeliverradio | 交付物完成率 | numeric | 23 | 10 |  | null | 交付物完成率 |
| 20 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 22 | fprojectid | 所属项目 | int8 | 64 |  | √ | 0 | [项目模板 plm_pm_projecttpl](../plmpm_files/plm_pm_projecttpl.md) |
| 23 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 24 | fdistfield | 领域下发 | bpchar | 1 |  | √ | '0' | 领域下发 |
| 25 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 26 | factenddate | 实际完成时间 | timestamp | 0 |  |  | null | 实际完成时间 |
| 27 | fsourcemilestoneid | fsourcemilestoneid | varchar | 50 |  | √ | ' ' |  |
| 28 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 29 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 30 | fphase | 阶段 | int8 | 64 |  | √ | 0 | [研发阶段 plm_pm_development](../plmpm_files/plm_pm_development.md) |
| 31 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |
| 32 | fcombofield | 里程碑状态 | varchar | 50 |  | √ | ' ' | 里程碑状态,枚举: A :未完成 B :已完成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_milestone |  | fid |
| 2 | idx_plm_ipd_milestone_m0 |  | fmasterid |
