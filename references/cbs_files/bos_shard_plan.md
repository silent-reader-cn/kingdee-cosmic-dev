# 分片计划表-bos_shard_plan

## 分片计划表-主表 t_bas_shardplan

- **表名称：** 分片计划表-主表
- **表名：** t_bas_shardplan

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fbillstatus | 单据状态 | varchar | 30 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fentitynumber | 分片目标 | varchar | 50 |  | √ | ' ' | 分片目标 |
| 6 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 7 | fshard_table | 分表名 | varchar | 50 |  | √ | ' ' | 分表名 |
| 8 | fshard_total_record | 预估数量 | int8 | 64 |  | √ | 0 | 预估数量 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 11 | fshard_moving_record | 已迁移数量 | int8 | 64 |  | √ | 0 | 已迁移数量 |
| 12 | fbillno | 单据编号 | varchar | 30 |  | √ | ' ' | 单据编号 |
| 13 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fshard_progess | 进度 | varchar | 50 |  | √ | ' ' | 进度 |
| 15 | fshard_index | 分表后缀 | varchar | 50 |  | √ | ' ' | 分表后缀 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bas_shardplan_pkey |  | fid |
| 2 | idx_bas_shardplan |  | fbillno |
