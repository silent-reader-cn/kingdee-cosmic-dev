# 流程资源关系-wf_resourcerelation

## 流程资源关系-主表 t_wf_resourcerelation

- **表名称：** 流程资源关系-主表
- **表名：** t_wf_resourcerelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnewversion | 新流程版本 | varchar | 36 |  | √ | ' ' | 新流程版本 |
| 3 | fnewmodelid | 新流程模型Id | int8 | 64 |  | √ | 0 | 新流程模型Id |
| 4 | fnewprocdefid | 新流程定义Id | int8 | 64 |  | √ | 0 | 新流程定义Id |
| 5 | forigversion | 原流程版本 | varchar | 36 |  | √ | ' ' | 原流程版本 |
| 6 | fnewresourceid | 新流程资源Id | int8 | 64 |  | √ | 0 | 新流程资源Id |
| 7 | fprocnumber | 流程编码 | varchar | 255 |  | √ | ' ' | 流程编码 |
| 8 | forigresourceid | 原流程资源Id | int8 | 64 |  | √ | 0 | 原流程资源Id |
| 9 | forigprocdefid | 原流程定义Id | int8 | 64 |  | √ | 0 | 原流程定义Id |
| 10 | forigmodelid | 原流程模型Id | int8 | 64 |  | √ | 0 | 原流程模型Id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_resrelation_newprocdef |  | fnewprocdefid |
| 2 | t_wf_resourcerelation_pkey |  | fid |
| 3 | idx_wf_resourcerelation |  | fprocnumber,forigversion |
