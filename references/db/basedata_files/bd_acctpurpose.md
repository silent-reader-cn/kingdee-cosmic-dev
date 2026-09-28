# 账户用途-bd_acctpurpose

## 账户用途-使用范围表 t_bd_accpurpose_u

- **表名称：** 账户用途-使用范围表
- **表名：** t_bd_accpurpose_u

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fcreateorgid | fcreateorgid | int8 | 64 |  |  | null |  |
| 2 | fdataid | fdataid | int8 | 64 |  | √ | null |  |
| 3 | fuseorgid | fuseorgid | int8 | 64 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdataid | fdataid,fuseorgid |
| 2 | fuseorgid | fdataid,fuseorgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_accpurpose_u_uo |  | fuseorgid |
| 2 | t_bd_accpurpose_u_pkey |  | fdataid,fuseorgid |

---

## 账户用途-使用范围位图表 t_bd_accpurpose_m

- **表名称：** 账户用途-使用范围位图表
- **表名：** t_bd_accpurpose_m

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | forgid | forgid | int8 | 64 |  | √ | null |  |
| 2 | fdata | fdata | bytea | 0 |  | √ | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | forgid | forgid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_accpurpose_m |  | forgid |

---

## 账户用途-主表 t_bd_accpurpose

- **表名称：** 账户用途-主表
- **表名：** t_bd_accpurpose

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | fdisabledate | 禁用日期 | timestamp | 0 |  |  | null | 禁用日期 |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 80 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 11 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 12 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 13 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fname | 名称 | varchar | 500 |  |  | ' ' | 名称 |
| 15 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 16 | fparentid | 上级账户用途 | int8 | 64 |  | √ | 0 | [账户用途 bd_acctpurpose](../basedata_files/bd_acctpurpose.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | ffullname | ffullname | varchar | 520 |  |  | ' ' |  |
| 19 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 20 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 21 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 23 | forder | 排序号 | varchar | 80 |  | √ | ' ' | 排序号 |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 26 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_accpurp_num |  | fnumber |
| 2 | t_bd_accpurpose_pkey |  | fid |
| 3 | idx_t_bd_accpurpose_master |  | fmasterid |
| 4 | idx_t_bd_accpurpose_createorg |  | fcreateorgid |

---

## 账户用途-多语言表 t_bd_accpurpose_l

- **表名称：** 账户用途-多语言表
- **表名：** t_bd_accpurpose_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  |  | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 520 |  |  | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_bd_accpurpose_l |  | fid,flocaleid |
| 2 | t_bd_accpurpose_l_pkey |  | fpkid |
