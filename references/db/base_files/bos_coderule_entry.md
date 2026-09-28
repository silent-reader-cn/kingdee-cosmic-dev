# 编码规则分录-bos_coderule_entry

## 编码规则分录-主表 t_cr_coderuleentry

- **表名称：** 编码规则分录-主表
- **表名：** t_cr_coderuleentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | 编码规则id | varchar | 36 |  | √ | ' ' | [编码规则 bos_coderule](../base_files/bos_coderule.md) |
| 2 | fisvisable | 是否显示 | bpchar | 1 |  | √ | ' ' | 是否显示 |
| 3 | fstep | 步长 | int8 | 64 |  | √ | 0 | 步长 |
| 4 | faddstyle | 补位 | bpchar | 1 |  | √ | ' ' | 补位 |
| 5 | flength | 长度 | int8 | 64 |  | √ | 0 | 长度 |
| 6 | fformat | 格式 | varchar | 100 |  | √ | ' ' | 格式 |
| 7 | finitial | 初始值 | int8 | 64 |  | √ | 0 | 初始值 |
| 8 | fseq | 序号 | int8 | 64 |  | √ | 0 | 序号 |
| 9 | fattusingmode | 适用模式 | varchar | 10 |  | √ | ' ' | 适用模式 |
| 10 | fissortitem | 流水号依据 | bpchar | 1 |  | √ | '1' | 流水号依据 |
| 11 | fsettingvalue | 设置值 | varchar | 20 |  | √ | ' ' | 设置值 |
| 12 | faddchar | 补位符号 | varchar | 1 |  | √ | ' ' | 补位符号 |
| 13 | fvalueatribute | 编码来源 | varchar | 50 |  | √ | ' ' | 编码来源 |
| 14 | fcutstyle | 截取 | bpchar | 1 |  | √ | ' ' | 截取 |
| 15 | fsplitsign | 段间分隔符 | bpchar | 1 |  | √ | '-' | 段间分隔符,枚举: - :- @ :@ # :# $ :$ % :% ^ :^ & :& * :* |
| 16 | fentryid | fentryid | varchar | 36 |  | √ | ' ' | id |
| 17 | fattributetype | 属性类型 | varchar | 10 |  | √ | ' ' | 属性类型 |
| 18 | fissplitsign | 段间分隔 | bpchar | 1 |  | √ | '1' | 段间分隔 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_t_cr_coderuleentry_fid |  | fid |
| 2 | t_cr_coderuleentry_pkey |  | fentryid |
