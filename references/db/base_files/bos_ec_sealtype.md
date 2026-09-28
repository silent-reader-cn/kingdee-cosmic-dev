# 签章类型-bos_ec_sealtype

## 签章类型-主表 t_bos_ec_sealtype

- **表名称：** 签章类型-主表
- **表名：** t_bos_ec_sealtype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 50 |  | √ | ' ' | 备注 |
| 3 | fname | 签章类型 | varchar | 255 |  | √ | ' ' | 签章类型 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bos_ec_sealtype |  | fid |
| 2 | idx_bos_ec_sealtype_number |  | fnumber |

---

## 签章类型-多语言表 t_bos_ec_sealtype_l

- **表名称：** 签章类型-多语言表
- **表名：** t_bos_ec_sealtype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 签章类型 | varchar | 255 |  | √ | ' ' | 签章类型 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_ec_sealtype_l_id_localid |  | fid,flocaleid |
| 2 | pk_bos_ec_sealtype_l |  | fpkid |
