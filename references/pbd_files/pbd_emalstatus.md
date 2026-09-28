# 电商状态-pbd_emalstatus

## 电商状态-多语言表 t_mal_emalstatus_l

- **表名称：** 电商状态-多语言表
- **表名：** t_mal_emalstatus_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 状态名称 | varchar | 100 |  | √ | ' ' | 状态名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_emalstatus_l |  | fpkid |
| 2 | idx_t_mal_emalstatus_l_fid |  | fid,flocaleid |

---

## 电商状态-主表 t_mal_emalstatus

- **表名称：** 电商状态-主表
- **表名：** t_mal_emalstatus

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fstatus | fstatus | bpchar | 1 |  | √ | ' ' |  |
| 3 | fname | fname | varchar | 100 |  | √ | ' ' |  |
| 4 | fstatustypenumber | 状态类型编码 | varchar | 50 |  | √ | ' ' | 状态类型编码 |
| 5 | femaltype | 电商平台 | bpchar | 1 |  | √ | ' ' | 电商平台,枚举: 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 6 | femalstatusname | 电商状态名称 | varchar | 100 |  | √ | ' ' | 电商状态名称 |
| 7 | fstatustype | 状态类型 | bpchar | 1 |  | √ | ' ' | 状态类型,枚举: 1 :电商订单状态 2 :售后状态 3 :开票状态 4 :库存 |
| 8 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 9 | femalstatusnumber | 电商状态编码 | varchar | 50 |  | √ | ' ' | 电商状态编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_mal_emalstatus_fnumber |  | fnumber |
| 2 | pk_t_mal_emalstatus |  | fid |
