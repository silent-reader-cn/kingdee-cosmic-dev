# 研发公共费用来源设置-rdem_collallocset

## 会计科目-多选基础资料表 t_pca_collallocset_e_ac

- **表名称：** 会计科目-多选基础资料表
- **表名：** t_pca_collallocset_e_ac

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [会计科目 bd_accountview](../gl_files/bd_accountview.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_collallocset_e_ac |  | fpkid |
| 2 | idx_pca_caset_e_acfk |  | fentryid |

---

## 项目任务-多选基础资料表 t_pca_collallocset_e_ta

- **表名称：** 项目任务-多选基础资料表
- **表名：** t_pca_collallocset_e_ta

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [项目成本核算对象 pca_costobject](../pca_files/pca_costobject.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_collallocset_e_ta |  | fpkid |
| 2 | idx_pca_caset_e_tafk |  | fentryid |

---

## 来源与分摊-多语言表 t_pca_collallocsetentry_l

- **表名称：** 来源与分摊-多语言表
- **表名：** t_pca_collallocsetentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcardname | 卡片名称 | varchar | 255 |  | √ | ' ' | 卡片名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_pca_collallocsetentry_l |  | fpkid |
| 2 | idx_pca_collallocset_e_l_0 |  | fentryid,flocaleid |

---

## 研发公共费用来源设置-主表 t_pca_collallocset

- **表名称：** 研发公共费用来源设置-主表
- **表名：** t_pca_collallocset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 7 | faccountbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  |  | null | 主数据内码 |
| 12 | fcostaccountid | 项目核算主体 | int8 | 64 |  | √ | 0 | [项目核算主体 pca_costaccount](../pca_files/pca_costaccount.md) |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 15 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_collallocset_m0 |  | fmasterid |
| 2 | idx_pca_collallocset_ca |  | fcostaccountid |
| 3 | pk_pca_collallocset |  | fid |

---

## 来源与分摊-子表 t_pca_collallocsetentry

- **表名称：** 来源与分摊-子表
- **表名：** t_pca_collallocsetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsubelementid | 成本子要素 | int8 | 64 |  | √ | 0 | [成本子要素 cad_subelement](../basedata_files/cad_subelement.md) |
| 3 | fglassgrp | 核算维度值 | varchar | 2000 |  | √ | ' ' | 核算维度值 |
| 4 | fallocstdgroupid | 分摊标准 | int8 | 64 |  | √ | 0 | [自定义分摊标准（组） pca_cusalloc_stdgroup](../pca_files/pca_cusalloc_stdgroup.md) |
| 5 | freceiver | 接收方（来自分摊标准） | varchar | 50 |  | √ | ' ' | 接收方（来自分摊标准）,枚举: all_projects :分摊标准内全部项目 all_tasks :分摊标准内全部任务 filtered_projects :通过条件筛选项目 filtered_tasks :通过条件筛选项目任务 specified_project :指定项目 specified_task :指定项目任务 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fallocmethod | 分摊方式 | varchar | 50 |  | √ | ' ' | 分摊方式,枚举: manual_alloc :手动分摊 auto_alloc :自动分摊 |
| 8 | fchangedcosttype | 成本变动方向 | varchar | 50 |  | √ | ' ' | 成本变动方向,枚举: 0 :减 1 :增 |
| 9 | fcardname | 卡片名称 | varchar | 255 |  | √ | ' ' | 卡片名称 |
| 10 | fruleid | 条件规则 | int8 | 64 |  | √ | 0 | [项目公共费用分摊规则 pca_alloc_revrule](../pca_files/pca_alloc_revrule.md) |
| 11 | fdirection | 借贷方向 | varchar | 50 |  | √ | ' ' | 借贷方向,枚举: 1 :借方 -1 :贷方 |
| 12 | fallocstdtype | 分摊标准 | varchar | 50 |  | √ | ' ' | 分摊标准,枚举: report_hour :汇报工时 custom_alloc :自定义 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 14 | facctviewbaltype | 取值来源 | varchar | 50 |  | √ | ' ' | 取值来源,枚举: 1 :实际损益发生额 2 :凭证 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_collallocset_e_fk |  | fid |
| 2 | pk_pca_collallocsetentry |  | fentryid |

---

## 研发公共费用来源设置-多语言表 t_pca_collallocset_l

- **表名称：** 研发公共费用来源设置-多语言表
- **表名：** t_pca_collallocset_l

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
| 1 | pk_pca_collallocset_l |  | fpkid |
| 2 | idx_pca_collallocset_l_0 |  | fid,flocaleid |

---

## 项目-多选基础资料表 t_pca_collallocset_e_pr

- **表名称：** 项目-多选基础资料表
- **表名：** t_pca_collallocset_e_pr

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [项目成本核算对象 pca_costobject](../pca_files/pca_costobject.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pca_caset_e_prfk |  | fentryid |
| 2 | pk_pca_collallocset_e_pr |  | fpkid |
