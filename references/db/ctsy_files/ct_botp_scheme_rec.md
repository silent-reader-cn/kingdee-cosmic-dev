# 主数据分发方案检测结果-ct_botp_scheme_rec

## 主数据分发方案检测结果-主表 t_ctbotp_scheme_rec

- **表名称：** 主数据分发方案检测结果-主表
- **表名：** t_ctbotp_scheme_rec

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fentityname | 实体名称 | varchar | 204 |  | √ | ' ' | 实体名称 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | faccountnumber | 数据中心名称 | varchar | 36 |  | √ | ' ' | 数据中心名称 |
| 5 | ftenantcode | 租户编码 | varchar | 36 |  | √ | ' ' | 租户编码 |
| 6 | fhasdistributionscheme | 是否分发 | bpchar | 1 |  | √ | ' ' | 是否分发 |
| 7 | facccountid | 数据中心ID | varchar | 36 |  | √ | ' ' | 数据中心ID |
| 8 | fentityid | 实体标识 | varchar | 36 |  | √ | ' ' | 实体标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ctbotp_scheme_rec |  | fid |

---

## 主数据分发方案检测结果-多语言表 t_ctbotp_scheme_rec_l

- **表名称：** 主数据分发方案检测结果-多语言表
- **表名：** t_ctbotp_scheme_rec_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fentityname | 实体名称 | varchar | 204 |  | √ | ' ' | 实体名称 |
| 3 | flocaleid | flocaleid | varchar | 14 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 40 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ctbotp_scheme_rec_l |  | fpkid |
