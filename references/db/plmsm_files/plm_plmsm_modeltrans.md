# PDM模型树列表传输-plm_plmsm_modeltrans

## PDM模型树列表传输-主表 t_plmsm_modeldata

- **表名称：** PDM模型树列表传输-主表
- **表名：** t_plmsm_modeldata

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 3 | fpdextmetadataid | fpdextmetadataid | varchar | 36 |  | √ | ' ' |  |
| 4 | fmodeltype | 模型类型 | varchar | 50 |  | √ | ' ' | 模型类型,枚举: A :基础模型 B :业务模型 C :关联关系模型 D :Version模型 E :Master模型 F :Branch模型 G :组合关系模型 H :聚合关系模型 I :ItemMaster模型 R :ItemRevision模型 |
| 5 | fformmetald | 模型 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 6 | fversionformmeta | 版本模型 | varchar | 36 |  | √ | ' ' | [表单元数据 bos_formmeta](../mdl_files/bos_formmeta.md) |
| 7 | fsourcemodelid | 源模型 | int8 | 64 |  | √ | 0 | 源模型 |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fmasterbizid | 主业务模型ID | int8 | 64 |  | √ | 0 | 主业务模型ID |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | ficon | 图标 | varchar | 50 |  | √ | ' ' | 图标 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fcontrolkey | 控制位 | int8 | 64 |  | √ | 2147483647 | 控制位 |
| 16 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 17 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [PDM模型树列表传输 plm_plmsm_modeltrans](../plmsm_files/plm_plmsm_modeltrans.md) |
| 19 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 20 | flongnumber | 长编码 | varchar | 2000 |  | √ | ' ' | 长编码 |
| 21 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 22 | ftargetmodelid | 目标模型 | int8 | 64 |  | √ | 0 | 目标模型 |
| 23 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 25 | fcfgextmetadataid | fcfgextmetadataid | varchar | 36 |  | √ | ' ' |  |

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

## PDM模型树列表传输-多语言表 t_plmsm_modeldata_l

- **表名称：** PDM模型树列表传输-多语言表
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
