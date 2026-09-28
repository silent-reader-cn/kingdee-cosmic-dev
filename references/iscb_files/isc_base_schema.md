# 参照数据方案-isc_base_schema

## 参照数据方案-主表 t_iscb_base_schema

- **表名称：** 参照数据方案-主表
- **表名：** t_iscb_base_schema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fnumber_field | 编码字段 | varchar | 100 |  | √ | ' ' | 编码字段,枚举: |
| 5 | fdata_schema | 集成对象 | int8 | 64 |  | √ | 0 | 集成对象 isc_metadata_schema |
| 6 | fprogress | 同步进度 | varchar | 100 |  | √ | ' ' | 同步进度 |
| 7 | fdata_source | 数据源 | int8 | 64 |  | √ | 0 | 数据源管理 isc_data_source |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fname_field | 名称字段 | varchar | 100 |  | √ | ' ' | 名称字段,枚举: |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcus_field1 | 自定义字段1 | varchar | 100 |  | √ | ' ' | 自定义字段1,枚举: |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fcus_field3 | 自定义字段3 | varchar | 100 |  | √ | ' ' | 自定义字段3,枚举: |
| 15 | fsync_state | 同步状态 | varchar | 30 |  | √ | ' ' | 同步状态,枚举: 1 :待反馈 2 :进行中 3 :已完成 4 :已失败 |
| 16 | fcus_field2 | 自定义字段2 | varchar | 100 |  | √ | ' ' | 自定义字段2,枚举: |
| 17 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iscb_bassm_fnum |  | fnumber |
| 2 | t_iscb_base_schema_pkey |  | fid |

---

## 参照数据方案-多语言表 t_iscb_base_schema_l

- **表名称：** 参照数据方案-多语言表
- **表名：** t_iscb_base_schema_l

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
| 1 | idx_iscb_bassc_l_fid |  | fid,flocaleid |
| 2 | t_iscb_base_schema_l_pkey |  | fpkid |
