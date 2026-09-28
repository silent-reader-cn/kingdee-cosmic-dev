# 第三方应用-third_app

## 访问策略-子表 t_openapi_strategy

- **表名称：** 访问策略-子表
- **表名：** t_openapi_strategy

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fstrategytypeid | 策略类型ID | int8 | 64 |  | √ | 0 | 访问策略类型 access_strategy_type |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_openapi_strategy |  | fentryid |
| 2 | idx_openapi_strategy_fid |  | fid |

---

## 代理用户分录-子表 t_open_3rdapps_basicauth

- **表名称：** 代理用户分录-子表
- **表名：** t_open_3rdapps_basicauth

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fremark | 备注 | varchar | 50 |  | √ | 'open' | 备注 |
| 3 | fbasesigncode | Secret Key | varchar | 500 |  | √ | ' ' | Secret Key |
| 4 | fstatus | 是否有效 | bpchar | 1 |  | √ | ' ' | 是否有效 |
| 5 | ftype | 类型 | bpchar | 1 |  | √ | '0' | 类型,枚举: |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fthirdsecconfigid | fthirdsecconfigid | int8 | 64 |  | √ | 0 |  |
| 8 | fendtime | fendtime | timestamp | 0 |  |  | null |  |
| 9 | fsystag | 系统标识 | varchar | 50 |  | √ | 'open' | 系统标识 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | fagentuserid | 代理用户 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fstarttime | fstarttime | timestamp | 0 |  |  | null |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_3rdapps_basicauth |  | fentryid |
| 2 | idx_un_open_basesigncode |  | fbasesigncode |
| 3 | idx_basicauth_thirdsecconfid |  | fthirdsecconfigid |
| 4 | idx_open_3rdapps_basicauth_fid |  | fid |

---

## 第三方应用-主表 t_open_3rdapps

- **表名称：** 第三方应用-主表
- **表名：** t_open_3rdapps

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisenhancetoken | 是否启用增强token认证 | bpchar | 1 |  | √ | '0' | 是否启用增强token认证 |
| 3 | fsecurityprivatekey | 私钥 | varchar | 2048 |  | √ | ' ' | 私钥 |
| 4 | fapptype | 系统类型 | bpchar | 1 |  | √ | '0' | 系统类型,枚举: 0 :自建 1 :预置 |
| 5 | fdisabledate | fdisabledate | timestamp | 0 |  |  | null |  |
| 6 | fwhitelist | fwhitelist | varchar | 256 |  | √ | ' ' |  |
| 7 | fsecuritypublickey | fsecuritypublickey | varchar | 2048 |  | √ | ' ' |  |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fsignshakey | 认证密钥 | varchar | 256 |  | √ | ' ' | 认证密钥 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'A' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fpresetappid | 预置应用模版id | varchar | 50 |  | √ | ' ' | 预置应用模版id |
| 14 | fcontact | 应用联系人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fgatewayappid | 网关侧APP主键ID | varchar | 50 |  | √ | ' ' | 网关侧APP主键ID |
| 16 | fisbasicauth | 启用基本认证 | bpchar | 1 |  | √ | '0' | 启用基本认证 |
| 17 | flaststoptime | 停止时间 | timestamp | 0 |  |  | null | 停止时间 |
| 18 | fisallowalluser | fisallowalluser | bpchar | 1 |  | √ | '1' |  |
| 19 | fisagencyuser | 启用代理用户控制 | bpchar | 1 |  | √ | '0' | 启用代理用户控制 |
| 20 | fjwtasymmetic | fjwtasymmetic | bpchar | 1 |  | √ | ' ' |  |
| 21 | fencryption | API加密策略(存库) | int8 | 64 |  | √ | 0 | API加密策略(存库) |
| 22 | fallowallapi | 授权全部API | bpchar | 1 |  | √ | '1' | 授权全部API |
| 23 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 24 | fpwdlength | fpwdlength | int8 | 64 |  |  | null |  |
| 25 | fname | 系统名称 | varchar | 200 |  | √ | ' ' | 系统名称 |
| 26 | fissignauth | 启用签名认证 | bpchar | 1 |  | √ | '0' | 启用签名认证 |
| 27 | fauthpluginenable | 认证插件启用 | bpchar | 1 |  | √ | '0' | 认证插件启用 |
| 28 | fk_kdxk_accountid | accountId | varchar | 50 |  | √ | ' ' | accountId |
| 29 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 30 | fjwtsigntype | JWT签名策略(存库) | int8 | 64 |  | √ | 0 | JWT签名策略(存库) |
| 31 | fjwtshakey | 认证密钥 | varchar | 256 |  | √ | ' ' | 认证密钥 |
| 32 | fdisablerid | fdisablerid | int8 | 64 |  |  | null |  |
| 33 | fisencryptallapi | 加密全部API | bpchar | 1 |  | √ | '0' | 加密全部API |
| 34 | fculimittac | 限流策略（次/秒） | int8 | 64 |  | √ | 0 | 限流策略（次/秒） |
| 35 | fisgatewayapp | 是否网关应用 | bpchar | 1 |  | √ | '0' | 是否网关应用 |
| 36 | fisresultsign | fisresultsign | bpchar | 1 |  | √ | '0' |  |
| 37 | fsyspwd | AccessToken认证密钥 | varchar | 1024 |  | √ | ' ' | AccessToken认证密钥 |
| 38 | fisjwtauth | 启用JWT认证 | bpchar | 1 |  | √ | '0' | 启用JWT认证 |
| 39 | fsrctype | 来源 | bpchar | 1 |  | √ | '1' | 来源,枚举: 1 :开放平台 2 :集成 3 :KEM |
| 40 | fis_preset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 41 | fallowip | 允许全部IP访问 | bpchar | 1 |  | √ | '1' | 允许全部IP访问 |
| 42 | fpublickey | 认证密钥 | varchar | 256 |  | √ | ' ' | 认证密钥 |
| 43 | fdiscription | 详细描述 | varchar | 500 |  | √ | ' ' | 详细描述 |
| 44 | flastenabletime | 启用时间 | timestamp | 0 |  |  | null | 启用时间 |
| 45 | fisdigestauth | 启用摘要认证 | bpchar | 1 |  | √ | '0' | 启用摘要认证 |
| 46 | fenable | 是否启用 | bpchar | 1 |  | √ | '1' | 是否启用,枚举: 0 :禁用 1 :可用 |
| 47 | fnumber | 系统编码 | varchar | 20 |  | √ | ' ' | 系统编码 |
| 48 | fsigntype | 签名加密策略(存库) | int8 | 64 |  | √ | 0 | 签名加密策略(存库) |

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

