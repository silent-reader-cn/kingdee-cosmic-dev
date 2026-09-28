# 损益报表定义-pa_income_define

## 损益报表定义-多语言表 t_pa_incomedefine_l

- **表名称：** 损益报表定义-多语言表
- **表名：** t_pa_incomedefine_l

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
| 1 | pk_t_pa_incomedefine_l |  | fpkid |
| 2 | idx_pa_incomedefine_l |  | fid |

---

## 列维度分录-子表 t_pa_incomedefinecol

- **表名称：** 列维度分录-子表
- **表名：** t_pa_incomedefinecol

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fdimnumber | 维度编码 | varchar | 50 |  | √ | ' ' | 维度编码 |
| 3 | fcoldimension | 维度 | int8 | 64 |  | √ | 0 | 维度 pa_dimension |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fdimname | 维度名称 | varchar | 100 |  | √ | ' ' | 维度名称 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_incomedifinecol |  | fid |
| 2 | pk_t_pa_incomedefinecol |  | fentryid |

---

## 损益报表定义-主表 t_pa_incomedefine

- **表名称：** 损益报表定义-主表
- **表名：** t_pa_incomedefine

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 4 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 5 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |
| 6 | fstatus | 数据状态 | bpchar | 1 |  | √ | 'C' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 7 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 8 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 9 | fanalysissystem | 体系 | int8 | 64 |  | √ | 0 | 分析体系 pa_anasystemsetting |
| 10 | fenable | 使用状态 | bpchar | 1 |  | √ | '1' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 50 |  | √ | ' ' | 编码 |
| 12 | fanalysismodel | 模型 | int8 | 64 |  | √ | 0 | 分析模型 pa_analysismodel |
| 13 | fmeasure | 度量 | int8 | 64 |  | √ | 0 | 度量 pa_measure |
| 14 | fdimension | 维度 | int8 | 64 |  | √ | 0 | 维度 pa_dimension |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_incomedefine_1 |  | fnumber,fname |
| 2 | idx_pa_incomedefine_2 |  | fname |
| 3 | pk_t_pa_incomedefine |  | fid |

---

## 行维度分录-子表 t_pa_incomedefinerow

- **表名称：** 行维度分录-子表
- **表名：** t_pa_incomedefinerow

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fintegerfield | 展示缩进 | int4 | 32 |  | √ | 0 | 展示缩进 |
| 3 | fcalculationrule | 计算规则 | varchar | 255 |  | √ | ' ' | 计算规则 |
| 4 | fcalculationrule_tag | 计算规则_详情 | text | 0 |  |  | null | 计算规则_详情 |
| 5 | fcalculationdesc_tag | 计算规则_详情 | text | 0 |  |  | null | 计算规则_详情 |
| 6 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 7 | freportitem | 报表项目 | varchar | 50 |  | √ | ' ' | 报表项目 |
| 8 | fcalculationdesc | 计算规则 | varchar | 255 |  | √ | ' ' | 计算规则 |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fdseq | 顺序 | int4 | 32 |  | √ | 0 | 顺序 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_pa_incomedefinerow |  | fid |
| 2 | pk_t_pa_incomedefinerow |  | fentryid |
