# 发票信息实体映射关系-er_invoicefieldmapping

## 单据体-子表 t_er_invfieldmap

- **表名称：** 单据体-子表
- **表名：** t_er_invfieldmap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fcodefield | 模型字段标识 | varchar | 100 |  | √ | ' ' | 模型字段标识 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fmetafield | 元数据实体标识 | varchar | 100 |  | √ | ' ' | 元数据实体标识 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_er_invfieldmap |  | fentryid |
| 2 | idx_er_invfieldmap_field |  | fmetafield,fcodefield |
| 3 | idx_er_invfieldmap_fid |  | fid |

---

## 发票信息实体映射关系-主表 t_er_invfieldmapping

- **表名称：** 发票信息实体映射关系-主表
- **表名：** t_er_invfieldmapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentitykey | 单据元数据标识 | varchar | 80 |  | √ | ' ' | 单据元数据标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_invfieldmapping_key |  | fentitykey |
| 2 | pk_t_er_invfieldmapping |  | fid |
