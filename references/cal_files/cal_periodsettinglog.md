# 存货核算初始化日志-cal_periodsettinglog

## 存货核算初始化日志-主表 t_cal_periodsettinglog

- **表名称：** 存货核算初始化日志-主表
- **表名：** t_cal_periodsettinglog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissuccess | 结果状态 | bpchar | 1 |  | √ | '0' | 结果状态 |
| 3 | flog_tag | 日志_详情 | text | 0 |  |  | null | 日志_详情 |
| 4 | fcalorgid | 核算组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 5 | foperationtime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 6 | ferrortype | 错误类型 | int4 | 32 |  | √ | 0 | 错误类型 |
| 7 | flog | 日志 | varchar | 255 |  | √ | ' ' | 日志 |
| 8 | flinkids_tag | 业务对象id_详情 | text | 0 |  |  | null | 业务对象id_详情 |
| 9 | flinkbillobject | 业务对象 | varchar | 255 |  | √ | ' ' | 业务对象 |
| 10 | fuserfield | 操作用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | ffaillink | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 12 | fcostaccountid | 成本主体 | int8 | 64 |  | √ | 0 | 成本主体 cal_bd_costaccount |
| 13 | foperation | 操作 | varchar | 255 |  | √ | ' ' | 操作,枚举: 1 :结束初始化 2 :批量反初始化 3 :启用 4 :反启用 5 :修改 6 :启用即时成本 7 :反启用即时成本 8 :获取库存期初数据 9 :引入内部单价 10 :引入外部单价 |
| 14 | flinkids | 业务对象id | varchar | 255 |  | √ | ' ' | 业务对象id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | index_costaccount |  | fcostaccountid |
| 2 | pk_t_cal_periodsettinglog |  | fid |
