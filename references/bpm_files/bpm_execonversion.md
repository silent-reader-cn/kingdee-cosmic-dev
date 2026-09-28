# 实例转换-bpm_execonversion

## 实例转换-主表 t_bpm_execonversion

- **表名称：** 实例转换-主表
- **表名：** t_bpm_execonversion

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsrcbusinesskey | 原业务主键 | varchar | 36 |  | √ | ' ' | 原业务主键 |
| 3 | fsrcexecutionid | 原executionId | int8 | 64 |  | √ | 0 | 原executionId |
| 4 | factivityid | 转换节点 | varchar | 255 |  | √ | ' ' | 转换节点 |
| 5 | fprocinstid | 流程实例id | int8 | 64 |  | √ | 0 | 流程实例id |
| 6 | fsrcentitynumber | 原实体编码 | varchar | 50 |  | √ | ' ' | 原实体编码 |
| 7 | ftagexecutionid | executionId | int8 | 64 |  | √ | 0 | executionId |
| 8 | ftagentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 9 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 10 | ftype | 转换类型 | varchar | 50 |  | √ | ' ' | 转换类型 |
| 11 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbizcode | 批次号 | varchar | 200 |  | √ | ' ' | 批次号 |
| 13 | ftagbusinesskey | 业务主键 | varchar | 36 |  | √ | ' ' | 业务主键 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bpm_execonver_proctag |  | fprocinstid,ftagentitynumber,ftagbusinesskey |
| 2 | pk_t_bpm_execonversion |  | fid |
| 3 | idx_bpm_execonver_tagbus |  | ftagbusinesskey |
