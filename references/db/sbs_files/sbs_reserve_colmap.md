# 字段映射（旧）（废弃）-sbs_reserve_colmap

## 字段映射（旧）（废弃）-主表 t_sbs_reserve_colmap

- **表名称：** 字段映射（旧）（废弃）-主表
- **表名：** t_sbs_reserve_colmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | freservebill | 预留单据 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fcreaterid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fcolmap | 字段对应关系 | varchar | 2000 |  | √ | ' ' | 字段对应关系 |
| 8 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 1 :启用 0 :禁用 |
| 9 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 10 | frequirebill | 需求单据 | varchar | 50 |  | √ | ' ' | 主实体对象 bos_entityobject |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_sbs_rs_cm_fbid |  | freservebill,frequirebill |
| 2 | idx_sbs_rs_cm_fno |  | fnumber |
| 3 | t_sbs_reserve_colmap_pkey |  | fid |
