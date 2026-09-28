# 业务取数规则-frm_recdatarule

## 取数规则-子表 t_ai_recdataruleentry

- **表名称：** 取数规则-子表
- **表名：** t_ai_recdataruleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdatafilter | 数据过滤条件 | varchar | 510 |  |  | ' ' | 数据过滤条件 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fdatafilterdesc | 过滤条件 | varchar | 2000 |  |  | ' ' | 过滤条件 |
| 5 | famount | 金额取值公式 | varchar | 2000 |  |  | ' ' | 金额取值公式 |
| 6 | ftasksize | 任务大小 | int4 | 32 |  | √ | 0 | 任务大小 |
| 7 | famountexp | 金额取值表达式 | varchar | 510 |  |  | ' ' | 金额取值表达式 |
| 8 | fbizflexsourcedesc | 业务维度来源 | varchar | 2000 |  | √ | ' ' | 业务维度来源 |
| 9 | fdatefielddesc | 业务日期 | varchar | 1000 |  | √ | ' ' | 业务日期 |
| 10 | fdisable | 禁用 | bpchar | 1 |  | √ | '0' | 禁用 |
| 11 | fbizflexsource | 业务维度来源（存储） | varchar | 510 |  | √ | ' ' | 业务维度来源（存储） |
| 12 | fdetailrule | 明细对账设置 | varchar | 36 |  | √ | ' ' | 明细对账设置,枚举: 1 :DAP关系 2 :凭证号 |
| 13 | fcommonfilter | 通用设置 | int8 | 64 |  | √ | 0 | 对账通用设置 frm_rec_common_filter |
| 14 | fbizflexsource_tag | 业务维度来源（存储）_详情 | text | 0 |  |  | ' ' | 业务维度来源（存储）_详情 |
| 15 | fbizobj | 来源对象 | varchar | 36 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 16 | fbizorgfieldin | 业务组织（存储） | varchar | 510 |  | √ | ' ' | 业务组织（存储） |
| 17 | fdescription | fdescription | varchar | 500 |  |  | ' ' |  |
| 18 | fdatafilter_tag | 数据过滤条件_详情 | text | 0 |  |  | ' ' | 数据过滤条件_详情 |
| 19 | fcurrencydesc | 币别 | varchar | 1000 |  | √ | ' ' | 币别 |
| 20 | fcurrencyin | 币别（存储） | varchar | 510 |  | √ | ' ' | 币别（存储） |
| 21 | fbizorgfielddesc | 业务组织 | varchar | 1000 |  | √ | ' ' | 业务组织 |
| 22 | famounttype | 对账类型 | int8 | 64 |  | √ | 0 | 对账类型 frm_amouttype_layout |
| 23 | famountexp_tag | 金额取值表达式_详情 | text | 0 |  |  | ' ' | 金额取值表达式_详情 |
| 24 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 25 | fdatatype | 业务数据类型 | varchar | 2 |  | √ | '0' | 业务数据类型,枚举: 0 :初始化 1 :期初余额 2 :增加项 3 :减少项 4 :期末余额 |
| 26 | fdatefieldin | 业务日期（存储） | varchar | 510 |  | √ | ' ' | 业务日期（存储） |

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

## 业务维度-多选基础资料表 t_ai_recdatarule_assist

- **表名称：** 业务维度-多选基础资料表
- **表名：** t_ai_recdatarule_assist

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | varchar | 36 |  | √ | '0' | 主实体对象 bos_entityobject |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

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
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 500 |  |  | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ai_recdataruleentry_l |  | fid,flocaleid |
| 2 | t_ai_recdataruleentry_l_pkey |  | fpkid |

---

## 业务取数规则-主表 t_ai_recdatarule

- **表名称：** 业务取数规则-主表
- **表名：** t_ai_recdatarule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 5 | fbizapp | 业务系统 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fuseorg | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 8 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 9 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fctrlstrategy | 控制策略 | varchar | 36 |  | √ | ' ' | 控制策略,枚举: 5 :全局共享 |
| 12 | fbatchmatch | 支持不同类型单据合并匹配凭证 | bpchar | 1 |  | √ | '0' | 支持不同类型单据合并匹配凭证 |
| 13 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fbizsourcetype | 业务来源类型 | bpchar | 1 |  | √ | '0' | 业务来源类型,枚举: 0 :业务单据 1 :业务报表 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fpreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 18 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 19 | fisbak | 是否备份 | bpchar | 1 |  | √ | '0' | 是否备份 |
| 20 | famounttype | famounttype | int8 | 64 |  | √ | 0 |  |
| 21 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 22 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 24 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

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
