# 自动分摊方案设置-rdem_autoallocscheme

## 费用承担方-子表 t_pca_autoallocreceiver

- **表名称：** 费用承担方-子表
- **表名：** t_pca_autoallocreceiver

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fprojectid | 项目号 | int8 | 64 |  | √ | 0 | [项目成本核算对象 pca_costobject](../pca_files/pca_costobject.md) |
| 2 | fbizorgid | 业务组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fprojectkindid | 项目分类 | int8 | 64 |  | √ | 0 | [项目分类 bd_projectkind](../basedata_files/bd_projectkind.md) |
| 4 | ffilterfield | 过滤字段 | varchar | 30 |  | √ | ' ' | 过滤字段,枚举: biz_org :业务组织 dep :负责部门 project_kind :项目分类 project_number :项目号 project_phase :项目阶段 task_number :项目任务号 all_project :全部项目 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fdepid | 负责部门 | int8 | 64 |  | √ | 0 | [行政组织（部门） bos_adminorg](../base_files/bos_adminorg.md) |
| 8 | ftaskid | 项目任务号 | int8 | 64 |  | √ | 0 | [项目成本核算对象 pca_costobject](../pca_files/pca_costobject.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fprojectphaseid | 项目阶段 | int8 | 64 |  | √ | 0 | [项目阶段 bd_projectphase](../basedata_files/bd_projectphase.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_autoallocreceiver |  | fdetailid |
| 2 | idx_pca_autoallocreceiver |  | fentryid |

---

## 费用发送方-子表 t_pca_autoallocsender

- **表名称：** 费用发送方-子表
- **表名：** t_pca_autoallocsender

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fallocstandard | 分摊标准 | varchar | 30 |  | √ | ' ' | 分摊标准,枚举: report_hour :汇报工时 custom_alloc :自定义分摊 |
| 4 | fassgrpid | 核算维度 | varchar | 2000 |  | √ | ' ' | null 002 |
| 5 | fcostobjecttype | 分摊目标类型 | varchar | 10 |  | √ | ' ' | 分摊目标类型,枚举: P :项目 T :项目任务 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | faccountviewid | 会计科目 | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_autoallocsender |  | fentryid |
| 2 | idx_pca_autoallocsender |  | fid |

---

## 自动分摊方案设置-主表 t_pca_autoallocscheme

- **表名称：** 自动分摊方案设置-主表
- **表名：** t_pca_autoallocscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 方案编码 | varchar | 255 |  | √ | ' ' | 方案编码 |
| 14 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_autoallocscheme |  | fid |
| 2 | idx_pca_autoallocscheme1 |  | fnumber |
| 3 | idx_pca_autoallocscheme2 |  | fcostaccountid |

---

## 自动分摊方案设置-多语言表 t_pca_autoallocscheme_l

- **表名称：** 自动分摊方案设置-多语言表
- **表名：** t_pca_autoallocscheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 方案名称 | varchar | 255 |  | √ | ' ' | 方案名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_autoallocscheme_l |  | fpkid |
| 2 | idx_pca_autoallocscheme_l |  | fid,flocaleid |
