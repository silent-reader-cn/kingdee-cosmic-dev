# 筛选条件-amccsa_quickentryfilter

## 筛选条件-主表 t_amccsa_quickentryfilter

- **表名称：** 筛选条件-主表
- **表名：** t_amccsa_quickentryfilter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | ffrequency | 交货频次 | int4 | 32 |  | √ | 0 | 交货频次 |
| 2 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 3 | fschemename | 方案名称 | varchar | 50 |  | √ | ' ' | 方案名称 |
| 4 | fdefault | 是否默认 | int4 | 32 |  | √ | '-1' | 是否默认 |
| 5 | ftime3 | 交货时间 | int4 | 32 |  | √ | '-1' | 交货时间 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 8 | fcustschdorderid | 销售计划协议 | int8 | 64 |  | √ | 0 | 销售计划协议 amccsa_custschdorder |
| 9 | fqtymethod | 数量录入方式 | bpchar | 1 |  | √ | ' ' | 数量录入方式,枚举: 0 :累计值 1 :净值 |
| 10 | ftime1 | 交货时间 | int4 | 32 |  | √ | '-1' | 交货时间 |
| 11 | ftime2 | 交货时间 | int4 | 32 |  | √ | '-1' | 交货时间 |
| 12 | fiszeroschd | 生成零计划 | bpchar | 1 |  | √ | '1' | 生成零计划 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_amccsa_quickentryfilter |  | fid |
| 2 | idx_amccsa_quickentryfilter_m0 |  | ftime3 |

---

## 单据体-子表 t_amccsa_quickentrydate

- **表名称：** 单据体-子表
- **表名：** t_amccsa_quickentrydate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ftype | 类型 | varchar | 50 |  | √ | ' ' | 类型,枚举: 0 :客户预测计划 1 :客户交货计划 2 :滚动发货计划 |
| 3 | fstartdate | 计划起始日 | timestamp | 0 |  |  | null | 计划起始日 |
| 4 | fplanweek | 计划周数 | int4 | 32 |  | √ | 0 | 计划周数 |
| 5 | fforecastqualifier | 默认需求预测类型 | int8 | 64 |  | √ | 0 | [需求预测类型 amccsa_forecastqualifier](../amccsa_files/amccsa_forecastqualifier.md) |
| 6 | fplanmonth | 计划月数 | int4 | 32 |  | √ | 0 | 计划月数 |
| 7 | fenable | 启用 | bpchar | 1 |  | √ | '0' | 启用 |
| 8 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 9 | fplanday | 计划日数 | int4 | 32 |  | √ | 0 | 计划日数 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_amccsa_quickentrydate |  | fentryid |
| 2 | idx_amccsa_quickentrydate_fk |  | fid |
