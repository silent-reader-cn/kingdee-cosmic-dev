# 财务健康度评价模型类型-dfa_health_evaluate_type

## 财务健康度评价模型类型-主表 t_dfa_health_evaluatetype

- **表名称：** 财务健康度评价模型类型-主表
- **表名：** t_dfa_health_evaluatetype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 模型名称 | varchar | 50 |  | √ | ' ' | 模型名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 5 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | [人员 bos_user](../base_files/bos_user.md) |
| 6 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 7 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 8 | fpreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 9 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 10 | frelative_report_type | 关联报表类型 | varchar | 50 |  | √ | ' ' | 关联报表类型,枚举: REPORT :报表 CONSOLIDATED_REPORT :合并报表 |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_health_evaluatetype |  | fid |
| 2 | idx_dfa_health_evaluatetype |  | fnumber |

---

## 财务健康度评价模型类型-多语言表 t_dfa_health_evaluatetype_l

- **表名称：** 财务健康度评价模型类型-多语言表
- **表名：** t_dfa_health_evaluatetype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 模型名称 | varchar | 50 |  | √ | ' ' | 模型名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 36 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_health_evaluatetype_l |  | fpkid |
| 2 | idx_dfa_health_evaluate_l |  | fid |

---

## 能力项权重信息-子表 t_dfa_health_evaluate_cap

- **表名称：** 能力项权重信息-子表
- **表名：** t_dfa_health_evaluate_cap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fquotatypeweigh | 能力项权重 | numeric | 23 | 10 |  | null | 能力项权重 |
| 3 | fcapacity_type | 能力类型 | varchar | 50 |  | √ | ' ' | 能力类型,枚举: 0 :现金流 1 :偿债能力 2 :成长能力 3 :盈利能力 4 :营运能力 5 :资产质量 |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_dfa_health_evaluate_cap |  | fentryid |
| 2 | idx_dfa_health_evaluate_cap_fk |  | fid |
