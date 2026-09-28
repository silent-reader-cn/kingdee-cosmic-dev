# PDM模型-plm_plmsm_modeltreedata

## PDM模型-主表 t_plmsm_modeldata

- **表名称：** PDM模型-主表
- **表名：** t_plmsm_modeldata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 5 | fpdextmetadataid | fpdextmetadataid | varchar | 36 |  | √ | ' ' |  |
| 6 | fparentid | 上级 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 7 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型,枚举: A :基础模型 B :业务模型 C :关联关系模型 D :Version模型 E :Master模型 F :Branch模型 G :组合关系模型 H :聚合关系模型 I :ItemMaster模型 R :ItemRevision模型 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fformmetald | 模型 | varchar | 36 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 10 | fversionformmeta | 版本模型 | varchar | 36 |  | √ | ' ' | 表单元数据 bos_formmeta |
| 11 | flongnumber | 长编码 | varchar | 2000 |  | √ | ' ' | 长编码 |
| 12 | fsourcemodelid | 源模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 13 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fmasterbizid | 主业务模型ID | int8 | 64 |  | √ | 0 | 主业务模型ID |
| 16 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 17 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 18 | ficon | 图标 | varchar | 50 |  | √ | ' ' | 图标 |
| 19 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 20 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 21 | ftargetmodelid | 目标模型 | int8 | 64 |  | √ | 0 | PDM模型 plm_plmsm_modeltreedata |
| 22 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 23 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 24 | fcfgextmetadataid | fcfgextmetadataid | varchar | 36 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plmsm_modeldata |  | fid |
| 2 | idx_plmsm_modeldata_name |  | fname |

---

## PDM模型-多语言表 t_plmsm_modeldata_l

- **表名称：** PDM模型-多语言表
- **表名：** t_plmsm_modeldata_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 2000 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_plmsm_modeldata_l_name |  | fname |
| 2 | pk_t_plmsm_modeldata_l |  | fpkid |
