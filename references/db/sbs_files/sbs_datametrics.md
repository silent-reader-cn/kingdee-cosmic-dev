# 数据指标-sbs_datametrics

## 数据指标-主表 t_sbs_datametrics

- **表名称：** 数据指标-主表
- **表名：** t_sbs_datametrics

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 指标分类 | int8 | 64 |  | √ | 0 | [指标分类分组 sbs_metricsgroup](../sbs_files/sbs_metricsgroup.md) |
| 3 | fforchatbi | 问数 | bpchar | 1 |  | √ | '0' | 问数 |
| 4 | fmodelid | 模型id | varchar | 50 |  | √ | ' ' | 模型id |
| 5 | fmetricsvaluetype | 指标值字段类型 | varchar | 50 |  | √ | ' ' | 指标值字段类型,枚举: num :数值 date :日期 int :整型 text :文本 |
| 6 | fformuladata | 计算公式（支持加减乘除） | varchar | 255 |  | √ | ' ' | 计算公式（支持加减乘除） |
| 7 | fsource | 取值来源 | varchar | 255 |  | √ | ' ' | 取值来源 |
| 8 | fformuladata_tag | 计算公式（支持加减乘除）_详情 | text | 0 |  |  | null | 计算公式（支持加减乘除）_详情 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fdecimal | 小数位数 | int4 | 32 |  | √ | 0 | 小数位数 |
| 11 | fappid | 所属应用 | varchar | 50 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 12 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fdatametricsid | 目标值对应的数据指标 | int8 | 64 |  | √ | 0 | [数据指标 sbs_datametrics](../sbs_files/sbs_datametrics.md) |
| 16 | fsourcetype | 取值来源类型 | varchar | 50 |  | √ | ' ' | 取值来源类型,枚举: 4 :单据 5 :自定义数据来源 |
| 17 | ffilterdata_tag | 数据过滤范围_详情 | text | 0 |  |  | null | 数据过滤范围_详情 |
| 18 | forgrange | 默认范围 | varchar | 50 |  | √ | ' ' | 默认范围,枚举: all :全部组织 current :登录组织 |
| 19 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 20 | ffilterdata | 数据过滤范围 | varchar | 255 |  | √ | ' ' | 数据过滤范围 |
| 21 | fresulttablename | 指标结果表名 | varchar | 50 |  | √ | ' ' | 指标结果表名 |
| 22 | fexceplan | fexceplan | varchar | 255 |  | √ | ' ' |  |
| 23 | freffirst | 先汇总参考指标 | bpchar | 1 |  | √ | ' ' | 先汇总参考指标 |
| 24 | fname | 指标名称 | varchar | 255 |  | √ | ' ' | 指标名称 |
| 25 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 26 | fexpression | 显示格式 | varchar | 255 |  | √ | ' ' | 显示格式 |
| 27 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 28 | fcomputewaydata | 统计方式 | varchar | 50 |  | √ | ' ' | 统计方式,枚举: SUM :求和 MAX :最大值 MIN :最小值 AVG :平均值 COUNT :计数 COUNTD :不重复计数 MAXDATERECORD :最大日期记录 MINDATERECORD :最小日期记录 |
| 29 | fdatascope | 数据范围 | varchar | 255 |  | √ | ' ' | 数据范围 |
| 30 | fsupportfixed | 支持物化 | bpchar | 1 |  | √ | ' ' | 支持物化 |
| 31 | fmetricsdatatype | 指标类型 | varchar | 50 |  | √ | ' ' | 指标类型,枚举: normal :普通 target :目标值 |
| 32 | findextendency | 业务相关性 | varchar | 50 |  | √ | ' ' | 业务相关性,枚举: high :正相关 low :负相关 |
| 33 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 34 | fdescription | 指标定义 | varchar | 255 |  | √ | ' ' | 指标定义 |
| 35 | fdatefield | 默认时间维度 | varchar | 50 |  | √ | ' ' | 默认时间维度,枚举: |
| 36 | fcustdatasourceid | 自定义数据来源 | int8 | 64 |  | √ | 0 | [自定义数据来源 sbs_custdatasource](../sbs_files/sbs_custdatasource.md) |
| 37 | fsuffix | 后缀 | varchar | 50 |  | √ | ' ' | 后缀 |
| 38 | fisthoubitapart | 千位分隔符 | bpchar | 1 |  | √ | ' ' | 千位分隔符 |
| 39 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 40 | ffilterschema | 过滤方案 | varchar | 50 |  | √ | ' ' | 过滤方案,枚举: |
| 41 | fnumber | 指标编码 | varchar | 50 |  | √ | ' ' | 指标编码 |
| 42 | fcomputeway | 计算公式 | varchar | 255 |  | √ | ' ' | 计算公式 |
| 43 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | funit | 显示单位 | varchar | 50 |  | √ | ' ' | 显示单位,枚举: none :--无-- percentage :百分比（%） thousands :千 tenthousands :万 millions :百万 auto :自动 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sbs_datametrics |  | fid |
| 2 | idx_sbs_datametrics_mid |  | fmodelid |

---

## 维度设置-多语言表 t_sbs_dimensionsetentry_l

