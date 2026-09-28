# 信控维度-ccm_dimension

## 信控维度-主表 t_ccm_dimension

- **表名称：** 信控维度-主表
- **表名：** t_ccm_dimension

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 4 | fdefoverquo | 默认逾期额度 | numeric | 23 | 10 | √ | 0 | 默认逾期额度 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgscope | 默认控制组织范围 | varchar | 50 |  | √ | ' ' | 默认控制组织范围,枚举: GLOBAL :集团范围 SINGLE :业务组织范围 |
| 7 | fdefsinglebal | 默认单笔限额 | numeric | 23 | 10 | √ | 0 | 默认单笔限额 |
| 8 | fdefexrate | 默认汇率表 | int8 | 64 |  | √ | 0 | [汇率表 bd_exratetable](../base_files/bd_exratetable.md) |
| 9 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 60 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fdefquo | 默认信用额度 | numeric | 23 | 10 | √ | 0 | 默认信用额度 |
| 15 | fdefscheme | 默认信控方案 | int8 | 64 |  | √ | 0 | [信用控制方案 ccm_schemes](../ccm_files/ccm_schemes.md) |
| 16 | fdefcurrency | 默认币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 17 | fenable | 使用状态 | varchar | 60 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fdefsinglecontrol | 默认币种隔离 | bpchar | 1 |  | √ | '0' | 默认币种隔离 |
| 19 | fdefpress | 默认压批批数 | int4 | 32 |  | √ | 0 | 默认压批批数 |
| 20 | fdefdays | 默认信用天数 | int4 | 32 |  | √ | 0 | 默认信用天数 |
| 21 | fnumber | 编码 | varchar | 120 |  | √ | ' ' | 编码 |
| 22 | fisdefault | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 23 | fautocrearchive | 自动创建信用档案 | bpchar | 1 |  | √ | '0' | 自动创建信用档案 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_ds_fnumber |  | fnumber |
| 2 | t_ccm_dimension_pkey |  | fid |

---

## 维度成员-子表 t_ccm_dimensionentry

- **表名称：** 维度成员-子表
- **表名：** t_ccm_dimensionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | 维度成员类型 | varchar | 80 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 3 | froleid | 维度成员 | int8 | 64 |  | √ | 0 | [维度成员 ccm_role](../ccm_files/ccm_role.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | frolenumber | 维度成员编码 | varchar | 80 |  | √ | ' ' | 维度成员编码 |
| 6 | frolename | 维度成员名称 | varchar | 80 |  | √ | ' ' | 维度成员名称 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ccm_ds_fid |  | fid |
| 2 | t_ccm_dimensionentry_pkey |  | fentryid |

---

## 信控维度-多语言表 t_ccm_dimension_l

- **表名称：** 信控维度-多语言表
- **表名：** t_ccm_dimension_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
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
| 1 | t_ccm_dimension_l_pkey |  | fpkid |
| 2 | idx_ccm_ds_fid_flocale |  | fid,flocaleid |
