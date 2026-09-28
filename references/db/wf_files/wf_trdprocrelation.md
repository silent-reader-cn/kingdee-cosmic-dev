# 流程与第三方关联关系-wf_trdprocrelation

## 流程与第三方关联关系-主表 t_wf_trdprocrelation

- **表名称：** 流程与第三方关联关系-主表
- **表名：** t_wf_trdprocrelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frelationvalue | 关联字段值 | varchar | 50 |  | √ | ' ' | 关联字段值 |
| 3 | fcommentid | 审批意见ID | int8 | 64 |  | √ | 0 | 审批意见ID |
| 4 | ftype | 类型 | varchar | 15 |  | √ | ' ' | 类型,枚举: |
| 5 | factinstid | 活动实例ID | int8 | 64 |  | √ | 0 | 活动实例ID |
| 6 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 7 | fentitynumber | 实体编码 | varchar | 36 |  | √ | ' ' | 实体编码 |
| 8 | factivityid | 节点ID | varchar | 255 |  | √ | ' ' | 节点ID |
| 9 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_wf_trdprocrel_procactinst |  | fprocinstid,factinstid |
| 2 | idx_wf_trdprocrel_relvaltype |  | frelationvalue,ftype |
| 3 | idx_wf_trdprocrel_buskeyenty |  | fbusinesskey,fentitynumber |
| 4 | pk_wf_trdprocrelation |  | fid |
