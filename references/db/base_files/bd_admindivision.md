# 行政区划-bd_admindivision

## 行政区划-多语言表 t_bd_admindivision_l

- **表名称：** 行政区划-多语言表
- **表名：** t_bd_admindivision_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 1024 |  | √ | ' ' | 长名称 |
| 4 | fsimplename | fsimplename | varchar | 255 |  | √ | ' ' |  |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 7 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_admindivision_l_pkey |  | fpkid |
| 2 | idx_t_bd_admindivision_l_id |  | fid,flocaleid |
| 3 | idx_t_bd_admindivision_l_name |  | fname |

---

## 行政区划-主表 t_bd_admindivision

- **表名称：** 行政区划-主表
- **表名：** t_bd_admindivision

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 3 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fcitynumber | 电话区号 | varchar | 80 |  | √ | ' ' | 电话区号 |
| 6 | fiscity | 城市 | bpchar | 1 |  | √ | ' ' | 城市 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置 |
| 11 | fareacode | 参考码 | varchar | 10 |  | √ | ' ' | 参考码 |
| 12 | ftimezone | 时区 | int8 | 64 |  | √ | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 13 | fsimplespell | 英文简称 | varchar | 255 |  | √ | ' ' | 英文简称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 16 | fparentid | 上级行政区划 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 17 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 18 | ffullname | 长名称 | varchar | 1024 |  | √ | ' ' | 长名称 |
| 19 | flongnumber | 长编码 | varchar | 255 |  | √ | ' ' | 长编码 |
| 20 | fcountryid | 所属国家或地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 21 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 22 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 23 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 24 | ffullspell | 英文全称 | varchar | 255 |  | √ | ' ' | 英文全称 |
| 25 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 26 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 27 | fadmindivisionlvid | 行政级次 | int8 | 64 |  | √ | 0 | [行政级次 bd_admindivisionlevel](../base_files/bd_admindivisionlevel.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_admindivis_num |  | fnumber |
| 2 | idx_bd_admindivis_counrynum |  | fcountryid,fnumber |
| 3 | idx_bd_admindivis_parent |  | fparentid,fnumber |
| 4 | t_bd_admindivision_pkey |  | fid |
| 5 | idx_bd_admindivis_name |  | fname |
