# 台账编辑调整记录-tcret_tz_adj_record

## 台账编辑调整记录-主表 t_tcret_tz_adj_record

- **表名称：** 台账编辑调整记录-主表
- **表名：** t_tcret_tz_adj_record

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsubbizid | 调整表业务子表id | int8 | 64 |  | √ | 0 | 调整表业务子表id |
| 3 | faftervalue | 变更后 | varchar | 50 |  | √ | ' ' | 变更后 |
| 4 | fbiztable | 调整业务表 | varchar | 50 |  | √ | ' ' | 调整业务表 |
| 5 | fbizrowtype | 变更行类型 | varchar | 50 |  | √ | ' ' | 变更行类型 |
| 6 | fupdatetime | 变更时间 | timestamp | 0 |  |  | null | 变更时间 |
| 7 | fupdateor | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fbizid | 调整表业务id | int8 | 64 |  | √ | 0 | 调整表业务id |
| 9 | fbeforevalue | 变更前 | varchar | 50 |  | √ | ' ' | 变更前 |
| 10 | fbizfield | 变更字段 | varchar | 50 |  | √ | ' ' | 变更字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_tcret_tz_adj_record |  | fid |
| 2 | idx_tcret_tz_adj_record |  | fbizid,fbizfield |
