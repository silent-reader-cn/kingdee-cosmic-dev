# 星空企业版第三方应用-xkinteg_trdapp_config

## 星空企业版第三方应用-主表 t_xkinteg_trdapp_config

- **表名称：** 星空企业版第三方应用-主表
- **表名：** t_xkinteg_trdapp_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 5 | fappsecret | 应用秘钥 | varchar | 500 |  | √ | ' ' | 应用秘钥 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | forgid | forgid | int8 | 64 |  | √ | 0 |  |
| 8 | fapptypeid | 应用类型 | varchar | 36 |  | √ | ' ' | [业务应用实体 bos_devportal_bizapp](../mdl_files/bos_devportal_bizapp.md) |
| 9 | fappid | 应用 Id | varchar | 500 |  | √ | ' ' | 应用 Id |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fdbid | 企业版数据中心 Id | varchar | 200 |  | √ | ' ' | 企业版数据中心 Id |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 15 | fappname | 应用名称 | varchar | 100 |  | √ | ' ' | 应用名称 |
| 16 | fdbname | 企业版数据中心名称 | varchar | 100 |  | √ | ' ' | 企业版数据中心名称 |
| 17 | furl | 企业版访问地址 | varchar | 500 |  | √ | ' ' | 企业版访问地址 |
| 18 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 20 | fxkuserlinktype | fxkuserlinktype | bpchar | 1 |  | √ | ' ' |  |
| 21 | flangid | 默认语言Id | varchar | 50 |  | √ | ' ' | 默认语言Id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_xkinteg_trdapp_config_dbid |  | fdbid |
| 2 | pk_xkinteg_trdapp_config |  | fid |

---

## 星空企业版第三方应用-多语言表 t_xkinteg_trdapp_config_l

- **表名称：** 星空企业版第三方应用-多语言表
- **表名：** t_xkinteg_trdapp_config_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fappname | 应用名称 | varchar | 80 |  | √ | ' ' | 应用名称 |
| 4 | fdbname | 企业版数据中心名称 | varchar | 100 |  |  | null | 企业版数据中心名称 |
| 5 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 6 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_xkinteg_trdapp_config_l |  | fpkid |
| 2 | idx_xkinteg_trdapp_config_l |  | fid,flocaleid |
