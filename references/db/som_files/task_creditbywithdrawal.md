# 信用加减分规则--批退原因-task_creditbywithdrawal

## 信用加减分规则--批退原因-使用范围表 t_tk_creditbywithdrawal_u

- **表名称：** 信用加减分规则--批退原因-使用范围表
- **表名：** t_tk_creditbywithdrawal_u

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
| 1 | idx_t_tk_creditbywithdrawal_u_uo |  | fuseorgid |
| 2 | t_tk_creditbywithdrawal_u_pkey |  | fdataid,fuseorgid |

---

## 信用加减分规则--批退原因-使用范围位图表 t_tk_creditbywithdrawal_m

- **表名称：** 信用加减分规则--批退原因-使用范围位图表
- **表名：** t_tk_creditbywithdrawal_m

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
| 1 | pk_t_tk_creditbywithdrawal_m |  | forgid |

---

## 信用加减分规则--批退原因-多语言表 t_tk_creditbywithdrawal_l

- **表名称：** 信用加减分规则--批退原因-多语言表
- **表名：** t_tk_creditbywithdrawal_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fsubscorestring | 减分str | varchar | 255 |  | √ | ' ' | 减分str |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_crewithdrawal_l_flocaleid |  | flocaleid |
| 2 | t_tk_creditbywithdrawal_l_pkey |  | fpkid |

---

## 信用加减分规则--批退原因-主表 t_tk_creditbywithdrawal

- **表名称：** 信用加减分规则--批退原因-主表
- **表名：** t_tk_creditbywithdrawal

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fwithdrawal | 批退原因 | int8 | 64 |  | √ | 0 | 批退原因 task_withdrawal |
| 7 | fsublevel | 减分至信用等级 | int8 | 64 |  | √ | 0 | 信用等级 task_creditlevel |
| 8 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 15 | fsubscorestring | fsubscorestring | varchar | 250 |  | √ | ' ' |  |
| 16 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fsubscore | 减分 | numeric | 19 | 6 | √ | 0.000000 | 减分 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 20 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 21 | fflag | 减分(0)或降级(1) | bpchar | 1 |  | √ | ' ' | 减分(0)或降级(1) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_creditbywit_fwithdrawal |  | fwithdrawal |
| 2 | t_tk_creditbywithdrawal_pkey |  | fid |
| 3 | idx_t_tk_creditbywithdrawal_master |  | fmasterid |
| 4 | idx_t_tk_creditbywithdrawal_createorg |  | fcreateorgid |
