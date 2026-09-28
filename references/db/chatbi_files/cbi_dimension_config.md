# 维度配置-cbi_dimension_config

## 展平维度-子表 t_cbi_flat_dimensions

- **表名称：** 展平维度-子表
- **表名：** t_cbi_flat_dimensions

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensiontype | 维度类型 | varchar | 20 |  | √ | ' ' | 维度类型,枚举: DATE :日期维度 NORMAL :普通维度 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fdimensionkey | 维度标识 | varchar | 255 |  | √ | ' ' | 维度标识 |
| 5 | fflatdimensionname | 维度名称 | varchar | 255 |  | √ | ' ' | 维度名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_flat_dimensions |  | fentryid |
| 2 | idx_cbi_flat_dimensions_fk |  | fid |

---

## 维度配置-主表 t_cbi_dimension_config

- **表名称：** 维度配置-主表
- **表名：** t_cbi_dimension_config

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatamodelid | 数据模型 | int8 | 64 |  | √ | 0 | [指标模型 cbi_agent_datamodel](../chatbi_files/cbi_agent_datamodel.md) |
| 3 | fanalysisdimension | 构成分析维度 | varchar | 255 |  | √ | ' ' | 构成分析维度 |
| 4 | fanalysisdimension_tag | 构成分析维度_详情 | text | 0 |  |  | null | 构成分析维度_详情 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_dimension_config_fk |  | fdatamodelid |
| 2 | pk_cbi_dimension_config |  | fid |

---

## 维度层级配置-子表 t_cbi_dimension_conf_tree

- **表名称：** 维度层级配置-子表
- **表名：** t_cbi_dimension_conf_tree

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensiontreename | 维度名称 | varchar | 255 |  | √ | ' ' | 维度名称 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fparententryid | fparententryid | int8 | 64 |  | √ | 0 | pid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_dimension_conf_tree_fk |  | fid |
| 2 | pk_cbi_dimension_conf_tree |  | fentryid |

---

## 关联维度单据体-子表 t_cbi_dimension_associate

- **表名称：** 关联维度单据体-子表
- **表名：** t_cbi_dimension_associate

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassociationdimension | 关联维度 | varchar | 2000 |  | √ | ' ' | 关联维度 |
| 3 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_dimension_associate |  | fentryid |
| 2 | idx_cbi_dimension_associate_fk |  | fid |

---

## 维度清单-子表 t_cbi_dimension_bill

- **表名称：** 维度清单-子表
- **表名：** t_cbi_dimension_bill

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fjoindataset | 关联的数据源 | int8 | 64 |  | √ | 0 | [数据源 cbi_datasource](../chatbi_files/cbi_datasource.md) |
| 3 | fdimensionname | 维度名称 | varchar | 255 |  | √ | ' ' | 维度名称 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdimensionkey | 维度标识 | varchar | 255 |  | √ | ' ' | 维度标识 |
| 6 | fdimensionclass | 维度类型 | varchar | 20 |  | √ | ' ' | 维度类型,枚举: DATE :日期维度 NORMAL :普通维度 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_dimension_bill_fk |  | fid |
| 2 | pk_cbi_dimension_bill |  | fentryid |
