# 智能体数据配置-cbi_agent_dataconfig

## 智能体数据配置-主表 t_cbi_agent_dataconfig

- **表名称：** 智能体数据配置-主表
- **表名：** t_cbi_agent_dataconfig

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fsynchronizationdimension_tag | 已经同步的维度_详情 | text | 0 |  |  | null | 已经同步的维度_详情 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 4 | frecalldimension_tag | 参与值召回的维度_详情 | text | 0 |  |  | null | 参与值召回的维度_详情 |
| 5 | fcreatetime | 创建日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 创建日期 |
| 6 | fsynchronizationtime | 同步时间： | timestamp | 0 |  |  | null | 同步时间： |
| 7 | frecalldimension | 参与值召回的维度 | varchar | 255 |  |  | ' ' | 参与值召回的维度 |
| 8 | fmodifytime | 修改日期 | timestamp | 0 |  | √ | LOCALTIMESTAMP | 修改日期 |
| 9 | fdimensionstatus | 维度值更新状态 | varchar | 30 |  | √ | ' ' | 维度值更新状态,枚举: Unupdated :未更新 DimensionIncreased :增加维度 DimensionDecreased :减少维度 DimensionAdjusted :同时增减 DimensionDecreasedNone :维度减少至0 |
| 10 | fdatamodelid | 数据模型 | int8 | 64 |  | √ | 0 | [指标模型 cbi_agent_datamodel](../chatbi_files/cbi_agent_datamodel.md) |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 12 | fsynchronizationdimension | 已经同步的维度 | varchar | 255 |  |  | ' ' | 已经同步的维度 |
| 13 | fagentbaseid | 智能体 | int8 | 64 |  | √ | 0 | [智能体 cbi_agent_base](../chatbi_files/cbi_agent_base.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_agent_dataconfig |  | fid |
| 2 | idx_t_cbi_agent_dataconfig_fk |  | fagentbaseid |

---

## 维度值配置-子表 t_cbi_dimension_val_conf

- **表名称：** 维度值配置-子表
- **表名：** t_cbi_dimension_val_conf

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensionvaluename | 维度值名称 | varchar | 255 |  | √ | ' ' | 维度值名称 |
| 3 | fdimensionid | 数据模型维度id | int8 | 64 |  | √ | 0 | 数据模型维度id |
| 4 | fdimensionname | 维度名称 | varchar | 255 |  | √ | ' ' | 维度名称 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fdimensionvaluealias | 维度值口语化别名 | varchar | 255 |  |  | ' ' | 维度值口语化别名 |
| 7 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 8 | fdimensionvalupdatetime | 维度值更新时间 | timestamp | 0 |  |  | null | 维度值更新时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_cbi_dimension_val_conf |  | fentryid |
| 2 | idx_cbi_dimension_val_conf_fk |  | fid |
