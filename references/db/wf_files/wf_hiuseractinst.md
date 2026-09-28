# 历史人工节点-wf_hiuseractinst

## 历史人工节点-主表 t_wf_hiuseractinst

- **表名称：** 历史人工节点-主表
- **表名：** t_wf_hiuseractinst

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fjoinflag | 汇聚标识 | varchar | 255 |  | √ | ' ' | 汇聚标识 |
| 3 | flastnodename | 上个节点名称 | varchar | 500 |  | √ | ' ' | 上个节点名称 |
| 4 | fcurrentactinstid | 当前节点的流程活动实例ID | int8 | 64 |  | √ | 0 | 当前节点的流程活动实例ID |
| 5 | flastnodecid | 上个节点的审批记录ID | int8 | 64 |  | √ | 0 | 上个节点的审批记录ID |
| 6 | fexecutionid | 上个人工节点执行实例Id | int8 | 64 |  | √ | 0 | 上个人工节点执行实例Id |
| 7 | fcurrentexecutionid | 当前节点执行实例Id | int8 | 64 |  | √ | 0 | 当前节点执行实例Id |
| 8 | fcurrentactid | 当前节点ID | varchar | 80 |  | √ | ' ' | 当前节点ID |
| 9 | flastusernodeactid | 上个人工节点ID | varchar | 80 |  | √ | ' ' | 上个人工节点ID |
| 10 | fcurrentnodename | 当前节点名称 | varchar | 500 |  | √ | ' ' | 当前节点名称 |
| 11 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 12 | fpathjson | 路径 | text | 0 |  |  | null | 路径 |
| 13 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 14 | fendtype | 结束类型 | varchar | 100 |  | √ | ' ' | 结束类型 |
| 15 | fbusinesskey | businesskey | varchar | 36 |  | √ | ' ' | businesskey |
| 16 | fproinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 17 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 18 | ftaskid | 当前任务Id | int8 | 64 |  | √ | 0 | 当前任务Id |
| 19 | flastnodeactinstid | 上个人工节点的流程活动实例ID | int8 | 64 |  | √ | 0 | 上个人工节点的流程活动实例ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_hiuseract_curinstid |  | fcurrentactinstid |
| 2 | t_wf_hiuseractinst_pkey |  | fid |
| 3 | idx_wf_hiuseractinst_procid |  | fproinstid |
| 4 | idx_wf_hiuseractinst_buskey |  | fbusinesskey |
| 5 | idx_wf_hiuseractinst_execid |  | fcurrentexecutionid |
| 6 | idx_wf_hiuseractinst_nodeid |  | fcurrentactid |

---

## 历史人工节点-多语言表 t_wf_hiuseractinst_l

- **表名称：** 历史人工节点-多语言表
- **表名：** t_wf_hiuseractinst_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcurrentnodename | 当前节点名称 | varchar | 500 |  | √ | ' ' | 当前节点名称 |
| 3 | flastnodename | 上个节点名称 | varchar | 500 |  | √ | ' ' | 上个节点名称 |
| 4 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_wf_hiuseractinst_l_pkey |  | fpkid |
| 2 | idx_wf_hiuseract_l_id_locid |  | fid,flocaleid |
