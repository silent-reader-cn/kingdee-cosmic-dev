# 自动对账报告-frm_autocheckreport

## 自动对账报告-主表 t_frm_autoreport

- **表名称：** 自动对账报告-主表
- **表名：** t_frm_autoreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fautoschema | 自动对账方案 | int8 | 64 |  | √ | 0 | [自动对账方案 frm_autoreconciliation](../frm_files/frm_autoreconciliation.md) |
| 3 | fexecstatus | 执行状态 | bpchar | 1 |  | √ | '1' | 执行状态,枚举: 1 :进行中 2 :成功 3 :失败 4 :已中止 |
| 4 | ftype | 执行类型 | bpchar | 1 |  | √ | ' ' | 执行类型,枚举: 0 :自动执行 1 :手动执行 |
| 5 | fbatchno | 批次号 | varchar | 50 |  | √ | ' ' | 批次号 |
| 6 | fexecstartdate | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 7 | fresult | 对账结果状态 | bpchar | 1 |  | √ | ' ' | 对账结果状态,枚举: 1 :全部对账平衡 2 :部分对账平衡 3 :全部不平衡 |
| 8 | fexecenddate | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 9 | fexecutorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_frm_autoreport_bn |  | fbatchno |
| 2 | pk_frm_autoreport |  | fid |

---

## 单据体-子表 t_frm_autoreportentry

- **表名称：** 单据体-子表
- **表名：** t_frm_autoreportentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbizapp | 业务系统 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 3 | fscheme | 业财对账方案 | int8 | 64 |  | √ | 0 | [业财对账方案 frm_reconciliation_scheme](../frm_files/frm_reconciliation_scheme.md) |
| 4 | fperiod | 对账期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | freconresult | 对账结果状态 | bpchar | 1 |  | √ | '1' | 对账结果状态,枚举: 1 :平衡 2 :不平衡 3 :账簿无适用的对账方案 4 :执行人没有智能会计平台许可 5 :执行人无对账权限 6 :异常失败 7 :当前账簿期间有正在执行的对账任务 |
| 7 | ftaskid | 对账任务id | int8 | 64 |  | √ | 0 | 对账任务id |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | facctbook | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_frm_autoreportentry |  | fentryid |
| 2 | idx_frm_autoreporte_fid |  | fid |
