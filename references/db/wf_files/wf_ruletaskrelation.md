# 规则任务关系实体-wf_ruletaskrelation

## 规则任务关系实体-主表 t_wf_rtrelation

- **表名称：** 规则任务关系实体-主表
- **表名：** t_wf_rtrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcurrentsubject | 当前任务主题 | varchar | 3000 |  | √ | ' ' | 当前任务主题 |
| 3 | fmarkid | 标记id | int8 | 64 |  | √ | 0 | 标记id |
| 4 | fpriority | 优先级 | int8 | 64 |  | √ | 50 | 优先级 |
| 5 | fruletype | 规则所属者类型 | varchar | 100 |  | √ | ' ' | 规则所属者类型 |
| 6 | fruleid | 规则id | int8 | 64 |  | √ | 0 | 规则id |
| 7 | fuserid | 拥有者id | int8 | 64 |  | √ | 0 | 拥有者id |
| 8 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 9 | ftaskid | 任务Id | int8 | 64 |  | √ | 0 | 任务Id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_rtrelation_userid |  | fuserid |
| 2 | idx_wf_rtrelation_markid |  | fmarkid |
| 3 | idx_wf_rtrelation_procinst |  | fprocinstid |
| 4 | idx_wf_rtrelation_task |  | ftaskid |
| 5 | t_wf_rtrelation_pkey |  | fid |
| 6 | idx_wf_rtrelation_rule |  | fruleid |

---

## 规则任务关系实体-多语言表 t_wf_rtrelation_l

- **表名称：** 规则任务关系实体-多语言表
- **表名：** t_wf_rtrelation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrentsubject | 当前任务主题 | varchar | 3000 |  | √ | ' ' | 当前任务主题 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_wf_rtrelation_l |  | fpkid |
| 2 | idx_wf_rtrelation_l |  | fid,flocaleid |
