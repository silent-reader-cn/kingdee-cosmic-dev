# KPI-occbo_kpi_base

## 单据配置信息-子表 t_occbo_kpi_bi

- **表名称：** 单据配置信息-子表
- **表名：** t_occbo_kpi_bi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcountcol | 统计字段标识 | varchar | 100 |  | √ | ' ' | 统计字段标识 |
| 3 | ffilterscheme | 自定义过滤字段 | text | 0 |  |  | null | 自定义过滤字段 |
| 4 | fcountcolname | 统计字段名称 | varchar | 100 |  | √ | ' ' | 统计字段名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fchannelcol | 统计渠道字段标识 | varchar | 100 |  | √ | ' ' | 统计渠道字段标识 |
| 7 | fchannelcolname | 统计渠道字段名称 | varchar | 100 |  | √ | ' ' | 统计渠道字段名称 |
| 8 | fcreatetimecol | 统计时间字段标识 | varchar | 100 |  | √ | ' ' | 统计时间字段标识 |
| 9 | ffullusercol | 统计人员字段全标识 | varchar | 100 |  | √ | ' ' | 统计人员字段全标识 |
| 10 | forgtypecolname | 统计组织字段名称 | varchar | 100 |  | √ | ' ' | 统计组织字段名称 |
| 11 | fusercolname | 统计人员字段名称 | varchar | 100 |  | √ | ' ' | 统计人员字段名称 |
| 12 | ffullcountcol | 统计字段全标识 | varchar | 100 |  | √ | ' ' | 统计字段全标识 |
| 13 | ffullchannelcol | 统计渠道字段全标识 | varchar | 100 |  | √ | ' ' | 统计渠道字段全标识 |
| 14 | fformula | 计算公式 | bpchar | 1 |  | √ | 'A' | 计算公式,枚举: 0 :累加 1 :扣减 |
| 15 | forgtypecol | 统计组织字段标识 | varchar | 100 |  | √ | ' ' | 统计组织字段标识 |
| 16 | fbillid | 单据编码 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 17 | ffullcreatetimecol | 统计时间字段全标识 | varchar | 100 |  | √ | ' ' | 统计时间字段全标识 |
| 18 | fcreatetimecolname | 统计时间字段名称 | varchar | 100 |  | √ | ' ' | 统计时间字段名称 |
| 19 | ffullorgtypecol | 统计组织字段全标识 | varchar | 100 |  | √ | ' ' | 统计组织字段全标识 |
| 20 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 21 | fusercol | 统计人员字段标识 | varchar | 100 |  | √ | ' ' | 统计人员字段标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_occbo_kpibi_fid |  | fid |
| 2 | pk_occbo_kpi_bi |  | fentryid |

---

## KPI-主表 t_occbo_kpi

- **表名称：** KPI-主表
- **表名：** t_occbo_kpi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | KPI名称 | varchar | 80 |  | √ | ' ' | KPI名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcomment | 备注 | varchar | 255 |  | √ | ' ' | 备注 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | KPI编码 | varchar | 80 |  | √ | ' ' | KPI编码 |
| 12 | fissyspreset | 系统预置 | bpchar | 1 |  | √ | '0' | 系统预置 |
| 13 | fattribute | KPI属性 | bpchar | 1 |  |  | 'A' | KPI属性,枚举: A :渠道 B :人员 C :部门 |
| 14 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 15 | fdimension | KPI维度 | bpchar | 1 |  | √ | '0' | KPI维度,枚举: 0 :金额 1 :数量 2 :次数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_kpi |  | fid |
| 2 | idx_occbo_kpi_num |  | fnumber |

---

## KPI-多语言表 t_occbo_kpi_l

- **表名称：** KPI-多语言表
- **表名：** t_occbo_kpi_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | KPI名称 | varchar | 80 |  | √ | ' ' | KPI名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_occbo_kpi_l |  | fpkid |
| 2 | idx_occbo_kpi_l_flid |  | flocaleid |
