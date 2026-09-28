# 维度值映射配置-cbi_dsvalue_mapping

## 维度值映射配置-主表 t_cbi_dsvalue_mapping

- **表名称：** 维度值映射配置-主表
- **表名：** t_cbi_dsvalue_mapping

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatasourceid | 数据源 | int8 | 64 |  | √ | 0 | [数据源 cbi_datasource](../chatbi_files/cbi_datasource.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_dsvalue_mapping |  | fid |
| 2 | idx_cbi_dsvalue_mp_dsid |  | fdatasourceid |

---

## 指标展示配置-子表 t_cbi_dsvalue_mapping_cf

- **表名称：** 指标展示配置-子表
- **表名：** t_cbi_dsvalue_mapping_cf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | foriginalvalue | 原始表的维度值 | varchar | 255 |  | √ | ' ' | 原始表的维度值,枚举: |
| 3 | fdimensionfieldcode | 维度类型 | varchar | 255 |  | √ | ' ' | 维度类型,枚举: |
| 4 | fmappingvalue | 映射的维度值 | varchar | 255 |  | √ | ' ' | 映射的维度值 |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fcreatetime | 创建时间 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建时间 |
| 7 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 8 | fdimensioncode | 字段编码 | varchar | 255 |  | √ | ' ' | 字段编码 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_dsvalue_mp_cf_fid |  | fid |
| 2 | pk_cbi_dsvalue_mapping_cf |  | fentryid |
