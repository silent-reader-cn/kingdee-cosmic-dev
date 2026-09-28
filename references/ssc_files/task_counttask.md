# 个人任务排名中间表-task_counttask

## 个人任务排名中间表-主表 t_tk_counttask

- **表名称：** 个人任务排名中间表-主表
- **表名：** t_tk_counttask

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | fprocessing | 处理中任务数 | int8 | 64 |  | √ | 0 | 处理中任务数 |
| 4 | frankcoefficient | 任务量 | numeric | 19 | 6 | √ | 0.000000 | 任务量 |
| 5 | ftaskcount | 已完成数 | int8 | 64 |  | √ | 0 | 已完成数 |
| 6 | fcounttime | fcounttime | timestamp | 0 |  |  | null |  |
| 7 | fcreatetime | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 8 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | 任务类型 task_tasktype |
| 9 | fpersonid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fdaterange | 日期范围 | int8 | 64 |  | √ | 0 | 日期范围 |
| 11 | fallocated | 已分配数 | int8 | 64 |  | √ | 0 | 已分配数 |
| 12 | fprocessrankcoefficient | 处理中任务量 | numeric | 19 | 6 | √ | 0.000000 | 处理中任务量 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_tk_counttime |  | fcounttime |
| 2 | idx_tk_tasktype |  | ftasktypeid |
| 3 | t_tk_counttask_pkey |  | fid |
| 4 | idx_tk_ssc |  | fsscid |
