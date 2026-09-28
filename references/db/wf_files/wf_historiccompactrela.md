# 历史流程压缩关联-wf_historiccompactrela

## 历史流程压缩关联-主表 t_wf_hiproccompactrel

- **表名称：** 历史流程压缩关联-主表
- **表名：** t_wf_hiproccompactrel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |
| 3 | fentitynumber | 实体编码 | varchar | 36 |  | √ | ' ' | 实体编码 |
| 4 | fprocinstid | 流程实例ID | int8 | 64 |  | √ | 0 | 流程实例ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_wf_hiproccompactrel |  | fid |
| 2 | idx_wf_hiproccomprel_buskey |  | fbusinesskey,fentitynumber |
| 3 | idx_wf_hiproccomprel_procinst |  | fprocinstid |
