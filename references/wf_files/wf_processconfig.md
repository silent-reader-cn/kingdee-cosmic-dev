# 流程配置-wf_processconfig

## 流程配置-主表 t_wf_processconfig

- **表名称：** 流程配置-主表
- **表名：** t_wf_processconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fallowstart | 允许启动 | bpchar | 1 |  | √ | '1' | 允许启动 |
| 3 | fbatchnumname | 批次号名称(表达式返回值为单语种) | varchar | 500 |  | √ | ' ' | 批次号名称(表达式返回值为单语种) |
| 4 | fbatchnumber | 批次号编码 | varchar | 500 |  | √ | ' ' | 批次号编码 |
| 5 | fprocdefid | 流程定义ID | int8 | 64 |  | √ | 0 | 流程定义ID |
| 6 | fentitynumber | 实体编码 | varchar | 36 |  | √ | ' ' | 实体编码 |
| 7 | fprocesstype | 流程类型 | varchar | 30 |  | √ | 'AuditFlow' | 流程类型,枚举: AuditFlow :审批流 BizFlow :业务流 |
| 8 | fcondruleid | 条件规则ID | int8 | 64 |  | √ | 0 | 条件规则ID |
| 9 | fstarttype | 启动类型 | varchar | 30 |  | √ | 'operation' | 启动类型,枚举: event :事件启动 operation :操作启动 |
| 10 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 11 | fisallownextperson | 启动流程时是否允许指定下一步参与人 | bpchar | 1 |  | √ | '0' | 启动流程时是否允许指定下一步参与人 |
| 12 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | feventnumber | 事件编码 | varchar | 50 |  | √ | ' ' | 事件编码 |
| 14 | fexceptionconfig | 异常配置 | varchar | 2000 |  | √ | ' ' | 异常配置 |
| 15 | fenable | 流程使用状态 | bpchar | 1 |  | √ | '0' | 流程使用状态 |
| 16 | fstartcondition | 启动条件 | text | 0 |  |  | null | 启动条件 |
| 17 | foperation | 操作编码 | varchar | 300 |  | √ | ' ' | 操作编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_processcfg_pdef |  | fprocdefid |
| 2 | t_wf_processconfig_pkey |  | fid |
| 3 | idx_wf_processcfg_enti_oper |  | fentitynumber,foperation,fisallownextperson,fenable |
