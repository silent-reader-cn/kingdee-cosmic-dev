# 单据反写报告-botp_writebackwatch

## 单据反写报告-主表 t_botp_writeback_watch

- **表名称：** 单据反写报告-主表
- **表名：** t_botp_writeback_watch

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftraceid | traceid | varchar | 150 |  | √ | ' ' | traceid |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | funiquekey | 唯一标识 | varchar | 200 |  | √ | ' ' | 唯一标识 |
| 5 | fmoudlekey | 模块key | varchar | 100 |  | √ | ' ' | 模块key |
| 6 | fsbillno | 源单编号 | varchar | 500 |  | √ | ' ' | 源单编号 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | ftbillid | 目标单内码 | int8 | 64 |  | √ | 0 | 目标单内码 |
| 9 | fstatus | 状态 | varchar | 36 |  | √ | ' ' | 状态,枚举: D :待生成 Z :生成中 S :已完成 F :生成失败 |
| 10 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 11 | ftbillno | 目标单编号 | varchar | 500 |  | √ | ' ' | 目标单编号 |
| 12 | fsentitynumber | 源单单据标识 | varchar | 150 |  | √ | ' ' | 源单单据标识 |
| 13 | furl | 报告地址 | varchar | 500 |  |  | null | 报告地址 |
| 14 | fdesc | 备注 | varchar | 500 |  |  | null | 备注 |
| 15 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 16 | ftentitynumber | 目标单单据标识 | varchar | 150 |  |  | null | 目标单单据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_botp_bf_watch_sbillno |  | fsbillno |
| 2 | idx_botp_bf_watch_tbillid |  | ftbillid |
| 3 | pk_t_botp_writeback_watch |  | fid |
| 4 | idx_botp_bf_watch_unikey |  | funiquekey |
| 5 | idx_botp_bf_watch_sbillid |  | fsbillid |
| 6 | idx_botp_bf_watch_traceid |  | ftraceid |
| 7 | idx_botp_bf_watch_tbillno |  | ftbillno |
