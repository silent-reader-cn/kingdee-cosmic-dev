# CDC异步任务状态-bd_cdc_taskstatus

## CDC异步任务状态-主表 t_bd_cdc_taskstatus

- **表名称：** CDC异步任务状态-主表
- **表名：** t_bd_cdc_taskstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransregdt | 事务启动时间 | timestamp | 0 |  |  | null | 事务启动时间 |
| 3 | fperiodid | 期间 | int8 | 64 |  | √ | 0 | 期间 |
| 4 | ftasktype | 任务类型 | int4 | 32 |  | √ | 0 | 任务类型 |
| 5 | finstanceid | 运行同步操作的实例ID | varchar | 50 |  | √ | ' ' | 运行同步操作的实例ID |
| 6 | forgid | 组织 | int8 | 64 |  | √ | 0 | 组织 |
| 7 | flast_cdc_id | 上次完成的最后一条CDC记录的ID | int8 | 64 |  | √ | 0 | 上次完成的最后一条CDC记录的ID |
| 8 | flast_max_srcid | 上次完成的最大新增源记录ID | int8 | 64 |  | √ | 0 | 上次完成的最大新增源记录ID |
| 9 | flast_max_srcentryid | 上次完成的最大新增源分录记录ID | int8 | 64 |  | √ | 0 | 上次完成的最大新增源分录记录ID |
| 10 | flaststatus | 上次完成的状态 | bpchar | 1 |  | √ | '3' | 上次完成的状态,枚举: 3 :成功 8 :失败 |
| 11 | flastcomptime | 上次完成时间 | timestamp | 0 |  |  | null | 上次完成时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_cdc_taskstatus_2 |  | ftasktype,flast_cdc_id,finstanceid |
| 2 | pk_bd_cdc_taskstatus |  | fid |
| 3 | idx_bd_cdc_taskstatus_un_1 |  | forgid,fperiodid,ftasktype |
