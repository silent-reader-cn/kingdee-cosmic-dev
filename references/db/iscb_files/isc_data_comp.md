# 数据对比方案-isc_data_comp

## 数据对比方案-多语言表 t_isc_data_comp_l

- **表名称：** 数据对比方案-多语言表
- **表名：** t_isc_data_comp_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 数据对比名称 | varchar | 100 |  | √ | ' ' | 数据对比名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_data_comp_l |  | fpkid |
| 2 | idx_isc_data_comp_l |  | flocaleid |
| 3 | idx_isc_data_comp_l2 |  | fname |

---

## 数据范围-子表 t_isc_data_comp_filter

- **表名称：** 数据范围-子表
- **表名：** t_isc_data_comp_filter

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffilter_column | 条件字段 | varchar | 50 |  | √ | ' ' | 条件字段 |
| 3 | ffilter_compare | 比较方式 | varchar | 30 |  | √ | ' ' | 比较方式,枚举: = :等于 STARTS_WITH :开头是 CONTAINS :包含 ENDS_WITH :结尾是 > :大于 >= :大于或等于 :不等于 in :IN not in :NOT IN NOT_STARTS_WITH :开头不是 NOT_CONTAINS :不包含 NOT_ENDS_WITH :结尾不是 IS_NULL :为空 IS_NOT_NULL :不为空 |
| 4 | ffilter_right_bracket | 右括号 | bpchar | 1 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) |
| 5 | ffilter_label | 条件描述 | varchar | 50 |  | √ | ' ' | 条件描述 |
| 6 | ffilter_value_var | 比较值变量 | varchar | 30 |  | √ | ' ' | 比较值变量,枚举: |
| 7 | ffilter_link | 逻辑连接符 | varchar | 30 |  | √ | ' ' | 逻辑连接符,枚举: AND :与 OR :或 |
| 8 | ffilter_value_fixed | 固定比较值 | varchar | 50 |  | √ | ' ' | 固定比较值 |
| 9 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 10 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 11 | ffilter_left_bracket | 左括号 | bpchar | 1 |  | √ | ' ' | 左括号,枚举: ( :( (( :(( |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_data_comp_filter |  | fentryid |
| 2 | idx_isc_data_comp_filter |  | fid,fentryid |

---

## 对比参数-子表 t_isc_data_comp_params

- **表名称：** 对比参数-子表
- **表名：** t_isc_data_comp_params

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fparam_type | 参数类型 | varchar | 30 |  | √ | ' ' | 参数类型,枚举: string :字符串 integer :整数 decimal :小数 datetime :日期/时间 |
| 3 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 4 | fparam_remark | 备注 | varchar | 200 |  | √ | ' ' | 备注 |
| 5 | fparam_name | 名称 | varchar | 50 |  | √ | ' ' | 名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fparam_title | 标题 | varchar | 50 |  | √ | ' ' | 标题 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_data_comp_params |  | fentryid |
| 2 | idx_isc_data_comp_params |  | fid,fentryid |

---

## 数据对比方案-主表 t_isc_data_comp

- **表名称：** 数据对比方案-主表
- **表名：** t_isc_data_comp

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fgroupid | 方案分类 | int8 | 64 |  | √ | 0 | 自定义分类 isc_schema_category |
| 5 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 6 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 7 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 8 | fstrategy | 对比策略 | varchar | 30 |  | √ | ' ' | 对比策略,枚举: CheckExist :目标单是否存在 CheckUpdate :目标单是否更新 |
| 9 | fauto_compensate | 自动补偿 | bpchar | 1 |  | √ | '0' | 自动补偿 |
| 10 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 11 | ftar_ts_field | 目标单时间戳属性 | varchar | 50 |  | √ | ' ' | 目标单时间戳属性 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 13 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 14 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 15 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 16 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 17 | fdata_copy | 数据集成方案 | int8 | 64 |  | √ | 0 | 数据集成方案 isc_data_copy |
| 18 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 19 | ftrigger | 补偿方案 | int8 | 64 |  | √ | 0 | 数据集成方案 isc_data_copy |
| 20 | fnumber | 数据对比编码 | varchar | 100 |  | √ | ' ' | 数据对比编码 |
| 21 | fts_expr | 判断表达式 | varchar | 200 |  | √ | ' ' | 判断表达式 |
| 22 | fsrc_ts_field | 源单时间戳属性 | varchar | 50 |  | √ | ' ' | 源单时间戳属性 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_data_comp |  | fid |
| 2 | idx_isc_data_comp2 |  | fnumber |
