# 第三方数据源信息记录-wf_trddatasourcerecord

## 第三方数据源信息记录-主表 t_wf_trddatasourcerecord

- **表名称：** 第三方数据源信息记录-主表
- **表名：** t_wf_trddatasourcerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcallactivityid | 子流程节点ID | varchar | 255 |  | √ | ' ' | 子流程节点ID |
| 3 | fcreatedate | 创建日期 | timestamp | 0 |  |  | null | 创建日期 |
| 4 | fcallexecutionid | 子执行实例ID | int8 | 64 |  | √ | 0 | 子执行实例ID |
| 5 | fsourcetype | 来源类型 | varchar | 50 |  | √ | ' ' | 来源类型 |
| 6 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 7 | fsourcedetailsjson | 来源详情 | varchar | 2000 |  | √ | ' ' | 来源详情 |
| 8 | fsuperprocinstid | 父流程实例ID | int8 | 64 |  | √ | 0 | 父流程实例ID |
| 9 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 10 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |
| 11 | fparentflag | 父子端标志 | varchar | 10 |  | √ | ' ' | 父子端标志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_trddatasrcrcd_billproc |  | fbusinesskey,fentitynumber,fprocinstid |
| 2 | pk_wf_trddatasourcerecord |  | fid |
| 3 | idx_wf_trddatasrcrcd_callexe |  | fcallexecutionid |
| 4 | idx_wf_trddatasrcrcd_procinst |  | fprocinstid |
| 5 | idx_wf_trddatasrcrcd_superproc |  | fsuperprocinstid |
