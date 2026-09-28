# 业务取数规则-frm_recdatarule

## 取数规则-子表 t_ai_recdataruleentry

- **表名称：** 取数规则-子表
- **表名：** t_ai_recdataruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatafilter | 数据过滤条件 | varchar | 510 |  |  | ' ' | 数据过滤条件 |
| 3 | flocalamountdesc | 本位币金额 | varchar | 2000 |  | √ | ' ' | 本位币金额 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fdatafilterdesc | 过滤条件 | varchar | 2000 |  |  | ' ' | 过滤条件 |
| 6 | famount | 原币金额 | varchar | 2000 |  |  | ' ' | 原币金额 |
| 7 | ftasksize | 任务大小 | int4 | 32 |  | √ | 0 | 任务大小 |
| 8 | famountexp | 原币金额表达式 | varchar | 510 |  |  | ' ' | 原币金额表达式 |
| 9 | fbizflexsourcedesc | 业务维度来源 | varchar | 2000 |  | √ | ' ' | 业务维度来源 |
| 10 | fdatefielddesc | 业务日期 | varchar | 1000 |  | √ | ' ' | 业务日期 |
| 11 | fdisable | 禁用 | bpchar | 1 |  | √ | '0' | 禁用 |
| 12 | fbizflexsource | 业务维度来源（存储） | varchar | 510 |  | √ | ' ' | 业务维度来源（存储） |
| 13 | fdetailrule | 明细对账设置 | varchar | 36 |  | √ | ' ' | 明细对账设置,枚举: 1 :DAP关系 2 :凭证号 |
| 14 | fcommonfilter | 通用设置 | int8 | 64 |  | √ | 0 | [对账通用设置 frm_rec_common_filter](../frm_files/frm_rec_common_filter.md) |
| 15 | fbizflexsource_tag | 业务维度来源（存储）_详情 | text | 0 |  |  | ' ' | 业务维度来源（存储）_详情 |
| 16 | fbizobj | 来源对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | fbizorgfieldin | 业务组织（存储） | varchar | 510 |  | √ | ' ' | 业务组织（存储） |
| 18 | flocalamount | 本位币金额表达式 | varchar | 1000 |  | √ | ' ' | 本位币金额表达式 |
| 19 | fdescription | fdescription | varchar | 500 |  |  | ' ' |  |
| 20 | fdatafilter_tag | 数据过滤条件_详情 | text | 0 |  |  | ' ' | 数据过滤条件_详情 |
| 21 | fcurrencydesc | 币种 | varchar | 1000 |  | √ | ' ' | 币种 |
| 22 | fcurrencyin | 币种（存储） | varchar | 510 |  | √ | ' ' | 币种（存储） |
| 23 | fbizorgfielddesc | 业务组织 | varchar | 1000 |  | √ | ' ' | 业务组织 |
| 24 | famounttype | 对账类型 | int8 | 64 |  | √ | 0 | [对账类型 frm_amouttype_layout](../frm_files/frm_amouttype_layout.md) |
| 25 | famountexp_tag | 原币金额表达式_详情 | text | 0 |  |  | ' ' | 原币金额表达式_详情 |
| 26 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 27 | fdatatype | 业务数据类型 | varchar | 2 |  | √ | '0' | 业务数据类型,枚举: 0 :初始化 1 :期初余额 2 :增加项 3 :减少项 4 :期末余额 |
| 28 | fdatefieldin | 业务日期（存储） | varchar | 510 |  | √ | ' ' | 业务日期（存储） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_recdataruleentry |  | fid |
| 2 | t_ai_recdataruleentry_pkey |  | fentryid |

---

## 业务取数规则-多语言表 t_ai_recdatarule_l

- **表名称：** 业务取数规则-多语言表
- **表名：** t_ai_recdatarule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_recdatarule_l_pkey |  | fpkid |
| 2 | idx_ai_recdatarule_l |  | fid,flocaleid |

