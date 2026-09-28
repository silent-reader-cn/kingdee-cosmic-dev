# 值转换数据-isc_mapping_data

## 值转换数据-多语言表 t_isc_mapping_data_l

- **表名称：** 值转换数据-多语言表
- **表名：** t_isc_mapping_data_l

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
| 1 | t_isc_mapping_data_l_pkey |  | fpkid |
| 2 | idx_isc_mappdata_l_fid |  | fid,flocaleid |

---

## 值转换数据-主表 t_isc_mapping_data

- **表名称：** 值转换数据-主表
- **表名：** t_isc_mapping_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | ftarget_id | 目标单ID | varchar | 100 |  | √ | ' ' | 目标单ID |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fsource_name | 源单名称 | varchar | 100 |  | √ | ' ' | 源单名称 |
| 7 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | ftarget_data | 目标数据 | int8 | 64 |  | √ | 0 | 参照数据 isc_basic_data |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | ftarget_number | 目标单编码 | varchar | 100 |  | √ | ' ' | 目标单编码 |
| 12 | ftarget_data_ref | ftarget_data_ref | int8 | 64 |  | √ | 0 |  |
| 13 | fsource_number | 源单编码 | varchar | 100 |  | √ | ' ' | 源单编码 |
| 14 | ftarget_name | 目标单名称 | varchar | 100 |  | √ | ' ' | 目标单名称 |
| 15 | fenable | 标志 | varchar | 30 |  | √ | ' ' | 标志,枚举: 0 :疑似失效 1 :有效 |
| 16 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 17 | fmapping_rule | 值转换规则 | int8 | 64 |  | √ | 0 | 值转换规则 isc_value_conver_rule |
| 18 | fsource_id | 源单ID | varchar | 100 |  | √ | ' ' | 源单ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_mapdata_fnum |  | fnumber |
| 2 | t_isc_mapping_data_pkey |  | fid |
| 3 | idx_isc_mapdata_scheandsoid |  | fmapping_rule,fsource_id |
