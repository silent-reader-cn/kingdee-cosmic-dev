# 定时生成经营流水账记录-xkoac_autovchlog

## 定时生成经营流水账记录-主表 t_xkoac_autovchlog

- **表名称：** 定时生成经营流水账记录-主表
- **表名：** t_xkoac_autovchlog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransid | 事务标识 | varchar | 50 |  | √ | ' ' | 事务标识 |
| 3 | fexecstatus | 执行状态 | bpchar | 1 |  | √ | ' ' | 执行状态,枚举: 1 :进行中 2 :成功 3 :失败 4 :已中止 |
| 4 | ftype | 执行类型 | bpchar | 1 |  | √ | ' ' | 执行类型,枚举: 0 :自动执行 1 :手动执行 |
| 5 | fintelschemaid | 执行方案 | int8 | 64 |  | √ | 0 | [定时生成经营流水账方案 xkoac_autovchplan](../xkoac_files/xkoac_autovchplan.md) |
| 6 | fexecstartdate | 方案开始时间 | timestamp | 0 |  |  | null | 方案开始时间 |
| 7 | fexecenddate | 方案结束时间 | timestamp | 0 |  |  | null | 方案结束时间 |
| 8 | ftaskid | 后台执行任务id | varchar | 50 |  | √ | ' ' | 后台执行任务id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkoac_autovchlog |  | fintelschemaid |
| 2 | pk_xkoac_autovchlog |  | fid |
