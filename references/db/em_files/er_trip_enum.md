# 商旅字段枚举-er_trip_enum

## 商旅字段枚举-主表 t_er_trip_enum

- **表名称：** 商旅字段枚举-主表
- **表名：** t_er_trip_enum

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fbillfield | 单据字段（废弃） | varchar | 255 |  | √ | ' ' | 单据字段（废弃） |
| 6 | ffunction | 星翰对接功能 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fbillvalue | 单据值（废弃） | varchar | 50 |  | √ | ' ' | 单据值（废弃） |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | varchar | 10 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | fserver | 服务商 | int8 | 64 |  | √ | 0 | [服务商设置 er_biz_info](../em_files/er_biz_info.md) |
| 13 | fjsonvalue | 报文值（废弃） | varchar | 255 |  | √ | ' ' | 报文值（废弃） |
| 14 | fenable | 使用状态 | varchar | 10 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 16 | fjsonfield | 报文字段（废弃） | varchar | 255 |  | √ | ' ' | 报文字段（废弃） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_trip_enum |  | fid |
| 2 | uq_enumserverjsonfield |  | fserver,ffunction,fjsonfield |

---

## 单据体-子表 t_er_trip_enum_entry

- **表名称：** 单据体-子表
- **表名：** t_er_trip_enum_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjvalue | 报文值 | varchar | 255 |  | √ | ' ' | 报文值 |
| 3 | fbvalue | 单据值 | varchar | 255 |  | √ | ' ' | 单据值 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fbfield | 单据字段 | varchar | 255 |  | √ | ' ' | 单据字段 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fjfield | 报文字段 | varchar | 255 |  | √ | ' ' | 报文字段 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | uq_trip_enum_fid |  | fid,fjfield,fjvalue,fbfield |
| 2 | pk_t_er_trip_enum_entry |  | fentryid |

---

## 商旅字段枚举-多语言表 t_er_trip_enum_l

- **表名称：** 商旅字段枚举-多语言表
- **表名：** t_er_trip_enum_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 50 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_trip_enumfid |  | fid |
| 2 | pk_t_er_trip_enum_l |  | fpkid |
