# 线上工作量统计表-ssc_workloadonline

## 线上工作量统计表-主表 t_tk_workloadonline

- **表名称：** 线上工作量统计表-主表
- **表名：** t_tk_workloadonline

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | fgroupid | 用户组 | int8 | 64 |  | √ | 0 | [用户组 task_usergroup](../ssc_files/task_usergroup.md) |
| 4 | ftasktype | 任务类型 | int8 | 64 |  | √ | 0 | [任务类型 task_tasktype](../ssc_files/task_tasktype.md) |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 6 | fstandardnum | 标准工作量 | numeric | 23 | 10 | √ | 0 | 标准工作量 |
| 7 | fhandlerid | 处理人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | ftasknum | 任务数 | int4 | 32 |  | √ | 1 | 任务数 |
| 9 | ftaskid | 任务id | int8 | 64 |  | √ | 0 | 任务id |
| 10 | fattribute | 任务属性 | bpchar | 1 |  | √ | ' ' | 任务属性,枚举: 0 :审单任务 1 :质检任务 |
| 11 | ftaskcoefficent | 任务量系数 | numeric | 23 | 10 | √ | 0 | 任务量系数 |
| 12 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 13 | fcompletetime | 任务完成时间 | timestamp | 0 |  |  | null | 任务完成时间 |
| 14 | fbilltypeid | 业务单据 | int8 | 64 |  | √ | 0 | [业务单据 task_taskbill](../ssc_files/task_taskbill.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_workloadonline |  | fid |
| 2 | idx_ssc_workloadonline_id |  | fsscid,ftaskid,fgroupid |
