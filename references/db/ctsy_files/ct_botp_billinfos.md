# 主数据分发检测单据-ct_botp_billinfos

## 主数据分发检测单据-主表 t_ctbotp_billinfors

- **表名称：** 主数据分发检测单据-主表
- **表名：** t_ctbotp_billinfors

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fbillnumber | 单据标识 | varchar | 36 |  | √ | ' ' | 单据标识 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 4 | faccountnumber | 数据中心名称 | varchar | 36 |  | √ | ' ' | 数据中心名称 |
| 5 | ftenantcode | 租户编码 | varchar | 36 |  | √ | ' ' | 租户编码 |
| 6 | fmodifier | 检测人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | facccountid | 数据中心ID | varchar | 36 |  | √ | ' ' | 数据中心ID |
| 8 | fcheckdate | 检测时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 检测时间 |
| 9 | fbillname | 单据名称 | varchar | 204 |  | √ | ' ' | 单据名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ctbotp_billinfors |  | fid |

---

## 主数据分发检测单据-多语言表 t_ctbotp_billinfors_l

- **表名称：** 主数据分发检测单据-多语言表
- **表名：** t_ctbotp_billinfors_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | flocaleid | flocaleid | varchar | 14 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 40 |  | √ | ' ' | pkid |
| 4 | fbillname | 单据名称 | varchar | 204 |  | √ | ' ' | 单据名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_ctbotp_billinfors_l |  | fpkid |
