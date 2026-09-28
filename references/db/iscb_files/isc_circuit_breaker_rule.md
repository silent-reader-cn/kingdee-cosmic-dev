# 熔断规则-isc_circuit_breaker_rule

## 熔断规则-主表 t_isc_breaker_rule

- **表名称：** 熔断规则-主表
- **表名：** t_isc_breaker_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmin_request_count | 最小请求数 | int4 | 32 |  | √ | 0 | 最小请求数 |
| 4 | fslow_percent | 慢响应比例 | int4 | 32 |  | √ | 0 | 慢响应比例 |
| 5 | ftype | 规则类型 | varchar | 50 |  | √ | ' ' | 规则类型,枚举: ERROR_RATIO :异常比例 SLOW_RATIO :慢响应比例 ERROR_COUNT :异常数 COMPOSITE :组合规则 |
| 6 | ferror_percent | 异常比例 | int4 | 32 |  | √ | 0 | 异常比例 |
| 7 | fsliding_window | 时间窗口（单位：秒） | int4 | 32 |  | √ | 0 | 时间窗口（单位：秒） |
| 8 | fmax_error_count | 最大异常数 | int4 | 32 |  | √ | 0 | 最大异常数 |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | fbreak_duration | 熔断持续时长（单位：秒） | int4 | 32 |  | √ | 0 | 熔断持续时长（单位：秒） |
| 11 | fslow_threshold | 慢请求阈值（单位：秒） | int4 | 32 |  | √ | 0 | 慢请求阈值（单位：秒） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_breaker_rule_num |  | fnumber |
| 2 | pk_t_isc_breaker_rule |  | fid |

---

## 熔断规则-多语言表 t_isc_breaker_rule_l

- **表名称：** 熔断规则-多语言表
- **表名：** t_isc_breaker_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_breaker_rule_l_0 |  | fid,flocaleid |
| 2 | pk_t_isc_breaker_rule_l |  | fpkid |

---

## 熔断规则分录-子表 t_isc_breaker_sub_rule

- **表名称：** 熔断规则分录-子表
- **表名：** t_isc_breaker_sub_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fsub_rule | 熔断规则 | int8 | 64 |  | √ | 0 | [熔断规则 isc_circuit_breaker_rule](../iscb_files/isc_circuit_breaker_rule.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_breaker_sub_rule_fk |  | fid |
| 2 | pk_t_isc_breaker_sub_rule |  | fentryid |
