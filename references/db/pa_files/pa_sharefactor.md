# 分摊因子-pa_sharefactor

## 因子值维护分录-子表 t_pa_sharefactorentry

- **表名称：** 因子值维护分录-子表
- **表名：** t_pa_sharefactorentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fvalue_ids | 维度成员ids字符串 | varchar | 255 |  |  | null | 维度成员ids字符串 |
| 3 | fvalue | 值 | numeric | 23 | 10 | √ | 0.00 | 值 |
| 4 | fdimensionjson | 维度json | varchar | 255 |  |  | null | 维度json |
| 5 | fdimensionjson_tag | 维度json_详情 | text | 0 |  |  | null | 维度json_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fvalue_ids_tag | 维度成员ids字符串_详情 | text | 0 |  |  | null | 维度成员ids字符串_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_share_factor_entry_1 |  | fid |
| 2 | pk_t_pa_sharefactorentry |  | fentryid |

---

## 分摊因子-主表 t_pa_sharefactor

- **表名称：** 分摊因子-主表
- **表名：** t_pa_sharefactor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescribe | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 6 | funitfield | 计量单位 | int8 | 64 |  | √ | 0 | 计量单位 bd_measureunits |
| 7 | fanalysis_system | 分析体系 | int8 | 64 |  | √ | 0 | 分析体系 pa_anasystemsetting |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | ffactortype | 类型 | bpchar | 1 |  | √ | '0' | 类型,枚举: 0 :期间 1 :固定 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fanalysis_model | 分析模型 | int8 | 64 |  | √ | 0 | 分析模型 pa_analysismodel |
| 14 | fenable | 启用状态 | bpchar | 1 |  | √ | '0' | 启用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_share_factor_1 |  | fanalysis_system,fanalysis_model |
| 2 | pk_t_pa_sharefactor |  | fid |

---

## 分摊因子-多语言表 t_pa_sharefactor_l

- **表名称：** 分摊因子-多语言表
- **表名：** t_pa_sharefactor_l

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
| 1 | pk_t_pa_sharefactor_l |  | fpkid |
| 2 | idx_pa_share_factor_l_1 |  | fid,flocaleid |

---

## 维度-多选基础资料表 t_pa_sharefactordim

- **表名称：** 维度-多选基础资料表
- **表名：** t_pa_sharefactordim

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 维度 pa_dimension |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_sharefactordim |  | fpkid |
| 2 | idx_pa_share_factor_dim_1 |  | fid |
