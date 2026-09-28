# 数据集-ids_gpe_dataset

## 数据集-多语言表 t_ids_gpe_dataset_l

- **表名称：** 数据集-多语言表
- **表名：** t_ids_gpe_dataset_l

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
| 1 | idx_ids_gpe_dataset_l_fname |  | fname |
| 2 | pk_t_ids_gpe_dataset_l |  | fpkid |

---

## 数据集-主表 t_ids_gpe_dataset

- **表名称：** 数据集-主表
- **表名：** t_ids_gpe_dataset

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | ffailmsg | 失败原因 | varchar | 255 |  | √ | ' ' | 失败原因 |
| 3 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 4 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | ffirstlinecolname | 首行为列名 | bpchar | 1 |  | √ | '1' | 首行为列名 |
| 8 | fissyncdata | 同步数据 | bpchar | 1 |  | √ | '0' | 同步数据 |
| 9 | ffilter | 过滤条件 | varchar | 255 |  | √ | ' ' | 过滤条件 |
| 10 | frequestid | 概览请求ID | varchar | 50 |  | √ | ' ' | 概览请求ID |
| 11 | fattachmentid | 附件 | int8 | 64 |  | √ | 0 | [附件 ids_gpe_attachment](../ids_files/ids_gpe_attachment.md) |
| 12 | fmetadata_tag | 元数据_详情 | text | 0 |  |  | null | 元数据_详情 |
| 13 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 14 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 15 | fmetadata | 元数据 | varchar | 255 |  | √ | ' ' | 元数据 |
| 16 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 17 | fsummary_tag | 概览统计_详情 | text | 0 |  |  | null | 概览统计_详情 |
| 18 | fsplitchar | 分隔符 | varchar | 10 |  | √ | ',' | 分隔符 |
| 19 | fexecutestatus | 执行状态 | varchar | 10 |  | √ | ' ' | 执行状态,枚举: 0 :等待执行 10 :执行中 20 :执行成功 30 :执行失败 |
| 20 | ffilter_tag | 过滤条件_详情 | text | 0 |  |  | null | 过滤条件_详情 |
| 21 | ffailmsg_tag | 失败原因_详情 | text | 0 |  |  | null | 失败原因_详情 |
| 22 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: predict :预测数据集 evaluation :评估数据集 future :未来数据集 other :其他 |
| 23 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 24 | fdatasource | 数据源 | int8 | 64 |  | √ | 0 | [数据源 ids_gpe_datasource](../ids_files/ids_gpe_datasource.md) |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 26 | ffieldvalueinfo | 字段值信息 | varchar | 2000 |  | √ | ' ' | 字段值信息 |
| 27 | fsummary | 概览统计 | varchar | 255 |  | √ | ' ' | 概览统计 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ids_gpe_dataset_name |  | fname |
| 2 | pk_t_ids_gpe_dataset |  | fid |
