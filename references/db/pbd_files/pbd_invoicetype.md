# 发票类型-pbd_invoicetype

## 发票类型-多语言表 t_mal_invoicetype_l

- **表名称：** 发票类型-多语言表
- **表名：** t_mal_invoicetype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_mal_invoicetype_l |  | fpkid |
| 2 | idx_mal_invoicetype_l_fid |  | fid,flocaleid |

---

## 发票类型-主表 t_mal_invoicetype

- **表名称：** 发票类型-主表
- **表名：** t_mal_invoicetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | femalinvoicenumber | 电商发票编码 | varchar | 255 |  | √ | ' ' | 电商发票编码 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | fname | varchar | 50 |  | √ | ' ' |  |
| 5 | femaltype | 电商平台 | varchar | 255 |  | √ | ' ' | 电商平台,枚举: 2 :京东商城 3 :苏宁易购 4 :得力商城 5 :西域商城 6 :晨光商城 7 :京东工业品 8 :鑫方盛商城 9 :震坤行商城 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fbdinvoicetype | 商城发票类型 | int8 | 64 |  | √ | 0 | [发票种类 bd_invoicetype](../basedata_files/bd_invoicetype.md) |
| 8 | fmalinvoicetype | 商城发票类型 | varchar | 255 |  | √ | ' ' | 商城发票类型,枚举: 1 :增值税电子普通发票 2 :增值税电子专用发票 3 :纸质增值税普通发票 4 :纸质增值税专用发票 |
| 9 | fauditdate | 审核时间 | timestamp | 0 |  |  | null | 审核时间 |
| 10 | femalinvoicetype | 电商发票类型 | varchar | 255 |  | √ | ' ' | 电商发票类型,枚举: 1 :电子普通发票 2 :电子发票 3 :普票 4 :普通 5 :增值税普票 6 :增值税专用发票 7 :增票 8 :增值税 9 :增值税专票 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fstatus | 数据状态 | bpchar | 1 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fpreset | 是否预置 | bpchar | 1 |  | √ | ' ' | 是否预置 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | fauditorid | 审核人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_mal_invoicetype_fmasterid |  | fmasterid |
| 2 | idx_mal_invoicetype_fnumber |  | fnumber |
| 3 | pk_t_mal_invoicetype |  | fid |
