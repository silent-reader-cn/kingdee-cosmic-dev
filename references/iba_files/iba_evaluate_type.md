# 财务评价模型类型-iba_evaluate_type

## 适用组织-多选基础资料表 t_iba_evaluate_type_orgs

- **表名称：** 适用组织-多选基础资料表
- **表名：** t_iba_evaluate_type_orgs

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fbasedataid | fbasedataid | int8 | 64 |  | √ | 0 | IPO编制组织 ipo_org |
| 3 | fpkid | fpkid | int8 | 64 |  | √ | 0 | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_t_iba_evaluate_type_orgs |  | fpkid |
| 2 | idx_iba_evaluate_type_orgs |  | fid |

---

## 财务评价模型类型-主表 t_iba_evaluate_type

- **表名称：** 财务评价模型类型-主表
- **表名：** t_iba_evaluate_type

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fname | 模型名称 | varchar | 50 |  | √ | ' ' | 模型名称 |
| 3 | fstatus | 数据状态 | varchar | 50 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmodifierid | 修改人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 5 | frelativetheme | 关联主题 | varchar | 50 |  | √ | ' ' | 关联主题,枚举: 0 :行业对标分析 1 :公司财务分析 |
| 6 | fcreatorid | 创建人 | int8 | 64 |  | √ | 0 | 人员 bos_user |
| 7 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 8 | fcreatetime | 创建时间 | timestamp | 0 |  |  | null | 创建时间 |
| 9 | fpreset | 是否预设 | bpchar | 1 |  | √ | '0' | 是否预设 |
| 10 | fenable | 使用状态 | varchar | 50 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 11 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |
| 12 | fmodifytime | 修改时间 | timestamp | 0 |  |  | null | 修改时间 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | pk_iba_evaluate_type |  | fid |
| 2 | idx_iba_evaluate_type_name |  | fname |
| 3 | idx_iba_evaluate_type_number |  | fnumber |

---

## 财务评价模型类型-多语言表 t_iba_evaluate_type_l

- **表名称：** 财务评价模型类型-多语言表
- **表名：** t_iba_evaluate_type_l

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
| 1 | idx_iba_evaluate_type_id |  | fid |
| 2 | pk_iba_evaluate_type_l |  | fpkid |

---

## 能力项权重信息-子表 t_iba_evaluate_weigh_cap

- **表名称：** 能力项权重信息-子表
- **表名：** t_iba_evaluate_weigh_cap

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fquotatypeweigh | 能力项权重 | numeric | 23 | 10 |  | null | 能力项权重 |
| 3 | fquotatype | 能力项 | int8 | 64 |  | √ | 0 | 指标分类目录 ipo_quota_type |
| 4 | fseq | 分录行号 | int4 | 32 |  | √ | 0 | 分录行号 |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_iba_evaluate_weigh_cap_id |  | fid |
| 2 | pk_iba_evaluate_weigh_cap |  | fentryid |
