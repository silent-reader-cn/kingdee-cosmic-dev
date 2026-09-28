# 国家预置数据-bd_country_preset_data

## 国家预置数据-主表 t_bd_country_preset

- **表名称：** 国家预置数据-主表
- **表名：** t_bd_country_preset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | flogo | 图片 | varchar | 255 |  | √ | ' ' | 图片 |
| 5 | fformatplanid | 区域格式 | int8 | 64 |  | √ | 0 | 区域格式 |
| 6 | ftwocountrycode | 二字码 | varchar | 10 |  | √ | ' ' | 二字码 |
| 7 | ffullname | 全称 | varchar | 1024 |  | √ | ' ' | 全称 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fdisabledate | 禁用时间 | timestamp | 0 |  |  | null | 禁用时间 |
| 10 | fdisablerid | 禁用人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fdescription | 英文全称 | varchar | 255 |  | √ | ' ' | 英文全称 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fthreecountrycode | 三字码 | varchar | 10 |  | √ | ' ' | 三字码 |
| 15 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 16 | fnumericcode | 数字编码 | varchar | 10 |  | √ | ' ' | 数字编码 |
| 17 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 19 | fareacode | 国际电话区号 | varchar | 10 |  | √ | ' ' | 国际电话区号 |
| 20 | fsimplespell | 英文简称 | varchar | 30 |  | √ | ' ' | 英文简称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bd_country_preset |  | fid |
| 2 | idx_bd_countrypreset_number |  | fnumber |

---

## 国家预置数据-多语言表 t_bd_country_preset_l

- **表名称：** 国家预置数据-多语言表
- **表名：** t_bd_country_preset_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 全称 | varchar | 1024 |  | √ | ' ' | 全称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bd_country_preset_l_id |  | fid,flocaleid |
| 2 | pk_t_bd_country_preset_l |  | fpkid |
