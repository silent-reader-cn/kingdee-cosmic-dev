# 多系统对接执行方案-pbd_dataexecutescheme

## 执行服务定义-子表 t_pbd_executeentry

- **表名称：** 执行服务定义-子表
- **表名：** t_pbd_executeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fexecuteserviceconfig | 服务配置 | text | 0 |  |  | null | 服务配置 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |
| 5 | fservicedesc | 执行服务描述 | varchar | 255 |  | √ | ' ' | 执行服务描述 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_executeentry_fid |  | fid |
| 2 | pk_pbd_executeentry |  | fentryid |

---

## 多系统对接执行方案-主表 t_pbd_executescheme

- **表名称：** 多系统对接执行方案-主表
- **表名：** t_pbd_executescheme

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 名称 | varchar | 512 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | fexecutechannelid | 执行渠道 | varchar | 36 |  | √ | ' ' | [集成渠道 pbd_scdatachannel](../pbd_files/pbd_scdatachannel.md) |
| 5 | ffailstrategy | 失败处理策略 | varchar | 50 |  | √ | ' ' | 失败处理策略,枚举: retry :重试三次挂起 ignore :直接挂起 |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 7 | fisnewrequired | 开启新事务 | bpchar | 1 |  | √ | '0' | 开启新事务 |
| 8 | fisv | 方案开发商 | varchar | 80 |  | √ | ' ' | 方案开发商 |
| 9 | fexecuteinterface | 业务处理接口 | varchar | 255 |  | √ | ' ' | 业务处理接口,枚举: beforeexecuteoperationtransaction :执行数据处理前事务外服务（beforeexecuteoperationtransaction） beginOperationTransaction :执行数据处理前事务内服务（beginOperationTransaction） endOperationTransaction :执行数据处理后事务内服务（endOperationTransaction） afterexecuteoperationtransaction :执行数据处理后事务外服务（afterexecuteoperationtransaction） |
| 10 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 11 | fexecutesceneid | 执行场景 | varchar | 36 |  | √ | ' ' | [处理场景定义 pbd_scenedefine](../pbd_files/pbd_scenedefine.md) |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 13 | fpreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 14 | fexecuteserviceid | 执行服务 | varchar | 36 |  | √ | ' ' | [请求服务定义 pbd_servicedefine](../pbd_files/pbd_servicedefine.md) |
| 15 | fissync | 是否同步 | bpchar | 1 |  | √ | '1' | 是否同步 |
| 16 | fenable | 使用状态 | bpchar | 1 |  | √ | '0' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 17 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 18 | fjointsystemtype | fjointsystemtype | varchar | 50 |  | √ | ' ' |  |
| 19 | fentityid | 业务处理对象 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 20 | foperatekey | 业务处理绑定操作 | varchar | 255 |  | √ | ' ' | 业务处理绑定操作,枚举: |
| 21 | fexecutetype | 触发方式 | varchar | 120 |  | √ | ' ' | 触发方式,枚举: operateevent :操作调用 manual :手工调用 |
| 22 | fislog | 记录日志 | bpchar | 1 |  | √ | '0' | 记录日志 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_executescheme_fnumber |  | fnumber |
| 2 | pk_pbd_executescheme |  | fid |

---

## 多系统对接执行方案-分表 t_pbd_executescheme_e

- **表名称：** 多系统对接执行方案-分表
- **表名：** t_pbd_executescheme_e

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fexecutetime | 最新执行时间 | timestamp | 0 |  |  | null | 最新执行时间 |
| 3 | fexecutestamp | 最新时间戳 | int8 | 64 |  | √ | 0 | 最新时间戳 |
| 4 | fexecutecount | 执行次数 | int8 | 64 |  | √ | 0 | 执行次数 |
| 5 | fexecuteuser | 最新执行用户名 | varchar | 255 |  | √ | ' ' | 最新执行用户名 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_executescheme_e_ftamp |  | fexecutestamp |
| 2 | pk_pbd_executescheme_e |  | fid |

---

## 多系统对接执行方案-多语言表 t_pbd_executescheme_l

- **表名称：** 多系统对接执行方案-多语言表
- **表名：** t_pbd_executescheme_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 40 |  | √ | ' ' |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pbd_executescheme_l |  | fid,flocaleid |
| 2 | pk_pbd_executescheme_l |  | fpkid |
