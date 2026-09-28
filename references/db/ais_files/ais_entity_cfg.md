# 全局搜索对象-ais_entity_cfg

## 全局搜索对象-主表 t_ais_entity_cfg

- **表名称：** 全局搜索对象-主表
- **表名：** t_ais_entity_cfg

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flastsyntime | 上一次完成同步时间 | varchar | 14 |  | √ | ' ' | 上一次完成同步时间 |
| 3 | fstatus | 同步状态 | varchar | 10 |  | √ | ' ' | 同步状态,枚举: A :创建 B :审核中 C :已审核 D :重新审核 disable :禁用 done :可用 ing :同步中 |
| 4 | fautoactivate | 是否已自动激活 | bpchar | 1 |  | √ | '1' | 是否已自动激活 |
| 5 | flastsyntimecustom | 上一次完成同步时间 | timestamp | 0 |  |  | null | 上一次完成同步时间 |
| 6 | fcreater | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fentitynumber | 业务对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 8 | fenable | 状态 | bpchar | 1 |  | √ | ' ' | 状态 |
| 9 | fentityfield | 可搜索字段 | varchar | 200 |  | √ | ' ' | 可搜索字段,枚举: |
| 10 | fdtsid | DTS表的内码 | int8 | 64 |  | √ | 0 | DTS表的内码 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fbizappid | 所属应用的内码 | varchar | 50 |  | √ | ' ' | 所属应用的内码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ais_entity_cfg_pkey |  | fid |
| 2 | idx_t_ais_entity_cfg_entitynum |  | fentitynumber |
| 3 | idx_t_ais_entity_cfg_e_st_mt |  | fenable,fstatus,fmodifytime |
