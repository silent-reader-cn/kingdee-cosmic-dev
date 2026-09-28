# PLM应用场景表记录-plm_plmsm_as_tablerecord

## 单据体-子表 t_plm_as_table_entry

- **表名称：** 单据体-子表
- **表名：** t_plm_as_table_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodifydatefield | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 3 | fcolumnsuffix | 列后缀名 | varchar | 50 |  | √ | ' ' | 列后缀名 |
| 4 | fcolumnsource | 列来源 | varchar | 50 |  | √ | ' ' | 列来源 |
| 5 | fformnumber | 单据标识 | varchar | 50 |  | √ | ' ' | 单据标识 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fmodifierfield | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 9 | fpropertyname | 属性名 | varchar | 50 |  | √ | ' ' | 属性名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_as_table_entry |  | fentryid |
| 2 | idx_plm_as_table_entry_id |  | fid |

---

## PLM应用场景表记录-主表 t_plm_as_tablerecord

- **表名称：** PLM应用场景表记录-主表
- **表名：** t_plm_as_tablerecord

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型 |
| 5 | fbillstatus | 单据状态 | varchar | 50 |  | √ | ' ' | 单据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fauditdate | 审核日期 | timestamp | 0 |  |  | null | 审核日期 |
| 8 | ftablestatus | 表状态 | varchar | 50 |  | √ | ' ' | 表状态,枚举: 1 :启用 0 :禁用 |
| 9 | fbillno | 表名称 | varchar | 30 |  | √ | ' ' | 表名称 |
| 10 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_plm_as_tablerecord |  | fid |
| 2 | idx_plm_as_tablerecord_billno |  | fbillno |
