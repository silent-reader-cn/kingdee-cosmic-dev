# 航迹跟踪查询记录-lgm_shipservicelog

## 航迹跟踪查询记录-主表 t_lgm_shipservicelog

- **表名称：** 航迹跟踪查询记录-主表
- **表名：** t_lgm_shipservicelog

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ftransid | 事务ID | varchar | 50 |  | √ | ' ' | 事务ID |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 运输工具号 | varchar | 255 |  | √ | ' ' | 运输工具号 |
| 5 | fretcode | 返回代码 | varchar | 50 |  | √ | ' ' | 返回代码 |
| 6 | fcreatetime | 操作时间 | timestamp | 0 |  |  | null | 操作时间 |
| 7 | fservicetype | 查询类型 | varchar | 50 |  | √ | ' ' | 查询类型,枚举: getShipTrackInfo :实时船位 getShipInfo :船舶搜索 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 执行状态 | varchar | 50 |  | √ | ' ' | 执行状态,枚举: 0 :成功 1 :失败 |
| 10 | fcreatorid | 操作人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fshiptoolid | 运输工具 | int8 | 64 |  | √ | 0 | [运输工具档案 lgm_shiptool](../lgm_files/lgm_shiptool.md) |
| 12 | fresultcount | 返回记录数 | int4 | 32 |  | √ | 0 | 返回记录数 |
| 13 | fendtime | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 14 | fbegtime | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_lgm_shipservicelog |  | fid |
| 2 | idx_lgm_shipservlog_shiptid |  | fshiptoolid |
