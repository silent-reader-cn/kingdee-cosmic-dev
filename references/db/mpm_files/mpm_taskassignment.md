# 任务资源分配-mpm_taskassignment

## 任务资源分配-主表 t_mpm_taskassignment

- **表名称：** 任务资源分配-主表
- **表名：** t_mpm_taskassignment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fprojectid | 项目 | int8 | 64 |  | √ | 0 | [项目 bd_project](../basedata_files/bd_project.md) |
| 4 | fbillstatus | 单据状态 | bpchar | 1 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fresourceid | 任务成员 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | ftaskowner | 任务负责人 | bpchar | 1 |  | √ | ' ' | 任务负责人 |
| 8 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 9 | fallocationpercent | 投入程度(%) | numeric | 23 | 10 |  | null | 投入程度(%) |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fenddate | 结束日期 | timestamp | 0 |  |  | null | 结束日期 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fstartdate | 开始日期 | timestamp | 0 |  |  | null | 开始日期 |
| 14 | ftaskid | 任务 | int8 | 64 |  | √ | 0 | [项目任务F7 mpm_task_f7](../mpm_files/mpm_task_f7.md) |
| 15 | fbillno | 单据编号 | varchar | 50 |  | √ | ' ' | 单据编号 |
| 16 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fworkload | 排期工时 | numeric | 23 | 10 |  | null | 排期工时 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mpm_taskassignment |  | fid |
| 2 | idx_taskassignment_billno |  | fbillno |
