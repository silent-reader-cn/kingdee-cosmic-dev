# 执行日志-pa_executionlog

## 规则列表-子表 t_pa_resultentry

- **表名称：** 规则列表-子表
- **表名：** t_pa_resultentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentry_writeoffstatus | 已冲销 | bpchar | 1 |  | √ | '1' | 已冲销,枚举: 4 :已冲销 1 :未调整 |
| 3 | fentry_executiontime | 执行日期 | timestamp | 0 |  |  | null | 执行日期 |
| 4 | fstepname | 步骤名称 | varchar | 50 |  | √ | ' ' | 步骤名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentry_businessrule | 业务规则 | int8 | 64 |  | √ | 0 | [业务规则 pa_businessrule](../pa_files/pa_businessrule.md) |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fentry_executionstatus | 执行状态 | bpchar | 1 |  | √ | '0' | 执行状态,枚举: 0 :新增 1 :进行中 2 :成功 9 :失败 |
| 9 | frule_id | 规则id | int8 | 64 |  | √ | 0 | 规则id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_resultentry_1 |  | fid |
| 2 | pk_t_pa_resultentry |  | fentryid |

---

## 调整列表-子表 t_pa_resultadjust

- **表名称：** 调整列表-子表
- **表名：** t_pa_resultadjust

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 4 | fadjustid | 调整单id | int8 | 64 |  | √ | 0 | 调整单id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_resultadjust |  | fentryid |
| 2 | idx_pa_resultadjust_1 |  | fid |

---

## 执行日志-主表 t_pa_executionlog

- **表名称：** 执行日志-主表
- **表名：** t_pa_executionlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fexecution_type | 执行方式 | bpchar | 1 |  | √ | '1' | 执行方式,枚举: 1 :手动执行 2 :系统执行 |
| 3 | fendperiod | 结束期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fremark | 备注 | varchar | 255 |  |  | null | 备注 |
| 5 | forgfield | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fexecution_status | 执行状态 | bpchar | 1 |  | √ | '0' | 执行状态,枚举: 0 :新增 1 :进行中 2 :执行成功 9 :执行失败 |
| 7 | fbusiness_plan | 规则组 | int8 | 64 |  | √ | 0 | [规则组 pa_businessplan](../pa_files/pa_businessplan.md) |
| 8 | fstartperiod | 期间 | int8 | 64 |  | √ | 0 | 会计日历 bd_period |
| 9 | fremark_tag | 备注_详情 | text | 0 |  |  | null | 备注_详情 |
| 10 | fanalysis_system | 分析体系 | int8 | 64 |  | √ | 0 | [分析体系 pa_anasystemsetting](../pa_files/pa_anasystemsetting.md) |
| 11 | fdetailtime | 详细时间 | int8 | 64 |  | √ | 0 | 详细时间 |
| 12 | fitemclasstypefield | 动态基础资料类型 | varchar | 255 |  | √ | ' ' | 动态基础资料类型,枚举: bd_period :会计期间 |
| 13 | fexecution_mode | 执行类型 | bpchar | 1 |  | √ | '0' | 执行类型,枚举: 0 :规则执行 1 :冲销执行 2 :调整执行 |
| 14 | fanalysis_model | 分析模型 | int8 | 64 |  | √ | 0 | [分析模型 pa_analysismodel](../pa_files/pa_analysismodel.md) |
| 15 | fnumber | 执行批次号 | varchar | 255 |  | √ | ' ' | 执行批次号 |
| 16 | fexecution_time | 执行日期 | timestamp | 0 |  |  | null | 执行日期 |
| 17 | fbusiness_rule | 业务规则 | int8 | 64 |  | √ | 0 | [业务规则 pa_businessrule](../pa_files/pa_businessrule.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_execution_log_1 |  | fanalysis_system,fanalysis_model,forgfield |
| 2 | pk_t_pa_executionlog |  | fid |
