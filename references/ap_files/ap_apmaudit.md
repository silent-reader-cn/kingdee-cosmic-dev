# 性能统计-ap_apmaudit

## 性能统计-主表 t_ap_apmaudit

- **表名称：** 性能统计-主表
- **表名：** t_ap_apmaudit

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcosttime | 总耗时 | numeric | 23 | 10 | √ | 0.0000000000 | 总耗时 |
| 3 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 4 | fnumber | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 5 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ap_apmaudit |  | fid |
| 2 | idx_ap_apmaudit_number |  | fnumber |
| 3 | idx_ap_apmaudit_traceid |  | ftraceid |
| 4 | idx_ap_apmaudit_begintime |  | fbegintime |

---

## 分录-子表 t_ap_apmauditentry

- **表名称：** 分录-子表
- **表名：** t_ap_apmauditentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcosttime | 总耗时(ms) | numeric | 23 | 10 | √ | 0.0000000000 | 总耗时(ms) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 5 | fnumber | 编号 | varchar | 50 |  | √ | ' ' | 编号 |
| 6 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 7 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fpercentage | 占比（%） | numeric | 23 | 10 | √ | 0.0000000000 | 占比（%） |
| 10 | fbegintime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ap_apmentry_fid |  | fid |
| 2 | pk_t_ap_apmauditentry |  | fentryid |
| 3 | idx_ap_apmentry_pid |  | fparententryid |
