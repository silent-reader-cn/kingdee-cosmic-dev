# 第三方应用（废弃）-open_3rdapps

## 第三方应用（废弃）-主表 t_open_3rdapps

- **表名称：** 第三方应用（废弃）-主表
- **表名：** t_open_3rdapps

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisenhancetoken | fisenhancetoken | bpchar | 1 |  | √ | '0' |  |
| 3 | fsecurityprivatekey | 私钥 | varchar | 2048 |  | √ | ' ' | 私钥 |
| 4 | fapptype | fapptype | bpchar | 1 |  | √ | '0' |  |
| 5 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 6 | fwhitelist | 白名单 | varchar | 256 |  | √ | ' ' | 白名单 |
| 7 | fsecuritypublickey | JWT非对称秘钥 | varchar | 2048 |  | √ | ' ' | JWT非对称秘钥 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsignshakey | fsignshakey | varchar | 256 |  | √ | ' ' |  |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fpresetappid | fpresetappid | varchar | 50 |  | √ | ' ' |  |
| 14 | fcontact | fcontact | int8 | 64 |  | √ | 0 |  |
| 15 | fgatewayappid | fgatewayappid | varchar | 50 |  | √ | ' ' |  |
| 16 | fisbasicauth | fisbasicauth | bpchar | 1 |  | √ | '0' |  |
| 17 | flaststoptime | 系统最后停止时间 | timestamp | 0 |  |  | null | 系统最后停止时间 |
| 18 | fisallowalluser | fisallowalluser | bpchar | 1 |  | √ | '1' |  |
| 19 | fisagencyuser | fisagencyuser | bpchar | 1 |  | √ | '0' |  |
| 20 | fjwtasymmetic | 是否启用jwt对称加密 | bpchar | 1 |  | √ | ' ' | 是否启用jwt对称加密 |
| 21 | fencryption | fencryption | int8 | 64 |  | √ | 0 |  |
| 22 | fallowallapi | fallowallapi | bpchar | 1 |  | √ | '1' |  |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fpwdlength | fpwdlength | int8 | 64 |  |  | null |  |
| 25 | fname | fname | varchar | 200 |  | √ | ' ' |  |
| 26 | fissignauth | fissignauth | bpchar | 1 |  | √ | '0' |  |
| 27 | fauthpluginenable | fauthpluginenable | bpchar | 1 |  | √ | '0' |  |
| 28 | fk_kdxk_accountid | fk_kdxk_accountid | varchar | 50 |  | √ | ' ' |  |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 30 | fjwtsigntype | fjwtsigntype | int8 | 64 |  | √ | 0 |  |
| 31 | fjwtshakey | fjwtshakey | varchar | 256 |  | √ | ' ' |  |
| 32 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 33 | fisencryptallapi | fisencryptallapi | bpchar | 1 |  | √ | '0' |  |
| 34 | fculimittac | fculimittac | int8 | 64 |  | √ | 0 |  |
| 35 | fisgatewayapp | fisgatewayapp | bpchar | 1 |  | √ | '0' |  |
| 36 | fisresultsign | fisresultsign | bpchar | 1 |  | √ | '0' |  |
| 37 | fsyspwd | 系统密码 | varchar | 1024 |  | √ | ' ' | 系统密码 |
| 38 | fisjwtauth | fisjwtauth | bpchar | 1 |  | √ | '0' |  |
| 39 | fsrctype | fsrctype | bpchar | 1 |  | √ | '1' |  |
| 40 | fis_preset | fis_preset | bpchar | 1 |  | √ | '0' |  |
| 41 | fallowip | fallowip | bpchar | 1 |  | √ | '1' |  |
| 42 | fpublickey | 对称加密秘钥 | varchar | 256 |  | √ | ' ' | 对称加密秘钥 |
| 43 | fdiscription | fdiscription | varchar | 500 |  | √ | ' ' |  |
| 44 | flastenabletime | 系统最后启用时间 | timestamp | 0 |  |  | null | 系统最后启用时间 |
| 45 | fisdigestauth | fisdigestauth | bpchar | 1 |  | √ | '0' |  |
| 46 | fenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用,枚举: 0 :禁用 1 :可用 |
| 47 | fnumber | 系统编码 | varchar | 20 |  | √ | ' ' | 系统编码 |
| 48 | fsigntype | fsigntype | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_open_3rdapps_pkey |  | fid |
| 2 | idx_t_open_3rdapps_fnumber |  | fnumber |

---

## 第三方应用（废弃）-多语言表 t_open_3rdapps_l

- **表名称：** 第三方应用（废弃）-多语言表
- **表名：** t_open_3rdapps_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 系统名称 | varchar | 200 |  | √ | ' ' | 系统名称 |
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
