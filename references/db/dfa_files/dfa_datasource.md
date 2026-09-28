# 数据源-dfa_datasource

## 本公司数据信息单据体-子表 t_dfa_cpdatainfo_entry

- **表名称：** 本公司数据信息单据体-子表
- **表名：** t_dfa_cpdatainfo_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftempnum | 业务模板编码 | varchar | 50 |  | √ | ' ' | 业务模板编码 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | ftempname | 业务模板名称 | varchar | 50 |  | √ | ' ' | 业务模板名称 |
| 5 | flatestperiod | 最新报告期 | varchar | 50 |  | √ | ' ' | 最新报告期 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_cpdatainfo_entry_fk |  | fid |
| 2 | pk_dfa_cpdatainfo_entry |  | fentryid |

---

## 数据源-主表 t_dfa_datasource

- **表名称：** 数据源-主表
- **表名：** t_dfa_datasource

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 3 | fname | 数据源名称 | varchar | 50 |  | √ | ' ' | 数据源名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdimensionupdatetime | 查询维度数据更新时间 | varchar | 50 |  | √ | ' ' | 查询维度数据更新时间 |
| 6 | fispreset | 是否预置 | bpchar | 1 |  | √ | '0' | 是否预置 |
| 7 | fdatasourcetype | 数据源类型 | varchar | 50 |  | √ | ' ' | 数据源类型,枚举: CWBB :财务报表 KMYEB :科目余额表 DBMB :对标分析业务模板 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | ffindatasyncparam | 财务报表最近同步参数 | varchar | 512 |  | √ | ' ' | 财务报表最近同步参数 |
| 10 | ffindatasyncparam_tag | 财务报表最近同步参数_详情 | text | 0 |  |  | null | 财务报表最近同步参数_详情 |
| 11 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 14 | fdatasource_env | 取数环境 | int8 | 64 |  | √ | 0 | [取数环境 dfa_datasource_env](../dfa_files/dfa_datasource_env.md) |
| 15 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fdesc | 描述 | varchar | 50 |  | √ | ' ' | 描述 |
| 17 | fnumber | 数据源编码 | varchar | 30 |  | √ | ' ' | 数据源编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_dfa_datasource_m0 |  | fmasterid |
| 2 | pk_dfa_datasource |  | fid |

---

## 默认查询参数单据体-子表 t_dfa_defaultparamentry

- **表名称：** 默认查询参数单据体-子表
- **表名：** t_dfa_defaultparamentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fqueryparamconfig | 查询参数配置真实字段 | varchar | 255 |  | √ | ' ' | 查询参数配置真实字段 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 3 | fqueryparamconfig_tag | 查询参数配置真实字段_详情 | text | 0 |  |  | null | 查询参数配置真实字段_详情 |
| 4 | fipoorg | 本公司（编制组织） | varchar | 50 |  | √ | ' ' | 本公司（编制组织） |
| 5 | fipoorg_number | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fqueryparamconfig_proxy | 查询参数配置 | varchar | 50 |  | √ | ' ' | 查询参数配置 |
| 8 | findustry | 所属行业 | int8 | 64 |  | √ | 0 | [申万行业 dfa_industry_info](../dfa_files/dfa_industry_info.md) |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_defaultparamentry |  | fentryid |
| 2 | idx_dfa_defaultparamentry_fk |  | fid |

---

## 数据源信息单据体-子表 t_dfa_dsinfo_entry

- **表名称：** 数据源信息单据体-子表
- **表名：** t_dfa_dsinfo_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fapiid | 编码 | int8 | 64 |  | √ | 0 | [API服务 openapi_apilist](../open_files/openapi_apilist.md) |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_dsinfo_entry |  | fentryid |
| 2 | idx_dfa_dsinfo_entry_fk |  | fid |

---

## 数据源-多语言表 t_dfa_datasource_l

- **表名称：** 数据源-多语言表
- **表名：** t_dfa_datasource_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 数据源名称 | varchar | 80 |  | √ | ' ' | 数据源名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_datasource_l |  | fpkid |
| 2 | idx_dfa_datasource_l_0 |  | fid,flocaleid |
