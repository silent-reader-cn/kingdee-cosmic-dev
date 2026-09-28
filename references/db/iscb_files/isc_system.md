# 服务注册（废弃）-isc_system

## 生产者队列信息-子表 t_isc_service_mq

- **表名称：** 生产者队列信息-子表
- **表名：** t_isc_service_mq

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fautocallback | 自动订阅 | bpchar | 1 |  | √ | '0' | 自动订阅 |
| 3 | fqueuename | 队列名 | varchar | 100 |  | √ | ' ' | 队列名 |
| 4 | fcallbackclass | 自动订阅处理类 | varchar | 300 |  | √ | ' ' | 自动订阅处理类 |
| 5 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 6 | fregion | 分类 | varchar | 100 |  | √ | ' ' | 分类 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_service_mq_pkey |  | fentryid |
| 2 | idx_isc_servicemq_fid |  | fid |

---

## 服务注册（废弃）-多语言表 t_isc_service_l

- **表名称：** 服务注册（废弃）-多语言表
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

## 单据体-子表 t_isc_serviceentry

- **表名称：** 单据体-子表
- **表名：** t_isc_serviceentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdefault | 默认值 | varchar | 255 |  | √ | ' ' | 默认值 |
| 3 | fparam | 参数名 | varchar | 50 |  | √ | ' ' | 参数名 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fregion | 参数区域 | int8 | 64 |  | √ | 0 | 参数区域,枚举: 1 :请求头 2 :请求体 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fsystementryid | fsystementryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_serviceentry_pkey |  | fentryid |
| 2 | idx_isc_serentry_fid |  | fid |

---

## 单据体-多语言表 t_isc_serviceentry_l

- **表名称：** 单据体-多语言表
- **表名：** t_isc_serviceentry_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fparamalias | 参数别名 | varchar | 100 |  | √ | ' ' | 参数别名 |
| 2 | find | find | int8 | 64 |  | √ | 0 |  |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_isc_serviceentry_l_pkey |  | fpkid |
| 2 | idx_isc_servie_l_fentid |  | fentryid,flocaleid |

---

## 服务注册（废弃）-主表 t_isc_service

- **表名称：** 服务注册（废弃）-主表
- **表名：** t_isc_service

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fisleaf | fisleaf | int8 | 64 |  | √ | 0 |  |
| 3 | fsendtype | 推送方式 | varchar | 30 |  | √ | ' ' | 推送方式,枚举: direct :单发消息 fanout :广播消息 |
| 4 | fmethod | 接口地址 | varchar | 255 |  | √ | ' ' | 接口地址 |
| 5 | fdeletedstatus | fdeletedstatus | int8 | 64 |  | √ | 0 |  |
| 6 | fpassword | 密码 | varchar | 200 |  | √ | ' ' | 密码 |
| 7 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 8 | fislogin | 登陆服务 | int8 | 64 |  | √ | 0 | 登陆服务 |
| 9 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fusername | 用户名 | varchar | 80 |  | √ | ' ' | 用户名 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fpreset | 预置 | int8 | 64 |  | √ | 0 | 预置 |
| 14 | fpushservice | 消息服务 | int8 | 64 |  | √ | 0 | MQ消息服务Old isc_mq |
| 15 | freferedstatus | freferedstatus | int8 | 64 |  | √ | 0 |  |
| 16 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 17 | fparentid | fparentid | int8 | 64 |  | √ | 0 |  |
| 18 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 19 | flongnumber | flongnumber | varchar | 200 |  | √ | ' ' |  |
| 20 | fimplclass | 服务实现类 | varchar | 255 |  | √ | ' ' | 服务实现类 |
| 21 | fsystementryid | 服务器 | int8 | 64 |  | √ | 0 | 对接系统查询 isc_othersys_query |
| 22 | flevel | flevel | int8 | 64 |  | √ | 0 |  |
| 23 | ftype | 服务协议 | int8 | 64 |  | √ | 0 | 服务协议,枚举: 1 :HTTP 2 :RabbitMQ 3 :WebService |
| 24 | fenable | 使用状态 | int8 | 64 |  | √ | 0 | 使用状态,枚举: 0 :禁用 1 :可用 |
| 25 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 26 | fsystemid | 连接系统 | int8 | 64 |  | √ | 0 | 外部集成信息（废弃） isc_sysconn |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_isc_service_fnum |  | fnumber |
| 2 | t_isc_service_pkey |  | fid |
