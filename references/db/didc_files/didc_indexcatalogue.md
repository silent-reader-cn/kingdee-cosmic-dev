# 数智指标-didc_indexcatalogue

## 参考指标-子表 t_didc_referentry

- **表名称：** 参考指标-子表
- **表名：** t_didc_referentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcomputeformuladata | 统计方法 | varchar | 2000 |  | √ | ' ' | 统计方法 |
| 3 | freferthoubitapart | 参考指标千位分隔符 | bpchar | 1 |  | √ | ' ' | 参考指标千位分隔符 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcomputeformula | 计算公式 | varchar | 255 |  | √ | ' ' | 计算公式 |
| 6 | frefersuffix | 参考指标后缀 | varchar | 255 |  | √ | ' ' | 参考指标后缀 |
| 7 | freferindexid | 参考指标id | varchar | 50 |  | √ | ' ' | 参考指标id |
| 8 | findexsource | 取值来源 | varchar | 255 |  | √ | ' ' | 取值来源 |
| 9 | freferdecimal | 参考指标小数位数 | int8 | 64 |  | √ | 0 | 参考指标小数位数 |
| 10 | findexexpression | 显示格式 | varchar | 255 |  | √ | ' ' | 显示格式 |
| 11 | frelation | 关系 | varchar | 255 |  | √ | ' ' | 关系,枚举: numerator :分子 denominator :分母 |
| 12 | findexname | 参考指标名称 | varchar | 255 |  | √ | ' ' | 参考指标名称 |
| 13 | freferunit | 参考指标显示单位 | varchar | 255 |  | √ | ' ' | 参考指标显示单位,枚举: none :--无-- percentage :百分比（%） thousands :千 tenthousands :万 millions :百分 auto :自动 |
| 14 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_referentry |  | fid |
| 2 | pk_didc_referentry |  | fentryid |

---

## 子单据体-子表 t_didc_inputdatasubentry

- **表名称：** 子单据体-子表
- **表名：** t_didc_inputdatasubentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fnum | 数值 | numeric | 23 | 10 | √ | 0 | 数值 |
| 2 | fdenominator | 分母 | numeric | 23 | 10 | √ | 0 | 分母 |
| 3 | fformatstyle | 显示格式 | varchar | 255 |  | √ | ' ' | 显示格式 |
| 4 | fmonth | 月份 | varchar | 255 |  | √ | ' ' | 月份 |
| 5 | fmonthdate | 月份日期 | timestamp | 0 |  |  | null | 月份日期 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fnumerator | 分子 | numeric | 23 | 10 | √ | 0 | 分子 |
| 8 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_didc_inputdatasubentry |  | fdetailid |
| 2 | idx_didc_inputdatasubentry |  | fentryid |

---

## 维度设置-多语言表 t_didc_dimensionsetentry_l

- **表名称：** 维度设置-多语言表
- **表名：** t_didc_dimensionsetentry_l

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
| 1 | pk_didc_dimensionsetentry_l |  | fpkid |
| 2 | idx_didc_dimensionsetentry_l |  | fentryid,flocaleid |

---

## 参考指标-多语言表 t_didc_referentry_l

- **表名称：** 参考指标-多语言表
- **表名：** t_didc_referentry_l

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
| 1 | pk_didc_referentry_l |  | fpkid |
| 2 | idx_didc_referentry_l |  | fentryid,flocaleid |

---

## 责任对象数据集-子表 t_didc_responsibility

- **表名称：** 责任对象数据集-子表
- **表名：** t_didc_responsibility

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fisview | 工作台可见 | bpchar | 1 |  | √ | ' ' | 工作台可见 |
| 3 | fusername | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fisresponsibilitytype | 主要责任人 | bpchar | 1 |  | √ | ' ' | 主要责任人 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fusernumber | 工号 | varchar | 50 |  | √ | ' ' | 工号 |
| 7 | fuserid | 用户ID | varchar | 50 |  | √ | ' ' | 用户ID |
| 8 | fusertype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: bos_usergroup_user :用户 perm_role :角色 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_responsibility |  | fid |
| 2 | pk_t_didc_responsibility |  | fentryid |

---

## 输入数据单据体-子表 t_didc_inputdataentry

- **表名称：** 输入数据单据体-子表
- **表名：** t_didc_inputdataentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fyeardate | 年度 | timestamp | 0 |  |  | null | 年度 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_inputdataentry |  | fid |
| 2 | pk_t_didc_inputdataentry |  | fentryid |

---

## 数智指标-多语言表 t_didc_indexcatalogue_l

- **表名称：** 数智指标-多语言表
- **表名：** t_didc_indexcatalogue_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 指标名称 | varchar | 255 |  | √ | ' ' | 指标名称 |
| 3 | fmanagepurpose | 指标管理目的 | varchar | 255 |  | √ | ' ' | 指标管理目的 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 指标定义 | varchar | 255 |  | √ | ' ' | 指标定义 |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_didc_indexcatalogue_l |  | fpkid |
| 2 | idx_didc_indexcatalogue_l |  | fid,flocaleid |

---

