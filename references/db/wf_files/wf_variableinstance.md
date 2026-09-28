# 流程变量实例-wf_variableinstance

## 流程变量实例-主表 t_wf_variable

- **表名称：** 流程变量实例-主表
- **表名：** t_wf_variable

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftext | 文本值 | text | 0 |  |  | null | 文本值 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fdouble | 双精度值 | numeric | 19 | 6 | √ | 0.000000 | 双精度值 |
| 5 | factinstid | 节点实例ID | int8 | 64 |  | √ | 0 | 节点实例ID |
| 6 | fexecutionid | 执行实例ID | int8 | 64 |  | √ | 0 | 执行实例ID |
| 7 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 8 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 9 | flong | 长精度值 | int8 | 64 |  | √ | 0 | 长精度值 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | ftype | 类型 | varchar | 30 |  | √ | ' ' | 类型 |
| 12 | fmodifydate | 最后修改时间 | timestamp | 0 |  |  | null | 最后修改时间 |
| 13 | ftaskid | 任务ID | int8 | 64 |  | √ | 0 | 任务ID |
| 14 | ftext2 | 文本值2 | text | 0 |  |  | null | 文本值2 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_variable_task_id |  | ftaskid |
| 2 | idx_wf_vari_exec_taskid |  | fexecutionid,ftaskid |
| 3 | idx_wf_variable_exec_name |  | fexecutionid,fname |
| 4 | t_wf_variable_pkey |  | fid |
| 5 | idx_wf_variable_procinst |  | fprocinstid |

---

## 流程变量实例-多语言表 t_wf_variable_l

- **表名称：** 流程变量实例-多语言表
- **表名：** t_wf_variable_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 3 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_variable_localeid |  | fid,flocaleid |
| 2 | t_wf_variable_l_pkey |  | fpkid |
