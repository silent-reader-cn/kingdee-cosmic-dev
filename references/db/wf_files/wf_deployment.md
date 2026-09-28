# 流程部署-wf_deployment

## 流程部署-主表 t_wf_deployment

- **表名称：** 流程部署-主表
- **表名：** t_wf_deployment

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 部署名称 | varchar | 50 |  | √ | ' ' | 部署名称 |
| 3 | fcategory | 类别 | varchar | 50 |  | √ | ' ' | 类别 |
| 4 | fdeploytime | 部署时间 | timestamp | 0 |  |  | null | 部署时间 |
| 5 | fnumber | 流程模型编码 | varchar | 50 |  | √ | ' ' | 流程模型编码 |
| 6 | fengineversion | 引擎版本 | varchar | 36 |  | √ | ' ' | 引擎版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_deployment_number |  | fnumber |
| 2 | t_wf_deployment_pkey |  | fid |
