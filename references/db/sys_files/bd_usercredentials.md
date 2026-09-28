# 证书管理-bd_usercredentials

## 证书管理-主表 t_bd_usercredentials

- **表名称：** 证书管理-主表
- **表名：** t_bd_usercredentials

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fbegin | 开始时间 | timestamp | 0 |  |  | null | 开始时间 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | LOCALTIMESTAMP | 创建时间 |
| 5 | funame | 关联用户 | varchar | 255 |  | √ | ' ' | 关联用户 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | fpublickey | 证书公钥 | varchar | 3000 |  | √ | ' ' | 证书公钥 |
| 9 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 10 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 11 | fissue | 颁发者 | varchar | 500 |  | √ | ' ' | 颁发者 |
| 12 | fenable | 证书状态 | bpchar | 1 |  | √ | '0' | 证书状态,枚举: 0 :禁用 1 :可用 |
| 13 | fcertname | 证书名 | varchar | 100 |  | √ | ' ' | 证书名 |
| 14 | fend | 结束时间 | timestamp | 0 |  |  | null | 结束时间 |
| 15 | fnumber | 证书序号 | varchar | 100 |  | √ | ' ' | 证书序号 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_usercredentials_fnumber_key |  | fnumber |
| 2 | t_bd_usercredentials_pkey |  | fid |

---

## 证书管理-多语言表 t_bd_usercredentials_l

- **表名称：** 证书管理-多语言表
- **表名：** t_bd_usercredentials_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 签发商 | varchar | 100 |  | √ | ' ' | 签发商 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_bd_usercredentials_l_fid_flocaleid_key |  | fid,flocaleid |
| 2 | t_bd_usercredentials_l_pkey |  | fpkid |
| 3 | idx_bd_usercerts_l_fid |  | fid,flocaleid |
