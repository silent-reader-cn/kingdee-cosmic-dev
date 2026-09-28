# 核销执行日志-msmod_wf_nlog

## 核销子任务-子表 t_msmod_wfnlogentry

- **表名称：** 核销子任务-子表
- **表名：** t_msmod_wfnlogentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftaskexectime | 执行时间 | timestamp | 0 |  |  | null | 执行时间 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | ftaskstatus | 任务状态 | bpchar | 1 |  | √ | 'u' | 任务状态,枚举: U :未发送 A :已发送 S :成功 F :失败 |
| 5 | ftaskexecinfo | 任务执行信息 | varchar | 255 |  | √ | ' ' | 任务执行信息 |
| 6 | ftaskname | 任务名称 | varchar | 100 |  | √ | ' ' | 任务名称 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | ftaskclass | 任务执行类 | varchar | 100 |  | √ | ' ' | 任务执行类 |
| 9 | ftaskexecinfo_tag | 任务执行信息_详情 | text | 0 |  |  | null | 任务执行信息_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_wfnlogentry_fid |  | fid |
| 2 | pk_t_msmod_wfnlogentry |  | fentryid |

---

## 核销执行日志-主表 t_msmod_wfnlog

- **表名称：** 核销执行日志-主表
- **表名：** t_msmod_wfnlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fwfseq | 核销/反核销批号 | varchar | 50 |  | √ | ' ' | 核销/反核销批号 |
| 3 | fstatus | 状态 | bpchar | 1 |  | √ | 'F' | 状态,枚举: S :成功 F :失败 W :进行中 |
| 4 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 5 | ftraceid | traceid | varchar | 50 |  | √ | ' ' | traceid |
| 6 | fexecuteinfo | 执行信息 | varchar | 2000 |  | √ | ' ' | 执行信息 |
| 7 | fsrcbillno_tag | 发起方单据编号_详情 | text | 0 |  |  | null | 发起方单据编号_详情 |
| 8 | fsrcbillno | 发起方单据编号 | varchar | 2000 |  | √ | ' ' | 发起方单据编号 |
| 9 | fwfmode | 核销方式 | bpchar | 1 |  | √ | 'F' | 核销方式,枚举: F :流程核销 M :手工核销 A :手工自动核销 |
| 10 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fsrcbillentity | 发起方单据对象 | varchar | 50 |  | √ | ' ' | [单据主实体 bos_billmainentity](../mdl_files/bos_billmainentity.md) |
| 12 | fwftype | 核销类别 | int8 | 64 |  | √ | 0 | [核销类别 msmod_writeofftype](../mscommon_files/msmod_writeofftype.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msmod_wfnlog_wfseq |  | fwfseq |
| 2 | pk_t_msmod_wfnlog |  | fid |
