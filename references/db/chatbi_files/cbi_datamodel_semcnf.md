# 指标语义配置-cbi_datamodel_semcnf

## 子单据体-子表 t_cbi_join_message_cnf

- **表名称：** 子单据体-子表
- **表名：** t_cbi_join_message_cnf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fpriority | 优先级 | int4 | 32 |  | √ | 1 | 优先级 |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fdetailid | fdetailid | int8 | 64 |  | √ | 0 | id |
| 4 | fdatasourceid | 数据源id | int8 | 64 |  | √ | 0 | 数据源id |
| 5 | fmetricfieldcode | 指标字段code | varchar | 255 |  | √ | ' ' | 指标字段code |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fdetailid | fdetailid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_join_message_cnf |  | fdetailid |
| 2 | idx_cbi_join_message_cnf_fk |  | fentryid |

---

## 指标语义-子表 t_cbi_datamodel_cnfd

- **表名称：** 指标语义-子表
- **表名：** t_cbi_datamodel_cnfd

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | findex_type | 类型 | varchar | 255 |  | √ | ' ' | 类型,枚举: METRIC :指标 |
| 3 | factivateriskwarn | 指标预警 | bpchar | 1 |  | √ | '0' | 指标预警,枚举: 1 :开启 0 :关闭 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fcomparetarget | 对比指标 | varchar | 255 |  | √ | ' ' | 对比指标,枚举: |
| 6 | fmeasuretype | 指标类型 | varchar | 50 |  | √ | 'original' | 指标类型,枚举: original :原子指标 calculate :计算指标 |
| 7 | ftextfield | 字段名称 | varchar | 255 |  | √ | ' ' | 字段名称 |
| 8 | fdefinition | 指标口径说明 | varchar | 255 |  | √ | ' ' | 指标口径说明 |
| 9 | findicator_computer | 指标计算关系 | varchar | 2000 |  | √ | ' ' | 指标计算关系 |
| 10 | findextype | 指标数据类型 | varchar | 15 |  | √ | 'NUM' | 指标数据类型,枚举: NUM :数值 TEXT :文本 |
| 11 | fdisplayformatstr | 显示格式字符串 | varchar | 50 |  | √ | ' ' | 显示格式字符串 |
| 12 | findicator_type | 指标类型(计算使用,已废弃) | varchar | 255 |  | √ | ' ' | 指标类型(计算使用,已废弃),枚举: NUM :数值 RATE :比率 |
| 13 | fwarningmethod | 预警方式 | varchar | 50 |  | √ | ' ' | 预警方式,枚举: FIXED :固定阈值 COMPARE :指标对比 |
| 14 | findicatorid | 指标id | int8 | 64 |  | √ | 0 | 指标id |
| 15 | ffieldname | ffieldname | varchar | 255 |  | √ | ' ' |  |
| 16 | faggregationmethod | 默认聚合方式 | varchar | 50 |  | √ | ' ' | 默认聚合方式,枚举: sum :求和 maxdate :最大日期记录 nosup :不聚合 |
| 17 | freach_name | 目标值 | varchar | 255 |  | √ | ' ' | 目标值 |
| 18 | findicator_name | 指标名称 | varchar | 255 |  | √ | ' ' | 指标名称 |
| 19 | fjoindimension | 关联维度 | varchar | 255 |  | √ | ' ' | 关联维度 |
| 20 | flowriskvalue | 低风险 | varchar | 255 |  | √ | ' ' | 低风险 |
| 21 | fhighriskvalue | 高风险 | varchar | 255 |  | √ | ' ' | 高风险 |
| 22 | findicator_join_ds | 数据源 | int8 | 64 |  | √ | 0 | [数据源 cbi_datasource](../chatbi_files/cbi_datasource.md) |
| 23 | fcalculateexpression | 计算表达式 | varchar | 200 |  | √ | ' ' | 计算表达式 |
| 24 | fevaluation_method | 指标评价方式 | varchar | 255 |  | √ | ' ' | 指标评价方式,枚举: 1 :越高越好 2 :越低越好 |
| 25 | freach_rule | 目标达成方式 | varchar | 255 |  | √ | ' ' | 目标达成方式,枚举: 0 :不涉及 1 :指标对比 2 :固定阈值 |
| 26 | fdisplayformat | 显示格式 | varchar | 255 |  | √ | ' ' | 显示格式 |
| 27 | fdatasource | fdatasource | varchar | 255 |  | √ | ' ' |  |
| 28 | findicatorkey | 指标标识 | varchar | 255 |  | √ | ' ' | 指标标识 |
| 29 | fmidriskvalue | 中风险 | varchar | 255 |  | √ | ' ' | 中风险 |
| 30 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_cbi_datamodel_cnfd_fk |  | fid |
| 2 | pk_cbi_datamodel_cnfd |  | fentryid |

---

## 指标语义配置-主表 t_cbi_datamodel_semcnf

- **表名称：** 指标语义配置-主表
- **表名：** t_cbi_datamodel_semcnf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fdatamodelid | 数据模型 | int8 | 64 |  | √ | 0 | [指标模型 cbi_agent_datamodel](../chatbi_files/cbi_agent_datamodel.md) |
| 3 | fdatamodel | fdatamodel | int8 | 64 |  | √ | 0 |  |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_datamodel_semcnf |  | fid |
| 2 | idx_cbi_datamodel_semcnf_fk |  | fdatamodelid |
