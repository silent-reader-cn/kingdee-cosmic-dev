# 聚合日期数据源配置-cbi_aggregation_date_conf

## 聚合日期数据源配置-主表 t_cbi_aggr_date_config

- **表名称：** 聚合日期数据源配置-主表
- **表名：** t_cbi_aggr_date_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatamodelid | 数据模型 | int8 | 64 |  | √ | 0 | [指标模型 cbi_agent_datamodel](../chatbi_files/cbi_agent_datamodel.md) |
| 3 | faggregationdatetype | 聚合日期粒度 | varchar | 20 |  | √ | ' ' | 聚合日期粒度,枚举: DAY :日 MONTH :月 YEAR :年 |
| 4 | faggdateformat | 聚合日期显示格式 | varchar | 25 |  | √ | 'yyyy' | 聚合日期显示格式,枚举: yyyy/MM/dd :yyyy/MM/dd yyyy/MM :yyyy/MM yyyy :yyyy yyyy/MM/dd HH:mm:ss :yyyy/MM/dd HH:mm:ss yyyy-MM-dd :yyyy-MM-dd yyyy-MM :yyyy-MM yyyy-MM-dd HH:mm:ss :yyyy-MM-dd HH:mm:ss yyyyMMdd :yyyyMMdd yyyyMM :yyyyMM yyyyMMdd HH:mm:ss :yyyyMMdd HH:mm:ss |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_aggr_date_config_fk |  | fdatamodelid |
| 2 | pk_cbi_aggr_date_config |  | fid |

---

## 数据源日期聚合方式-子表 t_cbi_datasource_config

- **表名称：** 数据源日期聚合方式-子表
- **表名：** t_cbi_datasource_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdateformat | 日期格式 | varchar | 50 |  | √ | ' ' | 日期格式 |
| 3 | fdatefieldkey | 聚合日期映射字段数据库key | varchar | 255 |  | √ | ' ' | 聚合日期映射字段数据库key |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdatasourceid | 数据源名称 | int8 | 64 |  | √ | 0 | [数据源 cbi_datasource](../chatbi_files/cbi_datasource.md) |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fdatefield | 聚合日期映射字段 | varchar | 255 |  | √ | ' ' | 聚合日期映射字段,枚举: |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_datasource_config_fk |  | fid |
| 2 | pk_cbi_datasource_config |  | fentryid |
