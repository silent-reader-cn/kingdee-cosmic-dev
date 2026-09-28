# 服务注册查询-isc_system_query

## 服务注册查询-多语言表 t_isc_service_l

- **表名称：** 服务注册查询-多语言表
- **表名：** t_isc_service_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 20 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_service_l_pkey |  | fpkid |
| 2 | idx_isc_service_l_fid |  | fid,flocaleid |

---

## 服务注册查询-主表 t_isc_service

- **表名称：** 服务注册查询-主表
- **表名：** t_isc_service

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | fisleaf | int8 | 64 |  | √ | 0 |  |
| 3 | fsendtype | fsendtype | varchar | 30 |  | √ | ' ' |  |
| 4 | fmethod | 接口地址 | varchar | 255 |  | √ | ' ' | 接口地址 |
| 5 | fdeletedstatus | fdeletedstatus | int8 | 64 |  | √ | 0 |  |
| 6 | fpassword | fpassword | varchar | 200 |  | √ | ' ' |  |
| 7 | fmodifytime | fmodifytime | timestamp | 0 |  |  | null |  |
| 8 | fislogin | 登陆服务 | int8 | 64 |  | √ | 0 | 登陆服务 |
| 9 | fstatus | fstatus | varchar | 50 |  | √ | ' ' |  |
| 10 | fusername | fusername | varchar | 80 |  | √ | ' ' |  |
| 11 | fcreatorid | fcreatorid | int8 | 64 |  | √ | 0 |  |
| 12 | fmasterid | fmasterid | int8 | 64 |  | √ | 0 |  |
| 13 | fpreset | fpreset | int8 | 64 |  | √ | 0 |  |
| 14 | fpushservice | fpushservice | int8 | 64 |  | √ | 0 |  |
| 15 | freferedstatus | freferedstatus | int8 | 64 |  | √ | 0 |  |
| 16 | fmodifierid | fmodifierid | int8 | 64 |  | √ | 0 |  |
| 17 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 18 | fcreatetime | fcreatetime | timestamp | 0 |  |  | null |  |
| 19 | flongnumber | flongnumber | varchar | 200 |  | √ | ' ' |  |
| 20 | fimplclass | fimplclass | varchar | 255 |  | √ | ' ' |  |
| 21 | fsystementryid | fsystementryid | int8 | 64 |  | √ | 0 |  |
| 22 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 23 | ftype | 服务协议 | int8 | 64 |  | √ | 0 | 服务协议,枚举: 1 :HTTP 2 :RabbitMQ |
| 24 | fenable | fenable | int8 | 64 |  | √ | 0 |  |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 26 | fsystemid | 连接系统 | int8 | 64 |  | √ | 0 | [外部集成信息（废弃） isc_sysconn](../iscb_files/isc_sysconn.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_service_fnum |  | fnumber |
| 2 | t_isc_service_pkey |  | fid |
