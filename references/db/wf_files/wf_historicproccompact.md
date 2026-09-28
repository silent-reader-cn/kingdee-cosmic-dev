# 历史流程数据压缩-wf_historicproccompact

## 历史流程数据压缩-主表 t_wf_hiproccompact

- **表名称：** 历史流程数据压缩-主表
- **表名：** t_wf_hiproccompact

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | factinfo | 活动实例信息 | text | 0 |  |  | null | 活动实例信息 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 5 | fbiztraceno | 业务跟踪号 | varchar | 255 |  | √ | ' ' | 业务跟踪号 |
| 6 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 7 | fentitynumber | 实体编码 | varchar | 36 |  | √ | ' ' | 实体编码 |
| 8 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 9 | fprocesstype | 流程类型 | varchar | 30 |  | √ | 'AuditFlow' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 10 | foperationlog | 操作日志 | text | 0 |  |  | null | 操作日志 |
| 11 | fbillno | 单据编码 | varchar | 255 |  | √ | ' ' | 单据编码 |
| 12 | fhiparticipant | 历史参与人 | text | 0 |  |  | null | 历史参与人 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_hiproccompact_buskey |  | fbusinesskey,fentitynumber |
| 2 | idx_wf_hiproccompact_procinst |  | fprocinstid |
| 3 | idx_wf_hiproccompact_billno |  | fbillno |
| 4 | pk_wf_hiproccompact |  | fid |
| 5 | idx_wf_hiproccompact_procdef |  | fprocdefid |
