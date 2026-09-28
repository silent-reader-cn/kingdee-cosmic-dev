# 插件执行记录-wf_pluginexedetail

## 插件执行记录-主表 t_wf_pluginexedetail

- **表名称：** 插件执行记录-主表
- **表名：** t_wf_pluginexedetail

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftraceid | traceId | varchar | 100 |  | √ | ' ' | traceId |
| 3 | fjobid | JobId | int8 | 64 |  | √ | 0 | JobId |
| 4 | fprocessno | 流程编码 | varchar | 50 |  | √ | ' ' | 流程编码 |
| 5 | fprocinstid | 流程实例id | int8 | 64 |  | √ | 0 | 流程实例id |
| 6 | felementid | 节点编码 | varchar | 255 |  | √ | ' ' | 节点编码 |
| 7 | fcreatedate | 开始执行时间 | timestamp | 0 |  |  | null | 开始执行时间 |
| 8 | fduration | 执行耗时(s) | int8 | 64 |  | √ | 0 | 执行耗时(s) |
| 9 | fexecutor | 执行机(Ip地址) | varchar | 255 |  | √ | ' ' | 执行机(Ip地址) |
| 10 | fbusinesskey | 业务单据Id | varchar | 36 |  | √ | ' ' | 业务单据Id |
| 11 | fpluginno | 插件编码 | varchar | 255 |  | √ | ' ' | 插件编码 |
| 12 | fendtime | 执行完成时间 | timestamp | 0 |  |  | null | 执行完成时间 |
| 13 | fpluginname | 插件名称 | varchar | 500 |  | √ | ' ' | 插件名称 |
| 14 | fbillno | 单据编号 | varchar | 255 |  | √ | ' ' | 单据编号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_pluginexedetl_jobid |  | fjobid |
| 2 | idx_wf_pluginexedetl_procinst |  | fprocinstid |
| 3 | pk_wf_pluginexedetail |  | fid |
| 4 | idx_wf_pluginexedetl_creadate |  | fcreatedate |
| 5 | idx_wf_pluginexedetl_pluginno |  | fpluginno |
| 6 | idx_wf_pluginexedetl_buskey |  | fbusinesskey |
| 7 | idx_wf_pluginexedetl_procno |  | fprocessno |

---

## 插件执行记录-多语言表 t_wf_pluginexedetail_l

- **表名称：** 插件执行记录-多语言表
- **表名：** t_wf_pluginexedetail_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fpluginname | 插件名称 | varchar | 500 |  | √ | ' ' | 插件名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_pluginexedetail_l |  | fpkid |
| 2 | idx_wf_pluginexedetail_l |  | fid,flocaleid |
