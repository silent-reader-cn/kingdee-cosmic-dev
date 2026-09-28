# 参照数据-isc_basic_data

## 参照数据-主表 t_iscb_basic_data

- **表名称：** 参照数据-主表
- **表名：** t_iscb_basic_data

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fbaseschema | 参照数据方案 | int8 | 64 |  | √ | 0 | [参照数据方案 isc_base_schema](../iscb_files/isc_base_schema.md) |
| 6 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fdataschema | 集成对象 | int8 | 64 |  | √ | 0 | [集成对象 isc_metadata_schema](../iscb_files/isc_metadata_schema.md) |
| 8 | fcus_field1 | 自定义字段1 | varchar | 100 |  | √ | ' ' | 自定义字段1 |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | foid | 单据ID | varchar | 100 |  | √ | ' ' | 单据ID |
| 12 | fcus_field3 | 自定义字段3 | varchar | 100 |  | √ | ' ' | 自定义字段3 |
| 13 | fcus_field2 | 自定义字段2 | varchar | 100 |  | √ | ' ' | 自定义字段2 |
| 14 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_basic_data_pkey |  | fid |
| 2 | idx_iscb_basdata_datasche |  | fdataschema |
| 3 | idx_iscb_basdata_combo |  | fbaseschema,foid |
| 4 | idx_iscb_basdata_fnum |  | fnumber |

---

## 参照数据-多语言表 t_iscb_basic_data_l

- **表名称：** 参照数据-多语言表
- **表名：** t_iscb_basic_data_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 512 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_basic_data_l_pkey |  | fpkid |
| 2 | idx_isc_basdat_l_fid |  | fid,flocaleid |
