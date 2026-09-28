# 资产政策-fa_depresystem

## 资产政策-使用范围位图表 t_fa_depresystem_m

- **表名称：** 资产政策-使用范围位图表
- **表名：** t_fa_depresystem_m

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
| 1 | pk_t_fa_depresystem_m |  | forgid |

---

## 资产政策-多语言表 t_fa_depresystem_l

- **表名称：** 资产政策-多语言表
- **表名：** t_fa_depresystem_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  |  | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 36 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_depresystem_l_pkey |  | fpkid |
| 2 | idx_fa_depsys_l_fid |  | fid |

---

## 资产政策-使用范围表 t_fa_depresystem_u

- **表名称：** 资产政策-使用范围表
- **表名：** t_fa_depresystem_u

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
| 1 | t_fa_depresystem_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_fa_depresystem_u_uo |  | fuseorgid |

---

## 资产政策信息-子表 t_fa_depresystemapentry

- **表名称：** 资产政策信息-子表
- **表名：** t_fa_depresystemapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdepremethodid | 折旧方法 | int8 | 64 |  | √ | 0 | 折旧方法 fa_depremethod |
| 3 | fdepreeffect | 变动影响 | varchar | 50 |  | √ | ' ' | 变动影响,枚举: NEXT :影响下期 CUR :影响当期 |
| 4 | fassetcatid | 资产类别 | int8 | 64 |  | √ | 0 | 资产类别 fa_assetcategory |
| 5 | fuseyear | 预计使用年限/预计总工作量 | int8 | 64 |  | √ | 0 | 预计使用年限/预计总工作量 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fdeprelimit | 一次性折旧限额 | numeric | 19 | 6 | √ | 0.000000 | 一次性折旧限额 |
| 8 | fdepreconventionid | fdepreconventionid | int8 | 64 |  | √ | 0 |  |
| 9 | fdecpolicyid | 减值政策 | varchar | 50 |  | √ | ' ' | 减值政策,枚举: 1 :不减值 2 :减值，可转回（限额：累计减值） 4 :减值，可转回（限额：账面价值） 3 :减值，不可转回 |
| 10 | fdepretime | 计提时点 | varchar | 50 |  | √ | ' ' | 计提时点,枚举: CLEAR :次月 NEW :当月 NEXT_DAY :次日 NEW_AND_CLEAR :当日 NEXT_YEAR :次年 THIS_YEAR :当年 FIRST_YEAR_CONVEN :首年常规 |
| 11 | fdeprepolicyid | fdeprepolicyid | int8 | 64 |  | √ | 0 |  |
| 12 | fnetresidualvalrate | 净残值率(%) | numeric | 19 | 6 | √ | 0.000000 | 净残值率(%) |
| 13 | fnodepre | 不提折旧 | bpchar | 1 |  | √ | '0' | 不提折旧 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 15 | fisallowdeduction | fisallowdeduction | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_fa_depresystemapentry_pkey |  | fentryid |
| 2 | idx_fa_depresystemap_fid |  | fid |

---

## 资产政策-主表 t_fa_depresystem

- **表名称：** 资产政策-主表
- **表名：** t_fa_depresystem

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fexchangetableid | 汇率表（已弃用） | int8 | 64 |  | √ | 0 | 汇率表 bd_exratetable |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 7 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | fbizenable | fbizenable | bpchar | 1 |  | √ | '0' |  |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fctrlstrategy | 控制策略 | varchar | 10 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 11 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fbasecurrencyid | 主币别（已弃用） | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 13 | fperiodtypeid | 会计期间类型（已弃用） | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 17 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 18 | fenable | 使用状态 | varchar | 30 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编号 | varchar | 60 |  | √ | ' ' | 编号 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 21 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_fa_depresystem_createorg |  | fcreateorgid |
| 2 | idx_fa_depsys_fnumber |  | fnumber |
| 3 | t_fa_depresystem_pkey |  | fid |
| 4 | idx_t_fa_depresystem_master |  | fmasterid |
