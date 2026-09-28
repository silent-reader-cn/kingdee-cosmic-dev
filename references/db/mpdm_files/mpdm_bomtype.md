# BOM类型-mpdm_bomtype

## BOM类型-主表 t_mpdm_bomtype

- **表名称：** BOM类型-主表
- **表名：** t_mpdm_bomtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fissalebom | 订单BOM | bpchar | 1 |  | √ | '0' | 订单BOM |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fismfg | fismfg | bpchar | 1 |  | √ | '0' |  |
| 8 | fispackage | fispackage | bpchar | 1 |  | √ | '0' |  |
| 9 | fisprocess | fisprocess | bpchar | 1 |  | √ | '0' |  |
| 10 | fissales | fissales | bpchar | 1 |  | √ | '0' |  |
| 11 | fistool | fistool | bpchar | 1 |  | √ | '0' |  |
| 12 | fisecnupdate | ECN修改(废弃) | bpchar | 1 |  | √ | '0' | ECN修改(废弃) |
| 13 | fisinsloc | 安装位置 | bpchar | 1 |  | √ | '0' | 安装位置 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 16 | fisparts | fisparts | bpchar | 1 |  | √ | '0' |  |
| 17 | fisversionvalid | 版本同时有效 | bpchar | 1 |  | √ | '0' | 版本同时有效 |
| 18 | fisecnversion | ECN版本 | bpchar | 1 |  | √ | '0' | ECN版本 |
| 19 | fissyspre | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 20 | fisstandard | 标准BOM | bpchar | 1 |  | √ | '0' | 标准BOM |
| 21 | fissuperbom | 配置BOM | bpchar | 1 |  | √ | '0' | 配置BOM |
| 22 | fiscost | fiscost | bpchar | 1 |  | √ | '0' |  |
| 23 | fisversion | fisversion | bpchar | 1 |  | √ | '0' |  |
| 24 | fisdesign | fisdesign | bpchar | 1 |  | √ | '0' |  |
| 25 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 27 | fisdefault | 默认类型 | bpchar | 1 |  | √ | '0' | 默认类型 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mpdm_bomtype_fnumber |  | fnumber |
| 2 | t_mpdm_bomtype_pkey |  | fid |

---

## BOM类型-多语言表 t_mpdm_bomtype_l

- **表名称：** BOM类型-多语言表
- **表名：** t_mpdm_bomtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_mpdm_bomtype_l_pkey |  | fpkid |
| 2 | idx_mpdm_bomtype_l |  | fid,flocaleid |