---

## 业务取数规则-使用范围位图表 t_ai_recdatarule_m

- **表名称：** 业务取数规则-使用范围位图表
- **表名：** t_ai_recdatarule_m

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
| 1 | pk_t_ai_recdatarule_m |  | forgid |

---

## 业务取数规则-使用范围表 t_ai_recdatarule_u

- **表名称：** 业务取数规则-使用范围表
- **表名：** t_ai_recdatarule_u

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
| 1 | t_ai_recdatarule_u_pkey |  | fdataid,fuseorgid |
| 2 | idx_t_ai_recdatarule_u_uo |  | fuseorgid |

---

## 对账维度-子表 t_ai_recdatarule_assist

- **表名称：** 对账维度-子表
- **表名：** t_ai_recdatarule_assist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | 来源标识 | varchar | 36 |  | √ | '0' | 来源标识 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 1 | 分录行号 |
| 4 | fpkid | fpkid | int8 | 64 |  | √ | 0 | id |
| 5 | fdatatype | 维度类型 | bpchar | 1 |  | √ | '1' | 维度类型,枚举: 1 :基础资料 2 :辅助资料 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_recdatarule_assist |  | fid |
| 2 | t_ai_recdatarule_assist_pkey |  | fpkid |

---

## 取数规则-多语言表 t_ai_recdataruleentry_l

- **表名称：** 取数规则-多语言表
- **表名：** t_ai_recdataruleentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | famountdescmulilang | 原币金额多语言 | varchar | 510 |  | √ | ' ' | 原币金额多语言 |
| 3 | flocalamountdescmulilang | 本位币金额多语言 | varchar | 510 |  | √ | ' ' | 本位币金额多语言 |
| 4 | fdatemulilang | 业务日期多语言 | varchar | 255 |  | √ | ' ' | 业务日期多语言 |
| 5 | fbizorgmulilang | 业务组织多语言 | varchar | 255 |  | √ | ' ' | 业务组织多语言 |
| 6 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 7 | fdescription | 描述 | varchar | 1020 |  |  | ' ' | 描述 |
| 8 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |
| 10 | fcurrencymulilang | 币种多语言 | varchar | 255 |  | √ | ' ' | 币种多语言 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_recdataruleentry_l_pkey |  | fpkid |
| 2 | idx_ai_recdataruleentry_l |  | fid,flocaleid |

---

## 业务取数规则-主表 t_ai_recdatarule

- **表名称：** 业务取数规则-主表
- **表名：** t_ai_recdatarule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmulcurrencytype | 对账币种 | varchar | 50 |  | √ | ',0,' | 对账币种,枚举: 0 :原币 1 :本位币 |
| 3 | fuseorg | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 4 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fbatchmatch | 支持不同类型单据合并匹配凭证 | bpchar | 1 |  | √ | '0' | 支持不同类型单据合并匹配凭证 |
| 8 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fpreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 12 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 13 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 14 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 15 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 17 | fbizapp | 业务系统 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | fquerylocalcurrency | 支持本位币对账（废弃） | bpchar | 1 |  | √ | '0' | 支持本位币对账（废弃） |
| 20 | fctrlstrategy | 控制策略 | varchar | 36 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 21 | fbizsourcetype | 业务来源类型 | bpchar | 1 |  | √ | '0' | 业务来源类型,枚举: 0 :业务单据 1 :业务报表 |
| 22 | fisbak | 是否备份 | bpchar | 1 |  | √ | '0' | 是否备份 |
| 23 | famounttype | famounttype | int8 | 64 |  | √ | 0 |  |
| 24 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 26 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_recdatarule_pkey |  | fid |
| 2 | idx_t_ai_recdatarule_createorg |  | fcreateorgid |
| 3 | idx_t_ai_recdatarule |  | fcreateorgid,fbizapp |
| 4 | idx_t_ai_recdatarule_master |  | fmasterid |
