# 计算任务列表-cal_cr_calcreport

## 计算任务列表-主表 t_cal_cr_calcreport

- **表名称：** 计算任务列表-主表
- **表名：** t_cal_cr_calcreport

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fretrospectrange | 计算范围 | varchar | 50 |  | √ | ' ' | 计算范围,枚举: 1 :期末结存 2 :出库 3 :入库 |
| 3 | fstatus | 状态 | varchar | 50 |  | √ | ' ' | 状态,枚举: 1 :执行中 2 :成功 3 :失败 |
| 4 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | ftasktype | 任务类型 | varchar | 50 |  | √ | ' ' | 任务类型,枚举: 1 :计算 2 :反计算 |
| 6 | fretrospectperiodid | 计算期间 | int8 | 64 |  | √ | 0 | [会计日历 bd_period](../fibd_files/bd_period.md) |
| 7 | fretrospectcplanid | 还原方案 | int8 | 64 |  | √ | 0 | [还原方案 cal_cr_retrospectplan](../cal_files/cal_cr_retrospectplan.md) |
| 8 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 9 | fstarttime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cal_cr_calcreport_pd |  | fretrospectcplanid |
| 2 | pk_cal_cr_calcreport |  | fid |
