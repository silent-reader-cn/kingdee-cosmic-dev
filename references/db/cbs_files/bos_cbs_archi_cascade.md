# 单据归档级联配置-bos_cbs_archi_cascade

## 单据归档级联配置-多语言表 t_cbs_archi_cascade_l

- **表名称：** 单据归档级联配置-多语言表
- **表名：** t_cbs_archi_cascade_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 500 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 500 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_cascade_l |  | fid,flocaleid |
| 2 | pk_cbs_archi_cascade_l |  | fpkid |

---

## 单据归档级联配置-主表 t_cbs_archi_cascade

- **表名称：** 单据归档级联配置-主表
- **表名：** t_cbs_archi_cascade

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | ' ' | 是否叶子 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fjoinfield | 关联属性 | varchar | 50 |  | √ | ' ' | 关联属性 |
| 7 | flongnumber | 长编码 | varchar | 500 |  | √ | ' ' | 长编码 |
| 8 | fentitynumber | 实体编码 | varchar | 50 |  | √ | ' ' | 实体编码 |
| 9 | fparentnumber | 父实体编码 | varchar | 50 |  | √ | ' ' | 父实体编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 16 | fparent | 父实体 | int8 | 64 |  | √ | 0 | [单据归档级联配置 bos_cbs_archi_cascade](../cbs_files/bos_cbs_archi_cascade.md) |
| 17 | fbillset | 归档实体 | int8 | 64 |  | √ | 0 | [可归档单据范围 bos_cbs_archi_billset](../cbs_files/bos_cbs_archi_billset.md) |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_cascade |  | fid |
| 2 | idx_cbs_archi_cascade |  | fentitynumber |
