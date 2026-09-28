# 科目表版本化-bd_accounttableref

## 科目表版本化-使用范围表 t_bd_accounttableref_u

- **表名称：** 科目表版本化-使用范围表
- **表名：** t_bd_accounttableref_u

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
| 1 | pk_t_bd_accounttableref_u |  | fdataid,fuseorgid |
| 2 | idx_t_bd_accounttableref_u_uo |  | fuseorgid |

---

## 科目表版本化-多语言表 t_bd_accounttableref_l

- **表名称：** 科目表版本化-多语言表
- **表名：** t_bd_accounttableref_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_accounttableref_l |  | fid,flocaleid |
| 2 | pk_t_bd_accounttableref_l |  | fpkid |

---

## 科目表版本化-使用范围位图表 t_bd_accounttableref_m

- **表名称：** 科目表版本化-使用范围位图表
- **表名：** t_bd_accounttableref_m

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
| 1 | pk_t_bd_accounttableref_m |  | forgid |

---

## 核算维度差异子分录-子表 t_bd_assgrp_defval

- **表名称：** 核算维度差异子分录-子表
- **表名：** t_bd_assgrp_defval

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fvalue | 值 | varchar | 512 |  | √ | ' ' | 值 |
| 2 | fmustinput | 是否必录 | bpchar | 1 |  | √ | '0' | 是否必录 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 6 | fassisttypeid | 核算维度类型 | int8 | 64 |  | √ | 0 | [核算维度 bd_asstacttype](../basedata_files/bd_asstacttype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_bd_assgrp_defval |  | fdetailid |
| 2 | idx_bd_assgrp_defval |  | fentryid |

---

## 科目表版本化-主表 t_bd_accounttableref

- **表名称：** 科目表版本化-主表
- **表名：** t_bd_accounttableref

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnewacttableid | 目标科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 3 | fnewacttablebakid | 备份目标科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fcheckaccounttype | 新旧科目类型需一致 | bpchar | 1 |  | √ | '0' | 新旧科目类型需一致 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 17 | foldacttableid | 源科目表 | int8 | 64 |  | √ | 0 | [科目表 bd_accounttable](../fibd_files/bd_accounttable.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fenabledate | 启用日期 | timestamp | 0 |  |  | null | 启用日期 |
| 20 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 21 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | '6' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 22 | fisentrychange | 分录是否发生变更 | bpchar | 1 |  | √ | '0' | 分录是否发生变更 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_accounttableref |  | forgid |
| 2 | idx_t_bd_accounttableref_createorg |  | fcreateorgid |
| 3 | idx_t_bd_accounttableref_master |  | fmasterid |
| 4 | pk_t_bd_accounttableref |  | fid |

---

## 对照信息单据体-子表 t_bd_accounttablerefentry

- **表名称：** 对照信息单据体-子表
- **表名：** t_bd_accounttablerefentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fischange | 反启用后是否更改 | bpchar | 1 |  | √ | '0' | 反启用后是否更改 |
| 3 | foldaccountid | 源科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fismapping | 完全对照 | bpchar | 1 |  | √ | '0' | 完全对照,枚举: 0 :否 1 :是 2 :长编码未完全对照 3 :长名称未完全对照 4 :核算维度默认值未设置 |
| 6 | fnewaccountbakid | 备份目标科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fnewaccountid | 目标科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_accttablerefentry |  | fid |
| 2 | pk_t_bd_accounttablerefentry |  | fentryid |
