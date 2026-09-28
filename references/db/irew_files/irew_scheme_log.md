# 预警方案执行日志-irew_scheme_log

## 预警方案执行日志-主表 t_irew_scheme_log

- **表名称：** 预警方案执行日志-主表
- **表名：** t_irew_scheme_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwarning_scheme_name | 预警方案 | varchar | 50 |  | √ | ' ' | 预警方案 |
| 3 | fwarning_scheme | 预警方案id | int8 | 64 |  | √ | 0 | 预警方案id |
| 4 | faudit_end_date | 审计范围.结束 | timestamp | 0 |  |  | null | 审计范围.结束 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 7 | foperate_type | 操作类型 | varchar | 2 |  | √ | ' ' | 操作类型,枚举: 0 :手动审计 1 :自动审计 |
| 8 | faudit_start_date | 审计范围.开始 | timestamp | 0 |  |  | null | 审计范围.开始 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fchecktype | 应用业务环节 | varchar | 2 |  | √ | ' ' | 应用业务环节,枚举: 1 :销项发票开具 2 :进项发票采集 3 :销项全票池审计 4 :进项全票池审计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_irew_scheme_log |  | fid |
| 2 | idx_irew_scheme_log_time |  | fcreatetime |
| 3 | idx_irew_scheme_log |  | fwarning_scheme,forgid |

---

## 引擎明细-子表 t_irew_scheme_log_items

- **表名称：** 引擎明细-子表
- **表名：** t_irew_scheme_log_items

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcustomize_engine | 引擎id | int8 | 64 |  | √ | 0 | 引擎id |
| 3 | fcustomize_engine_name | 引擎名称 | varchar | 50 |  | √ | ' ' | 引擎名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fend_time | 执行结束时间 | timestamp | 0 |  |  | null | 执行结束时间 |
| 6 | fstart_time | 执行开始时间 | timestamp | 0 |  |  | null | 执行开始时间 |
| 7 | fexecute_result | 校验成功 | bpchar | 1 |  | √ | ' ' | 校验成功 |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_irew_scheme_log_items |  | fentryid |
| 2 | idx_irew_scheme_log_items_fk |  | fid |
