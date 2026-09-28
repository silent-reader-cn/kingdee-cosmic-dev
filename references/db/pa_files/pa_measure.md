# 度量-pa_measure

## 度量-多语言表 t_pa_measure_l

- **表名称：** 度量-多语言表
- **表名：** t_pa_measure_l

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
| 1 | pk_t_pa_measure_l |  | fpkid |
| 2 | idx_pa_measure_l |  | fid,flocaleid |

---

## 度量-主表 t_pa_measure

- **表名称：** 度量-主表
- **表名：** t_pa_measure

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 3 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fdimensionid | 聚合维度 | int8 | 64 |  | √ | 0 | 维度 pa_dimension |
| 6 | fdimensionattrnb | 聚合属性设置编码 | varchar | 255 |  | √ | ' ' | 聚合属性设置编码 |
| 7 | fmeasuretype | 度量类型 | bpchar | 1 |  | √ | ' ' | 度量类型,枚举: 1 :普通型 2 :计算型 |
| 8 | fsituationtype | 情景类型 | bpchar | 1 |  | √ | '0' | 情景类型,枚举: 0 :实际数 1 :预算数 |
| 9 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 10 | fmeasureid | 计算度量 | int8 | 64 |  | √ | 0 | 度量 pa_measure |
| 11 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 12 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 13 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 14 | fdimensionattr | 聚合属性设置 | varchar | 255 |  | √ | ' ' | 聚合属性设置 |
| 15 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 16 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 17 | fsystemid | 分析体系 | int8 | 64 |  | √ | 0 | 分析体系 pa_anasystemsetting |
| 18 | faggregationtype | 聚合方式 | bpchar | 1 |  | √ | ' ' | 聚合方式,枚举: 1 :求和 |
| 19 | fisdefault | 是否默认预置 | bpchar | 1 |  | √ | '0' | 是否默认预置 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_measure_nbsys |  | fnumber,fsystemid |
| 2 | idx_pa_measure |  | fsystemid |
| 3 | pk_t_pa_measure |  | fid |
