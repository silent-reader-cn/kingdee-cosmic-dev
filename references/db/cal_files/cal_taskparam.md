# 核算后台任务参数-cal_taskparam

## 核算后台任务参数-主表 t_cal_taskparam

- **表名称：** 核算后台任务参数-主表
- **表名：** t_cal_taskparam

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftaskgroupno | 任务组key | varchar | 50 |  | √ | ' ' | 任务组key |
| 3 | fparam | 参数 | varchar | 255 |  | √ | ' ' | 参数 |
| 4 | fstatus | 状态 | varchar | 30 |  | √ | ' ' | 状态,枚举: A :运行中 B :成功 C :失败 |
| 5 | ftask | 任务名称 | int8 | 64 |  | √ | 0 | 任务名称 |
| 6 | ffunctionnum | 功能编码 | varchar | 50 |  | √ | ' ' | 功能编码 |
| 7 | fparam_tag | 参数_详情 | text | 0 |  |  | null | 参数_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cal_taskparam |  | fid |
| 2 | idx_cal_taskgroupno |  | ftaskgroupno |
