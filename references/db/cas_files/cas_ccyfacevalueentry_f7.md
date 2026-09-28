# 面额分录F7-cas_ccyfacevalueentry_f7

## 面额分录F7-多语言表 t_cas_currencyfventry_l

- **表名称：** 面额分录F7-多语言表
- **表名：** t_cas_currencyfventry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |

---

## 面额分录F7-主表 t_cas_currencyfventry

- **表名称：** 面额分录F7-主表
- **表名：** t_cas_currencyfventry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdenomination | 面额 | varchar | 100 |  | √ | ' ' | 面额 |
| 3 | ffacevalue | ffacevalue | int8 | 64 |  | √ | 0 |  |
| 4 | fusestatus | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 5 | fconversionratio | 换算 | numeric | 23 | 10 | √ | 0.0000000000 | 换算 |
| 6 | fseq | fseq | int8 | 64 |  | √ | 0 |  |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | funit | 换算值（基准单位为元） | varchar | 30 |  | √ | ' ' | 换算值（基准单位为元） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_cas_currencyfventry_pkey |  | fentryid |
| 2 | idx_cas_currencyfventry_fid |  | fid |
