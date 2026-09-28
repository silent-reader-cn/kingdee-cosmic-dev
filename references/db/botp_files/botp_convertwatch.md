# 单据转换报告-botp_convertwatch

## 单据转换报告-主表 t_botp_convert_watch

- **表名称：** 单据转换报告-主表
- **表名：** t_botp_convert_watch

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
| 8 | ftbillid | ftbillid | int8 | 64 |  | √ | 0 |  |
| 9 | fstatus | 状态 | varchar | 36 |  | √ | ' ' | 状态,枚举: D :待生成 Z :生成中 S :已完成 F :生成失败 |
| 10 | fsbillid | 源单内码 | int8 | 64 |  | √ | 0 | 源单内码 |
| 11 | ftbillno | ftbillno | varchar | 500 |  | √ | ' ' |  |
| 12 | fconvertruleid | 转换规则id | int8 | 64 |  | √ | 0 | 转换规则id |
| 13 | fsentitynumber | 源单单据标识 | varchar | 150 |  | √ | ' ' | 源单单据标识 |
| 14 | furl | 报告地址 | varchar | 500 |  |  | null | 报告地址 |
| 15 | fdesc | 备注 | varchar | 500 |  |  | null | 备注 |
| 16 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 17 | ftentitynumber | ftentitynumber | varchar | 150 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_botp_convert_watch_tbillid |  | ftbillid |
| 2 | idx_botp_convert_watch_sbillno |  | fsbillno |
| 3 | idx_botp_convert_watch_sbillid |  | fsbillid |
| 4 | idx_botp_convert_watch_unikey |  | funiquekey |
| 5 | idx_botp_convert_watch_traceid |  | ftraceid |
| 6 | pk_t_botp_convert_watch |  | fid |
| 7 | idx_botp_convert_watch_tbillno |  | ftbillno |
