# 基础资料同步配置-cbs_bdsync_config

## 基础资料同步配置-主表 t_cbs_bdsyncconfig

- **表名称：** 基础资料同步配置-主表
- **表名：** t_cbs_bdsyncconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftimingsequence | 时序字段 | varchar | 255 |  | √ | ' ' | 时序字段,枚举: |
| 3 | ftargetroute | 目标业务库 | varchar | 255 |  | √ | ' ' | 目标业务库,枚举: |
| 4 | frelationtableinfo | 关联表信息 | varchar | 50 |  | √ | ' ' | 关联表信息 |
| 5 | fentitynumber | 实体名称 | varchar | 255 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用 |
| 7 | fsyncstatus | 同步状态 | varchar | 50 |  | √ | ' ' | 同步状态,枚举: FINISHED :已同步 RUNNING :同步中 FAILED :同步失败 UNCONFIG :未配置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cbs_bdsyncconfig |  | fid |
| 2 | idx_cbs_bdsyncconfig |  | fentitynumber |
