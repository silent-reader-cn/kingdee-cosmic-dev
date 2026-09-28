# 数据同步配置-data_sync_config

## 数据同步配置-主表 t_dts_datasyncconfig

- **表名称：** 数据同步配置-主表
- **表名：** t_dts_datasyncconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 3 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 4 | fentitynumber | 实体对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 5 | fentityfields | 同步字段 | varchar | 1000 |  | √ | ' ' | 同步字段,枚举: |
| 6 | fbusinesstype | 场景类型 | varchar | 100 |  | √ | ' ' | 场景类型,枚举: |
| 7 | fen | fen | varchar | 30 |  | √ | ' ' |  |
| 8 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 9 | fmappingrule | 映射规则 | varchar | 300 |  | √ | ' ' | 映射规则 |
| 10 | ftimingsequence | 时序字段 | varchar | 100 |  | √ | ' ' | 时序字段,枚举: |
| 11 | fstatus | fstatus | varchar | 200 |  | √ | ' ' |  |
| 12 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 13 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 14 | fregion | 目标地址 | varchar | 100 |  | √ | ' ' | 目标地址,枚举: |
| 15 | fenable | 是否启用 | bpchar | 1 |  | √ | ' ' | 是否启用 |
| 16 | ftables | ftables | varchar | 500 |  | √ | ' ' |  |
| 17 | fnumber | fnumber | varchar | 30 |  | √ | ' ' |  |
| 18 | fdestinationtype | 目标类型 | varchar | 30 |  | √ | ' ' | 目标类型,枚举: fulltext :全文索引(elasticsearch) mongodb :mongodb businessdb :业务数据库 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_unique_entity_dest_region_mapping |  | fentitynumber,fdestinationtype,fregion,fmappingrule |
| 2 | idx_dts_datasyncconfig |  | fentitynumber |
| 3 | pk_dts_datasyncconfig |  | fid |
