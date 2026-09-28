# 反写快照_业务跟踪-botp_snapshot_tc

## 反写快照_业务跟踪-主表 t_botp_entrytracker

- **表名称：** 反写快照_业务跟踪-主表
- **表名：** t_botp_entrytracker

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftbillid | 目标单单据内码 | int8 | 64 |  | √ | 0 | 目标单单据内码 |
| 3 | fttableid | 目标单主实体表格编码 | int8 | 64 |  | √ | 0 | 目标单主实体表格编码 |
| 4 | fsbillid | 源单单据内码 | int8 | 64 |  |  | null | 源单单据内码 |
| 5 | fstableid | 源单主实体表格编码 | int8 | 64 |  |  | null | 源单主实体表格编码 |
| 6 | fsid | 源单主实体内码 | int8 | 64 |  |  | null | 源单主实体内码 |
| 7 | ftid | 目标单主实体内码 | int8 | 64 |  | √ | 0 | 目标单主实体内码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_botp_entrytracker_sid |  | fsbillid |
| 2 | t_botp_entrytracker_pkey |  | fid |
| 3 | idx_botp_entrytracker_tid |  | ftbillid |
