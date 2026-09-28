# 任务配置-tctb_task_config

## 任务配置-主表 t_tctb_task_config

- **表名称：** 任务配置-主表
- **表名：** t_tctb_task_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fpriority | 执行顺序 | int4 | 32 |  | √ | 0 | 执行顺序 |
| 3 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 4 | ftaskdefine | 任务 | varchar | 50 |  | √ | ' ' | [调度执行程序 sch_taskdefine](../sys_files/sch_taskdefine.md) |
| 5 | fbatchsize | 分批任务数 | int4 | 32 |  | √ | 0 | 分批任务数 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_tctb_task_config_1 |  | fnumber |
| 2 | pk_t_tctb_task_config |  | fid |
