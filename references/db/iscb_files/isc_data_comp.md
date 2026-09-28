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
| 3 | ffilter_compare | 比较方式 | varchar | 30 |  | √ | ' ' | 比较方式,枚举: = :等于 STARTS_WITH :开头是 CONTAINS :包含 ENDS_WITH :结尾是 > :大于 >= :大于或等于 < :小于 <= :小于或等于 <> :不等于 in :IN not in :NOT IN NOT_STARTS_WITH :开头不是 NOT_CONTAINS :不包含 NOT_ENDS_WITH :结尾不是 IS_NULL :为空 IS_NOT_NULL :不为空 |
| 4 | ffilter_right_bracket | 右括号 | bpchar | 1 |  | √ | ' ' | 右括号,枚举: ) :) )) :)) |
| 5 | ffilter_label | 条件描述 | varchar | 50 |  | √ | ' ' | 条件描述 |
| 6 | ffilter_value_var | 比较值变量 | varchar | 30 |  | √ | ' ' | 比较值变量,枚举: |
| 7 | ffilter_link | 逻辑连接符 | varchar | 30 |  | √ | ' ' | 逻辑连接符,枚举: AND :与 OR :或 |
| 8 | ffilter_value_fixed | 固定比较值 | varchar | 500 |  | √ | ' ' | 固定比较值 |
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
| 6 | fparam_value | 参数值 | varchar | 2000 |  | √ | ' ' | 参数值 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fparam_title | 标题 | varchar | 50 |  | √ | ' ' | 标题 |

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
| 2 | fgroupid | 方案分类 | int8 | 64 |  | √ | 0 | [自定义分类 isc_schema_category](../iscb_files/isc_schema_category.md) |
| 3 | fsrc_field | 来源取数字段 | varchar | 100 |  |  | ' ' | 来源取数字段 |
| 4 | fsource_tenant | 来源 | varchar | 100 |  | √ | ' ' | 来源 |
| 5 | fisv | 开发商 | varchar | 100 |  | √ | ' ' | 开发商 |
| 6 | fstrategy | 对比策略 | varchar | 30 |  | √ | ' ' | 对比策略,枚举: CheckExist :目标单是否存在 CheckUpdate :目标单是否更新 |
| 7 | fauto_compensate | 自动补偿 | bpchar | 1 |  | √ | '0' | 自动补偿 |
| 8 | fprotect_level | 保护等级 | varchar | 30 |  | √ | ' ' | 保护等级,枚举: DEFAULT :默认 READ_ONLY :只读 UNPROTECTED :无保护 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fsource_trace | 来源追溯 | varchar | 600 |  | √ | ' ' | 来源追溯 |
| 14 | fdata_copy | 数据集成方案 | int8 | 64 |  | √ | 0 | [数据集成方案 isc_data_copy](../iscb_files/isc_data_copy.md) |
| 15 | ftrigger | 补偿方案 | int8 | 64 |  | √ | 0 | [数据集成方案 isc_data_copy](../iscb_files/isc_data_copy.md) |
| 16 | fsrc_ts_field | 源单时间戳属性 | varchar | 50 |  | √ | ' ' | 源单时间戳属性 |
| 17 | fremark | 备注 | varchar | 300 |  | √ | ' ' | 备注 |
| 18 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 19 | fcallback_info | 回调信息 | varchar | 255 |  | √ | ' ' | 回调信息 |
| 20 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 21 | fjob_mutex | 后台任务组 | int8 | 64 |  | √ | 0 | [后台任务组 isc_job_mutex](../iscb_files/isc_job_mutex.md) |
| 22 | fbatch_size | 比较批量大小 | int4 | 32 |  | √ | 0 | 比较批量大小 |
| 23 | ftar_ts_field | 目标单时间戳属性 | varchar | 50 |  | √ | ' ' | 目标单时间戳属性 |
| 24 | ftar_field | 目标单取数字段 | varchar | 100 |  |  | ' ' | 目标单取数字段 |
| 25 | fdigest | 摘要模板 | varchar | 255 |  |  | ' ' | 摘要模板 |
| 26 | fdata_copy_trigger | 启动方案 | int8 | 64 |  | √ | 0 | [启动方案 isc_data_copy_trigger](../iscb_files/isc_data_copy_trigger.md) |
| 27 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 28 | fnumber | 数据对比编码 | varchar | 100 |  | √ | ' ' | 数据对比编码 |
| 29 | fts_expr | 判断表达式 | varchar | 200 |  | √ | ' ' | 判断表达式 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_isc_data_comp |  | fid |
| 2 | idx_isc_data_comp2 |  | fnumber |
