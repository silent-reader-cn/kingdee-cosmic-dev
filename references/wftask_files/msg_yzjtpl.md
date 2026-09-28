# 云之家模板-msg_yzjtpl

## 云之家模板-主表 t_msg_yzjtpl

- **表名称：** 云之家模板-主表
- **表名：** t_msg_yzjtpl

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 单据名称 | varchar | 100 |  | √ | ' ' | 单据名称 |
| 3 | fcreatedate | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 4 | fmodifydate | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 5 | fentitynumber | 单据编码 | varchar | 100 |  | √ | ' ' | 单据编码 |
| 6 | fappid | 轻应用ID | varchar | 50 |  | √ | ' ' | 轻应用ID |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_msg_yzjtpl |  | fid |
| 2 | idx_msg_yzjtpl |  | fentitynumber |

---

## 云之家模板-多语言表 t_msg_yzjtpl_l

- **表名称：** 云之家模板-多语言表
- **表名：** t_msg_yzjtpl_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 单据名称 | varchar | 100 |  | √ | ' ' | 单据名称 |
| 3 | flocaleid | flocaleid | varchar | 8 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msg_yzjtpl_l |  | fid,flocaleid |
| 2 | pk_t_msg_yzjtpl_l |  | fpkid |
