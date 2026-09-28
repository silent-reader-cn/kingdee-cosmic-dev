# 共享时长统计明细表-task_wftimestatistics

## 共享时长统计明细表-主表 t_tk_wftimestatistics

- **表名称：** 共享时长统计明细表-主表
- **表名：** t_tk_wftimestatistics

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsscid | 共享中心 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 3 | ftimemax | 节点最长耗时 | numeric | 23 | 10 | √ | 0 | 节点最长耗时 |
| 4 | ftasktypeid | 任务类型 | int8 | 64 |  | √ | 0 | 任务类型 task_tasktype |
| 5 | forgid | 组织 | int8 | 64 |  | √ | 0 | 业务单元 bos_org |
| 6 | fdate | 日期 | timestamp | 0 |  |  | null | 日期 |
| 7 | fpersonid | 处理人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 9 | fcount | 执行次数 | int8 | 64 |  | √ | 0 | 执行次数 |
| 10 | ftaskdefkey | 流程节点ID | varchar | 100 |  | √ | ' ' | 流程节点ID |
| 11 | ftimesum | 节点总耗时 | numeric | 23 | 10 | √ | 0 | 节点总耗时 |
| 12 | fbilltypeid | 业务单据 | int8 | 64 |  | √ | 0 | 业务单据 task_taskbill |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_tk_wftimestatistics |  | fid |
| 2 | idx_ssc_wfstatics_date |  | fdate |
