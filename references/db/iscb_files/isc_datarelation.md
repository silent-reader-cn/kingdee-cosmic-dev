# 数据对照（废弃）-isc_datarelation

## 数据对照（废弃）-多语言表 t_isc_datarelation_l

- **表名称：** 数据对照（废弃）-多语言表
- **表名：** t_isc_datarelation_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_datarelation_l_pkey |  | fpkid |
| 2 | idx_isc_datare_l_fid |  | fid |

---

## 数据对照（废弃）-主表 t_isc_datarelation

- **表名称：** 数据对照（废弃）-主表
- **表名：** t_isc_datarelation

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fsystem_2 | 目标系统 | int8 | 64 |  | √ | 0 | 外部集成信息（废弃） isc_sysconn |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fguide | 集成方案 | int8 | 64 |  | √ | 0 | 集成方案（废弃） isc_guide |
| 6 | fmd5uniqueflag | MD5值 | varchar | 32 |  | √ | ' ' | MD5值 |
| 7 | fsystem_1 | 源系统 | int8 | 64 |  | √ | 0 | 外部集成信息（废弃） isc_sysconn |
| 8 | forigsystemvalue | 源系统值 | varchar | 300 |  | √ | ' ' | 源系统值 |
| 9 | ftargetsystemkey | 目标系统标识 | varchar | 300 |  | √ | ' ' | 目标系统标识 |
| 10 | fnext_id | 下一代id | varchar | 100 |  | √ | ' ' | 下一代id |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fsystementity_2 | 目标实体 | varchar | 80 |  | √ | ' ' | 主实体对象 bos_entityobject |
| 13 | ftargetsystemvalue | 目标系统值 | varchar | 300 |  | √ | ' ' | 目标系统值 |
| 14 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 15 | fsystementity_1 | 源系统实体 | int8 | 64 |  | √ | 0 | 集成业务对象（废弃） isc_entity |
| 16 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 18 | forigsystemkey | 源系统唯一标识 | varchar | 300 |  | √ | ' ' | 源系统唯一标识 |
| 19 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 20 | fnextcloud | 集成到当前系统 | bpchar | 1 |  | √ | '0' | 集成到当前系统 |
| 21 | fdirection | 数据集成方向 | varchar | 100 |  | √ | ' ' | 数据集成方向 |
| 22 | fnumber | 编码 | varchar | 200 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_tarvalue |  | ftargetsystemvalue |
| 2 | idx_isc_orivalue |  | forigsystemvalue |
| 3 | t_isc_datarelation_pkey |  | fid |
| 4 | idx_isc_nextid |  | fnext_id |
| 5 | uk_isc_datare_key |  | fmd5uniqueflag |