- **表名称：** 维度设置-多语言表
- **表名：** t_sbs_dimensionsetentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fdimensionname | 显示名称 | varchar | 255 |  | √ | ' ' | 显示名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sbs_dimensionsetentry_l |  | fpkid |
| 2 | idx_sbs_dimentry_l |  | fentryid |

---

## 数据指标-多语言表 t_sbs_datametrics_l

- **表名称：** 数据指标-多语言表
- **表名：** t_sbs_datametrics_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 指标名称 | varchar | 255 |  | √ | ' ' | 指标名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 指标定义 | varchar | 1000 |  | √ | ' ' | 指标定义 |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_datametrics_l |  | fid |
| 2 | pk_sbs_datametrics_l |  | fpkid |

---

## 参考指标-子表 t_sbs_referentry

- **表名称：** 参考指标-子表
- **表名：** t_sbs_referentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomputeformuladata | 统计方式 | varchar | 50 |  | √ | ' ' | 统计方式,枚举: SUM :求和 MAX :最大值 MIN :最小值 AVG :平均值 COUNT :计数 COUNTD :不重复计数 |
| 3 | frefvaluetype | 参考指标值字段类型 | varchar | 50 |  | √ | ' ' | 参考指标值字段类型,枚举: num :数值 int :整型 date :日期 text :文本 |
| 4 | frefformuladata | 计算公式（支持加减乘除） | varchar | 100 |  | √ | ' ' | 计算公式（支持加减乘除） |
| 5 | freferthoubitapart | 参考指标千位分隔符 | bpchar | 1 |  | √ | ' ' | 参考指标千位分隔符 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcomputeformula | 计算公式 | varchar | 100 |  | √ | ' ' | 计算公式 |
| 8 | frefersuffix | 参考指标后缀 | varchar | 50 |  | √ | ' ' | 参考指标后缀 |
| 9 | freferindexid | 参考指标id | varchar | 50 |  | √ | ' ' | 参考指标id |
| 10 | findexsource | findexsource | varchar | 255 |  | √ | ' ' |  |
| 11 | freferdecimal | 参考指标小数位数 | int4 | 32 |  | √ | 0 | 参考指标小数位数 |
| 12 | frefdatakey | 指标标识 | varchar | 50 |  | √ | ' ' | 指标标识 |
| 13 | frefformuladata_tag | 计算公式（支持加减乘除）_详情 | text | 0 |  |  | null | 计算公式（支持加减乘除）_详情 |
| 14 | findexexpression | 显示格式 | varchar | 255 |  | √ | ' ' | 显示格式 |
| 15 | freffieldname | 参考指标结果字段名 | varchar | 50 |  | √ | ' ' | 参考指标结果字段名 |
| 16 | frelation | 关系 | varchar | 50 |  | √ | ' ' | 关系,枚举: numerator :分子 denominator :分母 |
| 17 | findexname | 参考指标名称 | varchar | 100 |  | √ | ' ' | 参考指标名称 |
| 18 | freferunit | 参考指标显示单位 | varchar | 50 |  | √ | ' ' | 参考指标显示单位,枚举: none :--无-- percentage :百分比（%） thousands :千 tenthousands :万 millions :百分 auto :自动 |
| 19 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_referentry |  | fid |
| 2 | pk_sbs_referentry |  | fentryid |

---

## 参考指标-多语言表 t_sbs_referentry_l

- **表名称：** 参考指标-多语言表
- **表名：** t_sbs_referentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 2 | findexname | 参考指标名称 | varchar | 255 |  | √ | ' ' | 参考指标名称 |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sbs_referentry_l |  | fpkid |
| 2 | idx_sbs_referentry_l |  | fentryid |

---

## 维度设置-子表 t_sbs_dimensionsetentry

- **表名称：** 维度设置-子表
- **表名：** t_sbs_dimensionsetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldvaltype | 字段值类型 | varchar | 50 |  | √ | ' ' | 字段值类型,枚举: num :数值 text :文本 date :日期 int :整型 |
| 3 | fdimensionfield | 维度字段 | varchar | 100 |  | √ | ' ' | 维度字段 |
| 4 | fdimfieldname | 结果表字段名 | varchar | 50 |  | √ | ' ' | 结果表字段名 |
| 5 | ffiltertype | 过滤控件类型 | varchar | 50 |  | √ | ' ' | 过滤控件类型,枚举: list :下拉列表 base :基础资料 text :文本 date :日期 num :数值 long :整型 |
| 6 | fdimensiontype | 维度类型 | varchar | 50 |  | √ | ' ' | 维度类型,枚举: DATE :周期 ACQUIESCE :普通 |
| 7 | fdimensionname | 显示名称 | varchar | 100 |  | √ | ' ' | 显示名称 |
| 8 | fbasedataentitykey | 对应基础资料 | varchar | 50 |  | √ | ' ' | [业务对象 bos_objecttype](../mdl_files/bos_objecttype.md) |
| 9 | fisorgdim | 默认组织 | bpchar | 1 |  | √ | '0' | 默认组织 |
| 10 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 11 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 12 | facquiesce | 默认时间维度 | varchar | 50 |  | √ | ' ' | 默认时间维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_sbs_dimensionsetentry |  | fentryid |
| 2 | idx_sbs_dimensionsetentry |  | fid |
