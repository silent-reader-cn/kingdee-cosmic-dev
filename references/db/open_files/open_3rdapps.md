# 第三方应用（废弃）-open_3rdapps

## 第三方应用（废弃）-多语言表 t_open_3rdapps_l

- **表名称：** 第三方应用（废弃）-多语言表
- **表名：** t_open_3rdapps_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 系统名称 | varchar | 600 |  | √ | ' ' | 系统名称 |
| 3 | fdiscription | fdiscription | varchar | 500 |  | √ | ' ' |  |
| 4 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_open_3rdapps_l_pkey |  | fpkid |
| 2 | idx_t_open_3rdapps_l_fid |  | fid,flocaleid |

---

## 第三方应用（废弃）-主表 t_open_3rdapps

- **表名称：** 第三方应用（废弃）-主表
- **表名：** t_open_3rdapps

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisenhancetoken | fisenhancetoken | bpchar | 1 |  | √ | '0' |  |
| 3 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 4 | fwhitelist | 白名单 | varchar | 256 |  | √ | ' ' | 白名单 |
| 5 | fsecuritypublickey | JWT非对称秘钥 | varchar | 2048 |  | √ | ' ' | JWT非对称秘钥 |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcontact | fcontact | int8 | 64 |  | √ | 0 |  |
| 8 | fgatewayappid | fgatewayappid | varchar | 50 |  | √ | ' ' |  |
| 9 | fisbasicauth | fisbasicauth | bpchar | 1 |  | √ | '0' |  |
| 10 | fisallowalluser | fisallowalluser | bpchar | 1 |  | √ | '1' |  |
| 11 | fjwtasymmetic | 是否启用jwt对称加密 | bpchar | 1 |  | √ | ' ' | 是否启用jwt对称加密 |
| 12 | fencryption | fencryption | int8 | 64 |  | √ | 0 |  |
| 13 | fallowallapi | fallowallapi | bpchar | 1 |  | √ | '1' |  |
| 14 | fname | 系统名称 | varchar | 600 |  | √ | ' ' | 系统名称 |
| 15 | fauthpluginenable | fauthpluginenable | bpchar | 1 |  | √ | '0' |  |
| 16 | fjwtsigntype | fjwtsigntype | int8 | 64 |  | √ | 0 |  |
| 17 | fjwtshakey | fjwtshakey | varchar | 256 |  | √ | ' ' |  |
| 18 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 19 | fisencryptallapi | fisencryptallapi | bpchar | 1 |  | √ | '0' |  |
| 20 | fisgatewayapp | fisgatewayapp | bpchar | 1 |  | √ | '0' |  |
| 21 | fisresultsign | fisresultsign | bpchar | 1 |  | √ | '0' |  |
| 22 | fisjwtauth | fisjwtauth | bpchar | 1 |  | √ | '0' |  |
| 23 | fsrctype | fsrctype | bpchar | 1 |  | √ | '1' |  |
| 24 | fpublickey | 对称加密秘钥 | varchar | 256 |  | √ | ' ' | 对称加密秘钥 |
| 25 | flastenabletime | 系统最后启用时间 | timestamp | 0 |  |  | null | 系统最后启用时间 |
| 26 | fisdigestauth | fisdigestauth | bpchar | 1 |  | √ | '0' |  |
| 27 | fenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 系统编码 | varchar | 100 |  | √ | ' ' | 系统编码 |
| 29 | fsigntype | fsigntype | int8 | 64 |  | √ | 0 |  |
| 30 | fcountry | fcountry | int8 | 64 |  | √ | 0 |  |
| 31 | fsecurityprivatekey | 私钥 | varchar | 2048 |  | √ | ' ' | 私钥 |
| 32 | fapptype | fapptype | bpchar | 1 |  | √ | '0' |  |
| 33 | fsignshakey | fsignshakey | varchar | 256 |  | √ | ' ' |  |
| 34 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 37 | fpresetappid | fpresetappid | varchar | 50 |  | √ | ' ' |  |
| 38 | flaststoptime | 系统最后停止时间 | timestamp | 0 |  |  | null | 系统最后停止时间 |
| 39 | fisagencyuser | fisagencyuser | bpchar | 1 |  | √ | '0' |  |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fpwdlength | fpwdlength | int8 | 64 |  |  | null |  |
| 42 | fissignauth | fissignauth | bpchar | 1 |  | √ | '0' |  |
| 43 | fk_kdxk_accountid | fk_kdxk_accountid | varchar | 50 |  | √ | ' ' |  |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 45 | fculimittac | fculimittac | int8 | 64 |  | √ | 0 |  |
| 46 | fsyspwd | 系统密码 | varchar | 1024 |  | √ | ' ' | 系统密码 |
| 47 | fis_preset | fis_preset | bpchar | 1 |  | √ | '0' |  |
| 48 | fallowip | fallowip | bpchar | 1 |  | √ | '1' |  |
| 49 | fdiscription | fdiscription | varchar | 500 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_open_3rdapps_pkey |  | fid |
| 2 | idx_t_open_3rdapps_fnumber |  | fnumber |
| 3 | idx_open_3rdapps_fid |  | fid |
