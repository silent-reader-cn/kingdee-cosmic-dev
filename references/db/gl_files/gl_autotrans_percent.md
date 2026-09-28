# 转账比例公式-gl_autotrans_percent

## 转账比例公式-主表 t_gl_percent

- **表名称：** 转账比例公式-主表
- **表名：** t_gl_percent

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | forgid | 核算组织 | int8 | 64 |  | √ | 0 | [业务单元 bos_org](../base_files/bos_org.md) |
| 3 | faccountbookid | 账簿 | int8 | 64 |  | √ | 0 | [账簿 gl_accountbook](../gl_files/gl_accountbook.md) |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_percent |  | forgid |
| 2 | t_gl_percent_pkey |  | fid |

---

## 单据体-子表 t_gl_percententry

- **表名称：** 单据体-子表
- **表名：** t_gl_percententry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fsign | 运算符号 | varchar | 2 |  | √ | '1' | 运算符号,枚举: + :+ - :- * :* / :/ 1 : |
| 3 | fvalue | 金额 | varchar | 2 |  | √ | ' ' | 金额,枚举: 0 :期初余额 1 :期末余额 2 :本期借方发生额 3 :本期贷方发生额 4 :本年累计借方发生额 5 :本年累计贷方发生额 6 :本期实际损益借方发生额 7 :本期实际损益贷方发生额 8 :本年实际损益借方发生额 9 :本年实际损益贷方发生额 |
| 4 | fleftbracket | 左括号 | varchar | 5 |  | √ | '1' | 左括号,枚举: 1 : ( :( (( :(( ((( :((( |
| 5 | frightbracket | 右括号 | varchar | 5 |  | √ | '1' | 右括号,枚举: 1 : ) :) )) :)) ))) :))) |
| 6 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | null 002 |
| 7 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 8 | faccoutid | 会计科目 | int8 | 64 |  | √ | 0 | 会计科目 bd_accountview |
| 9 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |
| 10 | fcurrencyid | 币种 | int8 | 64 |  | √ | 0 | [币种 bd_currency](../base_files/bd_currency.md) |
| 11 | fdefval | 固定值 | numeric | 23 | 10 | √ | 0.0000000000 | 固定值 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | idx_gl_percententry |  | fid |
| 2 | t_gl_percententry_pkey |  | fentryid |
