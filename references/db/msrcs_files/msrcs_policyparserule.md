# 政策解析规则-msrcs_policyparserule

## 政策解析规则-多语言表 t_msrcs_policyparse_l

- **表名称：** 政策解析规则-多语言表
- **表名：** t_msrcs_policyparse_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | 'zh_CN' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_policyparse_l |  | fpkid |
| 2 | idx_msrcs_policyparsel_flid |  | fid,flocaleid |

---

## 查询条件匹配规则-子表 t_msrcs_policyparsere

- **表名称：** 查询条件匹配规则-子表
- **表名：** t_msrcs_policyparsere

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fmodelcolname | 计算模型字段名称 | varchar | 50 |  | √ | ' ' | 计算模型字段名称 |
| 3 | fmatchplugin | 自定义匹配插件 | varchar | 255 |  | √ | ' ' | 自定义匹配插件 |
| 4 | fconditiontype | 条件类型 | bpchar | 1 |  | √ | 'A' | 条件类型,枚举: A :全局条件 B :分组条件（政策） C :分组条件（条件组） |
| 5 | fpolicycolname | 政策字段名称 | varchar | 50 |  | √ | ' ' | 政策字段名称 |
| 6 | fmodelcol | 计算模型字段标识 | varchar | 50 |  | √ | ' ' | 计算模型字段标识 |
| 7 | fmatchmode | 匹配方式 | varchar | 10 |  | √ | 'eq' | 匹配方式,枚举: = :等于 > :大于 >= :大于等于 < :小于 <= :小于等于 in :在…中 cus :自定义 |
| 8 | fpolicycol | 政策字段标识 | varchar | 50 |  | √ | ' ' | 政策字段标识 |
| 9 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_policyparsere |  | fentryid |
| 2 | idx_msrcs_policyparsere_id |  | fid |

---

## 计算变量映射规则-子表 t_msrcs_policyparserc

- **表名称：** 计算变量映射规则-子表
- **表名：** t_msrcs_policyparserc

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsourcecol | 来源字段标识 | varchar | 50 |  | √ | ' ' | 来源字段标识 |
| 3 | fsourcecolid | 来源字段取值ID | varchar | 50 |  | √ | ' ' | 来源字段取值ID |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fsourceentity | 变量取值来源 | varchar | 80 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 6 | fsourcecolname | 来源字段名称 | varchar | 50 |  | √ | ' ' | 来源字段名称 |
| 7 | fvarcol | 变量字段 | varchar | 50 |  | √ | ' ' | 变量字段,枚举: |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fsourcecolvalue | 来源字段取值 | varchar | 50 |  | √ | ' ' | 来源字段取值 |
| 10 | fsourceentrykey | 来源字段分录标识 | varchar | 50 |  | √ | ' ' | 来源字段分录标识 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_msrcs_policyparserc_id |  | fid |
| 2 | pk_msrcs_policyparserc |  | fentryid |

---

## 政策解析规则-主表 t_msrcs_policyparse

- **表名称：** 政策解析规则-主表
- **表名：** t_msrcs_policyparse

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | frebatefieldname | 返利对象 | varchar | 50 |  | √ | ' ' | 返利对象 |
| 3 | fname | 名称 | varchar | 255 |  | √ | ' ' | 名称 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | ffilterscheme | 自定义过滤条件 | varchar | 2000 |  | √ | ' ' | 自定义过滤条件 |
| 7 | frebatefield | 返利对象标识 | varchar | 50 |  | √ | ' ' | 返利对象标识 |
| 8 | fispreset | 系统预设 | bpchar | 1 |  | √ | '0' | 系统预设 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fconditiongroupentity | 条件组对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |
| 14 | frebateschemaid | 返利计算方案 | int8 | 64 |  | √ | 0 | [返利计算方案 msrcs_rebateschema](../msrcs_files/msrcs_rebateschema.md) |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 80 |  | √ | ' ' | 编码 |
| 17 | fpolicyentity | 政策对象 | varchar | 50 |  | √ | ' ' | [主实体对象 bos_entityobject](../mdl_files/bos_entityobject.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_msrcs_policyparse |  | fid |
| 2 | idx_msrcs_policyparse_num |  | fnumber |
