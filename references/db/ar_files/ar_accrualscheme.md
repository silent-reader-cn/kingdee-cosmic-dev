# 计提方案-ar_accrualscheme

## 来源类型-多选基础资料表 t_ar_mulbdfactor2

- **表名称：** 来源类型-多选基础资料表
- **表名：** t_ar_mulbdfactor2

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 来源类型 ar_sourcetype |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_mulbdfactor2_pkey |  | fpkid |
| 2 | idx_ar_mulbdfactor2_fentry |  | fentryid |

---

## 单据体-子表 t_ar_accrualschemeentry

- **表名称：** 单据体-子表
- **表名：** t_ar_accrualschemeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | faccrualrate | 计提比率(%) | numeric | 19 | 6 | √ | 0.000000 | 计提比率(%) |
| 3 | ffiltertext | ffiltertext | varchar | 2000 |  | √ | ' ' |  |
| 4 | fdays | 起始天数 | int8 | 64 |  | √ | 0 | 起始天数 |
| 5 | frange | 区间 | varchar | 30 |  | √ | ' ' | 区间 |
| 6 | fisabove | 天以上 | bpchar | 1 |  | √ | ' ' | 天以上 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fenddays | 截止天数 | int8 | 64 |  | √ | 0 | 截止天数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_accrualschemeentry_pkey |  | fentryid |
| 2 | idx_ar_asentry_fid |  | fid |

---

## 多选基础资料-多选基础资料表 t_ar_mulbdfactor0

- **表名称：** 多选基础资料-多选基础资料表
- **表名：** t_ar_mulbdfactor0

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_mulbdfactor0_fentry |  | fentryid |
| 2 | t_ar_mulbdfactor0_pkey |  | fpkid |

---

## 多选基础资料-多选基础资料表 t_ar_mulbdfactor1

- **表名称：** 多选基础资料-多选基础资料表
- **表名：** t_ar_mulbdfactor1

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 币种 bd_currency |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_mulbdfactor1_pkey |  | fpkid |
| 2 | idx_ar_mulbdfactor1_fentry |  | fentryid |

---

## 字段映射-子表 t_ar_fieldmapentry

- **表名称：** 字段映射-子表
- **表名：** t_ar_fieldmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffieldname | 字段名称 | varchar | 30 |  | √ | ' ' | 字段名称 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentityid | 实体类型 | varchar | 30 |  | √ | ' ' | 实体类型 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fdatatype | 数据类型 | varchar | 30 |  | √ | ' ' | 数据类型 |
| 7 | ffieldkey | 字段标识 | varchar | 30 |  | √ | ' ' | 字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_fieldmapentry_pkey |  | fentryid |
| 2 | idx_ar_fieldmapentry_fid |  | fid |

---

## 计提方案-多语言表 t_ar_accrualscheme_l

- **表名称：** 计提方案-多语言表
- **表名：** t_ar_accrualscheme_l

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
| 1 | t_ar_accrualscheme_l_pkey |  | fpkid |
| 2 | idx_ar_asl_fid |  | fid,flocaleid |

---

## 计提方案-主表 t_ar_accrualscheme

- **表名称：** 计提方案-主表
- **表名：** t_ar_accrualscheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | faccrualfrequency | 计提频率 | varchar | 30 |  | √ | ' ' | 计提频率,枚举: month :月 season :季 year :年 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 5 | faccrualfactordesc | faccrualfactordesc | varchar | 255 |  | √ | ' ' |  |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fisspread | 是否展开 | bpchar | 1 |  | √ | ' ' | 是否展开 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 5 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | faccrualmethod | 计提方法 | varchar | 30 |  | √ | ' ' | 计提方法,枚举: balancePct :余额百分比法 acctAgeAnalysis :账龄分析法 salesPct :销货百分比法 |
| 11 | faccrualfactor | 计提因素 | varchar | 255 |  | √ | ' ' | 计提因素 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 使用状态 | varchar | 5 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ar_as_fnumber |  | fnumber |
| 2 | t_ar_accrualscheme_pkey |  | fid |

---

## 政策分录-子表 t_ar_aspolicyentry

- **表名称：** 政策分录-子表
- **表名：** t_ar_aspolicyentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fpolicyid | 应收政策 | int8 | 64 |  | √ | 0 | 应收政策 ar_policy |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ar_aspolicyentry_pkey |  | fentryid |
| 2 | idx_ar_policyentry_fid |  | fid |
