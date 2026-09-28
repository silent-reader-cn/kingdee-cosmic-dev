# 外部系统配置-isc_cn_config

## 外部系统配置-多语言表 t_isc_cn_config_l

- **表名称：** 外部系统配置-多语言表
- **表名：** t_isc_cn_config_l

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
| 1 | idx_cn_config_l_1 |  | fid |
| 2 | pk_t_isc_cn_config_l |  | fpkid |

---

## 外部系统配置-主表 t_isc_cn_config

- **表名称：** 外部系统配置-主表
- **表名：** t_isc_cn_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | feas_service | EAS服务 | varchar | 100 |  | √ | ' ' | EAS服务 |
| 3 | fappsecret_new_enp | fappsecret_new_enp | text | 0 |  |  | null |  |
| 4 | fserver_ip | 服务器IP或域名 | varchar | 250 |  | √ | ' ' | 服务器IP或域名 |
| 5 | fappsecret_new | 开放应用密码 | varchar | 100 |  | √ | ' ' | 开放应用密码 |
| 6 | fattr_8 | 自定义属性_8 | varchar | 2000 |  | √ | ' ' | 自定义属性_8 |
| 7 | fattr_9 | 自定义属性_9 | varchar | 2000 |  | √ | ' ' | 自定义属性_9 |
| 8 | faccount | 账套ID | varchar | 100 |  | √ | ' ' | 账套ID |
| 9 | fsql_database | 数据库名 | varchar | 100 |  | √ | ' ' | 数据库名 |
| 10 | fdata_center | 数据中心 | varchar | 100 |  | √ | ' ' | 数据中心 |
| 11 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 12 | fappid | 开放应用编码 | varchar | 100 |  | √ | ' ' | 开放应用编码 |
| 13 | ftextfield10 | 字符集 | varchar | 50 |  | √ | ' ' | 字符集 |
| 14 | fattr_2 | 自定义属性_2 | varchar | 50 |  | √ | ' ' | 自定义属性_2 |
| 15 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 16 | fattr_3 | 自定义属性_3 | varchar | 50 |  | √ | ' ' | 自定义属性_3 |
| 17 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 18 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 19 | fattr_1 | 自定义属性_1 | varchar | 50 |  | √ | ' ' | 自定义属性_1 |
| 20 | fattr_6 | 自定义属性_6 | varchar | 50 |  | √ | ' ' | 自定义属性_6 |
| 21 | fdatabase_type | 连接类型 | varchar | 36 |  | √ | ' ' | [外部系统类型 isc_connection_type_x](../iscb_files/isc_connection_type_x.md) |
| 22 | ficid | 语言 | varchar | 50 |  | √ | ' ' | 语言,枚举: zh_CN :简体中文 zh_TW :繁体中文 en_US :英文 |
| 23 | fattr_7 | 自定义属性_7 | varchar | 2000 |  | √ | ' ' | 自定义属性_7 |
| 24 | fattr_4 | 自定义属性_4 | varchar | 50 |  | √ | ' ' | 自定义属性_4 |
| 25 | fattr_5 | 自定义属性_5 | varchar | 50 |  | √ | ' ' | 自定义属性_5 |
| 26 | fserver_port | 服务器端口 | int8 | 64 |  | √ | 0 | 服务器端口 |
| 27 | fattr_e1_enp | fattr_e1_enp | text | 0 |  |  | null |  |
| 28 | fhttp_protocal | HTTP协议 | varchar | 30 |  | √ | ' ' | HTTP协议,枚举: http :http https :https |
| 29 | flicense_info | 许可状态（该属性在运行期禁止访问） | varchar | 50 |  | √ | ' ' | 许可状态（该属性在运行期禁止访问）,枚举: free :默认免费 yes :正常 no :许可不足 expired :许可失效 |
| 30 | ftenant | 租户ID | varchar | 100 |  | √ | ' ' | 租户ID |
| 31 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 32 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 33 | fuser | 登录用户 | varchar | 100 |  | √ | ' ' | 登录用户 |
| 34 | foracle_service | Oracle服务 | varchar | 100 |  | √ | ' ' | Oracle服务 |
| 35 | fattr_e1 | 自定义属性_10 | varchar | 100 |  | √ | ' ' | 自定义属性_10 |
| 36 | flicense_sn | 许可序号（该属性在运行期禁止访问） | int8 | 64 |  | √ | 0 | 许可序号（该属性在运行期禁止访问） |
| 37 | fstate | 连接状态 | varchar | 30 |  | √ | ' ' | 连接状态,枚举: F :异常 S :活跃 |
| 38 | fnewpwd | 登录密码 | varchar | 100 |  | √ | ' ' | 登录密码 |
| 39 | fsource_system | 来源系统 | int8 | 64 |  | √ | 0 | [来源系统 isc_ds_srcsys](../iscb_files/isc_ds_srcsys.md) |
| 40 | fweb_app | Web应用名 | varchar | 100 |  | √ | ' ' | Web应用名 |
| 41 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :启用 |
| 42 | fnewpwd_enp | fnewpwd_enp | text | 0 |  |  | null |  |
| 43 | fierp_proxy_user | 当前账套回调代理用户 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 44 | fnumber | 编码 | varchar | 60 |  | √ | ' ' | 编码 |
| 45 | fmax_tps | 流量控制（次/秒） | int8 | 64 |  | √ | 0 | 流量控制（次/秒） |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_cn_config |  | fid |
| 2 | idx_cn_config_1 |  | fnumber |
