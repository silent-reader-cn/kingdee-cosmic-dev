# 合并规则-mpdm_mergerule

## 合并规则-多语言表 t_mpdm_mergerule_l

- **表名称：** 合并规则-多语言表
- **表名：** t_mpdm_mergerule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_mergerule_l |  | fid,flocaleid |
| 2 | t_mpdm_mergerule_l_pkey |  | fpkid |

---

## 合并规则-使用范围位图表 t_mpdm_mergerule_m

- **表名称：** 合并规则-使用范围位图表
- **表名：** t_mpdm_mergerule_m

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
| 1 | pk_t_mpdm_mergerule_m |  | forgid |

---

## 合并规则-使用范围表 t_mpdm_mergerule_u

- **表名称：** 合并规则-使用范围表
- **表名：** t_mpdm_mergerule_u

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
| 1 | t_mpdm_mergerule_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_mpdm_mergerule_u_uo |  | fuseorgid |

---

## 合并规则-主表 t_mpdm_mergerule

- **表名称：** 合并规则-主表
- **表名：** t_mpdm_mergerule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmergetype | 合并日期类型 | varchar | 30 |  | √ | ' ' | 合并日期类型,枚举: A :周期最早 B :周期最晚 |
| 3 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 4 | fchoosecycle | 指定周期 | int8 | 64 |  | √ | 0 | 合并周期 mpdm_mergecycle |
| 5 | fmergedimen | 合并维度 | int8 | 64 |  | √ | 0 | 合并维度 mpdm_mergedimension |
| 6 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fis_require_source | 考虑需求来源号 | bpchar | 1 |  | √ | '0' | 考虑需求来源号 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fmergetime | 合并时机 | varchar | 30 |  | √ | ' ' | 合并时机,枚举: A :净需求合并 B :毛需求合并 |
| 13 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 14 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 15 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | fctrlstrategy | 控制策略 | varchar | 30 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 19 | fdate_offsetday | 合并日期偏移天数 | int4 | 32 |  | √ | 0 | 合并日期偏移天数 |
| 20 | fdynamiccycle | 动态周期(天) | int8 | 64 |  | √ | 0 | 动态周期(天) |
| 21 | fcycletype | 周期类型 | varchar | 30 |  | √ | ' ' | 周期类型,枚举: A :动态 B :固定 C :指定 |
| 22 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fsplitbatch | 分割批量 | int8 | 64 |  | √ | 0 | 分割批量 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |
| 26 | ffixedcycle | 固定周期(天) | int8 | 64 |  | √ | 0 | 固定周期(天) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mpdm_mergerule_master |  | fmasterid |
| 2 | idx_t_mpdm_mergerule_createorg |  | fcreateorgid |
| 3 | idx_mpdm_mergerule |  | fnumber,fcreateorgid |
| 4 | t_mpdm_mergerule_pkey |  | fid |
