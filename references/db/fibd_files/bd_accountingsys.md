# 核算体系（已作废）-bd_accountingsys

## 核算体系（已作废）-主表 t_bd_accountingsys

- **表名称：** 核算体系（已作废）-主表
- **表名：** t_bd_accountingsys

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fislegal | 法人核算体系 | bpchar | 1 |  | √ | '0' | 法人核算体系 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 12 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 13 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 14 | fisdefaultsys | fisdefaultsys | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accountingsys_pkey |  | fid |
| 2 | idx_bd_accountingsys |  | fnumber |

---

## 记账范围分录-子表 t_bd_accountingsys_bizorg

- **表名称：** 记账范围分录-子表
- **表名：** t_bd_accountingsys_bizorg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizacctorgidb | fbizacctorgidb | int8 | 64 |  | √ | 0 |  |
| 3 | fbizorgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fbizorgidb | fbizorgidb | int8 | 64 |  | √ | 0 |  |
| 6 | fxkdefaultpolicyid | fxkdefaultpolicyid | int8 | 64 |  | √ | 0 |  |
| 7 | fdescription | fdescription | varchar | 100 |  | √ | ' ' |  |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fbizacctorgid | 记账范围 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 10 | fdefaultpolicyid | fdefaultpolicyid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_accountingsys_bizorg |  | fentryid |
| 2 | idx_accountingsys_bizorg_fid |  | fid |

---

## 核算体系（已作废）-多语言表 t_bd_accountingsys_l

- **表名称：** 核算体系（已作废）-多语言表
- **表名：** t_bd_accountingsys_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdesc | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_accountingsys_l_pkey |  | fpkid |
| 2 | idx_bd_accountingsys_l_id |  | fid,flocaleid |
