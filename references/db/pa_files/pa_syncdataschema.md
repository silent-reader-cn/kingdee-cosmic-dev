# 取数方案-pa_syncdataschema

## 维度映射单据体-子表 t_pa_dimensionmapentry

- **表名称：** 维度映射单据体-子表
- **表名：** t_pa_dimensionmapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimensionfield | 数据源维度标识 | varchar | 80 |  | √ | ' ' | 数据源维度标识 |
| 3 | fdimensionid | 目标模型维度 | int8 | 64 |  | √ | 0 | 维度 pa_dimension |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdimdefaultvalue | 默认值 | varchar | 50 |  | √ | ' ' | 默认值 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_dimensionmapentry |  | fentryid |
| 2 | idx_pa_dimensionmapentry |  | fdimensionfield |

---

## 度量映射单据体-子表 t_pa_measuremapentry

- **表名称：** 度量映射单据体-子表
- **表名：** t_pa_measuremapentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fconditiondesc | 条件取值 | varchar | 255 |  | √ | ' ' | 条件取值 |
| 3 | fcondition_tag | 条件取值json_详情 | text | 0 |  |  | null | 条件取值json_详情 |
| 4 | fselecttype | 取值类型 | bpchar | 1 |  | √ | ' ' | 取值类型,枚举: 3 :数据源度量 2 :常量 1 :条件取值 |
| 5 | fmeasuredefaultvalue | 常量 | numeric | 23 | 10 | √ | 0 | 常量 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | fcondition | 条件取值json | varchar | 100 |  | √ | ' ' | 条件取值json |
| 8 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 9 | fmeasurefield | 数据源度量 | varchar | 30 |  | √ | ' ' | 数据源度量,枚举: |
| 10 | fmeasureid | 目标模型度量 | int8 | 64 |  | √ | 0 | 度量 pa_measure |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_measuremapentry |  | fid |
| 2 | pk_t_pa_measuremapentry |  | fentryid |

---

## 取数方案-多语言表 t_pa_syncdataschema_l

- **表名称：** 取数方案-多语言表
- **表名：** t_pa_syncdataschema_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fdescription | 描述 | varchar | 255 |  | √ | ' ' | 描述 |
| 5 | fpkid | fpkid | varchar | 18 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_pa_syncdataschema_l |  | fpkid |
| 2 | idx_pa_syncdataschema_l |  | fid,flocaleid |

---

## 取数方案-主表 t_pa_syncdataschema

- **表名称：** 取数方案-主表
- **表名：** t_pa_syncdataschema

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodelid | 分析体系 | int8 | 64 |  | √ | 0 | 分析体系 pa_anasystemsetting |
| 6 | fdatasourceid | 数据源 | int8 | 64 |  | √ | 0 | 数据源 pa_datasourceconfig |
| 7 | fdescription | 描述 | varchar | 100 |  | √ | ' ' | 描述 |
| 8 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 9 | fbizappid | 适用模块范围 | varchar | 36 |  | √ | ' ' | 业务应用实体 bos_devportal_bizapp |
| 10 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 11 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 12 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 13 | fanalysismodelid | 分析模型 | int8 | 64 |  | √ | 0 | 分析模型 pa_analysismodel |
| 14 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 15 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_syncdataschema_un |  | fnumber,fmodelid |
| 2 | idx_pa_syncdataschema |  | fstatus,fenable,fanalysismodelid |
| 3 | pk_t_pa_syncdataschema |  | fid |
