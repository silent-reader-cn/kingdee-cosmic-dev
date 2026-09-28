# 货币面额设置-cas_currencyfacevalue

## 货币面额设置-多语言表 t_cas_currencyfacevalue_l

- **表名称：** 货币面额设置-多语言表
- **表名：** t_cas_currencyfacevalue_l

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
| 1 | t_cas_currencyfacevalue_l_pkey |  | fpkid |
| 2 | idx_cas_cfv_fidlocaleid |  | fid,flocaleid |

---

## 货币面额设置-主表 t_cas_currencyfacevalue

- **表名称：** 货币面额设置-主表
- **表名：** t_cas_currencyfacevalue

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fenableddenomination | 所有已启用面额 | varchar | 500 |  | √ | ' ' | 所有已启用面额 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fbaseunit | 基准单位 | varchar | 30 |  | √ | ' ' | 基准单位,枚举: 1 :元 2 :百元 3 :千元 4 :万元 5 :十万元 6 :百万元 7 :千万元 8 :亿元 9 :十亿元 |
| 7 | fispreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 13 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 14 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_currencyfacevalue_pkey |  | fid |
| 2 | idx_cas_ccyfv_fcurrencyid |  | fcurrencyid |

---

## 单据体-子表 t_cas_currencyfventry

- **表名称：** 单据体-子表
- **表名：** t_cas_currencyfventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdenomination | 面额 | varchar | 100 |  | √ | ' ' | 面额 |
| 3 | ffacevalue | 面值 | int8 | 64 |  | √ | 0 | 面值 |
| 4 | fusestatus | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态 |
| 5 | fconversionratio | 换算值 | numeric | 23 | 10 | √ | 0.0000000000 | 换算值 |
| 6 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | funit | 单位 | varchar | 30 |  | √ | ' ' | 单位 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_currencyfventry_pkey |  | fentryid |
| 2 | idx_cas_currencyfventry_fid |  | fid |
