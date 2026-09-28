# 区域-cts_zone

## 区域-多语言表 t_cts_zone_l

- **表名称：** 区域-多语言表
- **表名：** t_cts_zone_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 1023 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cts_zone_l |  | fpkid |
| 2 | idx_t_cts_zone_l_fid |  | fid |

---

## 区域-主表 t_cts_zone

- **表名称：** 区域-主表
- **表名：** t_cts_zone

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fparentid | 上级区域 | int8 | 64 |  | √ | 0 | [区域 cts_zone](../cts_files/cts_zone.md) |
| 6 | ffullname | 长名称 | varchar | 1023 |  | √ | ' ' | 长名称 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 9 | fconditionjson | 地址过滤条件 | text | 0 |  |  | null | 地址过滤条件 |
| 10 | fzonetype | 区域类型 | int8 | 64 |  | √ | 0 | [区域类型 cts_zonetype_config](../cts_files/cts_zonetype_config.md) |
| 11 | fstarttime | 起止日期.开始 | timestamp | 0 |  |  | null | 起止日期.开始 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 14 | fstatus | 数据状态 | varchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 17 | fissystem | 系统预置 | int4 | 32 |  | √ | 0 | 系统预置 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 20 | fendtime | 起止日期.结束 | timestamp | 0 |  |  | null | 起止日期.结束 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cts_zone_fnum |  | fnumber |
| 2 | pk_t_cts_zone |  | fid |
