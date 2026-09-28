# 被引用的实体-ais_entity_cfg_ref

## 被引用的实体-主表 t_ais_entity_cfg_ref

- **表名称：** 被引用的实体-主表
- **表名：** t_ais_entity_cfg_ref

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flastsyntime | 上一次完成同步时间 | varchar | 14 |  | √ | ' ' | 上一次完成同步时间 |
| 3 | fstatus | 同步状态 | varchar | 10 |  | √ | ' ' | 同步状态 |
| 4 | flastsyntimecustom | 上一次完成同步时间 | timestamp | 0 |  |  | null | 上一次完成同步时间 |
| 5 | fentitynumber | 实体对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fenable | 状态 | bpchar | 1 |  | √ | ' ' | 状态 |
| 7 | fentityfield | 可搜索字段 | varchar | 200 |  | √ | ' ' | 可搜索字段,枚举: |
| 8 | fdtsid | DTS表的内码 | int8 | 64 |  | √ | 0 | DTS表的内码 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fbizappid | 所属应用的内码 | varchar | 50 |  | √ | ' ' | 所属应用的内码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ais_entity_cfg_ref_pkey |  | fid |
| 2 | idx_t_ais_entity_cfg_refnum |  | fentitynumber |
