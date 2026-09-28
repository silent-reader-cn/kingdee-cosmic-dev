# 报表方案配置-fsa_rptscheme_config

## 用户数据权限-子表 t_fsa_scheme_pattern

- **表名称：** 用户数据权限-子表
- **表名：** t_fsa_scheme_pattern

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fdatasrc | 数据来源 | varchar | 30 |  | √ | ' ' | 数据来源,枚举: 0 :苍穹总账 1 :苍穹合并报表 9 :模拟数据 |
| 4 | fidxfactconfig | 指标配置内容 | varchar | 30 |  | √ | ' ' | 指标配置内容 |
| 5 | fauthcontent_tag | 权限内容_详情 | text | 0 |  |  | null | 权限内容_详情 |
| 6 | frpttype | 标准报表类型 | varchar | 30 |  | √ | ' ' | 标准报表类型 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fidxfactconfig_tag | 指标配置内容_详情 | text | 0 |  |  | null | 指标配置内容_详情 |
| 9 | ftablepattern | 数据集合 | int8 | 64 |  | √ | 0 | 标准报表 fsa_stdrpts |
| 10 | fauthcontent | 权限内容 | varchar | 30 |  | √ | ' ' | 权限内容 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_fsa_scheme_pattern |  | fentryid |
| 2 | fsa_idx_sch_pat |  | fid |

---

## 报表方案配置-多语言表 t_fsa_rptscheme_config_l

- **表名称：** 报表方案配置-多语言表
- **表名：** t_fsa_rptscheme_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_rptscheme_config_l |  | fid |
| 2 | pk_t_fsa_rptscheme_config_l |  | fpkid |

---

## 报表方案配置-主表 t_fsa_rptscheme_config

- **表名称：** 报表方案配置-主表
- **表名：** t_fsa_rptscheme_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fauthswitch | 是否启用数据权限 | bpchar | 1 |  | √ | ' ' | 是否启用数据权限 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fendperiodid | 过滤数据终止期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 10 | facctperiodtype | 期间类型 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 11 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 12 | flinetorowswitch | 是否启用列转行功能 | bpchar | 1 |  | √ | ' ' | 是否启用列转行功能 |
| 13 | fbeginperiodid | 过渡期间起始期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_fsa_scheme_config |  | fnumber |
| 2 | pk_t_fsa_rptscheme_config |  | fid |
