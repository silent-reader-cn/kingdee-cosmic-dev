# 数据源-ids_gpe_datasource

## 数据源-多语言表 t_ids_gpe_datasource_l

- **表名称：** 数据源-多语言表
- **表名：** t_ids_gpe_datasource_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_gpe_datasource_l_fname |  | fname |
| 2 | pk_t_ids_gpe_datasource_l |  | fpkid |

---

## 数据源-主表 t_ids_gpe_datasource

- **表名称：** 数据源-主表
- **表名：** t_ids_gpe_datasource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fmetadata | 元数据 | varchar | 255 |  | √ | ' ' | 元数据 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fentitynumber | 业务对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 7 | fsplitchar | 列分隔符 | varchar | 10 |  | √ | ' ' | 列分隔符 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: bizobj :业务对象 csv :CSV |
| 13 | ffirstlinecolname | 首行为列名 | bpchar | 1 |  | √ | '1' | 首行为列名 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | fattachmentid | 附件 | int8 | 64 |  | √ | 0 | [附件 ids_gpe_attachment](../ids_files/ids_gpe_attachment.md) |
| 17 | fmetadata_tag | 元数据_详情 | text | 0 |  |  | null | 元数据_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_gpe_datasource_name |  | fname |
| 2 | pk_t_ids_gpe_datasource |  | fid |
