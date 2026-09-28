# 虚开发票数据推送日志-irew_false_check_log

## 发票-子表 t_irew_false_invoice

- **表名称：** 发票-子表
- **表名：** t_irew_false_invoice

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fserial_no | 发票流水号 | varchar | 100 |  | √ | ' ' | 发票流水号 |
| 3 | fcheckresult | 风险等级 | varchar | 30 |  | √ | ' ' | 风险等级,枚举: 0 :暂无风险 1 :低风险 2 :中风险 3 :高风险 4 :高危风险 |
| 4 | finvoice_code | 发票代码 | varchar | 50 |  | √ | ' ' | 发票代码 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | finvoice_no | 发票号码 | varchar | 50 |  | √ | ' ' | 发票号码 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_irew_false_invoice |  | fid |
| 2 | pk_t_irew_false_invoice |  | fentryid |

---

## 虚开发票数据推送日志-主表 t_irew_false_check_log

- **表名称：** 虚开发票数据推送日志-主表
- **表名：** t_irew_false_check_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | 状态 | varchar | 30 |  | √ | '0' | 状态,枚举: 0 :未推送 1 :已推送 2 :已查询 |
| 3 | fapplyid | aws结果批次号 | varchar | 100 |  | √ | ' ' | aws结果批次号 |
| 4 | fwarning_scheme_id | 方案id | varchar | 50 |  | √ | ' ' | 方案id |
| 5 | fnew_error_info | 最新错误信息 | varchar | 255 |  | √ | ' ' | 最新错误信息 |
| 6 | fcustomize_engine_id | 引擎id | varchar | 50 |  | √ | ' ' | 引擎id |
| 7 | finvoice_type | 发票类型 | varchar | 50 |  | √ | ' ' | 发票类型 |
| 8 | fverify_level | 方案预警等级 | varchar | 50 |  | √ | ' ' | 方案预警等级 |
| 9 | fcheck_level | 引擎校验等级 | varchar | 50 |  | √ | ' ' | 引擎校验等级 |
| 10 | fnext_date | 下次执行时间 | timestamp | 0 |  |  | null | 下次执行时间 |
| 11 | fcreate_date | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_irew_false_check_log |  | fid |
| 2 | idx_irew_false_check_log |  | fapplyid |
