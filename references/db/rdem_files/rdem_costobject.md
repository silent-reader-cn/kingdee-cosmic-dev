# 研发费用核算对象-rdem_costobject

## 研发费用核算对象-主表 t_pca_costobject

- **表名称：** 研发费用核算对象-主表
- **表名：** t_pca_costobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子节点 | bpchar | 1 |  | √ | '0' | 是否叶子节点 |
| 3 | factualenddate | 实际结束日期 | timestamp | 0 |  |  | null | 实际结束日期 |
| 4 | forgid | 负责部门 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsrcbizop | 商机 | int8 | 64 |  | √ | 0 | [商机登记F7 mpm_bizopregf7](../mpm_files/mpm_bizopregf7.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | frelprojectid | 虚任务关联项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 9 | ftaskcntrcodeid | 业务类型 | int8 | 64 |  | √ | 0 | [任务业务类型 mpm_taskcntrcode](../mpm_files/mpm_taskcntrcode.md) |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fsourcetype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型,枚举: A :手工录入 B :项目云项目 C :PLM创建 D :项目云商机 |
| 14 | fcollrelid | 归集匹配内码 | int8 | 64 |  | √ | 0 | 归集匹配内码 |
| 15 | fsrcprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 16 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fprojectid | 上级项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | fsrcbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 21 | fiscostindcal | 成本独立结算 | bpchar | 1 |  | √ | '0' | 成本独立结算 |
| 22 | fdatatypesrcid | 类型来源 | varchar | 50 |  | √ | '0' | 类型来源,枚举: bd_projectkind :项目分类 bd_tasktype :任务类型 |
| 23 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 24 | factualbegindate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 25 | frootproject | 所属根项目(废弃) | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 26 | fsrcprojecttaskid | 项目任务 | int8 | 64 |  | √ | 0 | [项目任务 bd_projecttask](../basedata_files/bd_projecttask.md) |
| 27 | fstatustypeid | 项目状态类型 | int8 | 64 |  | √ | 0 | [状态类型 bd_statustype](../basedata_files/bd_statustype.md) |
| 28 | fdatatypeid | 类型 | int8 | 64 |  | √ | 0 | 项目分类 bd_projectkind |
| 29 | fprojectkindid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 30 | fcostobjecttype | 核算对象类型 | varchar | 255 |  | √ | ' ' | 核算对象类型,枚举: P :项目 T :项目任务 |
| 31 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 33 | fprojecttype | 项目类型 | varchar | 50 |  | √ | ' ' | 项目类型,枚举: 0 :普通项目 1 :研发项目 |
| 34 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 35 | fprojectphaseid | 项目阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |
| 36 | fprojectlongnum | 项目长编码 | varchar | 850 |  | √ | ' ' | 项目长编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_costobject_rootproject |  | frootproject,fisleaf |
| 2 | idx_pca_costobject_num |  | fnumber |
| 3 | pk_pca_costobject |  | fid |
| 4 | idx_pca_costobject_bizorg |  | fbizorgid |

---

## 研发费用核算对象-多语言表 t_pca_costobject_l

- **表名称：** 研发费用核算对象-多语言表
- **表名：** t_pca_costobject_l

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
| 1 | pk_pca_costobject_l |  | fpkid |
