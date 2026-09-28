# 自动转账Excel取数设置-gl_autotransexcelseting

## 自动转账Excel取数设置-主表 t_gl_autotransexcel

- **表名称：** 自动转账Excel取数设置-主表
- **表名：** t_gl_autotransexcel

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 | id |
| 2 | fautorowid | 行id | varchar | 50 |  | √ | ' ' | 行id |
| 3 | ffilepath | 文件路径 | varchar | 200 |  | √ | ' ' | 文件路径 |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fid | fid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_autotransexcel_pkey |  | fid |
| 2 | idx_gl_autotransexcel_row |  | fautorowid |

---

## 单据体-子表 t_gl_autotransexcelentry

- **表名称：** 单据体-子表
- **表名：** t_gl_autotransexcelentry

### 表格列定义

| 序号 | 列标题 | 列名称 | 类型 | 长度 | 精度 | 非空 | 默认值 | 备注 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | fid | fid | int8 | 64 |  | √ | 0 |  |
| 2 | fassgrpid | 核算维度 | int8 | 64 |  | √ | 0 | 核算维度 bd_asstacttype |
| 3 | fpage | 页签 | int8 | 64 |  | √ | 0 | 页签 |
| 4 | fseq | 分录行号 | int8 | 64 |  | √ | 0 | 分录行号 |
| 5 | fposition | 位置 | varchar | 50 |  | √ | ' ' | 位置 |
| 6 | fentryid | fentryid | int8 | 64 |  | √ | 0 | id |

### 列规则定义

| 序号 | 键编码 | 列字段 |
| :--- | :--- | :--- |
| 1 | fentryid | fentryid |

### 索引定义

| 序号 | 索引名 | 唯一 | 列字段 |
| :--- | :--- | :--- | :--- |
| 1 | t_gl_autotransexcelentry_pkey |  | fentryid |
| 2 | idx_gl_autotransexcelentry |  | fid |
