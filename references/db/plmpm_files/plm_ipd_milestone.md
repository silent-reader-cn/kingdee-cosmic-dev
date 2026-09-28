# 里程碑-plm_ipd_milestone

## 里程碑-多语言表 t_plm_ipd_milestone_l

- **表名称：** 里程碑-多语言表
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
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 任务 plm_ipd_task |
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

## 里程碑-主表 t_plm_ipd_milestone

- **表名称：** 里程碑-主表
- **表名：** t_plm_ipd_milestone

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fwbsnumber | WBS编码 | varchar | 50 |  | √ | ' ' | WBS编码 |
| 4 | fdeliverradio | 交付物完成率 | numeric | 23 | 10 |  | null | 交付物完成率 |
| 5 | fgroupid | 分组 | int8 | 64 |  | √ | 0 | 工作项类型配置 plm_ipditemgroup |
| 6 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 8 | fprojectid | 所属项目 | int8 | 64 |  | √ | 0 | 项目 plm_ipd_project |
| 9 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 11 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | factenddate | 实际完成时间 | timestamp | 0 |  |  | null | 实际完成时间 |
| 14 | fenddate | 计划完成时间 | timestamp | 0 |  |  | null | 计划完成时间 |
| 15 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 19 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 20 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 21 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 22 | fphase | 阶段 | int8 | 64 |  | √ | 0 | 研发阶段 plm_pm_development |
| 23 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |
| 24 | fcombofield | 里程碑状态 | varchar | 50 |  | √ | ' ' | 里程碑状态,枚举: A :未完成 B :已完成 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_ipd_milestone |  | fid |
| 2 | idx_plm_ipd_milestone_m0 |  | fmasterid |
