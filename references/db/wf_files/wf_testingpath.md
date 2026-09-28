# 测试计划路径-wf_testingpath

## 测试计划路径-多语言表 t_wf_testingpath_l

- **表名称：** 测试计划路径-多语言表
- **表名：** t_wf_testingpath_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fnodename | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_testingpath_l |  | fid,flocaleid |
| 2 | t_wf_testingpath_l_pkey |  | fpkid |

---

## 测试计划路径-主表 t_wf_testingpath

- **表名称：** 测试计划路径-主表
- **表名：** t_wf_testingpath

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstep | 步骤 | varchar | 30 |  | √ | ' ' | 步骤 |
| 3 | factinstid | 历史活动实例id | varchar | 30 |  | √ | ' ' | 历史活动实例id |
| 4 | fmodifyexp | 字段修改 | varchar | 50 |  | √ | ' ' | 字段修改 |
| 5 | fsourceid | 源节点ID | varchar | 30 |  | √ | ' ' | 源节点ID |
| 6 | fvariables | 变量 | text | 0 |  |  | null | 变量 |
| 7 | fexecutiontype | 执行类型 | varchar | 30 |  | √ | ' ' | 执行类型 |
| 8 | fplanid | 计划ID | int8 | 64 |  | √ | 0 | 计划ID |
| 9 | flevel | 层级 | int8 | 64 |  | √ | 0 | 层级 |
| 10 | fnodename | 节点名称 | varchar | 500 |  | √ | ' ' | 节点名称 |
| 11 | factivitytype | 节点类型 | varchar | 50 |  | √ | ' ' | 节点类型 |
| 12 | fassigneeid | 处理人ID | int8 | 64 |  | √ | 0 | 处理人ID |
| 13 | fnodeid | 节点ID | varchar | 255 |  | √ | ' ' | 节点ID |
| 14 | fcycle | 路径 | varchar | 50 |  | √ | ' ' | 路径 |
| 15 | fdecision | 决策项 | varchar | 50 |  | √ | ' ' | 决策项 |
| 16 | ftargetid | 目标节点ID | varchar | 30 |  | √ | ' ' | 目标节点ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_testingpath_pkey |  | fid |
| 2 | idx_wf_testingpath_planid |  | fplanid |
