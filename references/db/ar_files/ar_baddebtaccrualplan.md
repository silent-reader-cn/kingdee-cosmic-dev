# 计提方案（废弃）-ar_baddebtaccrualplan

## 计提方案（废弃）-主表 t_ar_baddebtaccrualplan

- **表名称：** 计提方案（废弃）-主表
- **表名：** t_ar_baddebtaccrualplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | 创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | faccrualfrequency | 计提频率 | varchar | 30 |  | √ | ' ' | 计提频率,枚举: month :月 quarter :季 semiannual :半年 year :年 |
| 4 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 5 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 8 | foffset | foffset | varchar | 30 |  | √ | ' ' |  |
| 9 | faccrualagingid | 计提账龄分组 | int8 | 64 |  | √ | 0 | [应收账龄分组设置 ar_accrualaging](../ar_files/ar_accrualaging.md) |
| 10 | fsrccreateorgid | 原创建组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fctrlstrategy | 控制策略 | bpchar | 1 |  | √ | ' ' | 控制策略,枚举: 2 :分配/局部共享 5 :全局共享 7 :私有 |
| 13 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | faccrualmethod | 计提方法 | varchar | 30 |  | √ | ' ' | 计提方法,枚举: 1 :账龄分析法 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 17 | fsourcedataid | 原资料id | int8 | 64 |  | √ | 0 | 原资料id |
| 18 | fbitindex | 位图 | int4 | 32 |  | √ | 0 | 位图 |
| 19 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 20 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 21 | fsourcebitindex | 原资料位图 | int4 | 32 |  | √ | 0 | 原资料位图 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_accplan_fnumber |  | fnumber |
| 2 | idx_t_ar_baddebtaccrualplan_createorg |  | fcreateorgid |
| 3 | pk_t_ar_baddebtaccrualplan |  | fid |
| 4 | idx_t_ar_baddebtaccrualplan_master |  | fmasterid |

---

## 卡片单据体-子表 t_ar_accrualplanentry

- **表名称：** 卡片单据体-子表
- **表名：** t_ar_accrualplanentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname |  | varchar | 50 |  | √ | ' ' |  |
| 3 | fcondition_tag | 计提条件_详情 | text | 0 |  |  | null | 计提条件_详情 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | foffset | 抵消规则 | varchar | 255 |  | √ | ' ' | 抵消规则 |
| 6 | faccrualentityobjid | 计提对象 | int8 | 64 |  | √ | 0 | [计提对象 ar_accrualentityobj](../ar_files/ar_accrualentityobj.md) |
| 7 | faccrualrate | 计提比率 | varchar | 255 |  | √ | ' ' | 计提比率 |
| 8 | faccrualrate_tag | 计提比率_详情 | text | 0 |  |  | null | 计提比率_详情 |
| 9 | fagingstartdatefield | 账龄起算日 | varchar | 30 |  | √ | ' ' | 账龄起算日 |
| 10 | fcondition | 计提条件 | varchar | 255 |  | √ | ' ' | 计提条件 |
| 11 | fnumber |  | varchar | 255 |  | √ | ' ' |  |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | foffset_tag | 抵消规则_详情 | text | 0 |  |  | null | 抵消规则_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_accplanentry_fid |  | fid |
| 2 | pk_t_ar_accrualplanentry |  | fentryid |
| 3 | idx_ar_accplanentry_entity |  | faccrualentityobjid |

---

## 计提方案（废弃）-使用范围表 t_ar_baddebtaccrualplan_u

- **表名称：** 计提方案（废弃）-使用范围表
- **表名：** t_ar_baddebtaccrualplan_u

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
| 1 | pk_t_ar_baddebtaccrualplan_u |  | fdataid,fuseorgid |
| 2 | idx_t_ar_baddebtaccrualplan_u_uo |  | fuseorgid |

---

## 计提方案（废弃）-使用范围位图表 t_ar_baddebtaccrualplan_m

- **表名称：** 计提方案（废弃）-使用范围位图表
- **表名：** t_ar_baddebtaccrualplan_m

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
| 1 | pk_t_ar_baddebtaccrualplan_m |  | forgid |

---

## 计提方案（废弃）-多语言表 t_ar_baddebtaccrualplan_l

- **表名称：** 计提方案（废弃）-多语言表
- **表名：** t_ar_baddebtaccrualplan_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ar_baddebtaccrualplan_l |  | fpkid |
| 2 | idx_ar_accrualplanl_fid |  | fid,flocaleid |

---

## 曾用名列表-子表 t_ar_baddebtaccrualplannh

- **表名称：** 曾用名列表-子表
- **表名：** t_ar_baddebtaccrualplannh

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fenddate | 失效日期 | timestamp | 0 |  |  | null | 失效日期 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  |  | null | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fstartdate | 生效日期 | timestamp | 0 |  |  | null | 生效日期 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fenable | 是否生效 | bpchar | 1 |  | √ | '1' | 是否生效 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | null | id |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ar_baddebtaccrualplannh |  | fentryid |
| 2 | idx_ar_baddebtaccrualplannh_fk |  | fid |

---

## 曾用名列表-多语言表 t_ar_baddebtaccrualplannh_l

- **表名称：** 曾用名列表-多语言表
- **表名：** t_ar_baddebtaccrualplannh_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | '' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | null | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_ar_baddebtaccrualplannh_l |  | fpkid |
| 2 | idx_ar_baddebtaccrualplannh_l_0 |  | fentryid,flocaleid |
