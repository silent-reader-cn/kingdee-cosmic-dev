# 反写日志-botp_log

## 反写日志-主表 t_botp_log

- **表名称：** 反写日志-主表
- **表名：** t_botp_log

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fparentid | 父日志 | int8 | 64 |  | √ | 0 | 父日志 |
| 3 | fttableid | 下游单主表编码 | int8 | 64 |  | √ | 0 | 下游单主表编码 |
| 4 | fstableid | 源单主表编码 | int8 | 64 |  | √ | 0 | 源单主表编码 |
| 5 | foptype | 操作类型 | bpchar | 1 |  | √ | '0' | 操作类型,枚举: 0 :下推 1 :选单 S :保存 B :提交 A :审核 D :删除 U :反审核 C :撤销 I :作废 V :反作废 |
| 6 | fdata_tag | 日志详情_详情 | text | 0 |  |  | null | 日志详情_详情 |
| 7 | fuserid | 用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fsbillno | 源单编号 | varchar | 200 |  | √ | ' ' | 源单编号 |
| 9 | fstarttime | 开始时间 | timestamp | 0 |  | √ | null | 开始时间 |
| 10 | fzipver | 日志压缩版本 | varchar | 30 |  | √ | ' ' | 日志压缩版本 |
| 11 | ftbillid | 下游单内码 | int8 | 64 |  | √ | 0 | 下游单内码 |
| 12 | fstatus | 状态 | bpchar | 1 |  | √ | '0' | 状态,枚举: 0 :未执行 1 :已完成 2 :异常 3 :重试成功 |
| 13 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 14 | ftbillno | 下游单编号 | varchar | 200 |  | √ | ' ' | 下游单编号 |
| 15 | fsentitynumber | 源单类型 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 16 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 17 | ftaskid | 任务号 | int8 | 64 |  | √ | 0 | 任务号 |
| 18 | flogtype | 日志类型 | bpchar | 1 |  | √ | '0' | 日志类型,枚举: T :行关联关系 W :反写需求 F :反写结果 V :反写值变化 E :异常日志 P :下推日志 |
| 19 | fdata | 日志详情 | varchar | 255 |  | √ | ' ' | 日志详情 |
| 20 | ftentitynumber | 下游单据类型 | varchar | 100 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_botp_log_parentid |  | fparentid |
| 2 | idx_botp_log_starttime |  | fstarttime |
| 3 | idx_botp_log_tbillno |  | ftbillno |
| 4 | idx_botp_log_sbillno |  | fsbillno |
| 5 | idx_botp_log_sbillid |  | fsbillid |
| 6 | pk_botp_log |  | fid |
