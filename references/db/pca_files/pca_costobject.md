# 项目成本核算对象-pca_costobject

## 项目成本核算对象-多语言表 t_pca_costobject_l

- **表名称：** 项目成本核算对象-多语言表
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

---

## 项目成本核算对象-主表 t_pca_costobject

- **表名称：** 项目成本核算对象-主表
- **表名：** t_pca_costobject

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子节点 | bpchar | 1 |  | √ | '0' | 是否叶子节点 |
| 3 | factualenddate | 实际结束日期 | timestamp | 0 |  |  | null | 实际结束日期 |
| 4 | forgid | 负责部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | frelprojectid | 关联子项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 11 | fcollrelid | 归集匹配内码 | int8 | 64 |  | √ | 0 | 归集匹配内码 |
| 12 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fprojectid | 所属项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fsrcbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 17 | fiscostindcal | 成本独立结算 | bpchar | 1 |  | √ | '0' | 成本独立结算 |
| 18 | fdatatypesrcid | 类型来源 | varchar | 50 |  | √ | '0' | 类型来源,枚举: bd_projectkind :项目分类 mpm_taskcntrcode :任务类型 |
| 19 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 20 | factualbegindate | 实际开始日期 | timestamp | 0 |  |  | null | 实际开始日期 |
| 21 | frootproject | 所属根项目 | int8 | 64 |  | √ | 0 | 项目 bd_project |
| 22 | fstatustypeid | 项目状态类型 | int8 | 64 |  | √ | 0 | 状态类型 bd_statustype |
| 23 | fdatatypeid | 类型 | int8 | 64 |  | √ | 0 | 项目分类 bd_projectkind |
| 24 | fcostobjecttype | 核算对象分类 | varchar | 255 |  | √ | ' ' | 核算对象分类,枚举: P :项目 T :项目任务 |
| 25 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 27 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 28 | fprojectphaseid | 项目阶段 | int8 | 64 |  | √ | 0 | 项目阶段 mpm_projectphase |
| 29 | fprojectlongnum | 项目长编码 | varchar | 850 |  | √ | ' ' | 项目长编码 |

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
