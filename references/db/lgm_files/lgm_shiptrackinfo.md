# 航迹跟踪-lgm_shiptrackinfo

## 航迹跟踪-主表 t_lgm_shiptrackinfo

- **表名称：** 航迹跟踪-主表
- **表名：** t_lgm_shiptrackinfo

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | null | id |
| 2 | ftransid | 事务ID | varchar | 50 |  | √ | ' ' | 事务ID |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ftracktime | 更新时间戳 | int8 | 64 |  |  | null | 更新时间戳 |
| 5 | fheading | 船首向 | int4 | 32 |  | √ | 0 | 船首向 |
| 6 | fdest | 目的地 | varchar | 255 |  | √ | ' ' | 目的地 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fdestcode | 目的港代码 | varchar | 255 |  | √ | ' ' | 目的港代码 |
| 9 | ftrackdatetime | 更新时间 | timestamp | 0 |  |  | null | 更新时间 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fdeststd | 标准化后的目的地 | varchar | 255 |  | √ | ' ' | 标准化后的目的地 |
| 12 | fetastd | 预到时间 | timestamp | 0 |  |  | null | 预到时间 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fshiptoolid | 运输工具号 | int8 | 64 |  | √ | 0 | [运输工具档案 lgm_shiptool](../lgm_files/lgm_shiptool.md) |
| 15 | fspeed | 航速（mm/s） | numeric | 23 | 10 | √ | 0 | 航速（mm/s） |
| 16 | flongitude | 经度 | int8 | 64 |  |  | null | 经度 |
| 17 | fshipstate | 航行状态 | varchar | 50 |  | √ | ' ' | 航行状态,枚举: SE0 :在行 SE1 :锚泊 SE2 :失控 SE3 :操纵受限 SE4 :吃水受限 SE5 :靠泊 SE6 :搁浅 SE7 :捕捞作业 SE8 :靠帆船提供动力 |
| 18 | flatitude | 纬度 | int8 | 64 |  |  | null | 纬度 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_lgm_shiptrackinfo_trktim |  | ftracktime |
| 2 | idx_lgm_shiptrackinfo_shipid |  | fshiptoolid |
| 3 | pk_lgm_shiptrackinfo |  | fid |
