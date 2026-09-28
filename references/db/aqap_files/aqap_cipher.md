# 银企云加密密钥-aqap_cipher

## 银企云加密密钥-主表 t_aqap_cipher

- **表名称：** 银企云加密密钥-主表
- **表名：** t_aqap_cipher

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | flength | 密钥长度 | int8 | 64 |  | √ | 0 | 密钥长度 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 8 | falgo | 加密算法 | varchar | 50 |  | √ | ' ' | 加密算法,枚举: RSA :RSA AES :AES SM2 :SM2 SM4 :SM4 DES :DES |
| 9 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 10 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 11 | fkey | 初始密钥 | varchar | 2000 |  | √ | ' ' | 初始密钥 |
| 12 | fgroup | 分组 | varchar | 255 |  | √ | ' ' | 分组,枚举: USER :USER ADMIN :ADMIN |
| 13 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 255 |  | √ | ' ' | 编码 |
| 15 | fversion | 版本 | int8 | 64 |  | √ | 0 | 版本 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cluster_cipher |  | fnumber |
| 2 | pk_aqap_cipher |  | fid |

---

## 银企云加密密钥-多语言表 t_aqap_cipher_l

- **表名称：** 银企云加密密钥-多语言表
- **表名：** t_aqap_cipher_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  |  | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_aqap_cipher_l |  | fpkid |
| 2 | idx_cluster_cipher_l |  | fname |
