# 费用单据实体类型设置-er_entitytype_setting

## 单据体-子表 t_er_entitytypeentry

- **表名称：** 单据体-子表
- **表名：** t_er_entitytypeentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 3 | fentitytype | 单据类型 | varchar | 255 |  | √ | ' ' | 单据类型,枚举: DAILYREIMBURSEBILL :费用报销单 PUBLICREIMBURSEBILL :对公报销单 DAILYAPPLYBILL :费用申请单 DAILYLOANBILL :借款单 TRIPREQBILL :出差申请单 TRIPREIMBURSEBILL :差旅报销单 REPAYMENTBILL :还款单 EXPENSERECORDBILL :费用记录 TRIPRECORDBILL :差旅记录 EXPENSESHAREBILL :费用分摊单 |
| 4 | fentityid | entityid | varchar | 255 |  | √ | ' ' | entityid |
| 5 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_er_typeset_fid |  | fid |
| 2 | t_er_entitytypeentry_pkey |  | fentryid |

---

## 费用单据实体类型设置-多语言表 t_er_entitytype_l

- **表名称：** 费用单据实体类型设置-多语言表
- **表名：** t_er_entitytype_l

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fname | 名称 | varchar | 100 |  | √ | ' ' | 名称 |
| 3 | flocaleid | flocaleid | varchar | 10 |  | √ | ' ' | localeid |
| 4 | fpkid | fpkid | varchar | 30 |  | √ | ' ' | pkid |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fpkid | fpkid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_typesetting_id_flcaleid |  | fid,flocaleid |
| 2 | pk_t_er_entitytype_l |  | fpkid |

---

## 费用单据实体类型设置-主表 t_er_entitytype

- **表名称：** 费用单据实体类型设置-主表
- **表名：** t_er_entitytype

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fcreateorgid | fcreateorgid | int8 | 64 |  | √ | 0 |  |
| 3 | fstatus | 数据状态 | varchar | 30 |  | √ | ' ' | 数据状态,枚举: A :暂存 B :已提交 C :已审核 |
| 4 | fmasterid | 主数据内码 | int8 | 64 |  | √ | 0 | 主数据内码 |
| 5 | fenable | 使用状态 | varchar | 30 |  | √ | ' ' | 使用状态,枚举: 0 :禁用 1 :可用 |
| 6 | fnumber | 编码 | varchar | 30 |  | √ | ' ' | 编码 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_er_entitytype_pkey |  | fid |
| 2 | idx_er_entity_number |  | fnumber |