## 代理用户-多选基础资料表 t_open_3rdapps_agency

- **表名称：** 代理用户-多选基础资料表
- **表名：** t_open_3rdapps_agency

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | 人员 bos_user |
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

## IP白名单分录-子表 t_open_3rdapps_ips

- **表名称：** IP白名单分录-子表
- **表名：** t_open_3rdapps_ips

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fstartip | 起始IP | varchar | 50 |  | √ | ' ' | 起始IP |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fpolicytype | IP策略 | bpchar | 1 |  | √ | '0' | IP策略,枚举: 0 :白名单 1 :黑名单 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fendip | 结束IP | varchar | 50 |  | √ | ' ' | 结束IP |
| 7 | fiptype | IP类型 | bpchar | 1 |  | √ | '1' | IP类型,枚举: 1 :IPv4 2 :IPv6 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_open_3rd_ip_fid |  | fid |
| 2 | pk_t_open_3rdapps_ips |  | fentryid |

---

## API加密策略分录-子表 t_open_3rdapps_encryptapi

- **表名称：** API加密策略分录-子表
- **表名：** t_open_3rdapps_encryptapi

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapiid | API编码 | int8 | 64 |  | √ | 0 | API服务 openapi_apilist |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fthirdsecconfigid | fthirdsecconfigid | int8 | 64 |  | √ | 0 |  |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 6 | fencryption | fencryption | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_3rdapps_encryptapi |  | fentryid |
| 2 | idx_open_3rapps_enthird |  | fid |
| 3 | idx_open_fapiid |  | fapiid |

---

## 第三方应用-多语言表 t_open_3rdapps_l

- **表名称：** 第三方应用-多语言表
- **表名：** t_open_3rdapps_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 系统名称 | varchar | 200 |  | √ | ' ' | 系统名称 |
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

## API授权分录-子表 t_open_3rdappsapis

- **表名称：** API授权分录-子表
- **表名：** t_open_3rdappsapis

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapiserviceid | API编码 | int8 | 64 |  | √ | 0 | API服务 openapi_apilist |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_3rdappsapis |  | fid |
| 2 | pk_open_3rdappsapis |  | fentryid |

---

## SSO可信白名单分录-子表 t_open_3rdapps_ssoip

- **表名称：** SSO可信白名单分录-子表
- **表名：** t_open_3rdapps_ssoip

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdomain_ip | 域名/IP | varchar | 200 |  | √ | ' ' | 域名/IP |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_open_3rdapps_ssoip_fid |  | fid |
| 2 | pk_t_open_3rdapps_ssoip |  | fentryid |

---

## 第三方应用-分表 t_open_3rdapps_g

- **表名称：** 第三方应用-分表
- **表名：** t_open_3rdapps_g

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fappsecret | appSecret | varchar | 255 |  | √ | ' ' | appSecret |
| 3 | fappkey | appId | varchar | 50 |  | √ | ' ' | appId |
| 4 | fgatewayappid | fgatewayappid | varchar | 50 |  | √ | ' ' |  |
| 5 | facgw_identity | x-acgw-identity | varchar | 255 |  | √ | ' ' | x-acgw-identity |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_open_3rdapps_g |  | fid |
| 2 | idx_t_open_3rdapps_g |  | fappkey |
