# 轻脚本监控记录-kingscript_monitor

## 单据体-子表 t_ks_monitor_log

- **表名称：** 单据体-子表
- **表名：** t_ks_monitor_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fexec_is_exception | 执行异常 | varchar | 50 |  |  | null | 执行异常,枚举: false :否 true :是 |
| 3 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fexec_time | 执行总时间(s) | numeric | 23 | 10 |  | null | 执行总时间(s) |
| 5 | fexec_exception_context_tag | 异常信息_详情 | text | 0 |  |  | null | 异常信息_详情 |
| 6 | fexec_count | 执行次数 | int8 | 64 |  |  | null | 执行次数 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | fexec_exception_context | 异常信息 | varchar | 255 |  |  | null | 异常信息 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fexec_scene | 执行场景 | varchar | 50 |  |  | null | 执行场景,枚举: engine_init :引擎初始化 engine_eval :脚本运行 engine_load_script :脚本加载 transpiler_trans :脚本编译 |
| 12 | fexec_max_time | 最大时间(s) | numeric | 23 | 10 |  | null | 最大时间(s) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ks_monitor_log_fid |  | fid |
| 2 | pk_t_ks_monitor_log |  | fentryid |

---

## 轻脚本监控记录-主表 t_ks_monitor

- **表名称：** 轻脚本监控记录-主表
- **表名：** t_ks_monitor

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fbillstatus | 单据状态 | varchar | 10 |  |  | null | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 6 | fscript_basedata | 轻脚本 | varchar | 50 |  |  | null | 插件脚本编辑 ide_pluginscript |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 9 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fall_count | 执行总次数 | int8 | 64 |  | √ | 0 | 执行总次数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ks_monitor |  | fid |
| 2 | idx_ks_monitor_billno |  | fbillno |
