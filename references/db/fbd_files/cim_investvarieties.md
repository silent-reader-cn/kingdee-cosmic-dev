# 投资品种-cim_investvarieties

## 投资品种-多语言表 t_cim_investvarieties_l

- **表名称：** 投资品种-多语言表
- **表名：** t_cim_investvarieties_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | ffullname | 长名称 | varchar | 255 |  | √ | ' ' | 长名称 |
| 4 | flocaleid | flocaleid | varchar | 30 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_cim_investvarieties_l |  | fpkid |
| 2 | idx_cim_investvarieties_l |  | fid,flocaleid |

---

## 投资品种-主表 t_cim_investvarieties

- **表名称：** 投资品种-主表
- **表名：** t_cim_investvarieties

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fisleaf | 叶子 | bpchar | 1 |  | √ | '1' | 叶子 |
| 4 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 5 | fisbondinvestfund | 证券投资基金 | bpchar | 1 |  | √ | '0' | 证券投资基金 |
| 6 | fparentid | 上级品种 | int8 | 64 |  | √ | 0 | [投资品种 cim_investvarieties](../fbd_files/cim_investvarieties.md) |
| 7 | fdescrible | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | ffullname | ffullname | varchar | 255 |  | √ | ' ' |  |
| 10 | flongnumber | 长编码 | varchar | 80 |  | √ | ' ' | 长编码 |
| 11 | finvesttype | 投资类型 | varchar | 80 |  | √ | ' ' | 投资类型,枚举: finance :理财产品 fixed :定期存款 notice :通知存款 structure :结构性存款 huge :大额存单 |
| 12 | finvestsource | 投资来源 | varchar | 30 |  | √ | ' ' | 投资来源,枚举: bank :银行市场 bond :债券市场 capital :资本市场 peer :同业市场 other :其他 settlecenter :内部金融 |
| 13 | fispreset | 预置 | bpchar | 1 |  | √ | '0' | 预置 |
| 14 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | flevel | 级次 | int8 | 64 |  | √ | 0 | 级次 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fisproduct | 存贷款产品 | bpchar | 1 |  | √ | ' ' | 存贷款产品 |
| 20 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 1 :可用 0 :禁用 |
| 21 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 22 | fislimitsurety | fislimitsurety | bpchar | 1 |  | √ | '0' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cim_investvarieties |  | fnumber |
| 2 | pk_t_cim_investvarieties |  | fid |
