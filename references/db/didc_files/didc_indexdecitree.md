# 指标决策树-didc_indexdecitree

## 指标决策树-主表 t_didc_indextree

- **表名称：** 指标决策树-主表
- **表名：** t_didc_indextree

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fgroupid | 指标树分类 | int8 | 64 |  | √ | 0 | [指标树分类 didc_indextreegroup](../didc_files/didc_indextreegroup.md) |
| 4 | fname | 决策树名称 | varchar | 255 |  | √ | ' ' | 决策树名称 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ffiltervalue | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fpreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 12 | ffiltervalue_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 13 | finformation | 主题描述 | varchar | 255 |  | √ | ' ' | 主题描述 |
| 14 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 决策树编码 | varchar | 30 |  | √ | ' ' | 决策树编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_didc_indextree |  | fid |
| 2 | idx_didc_indextree |  | fnumber |

---

## 角色权限-子表 t_didc_decitree_role

- **表名称：** 角色权限-子表
- **表名：** t_didc_decitree_role

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | froleid | 角色 | varchar | 36 |  | √ | ' ' | [通用角色 perm_role](../base_files/perm_role.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_decitree_role |  | fid |
| 2 | pk_didc_decitree_role |  | fentryid |

---

## 树形单据体-多语言表 t_didc_indextreeentry_l

- **表名称：** 树形单据体-多语言表
- **表名：** t_didc_indextreeentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 255 |  | √ | ' ' | localeid |
| 2 | fcontent | 分析内容 | varchar | 255 |  | √ | ' ' | 分析内容 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_indextreeentry_l |  | fentryid,flocaleid |
| 2 | pk_didc_indextreeentry_l |  | fpkid |

---

## 指标决策树-多语言表 t_didc_indextree_l

- **表名称：** 指标决策树-多语言表
- **表名：** t_didc_indextree_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 决策树名称 | varchar | 255 |  | √ | ' ' | 决策树名称 |
| 3 | finformation | 主题描述 | varchar | 255 |  | √ | ' ' | 主题描述 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_indextree_l |  | fid,flocaleid |
| 2 | pk_didc_indextree_l |  | fpkid |

---

## 用户权限-子表 t_didc_decitree_user

- **表名称：** 用户权限-子表
- **表名：** t_didc_decitree_user

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fuserfield | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_didc_decitree_user |  | fentryid |
| 2 | idx_didc_decitree_user |  | fid |

---

## 树形单据体-子表 t_didc_indextreeentry

- **表名称：** 树形单据体-子表
- **表名：** t_didc_indextreeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftreefiltervalue | 过滤条件内容 | varchar | 2000 |  | √ | ' ' | 过滤条件内容 |
| 3 | ftreefilter | 指标过滤 | varchar | 2000 |  | √ | ' ' | 指标过滤 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 6 | ftargetvalue | 目标值 | varchar | 50 |  | √ | ' ' | 目标值 |
| 7 | fuserid | 责任人 | int8 | 64 |  | √ | 0 | [用户信息 bos_usergroup_user](../base_files/bos_usergroup_user.md) |
| 8 | findexid | 关联指标 | int8 | 64 |  | √ | 0 | [数智指标 didc_indexcatalogue](../didc_files/didc_indexcatalogue.md) |
| 9 | fcontent | 分析内容 | varchar | 255 |  | √ | ' ' | 分析内容 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_didc_indextreeentry |  | fentryid |
| 2 | idx_didc_indextreeentry |  | fid |
