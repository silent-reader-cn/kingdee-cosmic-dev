# 商旅城市更新-er_city

## 商旅城市更新-多语言表 t_er_tripcity_l

- **表名称：** 商旅城市更新-多语言表
- **表名：** t_er_tripcity_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 城市中文名称 | varchar | 100 |  | √ | ' ' | 城市中文名称 |
| 3 | ffullname | ffullname | varchar | 255 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 6 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_tripcity_l_fname |  | fname |
| 2 | idx_er_tripcity_l_fid |  | fid,flocaleid |
| 3 | t_er_tripcity_l_pkey |  | fpkid |

---

## 商旅城市更新-主表 t_er_tripcity

- **表名称：** 商旅城市更新-主表
- **表名：** t_er_tripcity

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fnameen | 城市英文名称 | varchar | 44 |  | √ | ' ' | 城市英文名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 城市中文名称 | varchar | 100 |  | √ | ' ' | 城市中文名称 |
| 5 | fdidicityid | 滴滴城市id | int8 | 64 |  | √ | 0 | 滴滴城市id |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | '1970-01-01 00:00:00' | 创建时间 |
| 7 | fcityid | 携程城市id | int8 | 64 |  | √ | 0 | 携程城市id |
| 8 | fpoitype | POI类型 | int8 | 64 |  | √ | 0 | POI类型 |
| 9 | fcountryid | 国家id | int8 | 64 |  | √ | 0 | 国家id |
| 10 | fcountryname | fcountryname | varchar | 44 |  | √ | ' ' |  |
| 11 | ffullcityid | 携程城市id(全量) | int4 | 32 |  | √ | 0 | 携程城市id(全量) |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | '1970-01-01 00:00:00' | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fnamepinyin | 携程城市拼音 | varchar | 44 |  | √ | ' ' | 携程城市拼音 |
| 15 | fcountrycode | 国家二代码 | varchar | 44 |  | √ | ' ' | 国家二代码 |
| 16 | fadmindivisionid | 行政区划 | int8 | 64 |  | √ | 0 | [行政区划 bd_admindivision](../base_files/bd_admindivision.md) |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fprovinceid | 省id | int8 | 64 |  | √ | 0 | 省id |
| 20 | fcountryename | 国家英文名称 | varchar | 44 |  | √ | ' ' | 国家英文名称 |
| 21 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 22 | fnumber | 城市简拼 | varchar | 80 |  | √ | ' ' | 城市简拼 |
| 23 | fduplicatecitynameflag | 有重复名称标记 | int8 | 64 |  | √ | 0 | 有重复名称标记 |
| 24 | fcode | 携程城市三字码 | varchar | 44 |  | √ | ' ' | 携程城市三字码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_tripcity_code |  | fcode |
| 2 | idx_er_tripcity_cityid |  | fcityid |
| 3 | t_er_tripcity_pkey |  | fid |
