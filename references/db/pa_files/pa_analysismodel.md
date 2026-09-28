# 分析模型-pa_analysismodel

## 分析模型-主表 t_pa_analysismodel

- **表名称：** 分析模型-主表
- **表名：** t_pa_analysismodel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 6 | fanalysis_system | 分析体系 | int8 | 64 |  | √ | 0 | 分析体系 pa_anasystemsetting |
| 7 | ftablenumber | 数据表编码 | varchar | 50 |  | √ | ' ' | 数据表编码 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 10 | fperiodtypeid | 期间类型 | int8 | 64 |  | √ | 0 | 会计日历类型 bd_period_type |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 14 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 15 | ftablename | 数据表名称 | varchar | 50 |  | √ | ' ' | 数据表名称 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_number_system |  | fnumber,fanalysis_system |
| 2 | idx_pa_analysismodel |  | fstatus,fenable |
| 3 | pk_t_pa_analysismodel |  | fid |

---

## 度量分录-子表 t_pa_measureentry

- **表名称：** 度量分录-子表
- **表名：** t_pa_measureentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 3 | fmeasure_fieldnumber | 度量字段编码 | varchar | 255 |  | √ | ' ' | 度量字段编码 |
| 4 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 5 | fmeasure_id | 度量 | int8 | 64 |  | √ | 0 | 度量 pa_measure |
| 6 | fmeasure_fieldname | 字段选择 | varchar | 255 |  | √ | ' ' | 字段选择 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_measure_entry |  | fid |
| 2 | pk_t_pa_measureentry |  | fentryid |

---

## 维度分录-子表 t_pa_dimensionentry

- **表名称：** 维度分录-子表
- **表名：** t_pa_dimensionentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | ffield_number | 字段编码 | varchar | 255 |  | √ | ' ' | 字段编码 |
| 3 | ffield_number_tag | 字段编码_详情 | text | 0 |  |  | null | 字段编码_详情 |
| 4 | ffield_name | 字段 | varchar | 255 |  | √ | ' ' | 字段 |
| 5 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 7 | fdimension_id | 维度 | int8 | 64 |  | √ | 0 | 维度 pa_dimension |
| 8 | fnecessity_dim | 模型必要维度 | bpchar | 1 |  | √ | ' ' | 模型必要维度,枚举: 0 :组织 1 :会计期间 2 :会计科目 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_dimensionentry |  | fentryid |
| 2 | idx_pa_dimension_entry |  | fid |

---

## 分析模型-多语言表 t_pa_analysismodel_l

- **表名称：** 分析模型-多语言表
- **表名：** t_pa_analysismodel_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_analysismodel_l |  | fpkid |
| 2 | idx_pa_analysismodel_l |  | fid,flocaleid |
