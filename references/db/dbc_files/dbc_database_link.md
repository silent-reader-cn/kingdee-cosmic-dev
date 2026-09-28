# 数据库连接-dbc_database_link

## 数据库连接-多语言表 t_isc_database_link_l

- **表名称：** 数据库连接-多语言表
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

---

## 数据库连接-主表 t_isc_database_link

- **表名称：** 数据库连接-主表
- **表名：** t_isc_database_link

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fappsecret | fappsecret | varchar | 100 |  | √ | ' ' |  |
| 3 | fserver_ip | 服务器IP或域名 | varchar | 250 |  | √ | ' ' | 服务器IP或域名 |
| 4 | fappsecret_new | fappsecret_new | varchar | 100 |  | √ | ' ' |  |
| 5 | fsourceapp | fsourceapp | varchar | 50 |  | √ | ' ' |  |
| 6 | fattr_8 | fattr_8 | varchar | 2000 |  | √ | ' ' |  |
| 7 | fattr_9 | fattr_9 | varchar | 2000 |  | √ | ' ' |  |
| 8 | fdata_center | fdata_center | varchar | 100 |  | √ | ' ' |  |
| 9 | faccount | faccount | varchar | 100 |  | √ | ' ' |  |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fattr_2 | fattr_2 | varchar | 50 |  | √ | ' ' |  |
| 12 | fattr_3 | fattr_3 | varchar | 50 |  | √ | ' ' |  |
| 13 | fattr_1 | fattr_1 | varchar | 50 |  | √ | ' ' |  |
| 14 | fattr_6 | fattr_6 | varchar | 50 |  | √ | ' ' |  |
| 15 | fattr_7 | fattr_7 | varchar | 2000 |  | √ | ' ' |  |
| 16 | fattr_4 | fattr_4 | varchar | 50 |  | √ | ' ' |  |
| 17 | fattr_5 | fattr_5 | varchar | 50 |  | √ | ' ' |  |
| 18 | flicense_info | 许可状态（该属性在运行期禁止访问） | varchar | 20 |  | √ | ' ' | 许可状态（该属性在运行期禁止访问）,枚举: free :默认免费 yes :正常 no :许可不足 expired :许可失效 |
| 19 | fdum_link | fdum_link | varchar | 18 |  | √ | ' ' |  |
| 20 | foracle_service | Oracle服务 | varchar | 100 |  | √ | ' ' | Oracle服务 |
| 21 | fattr_e1 | fattr_e1 | varchar | 100 |  | √ | ' ' |  |
| 22 | fattr_e2 | fattr_e2 | varchar | 100 |  | √ | ' ' |  |
| 23 | fprivacy_domains | fprivacy_domains | int8 | 64 |  | √ | 0 |  |
| 24 | flicense_sn | 许可序号（该属性在运行期禁止访问） | int8 | 64 |  | √ | 0 | 许可序号（该属性在运行期禁止访问） |
| 25 | fnewpwd | fnewpwd | varchar | 100 |  | √ | ' ' |  |
| 26 | fweb_app | fweb_app | varchar | 100 |  | √ | ' ' |  |
| 27 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 29 | fcurrent_account_id | fcurrent_account_id | varchar | 100 |  | √ | ' ' |  |
| 30 | feas_service | feas_service | varchar | 100 |  | √ | ' ' |  |
| 31 | fappsecret_new_enp | fappsecret_new_enp | text | 0 |  |  | null |  |
| 32 | fattr_e2_enp | fattr_e2_enp | text | 0 |  |  | null |  |
| 33 | fisv | fisv | varchar | 100 |  | √ | ' ' |  |
| 34 | fcircuit_break_rule | fcircuit_break_rule | int8 | 64 |  | √ | 0 |  |
| 35 | fpassword | fpassword | varchar | 100 |  | √ | ' ' |  |
| 36 | fsql_database | 数据库名 | varchar | 100 |  | √ | ' ' | 数据库名 |
| 37 | fappid | fappid | varchar | 100 |  | √ | ' ' |  |
| 38 | ftoken_cache_strategy | ftoken_cache_strategy | varchar | 10 |  | √ | ' ' |  |
| 39 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 40 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 41 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 42 | fdatabase_type | 类型 | varchar | 30 |  | √ | ' ' | 类型,枚举: mysql :MySQL PostgreSQL_New :PostgreSQL（新版） PostgreSQL :PostgreSQL sqlserver :SQL Server oracle :Oracle db_proxy :数据库代理 DM :达梦数据库 CurrentDB :当前数据库 UserDefineDbDriver :自定义数据库类型 |
| 43 | ficid | ficid | varchar | 100 |  | √ | ' ' |  |
| 44 | fserver_port | 服务器端口 | varchar | 100 |  | √ | ' ' | 服务器端口 |
| 45 | fattr_e1_enp | fattr_e1_enp | text | 0 |  |  | null |  |
| 46 | fdb_route | fdb_route | varchar | 30 |  | √ | ' ' |  |
| 47 | fhttp_protocal | fhttp_protocal | varchar | 30 |  | √ | ' ' |  |
| 48 | ftenant | ftenant | varchar | 100 |  | √ | ' ' |  |
| 49 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 50 | fcharset | fcharset | varchar | 100 |  | √ | ' ' |  |
| 51 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 52 | fuser | 登录用户 | varchar | 100 |  | √ | ' ' | 登录用户 |
| 53 | fhas_assign_perm | fhas_assign_perm | bpchar | 1 |  | √ | '0' |  |
| 54 | fdeploy_state | fdeploy_state | bpchar | 1 |  | √ | ' ' |  |
| 55 | fstate | 连接状态 | varchar | 30 |  | √ | ' ' | 连接状态,枚举: F :异常 S :活跃 |
| 56 | fsource_system | fsource_system | int8 | 64 |  | √ | 0 |  |
| 57 | fierp_proxy_user | fierp_proxy_user | int8 | 64 |  | √ | 0 |  |
| 58 | fnewpwd_enp | fnewpwd_enp | text | 0 |  |  | null |  |
| 59 | fmax_tps | fmax_tps | int8 | 64 |  | √ | 0 |  |
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
