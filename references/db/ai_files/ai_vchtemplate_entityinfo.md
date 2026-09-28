# 凭证模板基础资料-ai_vchtemplate_entityinfo

## 凭证模板基础资料-主表 t_ai_vchtemplate

- **表名称：** 凭证模板基础资料-主表
- **表名：** t_ai_vchtemplate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fxml | fxml | text | 0 |  |  | null |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 5 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 6 | fstatus | fstatus | bpchar | 1 |  | √ | 'C' |  |
| 7 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 8 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 9 | faccttableid | faccttableid | int8 | 64 |  | √ | 0 |  |
| 10 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 11 | fxmllang | fxmllang | text | 0 |  |  | ' ' |  |
| 12 | fbitindex | fbitindex | int4 | 32 |  | √ | 0 |  |
| 13 | fissyspreset | fissyspreset | bpchar | 1 |  | √ | '0' |  |
| 14 | fvchtypedesc | fvchtypedesc | varchar | 500 |  | √ | ' ' |  |
| 15 | fbillno | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 16 | feventclassid | feventclassid | int8 | 64 |  | √ | 0 |  |
| 17 | fbizdatedesc | fbizdatedesc | varchar | 500 |  | √ | ' ' |  |
| 18 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 19 | freoper | freoper | varchar | 30 |  | √ | ' ' |  |
| 20 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 21 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 22 | fbillstatus | fbillstatus | bpchar | 1 |  | √ | 'C' |  |
| 23 | fnewsortorder | fnewsortorder | varchar | 255 |  | √ | ' ' |  |
| 24 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 25 | foper | foper | varchar | 30 |  | √ | ' ' |  |
| 26 | funoper | funoper | varchar | 30 |  | √ | ' ' |  |
| 27 | fauditdate | fauditdate | timestamp | 0 |  |  | null |  |
| 28 | fdescription | fdescription | varchar | 255 |  |  | ' ' |  |
| 29 | fsourcebill | fsourcebill | varchar | 36 |  | √ | ' ' |  |
| 30 | fctrlstrategy | fctrlstrategy | bpchar | 1 |  | √ | ' ' |  |
| 31 | fpresetnumber | fpresetnumber | varchar | 80 |  | √ | ' ' |  |
| 32 | fbooktypeid | fbooktypeid | int8 | 64 |  | √ | 0 |  |
| 33 | facctorgid | facctorgid | varchar | 100 |  | √ | ' ' |  |
| 34 | fenable | 单据状态 | bpchar | 1 |  | √ | '0' | 单据状态,枚举: |
| 35 | fbuildvchgen | fbuildvchgen | varchar | 30 |  | √ | ' ' |  |
| 36 | fvoucherdatedesc | fvoucherdatedesc | varchar | 500 |  | √ | ' ' |  |
| 37 | fnumber | fnumber | varchar | 80 |  | √ | ' ' |  |
| 38 | fsourcebitindex | fsourcebitindex | int4 | 32 |  | √ | 0 |  |
| 39 | fauditorid | fauditorid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_vchtemplate_pkey |  | fid |
| 2 | idx_ai_vchtemplate_sbill |  | fsourcebill |
| 3 | idx_t_ai_vchtemplate_createorg |  | fcreateorgid |
| 4 | idx_t_ai_vchtemplate_master |  | fmasterid |

---

## 凭证模板基础资料-多语言表 t_ai_vchtemplate_l

- **表名称：** 凭证模板基础资料-多语言表
- **表名：** t_ai_vchtemplate_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | fname | varchar | 255 |  | √ | ' ' |  |
| 3 | fxmllang | fxmllang | text | 0 |  |  | null |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fdescription | 描述 | varchar | 255 |  |  | ' ' | 描述 |
| 6 | facctbookname | facctbookname | varchar | 500 |  |  | ' ' |  |
| 7 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_ai_vchtemplate_l_pkey |  | fpkid |
| 2 | idx_ai_vchtemplate_l_fid |  | fid,flocaleid |
