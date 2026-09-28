# 事件分类-kem_eventgroup

## 事件分类-多语言表 t_kem_eventgroup_l

- **表名称：** 事件分类-多语言表
- **表名：** t_kem_eventgroup_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 分类名称 | varchar | 50 |  | √ | ' ' | 分类名称 |
| 3 | ffullname | 长名称 | varchar | 50 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_kem_eventgroup_l |  | fpkid |
| 2 | idx_kem_eventgroup_l_fid |  | fid,flocaleid |

---

## 事件分类-主表 t_kem_eventgroup

- **表名称：** 事件分类-主表
- **表名：** t_kem_eventgroup

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 5 | fparentid | 上级 | int8 | 64 |  | √ | 0 | [事件分类 kem_eventgroup](../kem_files/kem_eventgroup.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 8 | fdatasourceid | 数据源 | int8 | 64 |  | √ | 0 | [数据源管理 isc_data_source](../iscb_files/isc_data_source.md) |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 分类编码 | varchar | 100 |  | √ | ' ' | 分类编码 |
| 16 | fdesc | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 17 | feventsourceid | feventsourceid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_kem_eventgroup_dsid |  | fdatasourceid |
| 2 | pk_t_kem_eventgroup |  | fid |
| 3 | idx_kem_eventgroup_number |  | fnumber |
