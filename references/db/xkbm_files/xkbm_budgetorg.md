# 预算组织架构-xkbm_budgetorg

## 树形单据体-多语言表 t_xkbm_budgetorgentry_l

- **表名称：** 树形单据体-多语言表
- **表名：** t_xkbm_budgetorgentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgviewnumber | 预算组织 | varchar | 255 |  | √ | ' ' | 预算组织 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | forgname | 组织名称 | varchar | 255 |  | √ | ' ' | 组织名称 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_budgetorgentry_l |  | fpkid |
| 2 | idx_xkbm_budgetoentry_l_name |  | flocaleid,forgname |
| 3 | idx_xkbm_budgetoentry_l_etyid |  | fentryid |

---

## 树形单据体-子表 t_xkbm_budgetorgentry

- **表名称：** 树形单据体-子表
- **表名：** t_xkbm_budgetorgentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | forgviewnumber | 预算组织 | varchar | 255 |  | √ | ' ' | 预算组织 |
| 3 | fbudgetnumber | 预算组织编码 | varchar | 255 |  | √ | ' ' | 预算组织编码 |
| 4 | fparentorgid | 上级组织ID | int8 | 64 |  | √ | 0 | 上级组织ID |
| 5 | fownerorgid | 所属组织ID | int8 | 64 |  | √ | 0 | 所属组织ID |
| 6 | fbudgetorgunitid | 预算组织 | int8 | 64 |  | √ | 0 | [预算组织 xkbm_budgetorgunit](../xkbm_files/xkbm_budgetorgunit.md) |
| 7 | fdeptorgid | 组织ID | int8 | 64 |  | √ | 0 | 组织ID |
| 8 | forgnumber | 预算组织 | varchar | 255 |  | √ | ' ' | 预算组织 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | forgtype | 组织类型 | varchar | 20 |  | √ | ' ' | 组织类型,枚举: DEPT :部门 ORG :组织 |
| 11 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 12 | forgname | 组织名称 | varchar | 255 |  | √ | ' ' | 组织名称 |
| 13 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_budgetorgentry |  | fentryid |
| 2 | idx_xkbm_budgetorgentry_fid |  | fid |

---

## 预算组织架构-主表 t_xkbm_budgetorg

- **表名称：** 预算组织架构-主表
- **表名：** t_xkbm_budgetorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxkbmbusinessservice | 所属应用 | int8 | 64 |  | √ | 0 | [预算业务服务 xkbm_businessservice](../xkbm_files/xkbm_businessservice.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | frootorgid | 顶层预算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fnonerootorg | 无顶层组织 | bpchar | 1 |  | √ | '0' | 无顶层组织 |
| 7 | fisdefaultversion | 是否默认版本 | bpchar | 1 |  | √ | '1' | 是否默认版本 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fversionremark | 版本备注 | varchar | 255 |  | √ | ' ' | 版本备注 |
| 10 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 11 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fversiongroupid | 版本组 | int8 | 64 |  | √ | 0 | 版本组 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 19 | fversionname | 版本名称 | varchar | 255 |  | √ | ' ' | 版本名称 |
| 20 | fforbiddate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 21 | fforbidderid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fisdefault | 默认 | bpchar | 1 |  | √ | '1' | 默认 |
| 23 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |
| 24 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_budgetorg_number |  | fnumber |
| 2 | pk_xkbm_budgetorg |  | fid |

---

## 预算组织架构-多语言表 t_xkbm_budgetorg_l

- **表名称：** 预算组织架构-多语言表
- **表名：** t_xkbm_budgetorg_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fversionremark | 版本备注 | varchar | 255 |  | √ | ' ' | 版本备注 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fversionname | 版本名称 | varchar | 255 |  | √ | ' ' | 版本名称 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_budgetorg_l_fname |  | flocaleid,fname |
| 2 | pk_xkbm_budgetorg_l |  | fpkid |
| 3 | idx_xkbm_budgetorg_l_fid |  | fid |
