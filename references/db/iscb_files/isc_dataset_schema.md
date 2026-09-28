# 数据集-isc_dataset_schema

## 数据集-多语言表 t_iscb_dataset_schema_l

- **表名称：** 数据集-多语言表
- **表名：** t_iscb_dataset_schema_l

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
| 1 | t_iscb_dataset_schema_l_pkey |  | fpkid |
| 2 | idx_iscb_dataset_schema_l |  | fid,flocaleid |

---

## 数据集-主表 t_iscb_dataset_schema

- **表名称：** 数据集-主表
- **表名：** t_iscb_dataset_schema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 510 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 6 | fmeta_type | 集成对象类型 | varchar | 30 |  | √ | ' ' | 集成对象类型,枚举: STRUCT :结构 SERVICE :加载服务 QUERY :查询服务 |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | fdefine_json | 方案定义 | varchar | 510 |  | √ | ' ' | 方案定义 |
| 9 | fdata_source | 数据源 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 10 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 16 | fdefine_json_tag | 方案定义_详情 | text | 0 |  |  | null | 方案定义_详情 |
| 17 | fenable | 发布状态 | varchar | 30 |  | √ | ' ' | 发布状态,枚举: 1 :未发布 2 :已发布 |
| 18 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 19 | ffull_name | 全名 | varchar | 300 |  | √ | ' ' | 全名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_iscb_dataset_schema_pkey |  | fid |
| 2 | idx_iscb_dataset_schema |  | fmeta_type,fdata_source |
