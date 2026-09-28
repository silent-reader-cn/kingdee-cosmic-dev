# 协同数据处理配置-pbd_scdatahandle

## 协同数据处理配置-主表 t_pur_scdatahandle

- **表名称：** 协同数据处理配置-主表
- **表名：** t_pur_scdatahandle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' | id |
| 2 | fname | 数据处理描述 | varchar | 255 |  | √ | ' ' | 数据处理描述 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | ffailstrategy | 失败处理策略 | varchar | 50 |  | √ | ' ' | 失败处理策略,枚举: retry :重试三次挂起 ignore :直接挂起 |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fisv | 开发商 | varchar | 255 |  | √ | ' ' | 开发商 |
| 7 | fhandleclass | 请求处理类 | varchar | 255 |  | √ | ' ' | 请求处理类 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | foperate | 执行请求操作 | varchar | 36 |  | √ | ' ' | 执行请求操作,枚举: |
| 10 | fmasterid | 主数据内码 | varchar | 36 |  | √ | ' ' | 主数据内码 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fhandleconfig | 请求配置 | text | 0 |  |  | ' ' | 请求配置 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 15 | fisexcuteservice | 执行服务 | bpchar | 1 |  | √ | '0' | 执行服务 |
| 16 | fentityid | 执行请求实体 | varchar | 36 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_sdh_fnumber |  | fnumber |
| 2 | pk_t_pur_scdatahandle |  | fid |

---

## 参数配置-子表 t_pur_refscdataconfig

- **表名称：** 参数配置-子表
- **表名：** t_pur_refscdataconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fscdataconfigtext | 请求处理参数 | text | 0 |  |  | ' ' | 请求处理参数 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fscdataconfigid | 处理参数 | varchar | 36 |  | √ | ' ' | [协同数据处理参数配置 pbd_scdataconfig](../pbd_files/pbd_scdataconfig.md) |
| 5 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_sdc_ref_fid |  | fscdataconfigid |
| 2 | pk_pur_refscdataconfig |  | fentryid |

---

## 执行服务配置-子表 t_pur_refscdatahandle

- **表名称：** 执行服务配置-子表
- **表名：** t_pur_refscdatahandle

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | varchar | 36 |  | √ | ' ' |  |
| 2 | fscserviceconfig | 服务处理参数 | text | 0 |  |  | ' ' | 服务处理参数 |
| 3 | fscdataserviceid | 执行服务 | varchar | 36 |  | √ | ' ' | [协同数据处理服务注册 pbd_scdataservice](../pbd_files/pbd_scdataservice.md) |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_pur_sdh_ref_fid |  | fscdataserviceid |
| 2 | pk_pur_refscdatahandle |  | fentryid |
