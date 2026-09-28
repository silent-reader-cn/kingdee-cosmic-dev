# 国家和地区-bd_country

## 国家和地区-主表 t_bd_country

- **表名称：** 国家和地区-主表
- **表名：** t_bd_country

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifyorgid | fmodifyorgid | int8 | 64 |  | √ | 0 |  |
| 3 | flogo | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 4 | fformatplanid | 区域格式 | int8 | 64 |  | √ | 0 | [区域格式 inte_programme](../base_files/inte_programme.md) |
| 5 | ftwocountrycode | 二字码 | varchar | 10 |  | √ | ' ' | 二字码 |
| 6 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 7 | fregionalformat | 区域格式 | int8 | 64 |  | √ | 0 | [区域格式 inte_programme](../base_files/inte_programme.md) |
| 8 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fissystem | 是否系统预置 | bpchar | 1 |  | √ | '0' | 是否系统预置,枚举: 1 :是 0 :否 |
| 14 | fareacode | 国际电话区号 | varchar | 10 |  | √ | ' ' | 国际电话区号 |
| 15 | ftimezone | 时区 | int8 | 64 |  | √ | 0 | [时区 inte_timezone](../base_files/inte_timezone.md) |
| 16 | fsimplespell | 英文简称 | varchar | 30 |  | √ | ' ' | 英文简称 |
| 17 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | ffullname | 全称 | varchar | 255 |  | √ | ' ' | 全称 |
| 22 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 23 | fdescription | 英文全称 | varchar | 255 |  | √ | ' ' | 英文全称 |
| 24 | fthreecountrycode | 三字码 | varchar | 10 |  | √ | ' ' | 三字码 |
| 25 | fnumericcode | 数字编码 | varchar | 10 |  | √ | ' ' | 数字编码 |
| 26 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 27 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_country_pkey |  | fid |
| 2 | idx_t_bd_country_number |  | fnumber |

---

## 国家和地区-多语言表 t_bd_country_l

- **表名称：** 国家和地区-多语言表
- **表名：** t_bd_country_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 全称 | varchar | 255 |  | √ | ' ' | 全称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_country_l_pkey |  | fpkid |
| 2 | idx_t_bd_country_l_fid |  | fid,flocaleid |
