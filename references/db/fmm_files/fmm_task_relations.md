# 绑定工单数据存储-fmm_task_relations

## 绑定工单数据存储-主表 t_fmm_task_relations

- **表名称：** 绑定工单数据存储-主表
- **表名：** t_fmm_task_relations

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsourcebillentryid | 来源单据分录ID | varchar | 50 |  | √ | ' ' | 来源单据分录ID |
| 3 | fsourcebilltype | 来源单据类型 | varchar | 50 |  | √ | ' ' | 来源单据类型 |
| 4 | ftargetbillentryid | 目标单据分录ID | varchar | 50 |  | √ | ' ' | 目标单据分录ID |
| 5 | fsourcebillid | 来源单据ID | varchar | 50 |  | √ | ' ' | 来源单据ID |
| 6 | ftargetbilltype | 目标单据类型 | varchar | 50 |  | √ | ' ' | 目标单据类型 |
| 7 | ftargetbillid | 目标单据ID | varchar | 50 |  | √ | ' ' | 目标单据ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_fmm_task_relations |  | fid |
