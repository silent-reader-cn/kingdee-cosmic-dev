# 批量申报项目规则配置-bdtaxr_batch_rule_set

## 批量申报项目规则配置-主表 t_bdtaxr_batch_rule

- **表名称：** 批量申报项目规则配置-主表
- **表名：** t_bdtaxr_batch_rule

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 2 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 3 | fconditionjson | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 4 | forg | 组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 11 | fisbatch | 是否批量 | bpchar | 1 |  | √ | ' ' | 是否批量 |
| 12 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 13 | ffiltercondition | 过滤条件 | varchar | 2000 |  | √ | ' ' | 过滤条件 |
| 14 | fcountry | 国家/地区 | int8 | 64 |  | √ | 0 | [国家和地区 bd_country](../base_files/bd_country.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_batch_rule |  | fentryid |
| 2 | idx_bdtaxr_batch_rule |  | fnumber |

---

## 分组字段-多选基础资料表 t_bdtaxr_batch_rule_group

- **表名称：** 分组字段-多选基础资料表
- **表名：** t_bdtaxr_batch_rule_group

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [数据源字段配置 bdtaxr_datasource_entry](../bdtaxr_files/bdtaxr_datasource_entry.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_batch_rule_group_fk |  | fentryid |
| 2 | pk_bdtaxr_batch_rule_group |  | fpkid |

---

## 批量申报项目规则配置-多语言表 t_bdtaxr_batch_rule_l

- **表名称：** 批量申报项目规则配置-多语言表
- **表名：** t_bdtaxr_batch_rule_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fname | 业务名称 | varchar | 500 |  | √ | ' ' | 业务名称 |
| 2 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 3 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bdtaxr_batch_rule_l_0 |  | fentryid,flocaleid |
| 2 | pk_bdtaxr_batch_rule_l |  | fpkid |

---

## 单据体-子表 t_bdtaxr_batch_rule_entry

- **表名称：** 单据体-子表
- **表名：** t_bdtaxr_batch_rule_entry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdistinctfield | 目标字段 | int8 | 64 |  | √ | 0 | [数据源字段配置 bdtaxr_datasource_entry](../bdtaxr_files/bdtaxr_datasource_entry.md) |
| 3 | ffunc | 函数 | varchar | 50 |  | √ | ' ' | 函数,枚举: sum :求和 count :计数 distinct :去重 abs :绝对值 max :最大值 min :最小值 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_bdtaxr_batch_rule_entry |  | fid |
| 2 | idx_bdtaxr_batch_rule_entry_fk |  | fentryid |

---

## 数据源-多选基础资料表 t_bataxr_mult_table

- **表名称：** 数据源-多选基础资料表
- **表名：** t_bataxr_mult_table

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | [数据源配置 bdtaxr_custom_datasource](../bdtaxr_files/bdtaxr_custom_datasource.md) |
| 2 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |
| 3 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_bataxr_mult_table_fk |  | fentryid |
| 2 | pk_bataxr_mult_table |  | fpkid |
