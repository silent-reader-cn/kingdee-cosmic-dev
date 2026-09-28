# 预算组织-xkbm_budgetorgunit

## 单据体-子表 t_xkbm_orgunitentity

- **表名称：** 单据体-子表
- **表名：** t_xkbm_orgunitentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbudgetorgversionid | 组织架构版本组 | int8 | 64 |  | √ | 0 | 组织架构版本组 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_orgunitentity_id |  | fid |
| 2 | pk_xkbm_orgunitentity |  | fentryid |

---

## 子单据体-多语言表 t_xkbm_orgunitsubentity_l

- **表名称：** 子单据体-多语言表
- **表名：** t_xkbm_orgunitsubentity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentityname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 2 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_orgsubentity_l_fid |  | fdetailid |
| 2 | pk_xkbm_orgsubentity_ll |  | fpkid |

---

## 预算组织-多语言表 t_xkbm_orgunit_l

- **表名称：** 预算组织-多语言表
- **表名：** t_xkbm_orgunit_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkbm_orgunit_l |  | fid,flocaleid |
| 2 | pk_xkbm_orgunit_l |  | fpkid |

---

## 子单据体-子表 t_xkbm_orgunitsubentity

- **表名称：** 子单据体-子表
- **表名：** t_xkbm_orgunitsubentity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fentityname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 2 | fparentorgid | 上级组织ID | int8 | 64 |  | √ | 0 | 上级组织ID |
| 3 | fbudgetorgid | 组织架构id | int8 | 64 |  | √ | 0 | 组织架构id |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentitynumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 6 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 8 | fversion | 版本 | varchar | 50 |  | √ | ' ' | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_orgunitsubentity |  | fdetailid |
| 2 | idx_bm_orgunitsubentity |  | fentryid |

---

## 预算组织-主表 t_xkbm_orgunit

- **表名称：** 预算组织-主表
- **表名：** t_xkbm_orgunit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fownerorgid | 所属组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fdeptorgid | 来源基础资料 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | forgtype | 组织类型 | varchar | 50 |  | √ | ' ' | 组织类型,枚举: DEPT :部门 ORG :组织 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | forgclass | 来源基础资料类型 | varchar | 50 |  | √ | ' ' | 来源基础资料类型,枚举: bos_org :业务单元 bos_adminorg :行政组织（部门） |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 16 | fforbiddate | fforbiddate | timestamp | 0 |  |  | null |  |
| 17 | fforbidderid | fforbidderid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkbm_orgunit |  | fid |
| 2 | idx_xkbm_orgunit_number |  | fnumber |
