# 上下文容器-plm_plmsm_container

## 上下文容器-多语言表 t_plm_pdm_basic_l

- **表名称：** 上下文容器-多语言表
- **表名：** t_plm_pdm_basic_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | fdownloadname | fdownloadname | varchar | 1024 |  | √ | ' ' |  |
| 4 | fsyncresult | fsyncresult | varchar | 500 |  | √ | ' ' |  |
| 5 | fspecification | fspecification | varchar | 255 |  | √ | ' ' |  |
| 6 | fdisplayname | fdisplayname | varchar | 2000 |  | √ | ' ' |  |
| 7 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 8 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 9 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 10 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_plm_pdm_basic_l |  | fpkid |
| 2 | idx_plm_pdm_basic_l_0 |  | fid,flocaleid |

---

## 上下文容器-主表 t_plm_pdm_basic

- **表名称：** 上下文容器-主表
- **表名：** t_plm_pdm_basic

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | flcstatusid | flcstatusid | int8 | 64 |  | √ | 0 |  |
| 3 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 4 | fmodelid | 业务模型标识 | int8 | 64 |  | √ | 0 | 业务模型标识 |
| 5 | frdmversion | frdmversion | varchar | 10 |  | √ | ' ' |  |
| 6 | fconfigcollectid | fconfigcollectid | int8 | 64 |  | √ | 0 |  |
| 7 | fseq | fseq | int4 | 32 |  | √ | 0 |  |
| 8 | fsrccreateorgid | fsrccreateorgid | int8 | 64 |  | √ | 0 |  |
| 9 | fdatastagebit | fdatastagebit | int8 | 64 |  | √ | 1 |  |
| 10 | fhasmaterial | fhasmaterial | bpchar | 1 |  | √ | '-' |  |
| 11 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 12 | fdomainid | fdomainid | int8 | 64 |  | √ | 0 |  |
| 13 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 14 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 15 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 16 | fsyncresult | fsyncresult | varchar | 255 |  | √ | ' ' |  |
| 17 | fspecification | fspecification | varchar | 255 |  | √ | ' ' |  |
| 18 | fsourcedataid | fsourcedataid | int8 | 64 |  | √ | 0 |  |
| 19 | fbitindex | fbitindex | int8 | 64 |  | √ | 0 |  |
| 20 | fcontainerid | fcontainerid | int8 | 64 |  | √ | 0 |  |
| 21 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 22 | fbizorg | fbizorg | int8 | 64 |  | √ | 0 |  |
| 23 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 24 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 25 | fdownloadname | fdownloadname | varchar | 1024 |  | √ | ' ' |  |
| 26 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 27 | fdisplayname | fdisplayname | varchar | 1024 |  | √ | ' ' |  |
| 28 | fsummary_tag | fsummary_tag | text | 0 |  |  | null |  |
| 29 | fdescription | fdescription | varchar | 255 |  | √ | ' ' |  |
| 30 | fctrlstrategy | fctrlstrategy | varchar | 50 |  | √ | ' ' |  |
| 31 | fownerid | fownerid | int8 | 64 |  | √ | 0 |  |
| 32 | ffolderdomain | ffolderdomain | int8 | 64 |  | √ | 0 |  |
| 33 | fenable | fenable | varchar | 50 |  | √ | ' ' |  |
| 34 | fnumber | 编码 | varchar | 85 |  | √ | ' ' | 编码 |
| 35 | fcadeditstatus | fcadeditstatus | bpchar | 1 |  | √ | '0' |  |
| 36 | fsourcebitindex | fsourcebitindex | int8 | 64 |  | √ | 0 |  |
| 37 | fmodelnum | fmodelnum | varchar | 255 |  | √ | ' ' |  |
| 38 | fsummary | fsummary | varchar | 255 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_plm_pdm_basic_createorg |  | fcreateorgid |
| 2 | pk_plm_pdm_basic |  | fid |
| 3 | idx_t_plm_pdm_basic_master |  | fmasterid |
| 4 | idx_plm_pdm_basic_name |  | fname |
| 5 | idx_plm_pdm_basic_modelid |  | fmodelid |
| 6 | idx_plm_pdm_basic_number |  | fnumber |
