# 归档库管理-bos_cbs_archi_database

## 归档库管理-主表 t_cbs_archi_database

- **表名称：** 归档库管理-主表
- **表名：** t_cbs_archi_database

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 归档库名称 | varchar | 255 |  | √ | ' ' | 归档库名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fgroupid | 归档库分组 | int8 | 64 |  | √ | 0 | [归档库分组 bos_cbs_archi_group_rule](../cbs_files/bos_cbs_archi_group_rule.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fdatabase | 目标库 | varchar | 50 |  | √ | ' ' | 目标库,枚举: |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | flogicsuffix | 转储分区 | varchar | 3 |  | √ | ' ' | 转储分区 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 12 | farchiveroute | 逻辑库 | varchar | 50 |  | √ | ' ' | 逻辑库 |
| 13 | fdatabase_type | 目标库类型 | varchar | 50 |  | √ | ' ' | 目标库类型,枚举: db :数据库 es :Elasticsearch |
| 14 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbs_archi_database |  | fid |
| 2 | idx_cbs_archi_database |  | fnumber |

---

## 归档库管理-多语言表 t_cbs_archi_database_l

- **表名称：** 归档库管理-多语言表
- **表名：** t_cbs_archi_database_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 归档库名称 | varchar | 255 |  | √ | ' ' | 归档库名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbs_archi_database_l_0 |  | fid,flocaleid |
| 2 | pk_cbs_archi_database_l |  | fpkid |
