# 新增第三方应用-xkopenthird_app_new

## 代理用户-多选基础资料表 t_open_3rdapps_agency

- **表名称：** 代理用户-多选基础资料表
- **表名：** t_open_3rdapps_agency

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_3rdapps_agency |  | fpkid |
| 2 | index_apps_agency_user_fid |  | fid |

---

## 新增第三方应用-多语言表 t_open_3rdapps_l

- **表名称：** 新增第三方应用-多语言表
- **表名：** t_open_3rdapps_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 系统名称 | varchar | 600 |  | √ | ' ' | 系统名称 |
| 3 | fdiscription | 详细描述 | varchar | 500 |  | √ | ' ' | 详细描述 |
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

## 新增第三方应用-主表 t_open_3rdapps

- **表名称：** 新增第三方应用-主表
- **表名：** t_open_3rdapps

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisenhancetoken | 是否启用增强token认证 | bpchar | 1 |  | √ | '0' | 是否启用增强token认证 |
| 3 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 4 | fwhitelist | fwhitelist | varchar | 256 |  | √ | ' ' |  |
| 5 | fsecuritypublickey | fsecuritypublickey | varchar | 2048 |  | √ | ' ' |  |
| 6 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 7 | fcontact | 应用联系人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fgatewayappid | fgatewayappid | varchar | 50 |  | √ | ' ' |  |
| 9 | fisbasicauth | fisbasicauth | bpchar | 1 |  | √ | '0' |  |
| 10 | fisallowalluser | fisallowalluser | bpchar | 1 |  | √ | '1' |  |
| 11 | fjwtasymmetic | fjwtasymmetic | bpchar | 1 |  | √ | ' ' |  |
| 12 | fencryption | fencryption | int8 | 64 |  | √ | 0 |  |
| 13 | fallowallapi | 授权全部API | bpchar | 1 |  | √ | '1' | 授权全部API |
| 14 | fname | 系统名称 | varchar | 600 |  | √ | ' ' | 系统名称 |
| 15 | fauthpluginenable | fauthpluginenable | bpchar | 1 |  | √ | '0' |  |
| 16 | fjwtsigntype | fjwtsigntype | int8 | 64 |  | √ | 0 |  |
| 17 | fjwtshakey | fjwtshakey | varchar | 256 |  | √ | ' ' |  |
| 18 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 19 | fisencryptallapi | fisencryptallapi | bpchar | 1 |  | √ | '0' |  |
| 20 | fisgatewayapp | 是否网关应用 | bpchar | 1 |  | √ | '0' | 是否网关应用 |
| 21 | fisresultsign | fisresultsign | bpchar | 1 |  | √ | '0' |  |
| 22 | fisjwtauth | fisjwtauth | bpchar | 1 |  | √ | '0' |  |
| 23 | fsrctype | fsrctype | bpchar | 1 |  | √ | '1' |  |
| 24 | fpublickey | fpublickey | varchar | 256 |  | √ | ' ' |  |
| 25 | flastenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 26 | fisdigestauth | fisdigestauth | bpchar | 1 |  | √ | '0' |  |
| 27 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 系统编码 | varchar | 100 |  | √ | ' ' | 系统编码 |
| 29 | fsigntype | fsigntype | int8 | 64 |  | √ | 0 |  |
| 30 | fcountry | fcountry | int8 | 64 |  | √ | 0 |  |
| 31 | fsecurityprivatekey | fsecurityprivatekey | varchar | 2048 |  | √ | ' ' |  |
| 32 | fapptype | 系统类型 | bpchar | 1 |  | √ | '0' | 系统类型,枚举: 0 :自建 1 :预置 |
| 33 | fsignshakey | fsignshakey | varchar | 256 |  | √ | ' ' |  |
| 34 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 35 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 36 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 37 | fpresetappid | fpresetappid | varchar | 50 |  | √ | ' ' |  |
| 38 | flaststoptime | 停止时间 | timestamp | 0 |  |  | null | 停止时间 |
| 39 | fisagencyuser | 启用代理用户控制 | bpchar | 1 |  | √ | '0' | 启用代理用户控制 |
| 40 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fpwdlength | fpwdlength | int8 | 64 |  |  | null |  |
| 42 | fissignauth | fissignauth | bpchar | 1 |  | √ | '0' |  |
| 43 | fk_kdxk_accountid | fk_kdxk_accountid | varchar | 50 |  | √ | ' ' |  |
| 44 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 45 | fculimittac | 限流策略（次/秒） | int8 | 64 |  | √ | 0 | 限流策略（次/秒） |
| 46 | fsyspwd | fsyspwd | varchar | 1024 |  | √ | ' ' |  |
| 47 | fis_preset | fis_preset | bpchar | 1 |  | √ | '0' |  |
| 48 | fallowip | fallowip | bpchar | 1 |  | √ | '1' |  |
| 49 | fdiscription | 详细描述 | varchar | 500 |  | √ | ' ' | 详细描述 |

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
