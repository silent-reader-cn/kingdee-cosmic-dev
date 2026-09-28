# 校验日志-pa_verificationlog

## 校验日志-主表 t_pa_verificationlog

- **表名称：** 校验日志-主表
- **表名：** t_pa_verificationlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 80 |  | √ | ' ' | 名称 |
| 3 | fbaseperiod | 期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 4 | fcreatedate | 执行日期 | timestamp | 0 |  |  | null | 执行日期 |
| 5 | fcreatorid | 执行人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fconditionsetting | 校验条件 | varchar | 500 |  | √ | ' ' | 校验条件 |
| 7 | fspare | 联查 | varchar | 50 |  | √ | ' ' | 联查 |
| 8 | fanalysissystem | 体系 | int8 | 64 |  | √ | 0 | [分析体系 pa_anasystemsetting](../pa_files/pa_anasystemsetting.md) |
| 9 | fverificationresult | 校验结果 | bpchar | 1 |  | √ | ' ' | 校验结果,枚举: A :通过 B :不通过 |
| 10 | freturnresult | 结果 | varchar | 2000 |  | √ | ' ' | 结果 |
| 11 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | fanalysismodel | 模型 | int8 | 64 |  | √ | 0 | [分析模型 pa_analysismodel](../pa_files/pa_analysismodel.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pk_t_pa_verification_log_1 |  | fanalysissystem |
| 2 | pk_t_pa_verificationlog |  | fid |
| 3 | idx_pk_t_pa_verification_log_2 |  | fbaseperiod |
