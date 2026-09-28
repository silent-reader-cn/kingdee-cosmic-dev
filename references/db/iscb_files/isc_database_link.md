# 连接器配置-isc_database_link

## 连接器配置-主表 t_isc_database_link

- **表名称：** 连接器配置-主表
- **表名：** t_isc_database_link

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappsecret | 开放应用密码（废弃） | varchar | 100 |  | √ | ' ' | 开放应用密码（废弃） |
| 3 | fserver_ip | 服务器IP或域名 | varchar | 250 |  | √ | ' ' | 服务器IP或域名 |
| 4 | fappsecret_new | 开放应用密码 | varchar | 100 |  | √ | ' ' | 开放应用密码 |
| 5 | fsourceapp | 所属应用 | varchar | 50 |  | √ | ' ' | 所属应用 |
| 6 | fattr_8 | 自定义属性_8 | varchar | 2000 |  | √ | ' ' | 自定义属性_8 |
| 7 | fattr_9 | 自定义属性_9 | varchar | 2000 |  | √ | ' ' | 自定义属性_9 |
| 8 | fdata_center | 数据中心 | varchar | 100 |  | √ | ' ' | 数据中心 |
| 9 | faccount | 账套ID | varchar | 100 |  | √ | ' ' | 账套ID |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fattr_2 | 自定义属性_2 | varchar | 50 |  | √ | ' ' | 自定义属性_2 |
| 12 | fattr_3 | 自定义属性_3 | varchar | 50 |  | √ | ' ' | 自定义属性_3 |
| 13 | fattr_1 | 自定义属性_1 | varchar | 50 |  | √ | ' ' | 自定义属性_1 |
| 14 | fattr_6 | 自定义属性_6 | varchar | 50 |  | √ | ' ' | 自定义属性_6 |
| 15 | fattr_7 | 自定义属性_7 | varchar | 2000 |  | √ | ' ' | 自定义属性_7 |
| 16 | fattr_4 | 自定义属性_4 | varchar | 50 |  | √ | ' ' | 自定义属性_4 |
| 17 | fattr_5 | 自定义属性_5 | varchar | 50 |  | √ | ' ' | 自定义属性_5 |
| 18 | flicense_info | 许可状态（该属性在运行期禁止访问） | varchar | 20 |  | √ | ' ' | 许可状态（该属性在运行期禁止访问）,枚举: free :默认免费 yes :正常 no :许可不足 expired :许可失效 |
| 19 | fdum_link | 连接类型 | varchar | 18 |  | √ | ' ' | [连接类型 isc_connection_type](../iscb_files/isc_connection_type.md) |
| 20 | foracle_service | Oracle服务 | varchar | 100 |  | √ | ' ' | Oracle服务 |
| 21 | fattr_e1 | 自定义属性_10 | varchar | 100 |  | √ | ' ' | 自定义属性_10 |
| 22 | fattr_e2 | 自定义属性_11 | varchar | 100 |  | √ | ' ' | 自定义属性_11 |
| 23 | fprivacy_domains | 所属国家地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |
| 24 | flicense_sn | 许可序号（该属性在运行期禁止访问） | int8 | 64 |  | √ | 0 | 许可序号（该属性在运行期禁止访问） |
| 25 | fnewpwd | 登录密码 | varchar | 100 |  | √ | ' ' | 登录密码 |
| 26 | fweb_app | Web应用名 | varchar | 100 |  | √ | ' ' | Web应用名 |
| 27 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 29 | fcurrent_account_id | 所属账套ID | varchar | 100 |  | √ | ' ' | 所属账套ID |
| 30 | feas_service | EAS服务 | varchar | 100 |  | √ | ' ' | EAS服务 |
| 31 | fappsecret_new_enp | fappsecret_new_enp | text | 0 |  |  | null |  |
| 32 | fattr_e2_enp | fattr_e2_enp | text | 0 |  |  | null |  |
| 33 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 34 | fcircuit_break_rule | 熔断规则 | int8 | 64 |  | √ | 0 | [熔断规则 isc_circuit_breaker_rule](../iscb_files/isc_circuit_breaker_rule.md) |
| 35 | fpassword | 登录密码（废弃） | varchar | 100 |  | √ | ' ' | 登录密码（废弃） |
| 36 | fsql_database | 数据库名 | varchar | 100 |  | √ | ' ' | 数据库名 |
| 37 | fappid | 开放应用编码 | varchar | 100 |  | √ | ' ' | 开放应用编码 |
| 38 | ftoken_cache_strategy | Token缓存策略 | varchar | 10 |  | √ | ' ' | Token缓存策略,枚举: DCS :全局（分布式缓存） JVM :本地（JVM） |
| 39 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 42 | fdatabase_type | 连接类型 | varchar | 30 |  | √ | ' ' | 连接类型,枚举: eas :EAS系统 self :当前账套 k3cloud :金蝶云·星空 ierp :金蝶云·苍穹 CurrentDB :当前数据库 db_proxy :数据库代理 oracle :Oracle sqlserver :SQL Server mysql :MySQL PostgreSQL_New :PostgreSQL（新版） PostgreSQL :PostgreSQL DM :达梦数据库 Hive :Hive FTP :FTP FTP(apache) :FTP(apache) SFTP(jsch) :SFTP(jsch) EAS-API :EAS-API K3Cloud-API :星空-API IERP-API :苍穹-API SAP-RFC :SAP系统 CloudHub :云之家 WeChat :企业微信 DingDing :钉钉 WeLink :WeLink SCM-JD :京东 SCM-JDPRO :京东工业品 SCM-SN :苏宁 SCM-XY :西域 SCM-CG :晨光 SCM-DL :得力 TAXC-ZWY :账无忧 TAXC-GZTAX :广州税局 TCID :腾讯云IDaaS DummyConnector :哑连接 isc_hub :集成云HUB TMS_KD100 :快递100 FeiShu :飞书 Salesforce :Salesforce YuQue :语雀 FaDaDa :法大大 Zoho :卓豪 Neocrm :销售易 SCM-JDJOS :京东宙斯 eteams :泛微移动办公云OA Seeyon :致远OA Youzan :有赞云 1688 :阿里巴巴 TianYanCha :天眼查 IK-CRM :爱客CRM FXiaoKe :纷享销客 YXC_API :金蝶云星辰 JDY_YJXC :精斗云云进销存 UserDefineDbDriver :自定义数据库类型 |
| 43 | ficid | 语言 | varchar | 100 |  | √ | ' ' | 语言,枚举: zh_CN :简体中文 zh_TW :繁体中文 en_US :英文 |
| 44 | fserver_port | 服务器端口 | varchar | 100 |  | √ | ' ' | 服务器端口 |
| 45 | fattr_e1_enp | fattr_e1_enp | text | 0 |  |  | null |  |
| 46 | fdb_route | fdb_route | varchar | 30 |  | √ | ' ' |  |
| 47 | fhttp_protocal | HTTP协议 | varchar | 30 |  | √ | ' ' | HTTP协议,枚举: http :http https :https |
| 48 | ftenant | 租户ID | varchar | 100 |  | √ | ' ' | 租户ID |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fcharset | 字符集 | varchar | 100 |  | √ | ' ' | 字符集 |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fuser | 登录用户 | varchar | 100 |  | √ | ' ' | 登录用户 |
| 53 | fhas_assign_perm | 已分配权限 | bpchar | 1 |  | √ | '0' | 已分配权限 |
| 54 | fdeploy_state | 部署状态 | bpchar | 1 |  | √ | ' ' | 部署状态,枚举: N :未部署 Y :已部署 F :部署失败 |
| 55 | fstate | 连接状态 | varchar | 30 |  | √ | ' ' | 连接状态,枚举: F :异常 S :活跃 :未知 |
| 56 | fsource_system | 来源系统 | int8 | 64 |  | √ | 0 | [来源系统 isc_ds_srcsys](../iscb_files/isc_ds_srcsys.md) |
| 57 | fierp_proxy_user | 当前账套回调代理用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 58 | fnewpwd_enp | fnewpwd_enp | text | 0 |  |  | null |  |
| 59 | fmax_tps | 流量控制（次/秒） | int8 | 64 |  | √ | 0 | 流量控制（次/秒） |
| 60 | fcombofield | fcombofield | varchar | 30 |  | √ | ' ' |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_database_link_0 |  | fdatabase_type |
| 2 | t_isc_database_link_pkey |  | fid |

---

## 连接器配置-多语言表 t_isc_database_link_l

- **表名称：** 连接器配置-多语言表
- **表名：** t_isc_database_link_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_database_link_l_0 |  | flocaleid,fid |
| 2 | t_isc_database_link_l_pkey |  | fpkid |
