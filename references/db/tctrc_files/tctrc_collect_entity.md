# 风险收藏实体-tctrc_collect_entity

## 风险收藏实体-主表 t_tctrc_collect_entity

- **表名称：** 风险收藏实体-主表
- **表名：** t_tctrc_collect_entity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftime | 收藏时间 | timestamp | 0 |  |  | null | 收藏时间 |
| 3 | frisknumber | 风险编号 | int8 | 64 |  | √ | 0 | 风险编号 |
| 4 | fuser | 收藏用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | friskname | 风险名称 | varchar | 100 |  | √ | ' ' | 风险名称 |
| 6 | fcollectexplain | fcollectexplain | varchar | 510 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_tctrc_collect_entity_pkey |  | fid |
| 2 | idx_tctrc_collect_entity_id |  | frisknumber,fuser |