## 指标标签-多选基础资料表 t_didc_indexlabel_d

- **表名称：** 指标标签-多选基础资料表
- **表名：** t_didc_indexlabel_d

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 指标标签 didc_indexlabel |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_didc_indexlabel_d |  | fid,fbasedataid |
| 2 | pk_t_didc_indexlabel_d |  | fpkid |

---

## 数智指标-主表 t_didc_indexcatalogue

- **表名称：** 数智指标-主表
- **表名：** t_didc_indexcatalogue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fgroupid | 指标分类 | int8 | 64 |  | √ | 0 | 指标分类 didc_indexgroup |
| 3 | findexenum | 指标枚举项 | varchar | 255 |  | √ | ' ' | 指标枚举项 |
| 4 | fmodelid | 模型id | varchar | 50 |  | √ | ' ' | 模型id |
| 5 | findexid | 指标id | varchar | 50 |  | √ | ' ' | 指标id |
| 6 | fsource | 取值来源 | varchar | 255 |  | √ | ' ' | 取值来源 |
| 7 | fresponsibilitylist | 主要责任人 | varchar | 255 |  | √ | ' ' | 主要责任人 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改时间 |
| 9 | fdecimal | 小数位数 | int8 | 64 |  | √ | 0 | 小数位数 |
| 10 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsourcetype | 取值来源类型 | varchar | 50 |  | √ | ' ' | 取值来源类型,枚举: 1 :轻建模 2 :离线数据源 3 :手工输入 4 :单据 |
| 14 | ftargetvalue | 目标配置项 | varchar | 255 |  | √ | ' ' | 目标配置项 |
| 15 | fissyspreset | 系统预设 | bpchar | 1 |  | √ | ' ' | 系统预设 |
| 16 | fname | 指标名称 | varchar | 255 |  | √ | ' ' | 指标名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 18 | fresponsibilitydept | 责任部门 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 19 | fexpression | 显示格式 | varchar | 255 |  | √ | ' ' | 显示格式 |
| 20 | findexenum_tag | 指标枚举项_详情 | text | 0 |  |  | null | 指标枚举项_详情 |
| 21 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 22 | fcomputewaydata | 统计方式 | varchar | 2000 |  | √ | ' ' | 统计方式 |
| 23 | findextendency | 指标趋势 | varchar | 50 |  | √ | ' ' | 指标趋势,枚举: high :越高越好 low :越低越好 |
| 24 | fdescription | 指标定义 | varchar | 255 |  | √ | ' ' | 指标定义 |
| 25 | ffiltervalue | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 26 | fdatefield | 默认时间维度 | varchar | 50 |  | √ | ' ' | 默认时间维度,枚举: |
| 27 | fsuffix | 后缀 | varchar | 50 |  | √ | ' ' | 后缀 |
| 28 | fisthoubitapart | 千位分隔符 | bpchar | 1 |  | √ | ' ' | 千位分隔符 |
| 29 | ffiltervalue_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 30 | fmanagepurpose | 指标管理目的 | varchar | 255 |  | √ | ' ' | 指标管理目的 |
| 31 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 32 | ffilterschema | 过滤方案 | varchar | 50 |  | √ | ' ' | 过滤方案,枚举: |
| 33 | fnumber | 指标编码 | varchar | 30 |  | √ | ' ' | 指标编码 |
| 34 | fcomputeway | 计算公式 | varchar | 2000 |  | √ | ' ' | 计算公式 |
| 35 | ftargetvalue_tag | 目标配置项_详情 | text | 0 |  |  | null | 目标配置项_详情 |
| 36 | funit | 显示单位 | varchar | 50 |  | √ | ' ' | 显示单位,枚举: none :--无-- percentage :百分比（%） thousands :千 tenthousands :万 millions :百万 auto :自动 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_didc_indexcatalogue |  | fid |
| 2 | idx_didc_indexcatalogue |  | fnumber |

---

## 维度设置-子表 t_didc_dimensionsetentry

- **表名称：** 维度设置-子表
- **表名：** t_didc_dimensionsetentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensionfield | 维度字段 | varchar | 255 |  | √ | ' ' | 维度字段 |
| 3 | ffiltertype | 过滤控件类型 | varchar | 50 |  | √ | ' ' | 过滤控件类型,枚举: multiple :多选下拉 single :单选下拉 base :基础资料 enumvalue :枚举 |
| 4 | fdimensiontype | 维度类型 | varchar | 50 |  | √ | ' ' | 维度类型,枚举: DATE :周期 ACQUIESCE :普通 |
| 5 | fdimensionname | 显示名称 | varchar | 255 |  | √ | ' ' | 显示名称 |
| 6 | ffiltersourcevalue | 过滤值内容 | varchar | 255 |  | √ | ' ' | 过滤值内容 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | ffiltersource | 过滤值来源 | varchar | 255 |  | √ | ' ' | 过滤值来源 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | facquiesce | 默认时间维度 | bpchar | 1 |  | √ | ' ' | 默认时间维度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_didc_dimensionsetentry |  | fentryid |
| 2 | idx_didc_dimensionsetentry |  | fid |
