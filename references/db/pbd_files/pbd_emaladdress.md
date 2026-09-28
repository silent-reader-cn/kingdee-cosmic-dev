# 电商地址-pbd_emaladdress

## 电商地址-多语言表 t_mal_emaladdress_l

- **表名称：** 电商地址-多语言表
- **表名：** t_mal_emaladdress_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 510 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_emaladdress_l_fid |  | fid,flocaleid |
| 2 | pk_t_mal_emaladdress_l |  | fpkid |

---

## 电商地址-主表 t_mal_emaladdress

- **表名称：** 电商地址-主表
- **表名：** t_mal_emaladdress

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fisleaf | 是否叶子 | bpchar | 1 |  | √ | '1' | 是否叶子 |
| 4 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 5 | femaltype | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 1 :自建商城 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 |
| 6 | fparentid | 上级 | int8 | 64 |  | √ | 0 | 电商地址 pbd_emaladdress |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | ffullname | ffullname | varchar | 510 |  | √ | ' ' |  |
| 9 | flongnumber | 长编码 | varchar | 50 |  | √ | ' ' | 长编码 |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | flevel | 级次 | int4 | 32 |  | √ | 0 | 级次 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_emaladdress_fnumber |  | fnumber |
| 2 | pk_t_mal_emaladdress |  | fid |
