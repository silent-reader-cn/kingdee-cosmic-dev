# 管理员首页数据持续更新扩展-task_indexdata_update_ext

## 管理员首页数据持续更新扩展-主表 t_tk_indexdata_ext

- **表名称：** 管理员首页数据持续更新扩展-主表
- **表名：** t_tk_indexdata_ext

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fgroupid | 用户组 | int8 | 64 |  | √ | 0 | 用户组 task_usergroup |
| 4 | ftaskamount | 任务量 | numeric | 12 | 2 | √ | 0.00 | 任务量 |
| 5 | ftaskefficiency | 平均耗时(单/小时) | numeric | 10 | 2 | √ | 0.00 | 平均耗时(单/小时) |
| 6 | ftaskcount | 任务数 | int8 | 64 |  | √ | 0 | 任务数 |
| 7 | fuser | 用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fupdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tk_indexdata_ext_pkey |  | fid |
| 2 | index_ssc_indexdata_ext_u |  | fuser |
| 3 | index_ssc_indexdata_ext_s |  | fsscid |
